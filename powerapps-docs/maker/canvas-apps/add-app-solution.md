---
title: Create a canvas app in a solution | Microsoft Docs
description: In PowerApps, create a canvas app in a solution so that you can deploy the app to another environment
author: AFTOwen
manager: kvivek
ms.service: powerapps
ms.topic: article
ms.custom: canvas
ms.reviewer:
ms.date: 10/23/2018
ms.author: anneta
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Create a canvas app from within a solution

Create an app from within a solution if, for example, you want to deploy the app to a different environment. Solutions can contain not only apps but also customized entities, option sets, and other components. You can quickly customize an environment in a variety of ways by creating apps and other components from within a solution, exporting the solution, and then importing it into another environment.

Solutions are built on the same platform as Dynamics 365 for Customer Engagement. For more information, see [Solutions overview](../common-data-service/solutions-overview.md).

## Prerequisite

To follow the steps in this topic, you must switch to an environment that contains a Common Data Service (CDS) for Apps database.

## Create a solution

You can skip this procedure if you already have a solution in which you want to create an app or to which you want to link an app.

1. [Sign in](https://web.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) to PowerApps, and then (if necessary) switch to the appropriate environment:

    - If you want to create an app from within a solution, switch to any environment that contains a CDS for Apps database.
    - If you want to link an existing app to a solution, switch to the environment that contains that app.

1. In the left navigation bar, select **Solutions**.

    > [!div class="mx-imgBorder"]
    > ![Solutions option in the left navigation bar](./media/add-app-solution/left-nav.png "Solutions option in the left navigation bar")

1. In the banner under the title bar, select **New solution**.

    > [!div class="mx-imgBorder"]
    > ![New-solution option in the banner](./media/add-app-solution/banner-new-solution.png "New-solution option in the banner")

1. In the window that appears, specify a display name, a publisher, and a version for your solution.

    > [!div class="mx-imgBorder"]
    > ![Options for a new solution](./media/add-app-solution/configure-new-solution.png "Options for a new solution")

    A name (with no spaces) will be generated automatically based on the display name that you specify, but you can customize the generated name if you want. You can specify the default publisher for your environment and **1.0** for the version if you don't have specific needs in those areas.

1. Near the upper-left corner, select **Save and Close**.

    > [!div class="mx-imgBorder"]
    > ![Save a new solution](./media/add-app-solution/save-new-solution.png "Save a new solution")

## Create a canvas app in a solution

You can create a blank canvas app from within a solution. You can't automatically generate a three-screen app or customize a template or sample app from within a solution.

1. [Sign in](https://web.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) to PowerApps.

1. If necessary, switch to the environment that contains the solution in which you want to create a canvas app.

1. In the left navigation bar, select **Solutions**.

    > [!div class="mx-imgBorder"]
    > ![Solutions option in the left navigation bar](./media/add-app-solution/left-nav.png "Solutions option in the left navigation bar")

1. In the list of solutions, select the solution in which you want to create a canvas app.

1. In the banner under the title bar, select **New** > **App** > **Canvas app**, and then select the form factor (phone or tablet) of the app that you want to create.

    > [!div class="mx-imgBorder"]
    > ![Options to create an app in a solution](./media/add-app-solution/new-option.png "Options to create an app in a solution")

    PowerApps Studio opens with a blank canvas in another browser tab.

1. Create your app (or make at least one change), and then save your changes.

1. On the browser tab where you selected your solution, select **Done** to refresh the list of components in your solution.

    > [!div class="mx-imgBorder"]
    > ![Done button](./media/add-app-solution/done-button.png "Done button")

    Your new app appears in the list of components for that solution. If you save any changes to your app, they will be reflected in the version that's in the solution.

## Link an existing canvas app to a solution

If you want to link an app to a solution, both must be in the same environment, and the app must have been created from within a solution.

1. [Sign in](https://web.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) to PowerApps.

1. If necessary, switch to the environment that contains the solution to which you want to link an app.

1. In the left navigation bar, select **Solutions**.

    > [!div class="mx-imgBorder"]
    > ![Solutions option in the left navigation bar](./media/add-app-solution/left-nav.png "Solutions option in the left navigation bar")

1. In the list of solutions, select the solution to which you want to link an app.

1. In the banner under the title bar, select **Add existing** > **App** > **Canvas app**.

    > [!div class="mx-imgBorder"]
    > ![Banner options to link an existing app](./media/add-app-solution/add-existing.png "Banner options to link an existing app")

    A list of canvas apps that were created within a solution in this environment appears.

1. In the list of apps, select the app that you want to link to the solution, and then select **Add**.

    > [!div class="mx-imgBorder"]
    > ![Add button](./media/add-app-solution/add-button.png "Add button")

## Known limitations

For information about known limitations, see [Use solutions in PowerApps](../common-data-service/use-solution-explorer.md#known-limitations). 

## Next steps

- Create or link more apps and [other components](../common-data-service/use-solution-explorer.md), such as entities, flows, and dashboards, to your solution.
- [Export your solution](../common-data-service/import-update-export-solutions.md) so that you can deploy it to another environment, on AppSource, and so forth.
