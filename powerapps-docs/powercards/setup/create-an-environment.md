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

1. Go to [make.test.powerapps.com](https://www.make.test.powerapps.com) (or [aka.ms/pcdesigner](https://www.aka.ms/pcdesigner) for internal).

1. [Create an environment with a database](/power-platform/admin/create-environment#create-an-environment-with-a-database).

1. If you've set up your environment successfully, you'll see a green bar across the top of the Environments page letting you know that your new environment is being prepped. This preparation process can take up to five minutes, depending on your connection. If it doesn't automatically refresh once ready, refresh the page to update the status.

    :::image type="content" source="../media/create-an-environment/new-environment-success-msg.png" alt-text="Screenshot of successful environment creation notification." border="false":::

1. Once the instance is ready, go back to the Power Apps home page and refresh the page.

1. Select **Environment** from the top bar. You should see your environment at the bottom of the environment list. If there are too many environments to display at once, search for your environment and select it once it appears in the list.

    :::image type="content" source="../media/create-an-environment/new-environment-in-list.png" alt-text="Screenshot of all environments plus the newly created environment." border="false":::

1. [Import the adaptive card solution](powerapps/maker/data-platform/import-update-export-solutions) using the `AdaptiveCardsExtensions_managed` zip file.

1. A "Currently importing solution "Card"." notice will appear while the zip file is being loaded into Power Apps. As soon as the solution is loaded, you'll be notified. This can take up to five minutes, depending on your connection.

    :::image type="content" source="../media/create-an-environment/currently-importing-solution-banner.png" alt-text="Screenshot of solution importing banner." border="false":::

1. From the left pane, select **Cards**, then select **Create**.

1. On the Create page, select **Basic card**.

> [!NOTE]
> If you get a warning saying "The current environment hasn't been provisioned for card, switch to provisioned environment?", contact your sysadmin.
>
> :::image type="content" source="../media/create-an-environment/environment-error-banner.png" alt-text="Screenshot of error banner saying environment hasn't been provisioned for the solution upload." border="false":::
