---
title: "Web API EntityTypes (Microsoft Dataverse)| Microsoft Docs"
description: "Describes OData EntityTypes which are named structured types with a key. EntityTypes describe the data types available in Dataverse Web API."
ms.custom: ""
ms.date: 11/24/2021
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)" 
author: "JimDaly" # GitHub ID
ms.author: pehecke
manager: "sunilg"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Web API EntityTypes

Within the [CSDL $metadata document](web-api-service-documents.md#csdl-metadata-document), immediately below the [Service namespace](web-api-service-documents.md#service-namespace) you will find a list of *EntityTypes*. An entity type is a named structured type with a key. It defines the named properties and relationships of a table.

`EntityType` elements usually have the following attributes:

|Attribute  |Description  |
|---------|---------|
|Name     |The name of the type|
|BaseType |The EntityType that the type inherits from.|

For example, this is the `EntityType` element for the `account` entity, excluding properties and navigation properties.

```xml
<EntityType Name="account" BaseType="mscrm.crmbaseentity">  
  <Key>  
    <PropertyRef Name="accountid" />  
  </Key>  
  <!--Properties and navigation properties removed for brevity-->  
  <Annotation Term="Org.OData.Core.V1.Description" String="Business that represents a customer or potential customer. The company that is billed in business transactions." />  
</EntityType>  
```

Except for three exceptions, all entity types will have the following child elements:

|Element  |Description  |
|---------|---------|
|`Key`|Contains a `<PropertyRef>` element where the `Name` attribute represents the primary key for the table.|
|`Property`|Contains details about a property of the EntityType. See [Web API Properties](web-api-properties.md).|
|`NavigationProperty`|Contains details about a relationship with this EntityType. See [Web API Navigation Properties](web-api-navigation-properties.md)|

## Special entity types

There are three entity types which do not have `Key`, `Property` or `NavigationProperty` elements.

### crmbaseentity

This element defines a common abstract type for any table that contain business data.

`<EntityType Name="crmbaseentity" Abstract="true" />`

Because almost all entity types inherit from `crmbaseentity`, you will find `crmbaseentity` referenced when a value isn't specific to one table.

### expando

This element defines an EntityType that inherits from crmbaseentity but is also an OpenType.

`<EntityType Name="expando" BaseType="mscrm.crmbaseentity" OpenType="true" />`

An expando entity type can be used as a parameter to an Action or Function. More information: Expando EntityType.

### crmmodelbaseentity

Near the bottom of the $metadata document, you will find this element:

`<EntityType Name="crmmodelbaseentity" Abstract="true" />`

This element defines a common abstract type for any schema definitions. It is the base type for another abstract base class used for table definitions. More information: [Use the Web API with table definitions](use-web-api-metadata.md).

## EntityType inheritance

For business data you will find two more abstract EntityTypes:

|EntityType  |Description  |
|---------|---------|
|`principal`|`systemuser` and `team` EntityTypes inherit from the `principal` entity type. Principal provides only the `ownerid` property, which every user-owned entity has. This is what allows for user-owned entities to be assigned to either a user or a team. <br /><br />  The `ownerid` property is the primary key for both `systemuser` and `team` EntityTypes.|
|`activitypointer`|Any table that is configured as an activity will inherit from the `activitypointer` entity type. This type provides common properties found in entity types such as: `appointment`, `email`, `fax`, `letter`, `phonecall`, and `task`. These common properties make it possible to retrieve a list of activities of different types using these common properties<br /> <br /> The `activityid` property is the primary key for all entity types that inherit from `activitypointer`.|

When working with table definitions, there another hierarchy of inheritance. <xref:Microsoft.Dynamics.CRM.MetadataBase?text=MetadataBase EntityType/> inherits from the abstract `crmmodelbaseentity` to provide common `MetadataId` and `HasChanged` properties. More information: [Use the Web API with table definitions](use-web-api-metadata.md).

## Alternate Keys

When an entity type has any alternate keys defined, you will find an `Annotation` that describes the properties that are involved in the alternate key definition.

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

More information: [Retrieve using an alternate key](retrieve-entity-using-web-api.md#retrieve-using-an-alternate-key)

<!-- 
TODO:
Use Alternate Keys
o	Update using an alternate key
o	Delete using an alternate key
o	Reference a record using alternate key in a Function
o	Reference a record using an alternate key in an Action
-->

### See also  

[Use the Dataverse Web API](overview.md)<br />
[Web API types and operations](web-api-types-operations.md)<br />
[Web API Service Documents](web-api-service-documents.md)<br />
[Web API Properties](web-api-properties.md)<br />


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]