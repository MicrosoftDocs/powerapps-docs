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

Plan designer helps teams create and refine diagrams as part of the plan to clarify user interactions and build effective solutions. Process diagrams make workflows clearer, improve communication, and help teams work more efficiently, especially on complex projects.

Optionally, include images of existing process diagrams as additional resources during the creation experience to enhance clarity. But if you add predefined processes, Copilot might just replicate what you provide, which can limit creativity and cause duplication or misinterpretation.

> [!IMPORTANT]
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2189520), and are available before an official release so that customers can get early access and provide feedback.
> - Make sure you have preview features turned on for Plan designer. Learn more: [Turn on preview features for Plan designer](plan-designer.md#turn-on-preview-features-for-plan-designer)

To use the process diagram feature, turn on preview features. When preview features are on, the process diagram appears on the right as you [create a plan](create-plan.md). The diagram generates after you [create user requirements](create-plan.md#generate-user-requirements).


Processes use a two level hierarchy.

- **Process stages**: An overview of the processes needed to address the business problem and user stories.

  :::image type="content" source="media/process-diagram/process-diagram-1.png" alt-text="Screenshot of a process diagram that shows process stages for a business problem and user stories." lightbox="media/process-diagram/process-diagram-1.png":::

- **Process maps**: Select **View process** on a process tile to see detailed steps, events, and decision points for developing a process. Each activity shows the user role responsible for the action.

     :::image type="content" source="media/process-diagram/view-process.png" alt-text="Screenshot of a process diagram showing detailed steps, events, and decision points for a process." lightbox="media/process-diagram/view-process.png":::

## Understand a process

A process has these types of nodes.

1. **Events** 
   - **Start**: Event that starts the process.
   - **Intermediate**: Event that happens during the process before it continues.
   - **End**: Event that signals the process is finished.

1. **Gateways**  
   - **Exclusive**: At a decision point, the process takes only one path from the gateway.

1. **Activities**
   - **Task**: The main action a user or system takes to finish a user story.

### Edit a process

The process is an AI-first experience and might not always produce the results you expect. Use natural language to describe the changes you want, or manually edit the process. The AI then reassesses your changes and the overall process to generate a new process map.


:::image type="content" source="media/process-diagram/edit-process.png" alt-text="Screenshot of a process diagram that shows edit icons for making changes to the process.":::

Legend


1. **Ask Process Agent**: Use natural language to enter the changes you want to make. Type your prompt in the text box, as in the example prompt.

     ```copilot-prompt
    Add an approval gateway for HR to approve or reject the vacation request based on company HR policies.
    ```

1. **Add event**: Add a new event.
1. **Add decision**: Add a new decision.
1. **Add step**: Add a new step.
1. **Validate changes**: Confirm your changes. Changes aren't finalized or saved with the plan until you validate them. The process experience in plans is an AI-first experience, even when you make manual edits. When you validate changes, the AI reviews and merges them with the existing process. As a best practice, batch three to five manual changes at a time, then validate them. If you want to make more than five changes, try the natural language update first to save time and improve the accuracy of the AI-generated content.
1. **Delete**: Delete a node. Remove connecting lines by selecting the backspace key.
1. **Connect nodes**: Add connecting edges between nodes by selecting a node anchor and dragging it to another node.


## Known limitations (preview)

- Only exclusive gateways are supported.

- You can't add events manually.

- The process doesn't directly affect technology proposals.

- User stories don't update to reflect changes in the process.

- Only one set of changes can be validated at a time. If you make more changes while the AI validates, validation can lock up.

- After validation, you can't undo changes to the process. You can only make more changes.

- You can't edit process stages directly. To edit them, refine user stories and regenerate the process.

- You can't change node types. You can only delete and readd them.
