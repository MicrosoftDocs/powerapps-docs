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
To share an app you must have the [!INCLUDE [powerapps](../../includes/powerapps.md)] Environment Admin or System Admin role. 

## Share your app for basic use
To add privileges so the app user can run an app within the environment and perform common tasks for the records that they own, use the **Common Data Services User** security role.
1.	On the [Power Apps](https://web.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) site select **Apps**, next to the model-driven app you want to share select **…**, and then select **Share**. 
	> [!IMPORTANT]
    > The steps to share a model-driven app are different from a canvas app. For steps to share a canvas app, see [Share a canvas app in Power Apps](../canvas-apps/share-app.md). 

2.	Under **Assign users to the security role** select **Security Users**.
3.	From the list of enabled users select the users that you want to grant access to your app, and then on the command bar select **Manage Roles**. 
4.	In the **Manage User Roles** dialog box, select the **Common Data Service User** security role, and then select **OK**. 

    > [!div class="mx-imgBorder"] 
    > ![](media/share-model-driven-app/select-common-data-service-user.png "Select Common Data Service User")

5. [Add security roles to the app](#add-security-roles-to-the-app)
6. [Share the link to your app](#share-the-link-to-your-app)

Users with the Common Data Service User security role can now access your app. 

## Share a model-driven app for specific use
In this section you perform the tasks for sharing a model-driven app using two security roles, each specific to the app users needs. You learn how to:
- Create a custom security role
- Assign users to the custom security role
- Assign the security role to an app

### Tutorial overview 
The section will follow the company, Contoso, which has a pet grooming business that services dogs and cats. An app that contains a custom entity for tracking the pet grooming business has already been created and published. Now the app must be shared so that the pet grooming staff can use it. To share the app, an administrator or app maker assigns one or more security roles to users and to the app. 

### Create or configure a security role
The [!INCLUDE [powerapps](../../includes/powerapps.md)] environment includes [predefined security roles](#about-predefined-security-roles) that reflect common user tasks with access levels defined to match the security best-practice goal of providing access to the minimum amount of business data required to use the app. Remember that the Contoso pet grooming app is based on a custom entity. Because the entity is custom, privileges must be explicitly specified before users may work in it. To do this, you can choose to do one of the following.
- Expand an existing predefined security role, so that it includes privileges on records based on the custom entity. 
- Create a custom security role for the purpose of managing privileges for users of the app. 

Because the environment that will maintain the pet grooming records is also used for other apps that the Contoso business runs, a custom security role specific to the pet grooming app will be created. Additionally, two different sets of access privileges are required.
- Pet grooming technicians only need to read, update, and attach other records so their security role will have read, write, and append privileges. 
- Pet grooming schedulers need all the privileges that pet grooming technicians have, plus the ability to create, append to, delete, and share, so their security role will have create, read, write, append, delete, assign, append to, and share privileges.

For more information about access and scope privileges, see [Security roles](https://docs.microsoft.com/dynamics365/customer-engagement/admin/security-roles-privileges#security-roles).

### Create a custom security role
1. On the [!INCLUDE [powerapps](../../includes/powerapps.md)] site select **Apps**, next to the app you want to share select **…**, and  then select **Share**.

2. From the **Share this app** dialog, under **Create a security role** select **Security Setting**.

3. On the **All Roles** page, select **New**.  

4. From the security role designer, you select the actions, such as read, write, or delete, and the scope for performing that action. Scope determines how deep or high within the environments hierarchy the user can perform a particular action. In the **Role Name** box enter *Pet Grooming Technicians*.

5. Select the **Custom Entities** tab, and then locate the custom entity that you want. For this example, the custom entity named **Pet** is used. 

6. On the **Pet** row, select each of the following privileges four times until organization scope global ![Organization global scope](media/share-model-driven-app/organizational-scope-privilege.png) has been selected: **Read, Write, Append**

   > [!div class="mx-imgBorder"] 
   > ![New security role](media/share-model-driven-app/custom-security-role.png)

7. Because the pet grooming app also has a relationship with the account entity, select the **Core Records** tab, and on the **Account** row select **Read** four times until organization scope global ![Organization global scope](media/share-model-driven-app/organizational-scope-privilege.png) has been selected. 

8. Select the **Customization** tab, and then in the privileges list select the **Read** privilege next to **Model-driven App** so that organization scope ![Organization global scope](media/share-model-driven-app/organizational-scope-privilege.png) is selected.

9. Select **Save and Close**. 

10. On the security role designer, in the **Role Name** box enter *Pet Grooming Schedulers*. 

11. Select the **Custom Entities** tab, and then locate the **Pet** entity. 

12. On the **Pet** row, select each of the following privileges four times until organization scope global ![Organization global scope](media/share-model-driven-app/organizational-scope-privilege.png) has been selected:
    **Create, Read, Write, Delete, Append, Append To, Assign, Share**

13. Because the pet grooming app also has a relationship with the account entity and schedulers must be able to create and modify account records, select the **Core Records** tab, and on the **Account** row select each of the following privileges four times until organization scope global ![Organization global scope](media/share-model-driven-app/organizational-scope-privilege.png) has been selected. 
    **Create, Read, Write, Delete, Append, Append To, Assign, Share**

14. Select **Save and Close**.

### Assign security roles to users
Security roles control a user’s access to data through a set of access levels and permissions. The combination of access levels and permissions that are included in a specific security role sets limits on the user’s view of data and on the user’s interactions with that data.

#### Assign a security role to Pet Grooming Technicians
1. From the **Share this app** dialog, under **Assign users to the security role** select **Security Users**.
2. In the list that is displayed, select the users who are pet groomers, and then on the command bar select **Manage Roles**.

    > [!div class="mx-imgBorder"] 
    > ![Manage roles](media/share-model-driven-app/select-users-for-security-roles.png)

3. In the **Manage User Roles** dialog box, select the **Pet Grooming Technicians** security role that you created earlier, and then select **OK**.

#### Assign a security role to Pet Grooming Schedulers
1. From the **Share this app** dialog, under **Assign users to a security role** select **Security Users**.
2. In the list that is displayed, select the pet grooming schedulers.
3. Select **Manage Roles**.
4. In the **Manage User Roles** dialog box, select the **Pet Grooming Schedulers** security role that you created earlier, and then select **OK**.


## Add security roles to the app
One or more security roles need to be assigned to the app. Users will have access to apps based on the security roles they're assigned to.
1. From the **Share this app** dialog box, under **Add the security role to your app** select **My Apps**.
2. In the lower-right corner of the app tile of the app, select **More options (...)**, and then select **Manage Roles**.

    ![Manage roles for the app](media/share-model-driven-app/manage-roles.png)

4. In the **Roles** section, you can choose whether to give app access to all security roles or selected roles. For basic app access, select the **Common Data Service User** security role. For more specific access, select another standard, or a custom or customized security role. For example, select the **Pet Grooming Schedulers** and **Pet Grooming Technicians** roles you created earlier in this section. 

    > [!div class="mx-imgBorder"] 
    > ![Select security roles for the app](media/share-model-driven-app/app-security-roles.png)

5. Select **Save**. 
 

    > [!IMPORTANT]
    > Users granted **Create** or **Write** to the **Model-driven App** privilege have access to all apps in the environment, even when they're not part of any role that has access to the app.
    > ![Create and Write with Model-driven App privilege](media/app-access-cds.png)

## Share the link to your app
1. From the **Share this app** dialog box, under **Share the link to your app directly with users** copy the URL that is displayed.
   > [!div class="mx-imgBorder"] 
   > ![Share the link](media/share-model-driven-app/share-model-driven-url.png)

2. Select **Close**.
3. Paste the app URL in a location so that your users can access it, such as by posting it on a SharePoint site or send via email.

You can also find the app URL on the **Properties** tab in app designer. 

> [!div class="mx-imgBorder"] 
> ![Copy app URL](media/share-model-driven-app/app-designer-copy-web-url.png)

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



