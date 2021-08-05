---
title: Customize the Issue reporting sample app
description: Learn how to customize the Issue reporting sample app installed from teams store.
author: joel-lindstrom
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 07/15/2021
ms.author: namarwah
ms.reviewer: tapanm
contributors:
  - joel-lindstrom
  - navjotm
  - tapanm-msft
---

# Customize the Issue reporting sample app

The Issue reporting Power App template for Microsoft Teams is designed to be a complete app experience but allow makers to easily extend it for their own purposes. In this guide, we'll go over how to customize the Issue reporting app in Power Apps in Teams.

> [!NOTE]
> Before you can customize the app, you must install it from the Teams store. You can get the app at <https://aka.ms/TeamsIssueReporting>.

Once the app is installed, you can then customize the app using the following steps:

## Opening Power Apps app in Teams

1. In Teams, select **…** (ellipsis) from the left-pane.

1. Enter **Power Apps** in the search field.

    ![Search for Power Apps](media/customize-issue-reporting/search-app.png "Search for Power Apps")

1. Select the Power Apps app from the list to open the app. Power Apps will open inside of teams.

1. Right-click on the **Power Apps** logo, and select **Pin** to lock the app to the left pane for easy access.

   ![Power Apps button](media/customize-issue-reporting/power-apps-icon.png "Power Apps button")

    We recommended that you “pop out” Power Apps so that if you need to go somewhere else in Teams, you won’t lose your app configuration. To pop out the Power Apps app, right-click on the Power Apps logo, and select **Pop out app**.

1. Now that you've loaded the Power Apps app, select **Build** to show all teams that have Power Apps installed.

    ![Select Build tab](media/customize-issue-reporting/build-tab.png "Select Build tab")

1. Select the team in which you installed the Issue reporting app.

1. Select **Installed apps.** This screen will show all apps installed in the Team.

    Issue reporting solution includes two apps&mdash;**Issue reporting** for users to report issues, and **Manage issues** for managers to use to analyze issue reporting history and create or modify Issue templates.

1. Select **See more** in the **Issue reporting** tile.

    ![Issue reporting tile](media/customize-issue-reporting/issue-tile.png "Issue reporting tile")

1. You'll now see all of the apps, tables, flows, and chatbots in the Team.

## Extend the Issue reporting data model

If you're modifying or adding any fields to your app, you'll want to first update or add these columns in their Dataverse tables. In this section, we'll explore the data model for Issue reporting and how to modify it in Power Apps in Teams. Below is the data model for Issue reporting.

![Issue reporting data model](media/issue-reporting-architecture/data-model.png "Issue reporting data model")

Before modifying the fields, you need to first decide where the fields you want to add should go. What are the users doing when they should see or interact with these fields?

**Issue Report**

Issues refer to a problem or trouble being faced by the Users. Information such as the Name, Issue category, issue template, Planner Task ID, due date, assigned user, and description are stored in the Issue reports table.

An issue can be related only to a single Category and Template.

**Issue Report Category**

Categories are used to group issues that are similar. Details such as the name, category icon, Planner Bucket ID are stored in the Issue Report Categories table. A Category can have multiple Issues and Issue Templates associated to it.

**Issue Report Templates**

Issue templates have predefined questions that must be answered by the users while creating an issue that helps us in understanding it better. Details such as the Due Date, Category the user whom the tasks should be assigned, the primary contact information are stored in the Issue Report Templates table. There can be multiple questions and issues related to an Issue template. When an Issue Category is selected, the questions asked on the issue report form are based on the template.

**Issue Report Questions**

Questions are part of the Issue Templates that help in explaining the issue in a better way. Details such as the Issue template and the sequence are stored in the Issue Report Questions table. There can be multiple questions in an Issue template

**Issue Report Settings**

Settings are used to store configurations for the app, including the Team and Planner Ids for where to log issues as Planner Tasks.

**Issue Report User Setting**

User settings are used to store user preferences pertaining to seeing the Power Apps splash screen every time they log in to the app. There's one record for each user.

**Issue Report Photo**

This table has been included to hold photos for issues. It's currently not used in the app but is provided for easy extension.

## Issue reporting Screens

From the list of apps, chatbots, flows, and tables, select the **Issue reporting** app.

![Open issue Reporting](media/customize-issue-reporting/open-issue-reporting.png "Open Issue reporting")

Now that Issue reporting is open in Power Apps in Teams, select the **Tree View**.

![Select Tree view](media/customize-issue-reporting/select-tree-view.png "Select Tree view")

From the Tree View, you can see the screens included in the app. Selecting the arrow to the left of a screen will expand the contents of the screen, giving you access to the components of the screen, including galleries, buttons, text labels, and text input controls.

The following are the screens in Issue reporting:

| **Screen**                  | **Description**                                                                                                                                                                      |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Landing Screen              | This screen displays an image the app title as the app is loading.                                                                                                               |
| Hidden Admin Screen         | This screen is a helper screen for admins to try to understand the way that theming works in the app and support for dark mode and high contrast. This screen isn't visible to app users. |
| Insights Screen             | This screen is the first screen that users see, which provides insight to the number of issues created and providing access for users to navigate to the issue report screen.               |
| Issue Report Screen         | This screen is the form that users complete to create an issue.                                                                                                                      |
| Issue Stats Screen          | This screen displays the quantity of issues by status.                                                                                                                               |
| Template Selection Screen   | This screen is the list of category templates from which a user selects when creating an issue.                                                                                      |
| Assignment Selection Screen | This screen is where the user searches for and selects the user to whom the issue should be assigned.                                                                                |
| Issue Submission Screen     | This screen is the confirmation message when an issue has been submitted.                                                                                                            |
| Settings Missing Screen     | This screen is displayed if a user attempts to open the app without first configuring the Microsoft Planner location.                                                                |
| Tasks Access Denied Screen  | This screen is displayed if a user attempts to submit an issue when they don't have access to the Planner instance that the app is configured to use.                               |

## Manage Issue Screens

Now let’s look at the screens in the **Manage Issues** app:

1. In the Power Apps app, select the **Build** tab

1. Select the team in which you installed the Issue reporting app.

1. Select **Installed apps.** This screen will show all apps installed in the team.

1. Select **Manage issues** in the **Issue reporting** tile.

    ![Select Manage issues](media/customize-issue-reporting/select-manage-issues.png "Select Manage issues")

    Manage issues will open in the designer.

1. Select the **Tree view** and review the screens in the Manage Issues app.

The following are the screens in the Manage Issues app:

| **Screen**               | **Description**                                                                                                                                                                                                      |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Landing Screen           | Displays an image and the app name as the app loads                                                                                                                                                                  |
| Hidden Admin Screen      | This screen isn't visible to users of the app&mdash;it's designed to make it easy for makers to simulate scenarios within the designer. For example, you can toggle dark mode on and see how the app looks in dark mode. |
| Insights Screen          | The primary screen of the app, shows a summary of issues created by status and navigate to the task view in Planner.                                                                                                 |
| Issue Templates Screen   | From this screen, managers can add or modify issue categories and create issue templates.                                                                                                                            |
| Settings Screen          | Screen from which an administrator can manage user settings like restricting the manage app to Owner or selecting the Team and Planner where tasks will be created.                                                  |
| About Screen             | Scree that displays more details about the app.                                                                                                                                                                      |
| Incorrect Context Screen | This screen displays when a user tries to launch the app outside of Teams or in mobile.                                                                                                                    |

## Common customization scenarios

In this section, we discuss common customization/extension scenarios for Issue reporting, and where you would make these changes

### Add logo to launch screen

If you want to modify the loading screen of the Issue reporting loading screen, such as adding your logo to it, you would make this change in the **Landing Screen** of the **Issue reporting**  app.

### Automate task assignment

To automate task assignment, you would update the formula for create issue on the **Issue Report** screen of the **Issue reporting** app, or use a Power Automate flow.

### Modify app purpose

Issue reporting can be used as a starting point for any kind of scenario where a requestor submits an item for someone else to work on or resolve. It could be modified into a ticket management system like a helpdesk request system or a work order tracking system.

### Integrate with other task management system

The Power Platform includes connectors to multiple task scheduling applications, such as Microsoft To-do, Jira, and Trello. Using Power Automate, you can integrate tasks created in Issue reporting with other task management systems than Planner. This app can also be combined with other apps, such as [Inspection](https://aka.ms/teamsinspection)

### Add additional fields to populate when a task is created

Manage issues populates the most common fields used in Planner when creating a task, such as Description, Title, and Assigned to; however, you may want to populate additional fields or change the way the fields are mapped. To modify this logic, you would update the formula for creating issues on the **Issue Report** screen of the **Issue reporting** app.

## Publish changes

When you're done making modifications to the apps, select **Save** to save your changes**.**

- To preview your changes, select **Preview**.
    - The app will launch in preview mode, where you can test the user experience when running the app,
    - To exit preview mode, press **Escape** on your keyboard, or select the **X** in the upper-right corner.
- To publish your app changes, select **Publish to Teams**. Publishing the app makes your changes visible to users of the app.
    - A dialog will open confirming that you want to publish.

        ![Confirm publish](media/customize-issue-reporting/publish-confirm.png "Confirm publish")

    - To change app settings, such as icon and background color, select **Edit details**.
    - To publish the app, select **Next**.
    - On the next screen, confirm the channel you want the app to appear. You can add to other channels in the Team by selecting the **+** button.
    
    ![Add to channel](media/customize-issue-reporting/add-to-channel.png "Add to channel")
    
- To complete publishing your changes, select **Save and close**.

## Customization considerations

Before modifying the Issue reporting app, review the following considerations.

- Where are my table customizations? Columns and tables added by you'll go to **built by this team** section of the Power Apps app. You can also add new tables in the **See all** area.

    ![Built by this team](media/customize-issue-reporting/built-by-this-team.png "Built by this team")

- Changes made to an app will be added as a new version of the app. If you get a new version from store, your customizations won't be overridden. You'll get a new version that has the latest features, but the new version won't be published.

  For example, if you add a field called **urgent** to the issue report screen, then you install the latest version from the Teams store, your   urgent field will still be visible in the app after the upgrade.

  ![Install new version](media/customize-issue-reporting/install-new-version.png "Install new version")

  After upgrading the solution, your current app version will still be "live."

  The updated version of the app is available from the version history of the app. Selecting **Details** from the app list will display the versions of
  the app and allow you to publish the new version.

    ![Select Details](media/customize-issue-reporting/edit.png "Select Details")

-   When customizing the app, pop out the Power Apps app in Teams so you don’t lose your changes when you go to other parts of Teams.
    
-   The app theming has been developed to support dark and high contrast mode in Teams. Changing the fill color of screens may break dark and high contrast modes.

### See also

- [Issue reporting sample apps](issue-reporting.md)
- [Customize sample apps](customize-sample-apps.md)
- [Sample apps FAQs](sample-apps-faqs.md)
- [Use sample apps from the Microsoft Teams store](use-sample-apps-from-teams-store.md)

