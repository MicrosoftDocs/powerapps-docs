---
title: "Business skills overview" 
description: Learn how business skills provide reusable business-process instructions to Copilot and agents through Business Applications in Work IQ or direct Dataverse MCP connections.
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
# Business skills overview (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

Business skills are natural-language instructions that capture how your organization gets work done. They represent your business processes, policies, and domain knowledge in a format that agents can understand and follow. Each skill describes how to complete a specific type of work—the steps involved, the information required, and the business rules that apply.

[!INCLUDE [preview-note-business-applications-work-iq](~/../shared-content/shared/preview-includes/preview-note-business-applications-work-iq.md)]

Through [Business Applications in Work IQ](business-applications-work-iq.md), Copilot and connected agents can discover and use active business skills they have access to, completing tasks according to your organization's processes. Agents connected directly to the Dataverse MCP server can also discover and use business skills. When multiple agents use the same skill, they follow the same process, ensuring consistent behavior across your organization.

To enable business skills in a Dataverse environment, a Power Platform administrator turns on **Work IQ**. For more information, see [Manage participation in Business Applications in Work IQ](/power-platform/admin/business-applications-work-iq/manage-participation#environment-features-for-work-iq).

> [!IMPORTANT]
> Business skills are not executable code. They contain natural-language instructions that guide agent behavior, similar to how you might document a process for a new employee.

Key capabilities include: 

- Reusability—Define a process once and use it across multiple agents and surfaces.
- Consistency—Give agents the same process definition to reduce variation in outcomes.
- Maintainability—Update a skill in one place to change the instructions available to agents.
- Governance—Control who can create, modify, and use business skills through ownership, sharing, and Dataverse security roles.
- Solution awareness—Add skills to solutions and move them across environments.

## Skill structure 

Business skills use a layered structure for efficient discovery and retrieval. 

|Layer  |Content  |Purpose  |
|---------|---------|---------|
|Frontmatter      | Name, description, and optional key-value metadata   | Enables agents to quickly discover relevant skills and provides additional information for organizing them         |
|Instructions     | Full skill body   |  Contains the complete process definition     |
|Resources     | Attached reference files   | Provides supporting documents, templates, policies, and other materials agents can use when following the skill     |

Agents query frontmatter to find applicable skills, then retrieve full instructions and resources only when needed.

## How agents discover a skill

A skill's name, description, frontmatter, environment, state, and sharing settings all affect whether an agent can find and use it.

1. The agent searches the connected environment for skills that the current identity can access.
1. The agent compares skill frontmatter, especially the name and description, with the user's request.
1. The agent retrieves the complete instructions and resources for a relevant skill.
1. The agent uses its connected tools to carry out the process.

Write a description that states both what the skill does and when to use it. Agent selection is probabilistic, so test representative requests before you share a skill broadly.

## Security and governance 

Business skills are stored in Dataverse and follow Dataverse security patterns. The same permissions apply whether you use a skill in Copilot, a Work IQ-connected agent, or an agent connected directly to the Dataverse MCP server. Each skill has an owner who controls access. Owners can provide general access to everyone in the environment, share with selected Dataverse security roles, or provide direct access to specific users or groups.

Users who access a skill through a Dataverse security role must have both the selected role and the **Skill Sharing Role** security role. Security role access and direct access can provide view or edit permissions.

|Security role  |Privileges  |
|---------|---------|
| Basic User | Can create skills that they own.<br>Can use skills they have access to. |
| Environment Maker | Can create and share skills that they own.<br>Can manage solution deployment. |
| System Administrator or System Customizer | Can create and share skills.<br>Can manage solution deployment. |

## Next steps

[Create and use business skills](data-platform-business-skills.md)

[Work IQ MCP overview](/microsoft-365/copilot/extensibility/work-iq/mcp/overview)

[Configure the Dataverse MCP server for an environment](data-platform-mcp-disable.md)
