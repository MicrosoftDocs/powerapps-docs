---
title: Use the Plan designer to create a business solution with Copilot (preview)
description: Learn how to use the Plan designer to create comprehensive business solutions with AI-driven experiences.
author: mduelae
contributors:
ms.topic: conceptual
ms.date: 12/20/2024
ms.author: szlo
ms.reviewer: mkaur
ms.collection:
  - bap-ai-copilot
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-title
  - ai-gen-desc
---

# Use the Plan designer (preview)

[!INCLUDE [preview-banner](../../../shared/preview-includes/preview-banner.md)]

Learn how to use the Plan designer, a copilot-first development tool, to quickly create comprehensive business solutions. Describe your business problem in natural language and provide relevant images such as business process flows or screenshots of legacy apps. The Plan designer generates a complete Power Platform solution tailored to your needs, including Dataverse tables, canvas apps, model-driven apps, and suggested Power Automate flows. Follow the steps in this article to create a business solution and refine your requirements for precise and customized outputs.

Access the Plan designer from the Power Apps home page. It guides you through a multi-step process to generate user roles, user stories, data tables, and user experiences.

:::image type="content" source="media/pd-1-enter-problem.png" alt-text="Screenshot of entering a business problem in the Plan designer." lightbox="media/pd-1-enter-problem.png":::

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2189520), and are available before an official release so that customers can get early access and provide feedback.

## Prerequisite

On the Power Apps home page, turn on the **Try the new Power Apps experience** toggle. You should see the **Create a solution for almost any business problem** banner at the top.

:::image type="content" source="media/pd-3-enable-settings.png" alt-text="Screenshot of the Power Apps home page with the new Copilot experience banner." lightbox="media/pd-4-enter-sample-problem.png":::


## Create a plan

To show you how the Plan designer works, let's use a sample scenario to build a solution for managing paid time off (PTO) requests for employees and managers.

1. Sign in to [Power Apps](https://make.powerapps.com).

1. In the textbox, type **Employees need to log vacation days, and managers need to approve them**. You can also provide more context like process diagrams, data models, or screenshots of legacy apps. When you're done, press **Enter**.

   :::image type="content" source="media/pd-4-enter-sample-problem.png" alt-text="Screenshot of the Plan designer with a sample scenario input." lightbox="media/pd-3-enable-setting.png":::

   Copilot opens the Plan designer and begins creating a plan by identifying the user roles needed to address your business scenario based on your description.

   :::image type="content" source="media/pd-5-plan-loading.png" alt-text="Screenshot of the Plan designer generating user roles." lightbox="media/pd-5-plan-loading.png":::

### Generate user roles and user stories

Copilot shows you the user roles and stories that it generated based on your description.

In this scenario, two roles were generated: employee and manager. Each role comes with its own descriptions and user stories. On the left side, the user roles and stories are presented in a bullet list, while a visual diagram is shown on the right side.

:::image type="content" source="media/pd-6-generate-roles-stories.png" alt-text="Screenshot of the generated user roles and stories in the Plan designer." lightbox="media/pd-6-generate-roles-stories.png":::

1. Review the user roles and stories. Then, choose one of the following options:

    - Select **Accept** to generate a data model.
    - Select **Change** to provide feedback for the generated user roles or stories. You can select a specific user role and enter your feedback.

1. If you need to make any changes, provide a brief description of what you want to modify. Here are examples of what you can ask Copilot to do:

    - Add a user role for HR admin to monitor PTO across teams to manage payroll.
    - Add a user story for employees to view PTO blackout dates.
    - Remove the user story for managers for viewing vacation history of team members.

1. Review the changes and select **Keep** or **Undo**. When you're done, select **Accept** to move on to the next step and generate data tables.

    :::image type="content" source="media/pd-7-keep-or-undo.png" alt-text="Screenshot of the Plan designer showing updated user roles and stories." lightbox="media/pd-7-keep-or-undo.png"::: 

### Generate data tables

1. The proposed data tables are listed in the **Data** section of the plan. Select **Show details** to view the data in a diagram.

      :::image type="content" source="media/pd-8-show-detailed-data.png" alt-text="Screenshot of the proposed data tables in the Plan designer." lightbox="media/pd-8-show-detailed-data.png":::

1. **Show details** opens the data workspace, where you can view the complete Entity Relationship Diagram (ERD) containing all the generated tables. These Dataverse tables come with predefined columns and sample data. To see the specific details of a table, select **View data**.

      :::image type="content" source="media/pd-9-view-data.png" alt-text="Screenshot of the data workspace showing the ERD." lightbox="media/pd-9-view-data.png":::

      :::image type="content" source="media/pd-10-view-data-2.png" alt-text="Screenshot of the data workspace with table details." lightbox="media/pd-10-view-data-2.png":::

> [!IMPORTANT]
> During preview, the data workspace experience is read-only. The following items are not supported:
> - Editing tables or columns
> - Editing relationships between tables
> - Adding existing tables

### Edit tables

1. To modify the proposed tables, navigate back to the Plan designer and select **Change**.

1. When you're ready to generate user experiences, select **Save tables**.

      :::image type="content" source="media/pd-11-save-tables.png" alt-text="Screenshot of the Plan designer with the option to save tables." lightbox="media/pd-11-save-tables.png":::

### Generate user experiences

The Plan designer proposes a set of user experiences tailored to solve your business problem. In this scenario, a canvas app, a model-driven app, and two Power Automate flows are created. These user experiences are designed for specified user roles and with data tables generated from the previous steps.

:::image type="content" source="media/pd-12-generate-user-exp.png" alt-text="Screenshot of the proposed user experiences in the Plan designer." lightbox="media/pd-12-generate-user-exp.png":::

To view details of the proposed user experiences, hover over the **information icon**. The pop-up info card displays the name, description, targeted user role, and the included data tables.

:::image type="content" source="media/pd-13-more-info-about-plan.png" alt-text="Screenshot of the information icon pop-up with user experience details." lightbox="media/pd-13-more-info-about-plan.png":::

To make changes, select **Change** and follow the steps above. Or select **Accept** to create the assets.

### Accept user experiences

Once you accept the proposed user experiences, they're created. To open a canvas app or model-driven app, select the plus icon (**+**).  Opening precreated Power Automate flows isn't supported; it navigates to the Power Automate page within your solution.

:::image type="content" source="media/pd-14-open-app.png" alt-text="Screenshot of the Plan designer with the option to open created apps.":::

The proposed apps open in a new tab, fully functioning with the added data tables.

For canvas apps, a preview of the app is displayed with a welcome screen and other screens connected to tables. When you open a model-driven app, it launches the modern app designer with the tables already added. Both canvas and model-driven apps can then be saved and published for use.

## View and edit plans

When you start using the Plan designer, the **Plans** menu appears in the left navigation pane. You can access all of your plans and make any necessary edits.

:::image type="content" source="media/pd-your-plans.png" alt-text="View or edit your plans." lightbox="media/pd-your-plans.png" :::

1. **Plans**: Menu to access all your plans
1. **Your plans**: View your plans.
1. **Edit**: Edit the selected plan.
1. **Edit or Delete**: Edit or delete the selected plan.

## Known limitations

- **Inline editing user roles and user stories**: Direct inline editing of content isn't supported. All changes must be prompted in Copilot first to regenerate iterations.
- **Edit tables in Data workspace**: Editing Dataverse tables generated from the Plan designer isn't supported.
- **Add existing tables in Data workspace**: Adding existing tables in the data workspace within the Plan designer isn't currently supported.
- **Supported user experiences**: The Plan designer only generates canvas apps, model-driven apps, and suggested Power Automate flows.
- **Generated Power Automate flows**: Power Automate flows created in the Plan designer take you to the Power Automate page but aren't automatically generated.
- **Solution/ ALM support**: Data and artifacts are saved to a new solution with the same name as the plan. The publisher defaults to your preferred publisher. You can define the publisher using the save icon in the top right corner.
