---
title: "Troubleshoot plug-ins (Microsoft Dataverse for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn what plug-in errors can occur and how to fix them." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/16/2021
ms.reviewer: "pehecke"
ms.service: "powerapps"
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
# Troubleshoot plug-ins

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

This topic contains information about errors that can occur due to plug-in execution and how to fix them.

## Error: No Sandbox Worker processes are currently available

Error Code: `-2147204723`<br />
Error Message: `The plug-in execution failed because no Sandbox Worker processes are currently available. Please try again.`

This error simply means that the worker process running your plug-in code crashed. The reason it crashed may be your plug-in, but it could also be another plug-in running concurrently for your organization. Because the process crashed, we can’t extract any more specific information about why it crashed. But after examining data from the crash dumps after the fact, we have found that this usually happens for one of the 4 reasons below:

- Unhandled exception in plugin
- Stack Overflow error in plug-in
- Using threads to queue work with no try/catch in thread delegate
- Worker process reaches memory limit

### Unhandled exception in plugin

As mentioned in [Handle exceptions in plug-ins](handle-exceptions.md), when you write a plug-in you should try to anticipate which operations may fail and wrap them in a try-catch block. When any errors occur, you should use the <xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException> to gracefully terminate the operation with an error meaningful to the user.

A common scenario for this is when using a the [HttpClient.SendAsync Method](/dotnet/api/system.net.http.httpclient.sendasync?view=netframework-4.6.2) or [HttpClient.GetAsync Method](/dotnet/api/system.net.http.httpclient.getasync?view=netframework-4.6.2) which are asynchronous operations that returns a [Task](/dotnet/api/system.threading.tasks.task-1?view=netframework-4.6.2). To make this work in a plug-in where code needs to be synchronous, people may use the [Task<TResult>.Result Property](/dotnet/api/system.threading.tasks.task-1.result?view=netframework-4.6.2). When an error occurs, this returns an [AggregateException](/dotnet/api/system.aggregateexception?view=netframework-4.6.2) which consolidates multiple failures into a single exception which can be difficult to handle. A better design is to use [Task<TResult>.ConfigureAwait(false)](/dotnet/api/system.threading.tasks.task-1.configureawait?view=netframework-4.6.2).[GetAwaiter()](/dotnet/api/system.aggregateexception?view=netframework-4.6.2).[GetResult()](/dotnet/api/system.runtime.compilerservices.taskawaiter-1.getresult?view=netframework-4.6.2) because it propagates the results as the specific error that caused the failure.

The following example shows the correct way to manage the exception and an outbound call using [HttpClient.GetAsync Method](/dotnet/api/system.net.http.httpclient.getasync?view=netframework-4.6.2). This plug-in will attempt to get the response text for a Url set in the unsecure config for a step registered for it.

```csharp
using Microsoft.Xrm.Sdk;
using System;
using System.Net.Http;

namespace ErrorRepro
{
    public class AsyncError : IPlugin
    {
        private readonly string webAddress;

        public AsyncError(string unsecureConfig)
        {
            if (string.IsNullOrEmpty(unsecureConfig)) {
                throw new InvalidPluginExecutionException("The ErrorRepro.AsyncError plug-in requires that a Url be set in the unsecure configuration for the step registration.");
            }
            webAddress = unsecureConfig;

        }

        public void Execute(IServiceProvider serviceProvider)
        {
            ITracingService tracingService =
            (ITracingService)serviceProvider.GetService(typeof(ITracingService));

            tracingService.Trace($"Starting ErrorRepro.AsyncError");
            tracingService.Trace($"Sending web request to {webAddress}");

            try
            {
                string responseText = GetWebResponse(webAddress, tracingService);
                tracingService.Trace($"Result: {responseText.Substring(0, 100)}");
            }
            catch (Exception ex)
            {
                tracingService.Trace($"Error: ErrorRepro.AsyncError {ex.Message}");
                throw new InvalidPluginExecutionException(ex.Message);
            }
            tracingService.Trace($"Ending ErrorRepro.AsyncError");
        }

        //Gets the text response of an outbound web service call
        public string GetWebResponse(string webAddress, ITracingService tracingService)
        {
            try
            {
                using (HttpClient client = new HttpClient())
                {
                    client.Timeout = TimeSpan.FromMilliseconds(15000); //15 seconds
                    client.DefaultRequestHeaders.ConnectionClose = true; //Set KeepAlive to false

                    HttpResponseMessage response = client.GetAsync(webAddress).ConfigureAwait(false).GetAwaiter().GetResult(); //Make sure it is synchronous
                    response.EnsureSuccessStatusCode();

                    tracingService.Trace($"ErrorRepro.AsyncError.GetWebResponse succeeded.");

                    string responseContent = response.Content.ReadAsStringAsync().ConfigureAwait(false).GetAwaiter().GetResult(); //Make sure it is synchronous

                    tracingService.Trace($"ErrorRepro.AsyncError.GetWebResponse responseContent parsed successfully.");

                    return responseContent;

                }
            }
            catch (Exception ex)
            {
                //Capture the inner exception message if it exists.
                // It should have a more specific detail.
                string innerExceptionMessage = string.Empty;
                if (ex.InnerException != null) {
                    innerExceptionMessage = ex.InnerException.Message;
                }

                tracingService.Trace($"Error in ErrorRepro.AsyncError : {ex.Message} InnerException: {innerExceptionMessage}");
                if (!string.IsNullOrEmpty(innerExceptionMessage))
                {
                    throw new Exception($"A call to an external web service failed. {innerExceptionMessage}", ex);
                }

                throw new Exception("A call to an external web service failed.", ex);
            }
        }
    }
}
```

### Stack Overflow error in plug-in

This type of error occurs most frequently right after you make some change in your plug-in code. Some people use their own set of base classes to streamline their development experience. Sometimes these errors originate from changes to those base classes which a particular plug-in depends on.

For example, a recursive call without a termination condition, or a termination condition which doesn’t cover all scenarios can cause this to happen. More information: [StackOverflowException Class > Remarks](/dotnet/api/system.stackoverflowexception?view=netframework-4.6.2#remarks)

You should review any code changes that were applied recently for the plug-in and any other code that the plug-in code depends on.

#### Example

The following plug-in code will cause a `StackOverflowException` due to a recursive call with no limits. Despite the use of the tracing, and attempting to capture the error, neither the tracing or the error will be returned because the worker process that would process them has terminated.

```csharp
using Microsoft.Xrm.Sdk;
using System;

namespace ErrorRepro
{
    public class SOError : IPlugin
    {
        public void Execute(IServiceProvider serviceProvider)
        {
            ITracingService tracingService =
           (ITracingService)serviceProvider.GetService(typeof(ITracingService));

            tracingService.Trace($"Starting ErrorRepro.SOError");

            try
            {
                tracingService.Trace($"Calling RecursiveMethodWithNoLimit to trigger StackOverflow error.");

                RecursiveMethodWithNoLimit(tracingService); //StackOverflowException occurs here.
            }
            catch (Exception ex)
            {
                //This trace will not be written
                tracingService.Trace($"Error in ErrorRepro.SOError {ex.Message}");

                //This error will never be thrown
                throw new InvalidPluginExecutionException($"Error in ErrorRepro.SOError. {ex.Message}");
            }

            //This trace will never be written
            tracingService.Trace($"Ending ErrorRepro.SOError");
        }

        public static void RecursiveMethodWithNoLimit(ITracingService tracingService)
        {
            tracingService.Trace($"Starting ErrorRepro.SOError.RecursiveMethodWithNoLimit");

            RecursiveMethodWithNoLimit(tracingService);

            tracingService.Trace($"Ending ErrorRepro.SOError.RecursiveMethodWithNoLimit");
        }
    }
}
```

When the plug-in code above is used in a synchronous plug-in, the following error will be returned by the Web API:

```json
{
    "error": {
        "code": "0x8004418d",
        "message": "The plug-in execution failed because no Sandbox Worker processes are currently available. Please try again.\r\nSystem.ServiceModel.CommunicationException: The server did not provide a meaningful reply; this might be caused by a contract mismatch, a premature session shutdown or an internal server error.\r\n   at Microsoft.Crm.Sandbox.SandboxWorkerProcess.Execute(SandboxCallInfo callInfo, SandboxPluginExecutionContext requestContext, Guid pluginAssemblyId, Int32 sourceHash, String assemblyName, Guid pluginTypeId, String pluginTypeName, String pluginConfiguration, String pluginSecureConfig, Boolean returnTraceInfo, Int64& wcfExecInMs, Int64& initializeInMs, Int64& trackCallInMs, Int64& trackGoodReturnInMs, Int64& waitInMs, Int64& taskStartDelay) +0x330: Microsoft Dynamics CRM has experienced an error. Reference number for administrators or support: #8503641A",
        "@Microsoft.PowerApps.CDS.ErrorDetails.ApiExceptionSourceKey": "Plugin/ErrorRepro.SOError, ErrorRepro, Version=1.0.0.0, Culture=neutral, PublicKeyToken=c2bee3e550ec0851",
        "@Microsoft.PowerApps.CDS.ErrorDetails.ApiStepKey": "d5958631-b87e-eb11-a812-000d3a4f50a7",
        "@Microsoft.PowerApps.CDS.ErrorDetails.ApiDepthKey": "1",
        "@Microsoft.PowerApps.CDS.ErrorDetails.ApiActivityIdKey": "a3028bda-73c2-4eef-bcb5-157c5a4c323e",
        "@Microsoft.PowerApps.CDS.ErrorDetails.ApiPluginSolutionNameKey": "Active",
        "@Microsoft.PowerApps.CDS.ErrorDetails.ApiStepSolutionNameKey": "Active",
        "@Microsoft.PowerApps.CDS.ErrorDetails.ApiExceptionCategory": "SystemFailure",
        "@Microsoft.PowerApps.CDS.ErrorDetails.ApiExceptionMesageName": "SandboxWorkerNotAvailable",
        "@Microsoft.PowerApps.CDS.ErrorDetails.ApiExceptionHttpStatusCode": "500",
        "@Microsoft.PowerApps.CDS.HelpLink": "http://go.microsoft.com/fwlink/?LinkID=398563&error=Microsoft.Crm.CrmException%3a8004418d&client=platform",
        "@Microsoft.PowerApps.CDS.TraceText": "\r\n[ErrorRepro: ErrorRepro.SOError]\r\n[d5958631-b87e-eb11-a812-000d3a4f50a7: ErrorRepro.SOError: Create of account]\r\n\r\n",
        "@Microsoft.PowerApps.CDS.InnerError.Message": "The plug-in execution failed because no Sandbox Worker processes are currently available. Please try again.\r\nSystem.ServiceModel.CommunicationException: The server did not provide a meaningful reply; this might be caused by a contract mismatch, a premature session shutdown or an internal server error.\r\n   at Microsoft.Crm.Sandbox.SandboxWorkerProcess.Execute(SandboxCallInfo callInfo, SandboxPluginExecutionContext requestContext, Guid pluginAssemblyId, Int32 sourceHash, String assemblyName, Guid pluginTypeId, String pluginTypeName, String pluginConfiguration, String pluginSecureConfig, Boolean returnTraceInfo, Int64& wcfExecInMs, Int64& initializeInMs, Int64& trackCallInMs, Int64& trackGoodReturnInMs, Int64& waitInMs, Int64& taskStartDelay) +0x330: Microsoft Dynamics CRM has experienced an error. Reference number for administrators or support: #8503641A"
    }
}
```

This is how this error will be recorded in the Plug-in trace log:

```
Unhandled exception: 
Exception type: System.ServiceModel.FaultException`1[Microsoft.Xrm.Sdk.OrganizationServiceFault]
Message: The plug-in execution failed because no Sandbox Worker processes are currently available. Please try again.
System.ServiceModel.CommunicationException: The server did not provide a meaningful reply; this might be caused by a contract mismatch, a premature session shutdown or an internal server error.
   at Microsoft.Crm.Sandbox.SandboxWorkerProcess.Execute(SandboxCallInfo callInfo, SandboxPluginExecutionContext requestContext, Guid pluginAssemblyId, Int32 sourceHash, String assemblyName, Guid pluginTypeId, String pluginTypeName, String pluginConfiguration, String pluginSecureConfig, Boolean returnTraceInfo, Int64& wcfExecInMs, Int64& initializeInMs, Int64& trackCallInMs, Int64& trackGoodReturnInMs, Int64& waitInMs, Int64& taskStartDelay) +0x330: Microsoft Dynamics CRM has experienced an error. Reference number for administrators or support: #4BC22433Detail: 
<OrganizationServiceFault xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.microsoft.com/xrm/2011/Contracts">
  <ActivityId>48c5818e-4912-42f0-b1b6-e3bbe7ae013d</ActivityId>
  <ErrorCode>-2147204723</ErrorCode>
  <ErrorDetails xmlns:d2p1="http://schemas.datacontract.org/2004/07/System.Collections.Generic" />
  <HelpLink i:nil="true" />
  <Message>The plug-in execution failed because no Sandbox Worker processes are currently available. Please try again.
System.ServiceModel.CommunicationException: The server did not provide a meaningful reply; this might be caused by a contract mismatch, a premature session shutdown or an internal server error.
   at Microsoft.Crm.Sandbox.SandboxWorkerProcess.Execute(SandboxCallInfo callInfo, SandboxPluginExecutionContext requestContext, Guid pluginAssemblyId, Int32 sourceHash, String assemblyName, Guid pluginTypeId, String pluginTypeName, String pluginConfiguration, String pluginSecureConfig, Boolean returnTraceInfo, Int64&amp; wcfExecInMs, Int64&amp; initializeInMs, Int64&amp; trackCallInMs, Int64&amp; trackGoodReturnInMs, Int64&amp; waitInMs, Int64&amp; taskStartDelay) +0x330: Microsoft Dynamics CRM has experienced an error. Reference number for administrators or support: #4BC22433</Message>
  <Timestamp>2021-03-06T22:14:22.0629638Z</Timestamp>
  <ExceptionRetriable>false</ExceptionRetriable>
  <ExceptionSource>WorkerCommunication</ExceptionSource>
  <InnerFault i:nil="true" />
  <OriginalException>System.ServiceModel.CommunicationException: The server did not provide a meaningful reply; this might be caused by a contract mismatch, a premature session shutdown or an internal server error.

Server stack trace: 
   at System.ServiceModel.Channels.ServiceChannel.Call(String action, Boolean oneway, ProxyOperationRuntime operation, Object[] ins, Object[] outs, TimeSpan timeout)
   at System.ServiceModel.Channels.ServiceChannelProxy.InvokeService(IMethodCallMessage methodCall, ProxyOperationRuntime operation)
   at System.ServiceModel.Channels.ServiceChannelProxy.Invoke(IMessage message)

Exception rethrown at [0]: 
   at Microsoft.Crm.Sandbox.SandboxWorkerProcess.Execute(SandboxCallInfo callInfo, SandboxPluginExecutionContext requestContext, Guid pluginAssemblyId, Int32 sourceHash, String assemblyName, Guid pluginTypeId, String pluginTypeName, String pluginConfiguration, String pluginSecureConfig, Boolean returnTraceInfo, Int64&amp; wcfExecInMs, Int64&amp; initializeInMs, Int64&amp; trackCallInMs, Int64&amp; trackGoodReturnInMs, Int64&amp; waitInMs, Int64&amp; taskStartDelay)</OriginalException>
  <TraceText i:nil="true" />
</OrganizationServiceFault>
```

### Using threads to queue work with no try/catch in thread delegate

You shouldn’t use parallel execution patterns in plug-ins. This is called out in this best practice topic: [Do not use parallel execution within plug-ins and workflow activities](best-practices/business-logic/do-not-use-parallel-execution-in-plug-ins.md). Using these patterns can cause issues managing the transaction in a synchronous plug-in. However, another reason to not use these patterns is that any work done outside of a try/catch block in a thread delegate can crash the worker process.

### Worker process reaches memory limit

Each worker process has a finite amount of memory. There are conditions where multiple concurrent operations which include large amounts of data could exceed the available memory and cause the process worker to crash.

#### RetrieveMultiple with File data

The common scenario in this case is when a plug-in executes for a `RetrieveMultiple` operation where the request includes file data. For example, when retrieving email which include any file attachments. The amount of data that may be returned in a query like this is unpredictable because any email my be related to any number of file attachments and the attachments themselves can vary in size. 

When multiple requests of a similar nature are running concurrently, the amount of memory required becomes quite large. If it exceeds the limit the process will crash.  The key to preventing this is limiting `RetrieveMultiple` queries that include entities with related file attachments. Retrieve the records using `RetrieveMultiple`, but retrieve any related files as needed using individual `Retrieve` operations.

#### Memory Leaks

A less common scenario is where the code in the plug-in is leaking memory. This can occur when the plug-in isn’t written as stateless, which is another best practice: [Develop IPlugin implementations as stateless](best-practices/business-logic/develop-iplugin-implementations-stateless.md). When the plug-in isn’t stateless and there is an attempt to continually add data to a stateful property like an array. The amount of data grows to the point where it uses all the available memory.


## Transaction errors

There are two common types of errors related to transactions:

Error Code: `-2146893812`<br />
Error Message: `ISV code reduced the open transaction count. Custom plug-ins should not catch exceptions from OrganizationService calls and continue processing.`

Error Code: `-2147220911`<br />
Error Message: `There is no active transaction. This error is usually caused by custom plug-ins that ignore errors from service calls and continue processing.`

> [!NOTE]
> The top error was added most recently. It should occur immediately and in the context of the plug-in that contains the problem. The bottom error can still occur in different circumstances, typically involving custom workflow activities. It may be due to problems in another plug-in.

To understand the message, you need to appreciate that any time an error related to a data operation occurs within a synchronous plug-in the transaction for the entire operation will be ended.

More information: [Scalable Customization Design in Microsoft Dataverse](scalable-customization-design/overview.md)

The most common cause is simply that a developer might believe they can attempt to perform an operation that *might* succeed so they wrap that operation in a try/catch block and attempt to swallow the error if it fails.

While this may work for a client application, within the execution of a plug-in any data operation failure will result in rolling back the entire transaction. You can't swallow the error, so you must make sure to always return an <xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException>.

## Error: Sql error: Execution Timeout Expired

Error Code: `-2147204783`<br />
Error Message: `Sql error: 'Execution Timeout Expired.  The timeout period elapsed prior to completion of the operation or the server is not responding.'`

There are a wide variety of reasons that a SQL timeout error may occur.

### Blocking

Blocking is the most common cause for a SQL Timeout error is that the operation is waiting for resources that are being locked by another SQL transaction. The error is the result of the system protecting the integrity of the data and from long running requests that impact performance for users.

Blocking may be due to other concurrent operations. Your code may work fine in isolation in a test environment and still be susceptible to conditions that will only occur when multiple users are initiating the logic in your plug-in.

When writing plug-ins, it is essential to understand how to design customizations that are scalable. More information: [Scalable Customization Design in Dataverse](scalable-customization-design/overview.md)

### Cascade operations

Certain actions you make in your plug-in, such as assigning or deleting a record, can initiate cascading operations on related records. These actions could apply locks on related records causing subsequent data operations to be blocked which in turn can lead to a SQL timeout.

You should consider the possible impact of these cascading operations on data operations in your plug-in. More information: [Table relationship behavior](../../maker/data-platform/create-edit-entity-relationships.md#table-relationship-behavior)

Because these behaviors can be configured differently between environments, the behavior may be difficult to reproduce unless the environments are configured in the same way.

### Indexes on new tables

If the plug-in is performing operations using a table or column that has been created recently, some Azure SQL capabilities to manage indexes might make a difference after a few days.

## Errors due to user privileges

In a client application you can disable commands that users are not allowed to perform. Within a plug-in you don't have this. Your code may include some automation that the calling user doesn't have the privileges to perform.

You can register the plug-in to run in the context of a user known to have the correct privileges by setting the **Run in User's Context** value to that user. Or you can execute the operation impersonating another user. More information:
 - [Register a plug-in](register-plug-in.md)
 - [Impersonate a user](impersonate-a-user.md)

<!-- But if you prefer that the logic in your plug-in adapt to the privileges that the calling user has, you really need to verify the user's privileges in your code.-->

## Error: Message size exceeded when sending context to Sandbox

Error Code: `-2147220970`<br />
Error Message: `Message size exceeded when sending context to Sandbox. Message size: ### Mb`

This error occurs when a message payload is greater than 116.85 MB **AND** a plug-in is registered for the message. The error message will include the size of the payload that caused this error.

The limit will help ensure that users running applications cannot interfere with each other based on resource constraints. The limit will help provide a level of protection from unusually large message payloads that threaten the availability and performance characteristics of the Dataverse platform.

116.85 MB is large enough that it should be rare to encounter this case. The most likely situation where this case might occur is when you retrieve a record with multiple related records which include large binary files.

If you encounter this error you can:

1. Remove the plug-in for the message. If there are no plug-ins registered for the message, the operation will complete without an error.
2. If the error is occurring in a custom client, you can modify your code so that it doesn't attempt to perform the work in a single operation. Instead, write code to retrieve the data in smaller parts.

## Error: The given key was not present in the dictionary

Dataverse frequently uses classes derived from the abstract <xref:Microsoft.Xrm.Sdk.DataCollection`2> class that represents a collection of keys and values. For example, with plug-ins the  <xref:Microsoft.Xrm.Sdk.IExecutionContext>.<xref:Microsoft.Xrm.Sdk.IExecutionContext.InputParameters> property is a <xref:Microsoft.Xrm.Sdk.ParameterCollection> derived from the <xref:Microsoft.Xrm.Sdk.DataCollection`2> class. These classes are essentially dictionary objects where you access a specific value using the key name.

### Error codes

This error occurs when the key value in code doesn't exist in the collection. This is a run-time error rather a platform error. When this error occurs within a plug-in, the error code will depend on whether the error was caught.

If the developer caught the exception and returned an <xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException> as described in [Handle exceptions in plug-ins](handle-exceptions.md), the following error will be returned:

Error Code: `-2147220891`<br />
Error Message: `ISV code aborted the operation.`

However, with this error it is common that the developer doesn't catch it properly and the following error will be returned:

Error Code: `-2147220956`<br />
Error Message: `An unexpected error occurred from ISV code.`

> [!NOTE]
> "ISV" stands for *Independent Software Vendor*.

### Causes

This error frequently occurs at design time and can be due to a misspelling or using the incorrect casing. The key values are case sensitive.

At run-time the error is frequently due to the developer assuming that the value will be present when it isn't. For example, in a plug-in that is registered for the update of a table, only those values which are changed will be included in the <xref:Microsoft.Xrm.Sdk.Entity>.<xref:Microsoft.Xrm.Sdk.Entity.Attributes> collection.

### Prevention

To prevent this error you must check that the key exists before attempting to use it to access a value. 

For example, when accessing a table column, you can use the <xref:Microsoft.Xrm.Sdk.Entity>.<xref:Microsoft.Xrm.Sdk.Entity.Contains(System.String)> method to check whether a column exists in a table as shown in the following code.

```csharp
// Obtain the execution context from the service provider.  
IPluginExecutionContext context = (IPluginExecutionContext)
    serviceProvider.GetService(typeof(IPluginExecutionContext));

// The InputParameters collection contains all the data passed in the message request.  
if (context.InputParameters.Contains("Target") &&
    context.InputParameters["Target"] is Entity)
    {
    // Obtain the target entity from the input parameters.  
    Entity entity = (Entity)context.InputParameters["Target"];

    //Check whether the name attribute exists.
    if(entity.Contains("name"))
    {
        string name = entity["name"];
    }
```

Some developers use the <xref:Microsoft.Xrm.Sdk.Entity>.<xref:Microsoft.Xrm.Sdk.Entity.GetAttributeValue``1(System.String)> method to avoid this error when accessing a table column, but be aware that this method will return the default value of the type if the column doesn't exist. If the default value is null, this works as expected. But if the default value doesn't return null, such as with a `DateTime`, the value returned will be `1/1/0001 00:00` rather than null.

## Error: You cannot start a transaction with a different isolation level than is already set on the current transaction

Error Code: `-2147220989`<br />
Error Message: `You cannot start a transaction with a different isolation level than is already set on the current transaction`

Plug-ins are intended to support business logic. Modifying any part of the data schema within synchronous plug-in is not supported. These operations frequently take longer and may cause cached metadata used by applications to become out of sync. However, these operations can be performed in a plug-in step registered to run asynchronously.

[!INCLUDE[footer-include](../../includes/footer-banner.md)]