---
title: Work with Table Definitions in Microsoft Dataverse
description: Learn how to programmatically work with table definitions in Microsoft Dataverse, including table names, keys, ownership, activity tables, and states.
author: MsSQLGirl
ms.author: jukoesma
ms.topic: article
ms.date: 10/27/2026
ms.subservice: dataverse-developer
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors:
 - JimDaly
---

# Table definitions in Microsoft Dataverse

Table definitions in Microsoft Dataverse describe the structure and behavior of each table that stores structured data. This article explains how to work with table definitions programmatically, including table names, keys, ownership, and states. For developers, tables correspond to the classes you use when working with data in Microsoft Dataverse.

The SDK for .NET [EntityMetadata class](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata) and the Web API [EntityMetadata entity type](xref:Microsoft.Dynamics.CRM.EntityMetadata) contain the properties that define tables. 

> [!NOTE]
> When you retrieve table definitions using Web API, data in the response uses the [ComplexEntityMetadata complex type](xref:Microsoft.Dynamics.CRM.ComplexEntityMetadata). The difference is that the `Attributes`, `Keys`, `ManyToManyRelationships`, `ManyToOneRelationships`, and `OneToManyRelationships` are collections (arrays) rather than collection valued navigation properties. Use [EntityMetadata entity type](xref:Microsoft.Dynamics.CRM.EntityMetadata) when creating or updating tables using Web API.

## Table names

Each table has a unique name that you define when you create it. You see this name in several ways:

|Name Property |Description|Example|
|---------|---------|---------|
|`SchemaName`|Typically, a Pascal-cased version of the logical name.|`Account`|
|`CollectionSchemaName`|A plural form of the Schema name.|`Accounts`|
|`LogicalName`|All lower-case version of the schema name.|`account`|
|`LogicalCollectionName`|All lower-case version of the collection schema name.|`accounts`|
|`EntitySetName`|Used to identify collections with the Web API. By default, it's the same as the logical collection name.<br />You can change the entity set name by programmatically updating the table definition. Only make this change before writing any Web API code for the table. For more information, see [Entity set name](webapi/web-api-service-documents.md#entity-set-name).|`accounts`|


> [!NOTE]
> When you create a custom table with code you must prepend the [solution publisher](/power-platform/alm/solution-concepts-alm#solution-publisher) customization prefix to the `SchemaName`.  Dataverse doesn't verify that it's the correct customization prefix - only that it has a customization prefix. Ensure you use the correct prefix because you can't change it later.  
>
>`CollectionSchemaName`, `LogicalName`, `LogicalCollectionName`, and `EntitySetName` values are generated using the `SchemaName` value.

Each table also has three properties that can display localized values:

|Name  |Description  |Example|
|---------|---------|---------|
|`DisplayName`|Typically, the same as the schema name, but can include spaces.|**Account**|
|`DisplayCollectionName`|A plural form of the display name.|**Accounts**|
|`Description`|A short sentence describing the table.|**Business that represents a customer or potential customer. The company that is billed in business transactions.**|

Use these localizable values to refer to the tables in an app. You can change these values at any time. To add or edit localized values, see [Translate customized table, form, and column text into other languages](../../maker/data-platform/export-customized-entity-field-text-translation.md).


## Primary key

The `PrimaryIdAttribute` property value is the logical name of the column that serves as the primary key for the table.

By default, all tables include a single GUID unique identifier column named `<table logical name>Id`.

## Primary name

The `PrimaryNameAttribute` property value is the logical name of the column that stores the string value identifying the table record. This value appears in links that opens the record in a UI.

**Example**: The [Contact table](reference/entities/contact.md) uses the [FullName](reference/entities/contact.md#BKMK_FullName) column as the primary name column.

> [!NOTE]
> Not every table has a `PrimaryNameAttribute` property value. Some tables aren't intended to be displayed in a UI.

## Table images

The `PrimaryImageAttribute` property value is the logical name of the image column that you choose to represent the entity record. An application can display this image.

**Example**: The [Contact table](reference/entities/contact.md) [EntityImage](reference/entities/contact.md#BKMK_EntityImage) column can store a picture of the contact.

> [!NOTE]
> This image is different from the icon that model-driven apps display for a table. The `IconVectorName` property contains the name of the SVG web resource that sets the icon.

For more information, see:

- [Work with image column definitions using code](image-attributes.md)
- [Use image column data](image-column-data.md)
- [Sample: Image Operations using Dataverse SDK for .NET](org-service/samples/set-retrieve-entity-images.md)
- [Sample: Image Operations using Dataverse Web API](webapi/samples/image-operations.md)

## Types of tables

The capabilities and behavior of tables depend on several table properties. Most of these properties are relatively simple and have descriptive names. Four properties that require some more explanation are: [*Table ownership*](#table-ownership), [*Activity tables*](#activity-tables), [*Activityparty table*](#activityparty-table), and [*Child tables*](#child-tables).

### Table ownership

You can categorize tables by how the data within them is owned. This concept is important for understanding how to apply security to tables. The `OwnershipType` property holds this information. The following table describes the different ownership types:

|Ownership Type  |Description  |
|---------|---------|
|`BusinessOwned`|Data belongs to the business unit. You can control access to the data at the business unit level.|
|`None`|Data isn't owned by another table.|
|`OrganizationOwned`|Data belongs to the organization. You can control access to the data at the organization level.|
|`UserOwned`|Data belongs to a user or a team. You can control actions that can be performed on these records at the user level.|
|`Filtered` (preview)|Records have no owner. You can control access through security role privileges based on filters that evaluate column values.|


When you create new tables, the only ownership options are: `OrganizationOwned`, `UserOwned`, or `Filtered` (preview). You can't change this option after you make a choice. 

Choose `UserOwned` when records need user or team ownership, assignment, and sharing. Choose `OrganizationOwned` when organization-level access is sufficient. Choose `Filtered` (preview) when you need row-level access based on column values, with permissions granted through security role filters. Records in `Filtered` tables have no owner and can't be assigned or shared.

You can also apply record filters to `UserOwned` and `OrganizationOwned` tables to control row-level access based on column values without changing their `OwnershipType`. These tables retain their existing ownership model.

Learn more about filtered record ownership:

- [Filtered record ownership (preview)](../../maker/data-platform/filtered-view-record-ownership.md)
- [Filtered record ownership by using code (preview)](filtered-record-ownership.md)



### Activity tables

An activity is a task that a user performs or plans to perform. An activity is any action for which you can make an entry on a calendar. 

Activities are modeled differently from other kinds of tables that store business data. Data about activities is frequently displayed together in a list, yet each kind of activity requires unique properties. Instead of using a single Activity table with every possible property, use separate kinds of activity tables. 

Each of these tables inherits properties from a base [ActivityPointer table](reference/entities/activitypointer.md) (Web API [activitypointer entity type](xref:Microsoft.Dynamics.CRM.activitypointer)). These tables have the `IsActivity` property set to true.


|Table /<br />Entity type|Display name |Description  |
|---------|---------|---------|
|[adx_inviteredemption](reference/entities/adx_inviteredemption.md) /<br />[adx_inviteredemption](xref:Microsoft.Dynamics.CRM.adx_inviteredemption)|**Invite Redemption**|Holds information about the redemption of an invite.|
|[adx_portalcomment](reference/entities/adx_portalcomment.md) /<br />[adx_portalcomment](xref:Microsoft.Dynamics.CRM.adx_portalcomment)|**Portal Comment**|An activity which is used to share information between the user and the customer on the portal.|
|[Appointment](reference/entities/appointment.md) /<br />[appointment](xref:Microsoft.Dynamics.CRM.appointment)|**Appointment**|Commitment representing a time interval with start/end times and duration.|
|[chat](reference/entities/chat.md) /<br />[chat](xref:Microsoft.Dynamics.CRM.chat)|**Teams chat**|For internal use only. Entity which stores association data of Dynamics 365 records with Microsoft Teams chat.|
|[Email](reference/entities/email.md) /<br />[email](xref:Microsoft.Dynamics.CRM.email)|**Email**|Activity that is delivered using email protocols.|
|[Fax](reference/entities/fax.md) /<br />[fax](xref:Microsoft.Dynamics.CRM.fax)|**Fax**|Activity that tracks call outcome and number of pages for a fax and optionally stores an electronic copy of the document.|
|[Letter](reference/entities/letter.md) /<br />[letter](xref:Microsoft.Dynamics.CRM.letter)|**Letter**|Activity that tracks the delivery of a letter. The activity can contain the electronic copy of the letter.|
|[PhoneCall](reference/entities/phonecall.md) /<br />[phonecall](xref:Microsoft.Dynamics.CRM.phonecall)|**Phone Call**|Activity to track a telephone call.|
|[RecurringAppointmentMaster](reference/entities/recurringappointmentmaster.md) /<br />[recurringappointmentmaster](xref:Microsoft.Dynamics.CRM.recurringappointmentmaster)|**Recurring Appointment**|The Master appointment of a recurring appointment series.|
|[SocialActivity](reference/entities/socialactivity.md) /<br />[socialactivity](xref:Microsoft.Dynamics.CRM.socialactivity)|**Social Activity**|For internal use only.|
|[Task](reference/entities/task.md) /<br />[task](xref:Microsoft.Dynamics.CRM.task)|**Task**|Generic activity representing work needed to be done.|

When a user creates one of these kinds of activity table records, the system creates a corresponding `ActivityPointer` table record with the same `ActivityId` unique identifier column value. You can't create, update, or delete instances of the `ActivityPointer` table, but you can retrieve them. This design enables you to present all types of activities together in a list.

[You can create custom activity tables that behave the same way](custom-activities.md).

### ActivityParty table

Use the [ActivityParty table](reference/entities/activityparty.md) (Web API [activityparty entity type](xref:Microsoft.Dynamics.CRM.activityparty)) to add structure to the activity table `PartyListType` columns that include references to other tables. Use this table when setting values for activity table columns like `Email.to` or `PhoneCall.from`. Set the `participationtypemask` column to define the role that the reference plays. Roles include `Sender`, `ToRecipient`, `Organizer`, and more.

You can query the `ActivityParty` table, but you can't create, retrieve, update, or delete an activity party outside of the activity that it's related to.

### Child tables

Tables where the `IsChildEntity` property is true never have any privileges defined and are never User or Team owned. Operations that you can perform on a child table are bound to a table that they're associated to via a many-to-one relationship. Users can only perform operations on child tables if they can perform the same operation on the related table. Child tables get deleted automatically when the table record they depend on is deleted.

For example, [Comment (PostComment)](reference/entities/postcomment.md), and [Like (PostLike)](reference/entities/postlike.md) are children of the [Post](reference/entities/post.md) table.

## Alternate keys

Each alternate key definition describes one or more columns in combination that uniquely identify a record. Typically, you apply alternate keys only for integration with external systems. This feature is valuable if you're integrating data with a system that doesn't support GUID unique identifier keys. You can define a single column value or combination of column values to uniquely identify a table. Adding an alternate key enforces a uniqueness constraint on these columns. You can't create or update another record in the same table to have the same values.

For more information, see: 
 - [Define alternate keys to reference rows](../../maker/data-platform/define-alternate-keys-reference-records.md)
 - [Alternate Keys](data-synchronization.md#alternate-keys)

## Table states

Most tables have two properties to track the state of a record. These properties are `StateCode`, which appears as **Status** in model-driven apps, and `StatusCode`, which appears as **Status Reason** in model-driven apps. 

Both properties contain a set of choices that display the valid values. The `StateCode` and `StatusCode` values are linked so that only certain `StatusCode` choices are valid for a given `StateCode`.

This link can vary by table, but the common pattern for many tables, and the default for custom tables, is this pattern:

|StateCode Choices  |StatusCode Choices  |
|---------|---------|
|0: Active|1: Active|
|1: Inactive|2: Inactive|

Some tables have different sets of choices. 

**Example**: `PhoneCall` table `StateCode` and `StatusCode` choices


|StateCode|StatusCode|
|---------|---------|
|0: Open|1: Open|
|1: Completed|2: Made <br />4: Received|
|2: Canceled|3: Canceled|

You can't customize the set of valid state codes for a table, but you can customize the status codes. You can add more `StatusCode` choices for a corresponding `StateCode`.

For custom tables, you can define more criteria for valid transitions between statuses.

For more information, see:

- [Column definitions](entity-attribute-metadata.md)
- [Define custom state model transitions](define-custom-state-model-transitions.md).

### See also

[Dataverse tables](entities.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
