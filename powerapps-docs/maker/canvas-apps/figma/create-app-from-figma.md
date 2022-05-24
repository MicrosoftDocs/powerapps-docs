---
title: Create a canvas app from Figma (preview)
description: Learn about how to create canvas apps from Figma.
author: tapanm-msft
ms.topic: article
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 05/24/2022
ms.subservice: canvas-maker
ms.author: kaagar
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
---

# Create a canvas app from Figma (preview)

[This article is pre-release documentation and is subject to change.]

In this article, you'll learn about creating canvas apps using your existing Figma design. [Figma](https://www.figma.com/) is a graphics editor and a design tool that you can use to create prototypes for your intended software design. After the design has been finalized, use the **Figma to app** feature to generate apps directly from the layout and design that you defined in your Figma file.

## Prerequisites

- You must have access to a Figma design file that you want to use and create an app from.
- The Figma file must be designed using the [Create Apps from Figma UI Kit](https://go.microsoft.com/fwlink/?linkid=2193981).

> [!TIP]
> If you're using the UI kit for the first time, familiarize yourself with the feature [overview](overview.md), the [UI kit](design-using-kit.md) capabilities, and its [components](supported-components.md).

## Create an app

1. Sign in to [Power Apps](https://make.powerapps.com).

1. Under **Start from**, select **Figma (preview)**.

    :::image type="content" source="media/maker-figma.png" alt-text="Select Figma preview from available options.":::

1. Enter an app name.

1. Enter the Figma file URL. More information: [Share files and prototypes](https://help.figma.com/hc/articles/360040531773-Share-or-embed-files-and-prototypes)

1. Enter the Figma personal access token. More information: [Create a new personal access token](https://help.figma.com/hc/articles/360052378433-Bubble-and-Figma)

    :::image type="content" source="media/create-app.png" alt-text="Create app dialog box with app name, Figma URL and personal access token created.":::

    > [!NOTE]
    > Power Apps uses your personal access token to connect to your Figma page or frame with **Can view** (read-only) access, and doesn't make any changes inside Figma.

1. Select **Create**.

    Once the app is created, your new app will open up in Power Apps Studio so you can continue building and customizing your app.

    :::image type="content" source="media/studio.png" alt-text="Created app opened inside Power Apps Studio.":::

1. Extend this app by [connecting to data](../add-data-connection.md), [adding app logic](../working-with-formulas.md), and adding more [screens](../add-screen-context-variables.md) and [controls](../add-configure-controls.md) as necessary.

1. [Save, publish](../save-publish-app.md), and [share](../share-app.md) the app.

### See also

- [Troubleshoot common errors](common-errors.md)
- [Components supported by the UI Kit (preview)](supported-components.md)
