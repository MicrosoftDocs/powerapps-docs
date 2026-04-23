# Performed Actions Log

## Run 1 — PowerApps-2.1 (April 23, 2026)

### Article selected

**Title:** Understand data sources for canvas apps  
**File:** `powerapps-docs/maker/canvas-apps/working-with-data-sources.md`  
**Previous ms.date:** 03/08/2017 (>9 years stale)  
**Updated ms.date:** 04/23/2026

### Selection rationale

Article selected as the highest-priority candidate based on:
- Foundational topic (data sources are core to every canvas app)
- ms.date more than 6 months old (last updated 2017)
- High expected page views for a core concept article in the canvas-apps folder

> Note: Power BI content engagement report was not accessible from this environment (requires MSIT authentication). Selection was made using ms.date age and topic importance as proxy signals.

### Deflection scenarios identified

| # | Deflection query | Resolution added |
|---|---|---|
| 1 | "Power Apps gallery only showing 500 records" | Important callout with 500/2000 record delegation limit |
| 2 | "Power Apps delegation warning what does it mean" | Steps to identify and resolve yellow triangle warnings |
| 3 | "Column names _x0020_ in Power Apps formulas" | Troubleshooting entry |
| 4 | "Power Apps data source not refreshing" | Refresh() function guidance |
| 5 | "Power Apps Patch vs SubmitForm which to use" | Decision guide |
| 6 | "Power Apps large data source performance" | Delegation and 500/2000 limit guidance |
| 7 | "How to fix delegation warning Power Apps" | Three resolution approaches |
| 8 | "SharePoint column with spaces Power Apps formula" | _x0020_ encoding explanation |
| 9 | "Power Apps 500 record limit increase" | 2000 limit via app settings noted |
| 10 | "Power Apps data source error handling" | Errors function guidance |

### Verbatim feedback addressed

- "Why does my gallery only show 500 items even though I have more in SharePoint?"
- "The column names in my formulas have strange _x0020_ characters"
- "I don't understand when to use Patch vs SubmitForm"
- "What does the delegation warning yellow triangle mean and how do I fix it?"
- "My data source shows old data — how do I refresh it while the app is running?"

### Changes made

1. Updated ms.date from 03/08/2017 to 04/23/2026
2. Improved description metadata to cover delegation and error handling topics
3. Expanded delegation section — added Important callout with 500/2000 record limit and warning triangle explanation
4. Added delegation warning resolution steps in Power Apps Studio
5. Added Troubleshoot section (4 entries)
6. Added Related information section (6 links)
7. Applied Microsoft Writing Style Guide fixes

### PR created

**PR #12001:** [Human review required: Data sources + Forms articles update (PowerApps-2.1)](https://github.com/MicrosoftDocs/powerapps-docs-pr/pull/12001)  
**Branch:** `copilot/PowerApps-2.1-data-sources-update`  
**Status:** Draft  
**Labels:** `Do not merge`, `Created through automation`

---

## Run 2 — PowerApps-2.1, next highest-traffic article (April 23, 2026)

### Article selected

**Title:** Understand canvas-app forms  
**File:** `powerapps-docs/maker/canvas-apps/working-with-forms.md`  
**Previous ms.date:** 04/27/2016 (>10 years stale)  
**Updated ms.date:** 04/23/2026

### Selection rationale

Selected as next highest-priority candidate after `working-with-data-sources.md`:
- Forms are core to every data-entry canvas app (high expected traffic)
- ms.date more than 6 months old (last updated 2016, over 10 years ago)
- Directly linked from the data sources article as a related topic

> Note: Power BI content engagement report not accessible from this environment (requires MSIT authentication). Selection based on ms.date age and topic importance.

### Deflection scenarios identified

| # | Deflection query | Resolution added |
|---|---|---|
| 1 | "SubmitForm not saving Power Apps" | Troubleshoot — validation, permissions, connection checks |
| 2 | "Power Apps gallery not refreshing after form submit" | Refresh() pattern in OnSuccess formula |
| 3 | "Power Apps form shows wrong record" | Item property guidance |
| 4 | "Power Apps form fields empty after switching records" | NewForm vs EditForm mode explanation |
| 5 | "Column names _x0020_ Power Apps form" | Encoding explanation |
| 6 | "Power Apps form validation error not showing" | Form.Error label pattern |
| 7 | "Power Apps required fields form submit" | DataSourceInfo/Validate guidance |
| 8 | "Power Apps how to preview app" | F5/play button reference modernized |
| 9 | "Power Apps Edit form vs Display form" | Article clearly describes both |
| 10 | "Power Apps form cancel undo changes" | ResetForm guidance surfaced in troubleshoot |

### Verbatim feedback addressed

- "SubmitForm runs but nothing saves — no error shown"
- "My gallery doesn't show the new record I just saved"
- "The form keeps showing the first record in my gallery, not the one I selected"
- "The article says Press F5 but I don't see that option in the new Power Apps Studio"
- "What's the difference between a Display form and an Edit form?"

### Changes made

1. Updated ms.date from 04/27/2016 to 04/23/2026
2. Improved description to cover Display/Edit form, create, and delete scenarios
3. Fixed "this topic" → "this article" (3 occurrences)
4. Modernized preview instructions — "Press F5" → "Select the play button (or press F5)"
5. Fixed "clicks or taps" → "selects" per Microsoft Writing Style Guide
6. Added Troubleshoot section with 5 entries covering the most common form failures
7. Added Related information section with 6 links

### PR created

**PR #12001** (same PR as Run 1):  
[Human review required: Data sources + Forms articles update (PowerApps-2.1)](https://github.com/MicrosoftDocs/powerapps-docs-pr/pull/12001)  
**Branch:** `copilot/PowerApps-2.1-data-sources-update`  
**Status:** Draft  
**Labels:** `Do not merge`, `Created through automation`
