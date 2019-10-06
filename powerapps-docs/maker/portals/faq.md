---
title: Frequently asked questions | Microsoft Docs
description: Frequently asked questions in PowerApps Portals.
author: sbmjais
manager: shujoshi
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/02/2019
ms.author: shjais
ms.reviewer:
---

# PowerApps Portals FAQ

We have compiled a list of frequently asked questions and provided brief answers to help you get to your information quickly.

## I'm getting an error that only one portal can be created.

Currently, you can create only one portal of each type in an environment per language. If you try to create more than one portal, you'll see an error message as follows:

> [!div class=mx-imgBorder]
> ![Maximum portal created error](media/portal-max-error.png "Maximum portal created error")

To create more portals, you must create a new environment using the **create new environment** link in the error message. For more information on creating a portal, see [Create a portal](create-portal.md).

## I'm getting an error that I can't delete my portal.

If you don't have sufficient privileges to delete a portal, you'll see an error as follows:

> [!div class=mx-imgBorder]
> ![Delete portal error](media/portal-delete-error.png "Delete portal error")

For information on deleting a portal and the required privileges, see [Delete a portal](manage-existing-portals.md#delete).

## I'm getting an error that I can't create a portal.

If you don't have sufficient privileges to create a portal in an environment, you'll see an error as follows:

> [!div class=mx-imgBorder]
> ![Create portal error](media/portal-create-error.png "Create portal error")

For information on creating a portal and the required privileges, see [Create a portal](create-portal.md).

## I'm getting the message: “Your data isn’t quite ready”.

Sometimes the database creation can take time and the correct status might not reflect on the home page. In this case you'll see the following message:

> [!div class=mx-imgBorder]
> ![Data not ready](media/data-not-ready.png "Data not ready")

If you keep getting the create database prompt or your data isn't quite ready prompt, you can try refreshing the PowerApps home page before selecting the Portal from blank (Preview) tile.

## I'm getting an error that I don't have required permissions to create Azure Active Directory applications.

When you create a portal, portal as a new application is registered in Azure Active Directory associated with the tenant. If you don't have sufficient permissions to register an application with your Azure Active Directory tenant, you'll see an error as follows:

> [!div class=mx-imgBorder]
> ![Azure Active Directory error](media/azure-ad-error.png "Azure Active Directory error")

To create and register applications in Azure Active Directory, you must contact your tenant administrator to turn on the **App registrations** setting for your tenant. For information, see [Required permissions](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal#required-permissions).

## I'm getting an error that portal creation is blocked in this tenant by global administrator

If portal creation is blocked in a tenant by your global administrator, you'll see an error as follows:

> [!div class=mx-imgBorder]
> ![Portal creation blocked error](media/portal-create-blocked-error.png "Portal creation blocked error")

You must contact your global administrator to enable creation of portals by non-administrators also.

If you are a global administrator, you must disable the `disablePortalsCreationByNonAdminUsers` tenant level setting through PowerShell. Run the following command in a PowerShell window (run PowerShell as an administrator).

```
Set-TenantSettings -RequestBody @{ "disablePortalsCreationByNonAdminUsers" = $false }
```

More information: [Disable portal creation in a tenant](create-portal.md#disable-portal-creation-in-a-tenant)
