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
# Update and Delete entities

<!-- 
Adding parity with Web API topics

include information from https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/org-service/perform-specialized-operations-using-update 

https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/org-service/use-early-bound-entity-classes-create-update-delete
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/org-service/manage-duplicate-detection-create-update

-->

This topic will include examples using both late-bound and early-bound programming styles. More information: [Early-bound and Late-bound programming using the Organization service](early-bound-programming.md)

<!-- TODO make this an include? -->
Each of the examples uses a `svc` variable that represents an instance of a class that implements the methods in the <xref:Microsoft.Xrm.Sdk.IOrganizationService> interface. For information about the classes that support this interface see [IOrganizationService Interface](iorganizationservice-interface.md).

> [!IMPORTANT]
>  When updating an entity, only include the attributes you are changing. Simply updating the attributes of an entity that you previously retrieved will update each attribute even though the value is unchanged. This can cause system events that can trigger business logic that expects that the values have actually changed. This can also cause attributes to appear to have been updated in auditing data when in fact they haven’t actually changed. 
>
> You should create a new entity instance, set the id attribute and any attribute values you are changing, and use that entity instance to update the record.

## Basic update

Both of the examples below uses the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*> method to set attribute values for an entity that was previously retrieved.

Use the <xref:Microsoft.Xrm.Sdk.Entity>.<xref:Microsoft.Xrm.Sdk.Entity.Id> property to transfer the unique identifier value of the retrieved entity to the entity instance used to perform the update operation.

### Late-bound example

The following example shows using the <xref:Microsoft.Xrm.Sdk.Entity> class to create an account record using the  <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*> method. 

```csharp
var retrievedAccount = new Entity("account", new Guid("a976763a-ba1c-e811-a954-000d3af451d6"));

//Use Entity class with entity logical name
var account = new Entity("account");
account.Id = retrievedAccount.Id;
// set attribute values
// Boolean (Two option)
account["creditonhold"] = true;
// DateTime
account["lastonholdtime"] = DateTime.Now;
// Double
account["address1_latitude"] = 47.642311;
account["address1_longitude"] = -122.136841;
// Int
account["numberofemployees"] = 400;
// Money
account["revenue"] = new Money(new Decimal(2000000.00));
// Picklist (Option set)
account["accountcategorycode"] = new OptionSetValue(2); //Standard customer

//Update the account
svc.Update(account);
```

### Early-bound example

The following example shows using the generated `Account` class to update an account record using the  <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*> method.

```csharp
var retrievedAccount = new Account()
{ Id = new Guid("a976763a-ba1c-e811-a954-000d3af451d6") };

var account = new Account();
account.Id = retrievedAccount.Id;
// set attribute values
// Boolean (Two option)
account.CreditOnHold = true;
// DateTime
account.LastOnHoldTime = DateTime.Now;
// Double
account.Address1_Latitude = 47.642311;
account.Address1_Longitude = -122.136841;
// Int
account.NumberOfEmployees = 400;
// Money
account.Revenue = new Money(new Decimal(2000000.00));
// Picklist (Option set)
account.AccountCategoryCode = new OptionSetValue(2); //Standard customer

//Update the account
svc.Update(account);
```

## Use the UpdateRequest class

Instead of using the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*> method, you can use either the late-bound <xref:Microsoft.Xrm.Sdk.Entity> class or the generated early-bound entity classes with the <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> class by setting the entity instance to the <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest.Target> property and then using the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*> method.

> [!NOTE]
> The <xref:Microsoft.Xrm.Sdk.Messages.UpdateResponse> has no properties. While it is returned by the <xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*> method, it isn't necessary to refer to it.
 
```csharp
var request = new UpdateRequest()
{ Target = account };
svc.Execute(request);
```
### When to use the UpdateRequest class

You must use the <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> class if you want to pass optional parameters. There are two cases where you might need special parameters.
 - When you want duplicate detection rules to be applied. More information: [Check for Duplicate records](entity-operations-create.md#check-for-duplicate-records)
 - When you are creating an entity record that represents a solution component, such as a [WebResource](../reference/entities/webresource.md) and want to associate it with a specific solution. In this case, you would include the value of the [Solution.UniqueName](../reference/entities/solution.md#BKMK_UniqueName) using the `SolutionUniqueName` parameter. More information: [Use messages with the Organization service](use-messages.md)

You must also use the <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> class if you want to specify an optimistic concurrency behavior. More information: [Optimistic concurrency behavior](#optimistic-concurrency-behavior)

## Update related entities in one operation

In a similar manner to how you can [Create related entities in one operation](entity-operations-create.md#create-related-entities-in-one-operation), you can also update related entities.

To do this, you have to retrieve an entity with the related records so that you can access the id values. More information: [Retrieve with related records](entity-operations-retrieve.md#retrieve-with-related-records)

> [!IMPORTANT]
> Updates to records are made in a specific order. First, primary entities are processed, and then related entities are processed. If a change is made by the primary entity for a lookup or related entity attribute, and then a related entity updates the same attribute, the related entity value is retained. In general, a lookup attribute value and its equivalent in the `RelatedEntities` for the same relationship should not be used at the same time.

### Late-bound example

<!-- TODO -->

### Early-bound example

```csharp
var account = new Account();
account.Id = retrievedAccount.Id;

//Update the account
account.Name = "New Account name";

//Update the email address for the primary contact of the the account
account.account_primary_contact = new Contact
{ Id = retrievedAccount.PrimaryContactId.Id, EMailAddress1 = "someone_a@example.com" };

// Find related Tasks that need to be updated
List<Task> tasksToUpdate = retrievedAccount.Account_Tasks
    .Where(t => t.Subject.Equals("Example Task")).ToList();

// A list to put the updated tasks
List<Task> updatedTasks = new List<Task>();

//Fill the list of updated tasks based on the tasks that need to but updated
tasksToUpdate.ForEach(t =>
{
    updatedTasks
    .Add(new Task() {
        ActivityId = t.ActivityId,
        Subject = "Updated Subject"
    });

});

//Set the updated tasks to the collection
account.Account_Tasks = updatedTasks;

//Update the account and related contact and tasks
svc.Update(account);
```


## Check for Duplicate records

When updating an entity you may change the values so that the record represents a duplicate of another record. More information: [Check for Duplicate records](entity-operations-create.md#check-for-duplicate-records)

## Use Upsert

<!-- TODO -->

## Delete

The <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*> method simply requires the logical name of the entity and the unique identifier. Regardless of whether you are using late-bound <xref:Microsoft.Xrm.Sdk.Entity> class or a generated early-bound entity class, you can use the following syntax for a delete operation by passing the <xref:Microsoft.Xrm.Sdk.Entity>.<xref:Microsoft.Xrm.Sdk.Entity.LogicalName> and <xref:Microsoft.Xrm.Sdk.Entity>.<xref:Microsoft.Xrm.Sdk.Entity.Id> properties.

```csharp
svc.Delete(retrievedEntity.LogicalName, retrievedEntity.Id);
```
Or you can use the values:
```csharp
svc.Delete("account", new Guid("e5fa5509-2582-e811-a95e-000d3af40ae7"));
```
> [!IMPORTANT]
> Delete operations can initiate cascading operations that may delete child records to maintain data integity depending on logic defined for the relationships in the environment. More information: [Entity relationship behavior](../../../maker/common-data-service/entity-relationship-behavior.md)

## Use the DeleteRequest class

You can use the <xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> instead of the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*> method, but it is only required when you want to specify optimistic concurrency behavior.

```csharp
var retrievedEntity = new Entity("account")
{
    Id = new Guid("c81ffd82-cd82-e811-a95c-000d3af49bf8"),
    RowVersion = "986335"

};

var request = new DeleteRequest()
{
    Target = retrievedEntity.ToEntityReference(),
    ConcurrencyBehavior = ConcurrencyBehavior.IfRowVersionMatches
};

svc.Execute(request);
```

## Optimistic concurrency behavior

You can specify the optimistic concurrency behavior for the operation by setting the `ConcurrencyBehavior` property of the <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> classes.

The logic to update or delete the record may be based on stale data. If the current data is different because it has changed since it was retrieved, optimistic concurrency provides a way to cancel an update or delete operation so you might retrieve it again and use the current data to determine whether to proceed.

To determine whether the entity has been changed, you don't need to compare all the values, you can use the <xref:Microsoft.Xrm.Sdk.Entity.RowVersion> property to see if it has changed.

The following example will succeed only when:
- The `RowVersion` of the entity in the database equals `986323`
- The account entity is enabled for optimistic concurrency (<xref href="Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsOptimisticConcurrencyEnabled?text=EntityMetadata.IsOptimisticConcurrencyEnabled" /> is `true`)
- The `RowVersion` property is set on the entity passed with the request.

If the `RowVersion` doesn't match, an error with the message `The version of the existing record doesn't match the RowVersion property provided.` will occur.

```csharp
var retrievedAccount = new Account()
{   
    Id = new Guid("a976763a-ba1c-e811-a954-000d3af451d6"), 
    RowVersion = "986323" 
};

var account = new Account();
account.Id = retrievedAccount.Id;
account.RowVersion = retrievedAccount.RowVersion;

// set attribute values
account.CreditOnHold = true;

//Update the account
var request = new UpdateRequest()
{ 
    Target = account,
    ConcurrencyBehavior = ConcurrencyBehavior.IfRowVersionMatches 
};

try
{
    svc.Execute(request);
}
catch (FaultException<OrganizationServiceFault> ex)
{
    switch (ex.Detail.ErrorCode)
    {
        case -2147088254: // ConcurrencyVersionMismatch 
        case -2147088253: // OptimisticConcurrencyNotEnabled 
            throw new InvalidOperationException(ex.Detail.Message);                       
        case -2147088243: // ConcurrencyVersionNotProvided
            throw new ArgumentNullException(ex.Detail.Message);
        default:
            throw ex;
    }
}
```

More information: 
- [Optimistic Concurrency](../optimistic-concurrency.md)
- <xref href="Microsoft.Xrm.Sdk.ConcurrencyBehavior?text=ConcurrencyBehavior Enum" />

## Legacy update messages

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/org-service/perform-specialized-operations-using-update -->
