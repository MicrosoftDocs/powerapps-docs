---
title: "Add a Power BI visual in a model-driven app"
description: "Learn how to add Power BI visuals into model-driven apps"
ms.date: 10/10/2024
ms.topic: tutorial
author: joel-lindstrom
ms.author: matp
ms.reviewer: matp
---

# Add a Power BI visual into a model-driven app

Power BI is a powerful analysis and visualization tool. Power Apps is great at enabling people to take action via the web and mobile. With Power Apps, a Power BI dashboard can be embedded in an app. Similarly, a Power BI report tile can be added to an app. The best of both worlds can be achieved at the same place and at the same time.

In this tutorial, you create a quick Power BI report and a model-driven app. Then, you see how to add the report as a dashboard in the app.

## Prerequisites

To complete this tutorial, you need the following:

- Ability to create Power BI dashboards and reports in Power BI.
- Enable the Power BI visualization embedding setting for your environment from the Power Platform admin center. More information: [Manage feature settings](/power-platform/admin/settings-features#embedded-content)

## Create a workspace, dashboard, and report

First you sign in to Power BI, create a workspace, and then add a Power BI report and dashboard.

1. Sign in to [Power BI](https://powerbi.microsoft.com) with the same Microsoft Office subscription as the one you use for creating apps in Power Apps.

1. Select **Workspaces** on the left navigation pane, and then select **New workspace**.

<!-- Outdated   ![Select Create a workspace](media/add-a-power-bi-visual-into-a-model-driven-app/create-a-new-workspace-2.png "Select Create a workspace") -->

1. Enter a name for the workspace, such as *Power BI in Power App demo*, and then select **Apply**.

   The workspace is created. 
   ![The workspace gets created](media/add-a-power-bi-visual-into-a-model-driven-app/create-a-new-workspace-4.png "The workspace gets created")

1. Select **New item**, select **Dashboard**, enter a **Name**, and then select **Create**.

1. Select **Workspaces** on the left navigation pane, and then select the workspace you created in the previous step.
1. Select **New item**, and then select **Dataset** to create a new dataset.

1. Select the **Samples** link under **More ways to create your own content** to use sample data.

   ![Select the samples hyperlink](media/add-a-power-bi-visual-into-a-model-driven-app/create-a-new-workspace-9.png "Select the Samples hyperlink")

1. Select a sample, such as **Sales and Marketing Sample**.

   ![Select the Sales and Marketing sample](media/add-a-power-bi-visual-into-a-model-driven-app/create-a-new-workspace-10.png "Select the Sales and Marketing sample")

1. Select **Connect** to connect to the data sample.

   ![Select the Connect button to connect to the data sample](media/add-a-power-bi-visual-into-a-model-driven-app/create-a-new-workspace-11.png "Select the Connect button to connect to the data sample")

      A dataset with the sample, such as **Sales and Marketing Sample**, and a report is added to the workspace.

      ![Dataset with the sample, such as the Sales and Marketing Sample, and a report gets added](media/add-a-power-bi-visual-into-a-model-driven-app/create-a-new-workspace-12.png "Dataset with the Sales and Marketing sample and a report gets added")

1. On the left pane, select the report that was created from the dataset, such as the **Sales and Marketing Sample** report. Then, on the command bar, select **...** (ellipsis), and then select **Pin to dashboard**.

   ![Select the Pin to dashboard option](media/add-a-power-bi-visual-into-a-model-driven-app/create-a-new-workspace-13.png "Select the Pin to dashboard option")

1. Select **Existing dashboard**, select the dashboard, and then select **Pin live**.

   ![Select the dashboard and select Pin live](media/add-a-power-bi-visual-into-a-model-driven-app/create-a-new-workspace-14.png "Select the dashboard and select Pin live")

   The report is now added to the dashboard and is available in Power BI.

## Add the dashboard and report to a solution

In this section, you create a solution in Power Apps that includes a Power BI embedded dashboard.

1. Sign in to [Power Apps](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), on the left navigation pane select **Solutions**. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Create a new solution or open an existing unmanaged solutoin.

1. Open the solution and select **New** > **Dashboard** > **Power BI Embedded**.

<!-- These steps for the sales and marketing samples no longer work
Revise using the Excel file to build a report here https://learn.microsoft.com/en-us/power-bi/create-reports/service-from-excel-to-stunning-report
-->
1. Select or enter the following options, and then select **Save**:
   - **Display name**: *Test Embedded BI Report*
   - **Type**: **Power BI report**
   - **Power BI workspace**: **Power BI in Power App Demo** (the workspace you created earlier)
   - Clear **Show reports in this environment only**.
   - **Power BI report**: **Sales and Marketing Sample** (the report you created earlier)

     ![Enter the Display name Test Embedded BI Report](media/add-a-power-bi-visual-into-a-model-driven-app/add-the-dashboard-and-report-to-a-solution-5.png "Enter the Display name Test Embedded BI Report")
   
   A Power BI embedded dashboard is created and ready to add to a model-driven app.

## Create a new model-driven app and add the Power BI embedded report

In this section, you create a model-driven app and add the Power BI embedded report you created earlier.

1. Sign in to [Power Apps](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), select the environment you want, and then on the left navigation pane, select **Apps**.

   ![Go to make.powerapps.com](media/add-a-power-bi-visual-into-a-model-driven-app/create-a-new-model-driven-app-1.png "Go to make.powerapps.com")

1. On the command bar, select **+New app**, and then select **Model-driven**.

   ![Select Model-driven from the New app dropdown](media/add-a-power-bi-visual-into-a-model-driven-app/create-a-new-model-driven-app-2.png "Select Model-driven from the New app dropdown")

1. Enter a **Name** for the model-driven app, and then select **Done**.

   ![Enter a Name for the model-driven app](media/add-a-power-bi-visual-into-a-model-driven-app/create-a-new-model-driven-app-3.png "Enter a Name for the model-driven app")
   The model-driven app designer opens.
1. Select the **Edit Site Map** pencil icon, to open the sitemap designer.

   ![Select the Edit Site Map button to open the Site Map](media/add-a-power-bi-visual-into-a-model-driven-app/create-a-new-model-driven-app-4.png "Select the Edit Site Map button to open the Site Map")

1. Select **New subarea** on the site map. Then select the following **Properties**, and then select **Save**:
   - **Type**: **Dashboard**
   - **Default Dashboard**: **Test Embedded BI Report**
   - **Title**: **Test Embedded BI**

    ![Save and then Publish](media/add-a-power-bi-visual-into-a-model-driven-app/create-a-new-model-driven-app-5.png "Save and then Publish")

1. Select **Publish**, and then select **Save and Close** to close the sitemap designer.
1. On the app designer command bar select, **Save**, then **Validate**, and then select **Publish**.

   ![On the App Designer select Validate and then select Publish](media/add-a-power-bi-visual-into-a-model-driven-app/create-a-new-model-driven-app-6.png "On the App Designer select Validate and then select Publish")

1. On the command bar, select **Play**.

   ![Select the Play button on the top right to Play the app](media/add-a-power-bi-visual-into-a-model-driven-app/create-a-new-model-driven-app-7.png "Select the Play button on the top right to Play the app")

   The app opens with the **New BI Dashboard**.

   ![select the Test Embedded BI Report from the dropdown list](media/add-a-power-bi-visual-into-a-model-driven-app/create-a-new-model-driven-app-8.png "select the Test Embedded BI Report from the dropdown")

1. Select  **New BI Dashboard** to reveal the dashboard dropdown list, and then select **Test Embedded BI Report**.
  
   Notice how the report named **Test Embedded BI Report** is embedded in the model-driven app.

   ![BI report is embedded in the model-driven app](media/add-a-power-bi-visual-into-a-model-driven-app/create-a-new-model-driven-app-9.png "BI report is embedded in the model-driven app")

### See also
[Use Power BI with model-driven apps](use-power-bi.md)
