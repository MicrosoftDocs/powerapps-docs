---
title: Roles required for portal administration
description: Learn about the available security roles, admin roles, and other permissions that are required to administer Power Apps portals.
author: neerajnandwana-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 08/09/2021
ms.subservice: portals
ms.author: nenandw
ms.reviewer: tapanm
contributors:
    - neerajnandwana-msft
    - tapanm-msft
---

# Roles required for portal administration

Different administrative tasks in Power Apps portals can be performed by members of different roles. The admin and security roles required to do these tasks vary depending on the impact area.

For example, some tasks might require the user to be a member of admin roles in [Microsoft 365](/microsoft-365/admin/add-users/about-admin-roles?preserve-view=true&view=o365-worldwide), and others might need membership to security roles in the [Microsoft Power Platform environment](/power-platform/admin/database-security).

In this article, you'll learn about the roles and permissions required to do different administrative tasks for portals.

## Required roles and permissions

The following table lists different administrative tasks for portals, and the roles required to do that task. Users who are members of those roles can perform the corresponding task.

| Task | Required roles |
| - | - |
| [Add a custom domain name](add-custom-domain.md) | Any one of the following roles: <ul> <li> [Portal owner](#portal-owner) </li> <li> [System customizer](#system-customizer) </li> <li> [System administrator](#system-administrator) </li> <li> [Dynamics 365 administrator](#dynamics-365-administrator) </li> <li> [Power Platform administrator](#power-platform-administrator) </li> <li> [Global administrator](#global-administrator) </li> </ul>   |
| [Change the Dynamics 365 instance of an add-on portal](change-dynamics-instance.md) | Any one of the following roles: <ul> <li> [Portal owner](#portal-owner) </li> <li> [System customizer](#system-customizer) </li> <li> [System administrator](#system-administrator) </li> <li> [Dynamics 365 administrator](#dynamics-365-administrator) </li> <li> [Power Platform administrator](#power-platform-administrator) </li> <li> [Global administrator](#global-administrator) </li> </ul> |
| [Manage portal authentication key](manage-auth-key.md) | Any one of the following roles: <ul> <li> [Portal owner](#portal-owner) </li> <li> [System customizer](#system-customizer) </li> <li> [System administrator](#system-administrator) </li> <li> [Dynamics 365 administrator](#dynamics-365-administrator) </li> <li> [Power Platform administrator](#power-platform-administrator) </li> <li> [Global administrator](#global-administrator) </li> </ul> |
| [Convert an existing portal to capacity-based model](convert-portal.md#convert-an-existing-portal-to-capacity-based-model) |  [Portal app owner](#portal-app-owner) and any one of the following roles: <ul> <li> [Portal owner](#portal-owner) </li> <li> [System customizer](#system-customizer) </li> <li> [System administrator](#system-administrator) </li> <li> [Dynamics 365 administrator](#dynamics-365-administrator) </li> <li> [Power Platform administrator](#power-platform-administrator) </li> <li> [Global administrator](#global-administrator) </li> </ul> |
| [Convert a portal from trial to production](convert-portal.md#convert-a-portal-from-trial-to-production) | [Portal app owner](#portal-app-owner) and any one of the following roles: <ul> <li> [Portal owner](#portal-owner) </li> <li> [System customizer](#system-customizer) </li> <li> [System administrator](#system-administrator) </li> <li> [Dynamics 365 administrator](#dynamics-365-administrator) </li> <li> [Power Platform administrator](#power-platform-administrator) </li> <li> [Global administrator](#global-administrator) </li> </ul> |
| [Create a portal](..\create-portal.md) | Required roles and permissions in Azure Active Directory (Azure AD): <ul> <li> Is [portal creation disabled](../control-portal-creation.md) in the tenant? </li> <ul> <li> If **No**, [permissions to register an app](/azure/active-directory/develop/howto-create-service-principal-portal#permissions-required-for-registering-an-app) in Azure AD are required. </li> <li> If **Yes**, only a [Global administrator](#global-administrator) can create a portal. </ul> </ul> <br> Required roles and permissions in Microsoft Power Platform (both are required): <ul> <li>A user account with [Read-Write Access Mode](#read-write-access-mode). </li> <li>[System administrator](#system-administrator) role. </li> </ul> <ul>   |
| [Download the public key of a portal](get-public-key.md) | Any one of the following roles: <ul> <li> [Portal owner](#portal-owner) </li> <li> [System customizer](#system-customizer) </li> <li> [System administrator](#system-administrator) </li> <li> [Dynamics 365 administrator](#dynamics-365-administrator) </li> <li> [Power Platform administrator](#power-platform-administrator) </li> <li> [Global administrator](#global-administrator) </li> </ul> |
| [Import metadata translation](import-metadata-translation.md) | Any one of the following roles: <ul> <li> [Portal owner](#portal-owner) </li> <li> [System customizer](#system-customizer) </li> <li> [System administrator](#system-administrator) </li> <li> [Dynamics 365 administrator](#dynamics-365-administrator) </li> <li> [Power Platform administrator](#power-platform-administrator) </li> <li> [Global administrator](#global-administrator) </li> </ul> |
| [Reset a portal](reset-portal.md) | [Portal app owner](#portal-app-owner) and any one of the following roles: <ul> <li> [Portal owner](#portal-owner) </li> <li> [System customizer](#system-customizer) </li> <li> [System administrator](#system-administrator) </li> <li> [Dynamics 365 administrator](#dynamics-365-administrator) </li> <li> [Power Platform administrator](#power-platform-administrator) </li> <li> [Global administrator](#global-administrator) </li> </ul> |
| [Update the Dynamics 365 instance of a portal](update-dynamics365-instance.md) | User account with [Read-Write Access Mode](#read-write-access-mode) and any one of the following roles: <ul> <li> [System administrator](#system-administrator)</li><li>[Portal app owner](#portal-app-owner)</li> <li>[Global administrator](#global-administrator) </li> </ul> |
| [Update portal packages](update-portal-solution.md) | User account with [Read-Write Access Mode](#read-write-access-mode) and [System administrator](#system-administrator) |
| [View portal error logs](view-portal-error-log.md) | Any one of the following roles: <ul> <li> [Portal owner](#portal-owner) </li> <li> [System administrator](#system-administrator) </li> <li> [Dynamics 365 administrator](#dynamics-365-administrator) </li> <li> [Power Platform administrator](#power-platform-administrator) </li> <li> [Global administrator](#global-administrator) </li> </ul> |

## Manage membership of the required roles

This section describes how to manage the membership of the required roles in the preceding table for different kinds of administrative tasks in Power Apps portals.

### Dynamics 365 administrator

*Dynamics 365 administrator* is a Microsoft Power Platform service admin role. This role can do admin functions on Microsoft Power Platform because they have the system admin role.

To assign a user the Dynamics 365 administrator role, go to [Assign a service admin role to a user](/power-platform/admin/use-service-admin-role-manage-tenant#assign-a-service-admin-role-to-a-user).

### Global administrator

*Global administrator* is a Microsoft 365 admin role. A person who purchases the Microsoft business subscription is a global administrator. A global administrator has unlimited control over products in the subscription and access to most data.

To assign a user the global administrator role, go to [Assign admin roles in Microsoft 365](/microsoft-365/admin/add-users/assign-admin-roles?preserve-view=true&view=o365-worldwide).

More information: [About admin roles in Microsoft 365](/microsoft-365/admin/add-users/about-admin-roles?preserve-view=true&view=o365-worldwide)

### Portal app owner

A *portal app owner* is a user who owns [portal application registration](/azure/active-directory/develop/quickstart-register-app) in the [Azure portal](https://portal.azure.com).
<!--markdownlint-disable MD036-->
**To add an app owner for the portal app in the Azure portal**
<!--markdownlint-enable MD036-->
1. Sign in to the [Azure portal](https://portal.azure.com).

1. Search for and select **Azure Active Directory**.

1. Under **Manage**, select **App registrations**.

1. Select the Power Apps portals app from the list of available applications.

1. Under **Manage**, select **Owners**.

1. Select **Add owners**.

1. Select a user.

1. Select **Select**.

The user is added as an owner of the portal app.

### Portal owner

The *portal owner* is the user who created the Power Apps portal. This role can't be managed and can't be changed.

### Read-Write Access Mode

This is a user account in Microsoft Power Platform with **Access Mode** set to *Read-Write*. More information: [Create a Read-Write user account](/power-platform/admin/create-users-assign-online-security-roles#create-a-read-write-user-account)

### System administrator

*System administrator* is a Microsoft Power Platform security role. This role has full permissions to customize and administrator a Microsoft Power Platform environment.

To assign a user the System administrator Power Platform role, go to [Configure user security to resources in an environment](/power-platform/admin/database-security).

### System customizer

*System customizer* is a Microsoft Power Platform security role. This role has full permissions to customize a Microsoft Power Platform environment.

To assign a user the System administrator Power Platform role, go to [Configure user security to resources in an environment](/power-platform/admin/database-security).

### Power Platform administrator

*Power Platform administrator* is a Microsoft Power Platform service admin role. This role can perform admin functions on Microsoft Power Platform because they have the system admin role.

To assign a user the Power Platform administrator role, go to [Assign a service admin role to a user](/power-platform/admin/use-service-admin-role-manage-tenant#assign-a-service-admin-role-to-a-user).

### See also

[Portal admin center](admin-overview.md)  
[Portal Management app](../configure/configure-portal.md)  
[Portal site settings](../configure/configure-site-settings.md)  


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]