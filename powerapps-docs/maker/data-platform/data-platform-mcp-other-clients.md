---
title: Connect to Dataverse with model context protocol in non-Microsoft clients
description: Learn how to connect to Dataverse using the Model Context Protocol (MCP) server in non-Microsoft clients. Follow step-by-step instructions to enable seamless data interaction.
#customer intent: As a Power Apps maker, I want to connect to Dataverse using the Model Context Protocol server so that I can choose from different MCP clients that can interact with my data through natural language queries.
author: ShefaaliP
ms.author: spatankar
ms.reviewer: matp
ms.date: 11/10/2025
ms.topic: how-to
ms.collection: bap-ai-copilot
ms.subservice: dataverse-maker
---

# Connect to Dataverse with model context protocol in non-Microsoft clients

Connect to Microsoft Dataverse using a non-Microsoft model context protocol (MCP) client. This example describes how to connect using Claude.

## Prerequisites

These are the prerequisites for using a Dataverse MCP server with Claude.

- Enable the Dataverse MCP server for the environment through PPAC settings. More information: [Configure and manage the Dataverse MCP server for an environment](data-platform-mcp-disable.md#configure-and-manage-the-dataverse-mcp-server-for-an-environment)
- A Dataverse connection for the MCP configuration.
- Install the Dataverse MCP server local proxy.
- The tenant ID of your Dataverse environment.

> [!NOTE]
> Only Claude desktop is currently supported.

## Create a Dataverse connection for the MCP configuration

1. Go to Power Automate. If necessary, change to the correct environment by selecting it from the top right. 
1. Select **Connections** on the left navigation pane, and then select **+ New connection** on the command bar.
1. Type Dataverse in the search box, and then select the **Microsoft Dataverse** connector.
1. Complete the instructions on your screen.

   Make a note of the user name in the connection **Name**, this should be the same name that you used to create the environment earlier.

1. Select the connection to open it. Copy the URL from the browser and towards the end add *()* and save it. You need this URL for Claude desktop MCP configuration. <!--Need image of URL. The image resolution in the Word doc was too small to view the URL in your screenshot. Please add the screenshot to SharePoint so as to maintain higher resolution. Only the open and closed parentheses should be added? Also "towards the end" do you mean at the end of the URL. We need to be specific.-->

## Install the Dataverse MCP server local proxy

These steps install the Dataverse MCP server local proxy that is used by the MCP client, such as Claude desktop or VS Code GitHub Copilot.<!-- The local proxy steps aren't in the VS Code GitHub Copilot article. Shouldn't they be?-->

1. Install the .NET SDK 8.0 either from download or with this PowerShell command.

   `winget install Microsoft.DotNet.SDK.8`
1. In a Windows terminal window, run this command to install the Microsoft `PowerPlatform.Dataverse.MCP` local proxy.

   `dotnet tool install --global --add-source https://api.nuget.org/v3/index.json Microsoft.PowerPlatform.Dataverse.MCP`

## Get the tenant ID of your Dataverse environment

When you configure the Dataverse MCP server for either Claude Desktop or VS Code GitHub, you need to provide the `TenantID` value.

Here’s one way to get tenant ID details:

1. Go to [Power Apps](https://make.powerapps.com).
1. Select **Settings** (gear icon) on the top right, and then select **Session details**.
1. Copy the value of the **Tenant ID** from the **Power Apps session details** to the Windows clipboard. Make a note of this GUID because it's used in the configuration steps later.

## Configure and use the Dataverse MCP server in Claude

Claude AI is a large language model (LLM) and chatbot developed by Anthropic. It excels at natural language processing and is multimodal, meaning it can process text, audio, and visual inputs. Claude can answer questions, summarize documents, generate text, and even create diagrams, animations, and code.

### Download Claude desktop

If you haven't already done so, [download and install Claude desktop](https://claude.ai/download).

After you have Claude desktop installed, you can find and launch Claude from your desktop.

### Configure Dataverse MCP server in Claude desktop

1. Open Claude desktop and go to **File** > **Settings**.
1. If you haven't configured any MCP servers for Claude desktop previously, you observe a **Settings** dialog. Select **Edit Config**.
1.	The Claude desktop files displays. Open the `claude_desktop_config.json` file with your favorite JSON editor.
1. Replace &lt;connection URL&gt; and &lt;Tenant Id&gt; with your connection URL and tenant ID and paste the JSON snippet into the appropriate section of the file.
   More information: [Create a Dataverse connection for the MCP configuration](#create-a-dataverse-connection-for-the-mcp-configuration) and [Get the tenant ID of your Dataverse environment](#get-the-tenant-id-of-your-dataverse-environment)

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
 
### Verify and interact with the connection in Claude desktop

1. Restart Claude desktop and ensure that the changes take effect. Select **File** > **Exit**.
1. Open Claude desktop now that the Dataverse MCP server configuration is completed from the previous step. You need to use your credentials to sign in to your Dataverse environment.
1. Verify that you can view the Dataverse MCP server and the tools by selecting **Search and tools**. You should be able to observe your friendly name of Dataverse MCP server, *MyDataverseMCPServer* for example.
   :::image type="content" source="media/data-platform-mcp/claude-connected-data-platform.png" alt-text="Verify Claude desktop connection with Dataverse":::
1. Selecting the MCP server (*MyDataverseMCPServer*) allows you to view the list of tools, supported by that MCP server.

> [!TIP]
> You can enable and disable individual tools for each MCP server registered with Claude. This gives you control over what tools to use.

#### Interact with Dataverse MCP server in Claude desktop

If you have data in the Dataverse environment, you can start testing your setup by asking *list tables in Dataverse*, *describe table account*, or *how many accounts do I have*, and so on. More information: [Add and remove sample data](/power-platform/admin/add-remove-sample-data)

> [!TIP]
> If you have other MCP servers registered with Claude, it’s best to add in Dataverse in your prompt to be specific about which MCP server you’d like to use.

## Related articles

[Connect to Dataverse with Model Context Protocol](data-platform-mcp.md)