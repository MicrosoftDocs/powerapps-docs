---
title: Microsoft Dataverse Plugin for AI Agents (Preview)
description: Use the Microsoft Dataverse plugin with AI coding agents to develop data models, query records, automate operations, and manage solutions.
#customer intent: As a Dataverse developer, I want to use the plugin with my coding agent so that I can build and manage solutions with natural language prompts.
ms.date: 11/11/2026
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

The Microsoft Dataverse plugin for AI agents helps you develop and manage Dataverse solutions with an AI coding agent. You describe an outcome in natural language, and the agent selects skills and tools to help you achieve it. The open-source instructions are available in [microsoft/Dataverse-skills](https://github.com/microsoft/Dataverse-skills).

[!INCLUDE [preview-note-business-applications-work-iq](~/../shared-content/shared/preview-includes/preview-note-business-applications-work-iq.md)]

The plugin doesn't replace Dataverse development tools or platform security. It guides the agent's use of the Dataverse MCP server, Dataverse CLI, Python SDK, Power Platform CLI, and Web API.

## Get started

> [!div class="nextstepaction"]
> [Prerequisites, installation, connection setup, and example prompts](coding-agents.md)


Supported agents include:

- [GitHub Copilot](https://github.com/features/copilot)
- [Claude Code](https://code.claude.com/docs/en/overview)
- [Cursor](https://cursor.com/)
- [OpenAI Codex](https://openai.com/codex/)
- [ChatGPT](https://chatgpt.com/overview/)
- [Gemini CLI](https://geminicli.com/)
- [Google Antigravity](https://antigravity.google/)

## Tasks the Dataverse plugin helps with

Use the skills to coordinate development tasks across the Dataverse toolchain.

| Task | Skill guidance |
| --- | --- |
| Plan work and choose tools | [`dv-overview`](reference.md#dv-overview) |
| Set up a workspace and authenticate | [`dv-connect`](reference.md#dv-connect) |
| Query and analyze records | [`dv-query`](reference.md#dv-query) |
| Create, import, update, and seed records | [`dv-data`](reference.md#dv-data) |
| Create and evolve tables, columns, relationships, forms, and views | [`dv-metadata`](reference.md#dv-metadata) |
| Package and deploy solutions | [`dv-solution`](reference.md#dv-solution) |
| Assign access and verify role changes | [`dv-security`](reference.md#dv-security) |
| Manage supported environment settings and data lifecycle operations | [`dv-admin`](reference.md#dv-admin) |
| Work with linked Finance and Operations developer environments | [`erp-sql`](reference.md#erp-sql), [`erp-xpp`](reference.md#erp-xpp) |

## How the Dataverse plugin works

The agent loads an orientation skill first, then specialized skills based on your request. A single request can use several skills. For example, creating a recruiting data model, loading sample records, and packaging changes can combine schema, data, and solution guidance.

The agent selects from MCP, CLIs, and the Python SDK based on the operation, data volume, and tools available in your workspace. If an operation isn't available, the skills explain the limitation rather than inventing a tool or working around a control.

## Safety and guardrails for the Dataverse plugin

Review the proposed action and validate its result.

- By using interactive authentication, the agent signs in as you and can't exceed your permissions.
- Dataverse enforces security on every request.
- The agent confirms the target environment before making changes.
- You preview or approve stateful actions before execution.

For service-principal authentication, MCP access controls, and high-impact operations, see [Security and governance](security-governance.md).

## Related content

- [Use the Dataverse plugin with AI coding agents](coding-agents.md)
- [Microsoft Dataverse plugin for AI agents reference](reference.md)
- [Security and governance for the Dataverse plugin](security-governance.md)
- [Use the Microsoft Dataverse plugin in Cowork (preview)](/copilot/cowork/dataverse-plugin)
- [Dataverse-skills GitHub repository](https://github.com/microsoft/Dataverse-skills)
- [Dataverse MCP server](../../../maker/data-platform/data-platform-mcp.md)
- [Microsoft Dataverse node (n8n docs)](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftdataverse/)

The author created this article with assistance from AI.

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
