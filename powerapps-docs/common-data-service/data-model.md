---
title: Common Data Service for Apps Data Model | Microsoft Docs
description: Learn about the data model for the Common Data Service for Apps.
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
ms.date: 02/20/2018
ms.author: jdaly
---
# Common Data Service for Apps Data Model

Providing storage for data is the most important function of the Common Data Service for apps. The common data service includes a set of entities that provide a data model for business applications. 
<!-- You can view the base set of entities in the <link>Common Data Service for Apps Entity Reference</link>. -->

## Modify the data model

You can modify the entity metadata using several different methods.

### Use Designers

There are several ways to edit entity metadata using designers.


|Designer  |Description  |
|---------|---------|
|powerapps.com|The easiest and most common approach to modify the schema is to use the [powerapps.com](https://web.powerapps.com/) site to edit the common data service associated with an environment. Changes applied here are performed in the context of an unmanaged Common Data Service Default solution. <br /> More Information: TODO|
|Common Data Service Default solution explorer|There is another designer available from the [powerapps.com](https://web.powerapps.com/) site when editing the common data service. In the lower left-hand corner, the **Advanced** button will open the solution explorer to the Common Data Service Default solution. |
|Solution explorer for your solution |If you will distribute a solution you should create any new entities, attributes, or relationships in the context of the unmanaged solution that you will use to develop your solution. <br /> More information: [Create a solution publisher and solution](introduction-solutions.md#create-a-solution-publisher-and-solution)|
|From the form editor|When editing a model-driven app form for an entity, you can click the **New Field** button in the **Field Explorer**.|

### Import a solution

A solution can contain entity metadata as well as other customized components. Importing a managed or unmanaged solution into your common data service tenant will include those entities or extend existing entities with the new entity metadata they contain.

### Use Metadata services

The web services exposed in Common Data Service include capabilities to create, read, write, and delete entity metadata. These services are most frequently used to read the metadata because that data can inform your code at runtime about how the environment has been customized.

More information: [Metadata Services](use-web-services.md#metadata-services)

## Entity Metadata

The data model is defined as metadata that is stored within the common data service. This data about the schema is known as *Entity Metadata*. 

- The [EntityMetadata Class](/dotnet/api/microsoft.xrm.sdk.metadata.entitymetadata) defines this with the Organization service. 
- The [EntityMetadata EntityType](/dynamics365/customer-engagement/web-api/entitymetadata) defines this for the Web API. 

The Entity metadata includes the following information:


|Data  |Description  |
|---------|---------|
|Entity Properties|Each entity has nearly 100 properties that describe how it is identified and what can be done with it.  More information: [Entities](#entities)|
|Attributes|The entity Attributes property is a collection of attributes. Each attribute has around 50 properties to describe how it is identified, the type of data it contains, how it is formatted, and what can be done with it. More information: [Attributes](#attributes)|
|Relationships|Three of the entity properties are collections of relationships between entities. These collections contain different types of relationships: Many-To-Many, Many-To-One, and One-To-Many. More information: [Relationships](#relationships)|
|Privileges|One of the entity properties is a collection of between 0 and 8 privileges that identity the kinds of data operations that can be performed on that entity with a unique identifier associated with each one. These operations include: *Append*, *AppendTo*, *Assign*, *Create*, *Delete*, *Read*, *Share*, and *Write*.|
|Keys|By default, each entity has a single GUID unique identifier attribute and the Keys property is an empty collection. You can add alternate keys to an entity. 
More information: [Entity Keys](#entity-keys)|

> [!TIP]
> Developing an understanding of the entity metadata in the system can help you understand how the common data service works. Many of the properties also control what entities in model-driven apps can do. The designers available to edit metadata cannot show all the details found in the metadata. You can install a model app called the Metadata Browser which will allow you to view all the hidden entities and metadata properties that are found in the system. More information: [Dynamics 365 Developer Guide: Browse the metadata for your organization](/dynamics365/customer-engagement/developer/browse-your-metadata)


## Entities

Each entity provides the capability to store structured data. For developers, entities represent the classes you will use when working with data in the Common Data Service.

### Entity names
Each entity has a unique name defined when it is created. This name is presented in several ways:

|Name Property |Description|
|---------|---------|
|`SchemaName`|Typically, a Pascal cased version of the logical name. i.e. Account|
|`CollectionSchemaName`|A plural form of the Schema name. i.e. Accounts|
|`LogicalName`|All lower-case version of the schema name. i.e. account|
|`LogicalCollectionName`|All lower-case version of the collection schema name. i.e. accounts|
|`EntitySetName`|Used to identify collections with the Web API. By default, it is the same as the logical collection name.<br />It is possible to change the Entity Set name by programmatically updating the metadata. But this should only be done before any Web API code is written for the entity. More information: [Dynamics 365 Developer Guide: Web API types and operations > Change the name of an entity set](/dynamics365/customer-engagement/developer/webapi/web-api-types-operations#change-the-name-of-an-entity-set)|

> [!NOTE]
> When you create a custom entity, the name you choose will be prepended with the customization prefix value of the solution publisher associated with the solution that the entity was created within. Other than the entity set name, you cannot change the names of an entity after it is created.

Each entity also has three properties that can display localized values:


|Name  |Description  |
|---------|---------|
|`DisplayName`|Typically, the same as the schema name, but can include spaces. i.e. Account|
|`DisplayCollectionName`|A plural form of the Display name. i.e. Accounts|
|`Description`|A short sentence describing the entity i.e. *Business that represents a customer or potential customer. The company that is billed in business transactions.*|

These are the localizable values that are used to refer to the entities in an app. These values can be changed at any time. To add or edit localized values see  [Dynamics 365 Customization Guide: Translate customized entity and field text into other languages](/dynamics365/customer-engagement/customize/export-customized-entity-field-text-translation).


### Primary Key

The `PrimaryIdAttribute` property value is the logical name of the attribute that is the primary key for the entity.

By default, all entities have a single GUID unique identifier attribute. This is usually named *&lt; entity logical name &gt;*+ `Id`.

> [!NOTE]
> Although you can specify a GUID value when creating an entity record using the web services, it is recommended that you do not. Performance is enhanced when you let the common data service generate this value.

### Primary Name

The `PrimaryNameAttribute` property value is the logical name of the attribute that stores the string value that identifies the entity record. This is the value that will be displayed in a link to open the record in a UI.

**Example**: The Contact entity uses the `fullname` attribute as the primary name attribute.

> [!NOTE]
> Not every entity will have a primary name. Some entities are not intended to be displayed in a UI.

### Entity Images

The `PrimaryImageAttribute` property value is the logical name of the attribute that stores the image data for the entity record. Each entity can have only one image attribute and the logical name of that attribute is always `entityimage`.

**Example**: The Contact entity `entityimage` attribute can store a picture of the contact.

> [!NOTE]
> The icon displayed for an entity in model-driven apps is set using the `IconVectorName` property.

### Types of Entities

The capabilities and behavior of entities depends on several entity properties. Most of these properties are relatively simple and have descriptive names. Three that require some additional explanation are: *Ownership*, *Activity entities*, *Activityparty entity* and *Child entities*.

#### Entity Ownership

Entities can be categorized by how the data within them is owned. This is an important concept related to how security is applied to entities. This information is in the OwnershipType property. The following table describes the different ownership types:

|Ownership Type  |Description  |
|---------|---------|
|Business|Data belongs to the Business unit. Access to the data can be controlled at the business unit level.|
|None|Data not owned by another entity.|
|Organization|Data belongs to the organization. Access to the data is controlled at the organization level.|
|User or Team|Data belongs to a user or a team. Actions that can be performed on these records can be controlled on a user level.|

When you create new entities, the only ownership options are: **Organization** or **User or Team**. Once you make a choice for this option, you cannot change it. Choose **User or Team** for the most granular control over who can view or perform actions on the records. Choose **Organization** when this level of control is not necessary. 

#### Activity entities

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

#### ActivityParty entity

This entity is used to add structure to activity entity `PartyListType` attributes that include references to other entities. You will use this entity when setting values for activity entity attributes like `Email.to` or `PhoneCall.from`. Within the `ActivityParty` entity, you set the `ParticipationTypeMask` attribute to define the role that the reference is playing. Roles include `Sender`, `ToRecipient`, `Organizer` and more.

You can query the `ActivityParty` entity, but you cannot create, retrieve, update, or delete an activity party outside of the activity that it is related to.
More information: [Dynamics 365 Developer Guide: ActivityParty entity](/dynamics365/customer-engagement/developer/activityparty-entity).


#### Child entities

Entities where the `IsChildEntity` property is true will never have any privileges defined and will never be User or Team owned. Operations that can be performed on a child entity are bound to an entity that they are associated to via a Many-to-one relationship. Users can only perform operations on child entities if they can perform the same operation on the related entity. Child entities get deleted automatically when the entity record they depend on is deleted.

For example, `PostComment`, `PostLike`, and `PostRole` are each children of the `Post` entity.

### Entity Keys

Each alternate key definition describes one or more attributes in combination that will uniquely identify an entity instance. Alternate keys are typically only applied for integration with external systems. You can define alternate keys to uniquely identify a record. This is valuable if you are integrating data with a system that doesn’t support GUID unique identifier keys. You can define a single field value or combination of field values to uniquely identify an entity. Adding an alternate key will enforce a uniqueness constraint on these attributes. You will not be able to create or update another entity record to have the same values.

More information: 
 - [Dynamics 365 Customization Guide: Define alternate keys to reference Dynamics 365 records](/dynamics365/customer-engagement/customize/define-alternate-keys-reference-records)
 - [Dynamics 365 Developer Guide: Define alternate keys for an entity and Developer Guide: Synchronize Dynamics 365 data with external systems](/dynamics365/customer-engagement/developer/synchronize-dynamics-365-data-with-external-systems)

### Entity States

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
- [Dynamics 365 Developer Guide: Customize entity attribute metadata](/dynamics365/customer-engagement/developer/customize-entity-attribute-metadata)
- [Dynamics 365 Developer Guide: Define custom state model transitions](/dynamics365/customer-engagement/developer/define-custom-state-model-transitions).

## Attributes

Entities include a collection of attributes that represent the data that can be included within each record. Developers need to understand the different types of attributes and how to work with them. 

More information: [Dynamics 365 Developer Guide: Introduction to entity attributes](/dynamics365/customer-engagement/developer/introduction-entity-attributes)

### Attribute Names

Like entities, each attribute has a unique name defined when it is created. This name is presented in several ways:


|Name |Description  |
|---------|---------|
|SchemaName|Typically, a Pascal cased version of the logical name. i.e. `AccountNumber`|
|LogicalName|All lower-case name. i.e.  `accountnumber`|

When you create a custom attribute, the name you choose will be prepended with the customization prefix value of the solution publisher associated with the solution that the attribute was created within.

You cannot change the names of an attribute after it is created.

Each attribute also has two properties that can display localized values. These are the values that are used to refer to the attributes in an app.

|Name |Description  |
|---------|---------|
|`DisplayName`|Typically, the same as the schema name, but can include spaces. i.e. **Account Number**|
|`Description`|A short sentence describing the attribute or providing guidance to the user. i.e. *Type an ID number or code for the account to quickly search and identify the account in system views.*<br />
In model-driven apps, this information will appear when users hover over the field for this attribute in a form.|


These are the localizable values that are used to refer to the attributes in an app. These values can be changed at any time. To add or edit localized values see  [Dynamics 365 Customization Guide: Translate customized entity and field text into other languages](/dynamics365/customer-engagement/customize/export-customized-entity-field-text-translation).

### Attribute Types

The `AttributeTypeName` property describes the type of an attribute. This property contains a value of type `AttributeTypeDisplayName` which provides a label for each the different types of attributes that exist. 

In the following table:

- These types are grouped by category for comparison.
- For each `AttributeTypeDisplayName` value, the corresponding .NET assembly AttributeMetadata derived class is included where available. There is not a 1:1 relationship between these types and the `AttributeTypeDisplayName` label.
- Those attribute types that can be created as custom attributes include the corresponding label displayed in the UI.


|Category  |AttributeTypeDisplayName / <br />AttributeMetadata Type  |Can Create / <br /> Label  |Description  |
|---------|---------|---------|---------|
|Categorization|`BooleanType`<br />[BooleanAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.booleanattributemetadata)|Yes<br />**Two Options**|Contains the selected option value from two options that usually indicate a true or false value.<br />More information: [Option Sets](#option-sets)|
|Categorization|`EntityNameType`<br />[EntityNameAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.entitynameattributemetadata)|No|Contains an option value that corresponds to an entity in the system. For internal use only.|
|Categorization|`MultiSelectPicklistType`<br />[MultiSelectPicklistAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.multiselectpicklistattributemetadata)|Yes<br />**MultiSelect Option Set**|Contains multiple selected option values where multiple options can be selected.<br />More information: <br />[Option Sets](#option-sets)<br />[Dynamics 365 Developer Guide: Multi-Select Picklist attributes](/dynamics365/customer-engagement/developer/multi-select-picklist)|
|Categorization|`PicklistType`<br />[PicklistAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.picklistattributemetadata)|Yes<br />**Option Set**|Contains the selected option value where one option can be selected.<br />More information: [Option Sets](#option-sets)|
|Categorization|`StateType`<br />[StateAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.stateattributemetadata)|No|Contains the option value that describes the status of an entity record.<br />More information: [Option Sets](#option-sets)|
|Categorization|`StatusType`<br />[StatusAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.statusattributemetadata)|No|Contains the option value that describes the reason for the status of an entity record.<br />More information: [Option Sets](#option-sets)|
|Collection|`CalendarRulesType`|No|Contains a collection of `CalendarRules` entity records.<br />There are no attributes that use this type. When generating a proxy, the code generation tool will create two simulated attributes that are not present in the metadata. These attributes represent a view of the calendar rules records associated in a one-to-many relationship to the entity record.|
|Collection|`PartyListType`|No|Contains a collection of `ActivityParty` entity records.<br />More information: [ActivityParty entity](#activityparty-entity)|
|Date and Time|`DateTimeType`<br />[DateTimeAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.datetimeattributemetadata)|Yes<br />**Date and Time**|Contains a date and time value.<br />All date and time attributes support values as early as 1/1/1753 12:00 AM.|
|Image|`ImageType`<br />[ImageAttributeMetadata]()|Yes<br />**Image**|Contains data to support retrieving image data for an entity record. There are three additional attributes that support working with this data.<br />More information: [Dynamics 365 Developer Guide: Image attributes](/dynamics365/customer-engagement/developer/image-attributes)|
|Managed Property|`ManagedPropertyType`<br />[ManagedPropertyAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.imageattributemetadata)|No|Contains data that describe whether the solution component stored in the entity record can be customized when included in a managed solution.<br />More information: [Managed Properties](introduction-solutions.md#managed-properties)|
|Quantity|`BigIntType`<br />[BigIntAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.bigintattributemetadata)|No|Contains a `BigInt` value. For internal use only.|
|Quantity|`DecimalType`<br />[DecimalAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.decimalattributemetadata)|Yes<br />**Decimal Number**|Contains a `Decimal` value. The `Precision` property sets the level of precision.|
|Quantity|`DoubleType`<br />[DoubleAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.doubleattributemetadata)|Yes<br />**Floating Point Number**|Contains a `Double` value. The `Precision` property sets the level of precision.|
|Quantity|`IntegerType`<br />[IntegerAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.integerattributemetadata)|Yes<br />**Whole Number**|Contains an `Int` value|
|Quantity|`MoneyType`<br />[MoneyAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.moneyattributemetadata)|Yes<br />**Currency**|Contains a `Decimal` value. The `PrecisionSource` property determines where the level of precision is set.<br />0 : The `Precision` property<br />1 : The `Organization.PricingDecimalPrecision` attribute<br />2 : The `TransactionCurrency.CurrencyPrecision` attribute in the entity record|
|Reference|`CustomerType`<br />[LookupAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.lookupattributemetadata)|Yes<br />**Customer**|Contains a reference to either an account or contact entity record.|
|Reference|`LookupType`<br />[LookupAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.lookupattributemetadata)|Yes<br />**Lookup**|Contains a reference to an entity record. The logical names of the valid records are usually stored in the `Targets` property of the attribute.|
|Reference|`OwnerType`<br />[LookupAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.lookupattributemetadata)|No|Contains a reference to either a user or team entity record.|
|String|`MemoType`<br />[MemoAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.memoattributemetadata)|Yes<br />**Multiple Lines of Text**|Contains a string value intended to be displayed in a multi-line textbox.|
|String|`StringType`<br />[StringAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.stringattributemetadata)|Yes<br />**Single Line of Text**|Contains a string value intended to be displayed in a single-line textbox.|
|Unique identifier|`UniqueidentifierType`<br />[UniqueIdentifierAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.uniqueidentifierattributemetadata)|No|Contains a GUID unique identifier value.|
|Virtual|`VirtualType`|No|These attributes cannot be used in code and can generally be ignored.|


### Supported operations for attributes

Each attribute includes boolean properties that describe the kinds of operations it can participate in and how it is intended to be used in a form.

|Property|Description|
|--|--|
|`IsRequiredForForm`|The attribute must be included as a field in a form.|
|`IsValidForCreate`|The attribute value can be set in a create operation.|
|`IsValidForForm`|The attribute can be included as a field in a form.|
|`IsValidForRead`|The attribute value can be retrieved.|
|`IsValidForUpdate`|The attribute value can be set in an update operation.|

If you set a value in an update operation for an attribute that is not valid for update, the value will be ignored.

### Attribute Requirement level

The `RequiredLevel` property is a Boolean managed property that describes if an attribute value is required.

This property can have the following values set:

|Name|Value|UI Label|Description|
|--|--|--|--|
|`None`|0|**Optional**|No requirements are specified.|
|`SystemRequired`|1|**System Required**|The attribute is required to have a value.|
|`ApplicationRequired`|2|**Business Required**|The attribute is required by the business to have a value.|
|`Recommended`|3|**Business Recommended**|It is recommended that the attribute has a value.|

The Common Data Service only enforces the `SystemRequired` option for system entities. Custom attributes cannot be set to use the `SystemRequired` option. 

Model-driven apps will enforce the `ApplicationRequired` option and use a different presentation for the `Recommended` option. Creators of custom clients may use this information to require similar validation or presentation options.

Because this is a managed property, as a publisher of a managed solution you can decide whether consumers of your solution are able to change these settings on attributes in your solution.

More information: [Managed Properties](introduction-solutions.md#managed-properties)


### Rollup and Calculated attributes

Calculated and rollup attributes free the user from having to manually perform calculations and focus on their work. System administrators can define a field to contain the value of many common calculations without having to work with a developer. Developers can also leverage the platform capabilities to perform these calculations rather than within their own code.

More information: [Dynamics 365 Developer Guide: Calculated and rollup attributes](/dynamics365/customer-engagement/developer/calculated-rollup-attributes)

### Attribute Format

The format values for attributes controls how it is displayed in model-driven apps. Developer of custom apps may use this information to create similar experiences.

#### Integer Formats

Use the `Format` property with integer attributes to display alternate user experiences for this type.

|Option|Description|
|--|--|
|`None`|Displays a text box to edit a number value|
|`Duration`|Displays a drop-down list that contains time intervals. A user can select a value from the list or type an integer value that represents the number of minutes.|
|`TimeZone`|Displays a drop-down list that contains a list of time zones.|
|`Language`|Displays a drop-down list that contains a list of languages that have been enabled for the organization. If no other languages have been enabled, the base language will be the only option. The value saved is the LCID value for the language.|

#### String Formats

Use the `FormatName` property with string attributes to set values from the [StringFormatName Class](/dotnet/api/microsoft.xrm.sdk.metadata.stringformatname) to control how the string attribute is formatted.

|Name|Description|
|--|--|
|`Email`|The form field will validate the text value as an e-mail address and create a mailto link in the field.|
|`PhoneNumber`|The form field will contain a link to initiate a phone call by using Skype.|
|`PhoneticGuide`|For internal use only.|
|`Text`|The form will display a text box.|
|`TextArea`|The form will display a text area field.|
|`TickerSymbol`|The form will display a link that will open to display a quote for the stock ticker symbol.|
|`URL`|The form will display a link to open the URL.|
|`VersionNumber`|For internal use only.|

#### Date and Time Formats

The `DateTimeBehavior` property to controls the behavior for Date and Time attributes.
There are three options:

|Option|Short Description|
|--|--|
|`UserLocal`|Stores the date and time value as UTC value in the system.|
|`DateOnly`|Stores the actual date value with the time value as 12:00 AM (00:00:00) in the system.|
|`TimeZoneIndependent`|Stores the actual date and time values in the system regardless of the user time zone.|

Use the `Format` property control how the value is to be displayed in a model-driven app regardless of the `DateTimeBehavior`.

|Option|Description|
|--|--|
|DateAndTime|Display the full date and time|
|DateOnly|Display just the date.|

More information: [Dynamics 365 Developer Guide: Behavior and format of the date and time attribute](/dynamics365/customer-engagement/developer/behavior-format-date-time-attribute)

### AutoNumber attributes

You can add an auto-number attribute for any entity. Currently, you can add the attribute programmatically. There is no user interface to add this type of attribute.
More information: [Dynamics 365 Developer Guide: Create auto-number attributes](/dynamics365/customer-engagement/developer/create-auto-number-attributes)

### Option Sets

Those attributes which display a set of options can reference a set of options defined by the attribute or they can reference a separate set of options that can be shared by more than one attribute. This is particularly useful when values in one attribute also apply to other attributes. By referencing a common set of options, the options can be maintained in one place.

Each of these attribute inherit from [EnumAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.enumattributemetadata) and include an [OptionSet Property](/dotnet/api/microsoft.xrm.sdk.metadata.enumattributemetadata.optionset). This property contains the [OptionSetMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.optionsetmetadata) that includes the options within the [Options property](/dotnet/api/microsoft.xrm.sdk.metadata.optionsetmetadata.options). 

Retrieving available options with the Web API is a little different than using the organization service. More information: [Dynamics 365 Developer Guide: Query metadata using the Web API >Querying EntityMetadata attributes](/dynamics365/customer-engagement/developer/webapi/query-metadata-web-api#querying-entitymetadata-attributes)

More information: [Dynamics 365 Developer Guide : Customize global option sets](/dynamics365/customer-engagement/developer/org-service/customize-global-option-sets)

### Attribute Mapping

When you create a new entity record in the context of an existing entity record, you can automatically transfer certain values from the existing entity record as default values for the new entity record. This streamlines data entry for people using model-driven apps. Application users see the mapped values and can edit them before saving the entity.

For developers creating custom clients, the same behavior can be achieved by using the `InitializeFrom` message (Organization service  [InitializeFromRequest Class](/dotnet/api/microsoft.crm.sdk.messages.initializefromrequest) or Web API [InitializeFrom Function](/dynamics365/customer-engagement/web-api/initializefrom)) to get the entity data with the configured default values set.

More information 
- [Dynamics 365 Customization Guide: Map entity fields](/dynamics365/customer-engagement/customize/map-entity-fields#BKMK_mappingEntityFields)
- [Dynamics 365 Developer Guide Customize entity and attribute mappings](/dynamics365/customer-engagement/developer/customize-entity-attribute-mappings)

## Relationships

When you look at the solution explorer or the three relationship collections in the `EntityMetadata`, you might think that there are three types of entity relationships. Actually, there are only two, as shown in the following table.

|Relationship Type|Description|
|--|--|
|One-to-Many<br />[OneToManyRelationshipMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.onetomanyrelationshipmetadata)|An entity relationship where one entity record for the **Primary Entity** can be associated to many other **Related Entity** records because of a lookup field on the related entity.<br />When viewing a primary entity record you can see a list of the related entity records that are associated with it.|
|Many-to-Many<br />[ManyToManyRelationshipMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.manytomanyrelationshipmetadata)|An entity relationship that depends on a special *Relationship Entity*, sometimes called an *Intersect* entity, so that many records of one entity can be related to many records of another entity.<br />When viewing records of either entity in a Many-to-Many relationship you can see a list of any records of the other entity that are related to it.|

The `EntityMetadata` `ManyToOneRelationships` collection contains [OneToManyRelationshipMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.onetomanyrelationshipmetadata)types. One-to-Many relationships exist between entities and refer to each entity as either a *Primary Entity* or *Related Entity*. The related entity, sometimes called the *child entity*, has a lookup attribute that allows storing a reference to a record from the primary entity, sometimes called the *parent entity*. A Many-to-One relationship is just a One-to-Many relationship viewed from the related entity.

More information:
- [Dynamics 365 Customization Guide: Create and edit relationships between entities](/dynamics365/customer-engagement/customize/create-edit-entity-relationships)
- [Dynamics 365 Developer Guide: Customize entity relationship metadata](/dynamics365/customer-engagement/developer/customize-entity-relationship-metadata)

### Cascade Configuration

When a one-to-many entity relationship exists, there are cascading behaviors that can be configured to preserve data integrity and automate business processes.

More information:

- [Dynamics 365 Customization Guide: Create 1:N (one-to-many) or N:1 (many-to-one) relationships > Relationship behavior](/dynamics365/customer-engagement/customize/create-and-edit-1n-relationships#relationship-behavior)
- [Dynamics 365 Developer Guide: Entity relationship behavior](/dynamics365/customer-engagement/developer/entity-relationship-behavior)


### Create a Hierarchy of entities

Within a self-referential One-to-Many relationship you can set a hierarchy by setting the `IsHierarchical` property to `true`.

With model-driven apps, this enables an experience that enables you to view and interact with the hierarchy. 

For developers, this enables new types of queries based on the hierarchy using the `Under` and `Not Under` operators.

More information: [Dynamics 365 Developer Guide : Query and visualize hierarchically related data](/dynamics365/customer-engagement/customize/query-visualize-hierarchical-data)
