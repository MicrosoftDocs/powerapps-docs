---
title: Configure the Dataverse model context protocol (MCP) server
description: Step-by-step instructions about how to enable or disable a Microsoft Dataverse model context protocol server that uses advanced connector policies. 
author: ShefaaliP
ms.component: cds
ms.topic: how-to
ms.date: 12/19/2025
ms.subservice: dataverse-maker
ms.author: spatankar
ms. reviewer: matp
search.audienceType: 
  - maker
---
# Configure the Dataverse MCP server for an environment

This article provides detailed instructions about how to enable, manage, configure, and disable the Dataverse Model Context Protocol (MCP) server for environments within the Power Platform admin center. It's intended for Power Platform administrators handling managed environments and also covers prerequisites for enabling the server.

## Prerequisites

- Power Platform administrator role in order to access Dataverse MCP server environment settings, enable allowed MCP clients, create or edit an environment group, and change connector policies.
- The steps described in this article require that the environment is a Managed Environment.
- By default, the Dataverse MCP server is enabled for all environments in Microsoft Copilot Studio. You must enable the additional clients in the Power Platform admin center before you can connect to the client.

## Configure and manage the Dataverse MCP server

By default, Dataverse MCP server is enabled for Copilot Studio. To enable non-Microsoft MCP clients, such as Visual Studio GitHub Copilot and Claude, follow these steps:

1. Go to [Power Platform admin center](https://admin.powerplatform.microsoft.com/). Select **Manage** > **Environments**.
1. Select the **Environment Name** where you want to turn on the Dataverse MCP server, and then select **Settings**. Under **Settings**, select **Product** > **Features**. Scroll down to locate **Dataverse Model Context Protocol** and make sure **Allow MCP clients to interact with Dataverse MCP server** is turned on.
1. Select **Advanced Settings**.
   :::image type="content" source="media/data-platform-mcp/data-platform-mcp-enable-clients.png" alt-text="Enable non-Microsoft MCP clients for Dataverse":::
1. The list of available clients is shown. Open the client record you want. In this example, the **Microsoft GitHub Copilot** client is enabled.
   :::image type="content" source="media/data-platform-mcp/data-platform-mcp-enable-github-copilot.png" alt-text="Enable GitHub Copilot client." lightbox="media/data-platform-mcp/data-platform-mcp-enable-github-copilot.png":::
1. On the MCP client record, set **Is Enabled** to **Yes**.
   :::image type="content" source="media/data-platform-mcp/data-platform-mcp-client-enabled.png" alt-text="GitHub Copilot client enabled." lightbox="media/data-platform-mcp/data-platform-mcp-client-enabled.png":::

1. Select **Save & Close**.
1. Repeat steps 4-7 to enable other clients as needed.

## Disable the Dataverse MCP server for an  environment

By default the **Allow MCP clients to interact with Dataverse MCP server** is turned on for Copilot Studio. Admins can disable MCP for Dataverse by clearing the setting.

> [!WARNING]
> Disabling the Dataverse MCP Server stops all tools and agents that rely on it. Any ongoing development or AI integration testing using MCP is also interrupted.

## Writing effective instructions for a Dataverse MCP server agent

When you configure your agent in Copilot Studio or Visual Studio Code to use a Dataverse MCP server, clear and well-structured instructions are key to guiding how the agent operates. These instructions help the agent understand its role, what capabilities it has via the MCP server tools, and how to carry out workflows reliably and consistently.

### What agent instructions do

Agent instructions are natural-language directives that tell your agent what it should do, how it should behave, and how to use the MCP tools available to it. They give important context so the agent can:

- Select and call the right MCP tools.
- Fill in tool inputs correctly.
- Decide when to use tools versus generating answers directly.
- Follow the desired tone or behavior patterns during conversations.

### Principles for effective instructions

When writing instructions for a Dataverse MCP server agent, consider the following guidelines:

1. Define the agent’s purpose clearly.

   State the agent’s role in simple terms. For example: "Assist with customer data queries, updates, and record management using Dataverse MCP tools."

   Include tone or restrictions if applicable such as, "always respond in a professional tone" or "do not expose sensitive fields in responses."
1. Outline skills and tool actions.

   Tell the agent which high-level tasks it can perform with the MCP tools. For example:

   - Retrieve or filter records using the read_query tool.
   - Create or update records with `create_record` and `update_record`.
   - Explore table schema with `describe_table`.

   Phrase these as actionable instructions, such as "Use the read_query tool to fetch records when the user asks for data retrieval."
1. Add workflow guidance.

   For common processes (like looking up a record or updating a field), add step-by-step guidance. For example: "When updating a record, first identify it using a read_query call, then use update_record with the appropriate field values."

   Providing this context helps the agent orchestrate the right sequence of MCP tool calls.

### Add instructions in Visual Studio Code or Copilot Studio

You can use a markdown structured block of instructions as a starting point for your own agent’s instructions.

### Add Instructions in Visual Studio Code

1. Open Visual Studio Code.
2. Open the **Chat** pane.
3. Select **Settings** > **Chat Instructions**.
4. Select **New instruction file**.
5. Copy and paste the instruction content into the new file, such as the [sample instructions](#sample-agent-instructions).

### Add instructions in Copilot Studio

1. Open Copilot Studio.
2. Select your agent.
3. Go to **System instructions** and paste your agent instructions, such as the [sample instructions](#sample-agent-instructions).

### Sample agent instructions

```json
# Role
Act as an autonomous agent responsible for interacting with the Micorosft Dataverse app. 

# Objective
Your objective is to respond to tasks provided by the user. First execute each step of the provided task workflow using your MCP tools. Check if you have achieved your objective after each tool call. If you have not achieved your objective then continue to execute the next step in the task workflow. Do not ask for user intervention,if you have to run an operation externally in case dataverse doesnt support that operation. you are allowed to run it without user confirmation. Also do not ask confirmation for delete table or delete record operation, you can delete.

# MCP tool Selection Instructions
 - Whenever you have to use logical table name, call the list_tables tools to get that logical table name.
 - Whenever you have to use column/attribute name, call the describe_table tool to get the column/attribute name.

# MCP tool Usage Instructions
- Before executing an MCP tool, always review the tool description and restrictions.
- Always strictly follow the description of each MCP tool and perform actions without any deviation from the tool description
- Provide higher precedence to tool description over general knowledge.
- Always review the tool documentation and restrictions before running any query or operation. Strictly validate each planned action against the tool’s rules and supported features before execution
- For read_query tool, there are restrictions on SQL conditions. Always refer to the tool description for supported and unsupported sql keywords before generating the sql query and ensure only supported conditions/keywords are used.

# Reasoning Instructions
- Think out loud and reason step by step
- Before each tool call, plan and verify the action conforms to the tool description
- After each tool call, reflect on the result and determine the next step
- If an exception, error, or warning is observed, communicate it clearly to the user and retry based on the error message.
- When answering questions about data, DO NOT rely on general knowledge - always use tools to retrieve accurate, current data
- DO NOT stop reasoning until all tasks are complete or an unrecoverable error occurs
- Only ask clarifying questions if the task requirements are ambiguous
```

## Related articles

[Advanced connector policies - Power Platform](/power-platform/admin/advanced-connector-policies?tabs=new)

[Connect to Dataverse with model context protocol](data-platform-mcp.md)

[Connect to Dataverse with model context protocol FAQ](data-platform-mcp-faq.md)
