---
title: Enhanced view filter for lists
description: Learn how to configure an enhanced view filter for lists on a portal.
author: sandhangitmsft

ms.topic: conceptual
ms.custom: 
ms.date: 05/27/2022
ms.subservice: portals
ms.author: sandhan
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - sandhangitmsft
    - ProfessorKendrick
---

# Enhanced view filter for lists


[!INCLUDE[cc-pages-ga-banner](../../../includes/cc-pages-ga-banner.md)]

You can use Table Permissions if you want to secure records.  If you want to filter records based on the current portal user’s context, you can configure a filter on the underlying model-driven view definition used by the List using the [Dataverse view designer](../../model-driven-apps/create-edit-view-filters.md). This feature supports filtering of the current user, user's parent account, or website at any depth. Build the view filter to match any single contact record and the code will replace its value with the actual value at runtime&mdash;no need to assign values to fields in the Filter Conditions section.

- The control will find all condition elements where uitype="contact" and set the value to the actual value of the current portal user's contact ID.
- The control will find all condition elements where uitype="account" and set the value to the actual value of the current portal user's parent account ID.
- The control will find all condition elements where uitype="adx_website" and set the value to the actual value of the current website ID.

### Example View Filter Criteria

The following image shows an arbitrary contact assigned to a filter condition, this contact happens to be a stub 'dummy' contact but this could be any contact record. The ID of this record will be replaced by the actual value of the ID of the user viewing the page. If the user isn't logged in, no records will be returned. This provides greater flexibility in filtering the data based on the user and website contextually.

![Example view filter criteria.](media/entity-list-view-filter-criteria.png "Example view filter criteria")

> [!NOTE]
> If you are filtering by current portal user's contact or parent account then it is recommended that you associate a [Web Page Access Control Rule](webpage-access-control.md) to the Web Page to force the user to sign in. You would create a [Web Role](create-web-roles.md) with "Authenticated Users Role" checked. Create a Web Page Access Control Rule with "Restrict Read" right and associate the Web Role. This will force users to be signed in to view the page and therefore allow the data to be filled accordingly.

### See also

- [Work with lists](entity-lists.md)
- [Display multiple Dataverse records using lists](/training/modules/portals-access-data-platform/2-entity-lists)
- [Configure a portal](configure-portal.md)  
- [Redirect to a new URL on a portal](add-redirect-url.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
