---
title: Link a canvas app to a project | Microsoft Docs
description: Link a canvas app to a project in PowerApps so that you can deploy the app to another environment
author: AFTOwen
manager: kvivek
ms.service: powerapps
ms.topic: article
ms.custom: canvas
ms.reviewer:
ms.date: 10/17/2018
ms.author: anneta
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Link a canvas app to a project

Link an app to a project if you want to deploy the app, for example, in a different environment from the one in which it was created. Projects can contain not only apps but also other components, such as entities and option sets. By linking apps and other customized components to a project and then importing the project, you can quickly customize an environment in a variety of ways.

Projects are built on the solution system of the Dynamics 365 platform. For more information, see [Projects overview](../common-data-service/solutions-overview.md).

## Prerequisites

- You can link an existing app to a project only if the app is in an environment that contains a Common Data Service for Apps database.
- You can create an app from within a project only in an environment that contains a CDS for Apps database.

## Create a project

You can skip this procedure if you already have a project to which you want to link an existing app or in which you want to create an app from a blank screen.

1. [Sign in](https://web.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) to PowerApps.

1. Perform either of these steps:

    - If you want to link an existing app to a project, switch to the environment that contains that app.
    - If you want to create an app from within a project, switch to any environment that contains a CDS for Apps database.

1. In the left navigation bar, select **Projects**.

1. In the banner under the title bar, select **New project**.

1. In the window that appears, specify a display name, a publisher, and a version for your project.

    A name (with no spaces) will be automatically generated based on the display name that you specify, but you can customize the default value if you want. You can specify the default publisher for your environment and **1.0** for the version if you don't have specific needs in those areas.

1. Near the upper-left corner, select **Save and close**.

## Link an existing app to your project

1. [Sign in](https://web.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) to PowerApps.

1. If necessary, switch to the environment that contains the project to which you want to link an app.

1. In the left navigation bar, select **Projects**.

1. In the list of projects, select the project to which you want to link an app.

1. In the banner under the title bar, select **Add existing** > **App** > **Canvas app**.

1. In the list of apps, select the app that you want to link to the project, and then select **Add**.

## Create an app from within a project

You can create an app from within a project, but you must create the app from a blank screen. You can't automatically generate a three-screen app or customize a template or sample app from within a project.

1. [Sign in](https://web.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) to PowerApps.

1. If necessary, switch to the environment that contains the project to which you want to link an app.

1. In the left navigation bar, select **Projects**.

1. In the list of projects, select the project in which you want to create an app from a blank screen.

1. In the banner under the title bar, select **New** > **App** > **Canvas app**, and then select the form factor (phone or tablet) of the app that you want to create.

    PowerApps Studio opens with a blank canvas in another browser tab.

1. Create your app (or at least make a single change), and then save it.

1. Switch to the browser tab where you selected your project, and then select **Done** in the dialog box that appears.

    Your new app appears in the list of components for that project. If you make any changes to your app, they will be reflected in the version that's in the project.

## Next steps

- Add more apps or other components, such as entities, flows, and dashboards, to your project.
- Export your project so that you can deploy it in another environment, on AppSource, etc.