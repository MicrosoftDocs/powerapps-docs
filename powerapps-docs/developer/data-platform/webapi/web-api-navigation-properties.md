---
title: Web API navigation properties
description: Learn about OData navigation property elements that are defined for EntityTypes in the Microsoft Dataverse Web API.
ms.topic: how-to
ms.date: 04/06/2022
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
ms.custom: bap-template
---
# Web API navigation properties

In the [CSDL $metadata document](web-api-service-documents.md#csdl-metadata-document), each entity type that isn't abstract has `NavigationProperty` elements. `NavigationProperty` elements describe data that's related to the current entity type. When you retrieve a record, you can expand navigation properties to include related data.

The following table describes the attributes of `NavigationProperty` elements.


|Attribute |Description  |
|---------|---------|
|`Name`|The name of the navigation property; case-sensitive |
|`Type`|The related entity type; can be to a single value or a collection of a type|
|`Partner`|The name of the navigation property on the other side of the relationship|
|`Nullable="false"`|Whether the value can be null|

> [!IMPORTANT]
> There are two types of navigation properties: [*single-valued*](#single-valued-navigation-properties) and [*collection-valued*](#collection-valued-navigation-properties). This distinction is important because the capabilities of each type of navigation property are different.

## Single-valued navigation properties

When a navigation property `Type` refers to a single value, it represents a one-to-many relationship that creates a reference to another table record. This relationship is commonly called a *lookup*. The following example is the `account` table `createdby` navigation property:

```xml
<NavigationProperty 
    Name="createdby" 
    Type="mscrm.systemuser" 
    Nullable="false" 
    Partner="lk_accountbase_createdby">
    <ReferentialConstraint 
        Property="_createdby_value" 
        ReferencedProperty="systemuserid" />
</NavigationProperty>
```

This single-valued navigation property connects multiple `account` records to a single `systemuser` record. Each `systemuser` record has a collection-valued navigation property named `lk_accountbase_createdby` that connects it to the `account` records the user has created.

These values are stored in relationship definitions. You can access them using the SDK <xref:Microsoft.Xrm.Sdk.Metadata.OneToManyRelationshipMetadata> or the Web API <xref:Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata> entity type, as described in the following table.

|Attribute|OneToManyRelationshipMetadata property|Description|
|---------|---------|---------|
|`Name`|`ReferencingEntityNavigationPropertyName`|The name of the single-valued navigation property.|
|`Partner`|`ReferencedEntityNavigationPropertyName`|The name of the collection-valued navigation property.|


### Lookup properties

Single-valued navigation properties have a `ReferentialConstraint` with a `Property` attribute that refers to a lookup property. Lookup properties use the following naming convention: `_<name>_value`. [Learn more about lookup properties](web-api-properties.md#lookup-properties).

The `ReferentialConstraint` has a `ReferencedProperty` attribute that identifies the primary key name of the related entity type.

In most cases, the `<name>` found in the lookup property matches the name of the navigation property, except when the single-valued navigation property represents a multi-table lookup.

#### Multi-table lookups

When the single-valued navigation property is part of a multi-table, or polymorphic, lookup, a single lookup property is the `ReferentialConstraint` for more than one single-valued navigation property.

An entity type may have something like the following combination, where a single `_customerid_value` lookup property supports  multiple single-valued navigation properties that represent a multi-table lookup. There is one single-valued navigation property for each type of table supported by the multi-table lookup.

```xml
<EntityType 
    Name="socialprofile" 
    BaseType="mscrm.crmbaseentity">
    <Key>
        <PropertyRef Name="socialprofileid" />
    </Key>
    <Property 
        Name="_customerid_value" <!-- lookup property -->
        Type="Edm.Guid">
        <Annotation 
            Term="Org.OData.Core.V1.Description" 
            String="Shows the customer that this social profile belongs to." />
    </Property>
    <NavigationProperty 
        Name="customerid_contact" <!-- Name different from lookup property -->
        Type="mscrm.contact" 
        Nullable="false" 
        Partner="Socialprofile_customer_contacts">
        <ReferentialConstraint 
            Property="_customerid_value" <!--  Reference to lookup property  -->
            ReferencedProperty="contactid" />
    </NavigationProperty>
    <NavigationProperty 
        Name="customerid_account" <!-- Name different from lookup property -->
        Type="mscrm.account" 
        Nullable="false" 
        Partner="Socialprofile_customer_accounts">
        <ReferentialConstraint 
            Property="_customerid_value"  <!--  Reference to lookup property  -->
            ReferencedProperty="accountid" />
    </NavigationProperty>
</EntityType>
```

In these cases, setting the value of any of the single-valued navigation properties sets all the other participating single-valued navigation properties to null. The corresponding lookup property GUID value changes, but you need to retrieve specific annotations to know which table it now refers to. More information: [Lookup property data](query-data-web-api.md#lookup-property-data)

## Collection-valued navigation properties

When a navigation property `Type` refers to a collection value, it represents a many-to-one or many-to-many relationship. The following example is the account entity `Account_Tasks` navigation property:

```xml
<NavigationProperty 
    Name="Account_Tasks" 
    Type="Collection(mscrm.task)" 
    Partner="regardingobjectid_account_task" 
/>
```

This navigation property connects an `account` record to many `task` records. Each `task` has a single-valued navigation property named `regardingobjectid_account_task` that refers to the `account` as the regarding object.

The way you work with collection-valued navigation properties using OData is the same regardless of whether the relationship is one-to-many or many-to-many. Both are considered collections and you interact with them the same way.

### Many-to-one relationships

A many-to-one relationship is the mirror image of the one-to-many relationship. It has a partner single-valued navigation property. In the earlier [single-valued navigation properties](#single-valued-navigation-properties) example, we looked at the `createdby` single-valued navigation property for the `account` entity type.

In the `systemuser` entity type, the collection-valued navigation property partner named `lk_accountbase_createdby` exists.

```xml
<NavigationProperty Name="lk_accountbase_createdby"
    Type="Collection(mscrm.account)"
    Partner="createdby" />
```

### Many-to-many Relationships

When the `Name` and the `Partner` of the collection-valued navigation property are the same, it represents a many-to-many relationship.

Many-to-many relationships have some implementation details you can find in the service documents. For most use cases, you can ignore them.

For example, every many-to-many relationship has an *intersect table* that supports it. These intersect tables have entity types that typically have four read-only properties. In the following example, the `teammembership` entity type is an intersect table that supports a many-to-many relationship between the `systemuser` and `team` entity types:

```xml
<EntityType Name="teammembership"
    BaseType="mscrm.crmbaseentity">
    <Key>
        <PropertyRef Name="teammembershipid" />
    </Key>
    <Property Name="systemuserid"
        Type="Edm.Guid" />
    <Property Name="versionnumber"
        Type="Edm.Int64" />
    <Property Name="teammembershipid"
        Type="Edm.Guid" />
    <Property Name="teamid"
        Type="Edm.Guid" />
</EntityType>
```

You can't work with entity types that represent intersect tables directly because all the properties are read-only. Perform operations on the respective collection-valued navigation properties for each entity type. More information: [Associate and disassociate table rows using the Web API](associate-disassociate-entities-using-web-api.md)

For this many-to-many relationship, the `systemuser` entity type has the following collection-valued navigation property:

```xml
<NavigationProperty Name="teammembership_association"
    Type="Collection(mscrm.team)"
    Partner="teammembership_association" />
```

The `team` entity type has this collection-valued navigation property:

```xml
<NavigationProperty Name="teammembership_association"
    Type="Collection(mscrm.systemuser)"
    Partner="teammembership_association" />
```

These values are stored in relationship definitions. You can access them using the SDK <xref:Microsoft.Xrm.Sdk.Metadata.ManyToManyRelationshipMetadata> or the Web API <xref:Microsoft.Dynamics.CRM.ManyToManyRelationshipMetadata> entity type, as described in the following table.

|Attribute|ManyToManyRelationshipMetadata property|Description|
|---------|---------|---------|
|`Name`|`Entity1NavigationPropertyName`|The name of the collection-valued navigation property for one of the entity types|
|`Partner`|`Entity2NavigationPropertyName`|The name of the collection-valued navigation property for the other entity type|

## Next steps

Learn about Action definitions.

> [!div class="nextstepaction"]
> [Action definitions](web-api-actions.md)<br/>


### See also  

[Web API types and operations](web-api-types-operations.md)   
[Web API service documents](web-api-service-documents.md)   
[Web API EntityTypes](web-api-entitytypes.md)   
[Web API properties](web-api-properties.md)   
[Web API actions](web-api-actions.md)   
[Web API functions](web-api-functions.md)   
[Web API complex and enumeration types](web-api-complex-enum-types.md)   
[Use the Dataverse Web API](overview.md)   
[OData Version 4.0. Part 3: Common Schema Definition Language (CSDL) Plus Errata 03 7.1 Element edm:NavigationProperty](https://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part3-csdl/odata-v4.0-errata03-os-part3-csdl-complete.html#_Toc453752537)   


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
