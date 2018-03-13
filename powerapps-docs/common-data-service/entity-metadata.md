---
title: Entity Metadata | Microsoft Docs
description: Learn about the entity metadata use in the Common Data Service for Apps.
services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: faisalmo
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/12/2018
ms.author: jdaly
---

# Entity Metadata

Each entity provides the capability to store structured data. For developers, entities represent the classes you will use when working with data in the Common Data Service.

## Entity names
Each entity has a unique name defined when it is created. This name is presented in several ways:

|Name Property |Description|
|---------|---------|
|`SchemaName`|Typically, a Pascal cased version of the logical name. i.e. Account|
|`CollectionSchemaName`|A plural form of the Schema name. i.e. Accounts|
|`LogicalName`|All lower-case version of the schema name. i.e. account|
|`LogicalCollectionName`|All lower-case version of the collection schema name. i.e. accounts|
|`EntitySetName`|Used to identify collections with the Web API. By default, it is the same as the logical collection name.<br />It is possible to change the Entity Set name by programmatically updating the metadata. But this should only be done before any Web API code is written for the entity. More information: [Dynamics 365 Customer Engagement Developer Guide: Web API types and operations > Change the name of an entity set](/dynamics365/customer-engagement/developer/webapi/web-api-types-operations#change-the-name-of-an-entity-set)|

> [!NOTE]
> When you create a custom entity, the name you choose will be prepended with the customization prefix value of the solution publisher associated with the solution that the entity was created within. Other than the entity set name, you cannot change the names of an entity after it is created.

Each entity also has three properties that can display localized values:


|Name  |Description  |
|---------|---------|
|`DisplayName`|Typically, the same as the schema name, but can include spaces. i.e. Account|
|`DisplayCollectionName`|A plural form of the Display name. i.e. Accounts|
|`Description`|A short sentence describing the entity i.e. *Business that represents a customer or potential customer. The company that is billed in business transactions.*|

These are the localizable values that are used to refer to the entities in an app. These values can be changed at any time. To add or edit localized values see  [Dynamics 365 Customization Guide: Translate customized entity and field text into other languages](/dynamics365/customer-engagement/customize/export-customized-entity-field-text-translation).


## Primary Key

The `PrimaryIdAttribute` property value is the logical name of the attribute that is the primary key for the entity.

By default, all entities have a single GUID unique identifier attribute. This is usually named *&lt; entity logical name &gt;*+ `Id`.

> [!NOTE]
> Although you can specify a GUID value when creating an entity record using the web services, it is recommended that you do not. Performance is enhanced when you let the common data service generate this value.

## Primary Name

The `PrimaryNameAttribute` property value is the logical name of the attribute that stores the string value that identifies the entity record. This is the value that will be displayed in a link to open the record in a UI.

**Example**: The Contact entity uses the `fullname` attribute as the primary name attribute.

> [!NOTE]
> Not every entity will have a primary name. Some entities are not intended to be displayed in a UI.

## Entity Images

The `PrimaryImageAttribute` property value is the logical name of the attribute that stores the image data for the entity record. Each entity can have only one image attribute and the logical name of that attribute is always `entityimage`.

**Example**: The Contact entity `entityimage` attribute can store a picture of the contact.

> [!NOTE]
> The icon displayed for an entity in model-driven apps is set using the `IconVectorName` property.

## Types of Entities

The capabilities and behavior of entities depends on several entity properties. Most of these properties are relatively simple and have descriptive names. Three that require some additional explanation are: *Ownership*, *Activity entities*, *Activityparty entity* and *Child entities*.

### Entity Ownership

Entities can be categorized by how the data within them is owned. This is an important concept related to how security is applied to entities. This information is in the OwnershipType property. The following table describes the different ownership types:

|Ownership Type  |Description  |
|---------|---------|
|Business|Data belongs to the Business unit. Access to the data can be controlled at the business unit level.|
|None|Data not owned by another entity.|
|Organization|Data belongs to the organization. Access to the data is controlled at the organization level.|
|User or Team|Data belongs to a user or a team. Actions that can be performed on these records can be controlled on a user level.|

When you create new entities, the only ownership options are: **Organization** or **User or Team**. Once you make a choice for this option, you cannot change it. Choose **User or Team** for the most granular control over who can view or perform actions on the records. Choose **Organization** when this level of control is not necessary. 

### Activity entities

An activity is a task performed, or to be performed, by a user. An activity is any action for which an entry can be made on a calendar. 

Activities are modeled differently from other kinds of entities that store business data. Data about activities is frequently displayed together in a list, yet each kind of activity requires unique properties. Rather than have a single Activity entity with every possible property, there are separate kinds of activity entities and each of them inherits properties from base `ActivityPointer` entity. These entities will have the `IsActivity` property set to true.


|Schema Name  |Description  |
|---------|---------|
|`Appointment`|Commitment representing a time interval with start/end times and duration.|
|`Email`|Activity that is delivered using email protocols.|
|`Fax`|Activity that tracks call outcome and number of pages for a fax and optionally stores an electronic copy of the document.|
|`Letter`|Activity that tracks the delivery of a letter. The activity can contain the electronic copy of the letter.|
|`PhoneCall`|Activity to track a telephone call.|
|`RecurringAppointmentMaster`|The Master appointment of a recurring appointment series.|
|`SocialActivity`|For internal use only.|
|`Task`|Generic activity representing work needed to be done.|
|`UntrackedEmail`|Activity that is delivered using UntrackedEmail protocols.|

Whenever you create one of these kinds of activity entities, a corresponding `ActivityPointer` entity record will be created with the same `ActivityId` unique identifier attribute value. You cannot create, update, or delete instances of the `ActivityPointer` entity, but you can retrieve them. This is what allows all types of activities to be presented together in a list.

You can create custom activity entities that behave the same way.

### ActivityParty entity

This entity is used to add structure to activity entity `PartyListType` attributes that include references to other entities. You will use this entity when setting values for activity entity attributes like `Email.to` or `PhoneCall.from`. Within the `ActivityParty` entity, you set the `ParticipationTypeMask` attribute to define the role that the reference is playing. Roles include `Sender`, `ToRecipient`, `Organizer` and more.

You can query the `ActivityParty` entity, but you cannot create, retrieve, update, or delete an activity party outside of the activity that it is related to.
More information: [Dynamics 365 Customer Engagement Developer Guide: ActivityParty entity](/dynamics365/customer-engagement/developer/activityparty-entity).


### Child entities

Entities where the `IsChildEntity` property is true will never have any privileges defined and will never be User or Team owned. Operations that can be performed on a child entity are bound to an entity that they are associated to via a Many-to-one relationship. Users can only perform operations on child entities if they can perform the same operation on the related entity. Child entities get deleted automatically when the entity record they depend on is deleted.

For example, `PostComment`, `PostLike`, and `PostRole` are each children of the `Post` entity.

## Entity Keys

Each alternate key definition describes one or more attributes in combination that will uniquely identify an entity instance. Alternate keys are typically only applied for integration with external systems. You can define alternate keys to uniquely identify a record. This is valuable if you are integrating data with a system that doesn’t support GUID unique identifier keys. You can define a single field value or combination of field values to uniquely identify an entity. Adding an alternate key will enforce a uniqueness constraint on these attributes. You will not be able to create or update another entity record to have the same values.

More information: 
 - [Dynamics 365 Customer Engagement Customization Guide: Define alternate keys to reference Dynamics 365 records](/dynamics365/customer-engagement/customize/define-alternate-keys-reference-records)
 - [Dynamics 365 Customer Engagement Developer Guide: Define alternate keys for an entity and Developer Guide: Synchronize Dynamics 365 data with external systems](/dynamics365/customer-engagement/developer/synchronize-dynamics-365-data-with-external-systems)

## Entity States

Most entities have two properties to track the state of a record. These are `StateCode`, which is called **Status** in model-driven apps and `StatusCode`, which is called **Status Reason** in model-driven apps. 

Both attributes contain a set of options that display the valid values. The `StateCode` and `StatusCode` attribute values are linked so that only certain `StatusCode` options are valid for a given `StateCode`.

This can vary by entity but the common pattern for many entities, and the default for custom entities is this:

|StateCode Options  |StatusCode Options  |
|---------|---------|
|0 : Active|1 : Active|
|1: Inactive|2: Inactive|

Some entities will have different sets of options. 

**Example**: `PhoneCall` entity `StateCode` and `StatusCode` options


|Column1  |Column2  |
|---------|---------|
|0 : Open|1: Open|
|1 : Completed|2: Made <br />4: Received|
|2: Cancelled|3: Cancelled|

The set of valid state codes for an entity is not customizable, but the status codes are customizable. You can add additional `StatusCode` options for a corresponding `StateCode`.

For custom entities, you can define additional criteria for valid transitions between statuses. 
More information: 
- [Dynamics 365 Customer Engagement Developer Guide: Customize entity attribute metadata](/dynamics365/customer-engagement/developer/customize-entity-attribute-metadata)
- [Dynamics 365 Customer Engagement Developer Guide: Define custom state model transitions](/dynamics365/customer-engagement/developer/define-custom-state-model-transitions).

