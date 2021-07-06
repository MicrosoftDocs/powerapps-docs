---
title: "Detect duplicate data using the Organization service (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Organization service allows you to detect duplicate rows in Microsoft Dataverse to maintain integrity of data" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 06/09/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Detect duplicate data using the Organization service

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

The Microsoft Dataverse Organization service allows you to detect duplicate rows to maintain integrity of data. For detailed information about detecting duplicate data using code, see [Detect duplicate data using code](../detect-duplicate-data-with-code.md). 

> [!NOTE]
> Make sure there are appropriate duplicate detection rules in place. Dataverse includes default duplicate detection rules for accounts, contacts, and leads, but not for other types of rows. If you want the system to detect duplicates for other row types, you’ll need to create a new rule. <br/>- For information on how to create a duplicate detection rule using the UI, see [Set up duplicate detection rules to keep your data clean](/dynamics365/customer-engagement/admin/set-up-duplicate-detection-rules-keep-data-clean).<br/>- For information on creating duplicate detection rules using code, see [Duplicate rule tables](../duplicaterule-entities.md)


## Use RetrieveDuplicatesRequest message to detect duplicates before you create or update row

You can programmatically check whether a table row is a duplicate or will be a duplicate before creating or updating it by using the <xref:Microsoft.Crm.Sdk.Messages.RetrieveDuplicatesRequest> class.

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
    Console.WriteLine("{0} Duplicate rows found.", response.DuplicateCollection.Entities.Count);
}
```

## Use SuppressDuplicateDetection parameter to throw errors when you create or update row

If you want to have the platform throw an error when a new row you create is determined to be a duplicate row, or you update an existing row so that duplicate detection rules will be evaluated, you must use the <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> classes with the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*> method and apply the `SuppressDuplicateDetection` parameter set to `false`.

The following code will throw an `InvalidOperationException` exception with the message `A record was not created or updated because a duplicate of the current record already exists.` when the following are true:

- Duplicate Detection is enabled for the environment when a row is created or updated.
- The account table has duplicate detection enabled
- A Duplicate Detection Rule is published that checks whether the account name value is an exact match for an existing row
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
[Detect duplicate data using the Web API](../webapi/manage-duplicate-detection-create-update.md)



[!INCLUDE[footer-include](../../../includes/footer-banner.md)]