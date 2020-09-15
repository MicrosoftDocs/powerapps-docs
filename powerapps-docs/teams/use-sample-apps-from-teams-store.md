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

# Use sample apps from Teams store

[!INCLUDE [cc-beta-prerelease-disclaimer.md](../includes/cc-beta-prerelease-disclaimer.md)]

Sample apps created using Power Apps are available in the Teams store. You can select the sample app that best fits your business requirement and quickly install to get started. In this article, you'll learn about one such sample application that helps manage campaigns and ideas. Sample apps created using Power Apps and published to the Teams store may consist of multiple components such as apps, flows, and tables.

In this tutorial, you'll learn how to search for sample apps in Teams store, and add them to your team channel. After you install the sample app, you can go to the team that you added the app to and use the tabs for the apps just like other features such as **Post**, **Files**, or **Wiki**.

![Sample app](media/sample-app.png "Sample app")

> [!IMPORTANT]
> Installing the sample app automatically enables the selected team’s Microsoft 365 Group for security. For more information about Microsoft 365 Group and security, go to [enable security for the selected team’s Microsoft 365 Group](../maker/canvas-apps/share-app.md#share-an-app-with-office-365-groups).

## Available sample apps

Several sample apps are available from the Teams store that you can add to your Teams channels and use for different purposes.

| Name | Description |
| - | - |
| [Employee Ideas](employee-ideas.md) | Manager and employee apps for campaigns and ideas. |
| [Area Walk](area-walk.md) | Manager and user apps for area walks. |
| [Issue Reporting](issue-reporting.md) | Manager and user apps for issue reporting. |

The following tutorial shows how to install one of the available sample apps.

## Install the sample app

To get started with installing the sample Power Apps app in Teams:

1. Select **Apps** at the bottom of left pane inside Teams.

1. Search for the app name, for example **Employee Ideas**.

    ![Employee Ideas app search](media/sample-app-9.png "Employee Ideas app search")

1. Select the app.

1. Select **Add to a team**.

    ![Select Add to team](media/sample-app-1.png "Select Add to team")

1. Search for the Teams channel that you want to add the apps to.

    ![Search teams channel](media/sample-app-2.png "Search teams channel")

1. Select **Set up a tab**.

   ![Select set up tab](media/sample-app-3.png "Select set up tab")

1. Select **Save** to confirm and start the installation.

    ![Save changes](media/sample-app-4.png "Save changes")

    > [!NOTE]
    > You can keep **Post to the channel about this tab** selected to
    communicate the addition of the app. Unchecking will not announce the
    addition of the app on the selected channel as a post.

1. Installation of the app begins. Installation may take a while and you can continue
    with other activities.

    ![App installation](media/sample-app-5.png "App installation")

    > [!NOTE]
    > If the selected Teams team doesn’t already have an environment created, a new environment is created at this stage. For more information about environment lifecycle, go to [Environment lifecycle](/power-platform/admin/about-teams-environment.md).

1. After the app installs, you’ll see tab(s) added to the Teams channel you selected earlier. In this example, the tab called **Employee Ideas**.

    ![Remove installation tab](media/sample-app-6.png "Remove installation tab")

Similarly, you can find other apps in the Teams store, and add them to your Teams channel.

## Run the sample app

To run the installed app, select app from the available tabs inside the Teams channel that you added the app to. For example, to run the **Employee Ideas**, select the app from the available
tabs on your Teams channel.

### Step 1 - Allow connections

Before you can use the app, an app configured to use connection(s) may ask your permissions:

![Select Allow to let the app use connections](media/sample-app-10.png "Select Allow to let the app use connections")

Select **Allow** so the app can use connections.

### Step 2 - Select channel

Select the channel, in this case populated automatically - and then, select **Let's go**:

![Select Let's go](media/sample-app-11.png "Select Let's go")

### Step 3 - Use the app

The app **Employee Ideas** is now open and ready for your use.

![Select app from available list](media/sample-app-12.png "Select app from available list")

For more details about using the **Employee Ideas** app, go to [Employee Ideas](employee-ideas.md).

## Edit the sample app

You can further customize and edit the components of an installed Power Apps app in Teams. To edit and manage the installed Power Apps Teams app in Teams, go to [Manage your apps](manage-your-apps.md).

## Report installation errors

If you get any errors during the installation process, you can help us troubleshoot the problem much more effectively with the session details using CTRL+ALT+A on the keyboard. To learn more about the session details, go to [About tab](overview-of-the-power-apps-app.md#about-tab).

### See also

- [Area Walk](area-walk.md)
- [Employee Ideas](employee-ideas.md)
- [Issue Reporting](issue-reporting.md)
