---
title: Use sample apps from teams store | Microsoft Docs
description: Learn how to use sample apps from Teams store.
author: navjotm
ms.service: powerapps
ms.topic: conceptual
ms.custom: intro-internal
ms.date: 06/25/2021
ms.subservice: teams
ms.author: namarwah
ms.reviewer: tapanm
contributors:
  - tapanm-msft
---

# Use sample apps from the Microsoft Teams store

Sample apps that were created by using Power Apps are available in the Teams store. You can select the sample app that best fits your business requirement and quickly install it to get started. In this article, you'll learn about one such sample app that helps manage campaigns and ideas. Sample apps created with Power Apps and published to the Teams store can consist of multiple components such as apps, flows, and tables.

In this tutorial, you'll learn how to search for a sample app in the Teams store and add it to your team channel. After you install the sample app, you can go to the team that you added the app to and use the tabs for the app just as you use other features such as **Post**, **Files**, or **Wiki**.

![Employee ideas sample app.](media/sample-app.png "Employee ideas sample app")

> [!IMPORTANT]
> Installing the sample app automatically enables the selected team's Microsoft 365 Group for security. More information: [Enable security for the selected team's Microsoft 365 Group](../maker/canvas-apps/share-app.md#share-an-app-with-microsoft-365-groups)

## Available sample apps

Several sample apps are available from the Teams store that you can add to your Teams channels and use for different purposes.

:::row:::
   :::column span="":::
      ![Boards app (preview).](media/app-icons/boards-app-icon.png "Boards app (preview)") <br> [Boards (preview)](boards.md) <br> A simple way to connect and share with people in your organization with similar interests.
   :::column-end:::
   :::column span="":::
      ![Bulletins app](media/app-icons/bulletins-app-icon.png "Bulletins app") <br> [Bulletins](bulletins.md) <br> Manager and user apps for company communications.
   :::column-end:::
   :::column span="":::
      ![Employee ideas](media/app-icons/employee-ideas-app-icon.png "Employee ideas app") <br> [Employee ideas](employee-ideas.md) <br> App for campaigns and ideas.
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      ![How to.](media/app-icons/how-to-app-icon.png "How to app (preview)") <br> [How to](how-to.md) <br> Learn how to be a Power Apps maker.
   :::column-end:::
   :::column span="":::
      ![Inspection app](media/app-icons/inspection-app-icon.png "Inspection app") <br> [Inspection](inspection.md) <br> Manager and user apps for area inspections.
   :::column-end:::
   :::column span="":::
      ![Issue reporting app](media/app-icons/issue-reporting-app-icon.png "Issue reporting app") <br> [Issue reporting](issue-reporting.md) <br> Manager and user apps for issue reporting.
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      ![Milestones app](media/app-icons/milestones-app-icon.png "Milestones app") <br> [Milestones](milestones.md) <br> App to keep track of projects, and initiatives.
   :::column-end:::
    :::column span="":::
      ![Perspectives app (preview).](media/app-icons/perspectives-app-icon.png "Perspectives app (preview)") <br> [Perspectives (preview)](perspectives.md) <br> A simple way to add topics and extend the topics with Q&A for discussions.
   :::column-end:::
   :::column span="":::
      ![Profile+ app](media/app-icons/profile-app-icon.png "Profile+ app") <br> [Profile+ (preview)](profile-app.md) <br> Quickly find out about people in your organization.
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
    ![Get connected app](media/app-icons/get-connected-app-icon.png "Get connected app") <br> [Get connected (preview)](get-connected.md) <br> Connect with people in your organization with similar skills.
   :::column-end:::
   :::column span="":::
    :::column-end:::
   :::column span="":::
    :::column-end:::
:::row-end:::

The following tutorial shows how to install the Employee ideas app. You can use similar steps to install other sample apps.

## Install the sample app

> [!TIP]
> If you don't see the sample apps, check whether the [app permission policies in Microsoft Teams](/microsoftteams/teams-app-permission-policies) are configured to block some, or all Microsoft apps.

1. Select **Apps** at the bottom of the left pane in Teams.

1. Search for **Employee ideas**.

    ![Employee ideas app search.](media/sample-app-9.png "Employee ideas app search")

1. Select the app.

1. Select **Add to a team**.

    ![Select Add to a team.](media/sample-app-1.png "Select Add to a team")

1. Search for the team channel that you want to add the app to.

    ![Search for a team channel.](media/sample-app-2.png "Search for a team channel")

1. Select **Set up a tab**.

   ![Select set up a tab.](media/sample-app-3.png "Select set up a tab")

1. Select **Save** to confirm and start the installation.

    ![Save changes.](media/sample-app-4.png "Save changes")

    > [!NOTE]
    > You can keep **Post to the channel about this tab** selected to post an announcement
    to the channel that the app has been added. If you clear this check box, the addition of the app won't be announced.

1. Installation of the app begins. Installation might take a while; you can continue
    with other activities.

    ![App installation.](media/sample-app-5.png "App installation")

    > [!NOTE]
    > - If the selected Teams team doesn't already have an environment created, a new environment is created at this stage. More information: [Environment lifecycle](/power-platform/admin/about-teams-environment)
    > - Environment creation will fail if the Teams team that you selected has *Hiddenmembership* enabled. If this happens, try creating the app in a different team. More information: [Hidden membership groups](known-issues-limitations.md#hidden-membership-groups)

1. After the app is installed, you'll see a tab named **Employee ideas** added to the team channel that you selected earlier.

    ![New Employee ideas tab.](media/sample-app-6.png "New Employee ideas tab")

Similarly, you can find other apps in the Teams store and add them to your team channel.

## Run the sample app

To run the installed app, select the **Employee ideas** tab from the team channel.

### Step 1 - Allow connections

Before you can use the app, it might ask your permission to use connections.

> [!NOTE]
> The list of connections you see below is an example. The number and types of connections asking for your permissions may vary depending on the app you install.

![Select Allow to let the app use connections.](media/sample-app-10.png "Select Allow to let the app use connections")

Select **Allow**, so the app can use connections.

### Step 2 - Select the channel

Select the channel (in this example, the channel is populated automatically), and then select **Let's go**.

![Select Let's go.](media/sample-app-11.png "Select Let's go")

### Step 3 - Use the app

The **Employee ideas** app is now open and ready for your use.

![Select app from available list.](media/sample-app-12.png "Select app from available list")

For more details about using the **Employee ideas** app, go to [Employee ideas](employee-ideas.md).

## Edit the sample app

You can further customize and edit the components of an installed Power Apps app in Teams. More information: [Manage your apps](manage-your-apps.md)

## Report installation errors

If you get any errors during the installation process, you can help us troubleshoot the problem much more effectively by selecting **Ctrl**+**Alt**+**A** on the keyboard to get the session details. For more information about session details, go to [About tab](overview-of-the-power-apps-app.md#about).

## Sample app updates

Updates to the sample apps are published immediately. If you already have a sample app in use when this happens, a new version of the app is created with these updates and published as the live version. If you [customized a sample app](customize-sample-apps.md), you can [restore the app to a previous version](manage-your-apps.md#restore-an-app) with your customizations, or recreate the customizations on top of the updated live version. When restoring the app to preserve your customizations, ensure to check the app functionality for compatibility with the updates.

## Sample apps FAQs

For Frequently Asked Questions about sample apps, go to [Sample apps FAQs](sample-apps-faqs.md).

### See also

- [Boards (preview) sample app](boards.md)
- [Bulletins sample app](bulletins.md)
- [Employee ideas sample app](employee-ideas.md)  
- [Inspection sample apps](inspection.md)  
- [Issue reporting sample apps](issue-reporting.md)
- [Milestones sample app](milestones.md)
- [Perspectives (preview) sample app](perspectives.md)
- [Profile+ (preview) sample app](profile-app.md)
- [Get Connected (preview) sample app](get-connected.md)
- [Customize sample apps](customize-sample-apps.md)
- [Sample apps FAQs](sample-apps-faqs.md)

[!INCLUDE[footer-include](../includes/footer-banner.md)]