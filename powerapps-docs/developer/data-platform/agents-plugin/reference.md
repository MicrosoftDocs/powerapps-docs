---
title: Microsoft Dataverse Plugin for AI Agents Reference (Preview)
description: Review the Dataverse plugin skills, tools, and example prompts that AI coding agents use to connect, build, query, deploy, administer, and secure Dataverse.
#customer intent: As a developer using an AI coding agent, I want to review the available Dataverse skills so that I can understand which development tasks the agent can complete.
ms.date: 11/11/2026
ms.reviewer: jdaly
ms.topic: reference
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
# Microsoft Dataverse plugin for AI agents reference (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

The Microsoft Dataverse plugin for AI agents provides task-specific skills that your AI coding agent loads based on your request. This reference describes each skill, its tools, and example prompts so you know which Dataverse development tasks the agent can complete. Describe the outcome rather than naming a skill. The agent loads orientation guidance and can combine specialized skills for one task.

[!INCLUDE [preview-note-business-applications-work-iq](~/../shared-content/shared/preview-includes/preview-note-business-applications-work-iq.md)]

The skills use the [Dataverse CLI](../cli/index.md), [Dataverse MCP server](../../../maker/data-platform/data-platform-mcp.md), [Dataverse SDK for Python](../sdk-python/overview.md), [Power Platform CLI](/power-platform/developer/cli/introduction), and [Dataverse Web API](../webapi/overview.md).

For setup, see [Use the plugin with AI coding agents](coding-agents.md). For authentication and controls, see [Security and governance](security-governance.md). Skill source is in the [Dataverse-skills repository](https://github.com/microsoft/Dataverse-skills/tree/main/.github/plugins/dataverse/skills).

## Dataverse plugin skill index

Select a skill to review its tools, supported tasks, and example prompts.

| Skill | Use for |
| --- | --- |
| [`dv-overview`](#dv-overview) | Orientation, planning, and tool selection |
| [`dv-connect`](#dv-connect) | Workspace setup, authentication, and connection diagnostics |
| [`dv-query`](#dv-query) | Queries, paging, exports, and analytics |
| [`dv-data`](#dv-data) | Record writes, imports, files, and sample data |
| [`dv-metadata`](#dv-metadata) | Tables, columns, relationships, keys, forms, and views |
| [`dv-solution`](#dv-solution) | Publishers, solutions, deployment, and validation |
| [`dv-admin`](#dv-admin) | Supported environment settings, bulk delete, and retention |
| [`dv-security`](#dv-security) | User and application-user access, role assignment, and administrator self-elevation |
| [`erp-sql`](#erp-sql) | Opt-in temporary Reader SQL access in eligible Finance and Operations developer environments |
| [`erp-xpp`](#erp-xpp) | X++ development, compilation, deployment, and database synchronization |

## `dv-overview`

The overview skill provides the Dataverse context, common rules, and tool-selection guidance. The agent loads it before specialized skills.

It helps the agent:

- Check workspace and connection state.
- Select a managed tool based on the operation and data volume.
- Use the shared authentication patterns configured by [`dv-connect`](#dv-connect).
- Confirm the target environment and solution before metadata changes.
- Follow an environment-first workflow: make changes in Dataverse, then export, unpack, and commit them.
- Identify gaps rather than inventing unsupported commands or SDK methods.

Example prompt:

> *Create a recruiting data model, load sample records, and package the components in a solution.*

This request can combine [`dv-metadata`](#dv-metadata), [`dv-data`](#dv-data), [`dv-query`](#dv-query), and [`dv-solution`](#dv-solution).

## `dv-connect`

Use the connection guidance to set up or diagnose a coding-agent workspace. The flow checks the existing configuration and skips completed steps.

The skill:

- Checks Git, Node.js, Python, .NET SDK, Azure CLI, Power Platform CLI, and the Dataverse CLI.
- Installs or updates required tools when the host supports them.
- Discovers environments, selects authentication profiles, and configures interactive or service-principal authentication.
- Creates local environment configuration and source-control exclusions.
- Configures MCP for GitHub Copilot, Claude Code, Cursor, Codex, Gemini CLI, and Google Antigravity.
- Verifies CLI, SDK, and MCP connectivity where available.

Gemini CLI uses the extension's bundled MCP configuration and the GA endpoint. Antigravity uses its host-specific MCP registration. On constrained hosts, the skill uses its Python SDK path and skips local CLI and MCP setup.

Example prompts:

> *Connect to my Dataverse environment.*
>
> *Switch this workspace to the development environment and verify the MCP connection.*

For the connection flow, see [Connect to Dataverse](coding-agents.md#connect-to-dataverse).

## `dv-query`

The query skill reads and analyzes Dataverse records. It uses MCP for small interactive reads, the Dataverse CLI for headless queries, and the Python SDK for bulk reads and analytics.

It supports:

- Selecting, filtering, sorting, and paging records.
- Retrieving a record by ID.
- Resolving lookup display values and expanding related records.
- Supported server-side counts, grouping, aggregation, and joins through SQL or FetchXML.
- Streaming large result sets.
- CSV exports, notebooks, and pandas DataFrames.

The skill queries the live environment and limits selected columns. For SDK patterns, see [Query data using the Dataverse SDK for Python](../sdk-python/query.md).

For linked Finance and Operations environments, the skill uses ERP MCP or the Dataverse CLI's ERP target for business-data reads and runtime entity, schema, or action discovery, rather than the Dataverse Python SDK. Direct developer-database access is a separate, opt-in [`erp-sql`](#erp-sql) workflow.

Example prompts:

> *Group active opportunities by sales stage and show the count and total estimated value.*
>
> *Export account names, primary contacts, and cities to a CSV file.*

## `dv-data`

The data skill creates, corrects, imports, and seeds records. It uses MCP for small interactive sets, the Dataverse CLI for individual operations, and the Python SDK for scripted and bulk writes.

It supports:

- Single-record create, update, and delete operations.
- Alternate-key upsert for idempotent imports.
- Bulk create, update, and upsert operations.
- CSV mapping and lookup resolution.
- Multi-table imports ordered by foreign-key dependencies.
- pandas DataFrame write-back.
- File-column uploads.
- Schema-driven sample-data generation.

For large writes, the skill uses Dataverse bulk messages such as `CreateMultiple`, `UpdateMultiple`, and `UpsertMultiple`. Scripts divide large payloads into batches. On linked Finance and Operations environments, the skill has separate guidance for ERP record writes and Data Management Framework (DMF) package imports.

Example prompts:

> *Import contacts.csv and use email as an alternate key so rerunning the import doesn't create duplicates.*
>
> *Create 500 ticket records efficiently, with unique titles and valid priority values.*

For SDK write patterns, see [Work with data using the Dataverse SDK for Python](../sdk-python/work-data.md).

## `dv-metadata`

The metadata skill creates and inspects Dataverse schema. It uses MCP for supported table and column changes, the Python SDK for schema and form or view records, and managed Web API calls for gaps.

It supports:

- Tables and columns, including choice, lookup, and file columns.
- One-to-many and many-to-many relationships.
- Alternate keys.
- Forms and views.
- Existing schema inspection.
- Adding components to a solution.

Before the first metadata change, the agent confirms the environment, solution, and publisher prefix. It creates components in the environment through managed APIs and pulls the result into the repository by using solution export and unpack commands, rather than hand-writing new solution XML.

Example prompts:

> *Create a customer feedback table with name, rating, comment, and account lookup columns in the CustomerService solution.*
>
> *Add priority and assigned agent fields to the ticket main form and create a view for unresolved high-priority tickets.*

For SDK patterns, see [Work with table definitions using the Dataverse SDK for Python](../sdk-python/metadata.md).

## `dv-solution`

The solution skill manages the solution lifecycle. It uses Power Platform CLI to export, unpack, pack, and import solutions. It uses the Python SDK to manage publisher and solution records and to perform validation.

It supports:

- Discovering or creating publishers and solutions.
- Adding components to a solution.
- Exporting and unpacking unmanaged development solutions.
- Packing and importing solutions into another environment.
- Checking import progress and errors.
- Validating tables, forms, views, and role assignments after deployment.

The agent asks you to choose or confirm a publisher prefix before creating a publisher. It asks you to confirm the source or target environment before exporting or importing.

Example prompts:

> *Pull the schema into the CustomerService solution, export it from development, and unpack it into the repository.*
>
> *Pack the CustomerService solution, import it into test, and verify that the ticket table, main form, and active tickets view are available.*

See [Power Platform CLI solution commands](/power-platform/developer/cli/reference/solution).

## `dv-admin`

The administration skill manages supported environment-level settings and data lifecycle operations. It uses Power Platform CLI and Python SDK or Web API paths selected by the setting or operation.

It supports:

- Scheduling and managing bulk-delete jobs.
- Configuring retention and archival.
- Reading or updating allowlisted organization and OrgDB settings.
- Managing organization-level recycle bin configuration.
- Configuring supported audit settings.
- Listing or canceling supported Finance and Operations batch jobs in linked environments.

Settings are limited to a hard allow list. For other settings, use the Power Platform admin center. Unfiltered bulk delete is irreversible and bypasses the recycle bin. The skill requires an explicit acknowledgment naming the table and stating that **all records** are to be deleted.

Example prompts:

> *Show me whether auditing and plug-in trace logging are enabled in this environment.*
>
> *Create a retention policy for activities older than three years.*

For organization settings, see [Retrieve and update organization settings](../organization-table.md#use-pac-cli-to-retrieve-and-update-settings).

## `dv-security`

The security skill manages user access through first-party CLIs and verifies that changes were applied. It uses Power Platform CLI for role assignment and administrator self-elevation, with Dataverse reads to verify results.

It supports:

- Assigning existing security roles to users.
- Assigning roles to application users.
- Working with business-unit context for role assignment.
- Applying approved role changes across selected environments.
- Administrator self-elevation when the caller has the required tenant role.

Role changes need a preview that identifies the user, role, and environment, followed by confirmation and read-back verification. Self-elevation needs a separate risk statement, reason, and confirmation, and is logged to Microsoft Purview.

Example prompts:

> *Assign the Basic User role to `user@contoso.com` in development and verify the assignment.*
>
> *Add this application ID as an application user and assign the integration security role.*

## `erp-sql`

The ERP SQL skill describes temporary Reader access and bounded physical-table reads in eligible Finance and Operations unified development environments (UDEs). It uses the managed Dataverse CLI, Python helpers, and sqlcmd. This workflow is an explicit opt-in process, not an ordinary business-data query path or the Dataverse TDS endpoint.

The skill requires the environment System administrator role and approval of the user-supplied IP scope, reason, and bounded reads. A new grant invalidates existing SQL credentials for the same user and environment. The skill keeps credentials in memory and requires a verified connection rather than treating a credential response as success.

The skill notes that its credential action lacks a documented public API contract and stops if a compatible contract can't be verified. For the documented product workflow, see [Finance and operations product database access](/power-platform/developer/unified-experience/finance-operations-product-db-access).

Example prompt:

> *Explain the prerequisites and access impact before requesting temporary Reader access to my Finance and Operations developer database.*

## `erp-xpp`

The X++ skill covers code development and deployment for a linked Finance and Operations environment. It uses Power Platform CLI package and X++ SDK commands on Windows, with selected runtime checks through ERP tools.

The skill scaffolds models, guides authoring classes, custom services, APIs, and data entities, installs matching SDKs, compiles deployable packages, deploys packages, and synchronizes databases. SDK installation and compilation require Windows.

Before deployment or database synchronization, the agent confirms the Dataverse target and verifies the linked ERP environment. It asks you to choose the database synchronization scope when the request is ambiguous. Additional post-deployment checks are opt-in: the agent asks which checks you authorize and confirms inputs and expected effects before runtime execution.

Example prompts:

> *Create an X++ model for this customization and compile a deployable package.*
>
> *Deploy this package to the linked development environment without database synchronization.*

## Dataverse plugin skill selection examples

A request can use several skills.

| Request | Skills the agent might use |
| --- | --- |
| Connect and list tables | [`dv-overview`](#dv-overview), [`dv-connect`](#dv-connect), [`dv-query`](#dv-query) |
| Create a table and load a CSV file | [`dv-overview`](#dv-overview), [`dv-metadata`](#dv-metadata), [`dv-data`](#dv-data) |
| Analyze opportunity data in a notebook | [`dv-overview`](#dv-overview), [`dv-query`](#dv-query) |
| Package schema changes and deploy them to test | [`dv-overview`](#dv-overview), [`dv-solution`](#dv-solution) |
| Configure retention and review audit settings | [`dv-overview`](#dv-overview), [`dv-admin`](#dv-admin) |
| Add an integration user and assign a role | [`dv-overview`](#dv-overview), [`dv-security`](#dv-security) |

## Related content

- [Microsoft Dataverse plugin for AI agents](index.md)
- [Use the Dataverse plugin with AI coding agents](coding-agents.md)
- [Security and governance for the Dataverse plugin](security-governance.md)
- [Dataverse-skills GitHub repository](https://github.com/microsoft/Dataverse-skills)

The author created this article with assistance from AI.

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
