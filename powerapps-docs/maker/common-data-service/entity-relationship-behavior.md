---
title: "Entity relationship behavior (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "<Description>" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "Mattp123" # GitHub ID
ms.author: "matp" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
---
# Entity relationship behavior

Behaviors  for related entities is important because it helps ensure data integrity and can automate business processes for your company.

## Preserve data integrity

Some entities exist to support other entities. They don't make sense on their own. They will typically have a required lookup field to link to the primary entity they support. What should happen when the primary record is deleted?

You can use the relationship behavior to define this according to the rules for your business. Two options are:

- Prevent deleting the primary entity so that the related entity records can be reconciled, perhaps by associating them with a different primary entity.
- Allow the related entities to be deleted automatically with the deletion of the primary entity record.

If the related entity doesn't support a primary entity, you can allow the primary entity to be deleted and the value of the lookup will be cleared.

## Automate business processes
  
Let’s say that you have a new salesperson and you want to assign them a number of existing accounts currently assigned to another salesperson. Each account record may have a number of task activities associated with it. You can easily locate the active accounts you want to reassign and assign them to the new salesperson. But what should happen for any of the task activities that are associated with the accounts? Do you want to open each task and decide whether they should also be assigned to the new salesperson? Probably not. Instead, you can let the relationship apply some standard rules for you automatically. These rules only apply to task records associated to the accounts you are reassigning. Your options are:  
  
- Reassign all active tasks.  
- Reassign all tasks. 
- Reassign none of the tasks.  
- Reassign all tasks currently assigned to the former owner of the accounts.  
  
The relationship can control how actions performed on a record for the primary entity record cascade down to any related entity records.  

## Behaviors

There are several kinds of behaviors that can be applied when certain actions occur.

|Behavior|Description|
|--|--|
|**Cascade Active**|Perform the action on all active related entity records.|
|**Cascade All**|Perform the action on all related entity records.|
|**Cascade None**|Do nothing.|
|**Remove Link**|Remove the lookup value for all related records.|
|**Restrict**|Prevent the primary entity record from being deleted when related entity records exist.|
|**Cascade User Owned**|Perform the action on all related entity records owned by the same user as the primary entity record.|

## Actions

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

## Limitations on behaviors you can set
  
Because of parental relationships there are some limitations you should keep in mind when you define entity relationships.  
  
- A custom entity can’t be the primary entity in a relationship with a related system entity that cascades. This means you can’t have a relationship with any action set to **Cascade All**, **Cascade Active**, or **Cascade User-Owned** between a primary custom entity and a related system entity.  
- No new relationship can have any action set to **Cascade All**, **Cascade Active**, or **Cascade User-Owned** if the related entity in that relationship already exists as a related entity in another relationship that has any action set to **Cascade All**, **Cascade Active**, or **Cascade User-Owned**. This prevents relationships that create a multi-parent relationship.  
