---
title: "Set managed properties in Common Data Service metadata | MicrosoftDocs"
description: "Learn how to set managed properties for metadata items in a solution"
ms.custom: ""
ms.date: 12/19/2019
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
ms.assetid: edaa7d4a-a95f-4d66-a9d9-2ad6051332f7
caps.latest.revision: 41
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Set managed properties in Common Data Service metadata 

Managed properties only apply when you include metadata with a managed solution and import it into another environment. These settings allow a solution maker to have some control over the level of customization that they want to allow people who install their managed solution to have. 

For unmanaged components, you can view and change the managed properties. For managed components, you can view but not change the managed properties. 

> [!TIP]
> It is generally a good idea to allow people to extend metadata in your solution that works with business data. This will allow them to tailor your solution to their needs in the same way that they can for standard entities.
>
>For metadata that provides functionality to support your solution but does not contain business data, it is a good idea to limit what customizations are allowed.


## Entity managed properties
1.	Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and select **Solutions** from the left pane. 
2.	Open the solution that you want. 
3.	From the list of components in the solution, select **…** next to the unmanaged entity that you want to view or edit the managed properties, and then select **Managed properties**. 

    > [!div class="mx-imgBorder"] 
    > ![Entity managed properties command](media/entity-managed-properties.png "Entity managed properties command")

    The managed properties page is displayed. 

    > [!div class="mx-imgBorder"] 
    > <img src="media/managed-properties-dialog.png" alt="Managed properties pane" height="572" width="300">

<!-- [Managed properties pane](media/managed-properties-dialog.png "Managed properties pane") -->
  
Entities have more managed properties than any other type of solution component. If the entity is customizable, you can set the following options:  

|Option|Description|
|--|--|
|**Allow customizations** |Controls all the other options. If this option is `False`, none of the other settings apply. When it is `True`, you can specify the other customization options. When `False`, it is equivalent to setting all other options to false.|
|**Display name can be modified**|Whether the entity display name can be modified.|
|**Can Change Additional Properties** |Applies to anything not covered by other options.|
|**New forms can be created**|Whether new forms can be created for the entity.|
|**New charts can be created**|Whether new charts can be created for the entity.|
|**New views can be created** |Whether new views can be created for the entity.|
|**Can Change Hierarchical Relationship**|Whether Hierarchical Relationships settings can be changed. More information: [Define and query hierarchically related data](define-query-hierarchical-data.md)|
|**Can Change Tracking Be Enabled** |Whether the entity **Change Tracking** property can be changed.|
|**Can Enable sync to external search index** |Whether the entity can be configured to enable relevance search. More information: [Configure Relevance Search to improve search results and performance](/dynamics365/customer-engagement/admin/configure-relevance-search-organization) |

## Field managed properties

See [Create and edit fields for Common Data Service using Power Apps solution explorer](create-edit-field-solution-explorer.md) for information about how to edit fields.

While [viewing fields](create-edit-field-solution-explorer.md#view-fields), select a custom field from an unmanaged solution and then choose **More Actions** >  **Managed Properties** on the menu bar.

![View field managed properties](media/view-field-managed-properties-solution-explorer.png)  
  
This will open the **Set Managed Properties** dialog box.

![Set Field Managed Properties](media/set-field-managed-property.png)

The **Can be customized** option controls all the other options. If this option is **False**, none of the other settings apply. When it is **True**, you can specify the other customization options.  
  
If the field is customizable, you set the following options to **True** or **False**.  
  
- **Display name can be modified**
- **Can change requirement level** 
- **Can change Additional Properties**: This property controls any other customizations that do not have a specific managed property.

Setting all the individual options to **False**, is equivalent to setting **Can be customized** to **False**.  

Apply your choices and click **Set** to close the dialog box.

> [!NOTE]
> If this field is a **Date and Time** field, an additional **Can change date and time behavior** property is available. More information: [Behavior and format of the Date and Time field](behavior-format-date-time-field.md)

## Relationship managed properties

While viewing entity relationships, select a relationship from an unmanaged solution and then choose **More Actions** > **Managed Properties** on the menu bar.
  
With relationships, the only managed property is **Can Be Customized**. This single setting controls all changes that can be made to the entity relationship. 


### See also

[Managed properties](solutions-overview.md#managed-properties)<br />
[Create and edit entities using solution explorer](create-edit-entities-solution-explorer.md)<br />
[Create and edit fields for Common Data Service using Power Apps solution explorer](create-edit-field-solution-explorer.md)<br />
[Create and edit 1:N (one-to-many) or N:1 (many-to-one) entity relationships using solution explorer](create-edit-1n-relationships-solution-explorer.md)<br />
[Create N:N (many-to-many) entity relationships in Common Data Service using solution explorer](create-edit-nn-relationships-solution-explorer.md)
