---
title: "Detect duplicate data using the Organization service (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Organization service allows you to detect duplicate records in Common Data Service (CDS) for Apps to maintain integrity of data" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Detect duplicate data using the Organization service

The Organization service allows you to detect duplicate records to maintain integrity of data. For detailed information about duplicate detection feature, see . 

When creating new records or updating existing records in code, duplicate detection is not enabled by default. If you aren't sure about whether the record you are creating or updating will be a duplicate, there are several strategies you can use.

## Enable and disable duplicate detection

You can enable duplicate detection at various levels: globally, for an entity, or for specific operations. Similarly, You can disable duplicate detection globally or for an entity type by unpublishing the duplicate detection rules or by deleting the published rules. More information: [Enable and Disable duplicate detection](../enable-disable-duplicate-detection.md)

## Run Duplicate detection using UI

You can run regular duplicate detection jobs and expect it will be caught later. More information: [Run bulk system jobs to detect duplicate records](/dynamics365/customer-engagement/admin/run-bulk-system-jobs-detect-duplicate-records)

## Check before you programmatically create or update record

You can programmatically check whether an entity is a duplicate or will be a duplicate before creating or updating it by using the <xref:Microsoft.Crm.Sdk.Messages.RetrieveDuplicatesRequest> class.

```csharp
var account = new Account();
account.Name = "Sample Account";

var request = new RetrieveDuplicatesRequest()
{
    BusinessEntity = account,
    MatchingEntityName = account.LogicalName,
    PagingInfo = new PagingInfo() { PageNumber = 1, Count = 50 }
};

var response = (RetrieveDuplicatesResponse)svc.Execute(request);

if (response.DuplicateCollection.Entities.Count >= 1)
{
    Console.WriteLine("{0} Duplicate records found.", response.DuplicateCollection.Entities.Count);
}
```

### Use SuppressDuplicateDetection parameter in create/update operations to prevent duplicate records

If you want to have the platform throw an error when a new record you create is determined to be a duplicate record, or you update an existing record so that duplicate detection rules will be evaluated, you must use the <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> classes with the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*> method and apply the `SuppressDuplicateDetection` parameter set to `false`.

The following code will throw an `InvalidOperationException` exception with the message `A record was not created or updated because a duplicate of the current record already exists.` when the following are true:

- Duplicate Detection is enabled for the environment when a record is created or updated.
- The account entity is has duplicate detection enabled
- A Duplicate Detection Rule is published that checks whether the account name value is an exact match for an existing record
- There is an existing account with the name `Sample Account`

```csharp
var account = new Account();
account.Name = "Sample Account";

var request = new CreateRequest();
request.Target = account;
request.Parameters.Add("SuppressDuplicateDetection", false);

try
{
    svc.Execute(request);
}
catch (FaultException<OrganizationServiceFault> ex)
{
    switch (ex.Detail.ErrorCode)
    {
        case -2147220685:
            throw new InvalidOperationException(ex.Detail.Message);
        default:
            throw ex;
    }
}
```

### See also
- [Detect duplicate data using code](../detect-duplicate-with-code.md)
- [Sample: Use duplicate detection when creating and updating records](samples/use-duplicate-detection-when-creating-and-updating-records.md)
- [Duplicate detection messages](../duplicate-detection-messages.md)
- [Detect duplicate data so you can fix or remove it](/dynamics365/customer-engagement/admin/detect-duplicate-data)
- [Manage duplicate detection for create and update operations using the Web API](../webapi/manage-duplicate-detection-create-update.md)

