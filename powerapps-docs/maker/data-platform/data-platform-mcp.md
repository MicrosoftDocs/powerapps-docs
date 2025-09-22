---
title: Connect to Dataverse with model context protocol (MCP)
description: Step-by-step instructions for setup, connect, and use Microsoft Dataverse with a model context protocol server. 
author: sabinn-msft
ms.component: cds
ms.topic: how-to
ms.date: 09/22/2025
ms.subservice: dataverse-maker
ms.author: sabinn
ms. reviewer: matp
contributors: MsSQLGirl
search.audienceType: 
  - maker
---
# Connect to Dataverse with model context protocol (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

The Model Context Protocol (MCP) is an open protocol that enables seamless integration between LLM applications and external data sources and tools. Microsoft Dataverse can act as an MCP server, providing intelligent access to tables and records to various MCP clients like Copilot Studio agents, Visual Studio (VS) Code GitHub Copilot, Claude desktop, and many others. This integration standardizes and streamlines the interaction between AI models and Dataverse data, making it more efficient and effective for developers to apply Dataverse's rich data capabilities within their AI-driven applications.  

Once connected to the Dataverse MCP Server, you can choose from various tools in the Power Platform environment. These tools are: list tables, describe table, read data, create record, update record, list prompts, execute prompt, list knowledge sources, and retrieve knowledge.

A Power Platform environment with Dataverse can have one MCP server.

This article explains how to set up and use the Dataverse MCP server with Microsoft Copilot Studio, Claude desktop, or Visual Studio Code (VS Code) GitHub Copilot as an MCP client. By following the steps in this article, you can interact with Dataverse, asking natural language questions like "show me my contacts" and receive answers based on stored data.

[!INCLUDE [preview-note-pp.md](../../../shared/preview-includes/preview-note-pp.md)]

## Prerequisites

- Power Platform administrator role in order to manage environment settings, environment group, and connector policies.
- To use this feature the environment be a Managed Environment.
- By default, the Dataverse MCP server is disabled for environments. You must enable it in the Power Platform admin center before you can connect to it. More information: [Enable the Dataverse MCP server (preview)](data-platform-mcp-disable.md#enable-the-dataverse-mcp-server)
- The Power Platform with Dataverse environment must be setup with the MCP via connector as described in this article.

## Connect to Dataverse using an MCP server in Microsoft Copilot Studio

1. Go to [Power App](https://make.powerapps.com) and select your environment from the top right environment selector.
1. From the left navigation pane, select **Agents** > **Create new agent**. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Select **Create**.
1. Scroll down to the **Tools** section and select **+ Add tool**.
1. Select **Model Context Protocol**, and then select **Dataverse MCP Server**.
   1. If there's no existing Dataverse connection, you're prompted to do so.
1. Select **Add to agent**.

The individual tools available on this MCP server can be viewed and modified by selecting **...** > **Edit** next to the **Dataverse MCP Server** tool.

You can now interact with the Dataverse MCP Server tool in the **Test your agent** chat pane. Try commands like "list tables in Dataverse," "describe table account," or "how many accounts do I have."
:::image type="content" source="media/copilot-studio-mcp.png" alt-text="Dataverse MCP in Copilot Studio" lightbox="media/copilot-studio-mcp.png":::

## Connect to Dataverse using an MCP Server with Claude or GitHub Copilot in VS Code

### Prerequisites to connect

These are the prerequisites for using a Dataverse MCP Server with Claude or GitHub Copilot in VS Code:

1. [Create a Dataverse connection for the MCP configuration](#create-a-dataverse-connection-for-the-mcp-configuration)
1. [Install the Dataverse MCP server local proxy](#install-the-dataverse-mcp-server-local-proxy)
1. [Get the tenant ID of your Dataverse environment](#get-the-tenant-id-of-your-dataverse-environment)

Connecting to Dataverse with an MCP Server in Copilot Studio doesn't require any of these prerequisites.

### Create a Dataverse connection for the MCP configuration

1. Go to [Power Automate](https://make.powerautomate.com). If necessary, change to the correct environment by selecting it from the top right.
1. Select **Connections** on the left navigation pane, and then select **+ New connection** on the command bar.
1. Type *Dataverse* in the search box, and then select the green colored **Microsoft Dataverse** connector.
   :::image type="content" source="media/power-automate-connector.png" alt-text="Dataverse connector":::
1. Complete the instructions on your screen.
1. Note the user name in the connection **Name**, this should be the same name that you used to create the environment earlier.
1. Select the connection to open it and copy the entire URL from the browser and save it. You need this URL for Claude desktop and VS Code MCP configuration.
   :::image type="content" source="media/copy-entire-browser-url.png" alt-text="Copy entire browser URL" lightbox="media/copy-entire-browser-url.png":::

### Install the Dataverse MCP server local proxy

These steps install the Dataverse MCP server local proxy that is used by the MCP client, such as Claude desktop or VS Code GitHub Copilot.

1. Install the .NET SDK 8.0 either from Downloads or with this PowerShell command.

   `winget install Microsoft.DotNet.SDK.8`

1. In the Terminal window you opened earlier, run this command to install the Microsoft.PowerPlatform.Dataverse.MCP local proxy.

   `dotnet tool install --global --add-source https://api.nuget.org/v3/index.json Microsoft.PowerPlatform.Dataverse.MCP`

### Get the tenant ID of your Dataverse environment

When you configure the Dataverse MCP server for either Claude Desktop or VS Code GitHub, you need to provide the `TenantID` value.

Here’s one of the ways to get tenant ID details:

1. Go to https://make.powerapps.com.
1. Select **Settings** (gear icon) on the top right, and then select **Session details**.
1. Copy the value of the **Tenant ID** from the Power Apps session details. Make a note of this GUID because it's used in the configuration steps later.  

### Configure and use the Dataverse MCP server in Claude

Claude AI is a large language model (LLM) and chatbot developed by Anthropic. It excels at natural language processing and is multimodal, meaning it can process text, audio, and visual inputs. Claude can answer questions, summarize documents, generate text, and even create diagrams, animations, and code.

#### Download Claude desktop

If you haven't already done so, download and install Claude desktop [Download - Claude](https://claude.ai/download). 

Once you have Claude desktop installed, you can find and launch Claude from your desktop.

#### Configure Dataverse MCP server in Claude desktop

1. Open Claude desktop and go to **File** > **Settings**.
1. If you haven't configured any MCP servers for Claude desktop previously, you observe a **Settings** dialog. Select **Edit Config**.
1. This takes you to the Claude desktop files. Open the **claude_desktop_config.json** file with your favorite JSON editor.
1. Replace &lt;connection URL&gt; and &lt;Tenant Id&gt; with your connection URL and tenant ID. More information: [Create a Dataverse connection for the MCP configuration](#create-a-dataverse-connection-for-the-mcp-configuration) and [Get the tenant ID of your Dataverse environment](#get-the-tenant-id-of-your-dataverse-environment)
   
   Use a &lt;friendly name&gt; for your Dataverse MCP server that you can easily remember, for example: *MyDataverseMCPServer*. 

```json
{
     "mcpServers": {
    "<friendly name>": {
      "command": "Microsoft.PowerPlatform.Dataverse.MCP",
      "args": [
        "--ConnectionUrl",
        "<URL for Dataverse connection>",
        "--MCPServerName",
        "DataverseMCPServer",
        "--TenantId",
        "<Tenant Id GUID>",
        "--EnableHttpLogging",
        "true",
        "--EnableMsalLogging",
        "false",
        "--Debug",
        "false",
        "--BackendProtocol",
        "HTTP"
         ]
       }
     }
   }
```

5. Save this file and go back to Claude desktop.
6. To restart Claude desktop and ensure that the changes take effect, select **File** > **Exit**.
7. Open Claude desktop now that the Dataverse MCP server configuration is completed from the previous step. You need to use your credentials to sign in to your Dataverse environment.  
8.	Verify that you can view the Dataverse MCP server and the tools by selecting **Search and tools**. You should be able to observe your friendly name of Dataverse MCP Server, *MyDataverseMCPServer* for example.

   :::image type="content" source="media/claude-connected-data-platform.png" alt-text="Claude connected to Dataverse":::
9. Selecting the MCP server (*MyDataverseMCPServer*) allows you to view the list of tools, supported by that MCP server. 

> [!TIP]
> You can enable and disable individual tools for each MCP server registered with Claude. This gives you control over what tools to use.

#### Interact with Dataverse MCP server in Claude desktop

If you have  data in the Dataverse environment, you can start testing your setup by asking “list tables in Dataverse,” “describe table account,” or “how many accounts do I have,” and so on. More information: [Add and remove sample data](/power-apps/developer/data-platform/sample-data)

> [!TIP]
> If you have other MCP servers registered with Claude, it’s best to add *in Dataverse* in your prompt to be specific about which MCP server you’d like to use.

### Configure and use your MCP client with VS Code

This section shows you how to configure your MCP server in two ways in VS Code GitHub Copilot: reusing Dataverse MCP server configuration that you have defined for Claude desktop or creating a new Dataverse MCP configuration for your VS Code GitHub Copilot.

If you don’t have VS Code installed, [download Visual Studio Code - Mac, Linux, Windows](https://code.visualstudio.com/download).

#### Reuse Claude Desktop configuration

1. In VS Code, open the command palette using Ctrl+Shift+P or **View** > **Command Palette**. Type *MCP:* and a list of relevant MCP commands are displayed, such as MCP: List Servers and MCP: Add Servers.  
1. If you have configured the Dataverse MCP server as described earlier in the [Claude desktop](#configure-and-use-the-dataverse-mcp-server-in-claude) step and your VS Code MCP setting is set as `"chat.mcp.discovery.enabled": true`, VS Code is able to discover it. For example, when you choose **MCP: List Servers**, the MCP server, such as **MyDataverseMCPServer Running**, is displayed.
   :::image type="content" source="media/mcp-server-running.png" alt-text="MCP Dataverse server running":::

   If the Dataverse MCP server isn't running, select the server and then select **Start Server**. Observe the server start in the **Output** window of VS Code.

#### Configure the Dataverse MCP server in VS Code

These instructions help you configure a Dataverse MCP server at the user setting level.

1. In VS Code, open the command palette by selecting **View** > **Command Palette** (Ctrl + Shift + P).
1. Type *MCP: Open User Configuration*, and then select it.
1. Copy and paste this Dataverse MCP configuration JSON inside the mcp "servers" node following the curly brace.

   ```json
   "<friendly name>": {
   "command": "Microsoft.PowerPlatform.Dataverse.MCP",
   "args": [
     "--ConnectionUrl",
     "<URL you copied from the screen with connection at make.powerautomate.com>",
     "--MCPServerName",
     "DataverseMCPServer",
     "--TenantId",
     "<GUID you copied from Tenant ID value of Settings at make.powerapps.com>",
     "--EnableHttpLogging",
     "true",
     "--EnableMsalLogging",
     "false",
     "--Debug",
     "false",
     "--BackendProtocol",
     "HTTP"
    ]
   }
   ```

   :::image type="content" source="media/mcp-dataverse-json.png" alt-text="JSON snippet location for MCP Dataverse" lightbox="media/mcp-dataverse-json.png":::
1. In the mcp.json file where you pasted in the json in the previous step, replace &lt;connection URL&gt; and &lt;tenant ID&gt; from the [prerequisite steps](#prerequisites). Use a &lt;friendly name&gt; for your Dataverse MCP server that you can easily remember, for example: `MyDataverseMCPServerForGitHubCopilot`.
1. Select **File** > **Save**.

> [!NOTE]
> When the MCP server is configured correctly in mcp.json, you notice a status like **Start**. This means that syntactically, it's correct and you can start the MCP server. In case it doesn’t show **Start**, you can go to **Command Palette** (Ctrl+Shift+P), type *MCP:* and then select **MCP: List Servers**. You should observe the friendly name that you have assigned for the Dataverse MCP server so you can start the MCP server.

#### Interact with Dataverse MCP server in VS Code GitHub Copilot

1. In VS Code, open GitHub Copilot in Agent mode. Use CTRL+ALT+I to launch GitHub Copilot chat in VS Code.
1. From this point on, you can interact with the MCP server via Agent mode of GitHub Copilot. For example, “list tables in Dataverse,” “describe table account,” or “how many accounts do I have,” and so on.

> [!TIP]
> If you have other MCP servers registered with GitHub Copilot, there are a few ways to help MCP Client to choose the appropriate MCP Server. Examples:
> * add "in Dataverse" to your prompt to be specific about which MCP server you’d like to use for your question, or
> * at the beginning of the session, you can say "Use `<insert your MCP server name>` for this session."  

For more resources about how to use GitHub Copilot in VS Code:

- [GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/overview) 
- [Get started with GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/getting-started)
- [Getting started with Copilot Chat in VS Code](https://code.visualstudio.com/docs/copilot/chat/getting-started-chat)

To learn how to use Visual Studio Code and MCP Severs go to this document: [Use MCP servers in VS Code (Preview)](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)

## List of tools available in Dataverse MCP server

The following Dataverse MCP tools are available. Your prompt in the MCP client like Claude desktop and VS Code GitHub Copilot is automatically routed to one or more of these tools. So you can ask a question like "view Accounts data," which is likely be mapped to the `read_query` tool or `retrieve_knowledge`.  

## Dataverse tool reference

This table provides an overview of commonly used tools in Dataverse, organized by functionality.

| Tool                    | Description                                                                                                                  |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------|
| `create_table`          | Creates a new table in Dataverse with specified columns and data types.                                                      |
| `update_table`          | Modifies the structure of an existing table, such as adding or removing columns.                                             |
| `delete_table`          | Permanently deletes a table from Dataverse.                                                                                  |
| `describe_table`        | Retrieves the schema of a specified table in Dataverse, including column names and data types.                              |
| `list_tables`           | Returns a list of tables accessible in the current environment.                                                              |
| `create_record`         | Inserts a new row into a Dataverse table and returns the GUID of the created row.                                            |
| `read_query`            | Reads and retrieves data from tables in Dataverse based on query parameters.                                                 |
| `update_record`         | Updates an existing row in a Dataverse table.                                                                                |
| `delete_record`         | Removes a specific row from a Dataverse table using its unique identifier or a condition.                                    |
| `list_knowledge_sources`| Lists all knowledge sources available in Dataverse, including those used in Copilot Studio agents within the same environment.|
| `retrieve_knowledge`    | Uses a configured knowledge source to answer user questions.                                                                 |
| `execute_prompt`        | Runs a predefined prompt available in the current environment.                                                               |
| `list_prompts`          | Displays all predefined prompts available in the environment.                                                                |

## Related articles

[Disable a Dataverse MCP server using advanced connector policies](data-platform-mcp-disable.md)

Learn more about MCP:

- [Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)
- [Anthropic and Introduction - Model Context Protocol](https://modelcontextprotocol.io/introduction)
