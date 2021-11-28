---
title: "Web API Navigation Properties (Microsoft Dataverse)| Microsoft Docs"
description: "Describes OData Navigation Property elements defined for EntityTypes within the Dataverse Web API."
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
# Web API Navigation Properties

Within the [CSDL $metadata document](web-api-service-documents.md#csdl-metadata-document), each entity type that is not abstract will have `NavigationProperty` elements.

The `NavigationProperty` element describes data related to the current entity type. When you retrieve a record, you can expand navigation properties to include related data.

`NavigationProperty` elements have the following attributes:


|Attribute |Description  |
|---------|---------|
|`Name`|The name of the navigation property. This value is case sensitive.|
|`Type`|The related entity type. This can be to a single value or a collection of a type.|
|`Partner`|The name of the navigation property on the other side of the relationship.|
|`Nullable="false"`|Whether the value can be null.|

There are two types of navigation properties: ***single-valued*** and ***collection-valued***. This distinction is important because capabilities for each type of navigation property are different.

## Single-valued navigation properties

When a navigation property Type refers to a single value, it represents a many-to-one relationship to set a reference to another table record. This is commonly called a 'lookup'. For example, this is the `account` table `createdby` navigation property:

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

This single-valued navigation property connects multiple `account` records to a single `systemuser` record. Each `systemuser` record will have a collection-valued navigation property named `lk_accountbase_createdby` that connects them to the `account` records they have created.

### Lookup properties

Single-valued navigation properties will also have a `ReferentialConstraint` with a `Property` attribute that refers to a lookup property. You can recognize lookup properties because they use the following naming convention: `_<name>_value`. 

The `ReferentialConstraint` will also have a `ReferencedProperty` attribute that identifies the primary key name of the related entity type.

In most cases the `<name>` found in the lookup property will match the name of the navigation property. However, when the single-valued navigation property is part of a multi-table (or polymorphic) lookup there may be a single lookup property which is the `ReferentialConstraint` for more than one single-valued navigation property.

An entity type may have something like the following combination where a single `_customerid_value` lookup property supports  multiple single-valued navigation properties that represent a multi-table lookup. There will be one single-valued navigation property for each type of table supported by the multi-table lookup.

```xml
<EntityType 
    Name="socialprofile" 
    BaseType="mscrm.crmbaseentity">
    <Key>
        <PropertyRef Name="socialprofileid" />
    </Key>
    <Property 
        Name="_customerid_value" 
        Type="Edm.Guid">
        <Annotation 
            Term="Org.OData.Core.V1.Description" 
            String="Shows the customer that this social profile belongs to." />
    </Property>
    <NavigationProperty 
        Name="customerid_contact" 
        Type="mscrm.contact" 
        Nullable="false" 
        Partner="Socialprofile_customer_contacts">
        <ReferentialConstraint 
            Property="_customerid_value" 
            ReferencedProperty="contactid" />
    </NavigationProperty>
    <NavigationProperty 
        Name="customerid_account" 
        Type="mscrm.account" 
        Nullable="false" 
        Partner="Socialprofile_customer_accounts">
        <ReferentialConstraint 
            Property="_customerid_value" 
            ReferencedProperty="accountid" />
    </NavigationProperty>
</EntityType>
```

In these cases, setting the value of any of the single-valued navigation properties will set all the other participating single-valued navigation properties to null. The corresponding lookup property GUID value will change, but you will need to retrieve specific annotations available to know which table it now refers to. More information: [Retrieve data about lookup properties](query-data-web-api.md#retrieve-data-about-lookup-properties).

## Collection-valued navigation properties

When a navigation property `Type` refers to a collection value, it represents a one-to-many or many-to-many relationship. For example, this is the account entity `Account_Tasks` navigation property.

```xml
<NavigationProperty 
    Name="Account_Tasks" 
    Type="Collection(mscrm.task)" 
    Partner="regardingobjectid_account_task" 
/>
```

This navigation property connects an `account` record to many `task` records. Each `task` has a single-valued navigation property named `regardingobjectid_account_task` that refers to the `account` as the regarding object.

When the `Name` and the `Partner` of the collection-valued navigation property are the same, it represents a many-to-many relationship.

### Many-to-Many Relationships

The way you work with collection-valued navigation properties using OData is the same regardless of whether the relationship is a one-to-many or many-to-many relationship. Both are considered collections, but many-to-many relationships have some implementation details you can find in the service documents. For most use cases, you can ignore them.

For example, every many-to-many relationship has an *intersect table* which supports it. These intersect tables have entity types that typically have just 4 read-only properties. The following is an example of an entity type for an intersect table that supports a many-to-many relationship between `customer` and `product` tables.

```xml
<EntityType Name="new_customer_product" BaseType="mscrm.crmbaseentity">
    <Key>
        <PropertyRef Name="new_customer_productid" />
    </Key>
    <Property Name="new_customerid" Type="Edm.Guid" />
    <Property Name="versionnumber" Type="Edm.Int64"/>
    <Property Name="new_customer_productid" Type="Edm.Guid"/>
    <Property Name="new_productid" Type="Edm.Guid"/>
</EntityType>
```

You can't work with entity types that represent intersect tables directly because all the properties are read-only. Perform operations on the collection-valued navigation properties. More information: [Associate and disassociate table rows using the Web API](associate-disassociate-entities-using-web-api.md)


### See also  

[Use the Dataverse Web API](overview.md)<br />
[Web API types and operations](web-api-types-operations.md)<br />
[Web API Service Documents](web-api-service-documents.md)<br />
[Web API EntityTypes](web-api-entitytypes.md)<br />
[Web API Properties](web-api-properties.md)<br />
[Web API Actions](web-api-actions.md)<br />
[Web API Functions](web-api-functions.md)<br />
[Web API Complex and Enumeration types](web-api-complex-enum-types.md)<br />
[OData Version 4.0. Part 3: Common Schema Definition Language (CSDL) Plus Errata 03 7.1 Element edm:NavigationProperty](https://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part3-csdl/odata-v4.0-errata03-os-part3-csdl-complete.html#_Toc453752537)<br />


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]