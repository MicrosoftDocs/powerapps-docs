n ---
title: Create business solutions with Copilot (preview)
description: Learn how to use the Plan Designer to create comprehensive business solutions with AI-driven experiences.
author: mduelae
contributors:
ms.topic: conceptual
ms.date: 11/21/2024
ms.author: szlo
ms.reviewer: mkaur
ms.collection:
  - bap-ai-copilot
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-title
  - ai-gen-desc
---

# Create business solutions with Copilot (preview)

[!INCLUDE [preview-banner](../../../shared/preview-includes/preview-banner.md)]


The Plan Designer is an AI-driven tool that creates a business solution in minutes. Describe your business problem in natural language and include images like a legacy app or process diagram. You'll receive an outline of user roles and requirements. It generates a complete Power Platform solution with Dataverse tables, Power Apps (canvas and model-driven apps), and Power Automate flows. You can refine your requirements to produce a more precise output tailored to your needs.

Accessible directly from the Power Apps home page, the Plan Designer guides you through a multi-step process to generate user roles, user stories, data tables, and the appropriate user experiences.

:::image type="content" source="media/plan-designer/pd-1-enter-problem.png" alt-text="Screenshot of entering a business problem in the Plan Designer.":::

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2189520), and are available before an official release so that customers can get early access and provide feedback.
> - The Plan designer is only available in the US region during preview. 

## Prerequisite

1. **Turn on the new Copilot experience**: On the Power Apps home page, turn on the **Try the new Power Apps experience** toggle. You should see the **Create a solution for almost any business problem** banner at the top.

  :::image type="content" source="media/plan-designer/pd-3-enable-setting.png" alt-text="Screenshot of the Power Apps home page with the new Copilot experience banner.":::

## Create a plan

Let's use a sample scenario to build a solution for managing paid time off (PTO) requests for employees and managers.

1. Sign in to [Power Apps](https://make.powerapps.com).

1. In the textbox, type **Employees need to log vacation days, and managers need to approve them**. Optionally, provide more context like process diagrams, data models, or screenshots of legacy apps. When you're done, press Enter.

  :::image type="content" source="media/plan-designer/pd-4-enter-sample-problem.png" alt-text="Screenshot of the Plan Designer with a sample scenario input.":::

  Copilot opens the Plan Designer and begin creating a plan by identifying the user roles needed to address your business scenario based on your description.

  :::image type="content" source="media/plan-designer/pd-5-plan-loading.png" alt-text="Screenshot of the Plan Designer generating user roles.":::

## Generate user roles and user stories

Copilot shows you the user roles and stories that it generated based on your description.

In this example, it generated two roles: Employee and Manager, along with their descriptions and user stories. On the left-hand side, you can see the user roles and stories in a bullet list, while a visual diagram is displayed on the right.

:::image type="content" source="media/plan-designer/pd-6-generate-roles-stories.png" alt-text="Screenshot of the generated user roles and stories in the Plan Designer.":::

1. Review the user roles and user stories and select one of the following options:

    - Select **Accept:** To generate a data model. This is the next step in the plan.
    - Select **Change**: To provide feedback for the generated user roles or stories. You can select a specific user role and then enter your feedback.

1. If you want to change something, enter a brief description of the change you want to make. Here’s a few examples of what you can ask Copilot to do:

    - Add a user role for HR admin to monitor PTO across teams to manage payroll.
    - Add a user story for employees to view PTO blackout dates.
    - Remove the user story for managers for viewing vacation history of team members.

1. When you get the updated results, review the changes and choose either **Keep** or **Undo**. When you’re satisfied, select **Accept** to proceed to the next step to generate data tables.

    :::image type="content" source="media/plan-designer/pd-7-keep-or-undo.png" alt-text="Screenshot of the Plan Designer showing updated user roles and stories."::: 

## Generate data tables

1. The proposed data tables are listed in the **Data** section of the plan. Select **Show details** to view the data in a diagram.

      :::image type="content" source="media/plan-designer/pd-8-show-detailed-data.png" alt-text="Screenshot of the proposed data tables in the Plan Designer.":::

1. **Show details** opens the data workspace, where you can view the complete Entity Relationship Diagram (ERD) containing all the generated tables. These Dataverse tables come with predefined columns and sample data. To see the specific details of a table, select **View data**.

      :::image type="content" source="media/plan-designer/pd-9-view-data.png" alt-text="Screenshot of the data workspace showing the ERD.":::

      :::image type="content" source="media/plan-designer/pd-10-view-data-2.png" alt-text="Screenshot of the data workspace with table details.":::

> [!IMPORTANT]
> During preview, the data workspace experience is read-only. The following items are not supported in data workspace:
> - Edit tables or columns
> - Editing relationships between tables
> - Add existing tables

## Edit tables

1. If you want to modify the proposed tables, navigate back to the Plan Designer and select **Change**.

1. When you’re ready to generate user experiences, select **Save tables**.

      :::image type="content" source="media/plan-designer/pd-11-save-tables.png" alt-text="Screenshot of the Plan Designer with the option to save tables.":::

## Generate user experiences

The Plan Designer proposes a set of user experiences tailored to solve your business problem. For our sample scenario, a canvas app, a model-driven app, and two Power Automate flows are created. These user experiences are designed for specified user roles and with data tables generated from the previous steps.

:::image type="content" source="media/plan-designer/pd-12-generate-user-exp.png" alt-text="Screenshot of the proposed user experiences in the Plan Designer.":::

To view details of the proposed user experiences, hover over the **information icon**. The pop-up info card shows the name, description, targeted user role, and the data tables included.

:::image type="content" source="media/plan-designer/pd-13-more-info-about-plan.png" alt-text="Screenshot of the information icon pop-up with user experience details.":::

To make changes, select **Change** and follow the steps as mentioned above. Or select **Accept** to create the assets.

## Accept user experiences

Once you accept the proposed user experiences, they'll then be created. To open a canvas app or model-driven app, select the **plus icon**. Opening Power Automate flows with the flow precreated isn't supported. It navigates to the Power Automate page within your solution.

:::image type="content" source="media/plan-designer/pd-14-open-app.png" alt-text="Screenshot of the Plan Designer with the option to open created apps.":::

The proposed apps open in a new tab, with the added data tables as a fully functioning app.

For canvas apps, you’ll see a preview of the canvas app with a welcome screen along with other screens with tables connected. Opening a model-driven app launches the Modern app designer with the tables already added. Both canvas and model-driven apps can then be saved and published to be used.

## Known limitations

- **Inline editing user roles and user stories**: Currently, you can't inline edit the content directly. All changes must be prompted in copilot first to regenerate iterations.
- **Edit tables in Data workspace**: Editing Dataverse tables generated from the Plan designer isn't supported.
- **Add existing tables in Data workspace**: Adding existing tables in data workspace in the Plan designer isn't currently supported.
- **Supported user experiences**: Currently, the only supported artifacts that the Plan designer can generate are canvas apps, model-driven apps, and suggested Power Automate flows.
- **Generated Power Automate flows**: Power Automate flows generated in the Plan designer takes you to the Power Automate page but will not be automatically generated. 
- **Solution/ ALM support**: Data and artifacts are saved to a new solution matching the name of the plan. The publisher defaults to the preferred publisher in your preferred solution. You can define the publisher in the save icon on the top right corner. 
