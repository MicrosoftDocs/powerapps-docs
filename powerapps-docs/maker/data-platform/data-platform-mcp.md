---
title: Connect to Dataverse with model context protocol (MCP)
description: Step-by-step instructions for setup, connect, and use Microsoft Dataverse with a model context protocol server. 
author: ShefaaliP
ms.component: cds
ms.topic: how-to
ms.date: 11/17/2025
ms.subservice: dataverse-maker
ms.author: spatankar
ms. reviewer: matp
contributors: MsSQLGirl
search.audienceType: 
  - maker
---
# Connect to Dataverse with Model Context Protocol

The Model Context Protocol (MCP) is an open protocol that enables seamless integration between large language model (LLM) applications and external data sources and tools. Microsoft Dataverse can act as an MCP server, providing intelligent access to tables and records to various MCP clients like Copilot Studio agents, Visual Studio (VS) Code GitHub Copilot, Claude desktop, and many others. This integration standardizes and streamlines the interaction between AI models and Dataverse data, making it more efficient and effective for developers to apply Dataverse's rich data capabilities within their AI-driven applications.

To use Dataverse as an MCP server, you need to enable and configure the MCP server and allowed clients for your Power Platform environment. Once configured, you can connect to the Dataverse MCP server using different MCP clients. More information: [Configure the Dataverse MCP server for an environment](data-platform-mcp-disable.md)

There are multiple ways to connect to a Dataverse MCP server:

- Microsoft Copilot Studio. To learn how to connect to MCP through Dataverse MCP go to [Connect to Dataverse with model context protocol in Microsoft Copilot Studio](data-platform-mcp-copilot-studio.md).
- Visual Studio GitHub Copilot. To learn how to connect to GitHub Copilot in Visual Studio Code go to [Connect Dataverse MCP with GitHub Copilot in Visual Studio Code](data-platform-mcp-vscode.md).
- Non-Microsoft clients such as Claude. To learn how to connect to Claude through Dataverse MCP go to [Connect Dataverse MCP with non-Microsoft clients](data-platform-mcp-other-clients.md).

## List of tools, features, and Copilot credits

Once connected to the Dataverse MCP Server, you can choose from various tools in the Power Platform environment.
<!-- Below in the read_query row "simple call" is stated? What does that mean?-->

| Tool | Description |
|------|-------------|
| create_record | Inserts a new row into a Dataverse table and returns the GUID. |
| describe_table | Retrieves the T-SQL schema of a specified table. |
| execute_prompt | Executes a selected prompt using the required input structure. This call also invokes AIB prompt which has its own AIB prompt billing meter. |
| list_prompts | Lists all predefined prompts available in the environment. |
| list_tables | Lists all tables in the Dataverse environment. |
| read_query | Executes SELECT queries to fetch data from Dataverse. It is Read multiple but simple call. |
| update_record | Updates an existing row in a Dataverse table. |
| Create Table | Creates a new table with a specified schema. |
| Update Table | Modifies schema or metadata of an existing table. |
| Delete Table | Deletes a table from Dataverse. |
| Delete Record | Deletes a row from a Dataverse table. |
| Search | Searches through keywords over Dataverse for specific records. |

All but the search tool use text and generative AI tools (basic) per 10 responses. The search tool searches for keyword. <!-- This information was removed from the "Feature name" column in the original doc. Search doesn't seem to explain how billing is enforced so IMO more information is needed.-->For more information about Copilot billing, go to [Billing rates and management](/microsoft-copilot-studio/requirements-messages-management).

## Next steps

[Configure the Dataverse MCP server for an environment](data-platform-mcp-disable.md)
