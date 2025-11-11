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

There are multiple ways to connect to a Dataverse MCP server:

- Microsoft Copilot Studio. To learn how to connect to MCP through Dataverse MCP go to [Connect to Dataverse with model context protocol in Microsoft Copilot Studio](data-platform-mcp-copilot-studio.md).
- Visual Studio GitHub Copilot. To learn how to connect to GitHub Copilot in Visual Studio Code go to [Connect Dataverse MCP with GitHub Copilot in Visual Studio Code](data-platform-mcp-vscode.md).
- Non-Microsoft clients such as Claude. To learn how to connect to Claude through Dataverse MCP go to [Connect Dataverse MCP with non-Microsoft clients](data-platform-mcp-other-clients.md).

## Prerequisites

- Power Platform administrator role in order to manage environment settings, environment group, and connector policies.
- To use this feature the environment must be a Managed Environment.
- By default, the Dataverse MCP server is disabled for environments. You must enable it in the Power Platform admin center before you can connect to it. More information: [Enable the Dataverse MCP server](data-platform-mcp-disable.md)
- The Power Platform with Dataverse environment must be set up with the MCP via connector as described in this article: [Enable the Dataverse MCP server for an environment](data-platform-mcp-disable.md)

## List of tools available in Dataverse MCP server

Once connected to the Dataverse MCP Server, you can choose from various tools in the Power Platform environment.

| Tool          | Description                                                                    |
|---------------|--------------------------------------------------------------------------------------|
| `create_record` | Inserts a new row into a Dataverse table and returns the GUID.                       |
| `describe_table`| Retrieves the T-SQL schema of a specified table.                                    |
| `list_tables`   | Lists all tables in the Dataverse environment.                                      |
| `read_query`    | Executes SELECT queries to fetch data from Dataverse.                               |
| `update_record` | Updates an existing row in a Dataverse table.                                       |
| `Create Table`  | Creates a new table with a specified schema.                                        |
| `Update Table`  | Modifies schema or metadata of an existing table.                                   |
| `Delete Table`  | Deletes a table from Dataverse.                                                     |
| `Delete Record` | Deletes a row from a Dataverse table.                                               |
| `Search`        | Searches through keywords over Dataverse for specific record                        |
| `Fetch`         | Retrieves full content of a record in Dataverse using table name and ID          |

## Related articles

[Disable a Dataverse MCP server using advanced connector policies](data-platform-mcp-disable.md)

Learn more about MCP:

- [Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)
- [Anthropic and Introduction - Model Context Protocol](https://modelcontextprotocol.io/introduction)
