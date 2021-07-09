---
title: Create a canvas app from a template
description: Step-by-step instructions for creating a canvas app automatically based on a Power Apps template.
author: tapanm-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
  - canvas
  - intro-internal
ms.reviewer: 
ms.date: 01/29/2020
ms.author: tapanm
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---

# Create a canvas app from a template

Create a canvas app automatically based on a template for a specific scenario, such as tracking budgets and scheduling vacations, and then run the app to understand its default behavior.

To create an app from a template, you need a cloud-storage account (such as DropBox, OneDrive, or Google Drive) to store the template's sample data.

If you don't have a license for Power Apps, you can [sign up for free](../signup-for-powerapps.md).

## Create an app

1. Sign in to [Power Apps](https://make.powerapps.com).

1. Select **Apps** from left navigation. Select the **New app** drop down menu and then select **Canvas**.

    ![New canvas app.](./media/get-started-test-drive/new-canvas-app.png)

    This opens [Power Apps Studio](../../powerapps-overview.md#power-apps-for-app-makerscreators) in a new tab.

1. On the **App templates** tile, select **Phone layout** or **Tablet layout**.

    ![App from template tile.](./media/get-started-test-drive/template-tile.png)

1. In the list of templates, select a template, and then select **Use** (near the lower-right corner).

    ![Open a Power Apps template.](./media/get-started-test-drive/open-template.png)

    The Power Apps Studio opens in new tab and the app gets created.

    > [!NOTE]
    > If **Use** button is disabled, ensure you have selected a data source for the app. You can select the data source by selecting **Choose** at the bottom.
    >
    > ![Choose data source.](./media/get-started-test-drive/choose-data-source.png)

## Run the app
An app from a template opens in the default workspace, where you'll spend most of your time customizing. Before you make any changes to the app, explore how the app works in **Preview** mode.

1. Press F5 (or click or tap the right arrow in the upper-right corner) to open the app in **Preview** mode.

    ![Button to open Preview mode.](./media/get-started-test-drive/open-preview.png)

    The app is populated with sample data to demonstrate the functionality of the app. For example, the Cost Estimator app contains data for creating appointments and estimating the cost of installing a specific flooring product in a room of a particular size.

4. Explore the app's default behavior by creating, updating, and deleting sample data, and then verify that the data in your cloud-storage account reflects your changes.

    For example, make an appointment, and create a cost estimate in the Cost Estimator app.

5. Return to the default workspace by pressing Esc (or by clicking or tapping the **X** icon near the upper-right corner).

## Next steps
1. Press Ctrl-S, give your app a name, and then click or tap **Save** to save your app to the cloud.

1. [Share your app](share-app.md) with other people in your organization.

> [!IMPORTANT]
> Before you share an app, make sure that the people with whom you're sharing it have access to the data. For example, you must [share an Excel or other file](share-app-data.md) in a cloud-storage account.


[!INCLUDE[footer-include](../../includes/footer-banner.md)]