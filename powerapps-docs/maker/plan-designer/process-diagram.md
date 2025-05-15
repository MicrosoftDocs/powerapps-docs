---
title: Use Plan Designer to Simplify Process Diagrams
description: Discover how to use Plan Designer to generate process diagrams that enhance clarity and efficiency in complex workflows.
author: szlo
contributors: mduelae
ms.topic: how-to
ms.date: 05/19/2025
ms.author: mkaur
ms.reviewer: mkaur
ms.collection:
  - bap-ai-copilot
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-title
  - ai-gen-desc
  - copilot-scenario-highlight
  - ai-seo-date:05/05/2025
  - ai-gen-description
---

# Generate process diagrams (preview)

[This article is prerelease documentation and is subject to change.]

Plan designer makes it easier to create and refine diagrams as part of the plan, so teams can clarify user interactions and build effective solutions. Process diagrams make workflows clearer, improve communication, and help teams work more efficiently, especially on complex projects.

You optionally add images of process diagrams you already have as another resource during the creation experience to make the process clearer. Including predefined processes may bias Copilot to just duplicating what is provided, effectively limiting creativity and causing potential duplication or misinterpretation.

> [!IMPORTANT]
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2189520), and are available before an official release so that customers can get early access and provide feedback.
> - Make sure you have preview features turned on for Plan designer. Learn more: [Turn on preview features for Plan designer](plan-designer.md#turn-on-preview-features-for-plan-designer)

To use the process diagram feature, you need to turn on preview features. Once enabled, the process diagram will appears the right as you [creating a plan](create-plan.md). The diagram is generated after [user requirements](create-plan.md#generate-user-requirements) are created.


Processes use a two-level hierarchy.

- **Process stages**: An overview of the processes needed to address the business problem and user stories

  :::image type="content" source="media/process-diagram/process-diagram-1.png" alt-text="Screenshot of a process diagram that shows process stages for a business problem and user stories." lightbox="media/process-diagram/process-diagram-1.png":::

- **Process maps**: Select **View process** on a process tile to see detailed steps, events, and decision points for developing a process. Each activity shows the user role responsible for the action.

     :::image type="content" source="media/process-diagram/view-process.png" alt-text="Screenshot of a process diagram showing detailed steps, events, and decision points for a process." lightbox="media/process-diagram/view-process.png":::

## Understand a process

A process includes these process nodes.

1. **Events** 
   - **Start**: Event that triggers the process to start.
   - **Intermediate**: Events that occur in the middle of a process and happen inline before it continues.
   - **End**: Event that signals the process is complete.

1. **Gateways**  
   - **Exclusive**: At a decision point, only one path from the gateway is taken.

1. **Activities**
   - **Task**: The core actions a user or system takes to finish the user stories.

### Edit a process

The process is an AI-first experience that might not generate results exactly as you would expect. Use natural language to describe what you want to change, or manually edit it, and AI will again reason over your changes and the overall process to generate a new process map.


:::image type="content" source="media/process-diagram/edit-process.png" alt-text="Screenshot of the process diagram with edit icons for making changes to the process.":::

Legend:


1. **Ask Process Agent**: Use natural language to enter the changes you want to make. Type your prompt in the text box, like the example prompt below.

     ```copilot-prompt
    Add an approval gateway for HR to approve or reject the vacation request based on company HR policies.
    ```

1. **Add event**: Add a new event.
1. **Add decision**: Add a decision.
1. **Add step**: Add a step.
1. **Validate changes**: Confirm your changes. Changes aren't finalized and saved with the plan until they're validated. The process experience in plans is an AI-first experience, even when you make manual edits. When you validate changes, the AI reviews the changes you made and merges them with the existing process. As a recommended practice, batch three to five manual changes at a time, then validate them. If you want to make more than five changes, try the natural language update first to save time and improve the accuracy of the AI generated content.

1. **Delete**: Delete a node. Remove connecting lines by using the backspace key.

Add connecting edges between nodes by selecting a node anchor and dragging to another node.


## Known limitations (preview)

- Only exclusive gateways are supported.

- You can't add events manually.

- The process doesn't directly affect technology proposals.

- User stories don't update to reflect changes in the process.

- Only one set of changes can be validated at a time. If you make more changes while the AI validates, validation can lock up.

- After validation, you can't undo changes to the process. You can only make more changes.

- You can't edit process stages directly. To edit them, refine user stories and regenerate the process.

- You can't change node types; you can only delete and readd them.
