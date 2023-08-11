---
title: Create a canvas app from a template
description: Step-by-step instructions for creating a canvas app automatically based on a Power Apps template.
author: mduelae

ms.topic: conceptual
ms.custom: canvas
ms.collection: get-started
ms.reviewer: 
ms.date: 10/20/2021
ms.subservice: canvas-maker
ms.author: tapanm
search.audienceType: 
  - maker
contributors:
  - mduelae
---

# Create a canvas app from a template

Create a canvas app automatically based on a template for a specific scenario, such as tracking budgets and scheduling vacations, and then run the app to understand its default behavior.

To create an app from a template, you need a cloud-storage account (such as DropBox, OneDrive, or Google Drive) to store the template's sample data.

If you don't have a license for Power Apps, you can [sign up for free](../signup-for-powerapps.md).

## Create an app

1. Sign in to [Power Apps](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. From the home screen select, **Start with an app template**. Select a template to learn more. If you want to choose another template, select **Cancel** and then select another template.
2. Select one of the following options:
    - To create a three screen mobile app using data stored in Dataverse, select **From Dataverse**.
    - To create a three screen mobile app by connecting to an external data source, select one of these data sources:
      - **From SharePoint**
      - **From Excel**
      - **From SQL**
    - To use other templates, select a template from the list of **other app templates**.
5. After you select a template, you can update the app name and select the layout for your app. 
6. When you're done, select **Next**.


## Run the app

An app from a template opens in Power Apps Studio, where you'll spend most of your time customizing. Before you make any changes to the app, explore how the app works in [Preview](preview-app.md) mode.

1. Press F5 to open the app in preview mode. Alternatively, you can also select the play button on the top-right corner of the screen to [preview the app](preview-app.md).

    :::image type="content" source="media/get-started-test-drive/play-button.png" alt-text="Play the app":::

    The app is populated with sample data to demonstrate the functionality of the app.

1. Explore the app's default behavior by creating, updating, and deleting sample data, and then verify that the data in your cloud-storage account reflects your changes.

1. Return to the default workspace by pressing Esc (or by selecting **X** icon near the upper-right corner).

## Next steps

1. Press Ctrl-S, give your app a name, and then select **Save** to save your app to the cloud.

1. [Share your app](share-app.md) with other people in your organization.

> [!IMPORTANT]
> Before you share an app, make sure that the people with whom you're sharing it have access to the data. For example, you must [share an Excel or other file](share-app-data.md) in a cloud-storage account.

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
