#!/usr/bin/env python3
"""
cascade_dates.py

When a PR is merged in the includes repo, this script:
  1. Reads the list of changed include files (passed via CHANGED_FILES env var)
  2. For each downstream repo, finds all topic files that reference those includes
     via the [!INCLUDE [...](path/to/file.md)] syntax
  3. Updates ms.date in those topics to today's date
  4. Creates a branch and opens a PR in each downstream repo

Required environment variables:
  GITHUB_TOKEN   - PAT with repo scope (stored as CASCADE_PAT secret)
  CHANGED_FILES  - space-separated list of changed file paths (set by workflow)
  PR_NUMBER      - source PR number (set by workflow)
  PR_URL         - source PR URL (set by workflow)
"""

import json
import os
import re
import subprocess
import sys
import tempfile
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path


def load_config() -> dict:
    config_path = Path(__file__).parent / "cascade-config.json"
    with open(config_path, encoding="utf-8") as f:
        return json.load(f)


def get_changed_include_files(includes_path: str) -> list[str]:
    """Filter CHANGED_FILES env var to only include files in the includes path."""
    changed_raw = os.environ.get("CHANGED_FILES", "").strip()
    if not changed_raw:
        print("CHANGED_FILES is empty — nothing to process.")
        return []

    changed = changed_raw.split()
    include_files = [
        f for f in changed
        if f.startswith(includes_path) and f.endswith(".md")
    ]

    if include_files:
        print(f"Changed include files ({len(include_files)}):")
        for f in include_files:
            print(f"  {f}")
    else:
        print(f"No .md files changed under '{includes_path}'.")

    return include_files


def run(args: list[str], cwd: str = None, check: bool = True) -> subprocess.CompletedProcess:
    result = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
    if check and result.returncode != 0:
        raise RuntimeError(
            f"Command failed: {' '.join(args)}\n"
            f"stdout: {result.stdout}\n"
            f"stderr: {result.stderr}"
        )
    return result


def clone_repo(repo: str, dest: str, branch: str, token: str):
    """Shallow-clone a repo using the PAT for authentication."""
    url = f"https://x-access-token:{token}@github.com/{repo}.git"
    print(f"  Cloning {repo} (branch: {branch})...")
    run(["git", "clone", "--depth=1", "--branch", branch, url, dest])


def find_referencing_topics(
    repo_dir: str,
    include_paths: list[str],
    scope_path: str = "",
) -> dict[str, list[str]]:
    """
    Walk the repo (or a scoped subdirectory) and find all .md topic files that
    reference any of the changed include files via [!INCLUDE [...](...)].

    scope_path: optional subdirectory relative to repo_dir to restrict the search.
    Returns {path_relative_to_repo_dir: [matched_include_paths]}.
    Skips files inside 'includes' or 'shared' directories.
    """
    results: dict[str, list[str]] = {}
    repo_path = Path(repo_dir)
    search_root = repo_path / scope_path if scope_path else repo_path

    patterns = {
        inc: re.compile(
            r'\[!INCLUDE\s*\[[^\]]*\]\([^)]*' + re.escape(inc) + r'[^)]*\)',
            re.IGNORECASE,
        )
        for inc in include_paths
    }

    for md_file in sorted(search_root.rglob("*.md")):
        # Skip include/shared source directories
        parts = {p.lower() for p in md_file.relative_to(repo_path).parts[:-1]}
        if parts & {"includes", "shared"}:
            continue

        try:
            content = md_file.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            print(f"    Warning: cannot read {md_file}: {e}")
            continue

        matched = [inc for inc, pat in patterns.items() if pat.search(content)]
        if matched:
            rel = str(md_file.relative_to(repo_path))
            results[rel] = matched

    return results


def update_ms_date(file_path: str, new_date: str) -> bool:
    """
    Replace the ms.date value in a file's YAML frontmatter.
    Returns True if the field was found and updated.
    """
    path = Path(file_path)
    content = path.read_text(encoding="utf-8", errors="replace")

    new_content, count = re.subn(
        r'^(ms\.date\s*:\s*)\S+',
        lambda m: m.group(1) + new_date,
        content,
        flags=re.MULTILINE,
    )

    if count == 0:
        return False

    path.write_text(new_content, encoding="utf-8")
    return True


def pr_already_exists(repo: str, branch: str, token: str) -> bool:
    """Return True if a PR from this branch already exists in the repo."""
    result = subprocess.run(
        ["gh", "pr", "list", "--repo", repo, "--head", branch, "--json", "number"],
        capture_output=True,
        text=True,
        env={**os.environ, "GH_TOKEN": token},
    )
    if result.returncode != 0:
        return False
    try:
        return len(json.loads(result.stdout)) > 0
    except json.JSONDecodeError:
        return False


def create_pr(
    repo_dir: str,
    repo: str,
    branch: str,
    updated_files: list[str],
    title: str,
    body: str,
    base: str,
    labels: list[str],
    token: str,
    reviewer: str = "",
) -> str | None:
    """Commit changes, push the branch, and open a PR. Returns the PR URL."""
    env = {**os.environ, "GH_TOKEN": token}

    # Configure git identity for the bot commit (idempotent)
    run(["git", "config", "user.email", "github-actions[bot]@users.noreply.github.com"], cwd=repo_dir)
    run(["git", "config", "user.name", "github-actions[bot]"], cwd=repo_dir)

    # Always branch from the base so multiple docset PRs start from a clean state
    run(["git", "checkout", base], cwd=repo_dir)
    run(["git", "checkout", "-b", branch], cwd=repo_dir)

    for f in updated_files:
        run(["git", "add", f], cwd=repo_dir)

    run(["git", "commit", "-m", title], cwd=repo_dir)
    run(["git", "push", "origin", branch], cwd=repo_dir)

    gh_cmd = [
        "gh", "pr", "create",
        "--repo", repo,
        "--title", title,
        "--body", body,
        "--base", base,
        "--head", branch,
    ]
    if labels:
        gh_cmd += ["--label", ",".join(labels)]
    if reviewer:
        gh_cmd += ["--reviewer", reviewer]

    result = subprocess.run(gh_cmd, cwd=repo_dir, capture_output=True, text=True, env=env)
    if result.returncode != 0 and "not found" in result.stderr:
        # Strip optional flags that may fail due to missing repo members/labels,
        # then retry. Each flag is a two-element pair (--flag value) in gh_cmd.
        retried = False
        cmd = gh_cmd[:]
        for flag in ("--label", "--reviewer"):
            if flag in cmd:
                idx = cmd.index(flag)
                cmd = cmd[:idx] + cmd[idx + 2:]
                retried = True
        if retried:
            print("    Warning: reviewer or label not found in repo, retrying without them...")
            result = subprocess.run(cmd, cwd=repo_dir, capture_output=True, text=True, env=env)

    if result.returncode != 0:
        print(f"    Warning: gh pr create failed:\n{result.stderr}")
        return None

    return result.stdout.strip()


def get_include_diff(pr_number: str, source_repo: str, token: str) -> str:
    """Fetch the diff of the source PR. Returns the diff text or empty string on failure."""
    if not pr_number or pr_number.startswith("test"):
        return ""
    try:
        result = subprocess.run(
            ["gh", "pr", "diff", pr_number, "--repo", source_repo],
            capture_output=True, text=True,
            env={**os.environ, "GH_TOKEN": token},
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
        print(f"  Note: could not fetch diff for PR #{pr_number}: {result.stderr.strip()}")
    except Exception as exc:
        print(f"  Note: could not fetch diff: {exc}")
    return ""


def generate_smart_description(
    diff_text: str,
    include_files: list[str],
    token: str,
) -> str:
    """
    Call GitHub Models (GPT-4o-mini) to generate a summary and warnings from the include diff.
    Returns formatted markdown to prepend to the PR body, or empty string on failure.
    """
    if not diff_text or not token:
        return ""

    file_list = "\n".join(f"- {f}" for f in include_files)
    prompt = (
        "An include file used across multiple documentation topics was just updated.\n\n"
        f"Changed files:\n{file_list}\n\n"
        f"Diff:\n```\n{diff_text[:8000]}\n```\n\n"
        "Write a short section for a PR description with exactly two parts:\n"
        "1. A one or two sentence summary of what changed (be specific and practical).\n"
        "2. A bulleted list of warnings the writer should check in their topic, "
        "ONLY if relevant. Examples: product name changes, version number updates, "
        "deprecated features, changed URLs, significant content removed. "
        "If nothing warrants a warning, omit the warnings section entirely.\n\n"
        "Format your response as:\n"
        "SUMMARY: <your summary>\n"
        "WARNINGS:\n- <warning 1>\n- <warning 2>\n\n"
        "If there are no warnings, just output:\n"
        "SUMMARY: <your summary>"
    )

    url = "https://models.inference.ai.azure.com/chat/completions"
    payload = json.dumps({
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a technical writing assistant that analyzes diffs of shared documentation include files. Be concise and practical."},
            {"role": "user", "content": prompt},
        ],
        "max_tokens": 512,
        "temperature": 0.3,
    }).encode("utf-8")

    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = json.loads(resp.read().decode("utf-8"))
        raw = body["choices"][0]["message"]["content"].strip()
    except Exception as exc:
        print(f"  Note: smart description skipped (API call failed: {exc})")
        return ""

    # Parse the structured response into markdown
    lines = raw.split("\n")
    summary = ""
    warnings: list[str] = []
    in_warnings = False

    for line in lines:
        if line.startswith("SUMMARY:"):
            summary = line[len("SUMMARY:"):].strip()
        elif line.strip() == "WARNINGS:":
            in_warnings = True
        elif in_warnings and line.strip().startswith("-"):
            warnings.append(line.strip())

    if not summary:
        # LLM didn't follow the format — use raw text as summary
        summary = raw.split("\n")[0]

    heading = "## What changed in the include files" if len(include_files) > 1 else "## What changed in the include file"
    result = f"{heading}\n\n{summary}\n"
    if warnings:
        result += "\n⚠️ **Things to check in your topic:**\n"
        result += "\n".join(warnings) + "\n"
    result += "\n*This summary was generated by AI. Review the source PR for full details.*\n"
    result += "\n---\n\n"
    return result


def main():
    config = load_config()

    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("CASCADE_PAT")
    if not token:
        print("Error: GITHUB_TOKEN or CASCADE_PAT environment variable is required.")
        sys.exit(1)

    pr_number = os.environ.get("PR_NUMBER", "unknown")
    pr_url    = os.environ.get("PR_URL", "")

    includes_path   = config["includes_path"]
    downstream_repos = config["downstream_repos"]
    base_branch     = config["base_branch"]
    date_format     = config.get("date_format", "%m/%d/%Y")
    labels          = config.get("pr_labels", [])
    title_prefix    = config.get("pr_title_prefix", "chore: cascade date update")

    include_files = get_changed_include_files(includes_path)
    if not include_files:
        print("Nothing to cascade.")
        sys.exit(0)

    # Use the full relative path (e.g. "shared/dynamics365-core/file.md") so
    # the regex matches the invariant segment that always appears in references,
    # regardless of how many "../" prefixes the topic uses.
    include_paths = include_files  # already relative paths from repo root
    today = datetime.now(timezone.utc).strftime(date_format)
    source_repo = config.get("source_repo", "")
    pr_title_full = f"{title_prefix} (source PR #{pr_number})"

    def include_link(f: str) -> str:
        if source_repo:
            url = f"https://github.com/{source_repo}/blob/{base_branch}/{f}"
            return f"- [{f}]({url})\n"
        return f"- `{f}`\n"

    source_pr_line = (
        f"**Source PR:** [#{pr_number}]({pr_url})\n\n" if pr_url
        else f"**Source PR:** [#{pr_number}](https://github.com/{source_repo}/pull/{pr_number})\n\n" if source_repo and pr_number.isdigit()
        else f"**Source PR:** #{pr_number}\n\n"
    )

    pr_body = (
        "## Cascading include file changes\n\n"
        "This PR updates `ms.date` in all topics that reference the changed include(s) "
        "to force a rebuild, ensuring the latest include content is pulled in and the "
        "topic dates accurately reflect this update.\n\n"
        + source_pr_line
        + "**Changed include files:**\n"
        + "".join(include_link(f) for f in include_files) 
        + f"\nTopics referencing these files now have `ms.date` set to `{today}`.\n\n"
        "Please approve and merge to update content on Learn.\n\n"
        "---\n*Generated by cascade-include-changes workflow*"
    )

    # --- Smart description (optional, uses GitHub Models API) ---
    smart_desc_enabled = config.get("smart_descriptions", False)

    diff_text = get_include_diff(pr_number, source_repo, token) if smart_desc_enabled else ""
    smart_desc = generate_smart_description(diff_text, include_files, token)
    if smart_desc:
        pr_body = smart_desc + pr_body
        print("Smart description generated successfully.")
    elif smart_desc_enabled:
        print("Smart description skipped (no diff or API issue). Using static description.")

    summary: list[dict] = []

    with tempfile.TemporaryDirectory() as tmpdir:
        for repo_entry in downstream_repos:
            if isinstance(repo_entry, dict):
                repo = repo_entry["repo"]
                docsets = repo_entry.get("docsets")
                top_reviewer = repo_entry.get("reviewer", "")
            else:
                repo = repo_entry
                docsets = None
                top_reviewer = ""

            # Normalize to a flat list of units: each unit is one PR.
            # Repos without docsets produce a single unit covering the whole repo.
            if docsets:
                units = [
                    {
                        "scope": d["path"],
                        "reviewer": d.get("reviewer", ""),
                        "branch": f"cascade/include-changes-pr-{pr_number}-{d['path'].replace('/', '-')}",
                        "title": f"{title_prefix} — {d['path']} (source PR #{pr_number})",
                    }
                    for d in docsets
                ]
            else:
                units = [
                    {
                        "scope": "",
                        "reviewer": top_reviewer,
                        "branch": f"cascade/include-changes-pr-{pr_number}",
                        "title": pr_title_full,
                    }
                ]

            print(f"\n{'='*60}")
            print(f"Repo: {repo}")
            repo_dir = os.path.join(tmpdir, repo.replace("/", "__"))

            try:
                clone_repo(repo, repo_dir, base_branch, token)
            except Exception as exc:
                print(f"  Error cloning: {exc}")
                for unit in units:
                    summary.append({"repo": repo, "scope": unit["scope"], "status": f"error cloning: {exc}"})
                continue

            for unit in units:
                scope      = unit["scope"]
                reviewer   = unit["reviewer"]
                branch     = unit["branch"]
                unit_title = unit["title"]

                if scope:
                    print(f"\n  Docset: {scope}")

                try:
                    if pr_already_exists(repo, branch, token):
                        print(f"  PR already open for branch '{branch}' — skipping.")
                        summary.append({"repo": repo, "scope": scope, "status": "skipped (PR exists)"})
                        continue

                    topic_map = find_referencing_topics(repo_dir, include_paths, scope)

                    if not topic_map:
                        print("  No topics reference the changed includes.")
                        summary.append({"repo": repo, "scope": scope, "status": "no matching topics"})
                        continue

                    print(f"  Found {len(topic_map)} topic(s) to update:")
                    updated: list[str] = []
                    for topic_path, refs in topic_map.items():
                        full_path = os.path.join(repo_dir, topic_path)
                        if update_ms_date(full_path, today):
                            print(f"    [updated] {topic_path}  (refs: {', '.join(refs)})")
                            updated.append(topic_path)
                        else:
                            print(f"    [skipped] {topic_path}  (no ms.date field)")

                    if not updated:
                        print("  No files had an ms.date field — nothing to commit.")
                        summary.append({"repo": repo, "scope": scope, "status": "no ms.date fields found"})
                        continue

                    pr_link = create_pr(
                        repo_dir=repo_dir,
                        repo=repo,
                        branch=branch,
                        updated_files=updated,
                        title=unit_title,
                        body=pr_body,
                        base=base_branch,
                        labels=labels,
                        token=token,
                        reviewer=reviewer,
                    )

                    summary.append({
                        "repo": repo,
                        "scope": scope,
                        "status": "PR created" if pr_link else "PR creation failed",
                        "pr_url": pr_link,
                        "updated": updated,
                    })

                except Exception as exc:
                    print(f"  Error: {exc}")
                    summary.append({"repo": repo, "scope": scope, "status": f"error: {exc}"})

    # Final summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    for item in summary:
        label = f"{item['repo']}" + (f" ({item['scope']})" if item.get("scope") else "")
        print(f"  {label}: {item['status']}")
        if item.get("pr_url"):
            print(f"    -> {item['pr_url']}")
        for f in item.get("updated", []):
            print(f"       {f}")

    # Write markdown summary for PR comment and GitHub Actions step summary
    write_summary_markdown(summary, include_files, pr_number, source_repo)


def write_summary_markdown(
    summary: list[dict],
    include_files: list[str],
    pr_number: str,
    source_repo: str,
) -> None:
    """Write a markdown summary file for use as a PR comment and Actions step summary."""
    created = [item for item in summary if item.get("pr_url")]
    skipped = [item for item in summary if "skipped" in item.get("status", "")]
    no_match = [item for item in summary if "no matching" in item.get("status", "") or "no ms.date" in item.get("status", "")]
    errors = [item for item in summary if "error" in item.get("status", "")]

    lines: list[str] = []
    lines.append("## 🔄 Cascade include changes — summary\n")

    if created:
        lines.append(f"**{len(created)} PR(s) created:**\n")
        lines.append("| Repo | Scope | PR | Files updated |")
        lines.append("|---|---|---|---|")
        for item in created:
            repo = item["repo"]
            scope = item.get("scope", "")
            pr_url = item["pr_url"]
            file_count = len(item.get("updated", []))
            scope_display = f"`{scope}`" if scope else "—"
            lines.append(f"| {repo} | {scope_display} | [Open]({pr_url}) | {file_count} |")
        lines.append("")

    if skipped:
        lines.append(f"**Skipped** (PR already exists): {', '.join(s['repo'] for s in skipped)}\n")

    if no_match:
        labels = [f"{item['repo']}" + (f" ({item['scope']})" if item.get('scope') else "") for item in no_match]
        lines.append(f"**No matching topics:** {', '.join(labels)}\n")

    if errors:
        lines.append("**⚠️ Errors:**\n")
        for item in errors:
            lines.append(f"- {item['repo']}: {item['status']}")
        lines.append("")

    lines.append(f"**Changed includes:** {', '.join(f'`{f}`' for f in include_files)}\n")
    lines.append(f"cc @nathlaroche")

    md = "\n".join(lines)

    # Write to file for the workflow PR comment step
    summary_path = Path(os.environ.get("GITHUB_WORKSPACE", ".")) / "cascade-summary.md"
    summary_path.write_text(md, encoding="utf-8")
    print(f"\nSummary written to {summary_path}")

    # Also write to GITHUB_STEP_SUMMARY if available (shows in Actions UI)
    step_summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if step_summary_path:
        with open(step_summary_path, "a", encoding="utf-8") as f:
            f.write(md + "\n")


if __name__ == "__main__":
    main()
