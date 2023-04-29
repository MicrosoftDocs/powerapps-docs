---
title: Create a canvas app with data from Microsoft Dataverse (contains video)
description: Learn about how to automatically create a canvas app to manage data in Microsoft Dataverse.
author: mduelae

ms.topic: quickstart
ms.custom: 
  - canvas
  - intro-internal
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

Depending upon whether you have the [new look](intro-maker-portal.md#new-look) or [classic look](intro-maker-portal.md#classic) turned on, select the appropriate tab below to know more.

# [New look](#tab/home-new-look)

1. Sign in to [Power Apps](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. From the home screen select, **Start with data** > **Select an existing table**.
1. On the **Select a Dataverse table**, select your table, and then select **Create app**.
1. If the **Welcome to Power Apps Studio** dialog box appears, select **Skip**.

Your app opens in Power Apps Stuido where you can design, build, and manage your app. More information: [Understand Power Apps Studio](power-apps-studio.md)


# [Classic](#tab/home-classic)

Watch this short video that shows you how to create a canvas app quickly using Dataverse tables.
> [!VIDEO https://www.microsoft.com/videoplayer/embed/RE4YzH0]


1. Sign in to [Power Apps](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and, if necessary, [switch environments](intro-maker-portal.md#choose-an-environment).

1. Under **Start from**, select **Dataverse**.

1. If this is your first time, you're prompted to create a connection to Dataverse. Select **Create** this connection.

1. Under **Choose a table**, select your table (such as **Accounts** for this example), and then select **Connect**.

1. If the **Welcome to Power Apps Studio** dialog box appears, select **Skip**.

Your app opens to the browse screen, which shows a list of accounts in a control called a gallery. Near the top of the screen, a title bar shows icons for refreshing the data in the gallery, sorting the data in the gallery alphabetically, and adding data to the gallery. Under the title bar, a search box provides the option to filter the data in the gallery based on text that you type or paste. 

By default, the gallery shows an email address, a city, and an account name. As you'll see in [Next steps](data-platform-create-app.md#next-steps), you can customize the gallery to change how the data appears and even show other types of data.

![Browse screen.](./media/data-platform-create-app/browse-screen.png)

### Save the app
You'll probably want to make more changes before you use this app or share it with others. As a best practice, save your work so far before you proceed.

1. Select **Settings**.

1. Set the app name to **AppGen**, change the background color to deep red, and change the icon to a checkmark.

1. Set the app name to **AppGen**, and select **Save**.

1. Close the settings dialog.

1. Near the left edge, select **Save as** and then, in the lower-right corner, select **Save**.

### Next steps

In this quickstart, you created an app to manage sample data about accounts in Dataverse. As a next step, customize the gallery and other elements of the default browse screen to better suit your needs. More information: [Customize a gallery in Power Apps](customize-layout-sharepoint.md)

 ---

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
