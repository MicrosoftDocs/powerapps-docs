---
title: Manage custom fields in an entity | Microsoft Docs
description: Create, read, update, and delete custom fields in an entity.
services: powerapps
documentationcenter: na
author: kfend
manager: kfend
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 10/20/2017
ms.author: kfend

---
# Manage custom fields
You can create and update one or more custom fields in any entity. When you create a custom field, you specify a set of properties, such as the field's name, its display name, and the type of data that it will contain. For more information, see [Enity field data types](https://docs.microsoft.com/common-data-service/entity-reference/field-data-types) and [Entity field properties](https://docs.microsoft.com/common-data-service/entity-reference/field-properties).

> [!NOTE]
> Every entity has [system fields](data-platform-create-entity.md#system-fields-and-the-record-title-field), such as fields that indicate when a record was last updated, and who updated it. In addition, [standard entities](data-platform-intro.md#standard-entities) have standard (default) fields. You can't modify or delete system fields or standard fields. If you create a custom field, it should provide functionality on top of these built-in fields.

## Create a field

1. On [powerapps.com](https://web.powerapps.com), expand the **Common Data Service** section and click or tap **Entities** in the left navigation pane. A list of entities appears. To show custom entities at the top of the list, click or tap the **Type** column header. You can also filter the list by typing one or more characters in the search bar.

2. Click or tap an entity, and then click or tap **Add field** near the top of the screen.

3. Under **Display name**, specify the string of text that will identify the field to users. For more information, see [Create an app](data-platform-create-app.md).

4. Under **Name**, specify the string of text that you will use to refer to the field in, for example, a formula when you build an app.
   
    > [!IMPORTANT]
    > Specify a name that's unique, clear, and meaningful, because you can't change the name after you create the field.

5. Under **Type**, specify the type of data that the field will contain, such as **Text** or **Number**.
   
    > [!IMPORTANT]
    > Specify this property carefully, because you might not be able to change it after the field contains data. For information about the types of data that you can specify, see [Understand entities](data-platform-intro.md#custom-fields).

6. If you're prompted, specify additional information for the data type that you specified.

7. Under **Unique**, select the check box if every record must have a unique value in this field.

8. Under **Required**, select the check box if every record must have a value in this field.
   
    > [!IMPORTANT]
    > You can't require that a custom field in a standard entity contain data. This restriction prevents you from breaking any apps that rely on that entity.

9. Click or tap **Save** to submit your changes.
   
    > [!IMPORTANT]
    > Your changes will be lost if you don't save them before you open another page in the browser or exit the browser.

You're notified when the operation is completed successfully. If the operation is unsuccessful, an error message indicates the issues that occurred and how you can fix them.

## Update or delete a field
1. On [powerapps.com](https://web.powerapps.com), click or tap **Manage**, click or tap **Entities**, and then click or tap an entity.
2. In the list of fields for the entity that you selected, click or tap a field, and then follow one of these steps:
   
   * Change one or more properties of the field. Keep in mind the [best practices and restrictions](data-platform-manage-fields.md#best-practices-and-restrictions).
     
       To select the next property, press Tab. To undo all changes to a field, click or tap the ellipsis (...) for the field, and then click or tap **Undo**.
   * Delete the field by clicking or tapping the ellipsis (...) near the right edge of the field, and then clicking or tapping **Delete**.
3. Click or tap **Save** to submit your changes.
   
    > [!IMPORTANT]
    > Your changes will be lost if you don't save them before you open another page in the browser or exit the browser.

You're notified when the operation is completed successfully. If the operation is unsuccessful, an error message indicates the issues that occurred and how you can fix them.

## Best practices and restrictions
As you create and modify fields, keep these points in mind:

* You can't modify or delete system fields or their values.
* In a standard entity, you can't modify or delete a standard (default) field, add a field that requires data, or make any other change that might break an app that relies on that entity.
* In a custom entity, you should make sure that the changes that you make won't break any app that relies on that entity.
* You must give each custom field a name that's unique within the entity, and you can't rename a field after you create it.
* You can change the data type of any field, provided that the field doesn't yet contain data. If the field already contains data, you can change the data type, provided that all the existing data meets the requirements of the new data type. For example, you can change the data type of a field from **Number** to **String**, but you can't change the data type from **String** to **Number** if the field contains non-numerical data.
* You might break an app that uses an entity if you modify a field in that entity in one or more of these ways:
  * You change the field's data type.
  * You require values, but one or more records don't contain a value in that field.
  * You require unique values, but two or more records contain the same value in that field.

## Next steps
* [Define relationships between entities](data-platform-entity-lookup.md)
* [Create an app using entities](data-platform-create-app.md)
* [Create an app from scratch using a Common Data Service database](data-platform-create-app-scratch.md)

## Privacy notice
With the Microsoft PowerApps common data model we collect and store custom entity and field names in our diagnostic systems.  We use this knowledge to improve the common data model for our customers. The entity and field names that Creators create help us understand scenarios that are common across the Microsoft PowerApps community and ascertain gaps in the service’s standard entity coverage, such as schemas related to organizations. The data in the database tables associated with these entities is not accessed or used by Microsoft or replicated outside of the region in which the database is provisioned. Note, however, the custom entity and field names may be replicated across regions and are deleted in accordance with our data retention policies. Microsoft is committed to your privacy as described further in our [Trust Center](https://www.microsoft.com/trustcenter/Privacy/default.aspx).

