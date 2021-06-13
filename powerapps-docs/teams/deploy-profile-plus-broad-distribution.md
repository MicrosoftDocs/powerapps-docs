---
title: How to deploy Profile+ sample app as a broad distribution app (Preview)
description: Learn how to share Profile + with colleagues who are not members of the Team in which the app is installed..
author: joel-lindstrom
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 06/11/2021
ms.author: v-ljoel
ms.reviewer: tapanm
contributors:
- navjotm
---
# How to deploy Profile+ app as broad distribution app (Preview)
[This article is pre-release documentation and is subject to change.]

The Profile+ Power Apps template is designed to give you a single place to see complete information about the people in your organization, your organization hierarchy, and open positions for which you may want to apply.

The app addresses the following personas:

-   Manager: provide details about their department, including open positions that need to be filled.
    
-   User: view organization hierarchy and biographical information about the people in their organization, find open positions for which them may want to apply.

Profile + is installed in a Team, but it’s designed to be used primarily by people outside of the team. Since there is no app administration required, only
people who develop or customize the app need to be members of the team. Everybody else can use the app outside of the Team.

You want everyone at in your organization to be able to view Profile+, as well as updating their biographical information and publishing open positions. These are people outside of the Teams team. We will share the Profile+ app with them.

## Prerequisites 

You must be an owner of the Team in which the app is installed to share the app.

## Limitations

At the time that these instructions were written, Teams apps can only be shared with a single Active Directory group.

## Action required to share an app with colleagues for broad distribution

1.  Share the app with colleagues.

2.  Grant security permissions to the tables used in the app

Note: apps are installed in a Team in Microsoft Teams. People who develop and extend the app or managers who manage the app settings should use the app in a Team. For people who use the app or users who are not managers, sharing the app with colleagues outside of the team will enable them to use the app without having to be a member of the Team.

## Sharing App with Colleagues

This process begins by opening the app in the **Power Apps** app. You may have Power Apps pinned to your Teams App Bar.

1. In Microsoft Teams, select the **…** button from the left menu.

2. Type **Power Apps** in the search field.

![Search for Power Apps](media/profile-plus-broad-distribution/app-search.png "Search for Power Apps")

3. Select the Power Apps app from the list to open the app. Power Apps will open inside of teams.

4. Right click on the **Power Apps** logo and select **Pin** to lock the app to the side menu so it is easy to get to in the future.

![Pin the app](media/profile-plus-broad-distribution/pin.png "Pin the app")

5. It is recommended that you “pop out” Power Apps so that if you need to navigate somewhere else in Microsoft Teams you won’t lose your app configuration. To pop out the Power Apps app, right mouse click on the Power Apps logo and select **Pop out app**.

![Pop out app](media/profile-plus-broad-distribution/pop-out-app.png "Pop out app")



6.  Now that you have loaded the Power Apps app, select **Build**.

7. This screen will show all the teams that have Power Apps installed in them. Select the team that contain the app you want to share. Select **Share with colleagues**

![Share with colleagues](media/profile-plus-broad-distribution/share-with-colleagues.png "Share with colleagues")

8. Enter an AD security group or a different team with which you would like to share access to the app.

9. Set the **on/off** toggle to **on** for Profile +.

![Toggle share to on](media/profile-plus-broad-distribution/share-with-colleagues-2.png "Toggle share to on")

10. Select **Save**

## Granting Permissions to the tables

Understanding and assigning permissions to tables are vital to ensure proper security of your shared data. Here are the four permissions available for use.

-   Full Access – Allows end users to see and edit all records in the table.
-   Collaborate – Allows end users to see all records, but they can only edit their own records.
-   Reference – Provides a read-only view of data for end users.

-   Private – Allows end users to only view and edit their own data.


### Granting Permissions to the tables

By default, all of the table permissions for colleagues not in the Team are set to **none.** If you leave it that way, colleagues that you share the app with
will not be able to use the app, as they won’t have permission to the tables in the app. Follow these steps to set permissions for the tables in the app for
colleagues outside of the team:

1.  In Microsoft Teams, open the **Power Apps** app.

2.  Select the **Build** tab.

3.  Select the team that contain the app you want to share.

4.  Select **Installed apps.** This will show all apps installed in the Team.

5.  Select **See All** in the **Profile Plus** tile.

![Select See all](media/profile-plus-broad-distribution/profile-tile.png "Select See all")

6.  Select **Tables** from the solution components bar.

![Select tables](media/profile-plus-broad-distribution/tables.png "Select tables")

7.  Select the tables listed individually then **Manage Permissions.**

8.  Select the security group with which the app was shared. The initial  permission will show none. Select the desired permission and click **Save.**

9.  Repeat step 8 for each additional table in the app.

The following is recommended table permissions:

| Table                    | Permission                                                   |
| ------------------------ | ------------------------------------------------------------ |
| Expertise Tag            | Since colleagues outside of the team should be able to create new expertise tags, you will want to give them **Collaborate** permissions on the Expertise Tag table. |
| Open Position            | Since colleagues outside of the team should be able to read all open positions and create and edit open positions that they own, you will want to give them **Collaborate** permission on the Open Position table. |
| Person Position          | Person Position is the primary table for Profile Plus. Since colleagues outside of the team will need to read other people’s profiles as well as editing their own, you will want to give them **Collaborate** permission on the Person Position table. |
| ProfilePlus User Setting | Colleagues outside of the team should be able to create, read, and edit their own user setting record, but not see or edit other users’ setting record. You should give the **Private** permission on the Profile + User Setting table. |
| Project Tag              | Since colleagues outside of the team should be able to create new project tags and read all project tags, you should give them **Collaborate** permission on the Project Tab table. |

### Rename the app

In a large organization, you might have multiple people sharing the same template app with colleagues. If multiple departments are using Profile+, you can make it easier for your colleagues to find the app by renaming it.

1.  Open **Profile +** in Power Apps in Microsoft Teams.

2.  From the designer, in the upper right corner select the app name.

3.  Enter a new name for the app. For example, you may want to rename the app **Contoso Org Chart**.

4.  Save and publish the app

## Accessing shared apps

So now that you have shared Profile+ with colleagues outside of your team, here is how they will acquire the app.

1.  In Microsoft Teams, select the elipses (…) button on left.

2.  Select **More apps**.

3. Select **Built for your org**.

![Built for your org](media/profile-plus-broad-distribution/built-for-your-org.png "Built for your org")

4.  When the app information screen appears, select **Add** to add the app to the main teams app menu.

​        After adding the app to the Microsoft Teams app menu, select the icon for the app to open it full screen in Microsoft Teams.

5.  If you want to make the app always appear in the app menu so you can easily find it, right click on the Profile+ button on the app menu and select  **Pin**.

![Pin Profile +](media/profile-plus-broad-distribution/pin.png "Pin Profile +")

6.  If you would prefer to add the app to another team, select the drop-down by   the **Add** button and select **Add to a team**.

![Add app to a Team](media/profile-plus-broad-distribution/add-to-team.png "Add app to a Team")