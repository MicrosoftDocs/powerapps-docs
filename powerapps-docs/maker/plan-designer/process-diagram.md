---
title: Use Plan Designer to Simplify Process Diagrams
description: Discover how to use Plan Designer to generate process diagrams that enhance clarity and efficiency in complex workflows.
author: szlo
contributors: null
ms.topic: conceptual
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

[This section is prerelease documentation and is subject to change.]

The Plan Designer simplifies diagram creation and refinement, helping teams define user roles and develop effective solutions. Process diagrams enhance clarity, communication, and efficiency in workflows, especially in complex projects.

You can add pictures of process diagrams as an additional source during the creation experience to impact the process. However, including a predefined process can bias Copilot, limit creativity and potentially cause it to misinterpret and duplicate steps.

> [!IMPORTANT]
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2189520), and are available before an official release so that customers can get early access and provide feedback.
> - Make sure you have preview features turned on for Plan designer. Learn more: [Turn on preview features for Plan designer](plan-designer.md#turn-on-preview-features-for-plan-designer)

When process diagrams are enabled, the diagram on the right side of the Plan designer is replaced with the process diagram.

Processes are generated immediately after [user requirements](create-plan.md#generate-user-requirements) are completed and follow a two-level hierarchy.

- **Process Stages**: Overview of the processes required to resolve the business problem and user stories

   :::image type="content" source="media/create-a-plan/image14.png" alt-text="Screenshot of the Plan Designer interface showing process stages overview.":::

- **Process Maps**: Detailed steps, events, and decision points for developing a process. Process maps are accessed by selecting View Process on a process stage. Each activity shows the User Role that is expected to complete the defined action.

   :::image type="content" source="media/create-a-plan/image15.png" alt-text="Screenshot of the Plan Designer interface showing detailed process maps with steps, events, and decision points.":::

### Understand a process

Processes include the following process nodes.

1. **Events** 
   - **Start**: Event that triggers the start of the process  
   - **Intermediate**: Events that happen in the middle of a process that happen in-line before the process continues  
   - **End**: Event that signals the process has been completed  

1. **Gateways**  
   - **Exclusive**: From a decision point, only one path from the gateway is taken  

1. **Activities**
   - **Task**: The core actions that are taken by a user to complete the user stories  

### Edit a process

The process is an AI-first experience and might not align with the expected process. To resolve any discrepancies, processes can be edited using natural language or manual edits.

1. Edit a process with natural language by selecting the Process Agent icon and describing the changes you want to make to the process.

     Type your prompt in the text box such as the example prompt shown below.

     ```copilot-prompt
    Add an approval gateway for HR to approve or reject the vacation request based on company HR policies.
    ```

1. Add connecting edges between nodes by selecting one of the node anchors and dragging it to another node.

1. Add edits manually by selecting the icon to add the appropriate node. Additionally, if you drag a connecting line from a node, it will automatically add an activity node.

1. To delete nodes, select the trash can on the node. Connecting lines can be deleted by selecting backspace.

> [!NOTE]
> - All changes are batched and not saved until the **Validate changes** button is selected, either on the top left of the canvas or from a newly added node.
> - The process experience in plan is an AI-first experience, even when performing manual edits. When the validate changes button is selected, the AI reasons over the changes that were made and merges those changes with the existing process that was generated.
> - Batch 3–5 manual changes at a time, and then validate changes. If wanting to make more than 5 changes, try the natural language update first.

:::image type="content" source="media/process-diagram/image16.png" alt-text="Screenshot of a computer AI-generated content may be incorrect.":::

:::image type="content" source="media/process-diagram/image17.png" alt-text="Screenshot of a computer AI-generated content may be incorrect.":::

Add step

:::image type="content" source="media/process-diagram/image18.png" alt-text="Screenshot of a computer AI-generated content may be incorrect.":::

Add decision

:::image type="content" source="media/process-diagram/image19.png" alt-text="Screenshot of a computer AI-generated content may be incorrect.":::

Validate changes 

## Known limitations in Process Agent (preview)

- Only exclusive gateways are currently supported.

- Events cannot be manually added.

- Technology proposals are not directly impacted by process.

- User Stories are not updated to reflect changes in process.

- Only one set of changes can be validated at a time. Making additional changes while the AI validates can cause the validation to lock up.

- Once validated, changes to the process can't be undone; they can only be further changed.

- Process stages can't be directly edited. To edit process stages, refine user stories and regenerate the process.

- Node types can't be changed; they can only be deleted and readded.
