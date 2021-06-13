---
title: How to deploy Issue Reporting sample app as a broad distribution app
description: Learn how to share the Issue Reporting Power Apps template for Microsoft Teams with users outside of your Team.
author: joel-lindstrom
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 06/13/2021
ms.author: v-ljoel
ms.reviewer: tapanm
---
# How to deploy Issue Reporting app as broad distribution app

The Issue Reporting Power Apps template is designed to make it easy to capture issues with your equipment, facility, or store.

The app addresses the following personas:

-   Issue Reporter: This user submits issue reports and creates tasks

-   Issue Manager: This user creates issue types and oversees the issue reporting process, including analyzing created issues.

-   Issue Resolver (Indirectly): Issues logged in Issue Reporting create tasks in Microsoft Planner, from where issue resolvers can resolve the issues.

You want everyone at in your org, department, or a certain location to be able to report issues. These are people outside of the Teams team. We will share the issue reporting app with them.

The people responsible for managing the issue queue will use the manage issues app. This subgroup should be added as members of the team where the app is installed.

Finally, you have the persona who is assigned to fix the issue. Since all issues are tracked in Microsoft Planner, you want to make sure they have access to the Planner board.

## Prerequisites 

You must be an owner of the Team in which the app is installed to share the app.

## Limitations

At the time of writing Issue Reporting can only shared with a single Active Directory group.

## Action required to share an app with colleagues for broad distribution

1.  Share the app with colleagues

2.  Grant security permissions to the tables used in the app

> [!NOTE]
> Apps are installed in a Team in Microsoft Teams. People who develop and extend the app or managers who create or manage the issue forms should use the app in a Team. For people who log issues or users who are not managers, sharing the app with colleagues outside of the team will enable them to use the app without having to be a member of the Team.

## Sharing App with Colleagues

This process begins by opening the app in the **Power Apps** app. You may have Power Apps pinned to your Teams App Bar.

1.  In Microsoft Teams, select the **…** button from the left menu.

2.  Type **Power Apps** in the search field.

    ![Search for Power Apps](media/issue-reporting-broad-distribution/select-power-apps.png "Search for Power Apps")

3.  Select the Power Apps app from the list to open the app. Power Apps will open inside of teams.
    
4.  It is recommended that you “pop out” Power Apps so that if you need to navigate somewhere else in Microsoft Teams you won’t lose your app
    configuration. To pop out the Power Apps app, right mouse click on the Power Apps logo and select **Pop out app**.

![Pop out Power Apps](media/issue-reporting-broad-distribution/pop-out-app.png "Pop out Power Apps")

5.  Now that you have loaded the Power Apps app, select **Build**.

![Select Build tab](media/issue-reporting-broad-distribution/build-tab.png "Select Build tab")

6.  This screen will show all the teams that have Power Apps installed in them. Select the team that contain the app you want to share. Select **Share with colleagues**.

![Share with colleagues button](media/issue-reporting-broad-distribution/share-with-colleagues.png "Share with colleagues button")

7.  Enter an AD security group or a different team with which you would like to share access to the app.
    
8.  Set the **on/off** toggle to **on** for Issue Reporting.

    ![Share with colleagues screen](media/issue-reporting-broad-distribution/share-screen.png "Share with colleagues screen")
    
9.  Select **Save**

## Managing table permissions

Understanding and assigning permissions to tables are vital to ensure proper security of your shared data. Here are the four permissions available for use.

-   Full Access – Allows end users to see and edit all records in the table.

    ![Full access table permission](media/issue-reporting-broad-distribution/full-access.png "Full access table permission")

-   Collaborate – Allows end users to see all records, but they can only edit their own records.
    
    ![Collaborate table permission](media/issue-reporting-broad-distribution/collaborate.png "Collaborate table permission")
    
-   Reference – Provides a read-only view of data for end users.

    ![Reference table permission](media/issue-reporting-broad-distribution/reference.png "Reference table permission")

-   Private – Allows end users to only view and edit their own data.

    ![Private table permission](media/issue-reporting-broad-distribution/private.png "Private table permission")

## Granting permissions to the tables

By default, all of the table permissions for colleagues not in the Team are set to **none.** If you leave it that way, colleagues that you share the app with
will not be able to use the app, as they won’t have permission to the tables in the app. Follow these steps to set permissions for the tables in the app for
colleagues outside of the team:

1.  In Microsoft Teams, open the **Power Apps** app.

2.  Select the **Build** tab.

3.  Select the team that contain the app you want to share.

4.  Select **Installed apps.** This will show all apps installed in the Team.

5.  Select **See All** in the **Issue Reporting** tile.

![Select all link on the Issue Reporting tile](media/issue-reporting-broad-distribution/issue-tile-select-all.png "Select all link on the Issue Reporting tile")

6. Select **Tables** from the solution components bar.

   ![Select Tables in component list](media/issue-reporting-broad-distribution/tables.png "Select Tables in component list")

7. Select the tables listed individually then **Manage Permissions.**

8. Select the security group with which the app was shared. The initial permission will show none. Select the desired permission and select **Save.**

9. Repeat step 8 for each additional table in the app.

The following is recommended table permissions:

| Table                     | Permission                                                                                                                                                                                                                               |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Issue Report              | Colleagues outside of the team need to submit issues, we will give colleagues Collaborate permission on the Issue Report table.                                                                                                          |
| Issue Report Category     | Colleagues outside of the team need to select categories but not edit them, we will give collaborate permission on the Issue Report Category table.                                                                                      |
| Issue Report Photo        | Issue report photo is not actively used in the app, but is there if you would like to extend the app add photos to issues. If you elect to use photos, you would want to give collaborate permissions to colleagues outside of the team. |
| Issue Report Question     | Colleagues outside of the team should see questions but should not be able to modify question data, so you should give reference permission to colleagues outside of the team.                                                           |
| Issue Report Settings     | Colleagues outside of the team should be able to read issue report settings, but they should not be able to modify issue report setting data, so you would want to give reference permissions to colleagues outside of the team.         |
| Issue Report Template     | Colleagues outside of the team should be able to read issue report templates, but they should not be able to modify the data, so you would want to give reference permissions to colleagues outside of the team.                         |
| Issue Report User Setting | Colleagues outside of the team should be able to create and modify their own user setting records for Issue Reporting, so you should give them collaborate permission on Issue Report User Setting.                                      |

## Rename the app

In a large organization, you might have multiple people sharing the same template app with colleagues. If multiple departments are using Issue Reporting, you can make it easier for your colleagues to find the app by renaming it.

1. Open **Issue Reporting** in Power Apps in Microsoft Teams.

2. From the designer, in the upper right corner select the app name.

   ![Rename Issue Reporting](media/issue-reporting-broad-distribution/rename-app.png "Rename Issue Reporting")

3. Enter a new name for the app. For example, you may want to rename the app
   **Helpdesk** for IT helpdesk issues.

4. Save and publish the app

## Accessing shared apps

So now that you have shared Issue Reporting with colleagues outside of your
team, here is how they will acquire the app.

1.  In Microsoft Teams, select the elipses (…) button on left.

2.  Select **More apps**.

3.  Select **Built for your org**.

4.  When the app information screen appears, select **Add** to add the app to the main teams app menu.
    
    ![Apps built by your colleagues](media/issue-reporting-broad-distribution/built-by-your-colleagues.png "Apps built by your colleagues")
    
5.  After adding the app to the Microsoft Teams app menu, select the icon for the app to open it full screen in Microsoft Teams.
    
6.  If you want to make the app always appear in the app menu so you can easily find it, right click on the Issue Reporting button on the app menu and
    select **Pin**.
    
    ![Pin Issue Reporting app](media/issue-reporting-broad-distribution/pin-issue-reporting.png "Pin Issue Reporting app")
    
7.  If you would prefer to add the app to another team, select the drop-down by the **Add** button and select **Add to a team**.
    
    ![Add shared app to a Team](media/issue-reporting-broad-distribution/add-to-team.png "Add shared app to a Team")
