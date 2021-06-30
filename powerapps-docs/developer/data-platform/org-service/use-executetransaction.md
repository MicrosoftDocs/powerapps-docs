---
title: "Execute messages in a single database transaction (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "You can execute two or more organization service requests in a single database transaction using the ExecuteTransactionRequest message request." # 115-145 characters including spaces. This abstract displays in the search result.
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

# Execute messages in a single database transaction

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

It is a common requirement in business applications to coordinate changes of multiple table rows in the system so that either all the data changes succeed, or none of them do. In database terms, this is known as executing multiple operations in a single transaction with the ability to roll back all data changes should any one operation fail.  
  
 You can execute two or more organization service requests in a single database transaction using the <xref:Microsoft.Xrm.Sdk.Messages.ExecuteTransactionRequest> message request. To use this message, populate the <xref:Microsoft.Xrm.Sdk.Messages.ExecuteTransactionRequest.Requests> collection with two or more organization requests that are to be executed in the transaction. Set <xref:Microsoft.Xrm.Sdk.Messages.ExecuteTransactionRequest.ReturnResponses> to `true` if you want to get back a collection of responses, one for each message request executed, in the <xref:Microsoft.Xrm.Sdk.Messages.ExecuteTransactionResponse.Responses> collection. Message requests in the <xref:Microsoft.Xrm.Sdk.Messages.ExecuteTransactionRequest.Requests> collection are executed in order as they appear in the collection, where the element at index 0 is executed first. This same order is preserved in the <xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleResponse.Responses> collection.  
  
 Should any one of the requests fail and the transaction is rolled back, any data changes completed during the transaction are undone. In addition, a <xref:Microsoft.Xrm.Sdk.ExecuteTransactionFault> is returned identifying the index into the request collection of the request message that caused the fault.  
  
 An <xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest> may contain one or more <xref:Microsoft.Xrm.Sdk.Messages.ExecuteTransactionRequest> instances.  An <xref:Microsoft.Xrm.Sdk.Messages.ExecuteTransactionRequest> instance may not contain a <xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest> or <xref:Microsoft.Xrm.Sdk.Messages.ExecuteTransactionRequest>. For more information on <xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest>, see [Execute multiple requests using the Organization service](execute-multiple-requests.md). 

## Example

This example uses a single web method call to execute all message requests in a collection as part of a single database transaction. Settings to alter the execution behavior are also shown.

```csharp
// Create an ExecuteTransactionRequest object.
var requestToCreateRecords = new ExecuteTransactionRequest()
{
// Create an empty organization request collection.
Requests = new OrganizationRequestCollection(),
ReturnResponses = true
};

// Create several (local, in memory) entities in a collection. 
var input = new EntityCollection()
{
EntityName = Account.EntityLogicalName,
Entities = {
            new Account { Name = "ExecuteTransaction Example Account 1" },
            new Account { Name = "ExecuteTransaction Example Account 2" },
            new Account { Name = "ExecuteTransaction Example Account 3" },
            new Account { Name = "ExecuteTransaction Example Account 4" },
            new Account { Name = "ExecuteTransaction Example Account 5" }
        }
};

// Add a CreateRequest for each entity to the request collection.
foreach (var entity in input.Entities)
{
CreateRequest createRequest = new CreateRequest { Target = entity };
requestToCreateRecords.Requests.Add(createRequest);
}

// Execute all the requests in the request collection using a single web method call.
try
{
var responseForCreateRecords =
    (ExecuteTransactionResponse)svc.Execute(requestToCreateRecords);

int i = 0;
// Display the results returned in the responses.
foreach (var responseItem in responseForCreateRecords.Responses)
{
    if (responseItem != null)
    Console.WriteLine("Created " + ((Account)requestToCreateRecords.Requests[i].Parameters["Target"]).Name
        + " with account id as " + responseItem.Results["id"].ToString());
    i++;
}
}
catch (FaultException<OrganizationServiceFault> ex)
{
Console.WriteLine("Create request failed for the account{0} and the reason being: {1}",
    ((ExecuteTransactionFault)(ex.Detail)).FaultedRequestIndex + 1, ex.Detail.Message);
throw;
}
```

### See also

[Use messages with the Organization service](use-messages.md)<br />
[Execute multiple requests using the Organization service](execute-multiple-requests.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]