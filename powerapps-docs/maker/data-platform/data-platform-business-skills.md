---
title: "Create and use business skills" 
description: Create and manage business skills in Power Apps, and use them with Copilot and agents.
ms.date: 11/03/2026
ms.reviewer: matp
ms.topic: how-to
author: prithvi-khosla
ms.subservice: dataverse-maker
ms.author: pkhosla
ms.service: powerapps
ms.custom:
  - ai-gen-docs-bap
  - ai-seo-date:10/08/2026
ai-usage: ai-assisted
search.audienceType: 
  - maker
ms.collection: 
    - bap-ai-copilot
---
# Create and use business skills (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

This article explains how to create and manage business skills that ground agents in your organization's processes. You learn how to create or upload skills in Power Apps, edit and share them, use them with Copilot and agents, and move them between environments.

[!INCLUDE [preview-note-business-applications-work-iq](~/../shared-content/shared/preview-includes/preview-note-business-applications-work-iq.md)]

## Prerequisites

- A Dataverse environment with **Work IQ** enabled by a Power Platform administrator. For more information, see [Manage participation in Business Applications in Work IQ](/power-platform/admin/business-applications-work-iq/manage-participation#environment-features-for-work-iq).
- Permissions to create or use business skills in the environment. For more information, see [Security and governance](data-platform-business-skill-overview.md#security-and-governance).
- To use skills through Business Applications in Work IQ, you need access to a supported Copilot experience or connected agent. Administrators manage access as described in [Manage AI experience access to Business Applications in Work IQ](/power-platform/admin/business-applications-work-iq/manage-ai-experience-access). For Work IQ licensing requirements, see [Licensing requirements](/microsoft-365/copilot/extensibility/work-iq/api-overview#licensing-requirements).
- Only if you connect directly through Dataverse MCP, an environment enabled and configured for the Dataverse MCP server. This configuration isn't required for Work IQ MCP connections. For more information, see [Configure the Dataverse MCP server for an environment](data-platform-mcp-disable.md).

## Open the business skills page

1. Go to [Power Apps](https://make.powerapps.com) and select your environment.
2. In the left navigation pane, select **More**, and then select **Business skills (preview)**.

> [!TIP]
> Pin the **Business skills (preview)** page to the left navigation pane for quick access.

The **Business skills** page is the central hub for managing all business process knowledge in your environment. From here, you can create, edit, share, and organize the skills that agents use to follow your organization's processes.

## Manage business skills

### Create a business skill

You can create a business skill in Power Apps in two ways:

- [Start from scratch](#start-from-scratch) to define a skill with help from Skill Builder or write the instructions yourself.
- [Upload a business skill](#upload-a-business-skill) to reuse an existing skill in a markdown or zip file.

#### Start from scratch

Skill Builder is a specialized agent that helps you create business skills through natural-language conversation. Describe your business process or provide a document with business guidance, and the agent generates a agent ready skill name, description, instructions, and resources. You can ask it to refine the content as you clarify the steps, business rules, and intended outcome.

You can also write the skill yourself in the same editor without using Skill Builder.

1. On the **Business skills** page, select **Start from scratch** to open the editor.
2. To use Skill Builder, describe the skill in the **Skill builder agent** pane on the left. For example, "Create a skill for reviewing a customer refund request against our refund policy." Include the policy details in your message or attach the relevant guidance. If you're writing the skill yourself, enter the content directly in the following steps.
3. Review or enter a name for your skill. A unique name is generated automatically with the preferred solution's prefix.
4. In **Description**, explain the skill's purpose and when agents should use it.
5. In **Instructions**, review or write the step-by-step process in markdown. Check that it reflects your business rules and uses the correct Dataverse tables and columns when applicable. Ask Skill Builder to refine the content, or use **Edit markdown** and **Preview** to edit and review it yourself.
6. Optional: Select **Edit metadata** to add key-value information, such as the organization the skill applies to.
7. Select **Save** to save your work.
8. Optional: In **Resources**, select **Add Files** to attach reference materials that agents need when following the skill, such as policy documents, standard operating procedures, templates, forms, or calculations (20 MB limit).
9. Select **Save** to keep working, or **Save and activate** when the instructions and resources are ready for agents to use. For more information, see [Save and activate a business skill](#save-and-activate-a-business-skill).

To create several related skills, you can ask Skill Builder to generate them in one conversation. Review and save each skill you want to keep.

> [!NOTE]
> When using business skills with an agent in Microsoft Copilot Studio, only text-based resource files are supported. The agent can only read the first 20 KB of data from a text-based resource file.

#### Upload a business skill

If you already have a skill in a `Skill.md` (markdown) or `.zip` file, upload it instead of creating the content from scratch.

1. On the **Business skills** page, select **Upload skills** on the command bar, or select the **Reuse what you have** card.
2. Drag and drop a file into the upload area, or select **Select from device** to browse for a file.
3. Upload your skill file (30 MB limit).

The uploaded skill is saved in your environment. Open it to review its instructions and resources, and [edit the skill](#edit-a-business-skill) as needed before using it with an agent. For activation guidance, see [Save and activate a business skill](#save-and-activate-a-business-skill).

### Edit a business skill

1. Open a skill in the **Business skills** page by selecting its name in the list, or select a skill and then select **Edit** from the command bar or the three-dot menu (**&#8942;**).
2. Update the name, **Description**, metadata, **Instructions**, or **Resources** directly. Or, ask Skill Builder to revise the skill. Review any generated changes before saving.
3. Select **Save** to keep working, or **Save and activate** to make the updated skill available to agents.

### Save and activate a business skill

You can save a skill while you're still working on it and activate it when it's ready for agents to use. A skill can have only one active version. You can review all previous active versions through versioning. In the skill editor, choose the action that matches your intent:

| Action | Result |
|---|---|
| **Save** | Saves your working copy without changing the version agents use. A new skill remains inactive. If the skill already has an active version, that version stays active. |
| **Save and activate** | Makes your changes the active version, including its associated resources. The previous active version remains in version history. |

Repeated saves only update the same working copy rather than creating a separate historical version each time. Reopen the skill to continue editing your saved changes. Resource changes follow the same lifecycle as instructions: adding or removing a resource in your working copy doesn't change the resources used by the active version until you activate the changes.

### Review and restore skill versions

Version history helps you review earlier versions and recover a previous skill definition. In the skill editor, select the history icon to open the **Version history** pane. It identifies the active version, shows saved changes that aren't active, and records who changed or activated a version and when.

Open an earlier version to inspect its instructions and associated resources. Viewing a version doesn't change the active skill. To use that content again, restore the version. Restoring creates a new active version with the selected instructions and resources. It doesn't overwrite the historical version or remove intervening history.

You need edit access to restore a version. Users with view-only access can inspect version history but can't edit or restore versions. For more information, see [Security and governance](data-platform-business-skill-overview.md#security-and-governance).

### Create or update skills from Copilot and agents

You can also create and update skills through Copilot or an agent connected to Work IQ or the Dataverse MCP server:

1. Open Copilot or an agent connected to Work IQ or the Dataverse MCP server.
1. Ask your agent to create a new business skill or update an existing one.
1. Provide your business process information.
1. The business skill is saved in the environment you used to connect to the Dataverse MCP server or a relevant environment through Work IQ.

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

Access applies to the skill across its versions; you don't share each version separately.

### Deactivate a skill

To stop agents from discovering or using an active skill:

1. Select a skill, and then select **Deactivate** from the command bar or the three-dot menu (**&#8942;**).

Deactivating a skill preserves its content and version history. To reactivate, select the skill and then select **Activate**.

### Delete a skill

To permanently remove a business skill:

1. Select a skill, and then select **Delete** from the command bar or the three-dot menu (**&#8942;**).

> [!CAUTION]
> Deleting a skill is permanent and can't be undone. Any agents that reference the deleted skill can no longer use it.

## Choose Work IQ MCP or Dataverse MCP

Both MCP servers can provide access to business skills, but they serve different integration patterns.

| Consideration | Work IQ MCP | Dataverse MCP |
|---|---|---|
| Context | Combines supported Microsoft 365 and business applications context. | Connects directly to one Dataverse environment. |
| Environment routing | Can discover business applications paths across environments available to the user. Name the intended environment when the user has access to several. | The MCP connection is configured for a specific Dataverse environment. |
| Administration | An AI administrator controls availability for the entire Work IQ MCP server. Power Platform participation and security controls still apply. | An administrator enables, configures, and authorizes Dataverse MCP for the environment. |
| Best fit | Agents that need work context and business application context through one server. | Agents that need direct Dataverse tools, skill management, or an explicit environment boundary. |

Use only the connections and tools required for the scenario. A narrower connection can make the data boundary easier to explain, test, and govern.

## Use business skills

Business Applications in Work IQ brings your organization's business data and process context into Copilot and agents. After you create and activate business skills in your environment, Copilot Chat, Copilot Cowork, and connected agents can discover and use the skills you have access to and follow your organization's processes.

Business skills also remain supported in agents connected directly to the Dataverse MCP server, without connecting through Work IQ MCP.

1. Open Copilot Chat, Copilot Cowork, or your connected agent. For experiences that use Work IQ, follow the setup guidance in [Use Business Applications in Work IQ](business-applications-work-iq.md#use-business-applications-in-work-iq) or [Build agents that integrate with Business Applications in Work IQ](business-applications-work-iq.md#build-agents-that-integrate-with-business-applications-in-work-iq). For direct Dataverse MCP connections, use the client setup links that follow this procedure.
1. If you're building your own agent, add any other tools, including MCP servers and connectors, that it needs to carry out the processes defined in your skills.
1. Ask Copilot or your agent to find business skills you have access to. For example, "Show me the business skills in the Contoso Sales environment." Use the name of the environment that contains your skills.
1. Test a scenario that matches your skill's intended use case. For example, if you created a skill for logging call transcripts into Dataverse, provide a sample transcript and ask your agent to use the skill to log the transcript information.
1. Confirm that the intended actions were successful and refine the skill instructions based on the results.

For a Work IQ MCP connection example, see [Connect GitHub Copilot CLI to the Work IQ MCP server](/microsoft-365/copilot/extensibility/work-iq/mcp/quickstart/github-copilot-cli). You can also connect directly to Dataverse MCP from [Microsoft Copilot Studio](data-platform-mcp-copilot-studio.md), [Visual Studio Code](data-platform-mcp-vscode.md), or [other clients](data-platform-mcp-other-clients.md).

> [!TIP]
> If Copilot or your agent doesn't automatically retrieve skill instructions, ask it explicitly to use business skills. When building an agent, you can include an instruction such as "First look for relevant business skills in the specified environment, retrieve their instructions, and follow the process they describe."

## Test and troubleshoot skill use

Test each skill with a repeatable scenario before you share it broadly.

1. Name the target environment explicitly.
1. Ask the agent to list the skills it can access in that environment.
1. Ask the agent to describe the intended skill before it performs an action.
1. Run a representative request and record the expected data, tools, and result.
1. Repeat the request to identify ambiguous instructions or inconsistent outcomes.
1. Test failure paths, including missing data, missing permissions, and unavailable tools.
1. Refine the name, description, instructions, examples, and success criteria.

If the agent doesn't find or use a skill, check:

- The agent is connected to Work IQ MCP or the intended Dataverse MCP environment.
- The skill is active.
- The user or agent identity has access to the skill and the required Dataverse data.
- Users accessing the skill through a security role also have **Skill Sharing Role**.
- The skill description clearly states when the agent should use it.
- The prompt or agent instructions identify the correct environment.
- The agent has every tool required to complete the skill's instructions.

The **Business skills** page doesn't currently show per-skill runtime usage or feedback. Use controlled test cases and any logs or traces provided by the agent experience to collect evidence. When you report a problem, include the environment, skill, prompt, expected result, actual result, and whether the agent retrieved the skill.

## Add business skills to a solution

Business skills are solution-aware, which means you can package them into solutions for application lifecycle management (ALM). This allows you to move skills between environments as part of your deployment process.

Managed and unmanaged solution exports include only the active version of each skill, along with its metadata and associated resources. The export process doesn't include saved changes that aren't active or historical versions. Version history remains in the source environment.

To add a skill to a solution:

1. Sign in to [Power Apps](https://make.powerapps.com) and select your environment.
2. Make sure the version of each skill you want to move is active.
3. Go to **Solutions** and open an existing solution or create a new one.
4. Select **Add existing** > **Business skill** from the top navigation bar.
5. Choose the skills you want to add to your solution, and then select **Add**.

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