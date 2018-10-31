---
title: "Entity Operations using the Organization service (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about the Entity class used for data operations using the CDS for Apps organization service" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Entity Operations using the Organization service

When you work with Common Data Service for Apps data using the organization service you will use the <xref:Microsoft.Xrm.Sdk.Entity> class with the late-bound style or with generated entity classes using the early-bound style. The generated entity classes inherit from the <xref:Microsoft.Xrm.Sdk.Entity> class, so understanding the <xref:Microsoft.Xrm.Sdk.Entity> class is important for either style.

This topic will describe some of the most frequently used properties and methods of the <xref:Microsoft.Xrm.Sdk.Entity> class.

## Entity.LogicalName

When you instantiate a new <xref:Microsoft.Xrm.Sdk.Entity> instance using the late-bound style you must provide a valid string value to specify what type of entity it is. The `LogicalName` is defined in the entity metadata.

When using the early-bound style, this value is set by the constructor of the generated class. For example: `var account = new Entity("account");`

In your code, if you later want to retrieve the string value that describes the type of entity, you can use the <xref:Microsoft.Xrm.Sdk.Entity.LogicalName> property. This is useful for the many APIs that require an entity logical name as a parameter.

## Entity.Id

When you instantiate an entity instance, whether using the late-bound or early-bound style, it doesn't have a unique id set. If you are creating an entity, you shouldn't set it, but allow it to be set by the system when you create (save) it.

If you are retrieving an entity, it will include the primary key attribute value whether you request it or not. The primary key attribute name is different for each type of entity. Generally, the name of the primary key attribute is the entity `logicalname` + `id`. So for an account entity it is `accountid` and for contact it is `contactid`.

While you can get or set the primary key value using the primary key attribute, you can also use the <xref:Microsoft.Xrm.Sdk.Entity.Id>  property to access the value without having to remember the name of the primary key attribute.

## Early bound access to attributes

If you are using the early-bound style with generated classes, you will find typed properties for each attribute in the class. The properties for the attributes use the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.SchemaName> and they can be accessed directly on the entity instance.
For example: 


```csharp
//Using the early-bound Account entity class
var account = new Account();
// set attribute values
// string primary name
account.Name = "Contoso";
// Boolean (Two option)
account.CreditOnHold = false;
// DateTime
account.LastOnHoldTime = new DateTime(2017, 1, 1);
// Double
account.Address1_Latitude = 47.642311;
account.Address1_Longitude = -122.136841;
// Int
account.NumberOfEmployees = 500;
// Money
account.Revenue = new Money(new decimal(5000000.00));
// Picklist (Option set)
account.AccountCategoryCode = new OptionSetValue(1); //Preferred customer
```

## Late bound access to attributes

The data contained within an entity is in the <xref:Microsoft.Xrm.Sdk.Entity>.<xref:Microsoft.Xrm.Sdk.Entity.Attributes> property. This property is an <xref:Microsoft.Xrm.Sdk.AttributeCollection> that provides a whole set of methods to add new attributes, check whether an attribute exists, or remove attributes.

### Discover attribute names and data types

In the late-bound style, you need to know the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.LogicalName> for the attribute and the data type. The `LogicalName` is the lowercase version of the `SchemaName`. You can discover the `LogicalName` and type for attributes in several ways:

- View the definition of the attribute in the customization tools
- For system entities, you can review the [Entity Reference](../reference/about-entity-reference.md)
- Use a tool to browse the metadata for entities, such as the Metadata Browser described in [Browse the metadata for your environment](../browse-your-metadata.md)

Attribute types can be any of the following:

|Type|Description|
|--|--|
|<xref:Microsoft.Xrm.Sdk.EntityReference>|A **Lookup** attribute. A link to another record.|
|<xref:Microsoft.Xrm.Sdk.BooleanManagedProperty>|Used only for entities that can be solution components, such as the [WebResource Entity](../reference/entities/webresource.md). More information: [Use managed properties](../use-managed-properties.md)|
|<xref:Microsoft.Xrm.Sdk.Money>|A **Currency** attribute.|
|<xref:Microsoft.Xrm.Sdk.OptionSetValue>|An **Option Set** attribute. **State** and **Status** attributes also use this type. |
|<xref:System.Boolean>|A **Two Option** attribute.|
|<xref:System.Byte>[]|An **Image** attribute. Each entity can have one image and the attribute is named `entityimage`. A URL to download the image can be retrieved in a companion attribute named `entityimage_url`. More information: [Image attributes](../image-attributes.md) |
|<xref:System.DateTime>|A **Date and Time** attribute usually uses a UTC value. More information: [Behavior and format of the date and time attribute](../behavior-format-date-time-attribute.md)|
|<xref:System.Decimal>|A **Decimal Number** attribute.|
|<xref:System.Double>|A **Floating Point Number** attribute.|
|<xref:System.Guid>|Usually used as the unique identifier for the entity. |
|<xref:System.Int32>|A **Whole Number** attribute.|
|<xref:System.String>|**Multiple Lines of Text** and **Single Line of Text** attributes use this type.|



There are three different ways to interact with entity attributes using the late-bound style:
- Use the indexer on the entity
- Use the indexer on the `Attributes` collection
- Use the entity methods provided

### Use the indexer on the entity

In most cases using the late-bound style, you can interact with collection by using the indexer to get or set the value of an attribute using the `LogicalName` for the attribute. For example, to set the name attribute of an account:

```csharp
//Use Entity class with entity logical name
var account = new Entity("account");
// set attribute values
// string primary name
account["name"] = "Contoso";
// Boolean (Two option)
account["creditonhold"] = false;
// DateTime
account["lastonholdtime"] = new DateTime(2017, 1, 1);
// Double
account["address1_latitude"] = 47.642311;
account["address1_longitude"] = -122.136841;
// Int
account["numberofemployees"] = 500;
// Money
account["revenue"] = new Money(new decimal(5000000.00));
// Picklist (Option set)
account["accountcategorycode"] = new OptionSetValue(1); //Preferred customer
```

### Use the indexer on the Attributes collection

Just like you would on the entity, you can also access a value using the indexer on the Attributes collection.

```csharp
string accountName = account.Attributes["name"];
```

### Use the entity methods

You can also use <xref:Microsoft.Xrm.Sdk.Entity> methods to get or set attribute values.

|Method|Description|
|--|--|
|<xref:Microsoft.Xrm.Sdk.Entity.GetAttributeValue``1(System.String)>|Use this to return a typed attribute value|
|<xref:Microsoft.Xrm.Sdk.Entity.SetAttributeValue(System.String,System.Object)>|Use this to set a typed attribute value|

For example:

```csharp
account.SetAttributeValue("name", "Account Name");
var accountName = account.GetAttributeValue<string>("name");
```



## Entity.FormattedValues

Any entity attribute value that can be displayed in the UI and is not a string will have a string formatted value that can be used to display the value in the UI. For example:

- Money values will have a string value with the appropriate currency and precision formatting.
- Date values will have the formatting set depending on how the system is configured
- OptionSet values will display the localized label that represents the integer value

> [!NOTE]
> Formatted values only apply to entities that have been retrieved. Once you set the value, a new formatted value is not calculated until you save the entity and retrieve the entity again. The formatted value is generated on the server.

You can access the formatted values using the <xref:Microsoft.Xrm.Sdk.Entity.FormattedValues> collection using an indexer or with the entity <xref:Microsoft.Xrm.Sdk.Entity.GetFormattedAttributeValue(System.String)> method.

For example, both of these retrieve the same formatted value:

```csharp
var formattedRevenueString1 = account.FormattedValues["revenue"];
var formattedRevenueString2 = account.GetFormattedAttributeValue("revenue");
```

More information: [Access formatted values](entity-operations-query-data.md#access-formatted-values)

## Entity.RelatedEntities 

When you create an entity you can also define a set of related entity records to create in the same operation. More information: [Create related entities in one operation](entity-operations-create.md#create-related-entities-in-one-operation)

When you retrieve an entity you can compose use the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> to by setting the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest.RelatedEntitiesQuery> with a query to include related entities in the results. More information: [Retrieve with related records](entity-operations-retrieve.md#retrieve-with-related-records)

If you include related entities in the results, you can also update values on those related entities and include them when you update the entity. More information: [Update related entities in one operation](entity-operations-update-delete.md#update-related-entities-in-one-operation)

## Convert to an EntityReference

Many message properties require only an <xref:Microsoft.Xrm.Sdk.EntityReference>. Use the <xref:Microsoft.Xrm.Sdk.Entity>.<xref:Microsoft.Xrm.Sdk.Entity.ToEntityReference> method to convert an entity to an entity reference.

## Convert to an entity class

If you are using the early bound style, you will need to convert the <xref:Microsoft.Xrm.Sdk.Entity> instance to the type of generated entity class you are using. This can usually be done with a cast, but you can also use the <xref:Microsoft.Xrm.Sdk.Entity>.<xref:Microsoft.Xrm.Sdk.Entity.ToEntity``1> method.

```csharp
Account account1 = (Account)retrievedEntity;
Account account2 = retrievedEntity.ToEntity<Account>();
```

> [!NOTE]
> This method cannot be used to convert a generated entity instance to another generated class or to <xref:Microsoft.Xrm.Sdk.Entity> . It can only be used to convert an <xref:Microsoft.Xrm.Sdk.Entity> instance to one of the generated classes that inherit from it. If the <xref:Microsoft.Xrm.Sdk.Entity> instance isn't actually an instance of the generated class this message will throw an error.

## Next Steps

These topics will explain more about working with CDS for Apps entities.

[Quick Start: Organization service sample (C#)](quick-start-org-service-console-app.md)
[Query data](entity-operations-query-data.md)<br />
[Create entities](entity-operations-create.md)<br />
[Retrieve an entity](entity-operations-retrieve.md)<br />
[Update and Delete entities](entity-operations-update-delete.md)<br />
[Associate and disassociate entities](entity-operations-associate-disassociate.md)<br />
[Generate classes for early-bound programming](generate-early-bound-classes.md)<br />