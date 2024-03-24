---
title: Web API EntityTypes
description: Learn about OData EntityTypes, which are named structured types with a key. EntityTypes describe the data types available in Dataverse Web API.
ms.date: 05/18/2023
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
ms.service: powerapps
applies_to: 
  - "Dynamics 365 (online)" 
search.audienceType: 
  - developer
contributors:
 - JimDaly
---
# Web API EntityTypes

Within the [CSDL $metadata document](web-api-service-documents.md#csdl-metadata-document), immediately below the [Service namespace](web-api-service-documents.md#service-namespace) there's a list of *EntityTypes*. An entity type is a named structured type with a key. It defines the named properties and relationships of a table.

`EntityType` elements usually have the following attributes:

|Attribute  |Description  |
|---------|---------|
|`Name`     |The name of the type; the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.LogicalName> for the table.|
|`BaseType` |The EntityType that the type inherits from.|

For example, this XML element is the `EntityType` for the `account` entity, excluding properties and navigation properties.

```xml
<EntityType Name="account" BaseType="mscrm.crmbaseentity">  
  <Key>  
    <PropertyRef Name="accountid" />  <!--The name of the primary key --> 
  </Key>  
  <!--Properties and navigation properties removed for brevity-->  
  <Annotation Term="Org.OData.Core.V1.Description" String="Business that represents a customer or potential customer. The company that is billed in business transactions." />  
</EntityType>  
```

Except for three exceptions, all entity types have the following child elements:

|Element  |Description  |
|---------|---------|
|`Key`|Contains a `<PropertyRef>` element where the `Name` attribute represents the primary key for the table.|
|`Property`|Contains details about a property of the EntityType. See [Web API Properties](web-api-properties.md).|
|`NavigationProperty`|Contains details about a relationship with this EntityType. See [Web API Navigation Properties](web-api-navigation-properties.md)|

## Special entity types

There are three entity types that don't have `Key`, `Property`, or `NavigationProperty` elements.

### crmbaseentity

This element defines a common abstract type for any table that contains business data.

`<EntityType Name="crmbaseentity" Abstract="true" />`

Because all entity types that contain business data inherit from `crmbaseentity`, `crmbaseentity` is referenced when a value isn't specific to one table.

### expando

This element defines an entity type that inherits from `crmbaseentity` but is also an [OData OpenType](https://www.odata.org/getting-started/advanced-tutorial/#openType).

`<EntityType Name="expando" BaseType="mscrm.crmbaseentity" OpenType="true" />`

An expando entity type can be used as a parameter to an action, or as a response property from a function or action.

More information: [Use open types with custom APIs](../use-open-types.md)

### crmmodelbaseentity

This element exists near the bottom of the $metadata document:

`<EntityType Name="crmmodelbaseentity" Abstract="true" />`

This element defines a common abstract type for any schema definitions. It's the base type for another abstract base class used for table definitions. Unless you want to create and modify tables, columns, and relationships using Web API you don't need to use entity types that inherit from this type. More information: [Use the Web API with table definitions](use-web-api-metadata.md).

## EntityType inheritance

For business data, there are two more abstract entity types that inherit from `crmbaseentity`:

|EntityType  |Description  |
|---------|---------|
|`principal`|`systemuser` and `team` entity types inherit from the `principal` entity type. Principal provides only the `ownerid` property, which every user-owned table has. This inheritance is what allows for user-owned records to be assigned to either a user or a team. <br /><br />  The `ownerid` property is the primary key for both `systemuser` and `team` EntityTypes.|
|`activitypointer`|Any table that is configured as an activity inherits from the `activitypointer` entity type. This type provides common properties found in entity types such as: `appointment`, `email`, `fax`, `letter`, `phonecall`, and `task`. You can also create a custom table that represents an activity. These common properties make it possible to retrieve a list of activities of different types using these common properties<br /> <br /> The `activityid` property is the primary key for all entity types that inherit from `activitypointer`.|

When working with table definitions, there another hierarchy of inheritance. <xref:Microsoft.Dynamics.CRM.MetadataBase> entity type inherits from the abstract `crmmodelbaseentity` to provide common `MetadataId` and `HasChanged` properties. More information: [Use the Web API with table definitions](use-web-api-metadata.md).

## Alternate Keys

When an entity type has any alternate keys defined, there's an `Annotation` that describes the properties that are involved in the alternate key definition.

The following example shows the annotation when the `account` entity has been configured to enable the `accountnumber` property as an alternate key.

```xml
<Annotation Term="OData.Community.Keys.V1.AlternateKeys">
    <Collection>
        <Record Type="OData.Community.Keys.V1.AlternateKey">
            <PropertyValue Property="Key">
                <Collection>
                    <Record Type="OData.Community.Keys.V1.PropertyRef">
                        <PropertyValue Property="Alias" String="accountnumber" />
                        <PropertyValue Property="Name" PropertyPath="accountnumber" />
                    </Record>
                </Collection>
            </PropertyValue>
        </Record>
    </Collection>
</Annotation>
```

More information: [Retrieve record using an alternate key](retrieve-entity-using-web-api.md#retrieve-record-using-an-alternate-key)

## Next steps

Learn about properties.

> [!div class="nextstepaction"]
> [Properties](web-api-properties.md)<br/>

### See also  

[Web API types and operations](web-api-types-operations.md)<br />
[Web API Service Documents](web-api-service-documents.md)<br />
[Web API Properties](web-api-properties.md)<br />
[Web API Navigation Properties](web-api-navigation-properties.md)<br />
[Web API Actions](web-api-actions.md)<br />
[Web API Functions](web-api-functions.md)<br />
[Web API Complex and Enumeration types](web-api-complex-enum-types.md)<br />
[Use the Dataverse Web API](overview.md)<br />


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
