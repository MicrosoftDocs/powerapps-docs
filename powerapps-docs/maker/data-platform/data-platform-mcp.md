---
title: Connect to Dataverse with model context protocol (MCP)
description: Step-by-step instructions for set up, connect, and use Microsoft Dataverse with a model context protocol server. 
author: sabinn-msft
ms.component: cds
ms.topic: how-to
ms.date: 09/19/2024
ms.subservice: dataverse-maker
ms.author: sabinn
ms. reviewer: matp
search.audienceType: 
  - maker
---
# Connect to Dataverse with model context protocol (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

The Model Context Protocol (MCP) is an open protocol that enables seamless integration between LLM applications and external data sources and tools. Microsoft Dataverse can act as an MCP server, providing intelligent access to tables and records to various MCP clients like Copilot Studio agents, VSCode GitHub Copilot, Claude desktop, and many others. This integration standardizes and streamlines the interaction between AI models and Dataverse data, making it more efficient and effective for developers to leverage Dataverse's rich data capabilities within their AI-driven applications.  

Once connected to the Dataverse MCP Server, you can choose from a variety of tools in the Power Platform environment. These tools are: list tables, describe table, read data, create record, update record, list prompts, execute prompt, list knowledge sources, and retrieve knowledge.

This article explains how to set up and use the Dataverse MCP server with Claude Desktop or VS Code GitHub Copilot as an MCP client. By following the steps, you can interact with Dataverse, asking natural language questions like "show me my contacts" and receive answers based on stored data.

> [!IMPORTANT]
>
> - This is a preview feature.
> - [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]

## Prerequisites

During this preview, only a new Dataverse environment provisioned as outlined here works with the MCP server.  

After you create your environment for the preview, make a note of this information: 

- [User credentials that you are using](#create-a-new-first-release-dataverse-environment)
- [Environment name](#create-a-new-first-release-dataverse-environment)
- [Connection URL](#create-a-dataverse-connection-for-the-mcp-configuration)
- [Tenant ID](#get-the-tenant-id-of-your-dataverse-environment)

## Create a new first release Dataverse environment

1. Open a terminal or PowerShell console on your desktop in **Run as administrator** mode. For example, press the Windows key and type *Terminal*. Right-click **Terminal** and select **Run as administrator**.
1. Download and install the Power Platform admin PowerShell module. More information: [Get started with the Power Platform admin module](/powershell/powerapps/get-started-powerapps-admin?view=pa-ps-latest).

   `Install-Module -Name Microsoft.PowerApps.Administration.PowerShell`

1. After the module is installed, run the following command. Replace &lt;friendly name&gt; with the environment name you want to use for MCP.

   `New-AdminPowerAppEnvironment -DisplayName '<friendly name>' -Location unitedstatesfirstrelease -EnvironmentSku Trial -ProvisionDatabase`

   > [!NOTE]
   > You need to pass `Location` as *unitedstatesfirstrelease* and provide a friendly name for your environment. You will be prompted for your credentials, so make a note of this because you need it throughout the instructions.

   A list of attributes for your newly provisioned environment are displayed. This typically includes `EnvironmentName`, `DisplayName`, `Location` (expected value is unitedstatesfirstrelease), `CommonDataServiceDatabaseProvisioningState` (expected value is succeeded).

1. Note both the `EnvironmentName` and `DisplayName` for later steps.
1. Add sample data to the Dataverse environment, which helps you interact with the MCP server for evaluation. More information: [Add and remove sample data](/power-apps/developer/data-platform/sample-data)

## Ensure the latest PowerAIExtensions solution is installed 

You might need to update the version of the Microsoft Dynamics 365 – PowerAIExtensions solution in the environment if the version is earlier than 1.0.1.773.

1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/)
1. Go to **Environments**, and open your environment.
1. On the command bar, select **Resources** > **Dynamics 365 Apps**.
1. Next to Microsoft Dynamics 365 – PowerAIExtensions if there's an **Update available** link, select it and update the solution.

## Create a Dataverse connection for the MCP configuration

1. Go to [Power Automate](https://make.powerautomate.com). If necessary, change to the correct environment by selecting it from the top right.
1. Select **Connections** on the left navigation pane, and then select **+ New connection** on the command bar.
1. Type *Dataverse* in the search box, and then select the green colored **Microsoft Dataverse** connector.
   :::image type="content" source="media/power-automate-connector.png" alt-text="Dataverse connector":::
1. Complete the instructions on your screen.
1. Note the user name in the connection **Name**, this should be the same name that you used to create the environment earlier.
1. Select the connection to open it and copy the entire URL from the browser and save it. You need this URL for Claude desktop and VS Code MCP configuration.
   :::image type="content" source="media/copy-entire-browser-url.png" alt-text="Copy entire browser URL":::

## Install the Dataverse MCP server local proxy

These steps install the Dataverse MCP server local proxy that is used by the MCP client, such as Claude Desktop or VS Code GitHub Copilot.

1. Install the .NET SDK 8.0 either from Downloads or with this PowerShell command.
   `winget install Microsoft.DotNet.SDK.8`

1. In the Terminal window you opened earlier, run this command to install the Microsoft.PowerPlatform.Dataverse.MCP local proxy.
   `dotnet tool install --global --add-source https://api.nuget.org/v3/index.json Microsoft.PowerPlatform.Dataverse.MCP`

## Get the tenant ID of your Dataverse environment

When you configure the Dataverse MCP server for either Claude Desktop or VS Code GitHub, you need to provide the `TenantID` value.

Here’s one of the ways to get tenant ID details:

1. Go to https://make.powerapps.com.
1. Select **Settings** (gear icon) on the top right, and then select **Session details**.
1. Copy the value of the **Tenant ID** from the Power Apps session details. Make a note of this GUID as it be used in the configuration steps later.  

## Use the Dataverse MCP server in Microsoft Copilot Studio

1. Go to [Power App](https://make.powerapps.com) and select your environment from the top right environment selector.
1. From the left navigation pane select **Agents** > **Create new agent**. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Select **Create**.
1. Scroll down to the **Tools** section and select **+ Add tool**.
1. Select **Microsoft Dataverse Connector**, and then select **Dataverse MCP Server**.
   1. If you haven't yet created a Dataverse connection you are prompted to do so.
1. Select **Add to agent**.

The individual tools available on this MCP server can be viewed and modified by selecting **...** > **Edit** next to the **Dataverse MCP Server** tool.

You can now interact with the Dataverse MCP Server tool in the **Test your agent** chat pane. Try commands like "list tables in Dataverse", "describe table account", or "how many accounts do I have".
:::image type="content" source="media/copilot-studio-mcp.png" alt-text="Dataverse MCP in Copilot Studio":::

## Configure and use the Dataverse MCP server in Claude

Claude AI is a large language model (LLM) and chatbot developed by Anthropic. It excels at natural language processing and is multimodal, meaning it can process text, audio, and visual inputs. Claude can answer questions, summarize documents, generate text, and even create diagrams, animations, and code.

> [!NOTE]
> This step is independent from setting up Dataverse for MCP so you can do this at any time.

### Download Claude desktop

If you have not already done so, download and install Claude desktop [Download - Claude](https://claude.ai/download). 

Once you have Claude desktop installed, you can find and launch Claude from your desktop.

### Configure Dataverse MCP server in Claude desktop

1. Open Claude desktop and go to **File** > **Settings**.
1. If you haven't configured any MCP servers for Claude desktop previously, you observe a **Settings** dialog. Select **Edit Config**.
1. This takes you to the Claude desktop files. Open the **claude_desktop_config.json** file with your favorite JSON editor.
1. Enter this text into configuration – replacing &lt;URL from prerequisite&gt; and &lt;Tenant Id GUID from Prerequisite&gt; from the [Prerequisites](#prerequisites) described earlier. Use a <friendly name> for your Dataverse MCP server that you can easily remember, for example: *MyDataverseMCPServer*. 

```json
{
     "mcpServers": {
    "<friendly name>": {
      "command": "Microsoft.PowerPlatform.Dataverse.MCP",
      "args": [
        "--ConnectionUrl",
        "<URL from Prerequisite>",
        "--MCPServerName",
        "DataverseMCPServer",
        "--TenantId",
        "<Tenant Id GUID from Prerequisite>",
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

If you have  data in the Dataverse environment, you can start testing your setup by asking “list tables in Dataverse”, “describe table account” or “how many accounts do I have” and something similar. More information: [Add and remove sample data](/power-apps/developer/data-platform/sample-data)

> [!TIP]
> If you have other MCP servers registered with Claude it’s best to add *in Dataverse* in your prompt to be specific about which MCP server you’d like to use.


Learn more about MCP:

- [Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)
- [Anthropic and Introduction - Model Context Protocol](https://modelcontextprotocol.io/introduction)

