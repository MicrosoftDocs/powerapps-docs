---
title: Business Applications in Work IQ
description: Learn how to use Business Applications in Work IQ to bring business data understanding to AI agents and Copilot.
ms.date: 11/17/2026
ms.reviewer: matp
ms.topic: how-to
author: prithvi-khosla
ms.subservice: dataverse-maker
ms.author: pkhosla
ms.service: powerapps
ms.custom:
  - ai-gen-docs-bap
  - ai-seo-date:10/08/2026
ai-usage: ai-assisted
search.audienceType: 
  - maker
ms.collection: 
    - bap-ai-copilot
---
# Business Applications in Work IQ

Work IQ is the context and intelligence layer for Microsoft Copilot and agents. Business Applications in Work IQ adds data, processes, and operational context from Dynamics 365 and Power Apps. Users and agents can then work with business data while existing Dataverse permissions and application controls continue to apply.


> [!IMPORTANT]
> The Dataverse intelligence (preview) setting is now the Work IQ setting. Enable it in the Power Platform admin center to keep using your Dataverse data with Copilot and agents, along with the added capabilities in Business Applications in Work IQ 

Business Applications in Work IQ helps you:

- Enables scale across the enterprise. Organizations have many apps, agents, and processes––not just one. Business Applications in Work IQ addresses that broader problem by enabling business process context to become available everywhere Work IQ exists (Microsoft Copilot Copilot Cowork, Copilot Studio, coding agents)—for everyone: users, makers, and pro developers. 

- Understands how your business operates. Business Applications in Work IQ brings semantic understanding of your business processes via auto-generated semantic models and configurable business skills. 

- Work IQ is extensible by using MCP, CLI, or the Work IQ plugin for Coding Agents.

:::image type="content" source="media/business-applications-in-work-iq/work-iq-and-data.png" alt-text="Productivity and business data in Work IQ" lightbox="media/business-applications-in-work-iq/work-iq-and-data.png":::

## Choose how to use business context

Choose the connection based on the experience you're building and the data boundary you need.

| Option | Use it when | Scope and configuration |
|---|---|---|
| Microsoft Copilot and Copilot Cowork | People need business context in a Microsoft 365 work experience. | Administrators configure the Microsoft 365 audience. Power Platform administrators and makers configure participating environments and apps. |
| Work IQ MCP | An agent or coding client needs Microsoft 365 and supported business applications context through one MCP server. | Administrators control availability for the entire Work IQ MCP server. Environment, app, and data permissions still determine accessible business context. |
| Dataverse MCP | An agent needs direct, environment-specific Dataverse tools or business skills without the broader Work IQ context layer. | Configure and authorize the Dataverse MCP server for each environment that the client uses. |
| Dataverse Ask API | Application code needs a response grounded in a selected Dataverse semantic model. | The request targets a Dataverse environment and semantic model. |
| Dataverse plugin for coding agents | A coding agent needs Dataverse development guidance and tools while building a solution. | Install and configure the plugin in the coding environment. This option is for solution development, not end-user business-data grounding. |

These options can coexist with other enterprise data sources. You don't need to move every data source into Dataverse. Connect each source through an appropriate tool or service, and use the agent or application as the orchestration layer when the scenario spans multiple systems.

> [!NOTE]
> Work IQ MCP doesn't currently provide a retrieval-only parameter that bypasses response generation. If your architecture needs deterministic retrieval, use the source API or another targeted integration where available.

## Business Applications in Work IQ and existing apps

After you enable Business Applications in Work IQ, you can use it across existing app infrastructures, including Microsoft-provided apps like Dynamics 365 Sales or Dynamics 365 Service, and custom model-driven apps. Business Applications in Work IQ natively integrates into existing apps to provide enhanced functionality with little to no user input.

As new features become available in Business Applications in Work IQ, they integrate with the existing infrastructure.

## Supported line-of-business data

The following table lists the supported types of line-of-business data available in Business Applications in Work IQ.

| System of record | Description |
|---|---|
| Dynamics 365 ERP (preview) | Bring the data, business logic, and business skills of Dynamics 365 finance and operations apps into Work IQ, <br>Learn more: [Dynamics 365 ERP in Work IQ](/dynamics365/fin-ops-core/dev-itpro/copilot/erp-in-work-iq) |
| Dynamics 365 Customer Service | Access Customer Service MCP tools through Business Applications in Work IQ. <br>Learn more: [Overview of Dynamics 365 Customer Service MCP tools](/dynamics365/customer-service/develop/mcp-tools-overview) |
| Dynamics 365 Sales | Access Sales MCP tools through Business Applications in Work IQ. <br>Learn more: [MCP tools and skills support](/dynamics365/sales/ai-agent-overview#mcp-tools-and-skills-support) |
| Power Apps model-driven apps | Reason over and work with data from model-driven apps using Business Applications in Work IQ. <br>Learn more: [Use Business Applications in Work IQ](/power-apps/user/use-business-apps-work-iq) |

## Core capabilities

Business Applications in Work IQ core capabilities include business skills and semantic model.

### Business skills

Business skills let you define reusable business context that helps makers, users, and agents interpret data, follow processes, and make decisions. You define a skill once and reuse it across agents. For more information, see [Business skills overview](data-platform-business-skill-overview.md).

### Semantic model

The semantic model provides AI agents and Copilot experiences with a shared, business-aware understanding of your Dataverse data. For more information, see [Overview of Dataverse semantic model](semantic-model-overview.md).

## Use Business Applications in Work IQ

Information workers can query and reason over business data in natural language through the flow of their work with Microsoft Copilot. The following table lists the Copilot experiences currently supported as entry points to using Business Applications in Work IQ.

| Copilot experience | Description |
|---|---|
| Copilot Chat | Users can query, synthesize, and analyze line-of-business data in natural language conversation with Copilot and installed agents, once enabled by an administrator. <br>Learn more: [Set Up Business Applications in Work IQ](/power-platform/admin/business-applications-work-iq/quickstart?toc=/power-platform/business-applications-work-iq/toc.json&bc=/power-platform/breadcrumb/TOC.json) |
| Copilot Cowork (preview) | Users can collaborate with Cowork in real-time within their workflow, leveraging Business Applications in Work IQ to access and reason over business data. <br>Learn more: [Use the Business Applications in Work IQ plugin in Cowork](/microsoft-365/copilot/cowork/cowork-work-iq)|
| MCP tools  | Business applications MCP tools provide a standardized tool surface that enables AI clients such as Cowork, Copilot Studio, and coding agents to consistently discover, reason over, and execute work across business applications. <br> Learn more: [Work IQ MCP Tool reference](/microsoft-365/copilot/extensibility/work-iq/mcp/tool-reference) |

## Build agents that integrate with Business Applications in Work IQ

Build on existing business understanding and skills, and reuse it across the agents you build. The following table lists the agent building tools you can use to integrate your agents with Business Applications in Work IQ.

| Agent building tool | Description |
|---|---|
| Agent Builder in Copilot | Provide the agents you build with business context across your line-of-business systems. <br>Learn more: [Add Dynamics 365 and Power Apps data as a knowledge source](/microsoft-365/copilot/extensibility/agent-builder-add-knowledge#dynamics-365-and-power-apps-data) |
| Copilot Studio | Add business context from Work IQ to Copilot Studio agents built with the Microsoft Copilot harness. <br>Learn more: [Work IQ in Copilot Studio](/microsoft-copilot-studio/agents-experience/add-work-iq) |
| Microsoft Foundry | Connect Microsoft Foundry agents to your business data through the Work IQ MCP endpoint. <br>Learn more: [Connect agents to Microsoft 365 with Work IQ](/azure/foundry/agents/how-to/tools/work-iq#call-the-work-iq-mcp-endpoint)|
| GitHub Copilot | Install the Work IQ plugin for GitHub Copilot to query and reason over your business data. <br>Learn more: [Connect GitHub Copilot CLI to the Work IQ MCP server](/microsoft-365/copilot/extensibility/work-iq/mcp/quickstart/github-copilot-cli) |
| Other coding agents | Connect to Work IQ CLI through either CLI mode or MCP server mode. <br>Learn more: [Microsoft Work IQ CLI](/microsoft-365/copilot/extensibility/work-iq/cli) |

Additionally, you can use the [Dataverse plugin for coding agents](/power-apps/developer/data-platform/agents-plugin?toc=/power-platform/business-applications-work-iq/toc.json&bc=/power-platform/breadcrumb/TOC.json) alongside Work IQ to code business needs into consistent actions using Dataverse, or call the [Dataverse Ask API](/power-apps/developer/data-platform/ask?toc=/power-platform/business-applications-work-iq/toc.json&bc=/power-platform/breadcrumb/TOC.json) directly.

## Licensing

For information and terms for Work IQ licensing, see [Licensing requirements](/microsoft-365/copilot/extensibility/work-iq/api-overview#licensing-requirements).

## Prerequisites

Power Platform administrators must enable Work IQ in the environments that provide business context. AI administrators manage Microsoft Copilot and Work IQ MCP availability, and makers manage model-driven app participation. For more information, see [Set up Business Applications in Work IQ](/power-platform/admin/business-applications-work-iq/quickstart).

## Next steps

[Create and use business skills (preview)](data-platform-business-skills.md)

[Fine-tune semantic model signals (preview)](fine-tune-semantic-model-signals.md)
