---
title: Set permission and share your app using Power Apps in Teams | Microsoft Docs
description: Learn how to share your apps and set table permissions using Power Apps in Teams.
author: matthewbolanos
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/07/2021
ms.subservice: teams
ms.author: mabolan
ms.reviewer: tapanm
contributors:
  - tapanm-msft
---

# Set permission and share apps with colleagues

After collaboration with your team to build an app, as an owner of the team, you can share the app and its underlying data with other colleagues within your company that don't belong to your development team.

To share an app:

1. Assign the correct permissions for the tables in your app for the **Colleagues with access** role.

2. Select a security group you would like to assign to the **Colleagues with
access** role.
    
3. Choose which apps the **Colleagues with access** role should have access to.

Once you’re done sharing your apps, they’ll appear in the [Built for your
colleagues](/microsoftteams/manage-power-platform-apps) section within the Teams app store. If you’re a Teams admin, you can also pin apps for users in the Teams app bar for even easier discovery.

![Built by your colleagues.](media/built-for-your-colleagues.png "Built by your colleagues")

> [!NOTE]
> - If your app doesn't appear in the **Built by your colleagues** section, your Teams app might be caching information. If this happens, try signing out, and sign back in if you're using the Teams desktop app. If you're using Teams web app, try refreshing your browser.
> - You need to be an owner within the team to share apps and edit table
permissions. If you are not an owner, the **Manage permission** and **Share with colleagues** options won't appear.

## Assign table permissions

By default, the **Colleagues with access** role has no access to the data inside any of the custom tables you built using Dataverse for Teams. If you would like users outside of your team to access this data, you'll need to change the default access to one of these four permission sets:

- **Full access** – Allows end users to see and edit all records in the table.

- **Collaborate** – Allows end users to see all records, but they can only edit their own records.

- **Reference** – Provides a read-only view of data for end users.

- **Private** ­– Allows end users to only view and edit their own data.

> [!NOTE]
> You can also use this experience to alter the default access rights for
members and guests within your team. By default, Team members are given **Full
access** and guests are given **Private** access to new custom tables.

To set the permissions of a table:

1. Select **Build** tab.

1. Select the team that contains the app and tables you want to share.

1. Select **See all** under the list of resources in the team.

1. Select **Tables** from the left pane.

1. Select the table you want to share.  

    ![Manage permissions.](media/manage-permissions.png "Manage permissions")

1. Select the **Manage permissions** in the command bar.

1. Under the **Colleagues with access** role, and select the permission set that you want to grant this role.  

    ![Colleagues with access.](media/colleagues-with-access.png "Colleagues with access")

    > [!TIP]
    > After you assign a security group to the **Colleagues with access** role, you'll see the name of the security group reflected in
    the table permission panel.

1. Select **Save**.

1. Repeat the above steps for the remaining tables in your app.

## Assign the colleagues with access role to a security group and share the app

After you’ve completed setting the permissions to all your tables, you’re now
ready to share the app with an existing security group.

> [!NOTE]
> - You can share an app to a single security group.
> - If you want to share the app to a Microsoft 365 group, it must be [security enabled](../maker/canvas-apps/share-app.md#share-an-app-with-microsoft-365-groups).
> - The security group's membership type must be **Assigned**. More information: [Group membership types in Azure Active Directory](/azure/active-directory/fundamentals/active-directory-groups-create-azure-portal#membership-types)
> - Your Power Apps administrator may have applied the limit to the maximum size of the security group. By default, this limit is 10,000 members.

To share an app:

1. Select **Build** tab.

1. Select the team that contains the app you want to share.

1. In the top-right, select the **Share with colleagues**.

    ![Share with colleagues.](media/share-with-colleagues.png "Share with colleagues")

1. Search for, and select the security group you want to share the apps and tables with.

    ![Search and select group.](media/select-group-to-share.png "Search and select group")

1. Set **Colleague can use** toggle to **On** for the apps and tables that you want to share with the security group selected in the previous step.

    ![Set On for apps and tables.](media/toggle-on.png "Set On for apps and tables")

1. Select **Save**.

The apps you selected will now appear in the [Built for your
colleagues](/microsoftteams/manage-power-platform-apps) section within the Teams app store.

### Optional: Pin the app to the app bar as a tenant administrator

If you're a tenant administrator, you can go one step forward and pin the apps for end users in Teams. To pin apps in Teams, follow the steps to [add an app to the app catalog](embed-teams-app.md), and then, [edit or create a new Teams app setup policy](/microsoftteams/teams-app-setup-policies) with your app.

| Teams desktop client | Teams mobile client |
| - | - |
| ![Teams desktop client](media/app-setup-policies-desktop-app-bar.png "Teams desktop client") | ![Teams mobile client](media/mobile-app-ui.png "Teams mobile client")  |

### See also

[Publish your app in Teams](publish-and-share-apps.md)
