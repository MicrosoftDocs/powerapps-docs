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

1. Select the connection to open it. Copy the entire URL from the browser and towards the end add *()* and save it. You need this URL for Claude desktop MCP configuration. <!--Need image of URL. The image resolution in the Word doc was too small to capture the URL in your screenshot. Please add the screenshot to SharePoint so as to maintain higher resolution. Only the open and closed parentheses should be added? Also "towards the end" do you mean at the end of the URL. We need to be specific.-->

## Install the Dataverse MCP server local proxy

These steps install the Dataverse MCP server local proxy that is used by the MCP client, such as Claude desktop or VS Code GitHub Copilot.<!-- The local proxy steps aren't in the VS Code GitHub Copilot article. Shouldn't they be?-->

1. Install the .NET SDK 8.0 either from download or with this PowerShell command.

   `winget install Microsoft.DotNet.SDK.8`
1. In a Windows terminal window, run this command to install the Microsoft `PowerPlatform.Dataverse.MCP` local proxy.<!--Where is the step to open the terminal window in this article? I assume this doesn't exist in this article so removed your reference about an earlier step assuming this is a Windows terminal.  -->
   `dotnet tool install --global --add-source https://api.nuget.org/v3/index.json Microsoft.PowerPlatform.Dataverse.MCP`

## Get the tenant ID of your Dataverse environment
<!-- Start here-->
When you configure the Dataverse MCP server for either Claude Desktop or VS Code GitHub, you need to provide the TenantID value.
Here’s one of the ways to get tenant ID details:
1.	Go to https://make.powerapps.com.
2.	Select Settings (gear icon) on the top right, and then select Session details.
3.	Copy the value of the Tenant ID from the Power Apps session details. Make a note of this GUID because it's used in the configuration steps later.

## Configure and use the Dataverse MCP server in Claude

<!--STEPS -->
