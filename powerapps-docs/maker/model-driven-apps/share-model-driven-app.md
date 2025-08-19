---
title: Sharing a model-driven app - assigning security roles and privileges
description: Share a model-driven app with users or teams by assigning them security roles with privileges to access the app's data with Power Apps.
author: Mattp123
editor: ''
tags: ''
ms.topic: how-to
ms.component: model
ms.date: 02/25/2025
ms.subservice: mda-maker
ms.author: matp
search.audienceType:
  - maker
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-title
  - ai-seo-date:10/18/2023
  - ai-gen-desc
---

# Share a model-driven app

Share a model-driven app to make it available so other users can play it. Sharing includes the following steps:

1. [Identify the security roles to use for the app](#model-driven-app-sharing-basics)
1. [Assign security roles or people to a model-driven app](#assign-security-roles-or-people-to-a-model-driven-app)
1. [Share the link to the app](#share-the-link-to-the-app)

:::image type="content" source="media/share-model-driven-app/share-model-driven-app.png" alt-text="Share a model-driven app in Power Apps" lightbox="media/share-model-driven-app/share-model-driven-app.png":::

If your app contains only out-of-the-box tables, such as account or contact, you can use an existing [predefined security role](#about-predefined-security-roles).

## Model-driven app sharing basics

Model-driven apps use role-based security for sharing. The fundamental concept in role-based security is that a security role contains privileges that define a set of actions that can be performed on tables within the app. This approach means that while two people are able to use the app, one user might only be able to read records, or records that they themselves created. The other user might be able to see all records and have the rights to delete those records.

All app users must be assigned one or more predefined or custom security roles. Or, security roles can be assigned to teams. When a user or team is assigned to one of these roles, the person or team members are granted the set of privileges associated with that role.

The process for sharing a model-driven app is different from sharing a canvas app. Model-driven app sharing depends on how the Microsoft Dataverse data table privileges are assigned for the tables that are in the app. If security roles aren't already defined for your app, contact your Power Platform administrator to create them for you. 

More information: [Create or edit a security role to manage access](/power-platform/admin/create-edit-security-role)

## Assign security roles or people to a model-driven app

When you share a model-driven app, you can share it with all members of one or more security roles or a user or team.

1. Sign in to  the [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), on the left navigation pane select **Apps**, next to the app you want to share select **…**, and  then select **Share**.
1. From the **Share** *app name* pane, choose from the following options: 
   - Select the app, and then select the drop-down list in the right pane to display all available security roles. Select the security roles you want from the security role dropdown list.
   :::image type="content" source="media/share-model-driven-app/share-model-driven-app.png" alt-text="Assign security roles to app":::

   > [!IMPORTANT]
   > If your app has one or more custom tables, contact a Power Platform administrator to configure privileges to the custom tables in a security role. This is necessary in order for users to work with your custom table's records in the app. More information: [Create or edit a security role to manage access](/power-platform/admin/create-edit-security-role)
   - To assign an individual user or team, select the user name or team from the **People** list.
   :::image type="content" source="media/share-model-driven-app/share-user.png" alt-text="Assign specific users to a model-driven app":::
   
     If your app contains premium components, such as a map or address input components, users must have a Power Apps license to use the app. To request licenses for the users of your app, select **Request licenses** to submit a license request to your admin.

      :::image type="content" source="../canvas-apps/media/request-licenses-for-others-banner.png" alt-text="Request Power Apps licenses for your users.":::
    
      > [!Note]
      > You can't request licenses for security groups or distribution lists. For more information about requesting licenses, see [Request Power Apps licenses for your app users](../common/request-licenses-for-users.md).

1. Select **Share**.

## Share the link to the app

Unlike sharing canvas apps, sharing model-driven apps doesn't currently send an email with a link to the app.

To get the direct link to an app:

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), and then select **Apps** on the left navigation pane.
1. Select the model-driven app you want, and then select **Details** on the command bar.
1. Copy the **Web link**. Alternatively, you can make a copy of the **Mobile QR code** for mobile users.
1. Paste the app URL in a location so that your users can access it, such as by posting it on a SharePoint site or send via email.

## App sharing privilege and licensing requirements

There are a few key environment and licensing prerequisites required when sharing a model-driven app with a user.

- A Microsoft 365 user with Power Platform administrator rights must exist within the organization. [Learn how to assign Power Platform Administrator rights](/power-platform/admin/use-service-admin-role-manage-tenant).  This provides the user with administrator rights over all environments.
- The app sharer must have admin privileges to the specific environment (or be a Power Platform administrator). The app sharer must have a [security role](/power-platform/admin/security-roles-privileges) with equal or greater privileges than the security role they're assigning to the app and to other users. Usually, this takes the form of the app sharer having the Dataverse **System Administrator** or **System Customizer** security role.  These roles can be assigned by Power Platform administrators (who have rights over all Dataverse environments). The system administrator and system customizer security roles are standard roles that exist within all Dataverse environments.
- The user must exist as a user within the environment. It isn't enough to only be a Microsoft 365 user. This is because all users in an environment are accounted for and described within tables in the environment. [Learn how to add a user to an environment](/power-platform/admin/add-users-to-environment)
- Users must have the correct [license](/power-platform/admin/pricing-billing-skus) to be able to use the app. Users can [request a license themselves](../../user/request-license.md), or a [maker can request licenses for their app users](../common/request-licenses-for-users.md). Also, the license must be assigned in either the users home tenant or the tenant hosting the app.

  > [!Note]
      > Users who have the Environment Maker role assigned will not require licenses to use model-driven apps.

 > [!NOTE]
 > Users who have the Environment Maker security role assigned don't require licenses to use model-driven apps.

## About predefined security roles

There are several predefined roles available with Dataverse. To run apps that use only out-of-the-box tables, there's the Basic User security role, where members can play the app within the environment and perform common tasks for the records that they own. More information: [Predefined security roles](/power-platform/admin/database-security#predefined-security-roles)

## Use Microsoft Entra groups to manage access

Administrators can use their organization's Microsoft Entra groups to manage access rights for licensed Dataverse users. Both types of Microsoft Entra groups—Microsoft 365 and Security—can be used to secure user-access rights to an app. More information: [About group teams](/power-platform/admin/manage-teams#about-group-teams)

### See also

[Discover more about creating users and assign security roles](/power-platform/admin/create-users-assign-online-security-roles)

[Minimum privileges for common tasks](/power-platform/admin/create-edit-security-role#minimum-privileges-for-common-tasks)

[Run a model-driven app on a mobile device](/dynamics365/customerengagement/on-premises/basics/dynamics-365-phones-tablets-users-guide-onprem)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
