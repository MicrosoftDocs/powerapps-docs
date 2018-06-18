---
title: "Create and edit 1:N (one-to-many) or N:1 (many-to-one) entity relationships using solution explorer | MicrosoftDocs"
description: "Learn how to create one-to-many or many-to-one entity relationships using PowerApps solution explorer"
ms.custom: ""
ms.date: 05/27/2018
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
ms.author: "matp"
manager: "kvivek"
---

# Create and edit 1:N (one-to-many) or N:1 (many-to-one) entity relationships using solution explorer 

Solution explorer provides one way to create and edit 1:N (one-to-many) or N:1 (many-to-one) entity relationships for Common Data Service for Apps.

The [PowerApps portal](https://web.powerapps.com) enables configuring the most common options, but certain options can only be set using solution explorer. More information: 
- [Create 1:N (one-to-many) or N:1 (many-to-one) relationships](create-edit-1n-relationships.md)
- [Create and edit 1:N (one-to-many) or N:1 (many-to-one) entity relationships in PowerApps portal](create-edit-1n-relationships-portal.md)
  
## Open solution explorer

Part of the name of any custom relationship you create is the customization prefix. This is set based on the solution publisher for the solution you’re working in. If you care about the customization prefix, make sure that you are working in an unmanaged solution where the customization prefix is the one you want for this entity. More information: [Change the solution publisher prefix](change-solution-publisher-prefix.md) 

[!INCLUDE [cc_navigate-solution-from-powerapps-portal](../../../includes/cc_navigate-solution-from-powerapps-portal.md)]

## View entity relationships

In solution explorer, expand **Entities** an select an entity. Within that entity, select either **1:N Relationships** or **N:1 Relationships**

![View entity relationships](media/view-1n-entity-relationships-solution-explorer.png)

## Create relationships

While [viewing entity relationships](#view-entity-relationships), select either **New 1-to-Many Relationship** or **New Many-to-1 Relationship** from the command bar.

> [!NOTE]
> If the commands are not available, the entity is not eligible to create a custom relationship.

Either option will open a form like the following. The difference is whether the **Primary Entity** or **Related Entity** field is set.

![New one-to-many relationship form](media/new-1n-entity-relationship-form-solution-explorer.png)

- With **1:N Relationship**, the **Primary Entity** is set to the current entity
- With **N:1 Relationship**, the **Related Entity** is set to the current entity

The following fields must be set in order to save the entity relationship:

|Required Field|Description|
|--|--|
|**Primary Entity**|This entity will be the target type for the lookup field created on the related entity.|
|**Related Entity**|This entity will have a lookup field added to associate the entity records with the primary entity record.|
|**Name**|The name of the relationship. A value will be generated based on the primary and related entity values. This field will be prefixed by the customization prefix of the solution publisher.|
|**Lookup Field Display Name**|The localizable text for the lookup field that will be created for the related entity. This is usually the same as the display name for the primary entity. <br /> This can be changed later.|
|**Lookup Field Name**|The name of the lookup field that will be created on the related entity. A value will be generated based on the **Lookup Field Display Name**. This field will be prefixed by the customization prefix of the solution publisher.|

You can click ![Save entity relationship button](media/save-entity-icon-solution-explorer.png) to save the entity and continue editing. More information: [Edit relationships](#edit-relationships)

> [!NOTE]
> If either the **Name** or **Lookup Field Name** values already exist in the system you will get an error when you save. Edit the values so that they are unique and try again.

## Edit relationships

While [viewing entity relationships](#view-entity-relationships), select the entity you want to edit. The following entity relationship properties can be edited after the relationship is created.

> [!NOTE]
> The publisher of a managed solution can prevent some customizations of relationships that are part of their solution.

### Entity relationship properties

These properties are about the relationship.

|Field|Description|
|--|--|
|**Searchable**|Whether this relationship should be visible within Advanced Find in model-driven apps. Select **No** if this is a relationship that isn't important for your business.|
|**Hierarchical**|This option is enabled only for self-referential relationships. Whether the entity should be considered to define a hierarchy for the entity.<br />**Important**: Once you set this property rollup fields, processes, and views may be configured to depend on this property. If you later change this value those capabilities that depend on the hierarchy will not work. <br />More information: [Define and query hierarchically related data](define-query-hierarchical-data.md)|

### Lookup field

These are the properties of the lookup field created on the related entity. The properties can be edited here or by editing the lookup field directly. Some field properties are not editiable from the relationship. More information: [Edit a field](create-edit-field-solution-explorer.md#edit-a-field)

|Field|Description|
|--|--|
|**Display Name**|The localizable text for the lookup field that will be created for the related entity.|
|**Field requirement**|Whether the field must have data before a form in a model-driven app can be saved. More information: [Field Requirement options](create-edit-field-solution-explorer.md#field-requirement-options)|
|**Description**|Enter instructions to the user about what the field is for. These descriptions appear as tooltips for the user in model-driven apps when they hover their mouse over the label of the field.|

### Navigation Pane Item for Primary Entity

From the primary entity you can navigate to see related records. This data is used by model-driven apps to control how the related entity records are displayed. These settings can also be edited using the form editor.

|Field|Description|
|--|--|
|**Display Option**|How the related entity list should be displayed. More information: [Display Options](#display-options)|
|**Custom Label**|Specify the localizable text to be used instead of the plural name when you select **Use Custom Label** as the **Display Option** .|
|**Display Area**|Select one of the available groupings to display this list. The available options are: **Details** (for the *Common* group), **Marketing**, **Sales**, and **Service**. |
|**Display Order**|Controls where the navigation item will be included within the selected display area. The range of allowed numbers begins with 10,000. Navigation pane items with a lower value appear above other relationships with a higher value.|

<!-- TODO: Not sure whether Display Area or Display Order are still used anymore. Might only be used in the Outlook client?-->

#### Display Options

These are the available display options:

|Option|Description|
|--|--|
|**Do not Display**|Do not display the related entities for this relationship.|
|**Use Custom Label**|When this option is chosen, the **Custom Label** field is enabled so that you can specify the localizable text to be used instead of the plural name.|
|**Use Plural Name**|Use the plural display name defined for the related entity.|

### Relationship Behavior

This where you can define standard behaviors for related entities. This information is important because it helps ensure data integrity and can automate business processes for your company.

Let’s look at an example.  
  
Let’s say that you have a new salesperson and you want to assign them a number of existing opportunities currently assigned to another salesperson. Each opportunity record may have a number of task activities associated with it. You can easily locate the active opportunities you want to reassign and assign them to the new salesperson. But what should happen for any of the task activities that are associated with the opportunities? Do you want to open each task and decide whether they should also be assigned to the new salesperson? Probably not. Instead, you can let the relationship apply some standard rules for you automatically. These rules only apply to task records associated to the opportunities you are reassigning. Your options are:  
  
- Reassign all active tasks.  
- Reassign all tasks. 
- Reassign none of the tasks.  
- Reassign all tasks currently assigned to the former owner of the opportunity.  
  
The relationship can control how actions performed on a record for the primary entity record cascade down to any related entity records.   

There are several kinds of behaviors that can be applied when certain actions occur.

#### Behaviors

These are the behaviors available to be configured.

|Behavior|Description|
|--|--|
|**Cascade Active**|Perform the action on all active related entity records.|
|**Cascade All**|Perform the action on all related entity records.|
|**Cascade None**|Do nothing.|
|**Remove Link**|Remove the lookup value for all related records.|
|**Restrict**|Prevent the primary entity record from being deleted when related entity records exist.|
|**Cascade User Owned**|Perform the action on all related entity records owned by the same user as the primary entity record.|

#### Actions

These are the actions that can trigger certain behaviors:

|Field|Description|Options|
|--|--|--|
|**Assign**|What should happen when the primary entity record is assigned to someone else?|Cascade All<br />Cascade Active<br />Cascade User-owned<br />Cascade None|
|**Reparent**|What should happen when the lookup value of a related entity in a parental relationship is changed?<br />More information: [Parental entity relationships](#parental-entity-relationships)|Cascade All<br />Cascade Active<br />Cascade User-owned<br />Cascade None|
|**Share**|What should happen when the primary entity record is shared?|Cascade All<br />Cascade Active<br />Cascade User-owned<br />Cascade None|
|**Delete**|What should happend when the primary entity record is deleted?|Cascade All<br />Remove Link<br />Restrict|
|**Unshare**|What should happen when a primary entity record is unshared?|Cascade All<br />Cascade Active<br />Cascade User-owned<br />Cascade None|
|**Merge**|What should happen when a primary entity record is merged?|Cascade All<br />Cascade None|
|**Rollup View**|What is the desired behavior of the rollup view associated with this relationship? |Cascade All<br />Cascade Active<br />Cascade User-owned<br />Cascade None|

<!-- TODO: I find no official docs related to rollup views, but plenty of hits online: https://www.google.com/search?q=Dynamics+365++%27rollup+view%27 -->



#### Type of Behavior options

Use the **Type of Behavior** field to choose between a set of standard behaviors or whether you want to configure them independently. 

|Option|Description|
|--|--|
|**Parental**|**Assign**: Cascade All<br />**Reparent**: Cascade All<br />**Share**: Cascade All<br />**Delete**: Cascade All<br />**Unshare**: Cascade All<br />**Merge**: Cascade None<br />**Rollup View**: Cascade None \| Cascade All<br />|
|**Referential**|**Assign**: Cascade None<br />**Reparent**: Cascade None<br />**Share**: Cascade None<br />**Delete**: Remove Link<br />**Unshare**: Cascade None<br />**Merge**: Cascade None<br />**Rollup View**: Cascade None \| Cascade All<br />|
|**Referential, Restrict Delete**|**Assign**: Cascade None<br />**Reparent**: Cascade None<br />**Share**: Cascade None<br />**Delete**: Restrict<br />**Unshare**: Cascade None<br />**Merge**: Cascade None<br />**Rollup View**: Cascade None \| Cascade All<br />|
|**Configurable Cascading**|You can configure the behavior you want for each action depending on the options available|

> [!NOTE]
> You may not be able to choose the **Parental** option if either of the entities already participate in an parental entity relationship. More information: [Parental entity relationships](#parental-entity-relationships)
> 
> If you use **Configurable Cascading** to set the behaviors for the actions so that they match the behaviors for the actions associated with another **Type of Behavior**, when you save the relationship, the **Type of Behavior** is automatically set to the matching type.  



## Delete relationships

While [viewing entity relationships](#view-entity-relationships), select the entity relationship you want to delete and click the ![Delete command](media/delete.gif) command.

Deleteing the relationship will delete the lookup field on the related entity.

> [!NOTE]
> You will not be able to delete a relationship that has dependencies. For example, if you have added the lookup field to a form for the related entity, you must remove the field from the form before you delete the relationship.

## Parental entity relationships

Each pair of entities that are eligible to have a 1:N relationship can have multiple 1:N relationships between them. Yet usually only one of those relationships can be considered a parental entity relationship.

A parental entity relationship is any 1:N entity relationship where one of the cascading options in the **Parental** column of the following table is true.

|Action|Parental|Not Parental|  
|------------|--------------|------------------|  
|**Assign**|Cascade All<br />Cascade User-owned<br />Cascade Active|Cascade None|  
|**Delete**|Cascade All|RemoveLink<br />Restrict|  
|**Reparent**|Cascade All<br />Cascade User-owned<br />Cascade Active|Cascade None|  
|**Share**|Cascade All<br />Cascade User-owned<br />Cascade Active|Cascade None|  
|**Unshare**|Cascade All<br />Cascade User-owned<br />Cascade Active|Cascade None|  

For example, if you create a new custom entity and add a 1:N entity relationship with the account entity where your custom entity is the related entity, you can configure the actions for that entity relationship to use the options in the **Parental** column. If you later add another 1:N entity relationship with your custom entity as the referencing entity you can only configure the actions to use the options in the **Not Parental** column.

Usually this means that for each entity pair there is only one parental relationship. There are some cases where the lookup on the related entity may allow for a relationship to  to more than one type of entity.

For example, if an entity has a Customer lookup that can refer to either a contact or account entity. There are two separate parental 1:N entity relationships.

Any activity entity has a similar set of parental entity relationships for entities that can be associated using the regarding lookup field.

<a name="BKMK_RelationshipBehaviorLimitations"></a>   

### Limitations on behaviors you can set
  
Because of parental relationships there are some limitations you should keep in mind when you define entity relationships.  
  
- A custom entity can’t be the primary entity in a relationship with a related system entity that cascades. This means you can’t have a relationship with any action set to **Cascade All**, **Cascade Active**, or **Cascade User-Owned** between a primary custom entity and a related system entity.  
- No new relationship can have any action set to **Cascade All**, **Cascade Active**, or **Cascade User-Owned** if the related entity in that relationship already exists as a related entity in another relationship that has any action set to **Cascade All**, **Cascade Active**, or **Cascade User-Owned**. This prevents relationships that create a multi-parent relationship.  

### See also

[Create and edit relationships between entities](create-edit-entity-relationships.md)<br />
[Create and edit 1:N (one-to-many) or N:1 (many-to-one) relationships](create-edit-1n-relationships.md)<br />
[Create and edit 1:N (one-to-many) or N:1 (many-to-one) entity relationships in PowerApps portal](create-edit-1n-relationships-portal.md)<br />
[Create N:N (many-to-many) relationships](create-edit-nn-relationships.md)

