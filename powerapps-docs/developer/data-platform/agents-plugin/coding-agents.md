---
title: Use the Dataverse Plugin with AI Coding Agents (Preview)
description: Install the Microsoft Dataverse plugin in your coding agent, connect to Dataverse, and choose tools for development and administration.
#customer intent: As a developer using an AI coding agent, I want to install and connect the Dataverse plugin so that I can work with my environment.
ms.date: 11/11/2026
ms.reviewer: jdaly
ms.topic: how-to
author: kewear
ms.author: kewear
ms.collection: bap-ai-copilot
search.audienceType:
  - developer
contributors:
 - JimDaly
 - suyask-msft
ai-usage: ai-assisted
---
# Use the Dataverse plugin with AI coding agents (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

Use the Microsoft Dataverse plugin in your coding agent to build, query, and manage Dataverse solutions.

[!INCLUDE [preview-note-business-applications-work-iq](~/../shared-content/shared/preview-includes/preview-note-business-applications-work-iq.md)]

For an overview of the plugin and its development workflows, see [Microsoft Dataverse plugin for AI agents](index.md).

## Prerequisites

You need:

- A Dataverse environment available through Power Apps, Dynamics 365, or another applicable Power Platform plan. For a nonproduction environment, use a sandbox or managed developer environment.
- A user account with access to the environment and the privileges required for the operations you request.
- A supported agent: GitHub Copilot, Claude Code, Cursor, OpenAI Codex and ChatGPT, Gemini CLI, or Google Antigravity. Any other agent that reads local skills can also use them.
- Permission to install or run any required local tools.

The [`dv-connect`](reference.md#dv-connect) skill checks the local toolchain and guides installation or configuration when needed. Depending on the requested operations, the toolchain can include Git, Node.js, Python 3, .NET SDK, Azure CLI, Power Platform CLI, the Dataverse CLI, and the Dataverse SDK for Python.

Dataverse MCP access also requires tenant administrator consent and per-environment client allowlisting. The connection flow identifies these requirements and provides the appropriate instructions, but doesn't bypass administrator approval. See [Coding-agent authentication and authorization](security-governance.md#coding-agent-authentication-and-authorization).

## Install the plugin

Install the plugin for your coding agent.

- [GitHub Copilot](#github-copilot)
- [Claude Code](#claude-code)
- [Cursor](#cursor)
- [Codex](#codex)
- [Gemini CLI](#gemini-cli)
- [Google Antigravity](#google-antigravity)
- [Other agents](#other-agents)

### GitHub Copilot

```text
/plugin install dataverse@awesome-copilot
```

### Claude Code

```text
/plugin install dataverse@claude-plugins-official
```

You can also run `/plugin`, open **Discover**, and search for **dataverse**.

### Cursor

In agent chat, enter:

```text
/add-plugin dataverse
```

Alternatively, in Cursor, go to **Settings** > **Plugins**, search for **Dataverse**, open **Microsoft Dataverse**, and select **Add to Cursor**.

### Codex

In the Codex app:

1. Open **Plugins** > **Add marketplace**.
2. For **Source**, enter `https://github.com/microsoft/Dataverse-skills.git`.
3. Leave **Git ref** and **Sparse paths** empty, and then add the marketplace.
4. Open the **dataverse-skills** marketplace and install the `dataverse` plugin.

For the Codex CLI, add the marketplace:

```console
codex plugin marketplace add microsoft/Dataverse-skills
```

Then open `/plugins` and install `dataverse`.

You can also search for **Microsoft Dataverse** in the OpenAI plugin directory in Codex or ChatGPT, or run this command in the Codex CLI:

```console
codex plugin add dataverse@openai-curated
```

### Gemini CLI

Install the extension and configure your Dataverse environment URL:

```console
gemini extensions install https://github.com/microsoft/Dataverse-skills --skip-settings
gemini extensions config dataverse DATAVERSE_URL --scope workspace
```

Enter the Dataverse environment URL when prompted.

### Google Antigravity

Install the plugin from the Dataverse skills repository:

```console
agy plugin install https://github.com/microsoft/Dataverse-skills/tree/main/.github/plugins/dataverse
```

### Other agents

For any other agent that reads local skills, install every Dataverse skill with one command:

```console
npx skills add microsoft/Dataverse-skills -s "*"
```

## Connect to Dataverse

After installation, ask your coding agent:

> *Connect to my Dataverse environment.*

The [`dv-connect`](reference.md#dv-connect) skill:

1. Checks whether the workspace is already configured.
2. Verifies the required tools and installs or updates them when supported.
3. Discovers the environments available to your account and asks you to select one.
4. Configures Dataverse CLI and Power Platform CLI authentication.
5. Creates local workspace configuration and excludes credentials and generated artifacts from source control.
6. Configures the Dataverse MCP server for the coding agent.
7. Verifies the connection.

On hosts that can't run local CLIs or persist their credentials, the skill uses its Python SDK setup path rather than claiming that MCP is configured.

Some coding agents must be restarted after MCP registration before MCP tools become available. Follow the instructions provided by the connection flow.

To verify the connection after restarting, ask:

> *List the tables in my Dataverse environment.*

## Example prompts

Describe the task and relevant constraints. You don't normally need to identify a skill or tool.

- "Show me my open opportunities over $100,000 that close this quarter."
- "Import this CSV into the contacts table. Use an alternate key so I can safely run the import again."
- "Create a customer feedback table with name, rating, and comment columns in the CustomerService solution."
- "Create 500 ticket records efficiently in the `new_ticket` table. Each ticket needs a unique title and a priority value."
- "Export the CustomerService solution from development, unpack it into the repository, and validate the components."
- "Show me the audit settings for this environment."
- "Assign the Basic User role to `user@contoso.com` in the development environment."

Include the target environment, solution, expected volume, and safety constraints when they're important. The agent should still confirm the environment before making the first change in a session.

## Tool selection

The agent selects a tool based on the operation, data volume, and capabilities of the host.

| Tool | Typical use |
| --- | --- |
| [Dataverse MCP server](../../../maker/data-platform/data-platform-mcp.md) | Interactive queries, schema discovery, and small record or metadata operations |
| [Dataverse CLI](../cli/index.md) | Authentication, headless data operations, API discovery and invocation, and the local MCP proxy |
| [Dataverse SDK for Python](../sdk-python/overview.md) | Scripted schema operations, bulk data operations, paging, transformations, and analytics |
| [Power Platform CLI](/power-platform/developer/cli/introduction) | Solution application lifecycle management (ALM), environment operations, and role assignment |
| [Dataverse Web API](../webapi/overview.md) | Operations that aren't available through a managed tool |

For skill details, see the [plugin reference](reference.md). For authentication, confirmation rules, and high-impact operations, see [Security and governance](security-governance.md).

## Related content

- [Microsoft Dataverse plugin for AI agents](index.md)
- [Microsoft Dataverse plugin for AI agents reference](reference.md)
- [Security and governance for the Dataverse plugin](security-governance.md)
- [Dataverse-skills GitHub repository](https://github.com/microsoft/Dataverse-skills)

The author created this article with assistance from AI.

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
