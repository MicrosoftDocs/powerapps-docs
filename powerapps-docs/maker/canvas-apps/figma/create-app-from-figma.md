---
title: Create a canvas app from Figma (preview)
description: Learn about how to create canvas apps from Figma.
author: mduelae
ms.topic: how-to
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 03/10/2025
ms.subservice: canvas-maker
ms.author: kaagar
search.audienceType: 
  - maker
contributors:
  - mduelae
---

# Create a canvas app from Figma


In this article, you learn about creating canvas apps using your existing Figma design. [Figma](https://www.figma.com/) is a graphics editor and a design tool that you can use to create prototypes for your intended software design. After the design is finalized, use the **Figma to app** feature to generate apps directly from the layout and design that you defined in your Figma file.

## Prerequisites

- You must have access to a Figma design file that you want to use and create an app from.
- The Figma file must be designed using the [Create Apps from Figma UI Kit](https://go.microsoft.com/fwlink/?linkid=2193981).

> [!NOTE]
> - If you're using the UI kit for the first time, familiarize yourself with the feature [overview](overview.md), the [UI kit](design-using-kit.md) capabilities, and its [components](supported-components.md).
> - Power Apps doesn't persist the Figma files that you provide. The Figma files are only processed in-memory to generate the app.

## Create an app

1. Sign in to [Power Apps](https://make.powerapps.com/).

On the home screen, select **Start with a page design**.
 
1. Select **An image or Figma file** > **Start from Figma** > **Next**.

1. Enter an app name.

1. Enter the Figma file URL. More information: [Share files and prototypes](https://help.figma.com/hc/articles/360040531773-Share-or-embed-files-and-prototypes)

1. Enter the Figma personal access token. More information: [Create a new personal access token](https://help.figma.com/hc/articles/360052378433-Bubble-and-Figma#In_Figma)

    > [!NOTE]
    > Power Apps uses your personal access token to connect to your Figma page or frame with **Can view** (read-only) access, and doesn't make any changes inside Figma.

1. Select **Create app**.

Once the app is created, your new app opens in [Power Apps Studio](../power-apps-studio.md) so you can continue building and customizing your app.


1. Extend this app by [connecting to data](../add-data-connection.md), [adding app logic](../working-with-formulas.md), and adding more [screens](../add-screen-context-variables.md) and [controls](../add-configure-controls.md) as necessary.

1. [Save, publish](../save-publish-app.md), and [share](../share-app.md) the app.

### See also

- [Troubleshoot common errors](common-errors.md)
- [Components supported by the UI Kit](supported-components.md)
