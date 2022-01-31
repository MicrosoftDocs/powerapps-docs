---
title: Share a model-driven app using Power Apps | Microsoft Docs
description: Learn how to share a model-driven app
documentationcenter: ''
author: Mattp123
manager: kvivek
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: how-to
ms.component: model
ms.date: 03/04/2020
ms.subservice: mda-maker
ms.author: matp
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Share a model-driven app using Power Apps



Model-driven apps use role-based security for sharing. The fundamental concept in role-based security is that a security role contains privileges that define a set of actions that can be performed on tables within the app.  This approach means that while two people are able to use the app, one user might only be able to read records, or records that they themselves created. The other user might be able to see all records and have the rights to delete those records.

All app users must be assigned one or more predefined or custom security roles. Or, security roles can be assigned to teams. When a user or team is assigned to one of these roles, the person or team members are granted the set of privileges associated with that role.

The process for sharing a model-driven app is different from sharing a canvas app. Model-driven app sharing depends on how the Microsoft Dataverse data table privileges are assigned for the tables that are in the app.

## App sharing prerequisites

There are a few key environment and licensing prerequisites required when sharing a model-driven app with a user.

- A Microsoft 365 user with Power Platform administrator rights or global admin rights must exist within the organization. [Learn how to assign Power Platform Administrator rights](/power-platform/admin/use-service-admin-role-manage-tenant).  This provides the user with administrator rights over all environments.
- The app sharer must have admin privileges to the specific environment (or be a Power Platform administrator). The app sharer must have a [security role](/power-platform/admin/security-roles-privileges) with equal or greater privileges than the security role they're assigning to the app and to other users. Usually, this takes the form of the app sharer having the Dataverse **System Administrator** or **System Customizer** security role.  These roles can be assigned by Power Platform administrators (who have rights over all Dataverse environments). The system administrator and system customizer security roles are standard roles that exist within all Dataverse environments.
- The user must exist as a user within the environment. It is not enough to only be a Microsoft 365 user. This is because all users in an environment are accounted for and described within tables in the environment. [Learn how to add a user to an environment](/power-platform/admin/add-users-to-environment)
- The user must have the correct [license](/power-platform/admin/pricing-billing-skus) to be able to use the app. This may be assigned through a per app plan pass, a per user license, or a pay as you go license.

Once the app sharing prerequisites are in place, you can [Share a model-driven app](#share-a-model-driven-app).

## Create a security role for your app

Model-driven apps often contain custom tables and other custom configuration. It is important to first create a security role with the required level of privilege for all the components used in your app.

> [!NOTE]
> This step can be skipped if existing roles grant access to the data in your app.

### Create or configure a security role

Power Platform [!INCLUDE [powerapps](../../includes/powerapps.md)] environments with a Dataverse database include [predefined security roles](#about-predefined-security-roles) that reflect common user tasks with access levels defined to match the security best-practice goal of providing access to the minimum amount of business data required to use the app. The privileges in the standard security roles provide appropriate access to standard tables, such as account or contact.

Custom tables, or tables that are new to the environment, will not have any privileges associated with them, by default. The privileges for custom table must be explicitly specified before users can work with it. To do this, you can choose to do one of the following.

- Copy an existing security role and edit the privileges accordingly. Copying is preferred to creating a security role from blank as there are a range of privileges that must be set to create a valid role that goes beyond setting privileges on specific tables.
- Create a new custom security role for the purpose of managing privileges for users of the app. Configure the new role for all tables in the app relevant for the user.
- Update an existing predefined security role, such as **Basic User**, so that it includes privileges (to read, write, delete, and so on) on records based on the custom table.

For more information about access and scope privileges, see [Security roles](/dynamics365/customer-engagement/admin/security-roles-privileges#security-roles).

### Create a custom security role

The following steps describe how to create a new security role from a copy of an existing security role.

1. On the [!INCLUDE [powerapps](../../includes/powerapps.md)] site select **Apps**, next to the app you want to share select **…**, and  then select **Share**.

2. Select the app then expand the list of security roles.
3. Select **Manage Security Roles**. A new screen opens that lists the security roles available in the environment.
4. Select the security role you want to copy, such as **Basic User**.  Then select **More Actions** > **Copy Role**.

    :::image type="content" source="media/share-model-driven-app/copy-security-role.png" alt-text="Copy a dataverse security role":::

5. Give the role a name.

    >[!Note]
    > Where a new role is required on the **All Roles** page, select **New**.

6. From the security role designer, you select the actions, such as read, write, or delete, and the scope for performing that action. Scope determines how deep or high within the environments hierarchy the user can perform a particular action.

7. Select the **Custom Entities** tab, and then locate the custom table that you want. For this example, the custom table named **Pet** is used.

8. On the **Pet** row, select each of the following privileges four times until organization scope global ![Organization global scope.](media/share-model-driven-app/organizational-scope-privilege.png) has been selected: **Read, Write, Append**

   > [!div class="mx-imgBorder"]
   > ![New security role.](media/share-model-driven-app/custom-security-role.png)

9.  Because the pet grooming app also has a relationship with the account table, select the **Core Rows** tab, and on the **Account** row select **Read** four times until organization scope global ![Organization global scope.](media/share-model-driven-app/organizational-scope-privilege.png) has been selected.

10. Select the **Customization** tab, and then in the privileges list select the **Read** privilege next to **Model-driven App** so that organization scope ![Organization global scope.](media/share-model-driven-app/organizational-scope-privilege.png) is selected.

    > [!div class="mx-imgBorder"]
    > ![Select security roles for the app.](media/app-access-specific-use.png)

11. Select **Save and Close**.

12. On the security role designer, in the **Role Name** box enter *Pet Grooming Schedulers*.

13. Select the **Custom Entities** tab, and then locate the **Pet** Entity.  

14. On the **Pet** row, select each of the following privileges four times until organization scope global ![Organization global scope.](media/share-model-driven-app/organizational-scope-privilege.png) has been selected:
    **Create, Read, Write, Delete, Append, Append To, Assign, Share**

15. Because the pet grooming app also has a relationship with the account table and schedulers must be able to create and modify account rows, select the **Core Rows** tab, and on the **Account** row select each of the following privileges four times until organization scope global ![Organization global scope.](media/share-model-driven-app/organizational-scope-privilege.png) has been selected. 
    **Create, Read, Write, Delete, Append, Append To, Assign, Share**

16. Select **Save and Close**.

## Assign a security role to a model-driven app

1. From the **Share this app** dialog, under **Assign users to the security role** select **Security Users**.
2. In the list that is displayed, select the users who are pet groomers, and then on the command bar select **Manage Roles**.

3. Select **Manage security roles.**
    > [!div class="mx-imgBorder"]
    > ![Manage roles.](media/share-model-driven-app/manage-roles.png "Manage roles")

4. On the **All Roles** page, select **Microsoft Dataverse user** then select **Actions** then **Copy Role.**

   > [!TIP]
   > You can also create a new blank role instead of copying an existing role.

6. In the Role Name box, provide a descriptive role such as *My custom app access*. Select **Ok.**

7. From the security role designer, you select the actions, such as read, write, or delete, and the [access levels](/power-platform/admin/security-roles-privileges#security-roles). Access levels determine how deep or high within the environments hierarchy the user can perform a particular action. 

8. Select the **Custom Tables** tab, and then locate the custom table used in your app.

9.  On the row for your custom table, set access levels for each privilege.  

10. Repeat for other tables used in your app.

11. Select the **Customization** tab, and ensure **Read** privilege is set for **Model-driven App** so that organization access level ![Organization global scope.](media/share-model-driven-app/organizational-scope-privilege.png) is selected.

    > [!IMPORTANT]
    > Users granted **Read**, **Create**, and **Write** to the **Model-driven App** privilege have access to all apps in the environment, even when they're not part of any role that has access to the app.
    > ![Create and Write with Model-driven App privilege.](media/app-access-cds.png)

12. Select **Save and Close**.

## Share a model-driven app

Before you share an app, it is helpful to understand the following model-driven app sharing basics:
- The app must have at least one security role associated with it, such as **Basic User**.
- App users must be assigned a security role from the available roles. Alternatively, a team can be assigned a security role, and users can be made members of the team. A team can be an Owner, Access, Azure AD security group, or Microsoft 365 group. [Learn to manage a Dataverse team](/power-platform/admin/database-security).

1. Go to https://make.powerapps.com.
2. Select a model-driven app, and then select **Share**.
3. Select the app, and then choose a security role from the list. [Learn how to assign a security role to an app](#assign-a-security-role-to-a-model-driven-app)
    > [!div class="mx-imgBorder"]
    > ![Assign a role to the app.](media/share-model-driven-app/share-app.png "Assign a role to the app")
4. Search for and select the user or team. Then select a security role from the list.
    > [!div class="mx-imgBorder"]
    > !["Assign a role to the user.](media/share-model-driven-app/share-user.png "Assign a role to the user")
6. Select **Share**.

## Share the link to your app

Unlike sharing canvas apps, sharing model-driven apps doesn't currently send an email with a link to the app.

To get the direct link to an app:

1. Go to [Power Apps](https://make.powerapps.com).
1. Select **Solutions** from the left navigation pane, and then open the solution that contains the model-driven app.
1. Select the model-driven app, and then select **Edit** on the command bar.
1. In the classic designer, select the **Properties** tab, and then copy the **Unified Interface URL.**

    !["Acquiring the link for a model-driven app"](media/share-model-driven-app/app-designer-copy-web-url-process.gif "Acquiring the link for a model-driven app")

1. Paste the app URL in a location so that your users can access it, such as by posting it on a SharePoint site or sending via email.

## Add the security role to a solution

To ensure application lifecycle management, we recommend that you make custom security roles a part of the Power Platform solution.

To add a security role to your solution, follow these steps:
1. Go to [Power Apps](https://make.powerapps.com).
2. Select the environment with the unmanaged solution.
3. Open th solution that requires the security role.
4. Select **Add existing** from the top menu.
5. Select **Security** > **Security Role**.
6. Select the newly created security role from the list provided.
7. Select **Add**.

This will ensure that the solution now contains the security role for import into other environments.

## About predefined security roles

These predefined roles are available with a [!INCLUDE [powerapps](../../includes/powerapps.md)] environment.  This helps us to put the security roles into context, and understand the most important ones out of the many available.

|Security role  |*Privileges  |Description |
|---------|---------|---------|
|Environment Maker     |  None       | Can create new resources associated with an environment including apps, connections, custom APIs, gateways, and flows using Power Automate. However, does not have any privileges to access data within an environment. More information: [Environments overview](https://powerapps.microsoft.com/blog/powerapps-environments/)        |
|System Administrator     |  Create, Read, Write, Delete, Customizations, Security Roles       | Has full permission to customize or administer the environment, including creating, modifying, and assigning security roles. Can view all data in the environment. More information: [Privileges required for customization](/dynamics365/customer-engagement/customize/privileges-required-customization)        |
|System Customizer     | Create (self), Read (self), Write (self), Delete (self), Customizations         | Has full permission to customize the environment. However, can only view rows for environment tables that they create. More information: [Privileges required for customization](/dynamics365/customer-engagement/customize/privileges-required-customization)        |
|Basic User     |  Read, Create (self), write (self), delete (self)       | Can run an app within the environment and perform common tasks for the rows that they own.        |
|Delegate     | Act on behalf of another user        | Allows code to run as another user or impersonate.  Typically used with another security role to allow access to rows. More information: [Impersonate another user](/dynamics365/customer-engagement/developer/org-service/impersonate-another-user)        |

*Privilege is global scope unless specified otherwise.

## Use Azure Active Directory groups to manage access

Administrators can use their organization’s Azure Active Directory (Azure AD) groups to manage access rights for licensed Dataverse users. Both types of Azure AD groups—Microsoft 365 and Security—can be used to secure user-access rights to an app. More information: [About group teams](/power-platform/admin/manage-teams#about-group-teams)

### Next steps

[Discover more about creating users and assign security roles](/power-platform/admin/create-users-assign-online-security-roles)

[Run a model-driven app in a browser](../model-driven-apps/run-model-driven-app.md)

[Run a model-driven app on a mobile device](/dynamics365/customerengagement/on-premises/basics/dynamics-365-phones-tablets-users-guide-onprem)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]