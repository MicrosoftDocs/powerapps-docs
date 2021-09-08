---
title: "About table relationships for Microsoft Dataverse | MicrosoftDocs"
description: Learn about table relationships in Microsoft Dataverse
ms.custom: intro-internal
ms.date: 08/17/2020
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "overview"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
ms.assetid: c765b6d9-4d87-4c2d-aae2-5b1c3b664a71
caps.latest.revision: 28
ms.subservice: dataverse-maker
ms.author: "matp"
manager: "kvivek"
author: "Mattp123"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---
# Table relationships 
[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

Table relationships define how rows can be related to each other in the database. At the simplest level, adding a lookup column to a table creates a new 1:N (one-to-many) relationship between the two tables and lets you put that lookup column in a form. With the lookup column, users can associate multiple *child* rows of that table to a single *parent* table row.  
  
Beyond simply defining how rows can be related to other rows, 1:N table relationships also provide data to address the following questions:  
  
- When I delete a row should any rows related to that row also be deleted?  
- When I assign a row, do I also need to assign all rows related to that row to the new owner?  
- How can I streamline the data entry process when I create a new related row in the context of an existing row?  
- How should people viewing a row be able to view the associated rows?  
  
 Tables can also participate in a N:N (many-to-many) relationship where any number of rows for two tables can be associated with each other.  

<a name="BKMK_Connections"></a>

## Decide whether to use table relationships or connections 
Table relationships are metadata that make changes to the database. These relationships allow for queries to retrieve related data very efficiently. Use table relationships to define formal relationships that define the table or that most rows can use. For example, an opportunity without a potential customer wouldn't be very useful. The Opportunity table also has a N:N relationship with the Competitor table. This allows for multiple competitors to be added to the opportunity. You may want to capture this data and create a report that shows the competitors.  
  
There are other less formal kinds of relationships between rows that are called *connections*. For example, it may be useful to know if two contacts are married, or perhaps they are friends outside of work, or perhaps a contact used to work for another account. Most businesses won't generate reports using this kind of information or require that it is entered, so it's probably not worthwhile to create table relationships. More information: [Configure connection roles](configure-connection-roles.md)

  
<a name="BKMK_TypesOfRelationships"></a>
 
## Types of table relationships
When you look at the solution explorer you might think that there are three types of table relationships. Actually there are only two, as shown in the following table.  
  
|Relationship Type|Description|  
|-----------------------|-----------------|  
|**1:N (One-to-Many)**|A table relationship where one table row for the **Primary table** can be associated to many other **Related table** rows because of a lookup column on the related table.<br /><br /> When viewing a primary table row you can see a list of the related table rows that are associated with it.<br /><br /> In the Power Apps portal, **Current table** represents the primary table.|  
|**N:N (Many-to-Many)**|A table relationship that depends on a special **Relationship table**, sometimes called an Intersect table, so that many rows of one table can be related to many rows of another table.<br /><br /> When viewing rows of either table in a N:N relationship you can see a list of any rows of the other table that are related to it.|  
  
The **N:1 (many-to-one)** relationship type exists in the user interface because the designer shows you a view grouped by tables. 1:N relationships actually exist *between* tables and refer to each table as either a **Primary/Current table** or **Related table**. The related table, sometimes called the *child* table, has a lookup column that allows storing a reference to a row from the primary table, sometimes called the *parent* table. A N:1 relationship is just a 1:N relationship viewed from the related table.  
 
## Table relationship behavior
Behaviors  for related tables is important because it helps ensure data integrity and can automate business processes for your company.

### Preserve data integrity
Some tables exist to support other tables. They don't make sense on their own. They will typically have a required lookup column to link to the primary table they support. What should happen when the primary row is deleted?

You can use the relationship behavior to define this according to the rules for your business. Two options are:

- Prevent deleting the primary table so that the related table rows can be reconciled, perhaps by associating them with a different primary table.
- Allow the related tables to be deleted automatically with the deletion of the primary table row.

If the related table doesn't support a primary table, you can allow the primary table to be deleted and the value of the lookup will be cleared.

### Automate business processes
Let's say that you have a new salesperson and you want to assign them a number of existing accounts currently assigned to another salesperson. Each account row may have a number of task activities associated with it. You can easily locate the active accounts you want to reassign and assign them to the new salesperson. But what should happen for any of the task activities that are associated with the accounts? Do you want to open each task and decide whether they should also be assigned to the new salesperson? Probably not. Instead, you can let the relationship apply some standard rules for you automatically. These rules only apply to task rows associated to the accounts you are reassigning. Your options are:  
  
- Reassign all active tasks.  
- Reassign all tasks. 
- Reassign none of the tasks.  
- Reassign all tasks currently assigned to the former owner of the accounts.  
  
The relationship can control how actions performed on a row for the primary table row cascade down to any related table rows.  

### Behaviors
There are several kinds of behaviors that can be applied when certain actions occur.

|Behavior|Description|
|--|--|
|**Cascade Active**|Perform the action on all active related table rows.|
|**Cascade All**|Perform the action on all related table rows.|
|**Cascade None**|Do nothing.|
|**Remove Link**|Remove the lookup value for all related rows.|
|**Restrict**|Prevent the primary table row from being deleted when related table rows exist.|
|**Cascade User Owned**|Perform the action on all related table rows owned by the same user as the primary table row.|

### Actions
These are the actions that can trigger certain behaviors:

|Column|Description|Options|
|--|--|--|
|**Assign**|What should happen when the primary table row is assigned to someone else?|Cascade All<br />Cascade Active<br />Cascade User-owned<br />Cascade None|
|**Reparent**|What should happen when the lookup value of a related table in a parental relationship is changed?<br />More information: [Parental table relationships](#parental-table-relationships)|Cascade All<br />Cascade Active<br />Cascade User-owned<br />Cascade None|
|**Share**|What should happen when the primary table row is shared?|Cascade All<br />Cascade Active<br />Cascade User-owned<br />Cascade None|
|**Delete**|What should happen when the primary table row is deleted?|Cascade All<br />Remove Link<br />Restrict|
|**Unshare**|What should happen when a primary table row is unshared?|Cascade All<br />Cascade Active<br />Cascade User-owned<br />Cascade None|
|**Merge**|What should happen when a primary table row is merged?|Cascade All<br />Cascade None|
|**Rollup View**|What is the desired behavior of the rollup view associated with this relationship? |Cascade All<br />Cascade Active<br />Cascade User-owned<br />Cascade None|

> [!NOTE]
> Assign, Delete, Merge, and Reparent actions will not execute in the following situations:
> - If the original parent row and requested action contain the same values. Example: Attempting to trigger an Assign and 
>   choosing a contact that is already the owner of the row
> - Attempting to perform an action on a parent row that is already running a cascading action

> [!NOTE]
> When executing an assign, any workflows or business rules that are currently active on the rows will automatically be 
> deactivated when the reassignment occurs. The new owner of the row will need to reactivate the workflow or business rule 
> if they want to continue using it.

### Parental table relationships
Each pair of tables that are eligible to have a 1:N relationship can have multiple 1:N relationships between them. Yet usually only one of those relationships can be considered a parental table relationship.

A parental table relationship is any 1:N table relationship where one of the cascading options in the **Parental** column of the following table is true.

|Action|Parental|Not Parental|  
|------------|--------------|------------------|  
|**Assign**|Cascade All<br />Cascade User-owned<br />Cascade Active|Cascade None|  
|**Delete**|Cascade All|RemoveLink<br />Restrict|  
|**Reparent**|Cascade All<br />Cascade User-owned<br />Cascade Active|Cascade None|  
|**Share**|Cascade All<br />Cascade User-owned<br />Cascade Active|Cascade None|  
|**Unshare**|Cascade All<br />Cascade User-owned<br />Cascade Active|Cascade None|  

For example, if you create a new custom table and add a 1:N table relationship with the account table where your custom table is the related table, you can configure the actions for that table relationship to use the options in the **Parental** column. If you later add another 1:N table relationship with your custom table as the referencing table you can only configure the actions to use the options in the **Not Parental** column.

Usually this means that for each table pair there is only one parental relationship. There are some cases where the lookup on the related table may allow for a relationship to more than one type of table.

For example, if a table has a Customer lookup that can refer to either a contact or account table. There are two separate parental 1:N table relationships.

Any activity table has a similar set of parental table relationships for tables that can be associated using the regarding lookup column.

<a name="BKMK_RelationshipBehaviorLimitations"></a>   

### Limitations on behaviors you can set
Because of parental relationships there are some limitations you should keep in mind when you define table relationships.  
  
- A custom table can't be the primary table in a relationship with a related system table that cascades. This means you can't have a relationship with any action set to **Cascade All**, **Cascade Active**, or **Cascade User-Owned** between a primary custom table and a related system table.  
- No new relationship can have any action set to **Cascade All**, **Cascade Active**, or **Cascade User-Owned** if the related table in that relationship already exists as a related table in another relationship that has any action set to **Cascade All**, **Cascade Active**, or **Cascade User-Owned**. This prevents relationships that create a multi-parent relationship.  

### Inherited access rights cleanup

Using Reparent and Share cascading behaviors are helpful when you want to provide access to rows across related tables. But there can be a change in process or design that requires a change of the cascading behavior settings.

When a table relationship uses Reparent or Share, and the cascading behavior is changed from **Cascade All** to **Cascade None**, the table relationship prevents any new permission changes from cascading to the related child tables. In addition, inherited permissions that were granted while the cascading behavior was active must be revoked.

Inherited access rights cleanup is a system job that cleans up the legacy inherited access rights that remain after the cascading behavior is changed from **Cascade All** to **Cascade None**. This cleanup will not affect any user that was directly granted access to a table, but will remove access from anyone who received access through inheritance only.

> [!NOTE]
> Currently, to run inherited access rights cleanup requires using the Web API. More information: [CreateAsyncJobToRevokeInheritedAccess Action](/dynamics365/customer-engagement/web-api/createasyncjobtorevokeinheritedaccess?view=dynamics-ce-odata-9&preserve-view=true)

<!-- Automatic triggering to come later-- remove above alert at that time. The cleanup is automatically triggered when you switch Reparent or Share cascading behaviors from All to None. No action is required. -->

This is how inherited access rights cleanup works:

1. Identifies and collects all the tables that were in a cascading relationship with the updated parent.

2. Identifies and collects the users that were granted access to the related tables through inherited access.

3. Checks for users who were given direct access to a related table and removes them from the collection.

4. Removes inherited access for the collected users on the collected tables.

After the cleanup runs, users who were able to access related tables only because of the cascading feature can no longer access the rows, ensuring greater security.


### See also
[Monitor and manage system jobs](/power-platform/admin/monitor-manage-system-jobs) <br />
[Create and edit 1:N (one-to-many) or N:1 (many-to-one) relationships](create-edit-1n-relationships.md)<br />
[Create Many-to-many (N:N) table relationships](create-edit-nn-relationships.md)



[!INCLUDE[footer-include](../../includes/footer-banner.md)]