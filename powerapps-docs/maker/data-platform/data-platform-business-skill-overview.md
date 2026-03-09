---
title: "Business skills overview" 
description: Learn about business skills in Microsoft Dataverse to bring business data understanding to AI agents and Copilot.
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
# Business skills overview

[!INCLUDE [preview-banner](../../../shared/preview-includes/preview-banner.md)]

Business skills are natural-language instructions that capture how your organization gets work done. They represent your business processes, policies, and domain knowledge in a format that agents can understand and follow. Each skill describes how to complete a specific type of work—the steps involved, the information required, and the business rules that apply.

Agents discover and use business skills as needed at runtime to complete tasks according to your organization's processes. When multiple agents use the same skill, they follow the same process, ensuring consistent behavior across your organization.

> [!IMPORTANT]
>
> - This is a preview feature.
> - [!INCLUDE [cc-preview-features-definition](../../../../../../repos/powerapps-docs-pr/powerapps-docs/includes/cc-preview-features-definition.md)]
> - Business skills are not executable code. They contain natural-language instructions that guide agent behavior, similar to how you might document a process for a new employee.

Key capabilities include: 

- Reusability—Define a process once and use it across multiple agents and surfaces 
- Consistency—Agents follow the same process definition, reducing variation in outcomes 
- Maintainability—Update a skill in one place to change behavior across all agents that use it 
- Governance—Control who can create, modify, and share business skills using Dataverse security. Each skill has an owner; sharing follows Dataverse RBAC patterns 
- Solution-aware—A solution aware object that appears in Solution explorer and can be moved across environments 

## Skill structure 

Business skills use a layered structure for efficient discovery and retrieval. 

|Layer  |Content  |Purpose  |
|---------|---------|---------|
|Metadata      | Name and description   | Enables agents to quickly discover relevant skills         |
|Instructions     | Full skill body   |  Contains the complete process definition     |

Agents query metadata to find applicable skills, then retrieve full instructions only when needed.

## Security and governance 

Business skills follow Dataverse security patterns. Each skill has an owner who controls access through standard sharing mechanisms. Users these security roles can work with business skills.

|Security role  |Privileges  |
|---------|---------|
|Basic User     |  Can create skills (owned by them) <br/> Can use skills shared with them. <br/>Can't publish environment-wide.       |
|Environment Maker     |   Can create and share skills (owned by them)<br/> Can manage solution deployment       |
|System Administrator or System Customizer     |  Can create and share skills<br/> Can manage solution deployment       |

## Next steps

[Create and use business skills](data-platform-business-skills.md)

[Configure the Dataverse MCP server for an environment](data-platform-mcp-disable.md)