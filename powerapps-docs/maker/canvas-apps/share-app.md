---
title: Share an app | Microsoft Docs
description: Share your app by giving other users permission to run or modify it
author: AFTOwen

ms.service: powerapps
ms.topic: conceptual
ms.component: canvas
ms.date: 06/14/2018
ms.author: anneta

---
# Share an app in PowerApps
It’s great to build apps that address your own business needs, but the real magic of PowerApps comes from sharing those apps with others. In this topic, you learn how to share apps with specific users or security groups, or you can share it with your entire organization.

## Specify an app
1. Sign in to PowerApps, and then select **Apps** near the left edge.

    ![Show list of apps](./media/share-app/file-apps.png)

1. Select the ellipsis (...) for the app that you want to share, and then select **Share**.

    ![Open share screen](./media/share-app/ellipsis-share.png)

## Share an app
1. Specify with which users or security groups in Azure Active Directory you want to share the app and whether you want to send mail to those people notifying them.

    You can also share the app with your entire organization so that they can run the app, but they won't be able to modify or share it.

    ![Specify users](./media/share-app/share-list.png)

1. Specify the level of permissions, and then click or tap **Save**.

    * **Can use**: Users or groups can run the app but not share it.
    * **Can edit**: Users or groups can run the app, customize it, and share the customized version further to other users.

        ![Specify permissions](./media/share-app/edit-use.png)

To change permissions for a user or a group, repeat step 1 of this procedure, and then specify a different option in the list of permissions for that user or group. To remove all permissions for a user or group, click or tap the **x** icon for that user or group.

### Send email notification
When you share an app, you can select whether or not to notify users or a security group via email. If you choose this option, an email will be sent to notify the user or users or security groups. The email contains a link with which they can access the app. If appropriate, users are prompted to sign up for PowerApps.

The notification contains a different kind of link based on which permission you assign:

- When you share the app with **Can use** permission, the email contains the link to run the app.
- When you share the app with **Can edit** permission, the email contains the link to run or edit the app.

### Make sure users have access to the data your app uses

> [!IMPORTANT]
> If your app is based on Common Data Service for Apps, your users must be assigned to a security role that grants them access to the data that your app uses. For information about how to create security roles and assign users to them, see [Configure environment security](../../administrator/database-security.md).

Most apps rely on at least one of these types of resources:

* A connection to a data source
* An on-premises data gateway
* A custom connector
* An Excel workbook or other service
* A flow

Users and contributors need permissions to any data connections and gateways that the app uses. Some permissions come along implicitly with the app, but others must be explicitly granted. For more information, see [Share app resources](share-app-resources.md).

When you share an app that uses an older version of the Common Data Service, you must share the runtime permission to the Common Data Service separately. If you don’t have permission to do this, see your environment admin.

### How do my users see the app I shared?
After you share an app with one or more users or security groups, how they can see the app depends on the permission you shared the app with.

##### If you shared an app with *Can use* permission
The people you shared the app with will receive an email notification if you selected that check box in the app sharing screen. In the email, they can click or tap a link to run the app on [Dynamics 365](http://home.dynamics.com). Soon we will support universal links, which means if you have PowerApps Studio or PowerApps Mobile installed, the app will open in PowerApps Studio or PowerApps mobile.

Users can also discover the app in AppSource on [Dynamics 365](http://home.dynamics.com) (for example, if you didn't send email). [Read more](../../user/app-source.md) on how to users can get apps via AppSource.

##### If you shared an app with *Can edit* permission
The people you shared the app with will receive an email notification if you selected that check box in the app sharing screen. In the email, they can click or tap a link that opens the app directly for editing using PowerApps Studio. There is also a link to run the app on [Dynamics 365](http://home.dynamics.com). Soon we will support universal links, which means if you have PowerApps Studio or PowerApps Mobile installed, the app will open in PowerApps Studio or PowerApps Mobile.

Users can also discover the app in [powerapps.com](http://web.powerapps.com) (for example, if you didn't send email). This is the home for app creators to browse through all the apps they created or that have been shared with them with **Contributor** permission. In contrast, [Dynamics 365](http://home.dynamics.com) is where users can run apps from PowerApps and other business apps quickly.

## Other things to know
* To share an app, you must save it to the cloud, not locally.
* Before you share an app, consider which users and security groups you’re going to share it with and what role you want each to have: **Can edit** or **Can use**. If you share an app with a group, existing members of that group and anyone who joins it will have the permissions that you specify. Anyone who leaves the group loses those permissions unless they're members of a different group that has access or you specify permissions for them explicitly.
* Every member of a group has the same permissions for an app as the overall group does. However, you can specify greater permissions for one or more members of that group to allow them greater access. For example, you can give Security Group A the **Can use** permission, but you can also give User B, who belongs to that group, **Can edit** permission. Every member of the security group can run the app, but only User B can edit it. If you give Security Group A the **Can edit** permission and User B **Can use** permission, that user can still edit the app.
* You can share an app with your entire organization, but think carefully about whether everyone needs access to your app.
* Be aware that any changes you make to a shared app will flow through to the people you shared it with as soon as you save the changes. If you improve the app, everyone benefits. If you break the app, everyone is affected.
* Before you share an app, give it a meaningful name and description, so people know what your app is about and can easily pick it out from a list. On the **File** menu in PowerApps Studio, click or tap **App settings**, and then enter a description.

### What isn't supported?
* You can share to a security group but not a distribution group.
* You can share apps with users in your organization but not users in another tenant.
* You can re-share an app if you have **Can edit** (not **Can use**) permission to that app.
