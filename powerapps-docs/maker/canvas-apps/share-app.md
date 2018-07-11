---
title: Share an app | Microsoft Docs
description: Share your app by giving other users permission to run or modify it
author: AFTOwen
manager: kvivek

ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.date: 07/11/2018
ms.author: anneta
ms.reviewer: anneta

---
# Share an app in PowerApps

After you build an app that addresses a business need, specify which users in your organization can run the app and which can modify and even reshare it. Specify each user by name, or specify a security group in Azure Active Directory. If everyone would benefit from your app, specify that your entire organization can run it.

> [!IMPORTANT]
> For a shared app to function as you expect, you must also manage permissions for the data source or sources on which the app is based, such as [Common Data Service for Apps](#manage-permissions-in-common-data-service-for-apps) or [Excel](share-app-data.md). You might also need to share [other resources](share-app-resources.md) on which the app depends, such as flows, gateways, or connections.

## Prerequisites

Before you share an app, you must save it to the cloud (not locally) and then publish the app.

- Give your app a meaningful name and a clear description, so that people know what your app does and they can easily find it in a list. On the **File** menu in PowerApps Studio, select **App settings**, specify a name, and then type or paste a description.

- Whenever you make changes, you must save and publish the app again if you want others to see those changes.

## Share an app

1. [Sign in](https://web.powerapps.com) to PowerApps, and then select **Apps** near the left edge.

    ![Show list of apps](./media/share-app/file-apps.png)

1. Select the ellipsis (...) for the app that you want to share, and then select **Share**.

    ![Open share screen](./media/share-app/ellipsis-share.png)

1. Specify with which users or security groups in Azure Active Directory you want to share the app.

    > [!NOTE]
    > You can't share apps with a distribution group in your organization or with any users or groups outside your organization.

    ![Specify users](./media/share-app/share-list.png)

    You can also share the app with your entire organization so that they can run the app, but they won't be able to modify or share it.

1.  (optional) To help users find your app, select the check box for sending them an email invitation.

    The invitation contains a link that users can select to run the app.

    - If a user selects the link on a desktop computer, the app opens in [Dynamics 365](http://home.dynamics.com).
    - If the user selects the link on a mobile device, the app opens in PowerApps Mobile.

    If you grant users permission to modify the app, the message also contains a separate link to open the app for editing in PowerApps Studio.

    Regardless of whether you send an invitation, users can run the app from AppSource on [Dynamics 365](http://home.dynamics.com). Users who have **Can edit** permission can also edit the app from within [PowerApps](http://web.powerapps.com).

1. Specify the permission for each user or security group, and then select **Save**.

    * **Can use**: Users can run the app but not share it.
    * **Can edit**: Users can run the app, modify it, and share the customized version to other users.

        ![Specify permissions](./media/share-app/edit-use.png)

    To change permissions for a user or a security group, select the down arrow next to the permission that the user or group already has, and then specify a different permission.

    To remove all permissions for a user or a group, select the **x** icon for that user or group.

## Manage permissions in Common Data Service for Apps

When you share an app that uses an older version of the Common Data Service, you must share the runtime permission to the Common Data Service separately. If you don’t have permission to do this, see your environment admin.

## Security-group considerations

- If you share an app with a security group, existing members of that group and anyone who joins it will have the permission that you specify for that group. Anyone who leaves the group loses that permission unless they belong to a different group that has access or you give them permission as an individual.
- Every member of a security group has the same permission for an app as the overall group does. However, you can specify greater permissions for one or more members of that group to allow them greater access. For example, you can give Security Group A the **Can use** permission, but you can also give User B, who belongs to that group, **Can edit** permission. Every member of the security group can run the app, but only User B can edit it. If you give Security Group A the **Can edit** permission and User B **Can use** permission, that user can still edit the app.