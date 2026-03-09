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

[!INCLUDE [preview-banner](../../../shared/preview-includes/preview-banner.md)]

This article explains how to create business skills that agents can use to complete work according to your organization's processes. You'll learn how to enable the required features, author skill content, test skills with agents, and manage skills across environments.

[!INCLUDE [cc-preview-features-definition](../../../shared/preview-includes/preview-note-pp.md)]

## Prerequisites

- The environment must be enabled and configured for Dataverse MCP server preview. Business skills are only available for use with the preview version of Dataverse MCP server.
- The environment where you create and use business skills must be a Managed Environment.More information: [Use preview tools and upcoming features in Dataverse MCP server](data-platform-mcp-preview-tools.md)
- The environment must be enabled for [Dataverse intelligence](data-platform-intelligence.md).

## Create a business skill

You can create business skills in the following two ways:

### Use the Dataverse MCP server (preview) to create skills

The Dataverse MCP server (preview) has new tools to create skills. To create  a business skill using the tools:

   1. Add Dataverse MCP server Preview as a tool to any agent in Microsoft Copilot Studio or connect to it from coding agents in Visual Studio Code or non-Microsoft clients.
   1. Start by asking your agent to create a new skill and define its purpose.
   1. Provide your business process information.  
   1. The business skill is saved in the environment you used to connect to the MCP server.  

### Manually create skills in Power Apps

1. Go to [Power Apps](https://make.powerapps.com) and then go to **Tables**.  
1. Select **All** in the **Tables** list and search for **Business Skills**. This table stores all your skills in your environment.  
1. Open the business skills table and select **Create an app** on the command bar. Enter a suitable name such as *Skill Management App*, and then select **Create**.
1. When the app is created, select **Save and publish**.  

You can now use this app to manage and create skills manually.

> [!NOTE]
>
> - This app appears with all your other apps in the environment.  
> - All skills are active by default. [Deactivate a skill](#deactivate-a-skill)

## Use business skills 

After you create business skills in your environment, AI agents can use them to understand and run business processes. Access skills through the Dataverse MCP server preview.

- To start using business skills, connect to the Dataverse MCP server preview in Microsoft Copilot Studio or from agent mode in Visual Studio Code or non-Microsoft clients.
- Try asking your agent, "Show me all business skills in this environment." The agent retrieves a list of all the skills in your connected environment by using the Dataverse MCP server.  
- Start testing by asking your agent a relevant scenario that matches your skill’s intended use case. For example, if you created a skill for logging call transcripts into Dataverse, provide a sample transcript to your agent and ask it to log the transcript information in Dataverse.
  > [!NOTE]
  > If your agent doesn't automatically fetch skill details, try adding "Using business skills" before your actual prompt. For example, "Using business skills log this transcript in Dataverse."  
- Remember to add any other relevant tools, including MCP servers and connectors, that the agent needs access to for successfully executing your business processes defined in skills. 
- Confirm your intended actions were successful and continue to iterate on the skill instructions based on results. 

## Share a business skill

Skills are user-owned by default. To allow others to interact with the skills do the following: 

- Make skills viewable to everyone in your organization by granting permissions to view business skills. 
  - Go to the app you built earlier.  
  - Select a skill.  
  - Change the **Viewable by** property to organization to allow other users in your environment with at least basic user privileges to see the skill.  
  - The **Viewable by** property is **individual by default**, so if you create a skill, only you can view it.

- Share skills with other users or teams in the environment.
  - Go to the Skill Management app you built earlier.  
  - Select a skill and select **Share** in the top command bar. (If you don’t see **Share**, select the three dots for more capabilities and select **Share**.) 
  - Search for a user or team to share the skill with and select that user.
  - Choose the relevant permissions and select **Share**.

## Add business skills to a solution 

Business skills are solution-aware, which means you can package them into solutions for application lifecycle management (ALM). This allows you to move skills between environments as part of your deployment process.

To add a skill to a solution:

1. Sign in to [Power Apps](https://make.powerapps.com) and select your environment.
1. Go to **Solutions** and open an existing solution or create a new one.
1. Select **Add existing** > **Business skill** from the top navigation bar.
1. Choose the skills you want to add to your solution, and then select **Add**.

## Best practices when creating business skills 

- Write clear, specific instructions. Vague instructions lead to inconsistent agent behavior.
- Use descriptive names and descriptions. Help agents discover the right skill for the task.
- Keep skills focused—One skill, one process. Create separate skills for distinct workflows.
- Test with real scenarios—Validate behavior before sharing broadly.
- A well-structured business skill should include: 
   - Description:
      - What the skill does and when to use it.
      - Specific trigger phrases. For example, "Use when user asks about order status or mentions shipment tracking".
   - Step-by-step instructions:
      - Numbered steps in the process sequence.
      - What happens at each stage and how to validate before moving to the next step.
   - Examples:
      - Concrete examples showing expected inputs and outputs for common scenarios.
   - Troubleshooting:
       - Common errors with causes and solutions.
       - Recovery steps for failures.
   - Input and output specifications:
      - Required vs optional parameters with expected formats.
      - Output fields and success criteria.
      - Required tools for successful execution of skill.

## Sample Business skills for getting started 

To help you get started, sample business skills are available here: [Business skills repo on GitHub](https://aka.ms/DVBusinessSkillRepo)  

This open source GitHub repository also has a downloadable solution. Install the solution in your environment to explore working examples and use them as templates for your own skills. Refer to the ReadMe file located in the repository for more instructions  how you start using these sample skills.  

## Deactivate a skill

To prevent a skill from being used in agents until you have finalized them, do this:

1. Go to the **Skill Management** app you built earlier.
1. Select a skill and select **Deactivate** on the command bar.

Deactivate doesn't delete the skill but prevents agents from seeing it until you activate it.

## Next steps

[Business skills overview](data-platform-business-skill-overview.md)