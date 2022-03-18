---
title: "Create an environment in Cards"
description: "Learn how to create an environment in cards for your team"
keywords: "Power Cards, Power Cards Designer, Power Apps, Cards"
ms.date: 03/18/2022
ms.topic: article
author: eberhardts
ms.author: v-eberhardts
manager: shellyha
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Create an Environment in Power Cards

This procedure presumes you've downloaded the cards zip file.

1. Go to [make.test.powerapps.com](https://www.make.test.powerapps.com) (or [aka.ms/pcdesigner](https://www.aka.ms/pcdesigner) for internal)

1. Select gear from top bar

1. Select Admin center

    :::image type="content" source="../media/create-an-environment/select-admin-center.png" alt-text="Screenshot showing how to get to the Power Apps Admin Center." border="false":::

1. In the Admin center, select Environments from the left pane

    :::image type="content" source="../media/create-an-environment/add-new-environment.png" alt-text="Screenshot showing how to add a new environment to Power Apps." border="false":::

1. Choose the following for your new environment:

   1. Name: add a distinct name so you'll be able to find your environment in the drop down later

   1. Region: default is United States, but you can select Europe if you're based over there

   1. Type: you can choose from [Sandbox](https://docs.microsoft.com/power-platform/admin/sandbox-environments), Production, and [Trial](https://docs.microsoft.com/power-platform/admin/trial-environments). Don't select Production unless you're on a paid license, as this type of environment requires paid capacity. Sandbox will allow you to play with all of the features for an indefinite amount of time (uses a space in Dataverse), and Trial will give you 30 days to play around before it's auto-deleted See the links for more information.

   1. Purpose (optional)

   1. Create a database for this environment: flip toggle to Yes. This enables a dataverse connection.

    :::image type="content" source="../media/create-an-environment/new-environment-options.png" alt-text="Screenshot of environment options for new Power Apps environment." border="false":::

1. Select Next

1. Select any options on the next pane you'd like

   1. If Enable Dynamics 365 apps is greyed out, you may encounter some issues. See your sysadmin for more help.

   1. Add any security groups as needed.

    :::image type="content" source="../media/create-an-environment/new-environment-database.png" alt-text="Screenshot of database options for new Power Apps environments." border="false":::

1. Select Save

1. If you've set up your environment successfully, you'll see a green bar across the top of the Environments page letting you know that your new environment is being prepped. This preparation process can take up to five minutes, depending on your connection. If it doesn't automatically refresh once ready, refresh the page to update the status.

    :::image type="content" source="../media/create-an-environment/new-environment-success-msg.png" alt-text="Screenshot of successful environment creation notification." border="false":::

1. Once the instance is ready, go back to the Power Apps home page and refresh the page

1. Select Environment from the top bar. You should see your environment at the bottom of the environment list. If there are too many environments to display at once, search for your environment and select it once it appears in the list.

    :::image type="content" source="../media/create-an-environment/new-environment-in-list.png" alt-text="Screenshot of all environments plus the newly created environment." border="false":::

1. From the left pane, select Solutions

1. Select Import from the top bar

    :::image type="content" source="../media/create-an-environment/add-new-solution.png" alt-text="Screenshot showing how to add a new solution to the new environment via the Solutions tab." border="false":::

1. Select Browse and import the `AdaptiveCardsExtensions_managed` zip file.

1. Once the zip file has loaded, select Next.

    :::image type="content" source="../media/create-an-environment/import-new-solution.png" alt-text="Screenshot showing added zip file in Power Apps environment." border="false":::

1. Verify the settings to the solution you're importing, and then select Import.

1. A "Currently importing solution "Card"." notice will appear while the zip file is being loaded into Power Apps. As soon as the solution is loaded, you'll be notified. This can take up to five minutes, depending on your connection.

    :::image type="content" source="../media/create-an-environment/currently-importing-solution-banner.png" alt-text="Screenshot of solution importing banner." border="false":::

1. From the left pane, select Cards, then select Create

1. Select Basic card from the Create page

> [!NOTE]
> If you get a warning saying "The current environment hasn't been provisioned for card, switch to provisioned environment?", contact your sysadmin.
>
> :::image type="content" source="../media/create-an-environment/environment-error-banner.png" alt-text="Screenshot of error banner saying environment hasn't been provisioned for the solution upload." border="false":::
