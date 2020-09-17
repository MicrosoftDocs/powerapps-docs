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

# Use sample apps from the Microsoft Teams store

[!INCLUDE [cc-beta-prerelease-disclaimer.md](../includes/cc-beta-prerelease-disclaimer.md)]

Sample apps that were created by using Power Apps are available in the Teams store. You can select the sample app that best fits your business requirement and quickly install it to get started. In this article, you'll learn about one such sample app that helps manage campaigns and ideas. Sample apps created with Power Apps and published to the Teams store can consist of multiple components such as apps, flows, and tables.

In this tutorial, you'll learn how to search for a sample app in the Teams store and add it to your team channel. After you install the sample app, you can go to the team that you added the app to and use the tabs for the app just as you use other features such as **Post**, **Files**, or **Wiki**.

![Employee Ideas sample app](media/sample-app.png "Employee Ideas sample app")

> [!IMPORTANT]
> Installing the sample app automatically enables the selected team's Microsoft 365 Group for security. More information: [Enable security for the selected team's Microsoft 365 Group](../maker/canvas-apps/share-app.md#share-an-app-with-office-365-groups)

## Available sample apps

Several sample apps are available from the Teams store that you can add to your Teams channels and use for different purposes.

| Name | Description |
| - | - |
| [Employee Ideas](employee-ideas.md) | Manager and employee apps for campaigns and ideas. |
| [Inspection](inspection.md) | Manager and user apps for area inspections. |
| [Issue Reporting](issue-reporting.md) | Manager and user apps for issue reporting. |

The following tutorial shows how to install the Employee Ideas app.

## Install the sample app

1. Select **Apps** at the bottom of the left pane in Teams.

1. Search for **Employee Ideas**.

    ![Employee Ideas app search](media/sample-app-9.png "Employee Ideas app search")

1. Select the app.

1. Select **Add to a team**.

    ![Select Add to a team](media/sample-app-1.png "Select Add to a team")

1. Search for the team channel that you want to add the app to.

    ![Search for a team channel](media/sample-app-2.png "Search for a team channel")

1. Select **Set up a tab**.

   ![Select set up a tab](media/sample-app-3.png "Select set up a tab")

1. Select **Save** to confirm and start the installation.

    ![Save changes](media/sample-app-4.png "Save changes")

    > [!NOTE]
    > You can keep **Post to the channel about this tab** selected to post an announcement
    to the channel that the app has been added. If you clear this check box, the addition of the app won't be announced.

1. Installation of the app begins. Installation might take a while; you can continue
    with other activities.

    ![App installation](media/sample-app-5.png "App installation")

    > [!NOTE]
    > If the selected Teams team doesn't already have an environment created, a new environment is created at this stage. More information: [Environment lifecycle](/power-platform/admin/about-teams-environment.md)

1. After the app is installed, you'll see a tab named **Employee Ideas** added to the team channel that you selected earlier.

    ![New Employee Ideas tab](media/sample-app-6.png "New Employee Ideas tab")

Similarly, you can find other apps in the Teams store and add them to your team channel.

## Run the sample app

To run the installed app, select the **Employee Ideas** tab from the team channel.

### Step 1 - Allow connections

Before you can use the app, it might ask your permission to use connections.<!--note from editor: Can you say with assurance that this will happen, or is "might" accurate here?-->

![Select Allow to let the app use connections](media/sample-app-10.png "Select Allow to let the app use connections")

Select **Allow**, so the app can use connections.

### Step 2 - Select the channel

Select the channel (in this example, the channel is populated automatically), and then select **Let's go**.

![Select Let's go](media/sample-app-11.png "Select Let's go")

### Step 3 - Use the app

The **Employee Ideas** app is now open and ready for your use.

![Select app from available list](media/sample-app-12.png "Select app from available list")

For more details about using the **Employee Ideas** app, go to [Employee Ideas](employee-ideas.md).

## Edit the sample app

You can further customize and edit the components of an installed Power Apps app in Teams. More information: [Manage your apps](manage-your-apps.md)

## Report installation errors

If you get any errors during the installation process, you can help us troubleshoot the problem much more effectively by selecting **Ctrl**+**Alt**+**A** on the keyboard to get the session details. For more information about session details, go to [About tab](overview-of-the-power-apps-app.md#about-tab).

### See also

[Employee Ideas and Manage Campaigns sample apps](employee-ideas.md)  
[Inspection sample apps](inspection.md)  
[Issue Reporting sample apps](issue-reporting.md)
