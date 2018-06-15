---
title: "Entities and metadata in Common Data Service for Apps | MicrosoftDocs"
description: "Learn about entities and metadata in Common Data Service for Apps" 
ms.custom: ""
ms.date: 05/30/2018
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
ms.assetid: 88b18946-474c-4c94-8e4c-27532f930757
caps.latest.revision: 28
ms.author: "matp"
manager: "kvivek"
---

# Entities and metadata in Common Data Service for Apps

Common Data Service for Apps is designed so that you can quickly and easily create a data model for your application. Normally, you shouldn't have to concern yourself with some of the details about metadata that this topic will introduce. But if you want to develop a deeper understanding about how apps that use CDS for Apps work or you are evaluating what is possible, understanding the metadata used by CDS for Apps may provide you insight.

*Metadata* means data about data. CDS for Apps provides a flexible platform for you because it is relatively easy to edit the definitions of the data that the environment will use. In CDS for Apps, the metadata is a collection of entities. Entities describe the kinds of data which is stored in the database.  Each entity corresponds to a database table and each field (also known as attribute) within an entity represents a column in that table. Entity metadata is what controls the kinds of records you can create and what kind of actions can be performed on them. When you use the customization tools to create or edit entities, fields, and entity relationships, you are editing this metadata. 
  
Different clients people use to interact with the data in your environment depend on the entity metadata and adapt as you customize the metadata. But these clients also depend on other data to control what visual elements to display, any custom logic to apply, and how to apply security. This system data is also stored within entities but the entities themselves are not available for customization.

You can learn about standard entities, attributes, and entity relationships included by default in CDS for Apps by reviewing the [Entity Reference](/powerapps/developer/common-data-service/reference/about-entity-reference).

> [!TIP]
> The designers available to edit metadata cannot show all the details found in the metadata. You can install a model-driven app called the **Metadata Browser** which will allow you to view all the entities and metadata properties that are found in the system. More information: [Browse the metadata for your environment](../../developer/common-data-service/browse-your-metadata.md).
  
<a name="BKMK_CreateNewOrUseExistingMetadata"></a>

## Create new metadata or use existing metadata?

CDS for Apps comes with a number of standard entities that support core business application capabilities. For example, data about your customers or potential customers is intended to be stored using the account or contact entities.  
  
Each of these entities also contain a number of fields that represent common data that the system may need to store for the respective entity.  
  
For most organizations it is to your advantage to use the standard entities and attributes for the purposes they were provided. 
  
If you install a solution you can expect that the solution developer has leveraged the standard entities and attributes. Creating a new custom entity that replaces a system entity or attribute will mean that any solutions available may not work for your organization.  
  
For these reasons, we recommend that you look for and use the provided standard entities, fields, and entity relationships when they make sense for your organization. If they don’t make sense and can’t be edited to match your need, you should evaluate if creating a new entity, field, or entity relationships is required. 

<!--  Can we say this yet? 
    
> [!NOTE]
> The [Common Data Model](/powerapps/common-data-model/overview) will provide a capability to add additional standard entities. 

-->

Remember that you can change the display name of an entity so that it matches the nomenclature your organization uses. For example, it is very common for people to change the display name of the Account entity to *Company* or the name of the Contact entity to *Individual*. This can be done to entities or attributes without changing the behavior of the entity. For more information about renaming entities, see [Change the name of an entity](edit-entities.md#change-the-name-of-an-entity).
  
You can’t delete standard entities, fields, or entity relationships. They are considered part of the system solution and every organization is expected to have them. If you want to hide a standard entity, change the security role privileges for your organization to remove the read privilege for that entity. This will remove the entity from most parts of the application. If there is a system field that you don’t need, remove it from the form and any views that use it. Change the **Searchable** value in the field and entity relationship definitions so that they do not appear in advanced find. 
  
<a name="BKMK_LimitationsOnMetadata"></a>   

## Limitations on creating metadata items  

There is a limit to the number of entities you can create. You can find information about the maximum number in the **Settings** > **Administration** > **Resources In Use** page. If you need more custom entities, contact technical support. This upper limit can be adjusted.  
  
Within each entity there is an upper limit on the number of fields you can create. This limit is based on the technical limitations on the amount of data that can be stored in a row of a database table. It is difficult to provide a specific number because each type of field can use a different amount of space. The upper limit depends on the total space used by all the fields for the entity.  
  
Most people do not create enough custom fields to reach the limit, but if you find yourself planning to add hundreds of custom fields to an entity, you should consider if this is the best design. Do all the fields you plan to add describe properties for a record for that entity? Do you really expect that people using your organization will be able to manage a form that includes such a high number of fields? The number of fields you add to a form increase the amount of data that has to be transferred each time a record is edited and will affect the performance of the system. Take these factors into consideration when you are adding custom fields to an entity.  
  
Option set fields provide a set of options that will be displayed in a drop-down control on a form or in picklist control when using advanced find. Your environment can support thousands of options within an Option set, but you shouldn’t consider this as the upper limit. Usability studies have shown that people have trouble using a system where a drop-down control provides large numbers of options. Use option set field to define categories for data. Don’t use option set fields to select categories that actually represent separate items of data. For example, rather than maintain an option set field that stores each of hundreds of possible manufacturers of a type of equipment, consider creating an entity that stores references to each manufacturer and use a lookup field instead of an option set.  
  
### See also  

[Create or edit entities (record types)](create-edit-entities.md)<br />
[Create and edit virtual entities that contain data from an external data source](create-edit-virtual-entities.md)<br />
[Create and edit relationships between entities](create-edit-entity-relationships.md)<br />
[Create and edit fields for Common Data Service for Apps](create-edit-fields.md)<br />
[Create and edit global option sets for Common Data Service for Apps (picklists)](create-edit-global-option-sets.md)<br />
[Create and design forms](../model-driven-apps/create-design-forms.md)
