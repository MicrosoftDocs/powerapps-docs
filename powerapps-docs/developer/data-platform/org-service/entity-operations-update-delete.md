---
title: "Update and delete table rows using the Organization Service (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to update and delete table rows using the organization service." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 06/04/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Update and delete table rows using the Organization Service

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

This topic will include examples using both late-bound and early-bound programming styles. More information: [Early-bound and late-bound programming using the Organization service](early-bound-programming.md)

Each of the examples uses a `svc` variable that represents an instance of a class that implements the methods in the <xref:Microsoft.Xrm.Sdk.IOrganizationService> interface. For information about the classes that support this interface see [IOrganizationService Interface](iorganizationservice-interface.md).

> [!IMPORTANT]
> When updating a table row, only include the columns you are changing. Simply updating the columns of a table row that you previously retrieved will update each column even though the value is unchanged. This can cause system events that can trigger business logic that expects that the values have actually changed. This can also cause columns to appear to have been updated in auditing data when in fact they haven’t actually changed.
>
> You should create a new `Entity` instance, set the id attribute and any attribute values you are changing, and use that entity instance to update the table row.

> [!NOTE]
> The column definition includes a `RequiredLevel` property. When this is set to `SystemRequired`, you cannot set these columns to a null value. If you attempt this you will get error code  `-2147220989` with the message `Attribute: <attribute name> cannot be set to NULL`.
> 
> More information: [Column (attribute) requirement level](../entity-attribute-metadata.md#column-requirement-level)

## Basic update

Both of the examples below uses the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*> method to set column values for a table row that was previously retrieved.

Use the <xref:Microsoft.Xrm.Sdk.Entity>.<xref:Microsoft.Xrm.Sdk.Entity.Id> property to transfer the unique identifier value of the retrieved row to the entity instance used to perform the update operation.

> [!NOTE]
> If you attempt to update a row without a primary key value you will get the error: `Entity Id must be specified for Update`.
> 
> If you don't have a primary key value, you can also update rows using alternate keys. More information: [Update with Alternate Key](#update-with-alternate-key)

### Late-bound example

The following example shows using the <xref:Microsoft.Xrm.Sdk.Entity> class to create an account using the  <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*> method. 

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

The following example shows using the generated `Account` class to update an account row using the  <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*> method.

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
 - When you are creating a table row that represents a solution component, such as a [WebResource](../reference/entities/webresource.md) and want to associate it with a specific solution. In this case, you would include the value of the [Solution.UniqueName](../reference/entities/solution.md#BKMK_UniqueName) using the `SolutionUniqueName` parameter. More information: [Use messages with the Organization service](use-messages.md)

You must also use the <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> class if you want to specify an optimistic concurrency behavior. More information: [Optimistic concurrency behavior](#optimistic-concurrency-behavior)

## Update related entities in one operation

In a similar manner to how you can [Create related table rows in one operation](entity-operations-create.md#create-related-entities-in-one-operation), you can also update related table rows.

To do this, you have to retrieve a row with the related rows so that you can access the id values. More information: [Retrieve with related rows](entity-operations-retrieve.md#retrieve-with-related-rows)

> [!IMPORTANT]
> Updates to rows are made in a specific order. First, primary table rows are processed, and then related table rows are processed. If a change is made by the primary row for a lookup or related row column, and then a related row updates the same column, the related row value is retained. In general, a lookup column value and its equivalent in the <xref:Microsoft.Xrm.Sdk.Entity>.<xref:Microsoft.Xrm.Sdk.Entity.RelatedEntities> for the same relationship should not be used at the same time.

### Late-bound example


```csharp
var account = new Entity("account");
account.Id = retrievedAccount.Id;

//Define relationships
var primaryContactRelationship = new Relationship("account_primary_contact");
var AccountTasksRelationship = new Relationship("Account_Tasks");

//Update the account name
account["name"] = "New Account name";

//Update the email address for the primary contact of the account
var contact = new Entity("contact");
contact.Id = retrievedAccount.RelatedEntities[primaryContactRelationship]
.Entities.FirstOrDefault().Id;
contact["emailaddress1"] = "someone_a@example.com";

List<Entity> primaryContacts = new List<Entity>();
primaryContacts.Add(contact);  
account.RelatedEntities.Add(primaryContactRelationship, new EntityCollection(primaryContacts));

// Find related Tasks that need to be updated
List<Entity> tasksToUpdate = retrievedAccount
.RelatedEntities[AccountTasksRelationship].Entities
.Where(t => t["subject"].Equals("Example Task")).ToList();

// A list to put the updated tasks
List<Entity> updatedTasks = new List<Entity>();

//Fill the list of updated tasks based on the tasks that need to but updated
tasksToUpdate.ForEach(t => {
var updatedTask = new Entity("task");
updatedTask.Id = t.Id;
updatedTask["subject"] = "Updated Subject";

updatedTasks.Add(updatedTask);
});

//Set the updated tasks to the collection
account.RelatedEntities.Add(AccountTasksRelationship, new EntityCollection(updatedTasks));

//Update the account and related contact and tasks
svc.Update(account);
```


### Early-bound example

```csharp
var account = new Account();
account.Id = retrievedAccount.Id;

//Update the account
account.Name = "New Account name";

//Update the email address for the primary contact of the account
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

## Check for duplicate records

When updating a table row you may change the values so that the row represents a duplicate of another row. More information: [Detect duplicate data using the Organization service](detect-duplicate-data.md)

## Update with Alternate Key

If you have an alternate key defined for a table, you can use that in place of the primary key to update a row. You cannot use the early-bound class to specify the alternate key. You must use the [Entity(String, KeyAttributeCollection)](/dotnet/api/microsoft.xrm.sdk.entity.-ctor#Microsoft_Xrm_Sdk_Entity__ctor_System_String_Microsoft_Xrm_Sdk_KeyAttributeCollection_) constructor to specify the alternate key.

If you want to use early bound types, you can convert the <xref:Microsoft.Xrm.Sdk.Entity> to an early bound class using the <xref:Microsoft.Xrm.Sdk.Entity.ToEntity``1> method.

The following example shows how to update an `Account` using an alternate key defined for the `accountnumber` column (attribute).

> [!IMPORTANT]
> By default there are no alternate keys defined for any tables. This method can only be used when the environment is configured to define an alternate key for a table.

```csharp
var accountNumberKey = new KeyAttributeCollection();
accountNumberKey.Add(new KeyValuePair<string, object>("accountnumber", "123456"));

Account exampleAccount = new Entity("account", accountNumberKey).ToEntity<Account>();
exampleAccount.Name = "New Account Name";
svc.Update(exampleAccount);
```

More information: 
- [Work with alternate keys](../define-alternate-keys-entity.md)
- [Use an alternate key to create a row](../use-alternate-key-create-record.md)

## Update and delete documents in storage partitions

If you are updating or deleting table data stored in partitions be sure to specify the partition key when accessing that data. More information: [Improve performance when accessing table data using storage partitions](azure-storage-partitioning-sdk.md)

## Use Upsert

Typically in data integration scenarios you will need to create or update data in Microsoft Dataverse from other sources. Dataverse may already have records with the same unique identifier, which may be an alternate key. If a table row exists, you want to update it. If it doesn't exist, you want to create it so that the data being added is synchronized with the source data. This is when you want to use upsert.

The following example uses <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest> twice. The first time the account row is created, and the second time it is updated because it has an `accountnumber` value and there is an alternate key using that column (attrbute).

For both calls, the <xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse>.<xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse.RecordCreated> property indicates whether the operation created a row or not.

```csharp
// This environment has an alternate key set for the accountnumber attribute.

//Instantiate account entity with accountnumber value
var account = new Entity("account", "accountnumber", "0003");
account["name"] = "New Account";

//Use Upsert the first time
UpsertRequest request1 = new UpsertRequest() {
Target = account
};

//The new entity is created
var response1 = (UpsertResponse)svc.Execute(request1);
Console.WriteLine("Record Created: {0}",response1.RecordCreated); //true

//Update the name of the existing account entity
account["name"] = "Updated Account";

//Use Upsert for the second time
UpsertRequest request2 = new UpsertRequest()
{
Target = account
};

//The existing entity is updated.
var response2 = (UpsertResponse)svc.Execute(request1);
Console.WriteLine("Record Created: {0}", response2.RecordCreated); //false
```
More information: [Use Upsert to insert or update a record](../use-upsert-insert-update-record.md)

## Delete

The <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*> method simply requires the logical name of the table and the unique identifier. Regardless of whether you are using late-bound <xref:Microsoft.Xrm.Sdk.Entity> class or a generated early-bound class, you can use the following syntax for a delete operation by passing the <xref:Microsoft.Xrm.Sdk.Entity>.<xref:Microsoft.Xrm.Sdk.Entity.LogicalName> and <xref:Microsoft.Xrm.Sdk.Entity>.<xref:Microsoft.Xrm.Sdk.Entity.Id> properties.

```csharp
svc.Delete(retrievedEntity.LogicalName, retrievedEntity.Id);
```
Or you can use the values:
```csharp
svc.Delete("account", new Guid("e5fa5509-2582-e811-a95e-000d3af40ae7"));
```
> [!IMPORTANT]
> Delete operations can initiate cascading operations that may delete child rows to maintain data integrity depending on logic defined for the relationships in the environment. More information: [Table relationship behavior](/powerapps/developer/data-platform/org-service/create-edit-entity-relationships#entity-relationship-behavior)

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

The logic to update or delete the row may be based on stale data. If the current data is different because it has changed since it was retrieved, optimistic concurrency provides a way to cancel an update or delete operation so you might retrieve it again and use the current data to determine whether to proceed.

To determine whether the row has been changed, you don't need to compare all the values, you can use the <xref:Microsoft.Xrm.Sdk.Entity.RowVersion> property to see if it has changed.

The following example will succeed only when:
- The `RowVersion` of the row in the database equals `986323`
- The account row is enabled for optimistic concurrency (<xref href="Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsOptimisticConcurrencyEnabled?text=EntityMetadata.IsOptimisticConcurrencyEnabled" /> is `true`)
- The `RowVersion` property is set on the row passed with the request.

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
- <xref href="Microsoft.Xrm.Sdk.ConcurrencyBehavior?text=ConcurrencyBehavior Enum"  />

## Legacy update messages

<!-- https://docs.microsoft.com/dynamics365/customer-engagement/developer/org-service/perform-specialized-operations-using-update -->

There are several deprecated specialized messages that perform update operations. In earlier versions it was required to use these messages, but now the same operations should be performed using <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*> or <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> class with <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*>

[!INCLUDE [cc-legacy-update-messages](../includes/cc-legacy-update-messages.md)]

More information: [Behavior of specialized update operations](../special-update-operation-behavior.md)

### See also

[Create table rows using the Organization Service](entity-operations-create.md)<br />
[Retrieve a table row using the Organization Service](entity-operations-retrieve.md)<br />
[Associate and disassociate table rows using the Organization Service](entity-operations-associate-disassociate.md)<br />

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]