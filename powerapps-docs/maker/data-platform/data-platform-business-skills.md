---
title: "Create and use business skills?" 
description: Learn how to enable Microsoft Dataverse intelligence to bring business data understanding to AI agents and Copilot.
ms.date: 03/06/2026
ms.reviewer: matp
ms.topic: how-to
author: prithvi-khosla
ms.subservice: dataverse-maker
ms.author: pkhosla
ms.service: powerapps
search.audienceType: 
  - maker
---
# Create and use business skills

Business skills are natural-language instructions that capture how your organization gets work done. Business skills represent your business processes, policies, and domain knowledge in a format that agents can understand and follow. Each skill describes how to complete a specific type of work—the steps involved, the information required, and the business rules that apply.

This article explains how to create business skills that agents can use to complete work according to your organization's processes. You'll learn how to enable the required features, author skill content, test skills with agents, and manage skills across environments.

## Prerequisites

- The environment must be enabled and configured for Dataverse MCP server preview. Business skills are only available for use with the preview version of Dataverse MCP server. More information: [Use preview tools and upcoming features in Dataverse MCP server](data-platform-mcp-preview-tools.md)   
- The environment must be [enabled for Dataverse intelligence](#enable-dataverse-intelligence).

### Enable Dataverse intelligence

Microsoft Dataverse intelligence extends Work IQ to bring business data understanding to AI agents and Microsoft Copilot. Work IQ helps agents understand work artifacts like files, meetings, and messages. Dataverse intelligence builds on this foundation by enabling agents to understand and act on your business data.

With Dataverse intelligence, you can define reusable business context that agents use to understand what your data means, follow your organization's processes when taking actions, and read and update Dataverse records reliably. This business context is shared across agents, so you define it once and use it everywhere.

> [!IMPORTANT]
> To enable these settings, you need the following requirements:
> 
> - Power Platform administrator role to access Dataverse intelligence environment settings.
> - To use this feature, the environment must be a [Managed Environment](/power-platform/admin/managed-environment-overview).

1. Go to [Power Platform admin center](https://admin.powerplatform.microsoft.com/). Select **Manage** >**Environments**.
1. Open the environment where you want to turn on the Dataverse MCP server, and then select **Settings** > **Product** > **Features**.  
1. Scroll down to locate **Dataverse intelligence**.  
1. Turn on **Enable Dataverse intelligence (Work IQ) for agents and AI experiences**. 
1. Make sure **Allow MCP clients to interact with Dataverse MCP server (Preview version)** is enabled. If it's not, enable it. 
1. Select **Save** to save the setting changes.

## Create a business skill

You can create business skills in the following two ways:

### Use the Dataverse MCP server (preview) to create skills 
The Dataverse MCP server (preview) has new tools to create skills. To create  a business skill using the tools:

   1. Add Dataverse MCP server Preview as a tool to any agent in Microsoft Copilot Studio or connect to it from coding agents in Visual Studio Code or non-Microsoft clients.
   1. Start by asking your agent to create a new skill and define its purpose.
   1. Provide your business process information.  
   1. The business skill is saved in the environment you used to connect to the MCP server.  

### Manually create skills in Power Apps <!-- Is this the same as one of the two mentioned above or is a third option to create a business skill? We need to explain? -->

1. Go to [Power Apps](https://make.powerapps.com) and then go to **Tables**.  
1. Select **All** in the **Tables** list and search for **Business Skills**. This table stores all your skills in your environment.  
1. Open the business skills table and select **Create an app** on the command bar. Enter a suitable name such as *Skill Management App*, and then select **Create**.
1. When the app is created, select **Save and publish**.  

You can now use this app to manage and create skills manually.

> [!NOTE]
>
> - This app appears with all your other apps in the environment.  
> - All skills are active by default. [Deactivate a skill](#deactivate-a-skill)

## Deactivate a skill

To prevent a skill from being used in agents until you have finalized them, select **Deactivate** on the command bar. Deactivate doesn't delete the skill, but prevents agents from seeing it until you activate it.

## Next steps

[Create and use business skills](../../user/use-business-skills.md)
