---
title: "Execute multiple requests using the Organization service (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "ExecuteMultipleRequest message supports higher throughput bulk message passing scenarios in Microsoft Dataverse." # 115-145 characters including spaces. This abstract displays in the search result.
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

# Execute multiple requests using the Organization service

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

The primary purpose of executing multiple requests it so improve performance in high-latency environments by reducing the total volume of data that is transmitted over the network.

You can use the <xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest> message to support higher throughput bulk message passing scenarios in Microsoft Dataverse. <xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest> accepts an input collection of message <xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest.Requests>, executes each of the message requests in the order they appear in the input collection, and optionally returns a collection of <xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleResponse.Responses> containing each message’s response or the error that occurred. Each message request in the input collection is processed in a separate database transaction. <xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest> is executed by using the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*> method.  
  
In general, <xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest> behaves the same as if you executed each message request in the input request collection separately, except with better performance. Use of the <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceProxy.CallerId> parameter of the service proxy is honored and will apply to the execution of every message in the input request collection. Plug-ins and workflow activities are executed as you would expect for each message processed.  
  
Custom code in the form of plug-ins and custom workflow activities can even execute <xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest>. However, there are a few key points to keep in mind. An exception thrown by a synchronous registered plug-in is returned in the response collection item <xref:Microsoft.Xrm.Sdk.ExecuteMultipleResponseItem.Fault> parameter. If a plug-in executes within a database transaction, the plug-in executes <xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest>, and a transaction rollback is initiated, the rollback includes any data changes resulting from requests executed by <xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest>.  
  
<a name="example"></a>

## Example

 The following sample code demonstrates a single <xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest> that performs multiple create operations. Run-time execution options called *Settings* are used to control the request processing and returned results. These run-time options are discussed in the next section.  
  
```csharp

// Create an ExecuteMultipleRequest object.
ExecuteMultipleRequest requestWithResults = new ExecuteMultipleRequest()
{
    // Assign settings that define execution behavior: continue on error, return responses. 
    Settings = new ExecuteMultipleSettings()
    {
        ContinueOnError = false,
        ReturnResponses = true
    },
    // Create an empty organization request collection.
    Requests = new OrganizationRequestCollection()
};

// Create several (local, in memory) entities in a collection. 
EntityCollection input = GetCollectionOfEntitiesToCreate();

// Add a CreateRequest for each entity to the request collection.
foreach (var entity in input.Entities)
{
    CreateRequest createRequest = new CreateRequest { Target = entity };
    requestWithResults.Requests.Add(createRequest);
}

// Execute all the requests in the request collection using a single web method call.
ExecuteMultipleResponse responseWithResults =
    (ExecuteMultipleResponse)service.Execute(requestWithResults);

// Display the results returned in the responses.
foreach (var responseItem in responseWithResults.Responses)
{
    // A valid response.
    if (responseItem.Response != null)
        DisplayResponse(requestWithResults.Requests[responseItem.RequestIndex], responseItem.Response);

    // An error has occurred.
    else if (responseItem.Fault != null)
        DisplayFault(requestWithResults.Requests[responseItem.RequestIndex], 
            responseItem.RequestIndex, responseItem.Fault);
}
```
  
More information:  [Sample: Execute multiple requests](samples/execute-multiple-requests.md)
  
<a name="options"></a>

## Specify run-time execution options  

The <xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest.Settings> parameter of <xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest> applies to all of the requests in the request collection controlling execution behavior and results returned. Let’s take a look at these options in more detail.  
  
|ExecuteMultipleSettings Member|Description|  
|------------------------------------|-----------------|  
|<xref:Microsoft.Xrm.Sdk.ExecuteMultipleSettings.ContinueOnError>|When `true`, continue processing the next request in the collection even if a fault has been returned from processing the current request in the collection. When `false`, do not continue processing the next request.|  
|<xref:Microsoft.Xrm.Sdk.ExecuteMultipleSettings.ReturnResponses>|When `true`, return responses from each message request processed. When `false`, do not return responses.<br /><br /> If set to `true` and a request does not return a response, because that is its design, the <xref:Microsoft.Xrm.Sdk.ExecuteMultipleResponseItem> for that request is set to `null`.<br /><br /> However, even when `false`, the <xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleResponse.Responses> collection will not be empty if errors are returned. If errors are returned, there will be one response item in the collection for each processed request that returned a fault and <xref:Microsoft.Xrm.Sdk.ExecuteMultipleResponseItem.Fault> will be set to the actual fault that occurred.|  
  
 For example, in a request collection that contains six requests where the third and fifth request return faults, the following table indicates what the <xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleResponse.Responses> collection would contain.  
  
|Settings|Responses Collection Contents|  
|--------------|-----------------------------------|  
|ContinueOnError=true, ReturnResponses=true|6 response items: 2 have <xref:Microsoft.Xrm.Sdk.ExecuteMultipleResponseItem.Fault> set to a value.|  
|ContinueOnError=false, ReturnResponses=true|3 response items: 1 has <xref:Microsoft.Xrm.Sdk.ExecuteMultipleResponseItem.Fault> set to a value.|  
|ContinueOnError=true, ReturnResponses=false|2 response items: 2 have <xref:Microsoft.Xrm.Sdk.ExecuteMultipleResponseItem.Fault> set to a value.|  
|ContinueOnError=false, ReturnResponses=false|1 response item: 1 has <xref:Microsoft.Xrm.Sdk.ExecuteMultipleResponseItem.Fault> set to a value.|  
  
 An <xref:Microsoft.Xrm.Sdk.ExecuteMultipleResponseItem.RequestIndex> parameter in the response item indicates the sequence number, starting at zero, of the request that the response is associated with. In the previous example, the third request has a request index of 2.  
  
<a name="limitations"></a>

## Run-time limitations

There are several constraints related to the use of the <xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest> as described in the following list.  
  
-   **No recursion is allowed** <xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest> cannot invoke <xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest>. An <xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest> found in the request collection will generate a fault for that request item.  
  
-   **Maximum batch size** There is a limit to how many requests can be added to a request collection. If that limit is exceeded, a fault is thrown before the first request is ever executed. A limit of 1000 requests is typical though this maximum amount can be set for the Dataverse deployment.

> [!NOTE]
> There was once a limit on the number of concurrent ExecuteMultiple requests. The limit was 2. This was removed because service protection limits made it unnecessary. For more information: [Service Protection API Limits](../api-limits.md).

  
<a name="fault"></a>

## Handle a batch size fault

What should you do when your input request collection exceeds the maximum batch size? Your code can’t directly query the maximum batch size through the deployment web service unless it is run under an account that has the deployment administrator role.  
  
Fortunately, there is another method that you can use. When the number of requests in the input <xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest.Requests> collection exceeds the maximum batch size allowed for an organization, a fault is returned from the <xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest> call. The maximum batch size is returned in the fault. Your code can check for that value, resize the input request collection to be within the indicated limit, and re-submit the <xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest>. The following code snippet demonstrates some of this logic.  
  
```csharp
catch (FaultException<OrganizationServiceFault> fault)
{
    // Check if the maximum batch size has been exceeded. The maximum batch size is only included in the fault if
    // the input request collection count exceeds the maximum batch size.
    if (fault.Detail.ErrorDetails.Contains("MaxBatchSize"))
    {
        int maxBatchSize = Convert.ToInt32(fault.Detail.ErrorDetails["MaxBatchSize"]);
        if (maxBatchSize < requestWithResults.Requests.Count)
        {
            // Here you could reduce the size of your request collection and re-submit the ExecuteMultiple request.
            // For this sample, that only issues a few requests per batch, we will just print out some info. However,
            // this code will never be executed because the default max batch size is 1000.
            Console.WriteLine("The input request collection contains %0 requests, which exceeds the maximum allowed (%1)",
                requestWithResults.Requests.Count, maxBatchSize);
        }
    }
    // Re-throw so Main() can process the fault.
    throw;
}
```

### See also

[Use messages with the Organization service](use-messages.md)<br />
[Use ExecuteAsync](use-executeAsync.md)<br />
[Use ExecuteTransaction](use-executetransaction.md)<br />

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
