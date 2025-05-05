---
title: Use the Plan designer to create a business solution with Copilot (preview)
description: Use the Plan designer to create business solutions with AI-powered experiences.
author: mduelae
contributors:
ms.topic: conceptual
ms.date: 4/28/2025
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

# Use the Plan designer (preview)

[!INCLUDE [preview-banner](../../../shared/preview-includes/preview-banner.md)]

Learn how to use the Plan designer, a copilot-first development tool, to create comprehensive business solutions quickly. Describe your business problem in natural language and provide relevant images, like business process flows or screenshots of legacy apps. The Plan designer generates a complete Power Platform solution tailored to your needs, including Dataverse tables, canvas apps, model-driven apps, and Power Automate flows. Follow the steps in this article to create a business solution and refine your requirements for precise, customized outputs.

Go to the Plan designer from the Power Apps home page. It guides you through a multi-step process to generate user roles, user stories, data tables, and user experiences.

:::image type="content" source="media/pd-1-enter-problem.png" alt-text="Screenshot of entering a business problem in the Plan designer.":::

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2189520), and are available before an official release so that customers can get early access and provide feedback.

## Prerequisites

Turn on the **Try the new Power Apps experience** toggle on the Power Apps home page. 

:::image type="content" source="media/pd-3-enable-settings.png" alt-text="Screenshot of the Power Apps home page showing the new Copilot experience banner." :::


## Create a plan

To show you how the Plan designer works, let's use a sample scenario to build a solution for managing paid time off (PTO) requests for employees and managers.

1. Sign in to [Power Apps](https://make.powerapps.com).

1. Type your prompt in the text box such as the example prompt shown below. You can also provide more context like process diagrams, data models, or screenshots of legacy apps. When you're done, press **Enter**.

    ```copilot-prompt
    Employees need to log vacation days, and managers need to approve them.
    ```

    :::image type="content" source="media/pd-4-enter-sample-problem.png" alt-text="Screenshot of the Plan designer with a sample scenario input." :::


Copilot opens the Plan designer and addresses your business scenario based on your description.


### Plan agents

Within the Plan designer, you can view the presence status of plan agents, which are AI assistants that analyze your business problem and generate a plan for it. These plan agents utilize AI to help build your plan.

- The **Requirement Agent** examines the business problem and uses AI to generate user requirements.
- The **Data Agent** suggests a set of tables for storing business information, complete with recommended columns, data types, and relationships.
- The **Solution Agent** evaluates the needs, processes, and data to create a solution that addresses your business problem.

Review and correct the outputs created by the agent.


:::image type="content" source="media/pd-5-plan-agents.png" alt-text="Plan agents analyze your plan":::


### Generate user requirments

The Requirements Agent identifies user needs based on your description.

In this scenario, two roles were generated: employee and manager. Each role comes with its own descriptions and user stories. On the left side, the user roles and stories are presented in a bullet list, while a visual diagram is shown on the right side.


1. Review the user roles and stories. Then, choose one of the following options:

    - Select **Looks good** to generate a data model.
    - Select **Edit** to make edits inline or add new user roles or needs.
    
        :::image type="content" source="media/pd-6-generate-roles-stories.png" alt-text="Screenshot of the generated user roles and stories in the Plan designer." lightbox="media/pd-6-generate-roles-stories.png":::

1. Inline editing includes the following options:

    :::image type="content" source="media/pd-inline-editing.png" alt-text="Edit user needs inline." lightbox="media/pd-inline-editing.png":::

    Legend:
 
    1. Select a user role to edit it.
    1. Add a new user role or delete the selected role.
    1. Add a new user need above or below the selected user need, or delete the selected user need.
    1. Add a new user need.
    1. Add a new user role.
    
1. You can also use **Copilot** to provide feedback for the generated user needs. 

    :::image type="content" source="media/pd-edit-copilot.png" alt-text="Edit using Copilot":::

    If you need to make any changes, provide a brief description of what you want to modify. Here are examples of what you can ask Copilot to do:

    - Add a user role for HR admin to monitor PTO across teams to manage payroll.
    - Add a user story for employees to view PTO blackout dates.
    - Remove the user story for managers for viewing vacation history of team members.

1. Review the changes and select **Keep** or **Undo**.

1. When you're done, select **Add these roles** to move on to the next step and generate data tables.

### Generate data tables

1. The proposed data tables appear in the **Data** section of the plan.
    - Select **Edit** and describe what you'd like to change or add using Copilot.
    - Select **Show details** to view the data in a diagram and make edits.

      :::image type="content" source="media/pd-8-show-detailed-data.png" alt-text="Screenshot of the proposed data tables in the Plan designer." lightbox="media/pd-8-show-detailed-data.png":::

1. **Show details** opens the data workspace. Use the table visual designer experience where you create tables, configure table relationships, and can view a diagram of your data. For more information, see [Create and edit tables using Power Apps](../data-platform/create-edit-entities-portal.md#create-new-tables).

      :::image type="content" source="media/pd-9-view-data.png" alt-text="Screenshot of the data workspace showing the ERD." lightbox="media/pd-9-view-data.png":::

1. When you're done, select **Back**

1. When you're ready to generate user experiences, select **Looks good** to proceed.  

      :::image type="content" source="media/pd-11-save-tables.png" alt-text="Screenshot of the Plan designer with the option to save tables." lightbox="media/pd-11-save-tables.png":::

### Generate user experiences

The Solution Agent proposes a set of user experiences tailored to solve your business problem. In this scenario, a canvas app, a model-driven app, and two Power Automate flows are created. These user experiences are designed for specified user roles and with data tables generated from the previous steps.

:::image type="content" source="media/pd-12-generate-user-exp.png" alt-text="Screenshot of the proposed user experiences in the Plan designer." lightbox="media/pd-12-generate-user-exp.png":::

To view details of the proposed user experiences, hover over the **information icon**. The pop-up info card displays the name, description, targeted user role, and the included data tables.

:::image type="content" source="media/pd-13-more-info-about-plan.png" alt-text="Screenshot of the information icon pop-up with user experience details." :::

To make changes, select **Edit** and follow the steps above. Or select **Add these user experiences** to create the assets.

When you add the proposed user experiences, they're created.

### Save your plan and create items

1. To create an item like a canvas app or model-driven app, select **Create** > **Save all tables**.  

    Opening precreated Power Automate flows isn't supported; it navigates to the Power Automate page within your solution.

    :::image type="content" source="media/pd-14-open-app.png" alt-text="Screenshot of the Plan designer with the option to open created apps.":::

1. Before creating your apps, save your plan to a solution.

    1. Type the plan name.
    1. Choose a publisher or select an existing solution that will contain the items generated from the plan.
    1. Select **Save**.
   
       :::image type="content" source="media/pd-save-plan.png" alt-text="Screenshot of the save dialog box for a plan.":::

        The plan is stored within a solution. This action also enables the **Objects** view in the Plan designer, allowing makers to seamlessly switch between their plan and the solution view without leaving the Plan designer. For more information about solutions, see [Solution view](../data-platform/solutions-area.md).

        :::image type="content" source="media/pd-objects-view.png" alt-text="Screenshot of the objects view.":::

1. After saving the plan, select **Create** again. The proposed app opens in a new tab, fully functioning with the added data tables.

    :::image type="content" source="media/pd-15-final-create.png" alt-text="Screenshot of selecting create to create your items.":::

    For canvas apps, the app preview displays a welcome screen and other screens connected to tables. Opening a model-driven app launches the modern app designer with the tables already added. Both canvas and model-driven apps can then be saved and published for use.

### Known limitations

The **Objects** view is in preview, and several functions native to the solution view don't work in the embedded Plan designer experience. 

Navigation issues:

- When using the **Back** button after creating a new canvas app, model-driven app, Page, component library, or connection role, users are taken to the **All** section of **Objects** instead of their last location.
- After saving and exiting the row summary, you're redirected to the **All** section of **Objects** instead of their previous location.  
- Editing a table and then using the **Back** button also redirects users to the **All** section of **Objects** instead of their last location.
- Creating a new table and using the **Back** button takes users to the **All** section of **Objects** rather than their last location.
- When creating a new column security profile in apps, saving, and then using the **Back** button, the **Back** button doesn't work and causes continuous loading.
- Navigating to **Table** > **Forms**/**Views**/**Command** and then using the **Back** button redirects users to the **All** section of **Objects** instead of their last location.

## View and edit plans

When the Plan designer is turned on, you see the **Plans** menu in the left navigation pane. Use this menu to access your plans and make edits as needed.

:::image type="content" source="media/pd-your-plans.png" alt-text="Screenshot of the Plans menu showing options to view or edit plans." lightbox="media/pd-your-plans.png" :::

1. **Plans**: Use to access your plans.
1. **Create a plan**: Use to create a new plan.
1. **Your plans**: Use to view your plans.
1. **Edit**: Use to edit the selected plan.
1. **Edit or Delete**: Use to edit or delete the selected plan.

## Known limitations

- **Supported user experiences**: The Plan designer generates canvas apps, model-driven apps, and suggested Power Automate flows.
- **Generated Power Automate flows**: Power Automate flows created in the Plan designer take you to the Power Automate page but aren't generated automatically.
- **Solution/ALM support**: Data and artifacts are saved to a new solution with the same name as the plan. The publisher defaults to your preferred publisher. Select the **Saved** icon in the top right corner to define the publisher.

## Related information

[FAQ for the Plan designer](../common/faq-plan-designer.md)
