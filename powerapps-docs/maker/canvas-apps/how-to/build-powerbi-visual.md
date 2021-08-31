---
title: How to build a canvas app with Power BI visual
description: Learn about how to build a canvas app with Power BI visual.
author: joel-lindstrom
ms.service: powerapps
ms.topic: article
ms.custom: canvas
ms.reviewer:
ms.date: 08/31/2021
ms.subservice: canvas-maker
ms.author: emcoope
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
    - joel-lindstrom
    - tapanm-msft
---

# How to build a canvas app with Power BI visual

Microsoft Power BI is a powerful analysis and visualization tool. Power Apps is great at enabling people to take action on the web and mobile. Canvas apps created using Power Apps can be embedded in a Power BI report. Similarly, a Power BI report tile can be added to a canvas app. The best of both worlds can be achieved at the same place and same time.

In this example, we'll create a quick Power BI report and a canvas app, and then see how we can add the report as a tile in the app.

## Prerequisites

To complete this lesson, we'd need the ability to create Power BI dashboards and reports.

## Sign in to Power BI

Sign in to Power BI with the same Office license as the one used for creating the Power Apps.

## Create a new workspace

1. Select **Workspaces** from the left-pane.

    ![Select the Workspaces link](media/build-powerbi-visual/create-a-new-workspace-1.png "Select the Workspaces link")

1. Select **Create a workspace**.

    ![Select the Create a workspace button](media/build-powerbi-visual/create-a-new-workspace-2.png "Select the Create a workspace button")

1. Enter a name for the workspace, and then select **Save**.

    ![Enter a name for the workspace](media/build-powerbi-visual/create-a-new-workspace-3.png "Enter a name for the workspace")

    The workspace gets created

    ![The workspace gets created](media/build-powerbi-visual/create-a-new-workspace-4.png "The workspace gets created")

1. Select **+ New**, and add a dashboard.

    ![Select the New button and add a Dashboard](media/build-powerbi-visual/create-a-new-workspace-5.png "Select the New button and add a Dashboard")

1. Add a name for the dashboard, then select **Create**.

    ![Add a name for the dashboard](media/build-powerbi-visual/create-a-new-workspace-6.png "Add a name for the dashboard")

    The Power BI dashboard gets created within the workspace we created

    ![The Power BI Dashboard gets created](media/build-powerbi-visual/create-a-new-workspace-7.png "The Power BI Dashboard gets created")

1. Open the workspace, select **+ New**, and then select **Dataset** to create a new dataset.

    ![Open the workspace and select the New button](media/build-powerbi-visual/create-a-new-workspace-8.png "Open the workspace and select the New button")

1. Select **Samples** under "More ways to create your own content to use sample data”.

    ![Select the Samples hyperlink](media/build-powerbi-visual/create-a-new-workspace-9.png "Select the Samples hyperlink")

1. Select **Sales and Marketing sample**. You can also select another sample of your choice.

    ![Select the Sales and Marketing sample](media/build-powerbi-visual/create-a-new-workspace-10.png "Select the Sales and Marketing sample")

1. Select **Connect** to connect to the sample data.

    ![Select the Connect button to connect to the data sample](media/build-powerbi-visual/create-a-new-workspace-11.png "Select the Connect button to connect to the data sample")

    A dataset with the Sales and Marketing sample and a report gets added to the Workspace.

    ![Sample and a report gets added to the workspace](media/build-powerbi-visual/create-a-new-workspace-12.png "Sample and a report gets added to the workspace")

1. From the left-pane, select the report that was created from the dataset, select **...** (ellipsis), and select then select **Pin to a dashboard**.

    ![Select the Pin to dashboard option](media/build-powerbi-visual/create-a-new-workspace-13.png "Select the Pin to dashboard option")

1. Select **Existing dashboard**, select the dashboard, and then select **Pin live**.

    ![Select the dashboard and select Pin live](media/build-powerbi-visual/create-a-new-workspace-14.png "Select the dashboard and select Pin live")

The report gets added to the dashboard, and is ready for use in Power Apps.

## Create a new canvas app

1. Sign in to [Power Apps](https://make.powerapps.com), and then select **Create**.

    ![Go to make powerapps com](media/build-powerbi-visual/create-a-new-canvas-app-1.png "Go to make powerapps com")

1. Enter a name, and select **Create**.

    ![Give the app a name and select Create](media/build-powerbi-visual/create-a-new-canvas-app-2.png "Give the app a name and select Create")

    App gets created.

    ![The canvas app gets created](media/build-powerbi-visual/create-a-new-canvas-app-3.png "The canvas app gets created")

1. Select **Insert** > **Charts** > **Power BI tile**.

    ![Select Inser Charts and select Power BI Tile](media/build-powerbi-visual/create-a-new-canvas-app-4.png "Select Inser Charts and select Power BI Tile")

    The Power BI Tile gets added to the screen.

    ![The Power BI Tile gets added to the screen](media/build-powerbi-visual/create-a-new-canvas-app-5.png "The Power BI Tile gets added to the screen")

1. Select the Workspace, dashboard and tile created earlier to add the Power BI tile to the canvas app.

    ![Power BI Tile is added to the canvas app](media/build-powerbi-visual/create-a-new-canvas-app-6.png "Power BI Tile is added to the canvas app")

1. [Save and publish](../save-publish-app.md) the app.

You've created a canvas app with Power BI tile.

### See also

- [Connect to Power BI from Power Apps](../connections/connection-powerbi.md)
- [Power Apps visual for Power BI](../powerapps-custom-visual.md)
- [Power BI tile control in Power Apps](../controls/control-power-bi-tile.md)
- [Tutorial: Embed a Power Apps visual in a Power BI report](/power-bi/visuals/power-bi-visualization-powerapp)
