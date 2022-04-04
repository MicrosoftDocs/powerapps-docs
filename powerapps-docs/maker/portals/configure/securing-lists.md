---
title: Securing lists
description: Learn how to secure lists on a portal.
author: sandhangitmsft

ms.topic: conceptual
ms.custom: 
ms.date: 04/04/2022
ms.subservice: portals
ms.author: sandhan
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - sandhangitmsft
    - ProfessorKendrick
---

# Securing lists

>[!NOTE]
> This method of securing lists would be deprecated soon. Therefore, it shouldn't be used. Use proper [table permissions](entity-permissions-studio.md), and web role setup to provide access to users for any data instead. More information: [Table permission changes for forms and lists on new portals](../important-changes-deprecations.md#table-permission-changes-for-forms-and-lists-on-new-portals)

To secure a list, you must configure Table Permissions for the table for which records are being displayed and also select the checkbox for **Enable Table Permissions** setting. If you don't, you'll see the following warning:

"Table permissions should be enabled for this record or anyone on the internet can view the data.".

The act of securing a list will ensure that for any user who accesses the page, only records that they have been given permission to are shown. This is achieved by an additional filter being added to the model-driven app views that are being surfaced via the list. This filter will filter only for records that are accessible to the user, via **Read** permission.

In addition, any actions that are defined for the list will respect the corresponding permissions for that action on a per-record basis. That is, if you have Edit permission for a record, the Edit action will be enabled for that record. The same applies for Delete, Create, and so on. Note that if no records are available, a message indicating this will be shown when the list is loaded.

However, good website design requires that if a user is not in a role that has any permissions for the table (that is, there will never be a situation where they should see any records), they should not have access to the page at all. Ideally, the page should be protected by using Webpage Access Permissions.

If you have secured a list by selecting **Enable Table Permissions**, and want to display the records level actions that are applicable to the signed in user, you must set the value of **EntityList/ShowRecordLevelActions** site setting to **true**. For example, there are two users: Preston and Teddy. Preston has contact level all access on the Case table, whereas Teddy has global read access. If a list is created to show all the case records, Preston would see all actions (View, Edit, and Delete) on the records that are related his contact. On other records, he would only see the **View** action. On the other hand, Teddy would only see the **View** action on all records.

If the **EntityList/ShowRecordLevelActions** site setting is set to **false** and the table has multiple permissions, all the record level actions are visible. But, when a user tries to perform an action that he is not authorized to, an error is displayed.

### See also

- [Microsoft Learn: Display multiple Dataverse records using lists](/learn/modules/portals-access-data-platform/2-entity-lists)
- [Configure a portal](configure-portal.md)  
- [Redirect to a new URL on a portal](add-redirect-url.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
