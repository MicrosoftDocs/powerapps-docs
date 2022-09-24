---
title: Securing lists
description: Learn how to secure lists on a portal.
author: sandhangitmsft

ms.topic: conceptual
ms.custom: 
ms.date: 05/31/2022
ms.subservice: portals
ms.author: sandhan
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - sandhangitmsft
    - ProfessorKendrick
---

# Securing lists

To secure a list, you must configure [table permissions](entity-permissions-studio.md) for the table for which records are being displayed.

Starting with release [9.3.7.x](/power-platform/released-versions/portals/portalupdate1), newly created portals will have table permissions enforced for all lists irrespective of the **Enable Table Permissions** setting.

> [!NOTE]
> The changes described above also apply to portals [converted](../admin/convert-portal.md) from trial to production.

To configure anonymous access explicitly, use proper [table permissions](entity-permissions-studio.md), and relate to the **Anonymous Users** web role or a custom web role with **Anonymous Users Role** option.

Securing your list will ensure that users only see the records they have permissions for. 

Securing data related to specific users (or their related accounts) is accomplished by adding a relationship between the table and either the *contact* or *account* table whereby only portal users that have a relationship to these records will be able to access the data using the table permission type of *Account* or *Contact*, and the setting up appropriate privileges and associating [web roles](create-web-roles.md) to the table permission.

Good website design requires that if a user's role doesn't have permissions for the table (that is, there will never be a situation where they should see any records), they shouldn't have access to the page at all. Ideally, the page should also be protected by using [Page permissions](webpage-access-control.md).

If you want to display the records level actions that are applicable to the signed in user, you must set the value of **EntityList/ShowRecordLevelActions** site setting to **true**. 

For example, there are two users: Preston and Teddy. Preston has contact level all access on the *case* table, whereas Teddy has global read access. If a list is created to show all the *case* records, Preston would see all actions (**View**, **Edit**, and **Delete**) on the records that are related their contact. On other records, they would only see the **View** action. On the other hand, Teddy would only see the **View** action on all records.

If the **EntityList/ShowRecordLevelActions** site setting is set to **false** and the table has multiple permissions, all the record level actions are visible. But, when a user tries to perform an action without authorization, an error is displayed.

### See also

- [Work with lists](entity-lists.md)
- [Display multiple Dataverse records using lists](/learn/modules/portals-access-data-platform/2-entity-lists)
- [Configure a portal](configure-portal.md)  
- [Redirect to a new URL on a portal](add-redirect-url.md)
