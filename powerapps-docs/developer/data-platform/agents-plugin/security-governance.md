---
title: Dataverse AI Agents Plugin Security and Governance (Preview)
description: Learn how the Dataverse plugin for AI agents secures access with coding-agent authentication, MCP controls, and confirmation workflows.
#customer intent: As a Dataverse user or administrator, I want to understand the plugin's security model so that I can review access and approve changes safely.
ms.date: 11/11/2026
ms.reviewer: jdaly
ms.topic: concept-article
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
# Security and governance for the Dataverse plugin for AI agents (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

The Dataverse plugin for AI agents combines platform-enforced security with confirmation workflows for AI coding agents. Learn how both work so you can review access and approve changes safely when your coding agent uses Dataverse tools.

[!INCLUDE [preview-note-business-applications-work-iq](~/../shared-content/shared/preview-includes/preview-note-business-applications-work-iq.md)]

For installation and connection setup, see [Use the plugin with AI coding agents](coding-agents.md).

## Shared Dataverse security model

Dataverse enforces table privileges, field-level security, ownership and sharing, and administrator permissions on every request. An agent can't exceed the permissions of the signed-in identity. If that identity lacks a required privilege, the operation fails.

Skills are behavioral guidance, not a security boundary. They guide planning, environment confirmation, approval, and validation, but don't replace platform controls, coding-agent approvals, tenant policy, or your review of the proposed action. The agent confirms the environment before changes and previews or requests approval for stateful actions.

## Security for AI coding agents

Coding agents can use several tools, each with its own supported operations and authentication requirements. See [Use the plugin with AI coding agents](coding-agents.md) for installation and connection setup.

### Supported operations

Availability depends on the selected tool and the authenticated identity's privileges.

| Category | Examples | Requirement |
| --- | --- | --- |
| Read | Query records, inspect tables and columns, search metadata | Dataverse read privileges |
| Create | Create records, tables, columns, relationships, forms, and views | Corresponding create and customization privileges |
| Update | Update records, schema, forms, views, and supported environment settings | Corresponding update or administrator privileges |
| Import and export | Import CSV data, export or import solutions, run bulk data operations | Tool-specific privileges and access to the target environment |
| Delete | Delete records or metadata components | Corresponding delete or customization privileges |

### Coding-agent authentication and authorization

Interactive developer authentication uses Microsoft identity flows and caches tokens in the operating system credential store. Service-principal authentication is available for unattended scenarios. Service-principal tokens are held in memory rather than persisted. The agent can't exceed the authenticated user's or service principal's permissions.

Dataverse MCP has additional authorization layers:

1. The developer authenticates.
2. A tenant administrator grants consent to the MCP client application.
3. An environment administrator allows the client application in each target environment.

Other tools used by the plugin, such as the Dataverse SDK for Python and Power Platform CLI, authenticate directly and aren't subject to these MCP-specific controls. Their requests still require Dataverse authorization.

### Confirmation before changes

The coding agent instructions direct the agent to:

- Show the target environment URL and get confirmation before the first operation against that environment in a session.
- Verify the active organization connection.
- Ask which solution should contain new metadata.
- Show existing publishers and get confirmation before selecting or creating a publisher prefix. A prefix is permanent for components created with it.
- Preview security changes, environment-setting changes, bulk operations, and other stateful actions before execution.

### Irreversible and high-impact operations

Some operations need extra review:

- Bulk delete bypasses the recycle bin. The administration skill requires explicit acknowledgment that includes **all records** and the table logical name before it schedules an unfiltered bulk deletion.
- Deleting a table also removes dependent columns, forms, views, and other components.
- Importing a solution into production can affect all users. The solution skill includes post-import validation guidance.
- Bulk imports should use alternate keys and upsert when reruns are expected, and should be divided into appropriate batches.
- Assigning roles or using administrator self-elevation changes the security posture. The security skill requires explicit preview and confirmation. Self-elevation also requires a reason and a separate confirmation after the risk statement. Microsoft Purview logs self-elevation.
- X++ deployment and database synchronization require target confirmation and an explicit synchronization scope. Additional post-deployment validation is opt-in.
- Temporary ERP SQL access through `erp-sql` is restricted to eligible Unified Developer Environment (UDE) instances and Reader access. A new grant invalidates the same user's existing SQL credentials in that environment. The skill requires explicit approval for that impact, the user-supplied IP scope and reason, and any bounded reads.

### Credentials, data, logging, and telemetry

- Interactive tokens are stored in the operating system credential store. Service-principal tokens are held in memory.
- The connection flow excludes local configuration files that can contain credentials from source control.
- Client-side logs can contain tool execution events, request metadata, status codes, errors, and validation failures. They aren't intended to contain record data, credentials, or personal information.
- The environment's existing Dataverse audit and telemetry policies govern requests.
- Requests can include application metadata that identifies the plugin version, skill, and coding-agent type. Prompts, tool arguments, record data, file contents, and command strings aren't included in this attribution metadata.

## Report security issues and send feedback

For security issues, follow the instructions in the [Dataverse-skills SECURITY.md](https://github.com/microsoft/Dataverse-skills/blob/main/SECURITY.md). For product feedback or guardrail requests, [create an issue](https://github.com/microsoft/Dataverse-skills/issues).

## Related content

- [Microsoft Dataverse plugin for AI agents](index.md)
- [Use the Dataverse plugin with AI coding agents](coding-agents.md)
- [Microsoft Dataverse plugin for AI agents reference](reference.md)
- [Security concepts in Dataverse](../security-concepts.md)

The author created this article with assistance from AI.

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
