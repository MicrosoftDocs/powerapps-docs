---
title: How to deploy Inspection app as a broad distribution app
description: Learn about how to deploy Inspection as a broad distribution app
author: sbahl10
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 08/17/2021
ms.author: namarwah
ms.reviewer: tapanm
contributors:
  - joel-lindstrom
  - navjotm
  - tapanm-msft
  - sbahl10
---

# How to deploy Inspection app as broad distribution app

The Inspection sample app for Microsoft Teams is designed to make it easy to track and perform inspections of your assets, equipment, facility, or store.

The inspection solution addresses the following personas:

- **Inspection Manager**: This user creates Inspection forms and manages the list of areas or assets. Inspection Managers use the Manage Inspections app.

- **Inspection Reviewer**: This user reviews and approves submitted inspections. Inspection Reviewers use the Review Inspection app.

- **Inspection User**: This user submits inspections and uses the Inspection app.

You want everyone at in your org, department, or a certain location to be able to submit inspections. These are people outside of the Teams team. We'll share the inspection app with them.

The people responsible for managing and reviewing submitted inspections should be added as members of the team where the app is installed, as these apps are designed to be used from within a team.

> [!NOTE]
> By default, when an issue is logged in an inspection, a task is created in Microsoft Planner in the team in which the app is installed, so you should also share access to the Team Planner environment with the group for which the app is shared for broad distribution.

## Prerequisites

You must be an owner of the Team in which the app is installed to share the app.

### Action required to share an app with colleagues for broad distribution

1. Share the app with colleagues.
1. Grant security permissions to the tables used in the app.

> [!NOTE]
> Aps are installed inside of a tab in a Teams channel. People who develop and extend the app or managers who create or manage the inspection forms should use the app in a Team. For people who complete inspections or users who aren't managers, sharing the app with colleagues outside of the team will enable them to use the app without having to be a member of the Team.

## Sharing App with Colleagues

This process begins by opening the app in the **Power Apps** app. You may have Power Apps pinned to your Teams App Bar.

1. In Teams, select **…** (ellipsis) from the left-pane.

1. Type **Power Apps** in the search field.

    ![Search for Power Apps](media/deploy-inspection-as-a-broad-distribution-app/search-power-apps.png "Search for Power Apps")

1. Select the Power Apps app from the list to open the app. Power Apps will open inside of teams.

1. We recommend that you “pop out” Power Apps so that you won’t lose your app configuration as you move across applications. To pop out the Power Apps app, right-click on the Power Apps logo and select **Pop out app**.

    ![Pop-out app](media/deploy-inspection-as-a-broad-distribution-app/pop-out-app.png "Pop out app")

1. Right-click on the **Power Apps** logo, and select **Pin** to lock the app to the side menu so it's easy to get to in the future.

    ![Power apps icon](media/deploy-inspection-as-a-broad-distribution-app/select-power-apps-icon.png "Power apps icon")

1. Now that you've loaded the Power Apps app, select **Build**.

    ![Build tab](media/deploy-inspection-as-a-broad-distribution-app/build-tab.png "Build tab")

1. This screen will show all the teams that have Power Apps installed in them. Select the team that contain the app you want to share. Select **Share with colleagues**.

    ![Share with colleagues](media/deploy-inspection-as-a-broad-distribution-app/share-with-colleagues.png "Share with colleagues")

1. Enter an AD security group or a different team with which you would like to share access to the app.

1. Set the **on/off** toggle to **on** for **Inspection**.

    ![Set security group on for Inspection](media/deploy-inspection-as-a-broad-distribution-app/set-security-group-on-for-inspection.png "Set security group on for Inspection")

1. Select **Save**.

## Granting Permissions to the tables

Understanding and assigning permissions to tables are vital to ensure proper security of your shared data. Here are the four permissions available for use.

- **Full Access** – Allows end users to see and edit all records in the table.

    ![Full access feature](media/deploy-inspection-as-a-broad-distribution-app/full-access.png "Full access feature")

- **Collaborate** – Allows end users to see all records, but they can only edit their own records.

    ![Collaborate feature](media/deploy-inspection-as-a-broad-distribution-app/collaborate.png "Collaborate feature")

- **Reference** – Provides a read-only view of data for end users.

    ![Reference feature](media/deploy-inspection-as-a-broad-distribution-app/reference.png "Reference feature")

- **Private** – Allows end users to only view and edit their own data.

    ![Private feature](media/deploy-inspection-as-a-broad-distribution-app/private.png "Private feature")

### Granting permissions to the tables

By default, all of the table permissions for colleagues not in the Team are set to **none.** If you leave it that way, colleagues that you share the app with won't be able to use the app, as they won’t have permission to the tables in the app. Follow these steps to set permissions for the tables in the app for
colleagues outside of the team:

1. In Teams, open the **Power Apps** app.

1. Select the **Build** tab.

1. Select the team that contain the app you want to share.

1. Select **Installed apps.** This will show all apps installed in the Team.

1. Select **See All** in the **Area Inspection** tile.

    ![See all option for Installed apps](media/deploy-inspection-as-a-broad-distribution-app/see-all-option-for-installed-apps.png "See all option for Installed apps")

1. Select **Tables** from the solution components bar.

1. Select the tables listed individually then **Manage Permissions.**

    ![Manage permissions](media/deploy-inspection-as-a-broad-distribution-app/manage-permissions.png "Manage permissions")

1. Select the security group with which the app was shared. The initial permission will show none. Select the desired permission and select **Save.**

1. Repeat step 8 for each additional table in the app.

The following is recommended table permissions:

| Table                          | Permission                                                                                                                                                                                                                                                                                  |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Area Inspection                | Since colleagues outside of your team will need to create their own inspections but not read other users inspections, you should give them **Private** permission for Area Inspection table.                                                                                                |
| Area Inspection Checklist      | Area Inspection Checklist is the header for inspection forms. Since colleagues outside of your team will need to read all inspection checklists but not create or edit records, you should give them **Reference** permission for Area Inspection Checklist table.                          |
| Area Inspection Checklist Step | Area Inspection Checklist Steps are the checklist steps for inspection forms. Since colleagues outside of your team will need to read all inspection checklist step but not create or edit records, you should give them **Reference** permission for Area Inspection Checklist Step table. |
| Area Inspection Group          | Area Inspection Groups aren't actively used in the Inspection app, so you should select **None** for the permission for Area Inspection Group.                                                                                                                                             |
| Area Inspection Image          | Area Inspection Images aren't actively used in the Inspection app, so you should select **None** for the permission for Area Inspection Image.                                                                                                                                             |
| Area Inspection Label          | Since colleagues outside of your team will need to read inspection labels but shouldn't create or edit records, you should give them **Reference** permission for Area Inspection Label table.                                                                                             |
| Area Inspection Locations      | Since colleagues outside of your team will need to read inspection locations but shouldn't create or edit records, you should give them **Reference** permission for Area Inspection Location table.                                                                                       |
| Area Inspection Location Type  | Since colleagues outside of your team will need to read inspection location types but shouldn't create or edit records, you should give them **Reference** permission for Area Inspection Location Type table.                                                                             |
| Area Inspection Settings       | Since colleagues outside of your team will need to read inspection app settings but shouldn't create or edit records, you should give them **Reference** permission for Area Inspection Settings table.                                                                                    |
| Area Inspection Step           | Area Inspection Steps store the user input for inspections. Users will need to be able to create and edit inspection step records, so you should give them **Collaborate** permission on Area Inspection Step table.                                                                        |
| Area Inspection Tasks          | Area inspection tasks are created when users log an issue during an inspection, so you should give them **Collaborate** permission on Area Inspection Task table.                                                                                                                           |
| Area Inspection User Settings  | Since colleagues outside of your team need to create and edit their user setting record for Inspection but shouldn't be able to view or edit other users’ setting records, you should give them **Private** permission to the Area Inspection User Settings table.                         |

### Rename the app

In a large organization, you might have multiple people sharing the same template app with colleagues. If multiple departments are using Inspection, you
can make it easier for your colleagues to find the app by renaming it.

1. Open **Inspection** in Power Apps in Teams.
1. From the designer, in the upper right corner select the app name.
1. Enter a new name for the app. For example, you may want to rename the app **Store Inspection**.
1. Save and publish the app.

## Accessing shared apps

So now that you've shared Inspection with colleagues outside of your team, here's how they'll acquire the app.

1. In Teams, select the eclipses (…) button on left.

1. Select **More apps**.

1. Select **Built for your org**.

1. When the app information screen appears, select **Add** to add the app to the main teams app menu.

    ![Built for your org](media/deploy-inspection-as-a-broad-distribution-app/built-for-your-org.png "Built for your org")

1. After adding the app to the Teams app menu, select the icon for the app to open it full screen in Teams.

1. If you want to make the app always appear in the app menu so you can easily find it, right-click on the Inspection button on the app menu and select **Pin**.

    ![Pin the app](media/deploy-inspection-as-a-broad-distribution-app/pin-the-app-option.png "Pin the app")

1. If you would prefer to add the app to another team, select the drop-down by the **Add** button and select **Add to a team**.

    ![Add app to a team](media/deploy-inspection-as-a-broad-distribution-app/add-to-team.png "Add app to a team")

## Limitation

Currently, Teams apps can only be shared with a single Azure Active Directory group.

### See also

- [Understand Inspection sample app architecture](inspection-architecture.md)
- [Customize Inspection app](customize-inspections.md)
- [Sample apps FAQs](sample-apps-faqs.md)
- [Use sample apps from the Teams store](use-sample-apps-from-teams-store.md)


[!INCLUDE[footer-include](../includes/footer-banner.md)]