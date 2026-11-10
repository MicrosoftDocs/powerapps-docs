---
title: Microsoft Dataverse Plugin for AI Agents (Preview)
description: Learn how to install and use Microsoft Dataverse plugin for AI agents, including coding agents and Copilot Cowork, to build, query, and manage Dataverse solutions.
#customer intent: As a Dataverse developer, I want to use the Dataverse plugin with my AI agent, so that I can build and manage solutions with natural language prompts.
ms.date: 11/09/2026
ms.reviewer: jdaly
ms.topic: overview
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
# Microsoft Dataverse plugin for AI agents (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

Microsoft Dataverse plugin for AI agents is an open-source set of instructions that helps supported AI agents perform Dataverse development and administration tasks. You describe the outcome you want in natural language, and the agent selects the appropriate skill and tool.

[!INCLUDE [preview-note-business-applications-work-iq](~/../shared-content/shared/preview-includes/preview-note-business-applications-work-iq.md)]

The plugin doesn't replace the Dataverse development tools. It gives the agent task-specific guidance for using the [Dataverse CLI](../cli/index.md), [Dataverse MCP server](../../../maker/data-platform/data-platform-mcp.md), [Dataverse SDK for Python](../sdk-python/overview.md), [Microsoft Power Platform CLI](/power-platform/developer/cli/introduction), and [Dataverse Web API](../webapi/overview.md).

The same skills are available in more places over time. In addition to coding agents, the plugin is available in Microsoft Copilot Cowork, where it adds an approval-driven, conversational experience for building Dataverse data models and apps. Dataverse support in agents and tools is expanding quickly, with new skills, MCP server tools, and platforms added regularly.

The source is available in the [microsoft/Dataverse-skills](https://github.com/microsoft/Dataverse-skills) GitHub repository.

## Why use the Dataverse plugin?

Dataverse development frequently requires selecting and coordinating several tools. For example, creating a data model, loading records, and moving the changes to another environment can involve the Dataverse SDK for Python, the Dataverse CLI, Power Platform CLI, and the Web API.

The plugin provides the coding agent with guidance for:

- Loading the correct skill that identifies the right tool to accomplish the task.
- Selecting a tool based on the operation and data volume.
- Discovering environments and configuring authentication.
- Creating tables, columns, relationships, forms, and views in a solution.
- Reading, analyzing, importing, and updating Dataverse data.
- Exporting, importing, and validating solutions.
- Performing supported environment and security administration tasks.
- Applying confirmation steps before changes that affect an environment, solution, data, or security configuration.

This guidance reduces the amount of tool-specific syntax you need to provide in a prompt. You should still review proposed changes, confirm the target environment, and validate the result.

## How the plugin works

The coding agent plugin loads an overview skill for the Dataverse context and then selects one or more specialized skills based on your request. A single request can use several skills. For example, a request to create a recruiting data model, add sample data, and package it can use the metadata, data, query, and solution skills.

The agent selects among these supported tools:

| Tool | Typical use |
| --- | --- |
| Dataverse MCP server | Interactive queries, schema discovery, and small record or metadata operations |
| Dataverse CLI | Authentication, headless data operations, API discovery and invocation, and the local MCP proxy |
| Dataverse SDK for Python | Scripted schema operations, bulk data operations, paging, transformations, and analytics |
| Power Platform CLI | Solution application lifecycle management (ALM), environment operations, and role assignment |
| Dataverse Web API | Operations that aren't available through a managed tool |

For descriptions of all the included skills, see [Microsoft Dataverse plugin for AI agents reference](reference.md).

## Prerequisites

You need:

- A Dataverse environment available through Power Apps, Dynamics 365, or another applicable Power Platform plan. For a nonproduction environment, use a sandbox or managed developer environment.
- A user account with access to the environment and the privileges required for the operations you request.
- A supported agent: GitHub Copilot, Claude Code, Cursor, OpenAI Codex and ChatGPT, Gemini CLI, or Google Antigravity. Any other agent that reads local skills can also use them. For Copilot Cowork, see [Use the Microsoft Dataverse plugin in Cowork (preview)](/copilot/cowork/dataverse-plugin).
- For coding agents, permission to install or run any required local tools.

The [`dv-connect`](reference.md#dv-connect) skill checks the local toolchain and guides installation or configuration when needed. Depending on the requested operations, the toolchain can include Git, Node.js, Python 3, .NET SDK, Azure CLI, Power Platform CLI, the Dataverse CLI, and the Dataverse SDK for Python.

For coding agents, Dataverse MCP access also requires tenant administrator consent and per-environment client allowlisting. The connection flow identifies these requirements and provides the appropriate instructions, but doesn't bypass administrator approval.

## Install the plugin

Install the plugin for your coding agent.

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

## Use the plugin in Copilot Cowork

In Copilot Cowork, the Microsoft Dataverse plugin brings the same skills to a conversational experience. Cowork connects to one Dataverse environment through the Power Platform Dataverse connector, so you don't need to install local tools or allow a separate MCP client. Every change appears as an approval card, and Cowork can build and publish an app on your tables in Microsoft Copilot Managed Runtime (preview).

:::image type="content" source="media/agents-plugin/cowork-plugin-skills.png" alt-text="Screenshot of the Microsoft Dataverse plugin in Cowork, showing the Dataverse MCP server and the available dv skills." lightbox="media/agents-plugin/cowork-plugin-skills.png":::

Cowork works through the operations its connection exposes, which is a narrower set than coding agents that run the Dataverse CLI and SDKs, and it's growing. Where an operation isn't available, the skills tell you how to finish the step yourself rather than working around a control.

More information: [Use the Microsoft Dataverse plugin in Cowork (preview)](/copilot/cowork/dataverse-plugin)

## Connect to Dataverse

After installation, ask your coding agent:

> *Connect to my Dataverse environment.*

The [`dv-connect`](reference.md#dv-connect) skill:

1. Checks whether the workspace is already configured.
1. Verifies the required tools and installs or updates them when supported.
1. Discovers the environments available to your account and asks you to select one.
1. Configures Dataverse CLI and Power Platform CLI authentication.
1. Creates local workspace configuration and excludes credentials and generated artifacts from source control.
1. Registers the Dataverse MCP server for the coding agent.
1. Verifies the connection.

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

## Safety and guardrails

The skills combine Dataverse platform security with behavioral instructions for the coding agent. Dataverse enforces platform controls. Agent-level guardrails guide how the agent plans, confirms, and executes an operation, but they aren't a substitute for reviewing the proposed action.

### Supported operations

| Category | Examples | Requirement |
| --- | --- | --- |
| Read | Query records, inspect tables and columns, search metadata | Dataverse read privileges |
| Create | Create records, tables, columns, relationships, forms, and views | Corresponding create and customization privileges |
| Update | Update records, schema, forms, views, and supported environment settings | Corresponding update or administrator privileges |
| Import and export | Import CSV data, export or import solutions, run bulk data operations | Tool-specific privileges and access to the target environment |
| Delete | Delete records or metadata components | Corresponding delete or customization privileges |

### Authentication and authorization

Interactive developer authentication uses Microsoft identity flows and caches tokens in the operating system credential store. Service-principal authentication is available for unattended scenarios. The skills hold tokens in memory rather than persisting them.

The coding agent execution can't exceed the permissions of the authenticated identity. Dataverse enforces table privileges, field-level security, ownership and sharing, and administrator permissions on every request. If the identity lacks a required privilege, the operation fails.

Dataverse MCP has additional authorization layers:

1. The developer authenticates.
1. A tenant administrator grants consent to the MCP client application.
1. An environment administrator allows the client application in each target environment.

Other tools used by the plugin, such as the Dataverse SDK for Python and Power Platform CLI, authenticate directly and aren't subject to these MCP-specific controls.

### Confirmation before changes

The plugin instructions direct the agent to:

- Show the target environment URL and get confirmation before the first operation against that environment in a session.
- Verify the active organization connection.
- Ask which solution should contain new metadata.
- Show existing publishers and get confirmation before selecting or creating a publisher prefix. A prefix is permanent for components created with it.
- Preview security changes, environment-setting changes, bulk operations, and other stateful actions before execution.

### Irreversible and high-impact operations

Some operations need extra review:

- Bulk delete bypasses the recycle bin. The administration skill requires explicit acknowledgment that includes **all records** and the table logical name before it schedules an unfiltered bulk deletion.
- Deleting a table also removes dependent columns, forms, views, and other components.
- Importing a solution into a production environment can affect all users. The solution skill includes post-import validation guidance.
- Bulk imports should use alternate keys and upsert when reruns are expected, and should be divided into appropriate batches.
- Assigning roles or using administrator self-elevation changes the security posture. The security skill requires explicit preview and confirmation. Microsoft Purview logs self-elevation.

### Credentials, data, logging, and telemetry

- Interactive tokens are stored in the operating system credential store. Service-principal tokens are held in memory.
- The connection flow excludes local configuration files that can contain credentials from source control.
- Client-side logs can contain tool execution events, request metadata, status codes, errors, and validation failures. They aren't intended to contain record data, credentials, or personal information.
- The environment's existing Dataverse audit and telemetry policies govern requests.
- Requests can include application metadata that identifies the plugin version, skill, and coding-agent type. Prompts, tool arguments, record data, file contents, and command strings aren't included in this attribution metadata.

For security issues, follow the instructions in the repository [SECURITY.md](https://github.com/microsoft/Dataverse-skills/blob/main/SECURITY.md). For product feedback or guardrail requests, [create an issue](https://github.com/microsoft/Dataverse-skills/issues).

## Related content

- [Microsoft Dataverse plugin for AI agents reference](reference.md)
- [Use the Microsoft Dataverse plugin in Cowork (preview)](/copilot/cowork/dataverse-plugin)
- [Microsoft Dataverse node (n8n docs)](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftdataverse/)
- [What is Microsoft Copilot Managed Runtime? (preview)](/microsoft-365/copilot-managed-runtime/)
- [Work with data by using the Dataverse CLI](../cli/index.md)
- [Dataverse SDK for Python](../sdk-python/overview.md)
- [Dataverse MCP server](../../../maker/data-platform/data-platform-mcp.md)
- [Microsoft Power Platform CLI](/power-platform/developer/cli/introduction)
- [Dataverse-skills GitHub repository](https://github.com/microsoft/Dataverse-skills)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
