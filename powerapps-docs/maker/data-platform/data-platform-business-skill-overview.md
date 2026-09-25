---
title: "Business skills overview" 
description: Learn how business skills in Business Applications in Work IQ provide reusable business-process instructions to agents through Work IQ MCP and Dataverse MCP.
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
# Business skills overview (preview)

[!INCLUDE [preview-banner](../../../shared/preview-includes/preview-banner.md)]

Business skills are natural-language instructions that capture how your organization gets work done. They represent your business processes, policies, and domain knowledge in a format that agents can understand and follow. Each skill describes how to complete a specific type of work—the steps involved, the information required, and the business rules that apply.

Agents can discover and use the business skills they have access to as needed at runtime to complete tasks according to your organization's processes. When multiple agents use the same skill, they follow the same process, ensuring consistent behavior across your organization.

[!INCLUDE [cc-preview-features-definition](../../../shared/preview-includes/preview-note-pp.md)]

To enable business skills in a Dataverse environment, a Power Platform administrator turns on **Work IQ**. For more information, see [Manage participation in Business Applications in Work IQ](/power-platform/admin/business-applications-work-iq/manage-participation#environment-features-for-work-iq).

> [!IMPORTANT]
> Business skills are not executable code. They contain natural-language instructions that guide agent behavior, similar to how you might document a process for a new employee.

Key capabilities include: 

- Reusability—Define a process once and use it across multiple agents and surfaces 
- Consistency—Agents follow the same process definition, reducing variation in outcomes 
- Maintainability—Update a skill in one place to change behavior across all agents that use it 
- Governance—Control who can create, modify, and use business skills through ownership, sharing, and Dataverse security roles.
- Solution-aware—A solution aware object that appears in Solution explorer and can be moved across environments 

## Skill structure 

Business skills use a layered structure for efficient discovery and retrieval. 

|Layer  |Content  |Purpose  |
|---------|---------|---------|
|Frontmatter      | Name, description, and optional key-value metadata   | Enables agents to quickly discover relevant skills and provides additional information for organizing them         |
|Instructions     | Full skill body   |  Contains the complete process definition     |
|Resources     | Attached reference files   | Provides supporting documents, templates, policies, and other materials agents can use when following the skill     |

Agents query metadata to find applicable skills, then retrieve full instructions and resources only when needed.

## Security and governance 

Store business skills in Dataverse. They follow Dataverse security patterns whether agents access them through Work IQ MCP or directly through Dataverse MCP. Each skill has an owner who controls access. Owners can provide general access to everyone in the environment, share with selected Dataverse security roles, or provide direct access to specific users or groups.

Users who access a skill through a Dataverse security role must have both the selected role and the **Skill Sharing Role** security role. Security role access and direct access can provide view or edit permissions.

|Security role  |Privileges  |
|---------|---------|
|Basic User     |  Can create skills (owned by them) <br/> Can use skills they have access to.       |
|Environment Maker     |   Can create and share skills (owned by them)<br/> Can manage solution deployment       |
|System Administrator or System Customizer     |  Can create and share skills<br/> Can manage solution deployment       |

## Next steps

[Create and use business skills](data-platform-business-skills.md)

[Work IQ MCP overview](/microsoft-365/copilot/extensibility/work-iq/mcp/overview)

[Configure the Dataverse MCP server for an environment](data-platform-mcp-disable.md)
