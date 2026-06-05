---
title: "Create and use business skills" 
description: Learn how to enable Microsoft Dataverse intelligence to bring business data understanding to AI agents and Copilot.
ms.date: 04/15/2026
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

This article explains how to create and manage business skills that ground agents in your organization's processes. You'll learn how to enable the required features, author skill content, test skills with agents, and manage skills across environments.

[!INCLUDE [cc-preview-features-definition](../../../shared/preview-includes/preview-note-pp.md)]

## Prerequisites

- The environment must be enabled and configured for Dataverse MCP server preview. Business skills are only available for use with the preview version of Dataverse MCP server.
- The environment where you create and use business skills must be a Managed Environment. More information: [Use preview tools and upcoming features in Dataverse MCP server](data-platform-mcp-preview-tools.md)
- The environment must be enabled for [Dataverse intelligence](data-platform-intelligence.md).

## Open the business skills page

1. Go to [Power Apps](https://make.powerapps.com).
1. In the left navigation pane, select **More**, and then select **Business skills (preview)**.

> [!TIP]
> Pin the **Business skills** page to the left navigation pane for quick access.

The **Business skills** page is the central hub for managing all business process knowledge in your environment. From here, you can create, edit, share, and organize the skills that agents use to follow your organization's processes.

## Manage business skills

### Create a business skill

1. Select **New business skill** on the command bar, or select the **Create a business skill** card.
1. Enter a name for your skill. A unique name is generated automatically with the preferred solution's prefix.
1. In the **Description** field, describe the skill's purpose and when it should be followed. Agents use this description to understand when to perform the skill.
1. In the **Instructions** section, write the step-by-step process in markdown format. Use the **Edit markdown** and **Preview** options to switch between editing and previewing your instructions.
1. Select **Save**.
1. After saving, you can add resource files in the **Resources** section. Select **Add Files** to attach reference materials such as policy documents, SOPs, templates, forms, or calculations (20 MB limit).

> [!NOTE]
> All skills are active by default. [Deactivate a skill](#deactivate-a-skill)

### Upload a business skill

You can quickly create a business skill by uploading existing skills.

1. Select **Upload business skill** on the command bar, or select the **Upload a business skill** card.
1. Drag and drop a file into the upload area, or select **Select from device** to browse for a file.
1. Upload a `Skill.md` (markdown) or `.zip` file of your skill (30 MB limit).
1. The business skill gets uploaded and saved. You can edit the skill once uploaded. 

### Edit a business skill

1. Open a skill in the **Business skills** page by selecting its name in the list, or select a skill and then select **Edit** from the command bar or the three-dot menu (**&#8942;**).
1. Update the **Name**, **Description**, **Instructions**, or **Resources** as needed.
1. Select **Save**. 

### Create or update skills using the Dataverse MCP server (preview)

You can also create and update skills through an agent connected to the Dataverse MCP server (preview):

1. Add Dataverse MCP server (preview) as a tool to any agent in Microsoft Copilot Studio or connect to it from coding agents in Visual Studio Code or non-Microsoft clients.
1. Ask your agent to create a new skill or update an existing one.
1. Provide your business process information.
1. The business skill is saved in the environment you used to connect to the MCP server.

### Share a business skill

Skills are user-owned by default. You can share skills with specific users or teams and control their level of access.

1. Select a skill, and then select **Share** from the command bar or the three-dot menu (**&#8942;**).
1. Search for and add the users or teams you want to share with.
1. For each user or team, choose a permission level:
   - **Viewer** - Can view the skill only.
   - **Co-owner** - Can view and edit the skill.
1. Select **Share**.

Select **Manage access** to review who has access, change permission levels, or remove access. Pending invitations that haven't been shared yet are shown on the **Pending invites** tab.

### Change skill visibility

You can make a business skill visible to everyone in the organization or restrict it to just the owner and shared users.

1. Select a skill, and then select **Viewable by** from the command bar or the three-dot menu (**&#8942;**).
1. In the **Viewable by** dialog, select one of the following:
   - **Individual** - Only the owner and users the skill is shared with can see the skill. This is the default.
   - **Organization** - All users in the environment with at least basic user privileges can see the skill.
1. Select **Save**.

### Deactivate a skill

To prevent a skill from being used by agents until you have finalized it:

1. Select a skill, and then select **Deactivate** from the command bar or the three-dot menu (**&#8942;**).

Deactivating a skill doesn't delete it, but prevents agents from discovering or using it. To reactivate, select the skill and then select **Activate**.

### Delete a skill

To permanently remove a business skill:

1. Select a skill, and then select **Delete** from the command bar or the three-dot menu (**&#8942;**).

> [!CAUTION]
> Deleting a skill is permanent and can't be undone. Any agents that reference the deleted skill can no longer use it.

## Use business skills

After you create business skills in your environment, AI agents can use them to understand and run business processes. Access skills through the Dataverse MCP server (preview).

- To start using business skills, connect to the Dataverse MCP server (preview) in Microsoft Copilot Studio or from agent mode in Visual Studio Code or non-Microsoft clients.
- Try asking your agent, "Show me all business skills in this environment." The agent retrieves a list of all the skills in your connected environment by using the Dataverse MCP server.
- Start testing by asking your agent a relevant scenario that matches your skill's intended use case. For example, if you created a skill for logging call transcripts into Dataverse, provide a sample transcript to your agent and ask it to log the transcript information in Dataverse.
  > [!TIP]
  > If your agent doesn't automatically fetch skill details, try adding "Using business skills" before your actual prompt. For example, "Using business skills log this transcript in Dataverse."
- Remember to add any other relevant tools, including MCP servers and connectors, that the agent needs access to for successfully executing your business processes defined in skills.
- Confirm your intended actions were successful and continue to iterate on the skill instructions based on results.

## Add business skills to a solution

Business skills are solution-aware, which means you can package them into solutions for application lifecycle management (ALM). This allows you to move skills between environments as part of your deployment process.

To add a skill to a solution:

1. Sign in to [Power Apps](https://make.powerapps.com) and select your environment.
1. Go to **Solutions** and open an existing solution or create a new one.
1. Select **Add existing** > **Business skill** from the top navigation bar.
1. Choose the skills you want to add to your solution, and then select **Add**.

## Best practices for creating business skills

- Write clear, specific instructions. Vague instructions lead to inconsistent agent behavior.
- Use descriptive names and descriptions. Help agents discover the right skill for the task.
- Keep skills focused. One skill, one process. Create separate skills for distinct workflows.
- Test with real scenarios. Validate behavior before sharing broadly.
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

## Sample business skills for getting started

To help you get started, sample business skills are available: [Business skills repo on GitHub](https://aka.ms/DVBusinessSkillRepo)

This open source GitHub repository also has a downloadable solution. Install the solution in your environment to explore working examples and use them as templates for your own skills. Refer to the ReadMe file located in the repository for more instructions on how you start using these sample skills.

## Next steps

[Business skills overview](data-platform-business-skill-overview.md)