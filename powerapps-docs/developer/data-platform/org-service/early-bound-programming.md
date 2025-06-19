---
title: "Late-bound and early-bound programming using the SDK for .NET (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Describes the different programming styles available when using the .NET SDK assemblies with the SDK for .NET." # 115-145 characters including spaces. This abstract displays in the search result.
ms.collection: get-started
ms.topic: "article"
ms.date: 04/03/2022
author: MicroSri
ms.author: sriknair
ms.reviewer: pehecke
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - phecke
---

# Late-bound and early-bound programming using the SDK for .NET

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

When you work with the SDK for .NET assemblies, you have two programming styles you can use: *late-bound* and *early-bound*.

The key difference between early and late binding involves type conversion. While early binding provides compile-time checking of all types so that no implicit casts occur, late binding checks types only when the object is created or an action is performed on the type. The <xref:Microsoft.Xrm.Sdk.Entity> class requires types to be explicitly specified to prevent implicit casts.

Late binding allows you to work with custom tables (entities) or columns (attributes) that weren't available when your code was compiled.

## Late-bound

Late-bound programming uses the <xref:Microsoft.Xrm.Sdk.Entity> class where you need to refer to table rows and columns (entities and attributes) using their `LogicalName` property values:

- <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.LogicalName>
- <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.LogicalName>

Relationships don't have a `LogicalName` property, so the <xref:Microsoft.Xrm.Sdk.Metadata.RelationshipMetadataBase>.<xref:Microsoft.Xrm.Sdk.Metadata.RelationshipMetadataBase.SchemaName> property is used.

The main advantage for late-bound programming is that you don't need to generate the classes or include that generated file within your projects. The generated file can be large.

The main disadvantages are:

- You don't get compile time validation on names of entities, attributes, and relationships.
- You need to know the names of the attributes and relationships in the metadata.

> [!TIP]
> A tool that you can use to find this information easily is the Metadata Browser. This is an app you can download and install in your organization. More information: [Browse the metadata for your environment](../browse-your-metadata.md)

### Example

The following example creates an account using the late-bound style.

```csharp
//Use Entity class specifying the entity logical name
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

## Early-bound

Early-bound programming requires that you first generate a set of classes based on the table and column definitions (entity and attribute metadata) for a specific environment using the code generation tool [Power Platform CLI pac modelbuilder build command](/power-platform/developer/cli/reference/modelbuilder#pac-modelbuilder-build). More information: [Generate classes for early-bound programming using the SDK for .NET](generate-early-bound-classes.md)

After generating early-bound classes using the code generation tool, you'll enjoy a better experience while you write code because classes and properties use the respective `SchemaName` property values:

- <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.SchemaName>
- <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.SchemaName>
- <xref:Microsoft.Xrm.Sdk.Metadata.RelationshipMetadataBase>.<xref:Microsoft.Xrm.Sdk.Metadata.RelationshipMetadataBase.SchemaName>

Simply instantiate the class and let Visual Studio IntelliSense provide the names of properties and relationships.

The classes generated for early-bound programming can also include definitions for any custom actions that are defined for the environment. This provides you with a pair of request and response classes to use with these custom actions. More information: [Custom Actions](../custom-actions.md)

Classes are generated using table definitions from a specific environment instance and each instance may have different tables and columns where these can change over time. You may need to write code to work for tables that aren't present when you generate the strongly typed classes.

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

Which programming style you choose to use is up to you. The following table provides the advantages and disadvantages for each.

|Early-bound|Late-bound|
|--|--|
|You can verify entity, attribute, and relationship names at compile time|No compile time verification of entity, attribute, and relationship names|
|You must generate entity classes|You don't need to generate entity classes|
|Better IntelliSense support|Less IntelliSense support|
|Less code to write; code is more readable| More code to write; code is less readable|
|Very slightly less performant|Very slightly more performant|

## Mix early and late bound

Because all the generated classes inherit from the <xref:Microsoft.Xrm.Sdk.Entity> class used with late-bound programming, you can work with entities, attributes, and relationships not defined within classes.

### Examples

The following example shows one way to mix early and late binding methods using <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceContext>.  
  
```csharp  
// Create an context object  
AWCServiceContext context = new AWCServiceContext(_serviceProxy);  
  
// Instantiate an account object using the Entity class.  
Entity testaccount = new Entity("account");  
  
// Set several attributes. For account, only the name is required.   
testaccount["name"] = "Fourth Coffee";  
testaccount["emailaddress1"] = "marshd@contoso.com";  
  
// Save the entity using the context object.  
context.AddToAccountSet(testaccount);  
context.SaveChanges();  
  
```  

If a custom attribute wasn't included in the generated classes, you can still use it.

```csharp
var account = new Account();
// set attribute values
    // string primary name
    account.Name = "Contoso";
    // A custom boolean attribute not included in the generated classes.
    account["sample_customboolean"] = false;


//Create the account
Guid accountid = svc.Create(account);
```

#### Assign an early bound instance to a late bound instance  

 The following sample shows how to assign an early bound instance to a late bound instance.  
  
```csharp
Entity incident = ((Entity)context.InputParameters[ParameterName.Target]).ToEntity<Incident>();  
Task relatedEntity = new Task() { Id = this.TaskId };  
  
incident.RelatedEntities[new Relationship("Incident_Tasks")] =   
new EntityCollection(new Entity[] { relatedEntity.ToEntity<Entity>() });  
```

### See also

[Entity operations using the SDK for .NET](entity-operations.md)<br />
[Create table rows using the SDK for .NET](entity-operations-create.md)<br />
[Retrieve a table row using the SDK for .NET](entity-operations-retrieve.md)<br />
[Query data using the SDK for .NET](entity-operations-query-data.md)<br />
[Update and delete table rows using the SDK for .NET](entity-operations-update-delete.md)<br />
[Associate and disassociate table rows using the SDK for .NET](entity-operations-associate-disassociate.md)<br />
[IOrganizationService Interface](iorganizationservice-interface.md)<br />
[Using OrganizationServiceContext](organizationservicecontext.md)<br />

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
