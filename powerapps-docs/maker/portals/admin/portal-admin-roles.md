---
title: "Details about different security roles required to administer Power Apps portals with specific actions. | MicrosoftDocs"
description: "Learn about the available security roles, admin roles, and other permissions that are required to administer Power Apps portals."
author: neerajnandwana-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/12/2020
ms.author: nenandw
ms.reviewer: tapanm
---

# Admin roles required for portal administrative tasks

Power Apps portals has a variety of administrative tasks that can be performed by the members of different roles. The admin and security roles required to perform these tasks vary depending on the impact area. 

For example, some tasks may require the user to be a member of admin roles in [Microsoft 365](https://docs.microsoft.com/microsoft-365/admin/add-users/about-admin-roles?view=o365-worldwide&preserve-view=true), and others may need membership to security roles in [Power Platform environment](https://docs.microsoft.com/power-platform/admin/database-security). 

In this article, you'll learn about the role memberships required for a user to have the ability to perform specific administrative tasks for portals.

## Roles required for portal administrative tasks

The following table lists different administrative tasks for portals, and the roles required to perform that task. The listed tasks can be performed through the membership of the roles listed as required.

For example, to be able to download the public key of a portal, a user needs to be a member of only one of the listed required roles, such as a Global Admin, or a Power Platform admin. 

| Task | Required roles |
| - | - |
| [Download public key of a portal](get-public-key.md) | <ul> <li> [Global admin](#global-admin) or</li> <li> [Dynamics 365 administrator](#dynamics-365-administrator) or</li> <li> [Power Platform administrator](#power-platform-administrator)  or </li> <li> [System administrator](#system-administrator) or </li> <li> [Portal owner](#portal-owner) or </li> <li> [System customizer](#system-customizer) </li> </ul> |
| [Import metadata translation](import-metadata-translation.md) | <ul> <li> [Global admin](#global-admin) or</li> <li> [Dynamics 365 administrator](#dynamics-365-administrator) or</li> <li> [Power Platform administrator](#power-platform-administrator)  or </li> <li> [System administrator](#system-administrator) or </li> <li> [Portal owner](#portal-owner) or </li> <li> [System customizer](#system-customizer) </li> </ul> |
| [View portal error logs](view-portal-error-log.md) | <ul> <li> [Global admin](#global-admin) or</li> <li> [Dynamics 365 administrator](#dynamics-365-administrator) or</li> <li> [Power Platform administrator](#power-platform-administrator)  or </li> <li> [System administrator](#system-administrator) or </li> <li> [Portal owner](#portal-owner) </li> </ul> |
| [Reset a portal](reset-portal.md) | <ul> <li> [Global admin](#global-admin) or</li> <li> [Dynamics 365 administrator](#dynamics-365-administrator) or</li> <li> [Power Platform administrator](#power-platform-administrator)  or </li> <li> [System administrator](#system-administrator) or </li> <li> [Portal owner](#portal-owner) or </li> <li> [System customizer](#system-customizer) and [Portal app owner](#portal-app-owner) (both required) </li> </ul>  |
| [Convert a portal from trial to production](portal-lifecycle.md#convert-a-portal-from-trial-to-production) | <ul> <li> [Global admin](#global-admin) or</li> <li> [Dynamics 365 administrator](#dynamics-365-administrator) or</li> <li> [Power Platform administrator](#power-platform-administrator)  or </li> <li> [System administrator](#system-administrator) or </li> <li> [Portal owner](#portal-owner) or </li> <li> [System customizer](#system-customizer) and [Portal app owner](#portal-app-owner) (both required) </li> </ul> |
| [Convert an existing portal to a capacity-based model](portal-lifecycle.md#convert-an-existing-portal-to-a-capacity-based-model) | <ul> <li> [Global admin](#global-admin) or</li> <li> [Dynamics 365 administrator](#dynamics-365-administrator) or</li> <li> [Power Platform administrator](#power-platform-administrator)  or </li> <li> [System administrator](#system-administrator) or </li> <li> [Portal owner](#portal-owner) or </li> <li> [System customizer](#system-customizer) and [Portal app owner](#portal-app-owner) (both required) </li> </ul> |
| [Add a custom domain name](add-custom-domain.md) |  <ul> <li> [Global admin](#global-admin) or</li> <li> [Dynamics 365 administrator](#dynamics-365-administrator) or</li> <li> [Power Platform administrator](#power-platform-administrator)  or </li> <li> [System administrator](#system-administrator) or </li> <li> [Portal owner](#portal-owner) or </li> <li> [System customizer](#system-customizer) </li> </ul>   |
| [Connect to a Common Data Service environment using a portal](manage-auth-key.md) |  <ul> <li> [Global admin](#global-admin) or</li> <li> [Dynamics 365 administrator](#dynamics-365-administrator) or</li> <li> [Power Platform administrator](#power-platform-administrator)  or </li> <li> [System administrator](#system-administrator) or </li> <li> [Portal owner](#portal-owner) or </li> <li> [System customizer](#system-customizer) </li> </ul> |
| [Change the Dynamics 365 instance of a portal](change-dynamics-instance.md) |  <ul> <li> [Global admin](#global-admin) or</li> <li> [Dynamics 365 administrator](#dynamics-365-administrator) or</li> <li> [Power Platform administrator](#power-platform-administrator)  or </li> <li> [System administrator](#system-administrator) or </li> <li> [Portal owner](#portal-owner) or </li> <li> [System customizer](#system-customizer) </li> </ul> |

## Manage membership of the required roles

### Global admin

Global admin is a Microsoft 365 admin role. A person who purchases the Microsoft business subscription is a global admin. A global admin has unlimited control over products in the subscription and access to most data. 

To assign a user the global admin role, read [Assign admin roles in Microsoft 365](https://docs.microsoft.com/microsoft-365/admin/add-users/assign-admin-roles?view=o365-worldwide&preserve-view=true). 

More information: [About admin roles in Microsoft 365](https://docs.microsoft.com/microsoft-365/admin/add-users/about-admin-roles?view=o365-worldwide&preserve-view=true)

### Dynamics 365 administrator

Dynamics 365 administrator is a Power Platform service admin role. This role can perform admin functions on Power Platform because they have the system admin role.

To assign a user the Dynamics 365 administrator role, read [Assign a service admin role to a user](https://docs.microsoft.com/power-platform/admin/use-service-admin-role-manage-tenant#assign-a-service-admin-role-to-a-user).

### Power Platform administrator

Power Platform administrator is a Power Platform service admin role. This role can perform admin functions on Power Platform because they have the system admin role.

To assign a user the Power Platform administrator role, read [Assign a service admin role to a user](https://docs.microsoft.com/power-platform/admin/use-service-admin-role-manage-tenant#assign-a-service-admin-role-to-a-user).

### System administrator

System administrator is a Power Platform security role. This role has full permissions to customize and administrator Power Platform environment.

To assign a user the System administrator Power Platform role, read [Configure user security to resources in an environment](https://docs.microsoft.com/power-platform/admin/database-security).

### System customizer

System customizer is a Power Platform security role. This role has full permissions to customize Power Platform environment.

To assign a user the System administrator Power Platform role, read [Configure user security to resources in an environment](https://docs.microsoft.com/power-platform/admin/database-security).

### Portal owner

Portal owner is the user that created the Power Apps portal. This role can't be managed, and can't be changed.

### Portal app owner

Portal app owner is a user who owns [portal application registration](https://docs.microsoft.com/azure/active-directory/develop/quickstart-register-ap) in the [Azure portal](https://portal.azure.com)

To add an app owner for the portal app in Azure portal:

1. Sign in to the [Azure portal](https://portal.azure.com).

1. Search for and select **Azure Active Directory**.

1. Under **Manage**, select **App registrations**.

1. Select the Power Apps portals app from the list of available applications.

1. Under **Manage**, select **Owners**.

1. Select **Add owners**.

1. Select a user.

1. Select **Select**.

The user is added as an owner of the portal app.

### See also

- [Portal admin center](admin-overview.md)
- [Portal Management app](../configure/configure-portal.md)
- [Portal site settings](../configure/configure-site-settings.md)
