---
title: Use UpsertMultiple (preview)
description: Learn how to use UpsertMultiple to create or update multiple rows of data in a Microsoft Dataverse table. 
ms.date: 11/11/2023
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
ms.topic: how-to
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
ms.custom: bap-template
---

# Use UpsertMultiple (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

> [!IMPORTANT]
> This is a preview feature.
>
> [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]

Use `Upsert` to integrate data with external sources when you don't know whether the table exists in Dataverse or not.
Upsert operations frequently depend on alternate keys to identify records. Use `UpsertMultiple` to perform `Upsert` operations in bulk.

## [SDK for .NET](#tab/sdk)

Uses the [UpsertMultipleRequest class](xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest).

This static `UpsertMultipleExample` method depends on a `samples_bankaccount`table that has a string column named 
`samples_accountname` configured as an alternate key. It also has a string column named `samples_description`. This code uses the [Entity constructor that sets the keyName and keyValue](use-alternate-key-reference-record.md#using-the-entity-class) to specify the alternate key value.

```csharp
/// <summary>
/// Demonstrates using UpsertMultiple with alternate key values
/// </summary>
/// <param name="service">The authenticated IOrganizationService instance</param>
static void UpsertMultipleExample(IOrganizationService service)
{
    var tableLogicalName = "samples_bankaccount";
    // samples_accountname string column is configued as an alternate key
    // for the samples_bankaccount table
    var altKeyColumnLogicalName = "samples_accountname";

    // Create one record to update with upsert
    service.Create(new Entity(tableLogicalName)
    {
        Attributes =
        {
            {altKeyColumnLogicalName, "Record For Update"},
            {"samples_description","A record to update using Upsert" }
        }
    });

    // Using the Entity constructor to specify alternate key
    Entity toUpdate = new(
            entityName: tableLogicalName,
            keyName: altKeyColumnLogicalName,
            // Same alternate key value as created record.
            keyValue: "Record For Update");
    toUpdate["samples_description"] = "Updated using Upsert";

    Entity toCreate = new(
        entityName: tableLogicalName,
        keyName: altKeyColumnLogicalName,
        keyValue: "Record For Create");
    toCreate["samples_description"] = "A record to create using Upsert";

    // Add the records to a collection
    EntityCollection records = new()
    {
        EntityName = tableLogicalName,
        Entities = { toUpdate, toCreate }
    };

    // Send the request
    UpsertMultipleRequest request = new()
    {
        Targets = records
    };

    var response = (UpsertMultipleResponse)service.Execute(request);

    // Process the responses:
    foreach (UpsertResponse item in response.Results)
    {
        Console.WriteLine($"Record {(item.RecordCreated ? "Created" : "Updated")}");
    }
}
```

**Output:**

```
Record Updated
Record Created
```

## [Web API](#tab/webapi)

`UpsertMultiple` is currently available only using the SDK for .NET.

---

## Availability

Upsert multiple is available for tables that support `CreateMultiple` and `UpdateMultiple`. This includes all elastic tables. The queries found in [Availability with standard tables](bulk-operations.md#availability-with-standard-tables) will not return results for `UpsertMultiple`.

## Examples

The following code samples show how to use bulk operation messages. You can download the samples from [github.com/microsoft/PowerApps-Samples](https://github.com/microsoft/PowerApps-Samples):

[Sample: SDK for .NET Use bulk operations](org-service/samples/create-update-multiple.md)

> [!NOTE]
> Look for the [UpsertMultiple project](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/orgsvc/C%23-NETCore/BulkOperations/UpsertMultiple/README.md)

### See also

[Use bulk operation messages](bulk-operations.md)   
[Elastic tables (preview)](elastic-tables.md)  
[Sample: SDK for .NET Use bulk operations](org-service/samples/create-update-multiple.md)   