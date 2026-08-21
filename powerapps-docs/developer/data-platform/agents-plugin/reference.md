---
title: Microsoft Dataverse plugin for AI coding agents reference (preview)
description: Review the Microsoft Dataverse plugin that AI coding agents use to connect, build, query, deploy, administer, and secure Dataverse.
#customer intent: As a developer using an AI coding agent, I want to review the available Dataverse plugin so that I can understand which tasks the agent can complete for me.
ms.date: 07/31/2026
ms.reviewer: jdaly
ms.topic: reference
author: kewear
ms.author: kewear
ms.collection: bap-ai-copilot
search.audienceType:
  - developer
contributors:
 - JimDaly
ai-usage: ai-assisted
---
# Microsoft Dataverse plugin for AI coding agents reference (preview)

> [!NOTE]
> - This is a preview feature.
> - [!INCLUDE [cc-preview-features-definition](../../../includes/cc-preview-features-definition.md)]

Microsoft Dataverse plugin for AI coding agents provide task-specific instructions that a supported coding agent loads based on your request. You normally describe the outcome rather than naming a skill. The plugin will route the request, to the best skill so the agent can combine multiple skills for a task.

The plugin and skills use the [Dataverse CLI](../cli/index.md), [Dataverse MCP server](../../../maker/data-platform/data-platform-mcp.md), [Dataverse SDK for Python](../sdk-python/overview.md), [Microsoft Power Platform CLI](/power-platform/developer/cli/introduction), and Dataverse Web API. For installation and safety information, see [Microsoft Dataverse plugin for AI coding agents](index.md).

The plugin, and related skills, source is in the [Dataverse-skills GitHub repository](https://github.com/microsoft/Dataverse-skills/tree/main/.github/plugins/dataverse/skills).

## `dv-overview`

The overview skill provides the common rules and tool-selection guidance used for Dataverse requests. The agent loads it before a specialized skill.

It helps the agent:

- Check whether the workspace is initialized.
- Select a managed tool based on the operation and data volume.
- Use the shared authentication patterns created by [`dv-connect`](#dv-connect).
- Confirm the target environment and solution before making changes.
- Follow an environment-first metadata workflow: make changes in Dataverse, export and unpack the solution, and then commit the generated files.
- Identify operations that aren't covered rather than inventing unsupported commands or SDK methods.

The overview skill routes work across MCP, the Dataverse CLI, the Dataverse SDK for Python, Power Platform CLI, and the Web API. For example, MCP is appropriate for interactive queries and small record sets, while the Python SDK is appropriate for bulk operations, transformations, paging, and analytics.

Example prompt:

> *Create a recruiting system with tables for positions, candidates, interviews, and feedback; load sample data; and package the components in a solution.*

This request can cause the agent to combine [`dv-metadata`](#dv-metadata), [`dv-data`](#dv-data), [`dv-query`](#dv-query), and [`dv-solution`](#dv-solution).

## `dv-connect`

The connect skill sets up a workspace for a Dataverse environment. The flow is idempotent: it checks existing configuration and skips completed steps.

It can:

- Check Git, Node.js, Python, .NET SDK, Azure CLI, Power Platform CLI, and the Dataverse CLI.
- Install or update the Dataverse CLI and Dataverse SDK for Python when needed.
- Discover environments and select authentication profiles.
- Configure interactive or service-principal authentication.
- Create local environment configuration and source-control exclusions.
- Register the Dataverse MCP server for GitHub Copilot, Claude Code, Cursor, or Codex.
- Verify CLI, SDK, and MCP connectivity.

Example prompts:

> *Connect to my Dataverse environment.*

> *Switch this workspace to the development environment and verify the MCP connection.*

> *Fix the Dataverse authentication configuration for this project.*

For details about the CLI installed and configured by this skill, see [Work with data by using the Dataverse CLI](../cli/index.md).

## `dv-query`

The query skill reads and analyzes Dataverse records. It selects MCP for small interactive reads and the Dataverse SDK for Python for bulk iteration, advanced queries, exports, notebooks, and DataFrame analysis.

It supports:

- Selecting, filtering, sorting, and paging records.
- Retrieving a record by ID.
- Resolving lookup values and expanding related records.
- Server-side counts, grouping, aggregation, and joins by using supported SQL or FetchXML.
- Streaming large result sets.
- Loading query results into pandas DataFrames.
- Exporting query results for further analysis.

The skill instructs the agent to query the live Dataverse environment when you ask a question about Dataverse data and to limit selected columns to reduce data transfer.

Example prompts:

> *Show me open opportunities over $100,000 that close this quarter.*

> *Group active opportunities by sales stage and show the count and total estimated value.*

> *Export account names, primary contacts, and cities to a CSV file.*

For SDK query patterns, see [Query data using the Dataverse SDK for Python](../sdk-python/query.md).

## `dv-data`

The data skill creates, updates, deletes, upserts, imports, and generates Dataverse records. MCP can handle small interactive sets. Scripted write operations use the official Dataverse SDK for Python.

It supports:

- Single-record create, update, and delete operations.
- Bulk create, update, and upsert operations.
- Alternate-key upsert for idempotent imports.
- CSV imports and lookup resolution.
- Multi-table imports ordered by foreign-key dependencies.
- pandas DataFrame write-back.
- File-column uploads.
- Schema-driven sample-data generation.

For large writes, the skill uses Dataverse bulk messages such as `CreateMultiple`, `UpdateMultiple`, and `UpsertMultiple` rather than one request per record. Large payloads are divided into batches.

These prompts are based on tests in the repository:

> *Write a Python script that creates a single ticket record in my Dataverse `new_ticket` table with a title and priority field.*

> *Write a Python script that efficiently creates 500 ticket records in my Dataverse `new_ticket` table. Each ticket should have a unique title and a priority value. Optimize for the fewest HTTP calls.*

Other example prompts:

> *Import `contacts.csv` and use email as an alternate key so rerunning the import doesn't create duplicates.*

> *Generate 20 sample contacts using example email addresses and phone numbers.*

For SDK write patterns, see [Work with data using the Dataverse SDK for Python](../sdk-python/work-data.md).

## `dv-metadata`

The metadata skill creates and inspects Dataverse schema components.

It supports:

- Tables and columns, including choice, lookup, file, and other supported column types.
- One-to-many and many-to-many relationships.
- Alternate keys.
- Forms and views.
- Existing schema inspection.
- Adding components to a solution.

Before the first metadata change, the skill directs the agent to confirm the environment, solution, and publisher prefix. New components are created in the environment by using a managed API and then pulled into the repository with solution export and unpack commands. The agent shouldn't create new Dataverse components by writing solution XML manually.

Example prompts:

> *Create a customer feedback table with name, rating, comment, and account lookup columns in the CustomerService solution.*

> *Add an alternate key on the external ticket ID column so the data import can use upsert.*

> *Add the priority and assigned agent fields to the ticket main form, and create a view for unresolved high-priority tickets.*

For SDK metadata patterns, see [Work with table definitions using the Dataverse SDK for Python](../sdk-python/metadata.md).

## `dv-solution`

The solution skill manages the Dataverse solution lifecycle by using Power Platform CLI and the Dataverse SDK for Python.

It supports:

- Discovering or creating publishers and solutions.
- Adding components to a solution.
- Exporting and unpacking an unmanaged development solution.
- Packing and importing solutions into another environment.
- Monitoring imports.
- Validating tables, forms, views, role assignments, and import errors after deployment.

The skill asks you to choose or confirm a publisher prefix before creating a publisher. It also confirms the source or target environment before export or import operations.

Example prompts:

> *Pull the schema into the CustomerService solution, export it from development, and unpack it into the repository.*

> *Pack the CustomerService solution, import it into the test environment, and verify that the ticket table, main form, and active tickets view are available.*

> *Show the publishers in this environment and create a solution using the publisher I select.*

For Power Platform CLI solution commands, see [Microsoft Power Platform CLI solution command group](/power-platform/developer/cli/reference/solution).

## `dv-admin`

The administration skill performs a defined set of environment-level operations.

It supports:

- Scheduling and managing bulk-delete jobs.
- Configuring retention and archival.
- Reading or updating allowlisted organization and OrgDB settings.
- Managing organization-level recycle-bin settings.
- Configuring supported audit settings.
- Listing or canceling supported Finance and Operations batch jobs in linked environments.

The skill uses a hard allowlist for settings that it can change. For other settings, use the Power Platform admin center. Unfiltered bulk delete is irreversible and bypasses the recycle bin, so the skill requires an explicit acknowledgement that names the table and states that **ALL records** should be deleted.

Example prompts:

> *Show me whether auditing and plug-in trace logging are enabled in this environment.*

> *Create a retention policy for activities older than three years.*

> *Schedule a bulk-delete job for completed activities created before January 1, 2024.*

For supported organization settings, see [Retrieve and update organization settings](../organization-table.md#use-pac-cli-to-retrieve-and-update-settings).

## `dv-security`

The security skill manages Dataverse user access by using first-party CLI commands and verifies that changes were applied.

It supports:

- Assigning security roles to users.
- Assigning roles to application users.
- Working with business-unit context for role assignment.
- Applying the same role change across multiple environments.
- Administrator self-elevation when the caller has the required tenant role.

Role changes require a preview and confirmation that identifies the user, role, and environment. Self-elevation requires an additional risk statement and reason, and the action is logged to Microsoft Purview.

Example prompts:

> *Assign the Basic User role to `user@contoso.com` in the development environment and verify the assignment.*

> *Add application ID `<application-id>` as an application user and assign the integration security role.*

> *Give me System Administrator access to the test environment for incident 12345.*

## Skill selection examples

| Request | Skills the agent might use |
| --- | --- |
| Connect and list tables | [`dv-overview`](#dv-overview), [`dv-connect`](#dv-connect), [`dv-query`](#dv-query) |
| Create a table and load a CSV file | [`dv-overview`](#dv-overview), [`dv-metadata`](#dv-metadata), [`dv-data`](#dv-data) |
| Analyze opportunity data in a notebook | [`dv-overview`](#dv-overview), [`dv-query`](#dv-query) |
| Package schema changes and deploy them to test | [`dv-overview`](#dv-overview), [`dv-solution`](#dv-solution) |
| Configure retention and review audit settings | [`dv-overview`](#dv-overview), [`dv-admin`](#dv-admin) |
| Add an integration user and assign a role | [`dv-overview`](#dv-overview), [`dv-security`](#dv-security) |

## Related content

- [Microsoft Dataverse plugin for AI coding agents](index.md)
- [Work with data by using the Dataverse CLI](../cli/index.md)
- [Dataverse SDK for Python](../sdk-python/overview.md)
- [Dataverse MCP server](../../../maker/data-platform/data-platform-mcp.md)
- [Microsoft Power Platform CLI](/power-platform/developer/cli/introduction)
- [Dataverse-skills GitHub repository](https://github.com/microsoft/Dataverse-skills)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
