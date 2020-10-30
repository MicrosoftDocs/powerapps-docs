---
title: "Create and edit One-to-many or Many-to-one table relationships using Power Apps portal | MicrosoftDocs"
description: "Learn how to create one-to-many or many-to-one table relationships using Power Apps portal"
ms.custom: ""
ms.date: 08/27/2019
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Create and edit One-to-many or Many-to-one table relationships using Power Apps portal

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

The [Power Apps portal](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) provides an easy way to create and edit 1:N (one-to-many) or N:1 (many-to-one) relationships for  Common Data Service.

The portal enables configuring the most common options, but certain options can only be set using solution explorer. More information: 
- [Create and edit 1:N (one-to-many) or N:1 (many-to-one) relationships](create-edit-1n-relationships.md)
- [Create and edit 1:N (one-to-many) or N:1 (many-to-one) table relationships using solution explorer](create-edit-1n-relationships-solution-explorer.md).

## View table relationships

1. From the [Power Apps portal](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), select either **Model-driven** or **Canvas** design mode.
2. Select **Data** > **tables** and select the table that has the relationships you want to view.
3. With the **Relationships** tab selected, you can select the following views: 

 |View|Description|
 |--|--|
 |**All**| Shows all the relationships for the table|
 |**Custom**|Shows only custom relationships for the table|
 |**Default**|Shows only the standard relationships for the table|

![Account table relationships](media/view-account-relationships-portal.png)

## Create relationships

While [viewing table relationships](#view-table-relationships), in the command bar, select **Add relationship** and choose either **Many-to-one** or **One-to-many**.

![Select type of relationship](media/add-relationship-menu-portal.png)

> [!NOTE]
> For information about **Many-to-many** relationships see [Create N:N (many-to-many) relationships](create-edit-nn-relationships.md)

> [!Important]
> The portal uses different terminology than solution explorer. The solution explorer **Primary table** is the **Current table** in the portal.

Depending on your choice you will see either:

|Type|Panel|
|--|--|
|**Many-to-one**|![Many to one relationship panel](media/many-to-one-relationship-panel.png)|
|**One-to-many**|![One to many relationship panel](media/one-to-many-relationship-panel.png)|

Choose the **Related table** for the relationship you want to create between the two tables. 

> [!NOTE]
> With either choice, a lookup field will be created on the *current* table.

Once you select the table you can edit the details of the relationship. In this example, multiple contact table records can be associated with a single account.

> [!div class="mx-imgBorder"] 
> ![One to many relationship account and contact](media/One-to-many-account-contact.png)

You can edit the default values provided before you save. Select **More options** to view the **Relationship name** and **Lookup field description** values

|Field|Description|
|--|--|
|**Lookup field display name**|The localizable text for the lookup field that will be created on the related table.<br />This can be edited later.|
|**Lookup field name**|The name for the Lookup field that will be created on the related table.|
|**Relationship name**|The name for the relationship that will be created.|
|**Lookup field description**|The description for the lookup field. In model-driven apps this will appear as a tooltip when people hover their mouse over the field. <br />This can be edited later.|

You can continue editing the table. Select **Save table** to create the relationship you have configured.

## Edit relationships

While [viewing table relationships](#view-table-relationships), select the relationship you want to edit.

> [!NOTE]
> Each relationship can be found within the primary table or the related table as a **Many-to-one** or **One-to-many** relationship. Although it can be edited in either place, it is the same relationship.
>
> The publisher of a managed solution can prevent some customizations of relationships that are part of their solution.

The only fields you can edit are **Lookup field display name** and **Lookup field description**. These can also be edited in the properties of the lookup field in the related table. More information: [Edit a field](create-edit-field-portal.md#edit-a-field)

## Delete relationships

While [viewing table relationships](#view-table-relationships), select the relationship you want to delete.

![Delete table relationship](media/delete-table-relationship-portal.png)

You can use the **Delete relationship** command from the command bar or from the row context menu when you click the ellipses (**...**).

Deleting the relationship will delete the lookup field on the related table.

> [!NOTE]
> You will not be able to delete a relationship that has dependencies. For example, if you have added the lookup field to a form for the related table, you must remove the field from the form before you delete the relationship.

### See also

[Create and edit relationships between tables](create-edit-table-relationships.md)<br />
[Create and edit 1:N (one-to-many) or N:1 (many-to-one) relationships](create-edit-1n-relationships.md)<br />
[Create and edit 1:N (one-to-many) or N:1 (many-to-one) table relationships using solution explorer](create-edit-1n-relationships-solution-explorer.md)<br />
[Edit a field](create-edit-field-portal.md#edit-a-field)
