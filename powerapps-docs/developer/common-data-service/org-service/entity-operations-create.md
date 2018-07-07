---
title: "<Topic Title> (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "<Description>" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Create entities using the Organization Service

<!-- use-early-bound-entity-classes-create-update-delete.md
manage-duplicate-detection-create-update.md -->

This topic will include examples using both late-bound and early-bound programming styles. More information: [Early-bound and Late-bound programming using the Organization service](early-bound-programming.md)

## Basic Create

The following examples show how to create an entity record using the late-bound and early-bound style.


### Late-bound example

The following example shows using the <xref:Microsoft.Xrm.Sdk.Entity> class to create an account record using the  <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*> method. 

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
    account["revenue"] = 5000000.00;
    // Picklist (Option set)
    account["accountcategorycode"] = new OptionSetValue(1); //Preferred customer
                
//Create the account
Guid accountid = crmSvc.Create(account);
```

### Early-bound example

Most of the time you use the generated properties in the same way as the late-bound style, but for certain types, such as the <xref:Microsoft.Xrm.Sdk.Money> type used for the `Revenue` property below, you will need to cast a value to a specific type.


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
Guid accountid = crmSvc.Create(account);
```

## Use the CreateRequest class

Instead of using the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*> method, you can use either the late-bound <xref:Microsoft.Xrm.Sdk.Entity> class or the early-bound class with the <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> class by setting the instance to the <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest.Target> property and then using the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*> method to get a <xref:Microsoft.Xrm.Sdk.Messages.CreateResponse>. The id of the created record will be in the <xref:Microsoft.Xrm.Sdk.Messages.CreateResponse.id> property value.

```csharp
var request = new CreateRequest() { Target = account };
var response  = (CreateResponse)crmSvc.Execute(request);
Guid accountid = response.id;
```
<!-- TODO: Need information about why someone would do this -->

## Create related entities in one operation

When you create a new entity record you can also create related entity records in the same operation.

The following late-bound and early-bound examples will create an [Account](../reference/entities/account.md) and a [Contact](../reference/entities/contact.md) related to that account using the [contact account_primary_contact](../reference/entities/contact.md#BKMK_account_primary_contact) one-to-many relationship where the [account primarycontactid](../reference/entities/account.md#BKMK_PrimaryContactId) lookup is the `ReferencingAttribute`.

The examples will also create three related [Task](../reference/entities/task.md) entity records using the [account Account_Tasks](../reference/entities/account.md#BKMK_Account_Tasks) one-to-many relationship where the [task regardingobjectid](../reference/entities/task.md#BKMK_RegardingObjectId) lookup 
is the `ReferencingAttribute`.

### Late-bound example

In the late-bound style you must explicitly add the related entity(ies) to an <xref:Microsoft.Xrm.Sdk.EntityCollection> and then use the <xref:Microsoft.Xrm.Sdk.Relationship> class to specify the relationship using the `SchemaName` of the relationship before you can add them to the <xref:Microsoft.Xrm.Sdk.Entity>.<xref:Microsoft.Xrm.Sdk.Entity.RelatedEntities> property.

```csharp
// Use Entity class with entity logical name
var account = new Entity("account");

// Set attribute values
    // string primary name
    account["name"] = "Sample Account";

// Create Primary contact
var primaryContact = new Entity("contact");
primaryContact["firstname"] = "John";
primaryContact["lastname"] = "Smith";

// Add the contact to an EntityCollection
EntityCollection primaryContactCollection = new EntityCollection();
primaryContactCollection.Entities.Add(primaryContact);

// Set the value to the relationship
account.RelatedEntities[new Relationship("account_primary_contact")] = primaryContactCollection;

// Add related tasks to create
var taskList = new List<Entity>() {
            new Entity("task") { ["subject"] = "Task 1" },
            new Entity("task") { ["subject"] = "Task 2" },
            new Entity("task") { ["subject"] = "Task 3" }
        };

// Add the tasks to an EntityCollection
EntityCollection tasks = new EntityCollection(taskList);

// Set the value to the relationship
account.RelatedEntities[new Relationship("Account_Tasks")] = tasks;

// Create the account
Guid accountid = crmSvc.Create(account);
```

### Early-bound example

With early-bound classes you can write less code because the classes include definitions of the relationships.

```csharp
var account = new Account();
// set attribute values
// string primary name
account.Name = "Sample Account";

// Set the account primary contact
account.account_primary_contact = new Contact()
{ FirstName = "John", LastName = "Smith" };

// Set a list of Tasks to create
account.Account_Tasks = new List<Task>() {
        new Task() { Subject = "Task 1" },
        new Task() { Subject = "Task 2" },
        new Task() { Subject = "Task 3" }
    };

// Create the account
Guid accountid = crmSvc.Create(account);
```

## Associate entities on create

You can associate any new record with an existing record when you create it in the same way you would when updating it. You must use an <xref:Microsoft.Xrm.Sdk.EntityReference> to set the value of a lookup attribute.

This assignment is the same for both early and late-bound styles.

```csharp
//Use Entity class with entity logical name
var account = new Entity("account");

// set attribute values
    //string primary name
    account["name"] = "Sample Account";

Guid contactId = new Guid("e6fa5509-2582-e811-a95e-000d3af40ae7");

account["primarycontactid"] = new EntityReference("contact", contactId);

//Create the account
Guid accountid = crmSvc.Create(account);
```
### Use alternate keys

If you don't know the id of the entity and the following conditions are true:
- You have configured alternate keys for the entity
- You know the key values

You can use the alternate <xref:Microsoft.Xrm.Sdk.EntityReference> constructors using the `keyName` and `keyValue` parameters.
```csharp
account["primarycontactid"] = new EntityReference("contact", "sample_username", "john.smith123");
```
More information: 
- [Define alternate keys to reference records](../../../maker/common-data-service/define-alternate-keys-reference-records.md)
- [Work with alternate keys](../define-alternate-keys-entity.md)
- [Use an alternate key to create a record](../use-alternate-key-create-record.md)


## Check for Duplicate records

## Create a new entity from another entity

## Use IOrganizationService.Create

### Late-bound example

When you use the late bound programming style you need to refer to entities and attributes using their `LogicalName` property values. <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.LogicalName> and <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.LogicalName> respectively.

The following example shows using the <xref:Microsoft.Xrm.Sdk.Entity> class to create an account record using the  <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*> method. 

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
    account["revenue"] = 5000000.00;
    // Picklist (Option set)
    account["accountcategorycode"] = new OptionSetValue(1); //Preferred customer

// Set lookup to existing record
    var USDollarCurrencyId = new Guid("547d3ece-e80c-e811-a95b-000d3af4434f");
    var USDCurrencyReference = new EntityReference("transactioncurrency", USDollarCurrencyId);
    account["transactioncurrencyid"] = USDCurrencyReference;

// Create new related tasks at the same time
    var taskList = new List<Entity>() {
            new Entity("task") { ["subject"] = "Task 1" },
            new Entity("task") { ["subject"] = "Task 2" },
            new Entity("task") { ["subject"] = "Task 3" }
        };

    EntityCollection tasks = new EntityCollection(taskList);

    account.RelatedEntities[new Relationship("Account_Tasks")] = tasks;
                
//Create the account
Guid accountid = crmSvc.Create(account);
```

### Early-bound example

When you have generated early-bound entity classes using the CrmSvcUtil.exe code generation tool as described in [Generate classes for early-bound programming using the Organization service](generate-early-bound-classes.md) you will enjoy a better experience while you write code because classes and attribute properies using the respective <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.SchemaName> and <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.SchemaName> property values are available for you to use.

> [!NOTE]
> Most of the time you use the generated properties in the same way as the late-bound style, but for certain types, such as the <xref:Microsoft.Xrm.Sdk.Money> type used for the `Revenue` property below, you will need to cast a value to a specific type.


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

// Lookup
var USDollarCurrencyId = new Guid("547d3ece-e80c-e811-a95b-000d3af4434f");
var USDCurrencyReference = new EntityReference("transactioncurrency", USDollarCurrencyId);
account.TransactionCurrencyId = USDCurrencyReference;


// Create new related tasks at the same time
    account.Account_Tasks = new List<Task>() {
        new Task() { Subject = "Task 1" },
        new Task() { Subject = "Task 2" },
        new Task() { Subject = "Task 3" }
    };

//Create the account
Guid accountid = crmSvc.Create(account);
```

### Create related entities

When you create entities using the generated early-bound classes, you can create related records in the same operation. For example, if you want to create one or more related tasks, you can use the generated property for the entity relationships to set the value to a `List` of those instances.

For example, the following can be included in the example above to create three related task records at the same time you create the account entity record.

```csharp
    account.Account_Tasks = new List<Task>() {
        new Task() { Subject = "Task 1" },
        new Task() { Subject = "Task 2" },
        new Task() { Subject = "Task 3" }
    };
```


