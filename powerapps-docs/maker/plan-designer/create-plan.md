---
title: Use the Plan designer to create a business solution with Copilot (preview)
description: Use the Plan designer to create business solutions with AI-powered experiences.
author: mduelae
contributors:
ms.topic: conceptual
ms.date: 5/19/2025
ms.author: szlo
ms.reviewer: mkaur
ms.collection:
  - bap-ai-copilot
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-title
  - ai-gen-desc
  - copilot-scenario-highlight
---

# Create a plan using Plan designer

Use the Plan designer, a copilot-first development tool, to quickly create comprehensive business solutions. Describe your business problem in natural language and add relevant images, like business process flows or screenshots of legacy apps. The Plan designer generates a complete Power Platform solution tailored to your needs. It includes Dataverse tables, canvas apps, model-driven apps, Power Automate flows, and Copilot Studio Agents. Follow the steps in this article to create a business solution and refine your requirements for precise, customized outputs.

Open the Plan designer from the Power Apps home page. It guides you through a multi-step process to generate user roles, user stories, data tables, and user experiences.

To show how the Plan designer works, this article uses a sample scenario to build a solution for managing paid time off (PTO) requests for employees and managers.

1. Sign in to [Power Apps](https://make.powerapps.com/).

2. In the textbox, type **Employees need to log vacation days, and managers need to approve them**. You can also provide more context like process diagrams, data models, or screenshots of legacy apps. When you're done, press **Enter**.

:::image type="content" source="media/create-a-plan/image1.png" alt-text="Screenshot of the Plan designer interface with a textbox for entering business scenarios.":::

Copilot opens the Plan designer and analyzes your business scenario based on your description.

Within the Plan designer, you can view the presence status of plan agents, which are AI assistants that analyze your business problem and generate a plan for it. These plan agents utilize AI to help build your plan.

- The **Requirement Agent** examines the business problem and uses AI to generate user requirements.
- The **Data Agent** suggests a set of tables for storing business information, complete with recommended columns, data types, and relationships.
- The **Solution Agent** evaluates the needs, processes, and data to create a solution that addresses your business problem.
- The **Process Agent** (preview) generates a process diagram depicting the different steps in the business problem, along with the personas and artifacts in context.

Review and refine the outputs created by the agents.

:::image type="content" source="media/create-a-plan/image2.png" alt-text="Screenshot of the Plan designer displaying the presence status of plan agents."::: 



## Generate user requirements

The **Requirements Agent** identifies user needs based on your description.

In this scenario, two roles are generated: employee and manager. Each role has its own descriptions and user stories. On the left side, the user roles and stories appear in a bullet list, while a visual diagram is on the right side.

1. Review the user roles and stories, then choose one of the following options:

   - Select **Add these roles** to generate a data model.
   - Select **Edit** to make edits inline or add new user roles or needs.

:::image type="content" source="media/create-a-plan/image3.png" alt-text="Screenshot of the Plan designer showing user roles and stories with options to edit or add roles.":::

1. Inline editing has the following options:

:::image type="content" source="media/create-a-plan/image4.png" alt-text="Screenshot of inline editing options for user roles and needs in the Plan designer.":::

Legend:

1. Select a user role to edit it.  
2. Add a new user role or delete the selected role.  
3. Add a new user need.  
4. Add a new user need above or below the selected user need, or delete the selected user need.  
5. Add a new user role.

1. Use **Copilot** to provide feedback for the generated user needs.

:::image type="content" source="media/create-a-plan/image5.png" alt-text="Screenshot of Copilot providing feedback for user needs in the Plan designer.":::

To make changes, provide a brief description of what you want to modify. Here are examples of what you can ask Copilot to do:

- Add a user role for HR admin to monitor PTO across teams to manage payroll.
- Add a user story for employees to view PTO blackout dates.
- Remove the user story for managers for viewing vacation history of team members.

1. Review the changes and select **Keep** or **Undo**.

1. When you're done, select **Looks good** to proceed to the next step and generate data tables.

:::image type="content" source="media/create-a-plan/image6.png" alt-text="Screenshot of the Plan designer with the 'Looks good' button to proceed to the next step.":::

## Generate data model

1. The proposed data tables appear in the **Data** section of the plan.

   1. Select **Edit** and describe what you want to change or add using Copilot.  
   2. Select **Show details** to view the data in a diagram and edit it.

   :::image type="content" source="media/create-a-plan/image7.png" alt-text="Screenshot of the Plan designer showing proposed data tables.":::

2. **Show details** opens the data workspace. Use the table visual designer to create tables, configure table relationships, and view a diagram of your data. For more information, see [Create and edit tables using Power Apps](/power-apps/maker/data-platform/create-edit-entities-portal#create-new-tables).

   :::image type="content" source="media/create-a-plan/image8.png" alt-text="Screenshot of the data workspace in the Plan designer showing table relationships.":::

3. When you're done, select **Back**.

4. When you're ready to generate user experiences, select **Looks good** to continue.

   :::image type="content" source="media/create-a-plan/image9.png" alt-text="Screenshot of the Plan designer with the 'Looks good' button to continue to user experiences.":::

## Generate technology proposal

The Solution Agent proposes technologies tailored to solve your business problem. In this scenario, two canvas apps, a model-driven app, and a Power Automate flow are created. These user experiences are designed for specific user roles and use data tables generated from earlier steps.

:::image type="content" source="media/create-a-plan/image10.png" alt-text="Screenshot of the Plan designer that shows proposed technologies for the solution.":::

To view details of the proposed user experiences, hover over the **information icon**. The pop-up info card shows the name, description, targeted user role, and included data tables.

:::image type="content" source="media/create-a-plan/image11.png" alt-text="Screenshot of the Plan designer that shows details of proposed user experiences.":::

To make changes, select **Edit**, and follow the steps above.

Alternatively, select **Looks good** to accept the proposed technologies.

:::image type="content" source="media/create-a-plan/image12.png" alt-text="Screenshot of the Plan designer with the 'Looks good' button that finalizes the proposal."::: 



## Proposed technologies

The Plan designer proposes artifacts from the following list of technologies:

1. Applications – Canvas Apps, Model-driven Apps  
1. Power Pages Site  
1. Power Automate Flow  
1. Power BI Report  
1. Copilot Studio Agents  

## Generate process diagrams (preview)

Creating process diagrams are a default part of the Plan Designer experience when Preview features have been enabled. To enable preview features, check the “” when initially creating your plan.

:::image type="content" source="media/create-a-plan/image13.png" alt-text="Screenshot of the Plan Designer interface showing a white rectangular object with a black border.":::

Tip: Pictures of process diagrams can be added as an additional source during the creation experience that will impact the process. However, it is worth noting that including a predefined process can bias the Copilot and limit the creativity for creating the optimal process experience or possibly cause it to hallucinate and duplicate process steps if it sees the diagram differently than the user stories.

Once enabled, the diagram on the right-hand side of the Plan Designer experience is replaced with the process diagram.

Process generate immediately after User Stories have completed, and have a two-level hierarchy:

1. Process Stages – Overview of the processes required to resolve the business problem and user stories

   :::image type="content" source="media/create-a-plan/image14.png" alt-text="Screenshot of the Plan Designer interface showing process stages overview.":::

1. Process Maps – Detailed steps, events, and decision points for developing a process. Process maps are accessed by clicking View Process on a process stage. Each activity shows the User Role that is expected to complete the defined action.

   :::image type="content" source="media/create-a-plan/image15.png" alt-text="Screenshot of the Plan Designer interface showing detailed process maps with steps, events, and decision points.":::

## Understanding a Process

Processes currently support a select number of process nodes.

1. Events  
   1. Start – Event that triggers the start of the process  
   1. Intermediate – Events that happen in the middle of a process that happen in-line before the process continues  
   1. End – Event that signals the process has been completed  

1. Gateways  
   1. Exclusive – From a decision point, only one path from the gateway is taken  

1. Activities  
   1. Task – The core actions that are taken by a user to complete the user stories  

## Editing a process

Process is an AI-first experience and may not align with the expected process. To resolve any discrepancies, processes can be edited via natural language or manual edits.

1. Editing a process with natural language is done by clicking the Process Agent icon and describing the changes you want made to the process.  
   Example: Add an approval gateway for HR to approve or reject the vacation request based on company HR policies.

1. Connecting edges can be added between nodes by clicking on one of the node anchors and dragging to another node.

1. Additive edits can be added manually by clicking the icon to add the appropriate node. Additionally, if you drag a connecting line from a node, it will automatically add an activity node.

1. To delete nodes, click the trash can on the node. Connecting lines can be deleted by clicking backspace.

> [!NOTE]
> - All changes are batched and not saved until the “Validate changes” button is clicked, either on the top left of the canvas or from a newly added node.
> - The process experience in plan is an AI-first experience, even when performing manual edits. When the validate changes button is clicked, the AI reasons over the changes that were made and merges those changes with the existing process that was generated.
> - Batch up 3-5 manual changes at a time, and then validate changes. If wanting to make more than 5 changes, try the natural language update first.

:::image type="content" source="media/create-a-plan/image16.png" alt-text="Screenshot of a computer AI-generated content may be incorrect.":::

:::image type="content" source="media/create-a-plan/image17.png" alt-text="Screenshot of a computer AI-generated content may be incorrect.":::

Add step

:::image type="content" source="media/create-a-plan/image18.png" alt-text="Screenshot of a computer AI-generated content may be incorrect.":::

Add decision

:::image type="content" source="media/create-a-plan/image19.png" alt-text="Screenshot of a computer AI-generated content may be incorrect.":::

Validate changes 

## Known Limitations in Process Agent (preview)

- Only exclusive gateways are currently supported.

- Events cannot be manually added.

- Technology proposals are not directly impacted by process.

- User Stories are not updated to reflect changes in process.

- Only one set of changes can be validated at a time, making additional changes while the AI is validating can cause the validation to lock up.

- Once validated, changes to the process cannot be undone, just further changed.

- Process stages cannot be directly edited. To edit process stages, refine User Stories and regenerate the process.

- Node types cannot be changed, only deleted and readded.

## Save your plan

Before creating your apps, save your plan to a solution.

1. Type the Solution name.  
1. Choose a publisher or select an existing solution that will contain the items generated from the plan.  
1. Select **Save**.

:::image type="content" source="media/create-a-plan/image20.png" alt-text="Screenshot of the Save your plan screen showing the solution name and publisher options.":::

The plan is stored within a solution. Learn more here – \<link to Manage solution docs\>.

## View and edit plans

When the Plan designer is turned on, you see the **Plans** menu in the left navigation pane. Use this menu to access your plans and make edits as needed.

:::image type="content" source="media/create-a-plan/image21.png" alt-text="Screenshot of the Plans menu in the left navigation pane showing options to create, view, and edit plans.":::

1. **Plans**: Use to access your plans.  
1. **Create a plan**: Use to create a new plan.  
1. **Your plans**: Use to view your plans.  
1. **Edit**: Use to edit the selected plan.  
1. **Edit or Delete**: Use to edit or delete the selected plan.  