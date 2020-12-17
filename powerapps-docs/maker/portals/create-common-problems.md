---
title: Common problems, issues, FAQs and resolutions while creating a Power Apps portal. | Microsoft Docs
description: Learn about frequent issues, problems, FAQs and resolutions while creating a Power Apps portal.
author: neerajnandwana-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 07/24/2020
ms.author: nenandw
ms.reviewer: tapanm
---

# Common problems and resolutions while creating a portal

In this article, you'll learn about the common problems that occur while creating a Power Apps portal, and how to resolve them.

## One portal of each type

Currently, you can create only one portal of each type in an environment per language. If you try to create more than one portal, you'll see an error message as follows:

> [!div class=mx-imgBorder]
> ![Maximum portal created error](media/portal-max-error.png "You have reached maximum limit of n portal(s) on this environment. Please choose another environment or create a new environment.")

To create more portals, you must create a new environment using the **Create new environment** link in the error message.

## No permissions to create a portal

If you don't have sufficient privileges to create a portal in an environment, you'll see an error as follows:

> [!div class=mx-imgBorder]
> ![Create portal error](media/portal-create-error.png "You don't have appropriate permissions to create a portal in this environment. Try selecting another environment or create new environment.")

More information: [Create a portal](create-portal.md), [Admin roles required for portal administrative tasks](admin/portal-admin-roles.md)

## Your data isn't quite ready

Sometimes the database creation can take time and the correct status might not reflect on the home page. In this case, you'll see the following message:

> [!div class=mx-imgBorder]
> ![Data not ready](media/data-not-ready.png "Your data isn't quite ready. The database that includes data for this app is still being built. We'll let you know once it's ready.")

If you keep getting the "create database" prompt or "your data isn't quite ready" prompt, you can try refreshing the Power Apps home page before selecting the **Portal from blank** tile.

## No permissions to create Azure Active Directory application

When you create a portal, portal as a new application is registered in Azure Active Directory associated with the tenant. If you don't have sufficient permissions to register an application with your Azure Active Directory tenant, you'll see an error as follows:

> [!div class=mx-imgBorder]
> ![Azure Active Directory error](media/azure-ad-error.png "You don't have required permissions to create Azure Active Directory applications in this tenant.")

To create and register applications in Azure Active Directory, you must contact your tenant administrator to turn on the **App registrations** setting for your tenant. For information, see [Required permissions](https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal#required-permissions).

## Portal creation blocked by global administrator

If portal creation is blocked in a tenant by your global administrator, you'll see an error as follows:

> [!div class=mx-imgBorder]
> ![Portal creation blocked error](media/portal-create-blocked-error.png "You don't have permissions to create a portal in this tenant as it is blocked by your global administrator.")

Contact your global administrator to enable creation of portals by non-administrators also.

If you're a global administrator, you must disable the `disablePortalsCreationByNonAdminUsers` tenant level setting through PowerShell. Run the following command in a PowerShell window (run PowerShell as an administrator).

```
Set-TenantSettings -RequestBody @{ "disablePortalsCreationByNonAdminUsers" = $false }
```

More information: [Disable portal creation in a tenant](create-portal.md#disable-portal-creation-in-a-tenant)

### See also

- [Create a Dataverse starter portal](create-portal.md)
- [Create a portal in an environment containing customer engagement apps](create-dynamics-portal.md)
- [Provision a portal using the older portal add-on](provision-portal-add-on.md)
