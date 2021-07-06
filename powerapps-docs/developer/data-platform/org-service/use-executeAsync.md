---
title: "Use ExecuteAsync to execute messages asynchronously  (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "You can use the ExecuteAsync message to import solutions asynchronously." # 115-145 characters including spaces. This abstract displays in the search result.
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

# Use ExecuteAsync to execute messages asynchronously

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

Except for a few operations described below, all data operations using the SDK assembly request classes are synchronous.

Importing a solution is one operation which can require considerable resources, so there is an option to execute this operation asynchronously using the <xref:Microsoft.Xrm.Sdk.Messages.ExecuteAsyncRequest> request class. The <xref:Microsoft.Crm.Sdk.Messages.DeleteAndPromoteRequest> request class performs similar resource intensive operations.

Importing a solution asynchronously improves system performance by postponing message execution until some later time when the server load may be less. Interactive users do not have to wait for the target message to execute before they can continue. This is especially useful when importing solutions which may take a few minutes or more to execute.  

Merging rows with a large number of related activities or other table types can also take a long time to update all the related rows, so executing these in the background can improve the user experience.
  
> [!NOTE]
> <xref:Microsoft.Crm.Sdk.Messages.ImportSolutionRequest>, <xref:Microsoft.Crm.Sdk.Messages.DeleteAndPromoteRequest>, and <xref:Microsoft.Crm.Sdk.Messages.MergeRequest> are the only request classes that can be used with <xref:Microsoft.Xrm.Sdk.Messages.ExecuteAsyncRequest>.
  
Use the <xref:Microsoft.Xrm.Sdk.Messages.ExecuteAsyncRequest> request class to execute a message asynchronously. You configure the request and pass the request instance as an argument to <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*>. <xref:Microsoft.Xrm.Sdk.Messages.ExecuteAsyncResponse> returns with the ID of the asynchronous job. You can (optionally) query the job using the ID to find out its current state.  
  
You can use the <xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest> request class to queue multiple solutions to be imported asynchronously. To do this, add one or more `ExecuteAsync` message requests to an `ExecuteMultiple` message request. Due to throttling restrictions that improve overall system performance, only one message running asynchronously is allowed to execute at a time for each organization.

For more information about the `ExecuteMultiple` message, see [Execute multiple requests using the Organization service](execute-multiple-requests.md).  

## Example

The following example shows how to use the <xref:Microsoft.Xrm.Sdk.Messages.ExecuteAsyncRequest> message request class with the <xref:Microsoft.Crm.Sdk.Messages.ImportSolutionRequest> message request class.

```csharp
string ManagedSolutionLocation = @"C:\temp\ManagedSolutionForImportExample.zip";

byte[] fileBytes = File.ReadAllBytes(ManagedSolutionLocation);

ImportSolutionRequest impSolReq = new ImportSolutionRequest()
{
CustomizationFile = fileBytes
};

ExecuteAsyncRequest asyncReq = new ExecuteAsyncRequest()
{
Request = impSolReq
};

var asyncResp = (ExecuteAsyncResponse)svc.Execute(asyncReq);

Guid asyncOperationId = asyncResp.AsyncJobId;
```

You can then poll the [AsyncOperation](../reference/entities/asyncoperation.md) table using the `asyncOperationId` value for the system job with the matching [AsyncOperationId](../reference/entities/asyncoperation.md#BKMK_AsyncOperationId) to detect when the [StatusCode](../reference/entities/asyncoperation.md#BKMK_StatusCode) value indicates whether the operation has succeeded (30), failed (31), or was cancelled (32).

### See Also

[Use messages with the Organization service](use-messages.md)<br />
[Use ExecuteTransaction](use-executetransaction.md)<br />
[Execute multiple requests using the Organization service](execute-multiple-requests.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]