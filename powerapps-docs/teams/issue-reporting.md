---
title: Use Issue reporting app from teams store | Microsoft Docs
description: Learn how to use the Issue reporting app from Teams store.
author: josephshum
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/05/2020
ms.subservice: teams
ms.author: jshum
ms.reviewer: tapanm
contributors:
  - joel-lindstrom
  - josephshum
  - tapanm-msft
---

# Issue reporting sample apps

In this tutorial, learn about the Manage Issues and Issue reporting apps, and how to use them effectively.

## Overview

Issue reporting consists of two different apps, one for reporting issues and another for managing them:

- [Manage Issues app](#manage-issues-app)

    The Manage Issues app is used by team managers to:

    - Configure the app experience, including the channel in which Microsoft Teams messages and Planner tasks are created by the app.
    - Create, review, edit, or delete issue template forms to collect information when a user reports an issue.
    - Review team issues, report on issue history, and efficiently manage issue resolution.

- [Issue reporting app](#issue-reporting-app)

    The Issue reporting app is used by employees to:

    - Log issues with the information required to resolve the issue.
    - Modify existing issues and assist with resolution
    - Get a high-level view of the issues and team issues.

Watch this video for a demonstration of this app.
> [!VIDEO https://www.microsoft.com/videoplayer/embed/RE4MbLW]

> [!NOTE]
> Before you can use this app, you may be asked for your permissions to use the connection. More information: [Allow connections in sample apps](use-sample-apps-from-teams-store.md#step-1---allow-connections)

## Prerequisites

Before using this app:

1. Find the app in Teams store.
2. Install the app.
3. Set up the app for the first use.

You also need to [configure](https://support.microsoft.com/office/use-planner-in-microsoft-teams-62798a9f-e8f7-4722-a700-27dd28a06ee0) Planner in Teams.

For details about the above steps, go to [Use sample apps from the Teams store](use-sample-apps-from-teams-store.md).

## Manage Issues app

This app provides the following capabilities:

- [Configure the app](#configure-the-app)
- [Edit the app configuration](#edit-the-app-configuration)
- [Add a new issue category](#add-a-new-issue-category)
- [Update a category icon](#update-a-category-icon)
- [Update a category title](#update-a-category-title)
- [Delete a category](#delete-a-category)
- [Add a new issue template](#add-a-new-issue-template)
- [Edit an issue template](#edit-an-issue-template)
- [Delete an issue template](#delete-an-issue-template)
- [Review an issue report](#review-an-issue-report)
- [View issue tasks in Planner](#view-issue-tasks-in-planner)

### Configure the app

1. Sign in to Teams.

1. Select the team.

1. Select the channel where you installed the **Issue reporting** app.

1. Add **Tasks (Planner)** tab.

    > [!TIP]
    > Give your Planner a distinct name, such as “Issue tasks”. This way, you'll be able to identify the right Planner based on this name. The list of Planner instances inside the app as options shows Planner names, and not the name on the Teams tab for the Planner.

1. Select the **Manage Issues** tab in Teams.

1. Select the channel where the messages will be posted.

1. Select the **Tasks (Planner)** instance to integrate the app with Planner.

    > [!NOTE]
    > Issue reporting requires a Planner tab to be installed before the app can be used. If you didn't add Planner tab, add the tab first and then, reopen the **Manage Issues** app.

1. Select **Continue**.

    ![Select channel and tasks.](media/issue-reporting/select-channel-tasks.png "Select channel and tasks")

1. Follow the steps provided on the page (Steps 1 and 2) to get the SharePoint site URL. Then paste the URL in the **Step 3** box.

1. Select **Let's go**.

    ![Configure the app.](media/issue-reporting/configure-app.png "Configure the app")

### Edit the app configuration

To edit the app configuration:

1. Select the **Manage Issues** tab in Teams.

1. Select the **Insights** tab on the **Manage Issues** screen.

1. Select **Settings**.

    ![Insights settings.](media/issue-reporting/insights-settings.png "Insights settings")

1. Make the required changes.

1. Select **Save**.

    ![Save changes.](media/issue-reporting/save-changes.png "Save changes")

### Add a new issue category

To add a new issue category:

1. Select the **Manage Issues** tab in Teams.

1. Select the **Issue templates** tab on the **Manage Issues** screen.

1. Select **Add category** on the left pane in the app.

1. Enter *Title*.

1. Select **Update icon** and update the icon.

1. Select **Save**.

    ![New issue category.](media/issue-reporting/new-issue-category.png "New issue category")

### Update a category icon

To update a category icon:

1. Select the **Manage Issues** tab in Teams.

1. Select the **Issue templates** tab on the **Manage Issues** screen.

1. Select **Edit**.

1. Select **Update icon** and update the icon as required.

1. Select **Save**.

    ![Update category icon.](media/issue-reporting/update-category-icon.png "Update category icon")

### Update a category title

To update a category title:

1. Select **Tasks** (Planner).

1. Select the required category.

1. Rename the category.

    ![Rename the category in Tasks.](media/issue-reporting/rename-category-tasks.png "Rename the category in Tasks")

1. Sign in to Teams.

1. Select the **Manage Issues** tab in teams.

1. Select the **Issue templates** tab.

1. Open the category that you updated in Tasks (Planner) earlier.

1. Select **Update title** to reflect the updated category title in the app.

    ![Update title inside app.](media/issue-reporting/update-title-app.png "Update title inside app")

    > [!NOTE]
    > The notification bar shows a notification about the title update in Tasks.

### Delete a category

To delete a category:

1. Select the **Manage Issues** tab in Teams.

1. Select the **Issue templates** tab on the **Manage Issues** screen.

1. Select the required category.

1. Select **Edit**.

1. Select **Delete**.

1. Select the **I understand** check box.

1. Select **Delete**.

    ![Delete a category.](media/issue-reporting/delete-category.png "Delete a category")

### Add a new issue template

To add a new issue template:

1. Select the **Manage Issues** tab in Teams.

1. Select the **Issue templates** tab on the **Manage Issues** screen.

1. Select a category to add the new issue template.

1. Select **Add issue template**.

    ![Add issue template.](media/issue-reporting/add-issue-template.png "Add issue template")

1. Enter the details:

    - *Title*
    - *Due within*
    - *Auto assign issue to*
    - *Issue questions*
    - *Additional help*
    - *Primary contact*
    - *Supporting information*

    ![Enter issue template details.](media/issue-reporting/issue-template-details.png "Enter issue template details")

1. Select **Save**.

### Edit an issue template

To edit an issue template:

1. Select the **Manage Issues** tab in Teams.

1. Select the **Issue templates** tab on the **Manage Issues** screen.

1. Select the required category.

1. Select **Edit** for the required issue template.

    ![Edit issue template.](media/issue-reporting/edit-issue-template.png "Edit issue template")

1. Edit the issue template as required.

1. Select **Save**.

    ![Save issue template changes.](media/issue-reporting/save-issue-template-changes.png "Save issue template changes")

### Delete an issue template

To delete an issue template:

1. Select the **Manage Issues** tab in Teams.

1. Select the **Issue templates** tab on the **Manage Issues** screen.

1. Select the required category.

1. Select **Edit** for the required issue template.

1. Select **Delete**.

1. Select the **I understand** check box.

1. Select **Delete**.

    ![Delete an issue template.](media/issue-reporting/delete-issue-template.png "Delete an issue template")

### Review an issue report

To review an issue report:

1. Select the **Manage Issues** tab in Teams.

1. Select the **Insights** tab.

    ![Review a issue report.](media/issue-reporting/review-issue-report.png "Review a issue report")

### View issue tasks in Planner

To view issue tasks in Planner

1. Select the **Manage Issues** tab in Teams.

1. Select the **Insights** tab.

1. Select **View Issues**.

    ![View issues.](media/issue-reporting/view-issues.png "View issues")

## Issue reporting app

The Issue reporting app provides the following capabilities:

- [Submit a new issue](#submit-a-new-issue)
- [View an issue task in Planner](#view-an-issue-task-in-planner)
- [Review and edit existing issues in Planner](#review-and-edit-existing-issues-in-planner)

### Submit a new issue

To submit a new issue:

1. Select the **Issue reporting** tab in Teams.

1. Select **Report an issue**.

1. Select the issue type.

1. Enter issue details.

    > [!NOTE]
    > Some of the issue details are automatically entered.

1. Select **Submit issue**.

    ![Submit a new issue.](media/issue-reporting/submit-new-issue.png "Submit a new issue")

### View an issue task in Planner

To view an issue task in Planner:

1. Select the **Issue reporting** tab in Teams.

1. Select **View issues**.

    ![View issues for Planner.](media/issue-reporting/view-issue.png "View issues for Planner")

1. Select **View in Tasks**.

    ![View issue in Tasks.](media/issue-reporting/view-issue-tasks.png "View issue in Tasks")

This action opens Planner with the selected issue task.

![Planner with issue task.](media/issue-reporting/planner-issue-task-open.png "Planner with issue task")

### Review and edit existing issues in Planner

To review and edit existing issues in Planner:

1. Go to Tasks (Planner).

1. Select the issue task.

1. Edit the task.

    ![Review and edit a task in Planner.](media/issue-reporting/review-edit-task-planner.png "Review and edit a task in Planner")

### See also

- [Understand Issue Reporting sample app architecture](issue-reporting-architecture.md)
- [Customize issue reporting app](customize-issue-reporting.md)
- [Sample apps FAQs](sample-apps-faqs.md)
- [Use sample apps from the Microsoft Teams store](use-sample-apps-from-teams-store.md)


[!INCLUDE[footer-include](../includes/footer-banner.md)]