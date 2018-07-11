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

After you build an app that addresses a business need, specify which users in your organization can run the app and which can modify and even reshare it. Specify each user by name, or specify all users in a security group. As an alternative, specify that your entire organization can run the app if everyone would benefit from it.

> [!IMPORTANT]
> For a shared app to function as you expect, you must also share the data source or sources on which the app is based, such as [Common Data Service for Apps](../../administrator/database-security.md) or [Excel](share-app-data.md). You might also need to share [other resources](share-app-resources.md) on which the app depends, such as flows, gateways, or connections.

## Prerequisites

Before you share an app, you must save it to the cloud (not locally), and then publish the app.

- Give your app a meaningful name and a clear description, so that people know what your app does and they can easily find it in a list. On the **File** menu in PowerApps Studio, select **App settings**, specify a name, and then type or paste a description.

- Whenever you make changes, you must save and publish the app again if you want others to see those changes.

## Share an app

1. [Sign in](https://web.powerapps.com) to PowerApps, and then select **Apps** near the left edge.

    ![Show list of apps](./media/share-app/file-apps.png)

1. Select the ellipsis (...) for the app that you want to share, and then select **Share**.

    ![Open share screen](./media/share-app/ellipsis-share.png)

1. Specify with which users or security groups in Azure Active Directory you want to share the app.

    ![Specify users](./media/share-app/share-list.png)

    You can also share the app with your entire organization so that they can run the app, but they won't be able to modify or share it.

1.  Specify whether you want to send mail to everyone with whom you're sharing the app.

    The email contains a link that users can select to run or modify the app, based on which permission you grant them.

1. Specify the permission for each user or security group, and then select **Save**.

    * **Can use**: Users can run the app but not share it.
    * **Can edit**: Users can run the app, modify it, and share the customized version to other users.

        ![Specify permissions](./media/share-app/edit-use.png)

To change permissions for a user or a security group, select the down arrow next to the permission that the user or group already has, and then specify a different permission. To remove all permissions for a user or a group, select the **x** icon for that user or group.


When you share an app that uses an older version of the Common Data Service, you must share the runtime permission to the Common Data Service separately. If you don’t have permission to do this, see your environment admin.

## How do my users see the app I shared?
After you share an app with one or more users or security groups, how they can see the app depends on the permission you shared the app with.

### If you shared an app with *Can use* permission
The people you shared the app with will receive an email notification if you selected that check box in the app sharing screen. In the email, they can click or tap a link to run the app on [Dynamics 365](http://home.dynamics.com). Soon we will support universal links, which means if you have PowerApps Studio or PowerApps Mobile installed, the app will open in PowerApps Studio or PowerApps mobile.

Users can also discover the app in AppSource on [Dynamics 365](http://home.dynamics.com) (for example, if you didn't send email). [Read more](../../user/app-source.md) on how to users can get apps via AppSource.

### If you shared an app with *Can edit* permission
The people you shared the app with will receive an email notification if you selected that check box in the app sharing screen. In the email, they can click or tap a link that opens the app directly for editing using PowerApps Studio. There is also a link to run the app on [Dynamics 365](http://home.dynamics.com). Soon we will support universal links, which means if you have PowerApps Studio or PowerApps Mobile installed, the app will open in PowerApps Studio or PowerApps Mobile.

Users can also discover the app in [powerapps.com](http://web.powerapps.com) (for example, if you didn't send email). This is the home for app creators to browse through all the apps they created or that have been shared with them with **Contributor** permission. In contrast, [Dynamics 365](http://home.dynamics.com) is where users can run apps from PowerApps and other business apps quickly.

## Other things to know
* Before you share an app, consider which users and security groups you’re going to share it with and what role you want each to have: **Can edit** or **Can use**. If you share an app with a group, existing members of that group and anyone who joins it will have the permissions that you specify. Anyone who leaves the group loses those permissions unless they're members of a different group that has access or you specify permissions for them explicitly.
* Every member of a group has the same permissions for an app as the overall group does. However, you can specify greater permissions for one or more members of that group to allow them greater access. For example, you can give Security Group A the **Can use** permission, but you can also give User B, who belongs to that group, **Can edit** permission. Every member of the security group can run the app, but only User B can edit it. If you give Security Group A the **Can edit** permission and User B **Can use** permission, that user can still edit the app.
* Be aware that any changes you make to a shared app will flow through to the people you shared it with as soon as you save and publish the changes. If you improve the app, everyone benefits. If you break the app, everyone is affected.

### What isn't supported?
* You can share to a security group but not a distribution group.
* You can share apps with users in your organization but not users in another tenant.
* You can re-share an app if you have **Can edit** (not **Can use**) permission to that app.
