---
title: "Create and use business skills" 
description: Create and manage business skills in Power Apps, and use them in agents through Work IQ MCP or Dataverse MCP.
ms.date: 09/25/2026
ms.reviewer: matp
ms.topic: how-to
author: prithvi-khosla
ms.subservice: dataverse-maker
ms.author: pkhosla
ms.service: powerapps
search.audienceType: 
  - maker
ms.collection: 
    - bap-ai-copilot
---
# Create and use business skills (preview)

[!INCLUDE [preview-banner](../../../shared/preview-includes/preview-banner.md)]

This article explains how to create and manage business skills that ground agents in your organization's processes. You learn how to enable the required features, author skill content in Power Apps, use skills with agents through Work IQ MCP or Dataverse MCP, and manage skills across environments.

[!INCLUDE [cc-preview-features-definition](../../../shared/preview-includes/preview-note-pp.md)]

## Prerequisites

- A Dataverse environment with **Work IQ** enabled by a Power Platform administrator. For more information, see [Manage participation in Business Applications in Work IQ](/power-platform/admin/business-applications-work-iq/manage-participation#environment-features-for-work-iq).
- Permissions to create or use business skills in the environment. For more information, see [Security and governance](data-platform-business-skill-overview.md#security-and-governance).
- To use skills through Work IQ MCP, access to the Work IQ MCP server and an agent that supports connecting to it. Administrators manage MCP server and application access as described in [Manage AI experience access to Business Applications in Work IQ](/power-platform/admin/business-applications-work-iq/manage-ai-experience-access). For Work IQ licensing requirements, see [Licensing requirements](/microsoft-365/copilot/extensibility/work-iq/api-overview#licensing-requirements).
- Only if you connect directly through Dataverse MCP, an environment enabled and configured for the Dataverse MCP server. This configuration isn't required for Work IQ MCP connections. For more information, see [Configure the Dataverse MCP server for an environment](data-platform-mcp-disable.md).

## Open the business skills page

1. Go to [Power Apps](https://make.powerapps.com).
1. In the left navigation pane, select **More**, and then select **Business skills (preview)**.

> [!TIP]
> Pin the **Business skills (preview)** page to the left navigation pane for quick access.

The **Business skills** page is the central hub for managing all business process knowledge in your environment. From here, you can create, edit, share, and organize the skills that agents use to follow your organization's processes.

## Manage business skills

### Create a business skill

1. Select **New business skill** on the command bar, or select the **Create a business skill** card.
1. Enter a name for your skill. A unique name is generated automatically with the preferred solution's prefix.
1. In the **Description** field, describe the skill's purpose and when it should be followed. Agents use this description to understand when to perform the skill.
1. Optional: Select **Edit metadata** to add key-value metadata that provides more information about the skill, such as its organization.
1. In the **Instructions** section, write the step-by-step process in markdown format. Use the **Edit markdown** and **Preview** options to switch between editing and previewing your instructions.
1. Select **Save**.
1. Optional: After saving, you can add resource files in the **Resources** section. Select **Add Files** to attach reference materials such as policy documents, SOPs, templates, forms, or calculations (20 MB limit).

> [!NOTE]
> All skills are active by default. [Deactivate a skill](#deactivate-a-skill)

> [!NOTE]
> When using business skills with an agent in Microsoft Copilot Studio, only text-based resource files are supported. The agent can only read the first 20 KB of data from a text-based resource file.

### Upload a business skill

You can quickly create a business skill by uploading existing skills.

1. Select **Upload business skill** on the command bar, or select the **Upload a business skill** card.
1. Drag and drop a file into the upload area, or select **Select from device** to browse for a file.
1. Upload a `Skill.md` (markdown) or `.zip` file of your skill (30 MB limit).
1. The business skill gets uploaded and saved. You can edit the skill once uploaded. 

### Edit a business skill

1. Open a skill in the **Business skills** page by selecting its name in the list, or select a skill and then select **Edit** from the command bar or the three-dot menu (**&#8942;**).
1. Update the **Name**, **Description**, **Metadata**, **Instructions**, or **Resources** as needed.
1. Select **Save**. 

### Create or update skills using the Dataverse MCP server

You can also create and update skills through an agent connected to the Dataverse MCP server:

1. Add Dataverse MCP server as a tool to any agent in Microsoft Copilot Studio or connect to it from agents in Visual Studio Code or non-Microsoft clients.
1. Ask your agent to create a new skill or update an existing one.
1. Provide your business process information.
1. The business skill is saved in the environment you used to connect to the MCP server.

The following Dataverse MCP server tools support business skill management:

| Tool | Description |
|------|-------------|
| `upsert_skill` | Creates a new business skill or updates an existing one. |
| `delete_skill` | Deletes an existing business skill from the environment. |
| `search` | Searches table schemas, business skills, and apps by keyword. |
| `describe` | Gets details from search results for tables, records, schemas, skills, and apps. |

### Share a business skill

Skills are user-owned by default. You can provide access to a business skill in three ways:

- **General access**—Makes the skill available to everyone in the environment. Use this option for skills that apply broadly across your organization.
- **Security role access**—Provides access based on Dataverse security roles. You can share a skill with roles assigned to you. Admins can share with any role.
- **Direct access**—Shares the skill with specific users or groups and lets you choose whether they can view or edit the skill.

1. Select a skill, and then select **Share** from the command bar or the three-dot menu (**&#8942;**).
1. Choose how to provide access:
   - For general access, choose **Anyone can view** to allow everyone in the organization to use this skill. This option provides view-only access.
   - For security role access, under **Security roles**, select one or more security roles and then choose whether they can view or edit the skill.
   - For direct access, under **Direct Access**, add a name, group, or email address, and then choose whether they can view or edit the skill.
1. Select **Share**.

> [!IMPORTANT]
> Security role access requires users to have two roles. An administrator must assign users the **Skill Sharing Role**, either directly or through a team. Users must also have the security role that the skill is shared with. For more information, see [Assign security roles](/power-platform/admin/assign-security-roles).

For example, if a skill is shared with the **Customer Service Representative** role, only users who have both **Customer Service Representative** and **Skill Sharing Role** can access it. Having either role by itself isn't enough.

Select **Manage access** to review who has access, change access levels, or remove access.

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

After you create business skills in your environment, agents can discover and use them through the Work IQ MCP server to follow your organization's processes. Direct connections through the Dataverse MCP server remain supported.

1. Connect your agent to the [Work IQ MCP server](/microsoft-365/copilot/extensibility/work-iq/mcp/overview). For a setup example, see [Connect GitHub Copilot CLI to the Work IQ MCP server](/microsoft-365/copilot/extensibility/work-iq/mcp/quickstart/github-copilot-cli). Alternatively, connect directly to Dataverse MCP from [Microsoft Copilot Studio](data-platform-mcp-copilot-studio.md), [Visual Studio Code](data-platform-mcp-vscode.md), or [other clients](data-platform-mcp-other-clients.md).
1. Add any other tools, including MCP servers and connectors, that the agent needs to carry out the processes defined in your skills.
1. Ask your agent to find business skills you have access to. For example, "Show me the business skills in the Contoso Sales environment." Use the name of the environment that contains your skills.
1. Test a scenario that matches your skill's intended use case. For example, if you created a skill for logging call transcripts into Dataverse, provide a sample transcript and ask your agent to use the skill to log the transcript information.
1. Confirm that the intended actions were successful and refine the skill instructions based on the results.

> [!TIP]
> If your agent doesn't automatically retrieve skill instructions, ask it explicitly to use business skills. When building an agent, you can include an instruction such as "First look for relevant business skills in the specified environment through the connected MCP server, retrieve their instructions, and follow the process they describe."

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
- Test with real scenarios. Validate behavior before sharing with users, groups, or security roles.
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
