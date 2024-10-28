---
title: "Don't use batch request types in plug-ins and workflow activities | MicrosoftDocs"
description: "You shouldn't use ExecuteMultipleRequest or ExecuteTransactionRequest message request classes within the context of a plug-in or workflow activity."
suite: powerapps
author: jowells
ms.author: jowells
ms.reviewer: jdaly
ms.date: 02/08/2024
ms.subservice: dataverse-developer

search.audienceType: 
  - developer
---
# Don't use batch request types in plug-ins and workflow activities

**Category**: Usage, Reliability, Performance

**Impact potential**: Medium

<a name='symptoms'></a>

## Symptoms

User experiences are degraded and time out errors might occur when you use *batch request types* in plug-ins and workflow activities that occur within synchronous operations.

The following message request classes are considered *batch request types* because they perform operations on multiple records within a single request:

- <xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest>
- <xref:Microsoft.Xrm.Sdk.Messages.ExecuteTransactionRequest>
- <xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>
- <xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>
- <xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>


<a name='guidance'></a>

## Guidance

Use these batch messages in client applications to perform operations on multiple records. Don't use these messages within code that Dataverse invokes during the execution of another operation: a plug-in or workflow activity registered for a synchronous step.

More specifically, use them in the following scenarios:

- Use <xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest> to bulk load data or external processes that are intentional about executing long-running operations (greater than two minutes).

- Use <xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest> to minimize the round trips between custom client and Dataverse servers, to reduce the cumulative latency incurred.

- Use <xref:Microsoft.Xrm.Sdk.Messages.ExecuteTransactionRequest> for external clients that require the batch of operations to be committed as a single, atomic database transaction or rollback if any exception is encountered. Be aware of the potential for database blocking during the long-running transaction.

- [Use bulk operation messages](../../bulk-operations.md) (<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>, <xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>, and <xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>) for the same scenarios and to achieve a higher level of throughput.

<a name='problem'></a>

## Problematic patterns

The following example shows using <xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest> in the context of a plug-in.

> [!WARNING]
> This scenario should be avoided.

```csharp
public class ExecuteMultipleRequestInPlugin : IPlugin
{
    public void Execute(IServiceProvider serviceProvider)
    {
        IPluginExecutionContext context = (IPluginExecutionContext)serviceProvider.GetService(typeof(IPluginExecutionContext));
        IOrganizationServiceFactory factory = (IOrganizationServiceFactory)serviceProvider.GetService(typeof(IOrganizationServiceFactory));
        IOrganizationService service = factory.CreateOrganizationService(context.UserId);

        QueryExpression query = new QueryExpression("account")
        {
            ColumnSet = new ColumnSet("accountname", "createdon"),
        };

        //Obtain the results of previous QueryExpression
        EntityCollection results = service.RetrieveMultiple(query);

        if (results != null && results.Entities != null && results.Entities.Count > 0)
        {
            ExecuteMultipleRequest batch = new ExecuteMultipleRequest();
            foreach (Entity account in results.Entities)
            {
                account.Attributes["accountname"] += "_UPDATED";

                UpdateRequest updateRequest = new UpdateRequest();
                updateRequest.Target = account;

                batch.Requests.Add(updateRequest);
            }

            service.Execute(batch);
        }
        else return;

    }
}
```

This example includes usage of the type directly with the `Execute` method. The usage can be anywhere within the context of a plug-in or workflow activity execution. This might be in a method that is contained within the same or a separate class, as well. It isn't limited to being directly contained in the `Execute` method definition.

<a name='additional'></a>

## Additional information

The purpose of the `ExecuteMultiple` message is to minimize round trips between client and server over high-latency connections. Plug-ins either execute directly within the application process or in close proximity when sandbox-isolated, meaning latency is rarely an issue. Plug-in code should be focused operations that execute quickly and minimize blocking to avoid exceeding timeout thresholds and ensure a responsive system for synchronous scenarios. Submit each request directly instead of batching them and submitting as a single request.

For example: `foreach (request in requests) service.Execute(request)`

On the server side, the operations included in a batch request are executed sequentially and aren't done in parallel. This is the case even if the <xref:Microsoft.Xrm.Sdk.ExecuteMultipleSettings>.<xref:Microsoft.Xrm.Sdk.ExecuteMultipleSettings.ReturnResponses> property is set to false. Developers tend to use batch requests in this manner assuming that it allows for parallel processing. Batch requests don't accomplish this objective. 

People use <xref:Microsoft.Xrm.Sdk.Messages.ExecuteTransactionRequest> to ensure that each operation is included in a transaction. This is unnecessary within a synchronous plug-in step because the plug-in already being executed within the context of a database transaction, negating the need to use the `ExecuteTransaction` message.

<a name='seealso'></a>

### See also

[Event Framework](../../event-framework.md)<br />
[Run-time limitations](../../org-service/execute-multiple-requests.md#run-time-limitations)<br/>
[Execute multiple requests using the SDK for .NET](../../org-service/execute-multiple-requests.md)<br/>
[Execute messages in a single database transaction](../../org-service/use-executetransaction.md)


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
