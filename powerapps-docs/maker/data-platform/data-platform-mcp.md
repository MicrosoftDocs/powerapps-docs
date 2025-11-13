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
<!-- What is AIB in the table below? It's mentioned several times w/out any spelling out or explanation.-->
<!-- Below in the read_query row "simple call" is stated? What does that mean?-->
<!-- In the Search row what do you mean by version 1 and version 2?-->
<!-- The previous table of tools had Fetch. The new table you have has this identified as "post GA." Should it be included here? -->
| Tool | Description | Categorization (tools and resources) | API call type | Feature name | Metadata | Copilot credits |
|------|------------------|------------------------------------|----------------|--------------|----------|---------------------------|
| create_record | Inserts a new row into a Dataverse table and returns the GUID. | Tool | Basic | Text and generative AI tools (basic) per 10 response. | Dataverse MCP Tools – create_record | 0.1 |
| describe_table | Retrieves the T-SQL schema of a specified table. | Tool | Basic | Text and generative AI tools (basic) per 10 response | Dataverse MCP Tools – describe_record | 0.1 |
| execute_prompt | Executes a selected prompt using the required input structure. This call also invokes AIB prompt which has its own AIB prompt billing meter. | Tool | Basic + AIB cost | Text and generative AI tools (basic) per 10 response | Dataverse MCP Tools – execute_prompt | 0.1 + AIB cost |
| list_prompts | Lists all predefined prompts available in the environment. | Tool (LLM based) | Basic | Text and generative AI tools (basic) per 10 response. | Dataverse MCP Tools – list_prompts | 0.1 |
| list_tables | Lists all tables in the Dataverse environment. | Tool | Basic | Text and generative AI tools (basic) per 10 response | Dataverse MCP Tools – list_tables | 0.1 |
| read_query | Executes SELECT queries to fetch data from Dataverse.<br>It is Read multiple but simple call <!-- --> | Tool | Basic | Text and generative AI tools (basic) per 10 response | Dataverse MCP Tools – read_query | 0.1 |
| update_record | Updates an existing row in a Dataverse table. | Tool | Basic | Text and generative AI tools (basic) per 10 response | Dataverse MCP Tools – update_record | 0.1 |
| Create Table | Creates a new table with a specified schema. | Tool | Basic | Text and generative AI tools (basic) per 10 response | Dataverse MCP Tools – create_table | 0.1 |
| Update Table | Modifies schema or metadata of an existing table. | Tool | Basic | Text and generative AI tools (basic) per 10 response | Dataverse MCP Tools – update_table | 0.1 |
| Delete Table | Deletes a table from Dataverse. | Tool | Basic | Text and generative AI tools (basic) per 10 response | Dataverse MCP Tools – delete_table | 0.1 |
| Delete Record | Deletes a row from a Dataverse table. | Tool | Basic | Text and generative AI tools (basic) per 10 response | Dataverse MCP Tools – delete_record | 0.1 |
| Search | Searches through keywords over Dataverse for specific record. | Index based search tool | Premium | Version 1 searches for keyword, Version 2 is for knowledge retrieval | Tenant grounding<br>Dataverse MCP Tools – search | 10 |


<!-- Old table to be removed

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
-->
## Next steps

[Configure the Dataverse MCP server for an environment](data-platform-mcp-disable.md)
