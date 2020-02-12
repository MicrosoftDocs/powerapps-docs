---
title: Share a model-driven app with Power Apps | Microsoft Docs
description: Learn how to share a model-driven app
documentationcenter: ''
author: Mattp123
manager: kvivek
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: conceptual
ms.component: model
ms.date: 12/17/2019
ms.author: matp
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Share a model-driven app with Power Apps

[!INCLUDE [powerapps](../../includes/powerapps.md)] apps use role-based security for sharing. The fundamental concept in role-based security is that a security role contains privileges that define a set of actions that can be performed within the app. All app users must be assigned to one or more predefined or custom roles. Or, roles can also be assigned to teams. When a user or team is assigned to one of these roles, the person or team members are granted the set of privileges associated with that role. 

## Prerequisites
Ensure you have a [security role](https://docs.microsoft.com/power-platform/admin/security-roles-privileges) with equal or greater permissions than the role you're assigning to the app and to other users. 

You may **not** assign higher permissions roles than your current role. For example, users with the **System Customizer** role can assign other users the **Common Data Services User** role, but not vice versa. 

## Create a security role for your app
Generally model-driven apps contain custom entities and other custom configuration. It's important to first [create a security role](#create-a-security-role-for-your-app) with permission for all the components used in your app.  
> [!NOTE]
> This step can be skipped if existing roles grant access to the data in your app. 

## Share a model-driven app 
Sharing a model-driven app involves two primary steps. First, associate a one or more security role(s) with the app then assign the security role(s) to users. 
1. Visit https://make.powerapps.com
2. Select a model-driven app and click **Share**.
3. Select the app then choose a security role from the list.
4. Search for a user
5. Select the user then select a role from the list.
6. Click **Share**.

### Share the link to your app
Unlike sharing canvas apps, sharing model-driven apps does not currently send an email with a link to the app.

To get the direct link to an app:
1. Edit the app and click the **Properties** tab
2. Copy the **Unified Interface URL.**
3. Paste the app URL in a location so that your users can access it, such as by posting it on a SharePoint site or send via email.


## Create or configure a security role
The [!INCLUDE [powerapps](../../includes/powerapps.md)] environment includes [predefined security roles](#about-predefined-security-roles) that reflect common user tasks with access levels defined to match the security best-practice goal of providing access to the minimum amount of business data required to use the app. For example, if your app is based on a custom entity, the entity privileges must be explicitly specified before users may work in it. To do this, you can choose to do one of the following.
- Expand an existing predefined security role, so that it includes privileges on records based on the custom entity. 
- Create a custom security role for the purpose of managing privileges for users of the app. 

For more information about access and scope privileges, see [Security roles](https://docs.microsoft.com/dynamics365/customer-engagement/admin/security-roles-privileges#security-roles).

### Create a custom security role
1. On the [!INCLUDE [powerapps](../../includes/powerapps.md)] site select **Apps**, next to the app you want to share select **…**, and  then select **Share**.

2. Select the app then expand the list of security roles.

3. Click **Manage security roles.**

4. On the **All Roles** page, select **Common data service user** then click **Actions** then **Copy Role.** 

> [!TIP]
> You may also create a new blank role instead of copying an existing role. 

6. In the **Role Name** box provide a descriptive role such as *My custom app access*.  Click **Ok.**

7. From the security role designer, you select the actions, such as read, write, or delete, and the [access levels](https://docs.microsoft.com/power-platform/admin/security-roles-privileges#security-roles). Access levels determine how deep or high within the environments hierarchy the user can perform a particular action. 

8. Select the **Custom Entities** tab, and then locate the custom entity used in your app. 

9.  On the row for your custom entity, set access levels for each permission.  

10. Repeat for other entities used in your app. 

11. Select the **Customization** tab, and ensure **Read** privilege is set for **Model-driven App** so that organization access level ![Organization global scope](media/share-model-driven-app/organizational-scope-privilege.png) is selected.

    > [!IMPORTANT]
    > Users granted **Create** or **Write** to the **Model-driven App** privilege have access to all apps in the environment, even when they're not part of any role that has access to the app.
    > ![Create and Write with Model-driven App privilege](media/app-access-cds.png)

12. Select **Save and Close**. 


## About predefined security roles
These predefined roles are available with a [!INCLUDE [powerapps](../../includes/powerapps.md)] environment.


|Security role  |*Privileges  |Description |
|---------|---------|---------|
|Environment Maker     |  None       | Can create new resources associated with an environment including apps, connections, custom APIs, gateways, and flows using Power Automate. However, does not have any privileges to access data within an environment. More information: [Environments overview](https://powerapps.microsoft.com/blog/powerapps-environments/)        |
|System Administrator     |  Create, Read, Write, Delete, Customizations, Security Roles       | Has full permission to customize or administer the environment, including creating, modifying, and assigning security roles. Can view all data in the environment. More information: [Privileges required for customization](https://docs.microsoft.com/dynamics365/customer-engagement/customize/privileges-required-customization)        |
|System Customizer     | Create (self), Read (self), Write (self), Delete (self), Customizations         | Has full permission to customize the environment. However, can only view records for environment entities that they create. More information: [Privileges required for customization](https://docs.microsoft.com/dynamics365/customer-engagement/customize/privileges-required-customization)        |
|Common Data Service User     |  Read, Create (self), write (self), delete (self)       | Can run an app within the environment and perform common tasks for the records that they own.        |
|Delegate     | Act on behalf of another user        | Allows code to run as another user or impersonate.  Typically used with another security role to allow access to records. More information: [Impersonate another user](https://docs.microsoft.com/dynamics365/customer-engagement/developer/org-service/impersonate-another-user)        |

*Privilege is global scope unless specified otherwise.

## Use Azure Active Directory groups to manage access
Administrators can use their organization’s Azure Active Directory (Azure AD) groups to manage access rights for licensed Common Data Service users. Both types of Azure AD groups—Office and Security—can be used to secure user-access rights to an app. More information: [About group teams](/power-platform/admin/manage-teams.md#about-group-teams) 


### See also
[Run a model-driven app on a mobile device](../../user/run-app-client-model-driven.md)

[Create users and assign security roles](https://docs.microsoft.com/power-platform/admin/create-users-assign-online-security-roles)


