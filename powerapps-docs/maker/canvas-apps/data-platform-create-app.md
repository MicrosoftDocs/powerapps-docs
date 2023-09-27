---
title: Create a canvas app with data from Microsoft Dataverse (contains video)
description: Learn about how to automatically create a canvas app to manage data in Microsoft Dataverse.
author: mduelae

ms.topic: quickstart
ms.custom: canvas
ms.collection: get-started
ms.reviewer: 
ms.date: 01/27/2022
ms.subservice: canvas-maker
ms.author: tapanm
search.audienceType: 
  - maker
contributors:
  - mduelae
  - lancedmicrosoft
---
# Create a canvas app with data from Microsoft Dataverse

In Power Apps, create a canvas app based on a list of sample accounts in [Dataverse](../data-platform/data-platform-intro.md). In this app, you can browse all accounts, show details of a single account, and create, update, or delete an account.

If you're not signed up for Power Apps, [sign up for free](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) before you start.

## Prerequisites

To follow this quickstart, you must be assigned to the [Environment Maker](/power-platform/admin/database-security#predefined-security-roles) security role, and you must [switch to an environment](intro-maker-portal.md#choose-an-environment) in which a database in Dataverse has been created, contains data, and allows updates. If no such environment exists and you have administrative privileges, you can [create an environment](/power-platform/admin/create-environment) that meets this requirement.

## Create an app

1. Sign in to [Power Apps](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
2. Depending on how you want to create your app, from the home screen, select one of the following options:
    - To create a single-page gallery app with a responsive layout, choose either:
      - **Start with data** > **Select an existing table**.
      - **Start with a page design** > **Gallery connected to table**.
    - To create a three screen mobile app, select **Start with an app template** > **From Dataverse**.
3. Select a table, and then select **Create app**.


## Save and design the app

Your app opens in Power Apps Studio where you can design, build, and manage your app. More information: [Understand Power Apps Studio](power-apps-studio.md)

As a best practice, before you make any more changes save your work before you proceed.

1. On the command bar, select **Settings**.

1. Set the app name such as **AppGen**, change the icon to a checkmark, and the icon background color to a deep red.

1. Close the setting screen and then select the **Save** icon on upper-right corner.

 
 ## Next steps

As a next step, customize the gallery and other elements of the default browse screen to better suit your needs. More information: [Customize a gallery in Power Apps](customize-layout-sharepoint.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
