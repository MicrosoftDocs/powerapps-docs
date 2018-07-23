---
title: "Late-bound and Early-bound programming using the Organization service (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "<Description>" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Late-bound and Early-bound programming using the Organization service

When you work with the Organization service assemblies you have two styles you can use: *late-bound* and *early-bound*.

## Late-Bound

Late-bound programming uses the <xref:Microsoft.Xrm.Sdk.Entity> class and you need to refer to entities, and attributes using their `LogicalName` property values: 
- <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.LogicalName> 
- <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.LogicalName>

Relationships do not have a `LogicalName` property, so the <xref:Microsoft.Xrm.Sdk.Metadata.RelationshipMetadataBase>.<xref:Microsoft.Xrm.Sdk.Metadata.RelationshipMetadataBase.SchemaName> property is used.

The main advantage for late-bound programming is that you don't need to generate the classes or include that generated file within your projects. The generated file can be quite large. The main disadvantage is that you don't get compile time validation of names of entities, attributes, and relationships.

### Example

The following example creates an account using the late-bound style.

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
                
//Create the account
Guid accountid = svc.Create(account);
```

## Early-Bound

Early-bound programming requires that you first generate a set of classes based on the metadata for a specific organization using the code generation tool (CrmSvcUtil.exe). More information: [Generate classes for early-bound programming using the Organization service](generate-early-bound-classes.md)

When you have generated early-bound entity classes using the code generation tool you will enjoy a better experience while you write code because classes and attribute properties using the respective `SchemaName` property values:

- <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.SchemaName> 
- <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.SchemaName>
- <xref:Microsoft.Xrm.Sdk.Metadata.RelationshipMetadataBase>.<xref:Microsoft.Xrm.Sdk.Metadata.RelationshipMetadataBase.SchemaName>

Simply instantiate the class and let IntelliSense in Visual Studio provide the names of properties and relationships.

The classes generated for early-bound programming can also include definitions for any custom actions that are defined for the environment. This will provide you with a pair of request and response classes to use with these custom actions. More information: [Custom Actions](../custom-actions.md)

There is also an option to extend the code generation tool to change the output. One extension creates enums for each optionset option value. This provides a better experience because you don't have to look up the integer value for each option. More information: [Create extensions for the code generation tool](extend-code-generation-tool.md)

However, because the classes are generated using metadata from a specific instance, and each instance may have different entities and attributes, and these can change over time. You may need to write code to work for entities that are not present when you generate the strongly typed classes.

> [!IMPORTANT]
> If you are using the <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceProxy> to provide the <xref:Microsoft.Xrm.Sdk.IOrganizationService> methods you will use, you must call the <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceProxy>.<xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceProxy.EnableProxyTypes> method to enable early bound types.


### Example

The following example creates an account using the early-bound style.

```csharp
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

//Create the account
Guid accountid = svc.Create(account);
```

## Choose which style

Which style you choose to use is up to you. The following table provides the advantages and disadvantages for each.

|Early-bound|Late-bound|
|--|--|
|You can verify entity, attribute, and relationship names at compile time|No compile time verification of entity, attribute, and relationship names|
|You must generate entity classes|You don't need to generate entity classes|
|Better IntelliSense support|Less IntelliSense support|
|Less, more readable code| More, less readable code|
|Very slightly less performant|Very slightly more performant|


## Mix early and late bound

Because all the generated classes inherit from the <xref:Microsoft.Xrm.Sdk.Entity> class used with late-bound programming, you can work with entities, attributes, and relationships not defined within classes.

### See also

[IOrganizationService Interface](iorganizationservice-interface.md)<br />
[Using OrganizationServiceContext](organizationservicecontext.md)