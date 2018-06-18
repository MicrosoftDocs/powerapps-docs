---
title: "Map entity fields in PowerApps | MicrosoftDocs"
description: "Learn how to map entity fields"
ms.custom: ""
ms.date: 05/29/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 7c5aa1c3-bde9-43f1-a369-fdcdbf14dec0
caps.latest.revision: 33
ms.author: "matp"
manager: "kvivek"
tags: 
---
# Map entity fields
 
You can map attributes between entities that have an entity relationship. This lets you set default values for a record that is created in the context of another record. 

## Easier way to create new records in model-driven apps

Let’s say that people want to add a new contact record for a person who is an employee for a specific account. They can do this in two different ways:  
  
### The hard way

People could just navigate in the app to create a new contact record from scratch. But then they need to set the parent account and enter several items of information (such as address and phone information) which are probably the same as the parent account. This can be time consuming and introduces opportunities for errors.  
  
### The easier way

The easier way is to start with the account entity and, using the **Contacts** subgrid on the form, select **+** to add a contact. It will first guide people to look up any existing related contacts so they don’t accidentally create a duplicate record. If they don’t find an existing record, they can select **New** and create a new contact record. 

The new contact record form will include any of the mapped attribute values from the account (such as address and phone information) as the default values. People can edit these values before they save the record.

## How this works

When you map entity fields for a 1:N entity relationship certain items of data from the primary entity record will be copied into the new related entity form to set default values that people can edit before saving.
 
  
> [!NOTE]
> These mappings only set default values to a record before it is saved. People can edit the values before saving. The data that is transferred is the data at that point in time. It isn’t synchronized if the source data later changes.
>   
> These mappings aren’t applied to related records created using a workflow or dialog process. They aren’t automatically applied to new records created using code, although developers can use a special message called `InitializeFrom` ([InitializeFrom Function](/dynamics365/customer-engagement/web-api/initializefrom?view=dynamics-ce-odata-9) or [InitializeFromRequest Class](/dotnet/api/microsoft.crm.sdk.messages.initializefromrequest?view=dynamics-general-ce-9)) to create a new record using available mappings.  

## Open solution explorer

The only way to map entity fields is to use solution explorer.

[!INCLUDE [cc_navigate-solution-from-powerapps-portal](../../../includes/cc_navigate-solution-from-powerapps-portal.md)]
  
Mapping fields is done in the context of a 1:N or N:1 entity relationship, so first you need to [view 1:N or N:1 entity relationships](create-edit-1n-relationships-solution-explorer.md#view-entity-relationships).

## View mappable fields

Field mappings aren’t actually defined within the entity relationships, but they are exposed in the relationship user interface. Not every 1:N entity relationship has them. When you view a list of 1:N (or N:1) entity relationships for an entity, you can filter the relationships shown by type. You can select either **All**, **Custom**, **Customizable**, or **Mappable**. Mappable entity relationships provide access to allow mapping entity fields. 

![View mappable entity relationships](media/mappable-entity-relationships.png) 

When you open a mappable entity relationship, select **Mappings** in the left navigation.

![Select Mappings for the entity relationship](media/map-entity-fields-ui-solution-explorer.png)

## Delete mappings

If there are any mappings that you do not want to apply, you can select them and click the ![Delete icon](media/delete.gif) icon.

## Add new mappings

To create a new mapping click **New** in the toolbar. This will open the **Create Field Mapping** dialog.

![Create field mapping dialog](media/create-field-mapping-dialog.png)

Select one source entity field and one target entity fields with values you want to map. 

![Configure field mapping](media/configure-field-mapping.png)

Then select **OK** to close the dialog.

The following rules show what kinds of data can be mapped.  
  
- Both fields must be of the same type and the same format.  
- The length of the target field must be equal to or greater than the length of the source field.  
- The target field can’t be mapped to another field already.  
- The source field must be visible on the form.  
- The target field must be a field that a user can enter data into.  
- Address ID values can’t be mapped.
- If you map to or from a field that isn’t displayed on a form, the mapping won't be done until the field is added to a form.
- If the fields are option sets, the integer values for each option should be identical.  
  
> [!NOTE]
>  If you need to map option set fields, we recommend you configure both fields to use the same global option set. Otherwise, it can be difficult to keep two separate sets of options synchronized manually. If the integer values for each option aren’t mapped correctly you can introduce problems in your data. More information: [Create and edit global option sets for Common Data Service for Apps (picklists)](create-edit-global-option-sets.md)  
  
## Automatically generate field mappings  

You can also generate mappings automatically by selecting **Generate Mappings** from the **More Actions** menu.

You should use care when doing this with system entities. Use this when you create custom entities and want to leverage mapping. 

> [!WARNING]
> This removes any existing mappings and replaces them with suggested mappings that are based only on the fields that have similar names and data types. If you use this on a system entity, you could lose some expected mappings. For custom entities, it helps save time because you can more easily delete any mappings you don’t want and add any others that the generate mappings action didn’t create.  


## Publish customizations 

Because field mappings are not metadata, you must publish them before changes take effect. 
<!-- TODO Need a general topic about publishing to link to in situations like this -->

### See also
[Create and edit 1:N (one-to-many) or N:1 (many-to-one) entity relationships using solution explorer](create-edit-1n-relationships-solution-explorer.md)<br />
[Developer Documentation: Customize entity and attribute mappings](/dynamics365/customer-engagement/developer/customize-entity-attribute-mappings)<br />
[Developer Documentation: Web API Create a new entity from another entity](/dynamics365/customer-engagement/developer/webapi/create-entity-web-api#create-a-new-entity-from-another-entity)
