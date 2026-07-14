---
title: "Create or edit a Power BI embedded system dashboard"
description: Set up and use a system dashboard that references a Power BI report or dashboard in a model-driven app.
ms.custom: ""
ms.date: 01/18/2025
ms.reviewer: "matp"
ms.topic: "how-to"
ms.subservice: mda-maker
ms.author: "aorth"
author: "adrianorth"
search.audienceType: 
  - maker
---
# Create or edit a Power BI embedded system dashboard

This article explains how to set up and use a system dashboard that references a Power BI report or dashboard in a model-driven app. System administrators and system customizers can create system reports and dashboards, which can be made available to model-driven app users.  Users need to have the relevant Power BI license and authorization to consume content.  

> [!NOTE]
> Power BI embedded in a system dashboard or form ignores the Power Platform admin center **Power BI visualization embedding** environment setting. That setting controls whether end users can add embedded Power BI reports to personal views, charts, and dashboards.

:::image type="content" source="media/example-pbi-embedded-runtime.png" alt-text="Example Power BI report in a model-driven app" lightbox="media/example-pbi-embedded-runtime.png":::

Read more about relevant Power BI licenses at [Power BI pricing](https://powerbi.microsoft.com/en-us/pricing/).

To learn more about Power BI reports and dashboards, go to [Create reports and dashboards in Power BI](/power-bi/create-reports/).

## Create a system dashboard with Power BI embedded

This procedure shows you how to set up a Power BI embedded page for a single environment connected to a Power BI workspace.

1. Select **Solutions** on the left navigation pane in Power Apps (make.powerapps.com), and then create or open an existing solution. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]

1. Select **New** > **Dashboards** > **Power BI embedded**.

1. Enter or select the following properties in the **New Power BI embedded** dialog that appears:
   - Enter a **Display name** for the dashboard, which will be shown to the user in the selector on the **Dashboards** page.
   - Select the type, either **Power BI report** or **Power BI dashboard**.
   - If you clear **Show reports in this environment only**, you can select a Power BI report or a Power BI dashboard from another workspace.
   - Select **Use environment variable** if you want to replace a static workspace and report to use an environment variable from configuration. You use this option when you want to move the report to another environment in a solution. More information: [Environment variables overview](../data-platform/EnvironmentVariables.md) and [Create Power BI embedded page with an environment variable](#create-power-bi-embedded-page-with-an-environment-variable) 
   - Select a **Power BI workspace**.
   - Select a Power BI report or dashboard.
   :::image type="content" source="media/create-edit-powerbi-embedded-page/new-dashboard-powerbi-embedded-panel.png" alt-text="New dashboard Power BI embedded panel"::: 

1. Select **Save** to save and publish the system dashboard.

## Add a Power BI embedded page to a model-driven app

1. Create or edit an existing model-driven app using the app designer.
1. In the app designer select **Add page** > **Dashboard**.
1. Select the **System dashboards** picker, and then select **Power BI dashboards**.
1. Select the Power BI dashboard you want, and then select **Add**.
1. Select the **Dashboards** subarea on the app designer canvas.
1. Select **Save**. To make your changes available to users, select **Save and Publish**.

## Select the Power BI embedded page in the model-driven app

1. Play the model-driven app, and then select a dashboard from the left navigation pane.
1. Select the Power BI embedded page to perform actions, such as expand, copy as image, and filter.
:::image type="content" source="media/example-pbi-embedded-runtime.png" alt-text="Example Power BI report in a model-driven app" lightbox="media/example-pbi-embedded-runtime.png":::

## Create Power BI embedded page with an environment variable

When a solution with a Power BI embedded component will be moved to other environments, you can turn on **Use environment variable** to configure the dashboard. For each environment, you specify the workspace and either a dashboard or report to reference. Environment variables allow configuration without unmanaged customizations.

1. When you create or edit an existing Power BI embedded system dashboard in Power Apps (make.powerapps.com), select **Use environment variable**.
   create-edit-powerbi-embedded:::image type="content" source="media/create-edit-powerbi-embedded-page/power-bi-embedded-use-environment-variable.png" alt-text="Use an environment variable for the Power BI report":::
1. Open the **Power BI environment variable** selector and then select **New environment variable**.
   :::image type="content" source="media/create-edit-powerbi-embedded-page/power-bi-embedded-new-environment-variable.png" alt-text="Select a new environment variable.":::

    A nested panel opens where you create the environment variable. The environment variable properties are automatically filled using the dashboard **Display Name** and **Name**.

    You can configure the workspace and report or dashboard. The values are stored as JSON. More information: [Environment variables overview](../data-platform/environmentvariables.md)
    :::image type="content" source="media/create-edit-powerbi-embedded-page/powerbi-embedded-env-var-panel.png" alt-text="Power BI embedded environment variable panel.":::

1. Save the environment variable. The default and current values for workspace and report or dashboard are displayed.
   :::image type="content" source="media/create-edit-powerbi-embedded-page/power-bi-embedded-environment-variable-value-preview.png" alt-text="Power BI embedded environment variable value preview.":::

### See also

[Create or edit model-driven app dashboards](create-edit-dashboards.md) <br />
[View table data in Power BI Desktop](../data-platform/view-entity-data-power-bi.md) <br />
[Use Power BI](use-power-bi.md) <br />
[Use Power BI with Microsoft Dataverse](../data-platform/use-powerbi-dataverse.md) <br />
[Create a Power BI report using the Common Data Service connector](../data-platform/data-platform-powerbi-connector.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
