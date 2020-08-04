---
title: Use sample apps from teams store | Microsoft Docs
description: Learn how to use sample apps from Teams store.
author: tapanm-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 08/17/2020
ms.author: tapanm
ms.reviewer: 
---

# Installing sample Power Apps app in Teams

A sample Power Apps app is available with the release of this Private Preview. The sample app can be installed to Teams using the **Apps** option.

> [!NOTE]
> You must use <https://aka.ms/teams-fullscreen-test> to install the sample Power Apps app in Teams during the private preview period.

The sample app available consists of several tables and two apps, **Inspection App** and **Manage Asset Classes**. After you install the sample app, you can go to the team that you added the app to and use the tabs for the apps just like other features such as **Post**, **Files** or **Wiki**.

![Sample app](media/sample-app.png "Sample app")

> [!IMPORTANT]
> Installing the sample app automatically enables the selected team’s Microsoft 365 Group for security. For more information about Microsoft 365 Group and security, go to [enable security for the selected team’s Microsoft 365 Group](https://docs.microsoft.com/powerapps/maker/canvas-apps/share-app#share-an-app-with-office-365-groups).

To get started with installing the sample Power Apps app in Teams:

1. Select **Apps** at the bottom of left pane inside Teams.

2. Search for **Inspection App**.

3. Select the **Inspection App**.

4. Select **Add to a team**.

    ![Select Add to team](media/sample-app-select-add-to-team.png "Select Add to team")

5. Search for the Teams channel that you want to add the apps to.

    ![Search teams channel](media/sample-app-search-teams-channel.png "Search teams channel")

6. Select **Set up a tab**.

   ![Select set up tab](media/sample-app-select-setup-tab.png "Select set up tab")

7. Select **Save** to confirm and start the installation.

    ![Select save](media/sample-app-select-save.png "Select save")

    > [!NOTE]
    > You can keep **Post to the channel about this tab** selected to
    communicate the addition of the app. Unchecking will not announce the
    addition of the app on the selected channel as a post.

8. Installation of the app begins. This may take a while and you can continue
    with other activities.

    ![App installation](media/sample-app-installation.png "App installation")

    **NOTE:** If the selected Teams team doesn’t already have an environment created, a new environment is created at this stage. For more information about environment lifecycle, go to Environment lifecycle.

9. After the app installs, you’ll see two tabs added, **Inspection App** and **Manage Asset Classes.** Upon completion of installation, you can remove the **Installing App** tab.

    ![Remove installation tab](media/sample-app-remove-installation-tab.png "Remove installation tab")

## Running the sample app

To run the installed app, select app from the available tabs inside the Teams channel that you added the app to.

For example, to run the **Inspection App**, select the app from the available
tabs on your Teams channel.

![select app from available list](media/sample-app-select-from-available-list.png "Select app from available list")

Likewise, select **Manage Asset Classes** to run the asset class management app.

![Asset class management app](media/sample-app-asset-management-app.png "Asset class management app")

### Adding Asset Types

To start with the **Inspection App**, you’ll need to add **Asset Types**. The
Asset Types define the classes of different assets that can be added to the app
for inspection.

To add asset types:

1. Go to **Asset Manager** tab in Teams.

2. Select **Assets** tab inside the app.

3. Add asset types, such as Bike, Car or a Truck.

### Adding Assets

Assets are the individual items or vehicles that you want to inspect.

To add assets:

1. Go to **Manage Asset Classes** tab in Teams.

2. Select **Assets** tab inside the app.

3. In the form that opens, fill in the asset details such as the asset name, unique ID and asset class.

### Adding Inspection Forms

Inspections forms are tied to asset types. You can define more than one inspection form for each asset type. For example, you can define a “Daily Car Inspection” and a “Daily Car Inspection” form for the asset type “Car”.

To add Inspection Forms:

1. Go to **Manage Asset Classes** tab in Teams.

2. Select **Inspection Forms** tab inside the app.

3. Select **Add a form** on left-side of the screen.

You can enter one or more checks for this inspection form. Each check can have a *Title*, *Detailed Instructions*, and an *Image*. Each checklist item can also have up to three action buttons associated, reflecting “Pass”, “Fail” and “Not Applicable” outcomes. The labels of the buttons can be customized.

### Associate forms to asset types

To associate forms to the asset types:

1. Go to **Asset Manager** tab in Teams.

2. Select **Assets** tab inside the app.

3. Associate the inspection form to the asset type.

## Editing the sample app

You can further customize and edit the components of an installed Power Apps app in Teams. To edit and manage the installed Power Apps Teams app in Teams, go to Managing an app.

### Reporting installation errors

If you encounter any errors during the installation process, you can help us troubleshoot the problem much more effectively with the session details using CTRL+ALT+A on the keyboard. To learn more about the session details, go to About tab.
