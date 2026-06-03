---
title: Connect to Dataverse with model context protocol (MCP)
description: Step-by-step instructions for setup, connect, and use Microsoft Dataverse with a model context protocol server. 
author: ShefaaliP
ms.component: cds
ms.topic: how-to
ms.date: 05/26/2026
ms.subservice: dataverse-maker
ms.author: spatankar
ms.reviewer: matp
contributors: 
- MsSQLGirl
- seanwat-msft
- kewear
search.audienceType: 
  - maker
---
# Connect to Dataverse with Model Context Protocol

The Model Context Protocol (MCP) is an open protocol that enables seamless integration between large language model (LLM) applications and external data sources and tools. Microsoft Dataverse can act as an MCP server, providing intelligent access to tables and records to various MCP clients like Copilot Studio agents, Visual Studio (VS) Code GitHub Copilot, GitHub Copilot CLI, Claude desktop, Claude Code, and many others. This integration standardizes and streamlines the interaction between AI models and Dataverse data, making it more efficient and effective for developers to apply Dataverse's rich data capabilities within their AI-driven applications.

To use Dataverse as an MCP server, you need to enable and configure the MCP server and allowed clients for your Power Platform environment. Once configured, you can connect to the Dataverse MCP server using different MCP clients. More information: [Configure the Dataverse MCP server for an environment](data-platform-mcp-disable.md)

### Dataverse MCP server URL

The Dataverse MCP remote server URL follows this format:

`https://{dataverseOrgName}.crm.dynamics.com/api/mcp`

For example, if your Dataverse organization name is `contoso`, the MCP server URL is:

`https://contoso.crm.dynamics.com/api/mcp`

## Connect to a Dataverse MCP server

There are multiple ways to connect to a Dataverse MCP server:

- Microsoft Copilot Studio. To learn how to connect to MCP through Dataverse MCP go to [Connect to Dataverse with model context protocol in Microsoft Copilot Studio](data-platform-mcp-copilot-studio.md).
- Visual Studio GitHub Copilot and Copilot CLI. To learn how to connect to GitHub Copilot in Visual Studio Code or Copilot CLI go to [Connect Dataverse MCP with GitHub Copilot in Visual Studio Code and Copilot CLI](data-platform-mcp-vscode.md).
- Non-Microsoft clients such as Claude desktop and Claude Code. To learn how to connect through Dataverse MCP go to [Connect Dataverse MCP with non-Microsoft clients](data-platform-mcp-other-clients.md).

## List of tools

Once connected to the Dataverse MCP Server, you can choose from the following tools in the Power Platform environment.

| Tool | Description |
|------|-------------|
| `search_data` | Search structured and unstructured data. |
| `search` | Search table schemas and business skills by keyword. |
| `create_record` | Inserts a new row into a Dataverse table and returns the GUID. |
| `update_record` | Updates an existing row in a Dataverse table. |
| `delete_record` | Delete a row, only after explicit user approval. |
| `create_table` | Creates a new table with a specified schema. |
| `update_table` | Modifies schema or metadata of an existing table. |
| `delete_table` | Deletes a table from Dataverse, only after explicit user approval. |
| `read_query` | Run supported Dataverse SQL `SELECT` queries. |
| `describe` | Get details from search results for tables, records, schemas, skills, and apps. |
| `upsert_skill` | Add or update a Dataverse skill/playbook. | 
| `delete_skill` | Delete a Dataverse skill/playbook by name. | 
| `init_file_upload` | Generate a SAS URL for file upload. |
| `commit_file_upload` | Commit a file upload. |
| `file_download` | Generate a SAS URL for file download. |

> [!IMPORTANT]
> The Dataverse MCP server tool surface is changed. The following tools were removed and their functionality replaced by the tools in the preceding table: `describe_table`, `list_tables`, and `fetch` (replaced by `describe`); and the previous `search` tool that searched Dataverse data (renamed to `search_data`). The current `search` tool searches metadata. If you maintain allow or deny lists in your MCP client by tool name, review your configuration so that the new tool names reflect your intended permissions. More information: [Connect to Dataverse with model context protocol FAQ](data-platform-mcp-faq.md)

> [!NOTE]
> Starting December 15, 2025 Dataverse MCP tools are charged when accessed by AI agents created outside of Microsoft Copilot Studio. If you have Dynamics 365 Premium licenses (such as Dynamics 365 Sales Premium, Finance Premium, Supply Chain Premium, and Customer Service Premium) or a Microsoft 365 Copilot User Subscription License (USL), you aren't charged for accessing Dynamics 365 data, even when that data is accessed from outside Microsoft Copilot Studio.

The `search_data` tool is billed at the same Copilot Credit rate as Tenant graph grounding. All other tools, including the metadata `search` tool, follow the Text and generative AI tools (basic) per 10 response Copilot credit rate. For information about Copilot billing, go to [Billing rates and management](/microsoft-copilot-studio/requirements-messages-management).

## Next steps

[Configure the Dataverse MCP server for an environment](data-platform-mcp-disable.md)
