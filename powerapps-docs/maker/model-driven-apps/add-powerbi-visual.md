---
title: "Add a Power BI visual in a model-driven app"
description: "Learn how to add Power BI visuals into model-driven apps"
ms.date: 10/10/2024
ms.topic: tutorial
author: Mattp123
ms.author: matp
ms.reviewer: matp
ms.subservice: mda-maker
---
# Add a Power BI visual to a model-driven app

Power BI is a powerful analysis and visualization tool. Power Apps is great at enabling people to take action via the web and mobile. With Power Apps, a Power BI dashboard can be embedded in an app. Similarly, a Power BI report tile can be added to an app. The best of both worlds can be achieved at the same place and at the same time.

In this article, you create a simple Power BI report and a model-driven app. Then, you learn how to add the report as a dashboard in the app.

## Prerequisites

To complete this tutorial, you need the following:

- Ability to create Power BI dashboards and reports in Power BI.
- Enable the Power BI visualization embedding setting for your environment from the Power Platform admin center. More information: [Manage feature settings](/power-platform/admin/settings-features#embedded-content)

## Create a workspace, dashboard, and report

If you don't already have a workspace with a Power BI report, follow these steps to create one. If you do have one, go to [Add the dashboard and report to a solution](#add-the-dashboard-and-report-to-a-solution).

1. Download the [Excel financial sample Excel workbook](https://go.microsoft.com/fwlink/?LinkID=521962).
1. Sign in to [Power BI](https://powerbi.microsoft.com) with the same Microsoft Office subscription as the one you use for creating apps in Power Apps.
1. Select **Workspaces** on the left navigation pane, and then select **New workspace**.
1. Enter a name for the workspace, such as *Contoso Power BI workspace*, and then select **Apply**.
1. Select **New item**, select **Dashboard**, enter a **Name**, and then select **Create**.
1. Select Workspaces on the left navigation pane and select the workspace you created. Select **New item** > **Report**.
1. Select **Excel**, select **Upload file**, select **Browse**, locate and select the **Financial Sample.xlsx** file you downloaded previously, and then select **Open**.
1. When the file has been uploaded select **Sign in**, and then select **Next**.
1. Select the **financials** tab, and then select **Create**.
1. Now, build a visual:

   - Expand **financials** in the right-hand **Data** pane, and drag **Profit** to the report canvas.
   - Drag **Date** and drop it on top of the **Profit** chart.
   - Drag an edge of the chart to resize it.
   - Select the chart and then select the forked double arrows to show quarters, then select them again to show months.

   :::image type="content" source="media/add-a-power-bi-visual-into-a-model-driven-app/sample-pbi-report.png" alt-text="Sample Power BI report with date and profit information" lightbox="media/add-a-power-bi-visual-into-a-model-driven-app/sample-pbi-report.png":::

1. Save your report as *Financial Samples*.

## Add the dashboard and report to a solution

In this section, you create a solution in Power Apps that includes a Power BI embedded dashboard object.

1. Sign in to [Power Apps](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), on the left navigation pane select **Solutions**. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Create a new solution or open an existing unmanaged solution.
1. Open the solution and select **New** > **Dashboard** > **Power BI Embedded**.
1. In the right properties pane, enter or select the following properties:

   - **Name**. *Test Embedded BI Report*
   - Clear the **Show reports in this environment only** option.
   - **Type**: **Power BI report**
   - **Power BI workspace**: Locate and select the workspace you created earlier, such as **Contoso Power BI workspace**.
   - **Power BI Report**: Locate and select the **Financial Sample** report you created for the workspace.

1. Select **Save**.
1. Select **Publish** on the command bar.

## Create a model-driven app and add the Power BI report

In this section, you create a model-driven app and add the Power BI embedded report you created earlier.

1. Sign in to [Power Apps](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), select the environment you want, and then on the left navigation pane, select **Solutions**.
1. Open the solution you created to add the embedded Power BI dashboard.
1. On the command bar, select **New** > **App** > **Model-driven app**.
1. Enter a **Name**, such as *Model-driven app with Power BI dashboard*, and then select **Create**.
1. In the app designer on the command bar select **Add page**, select **Dashboard**, and then in the dashboard picker select **Power BI dashboards**.
   :::image type="content" source="media/add-a-power-bi-visual-into-a-model-driven-app/dashboard-selector.png" alt-text="Select Power BI dashboards from the dashboard picker":::

1. Select the **Test Power BI report** you created earlier, and then select **Add**.

   The report is loaded in the app designer similar to how it will appear to your users when they play the app.
   :::image type="content" source="media/add-a-power-bi-visual-into-a-model-driven-app/embedded-power-bi-dashboard-in-model-driven-app.png" alt-text="Embedded Power BI report in a model-driven app dashboard" lightbox="media/add-a-power-bi-visual-into-a-model-driven-app/embedded-power-bi-dashboard-in-model-driven-app.png":::

1. Select **Save** to save your app or select **Publish** to save and publish you app making it available for users.

### See also

[Use Power BI with model-driven apps](use-power-bi.md)
