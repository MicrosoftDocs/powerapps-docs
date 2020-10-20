---
title: "Edit an entity in Power Apps | MicrosoftDocs"
description: "Learn the different ways that an entity can be edited"
ms.custom: ""
ms.date: 10/20/2020
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
ms.assetid: 8b00780c-74f0-4e3a-b570-b9289d0d5383
caps.latest.revision: 41
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Edit an entity

You can edit any custom entity that you create. Standard entities or managed custom entities may have limitations about changes you can make.  

You can perform the following edits to an entity:

- Entity properties. More information: [Edit entity properties using Power Apps](#edit-entity-properties-using-power-apps)

- **Fields**. More information:  [Create and edit fields for Common Data Service](create-edit-fields.md)
  
- **Relationships**. More information:  [Create and edit relationships between entities](create-edit-entity-relationships.md)

- **Keys**. [Define alternate keys to reference records](define-alternate-keys-reference-records.md)
  
You can also make changes to records that support the entity:  

- **Business Rules**. More information: [Create business rules and recommendations to apply logic in a form](../model-driven-apps/create-business-rules-recommendations-apply-logic-form.md)

- **Views**. More information:  [Create or edit a view](../model-driven-apps/create-edit-views.md)
  
- **Forms**. More information:  [Create and design forms](../model-driven-apps/create-design-forms.md)

- **Dashboards**. More information: [Create or edit dashboards](../model-driven-apps/create-edit-dashboards.md)

- **Charts**. [Create or edit a system chart](../model-driven-apps/create-edit-system-chart.md)

> [!NOTE]
> **Standard** entities are common entities that are included with your environment that are not **System** or **Custom** entities. *Managed custom entities* are entities that have been added to the system by importing a managed solution. The degree to which you can edit these entities is determined by the managed properties set for each entity. Any properties that can’t be edited will be disabled.

## Edit entity properties using Power Apps

In [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), select **Solutions**, open the unmanaged solution you want, and then select the entity you want to edit. To modify the entity properties, select **Settings** on the command bar to view the **Edit entity** pane as shown below:

![Edit entity properties](media/edit-entity-properties-powerapps-portal-designer.png)

For a description of the properties available to edit see, [Create an entity](data-platform-create-entity.md#create-an-entity).

> [!NOTE]
> Once enabled, not all entity properties can be changed. More information: [Entity options that can only be enabled](#entity-options-that-can-only-be-enabled)
>
> The name of many standard entities may also be used in other text in the application. To locate and change text where this name was used, see [Edit standard entity messages](edit-system-entity-messages.md)


## Edit an entity using Solution Explorer

When editing an entity using the solution explorer you need to find the unmanaged solution that you want to add it to.

[!INCLUDE [cc_navigate-solution-from-powerapps-portal](../../includes/cc_navigate-solution-from-powerapps-portal.md)]
  
<a name="BKMK_ChangeEntityName"></a> 
  
## Change the name of an entity  

Use the **Display Name** and **Plural Name** properties to change the name of the entity in the application. 

> [!NOTE]
>  The name of many standard entities may also be used in other text in the application. To locate and change text where this name was used, see [Edit standard entity messages](edit-system-entity-messages.md)
  
<a name="BKMK_ChangeEntityIcon"></a>   

###  Change the icons used for custom entities  

By default, all custom entities in the web application have the same icons. You can create image web resources for the icons you want for your custom entities. More information:  [Change icons for custom entities](../model-driven-apps/change-custom-entity-icons.md).  
  
<a name="BKMK_EnableOptions"></a>  
 
###  Entity options that can only be enabled  

The following table lists the options that you can enable for an entity, but after these items are enabled, they can’t be disabled:  

[!INCLUDE [cc_entity-set-once-options-table](../../includes/cc_entity-set-once-options-table.md)] 
  
<a name="BKMK_EnableDisableOptions"></a>  
 
###  Enable or disable entity options  

The following table lists the entity options that you can enable or disable at any time.  

[!INCLUDE [cc_entity-changeable-options-table](../../includes/cc_entity-changeable-options-table.md)] 

### See also

[Create an entity](create-edit-entities.md)<br />
[Create and edit entities using solution explorer](create-edit-entities-solution-explorer.md)
