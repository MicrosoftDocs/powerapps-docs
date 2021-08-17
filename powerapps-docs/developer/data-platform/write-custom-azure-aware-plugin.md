---
title: "Write a custom Azure-aware plug-in (Microsoft Dataverse) | Microsoft Docs"
description: "Learn how to write plug-in code that can post a message or the execution context of the current database transaction to the Azure Service Bus."
keywords: ""
ms.date: 03/18/2021
ms.service: powerapps
ms.topic: article
ms.assetid: 93d0442e-5fc9-c43c-c8c1-a433687f3d0a
author: JimDaly # GitHub ID
ms.subservice: dataverse-developer
ms.author: jdaly # MSFT alias of Microsoft employees only
manager: ryjones # MSFT alias of manager or PM counterpart
ms.reviewer: "pehecke"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Write a custom Azure-aware plug-in

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

Writing a plug-in that works with Azure is similar to writing any other Dynamics 365 Microsoft Dataverse plug-in. However, in addition to invoking any desired web service methods, the plug-in must include code to initiate posting the current transaction's execution context to the Azure Service Bus.  
  
<a name="bkmk_design"></a>

## Plug-in design considerations

For a plug-in that executes synchronously, the recommended design is for the plug-in to send a message to Azure for the purpose of retrieving information from a listener application or other external service. Use of a two-way or REST contract on the Azure Service Bus endpoint allows a data string to be returned to the plug-in.  
  
It is not recommended that a synchronous plug-in use the Azure Service Bus to update data with an external service. Problems can arise if the external service becomes unavailable or if there is a lot of data to update. Synchronous plug-ins should execute fast and not hold up all logged in users of an organization while a lengthy operation is performed. In addition, if a rollback of the current core operation that invoked the plug-in occurs, any data changes made by the plug-in are undone. This could leave Dynamics 365 and an external service in an un-synchronized state.  
  
Note that it is possible for synchronous registered plug-ins to post the current transaction's execution context to the Azure Service Bus.  
  
<a name="bkmk_writing"></a>
  
## Write the plug-in code

In the following sample plug-in code has been added to obtain the Azure service provider and initiate posting the execution context to the Service Bus by calling <xref:Microsoft.Xrm.Sdk.IServiceEndpointNotificationService.Execute(Microsoft.Xrm.Sdk.EntityReference,Microsoft.Xrm.Sdk.IExecutionContext)>. Tracing code has been added to facilitate debugging of the plug-in because the plug-in must run in the sandbox.  

> [!NOTE]
> The `serviceEndpointId` passed into the constructor in this code is the one you get from creating a service endpoint as described in [Walkthrough: Configure Azure (SAS) for integration with Dataverse](walkthrough-configure-azure-sas-integration.md)
>
> You can query available service endpoints for your environment using a `GET` request to Web API using your browser with a query like this: *`[organization Uri]`*`/api/data/v9.0/serviceendpoints?$select=name,description,serviceendpointid`
  
```csharp
using System;
using System.Diagnostics;
using System.Threading;
using System.Runtime.Serialization;

using System.ServiceModel;
using System.ServiceModel.Channels;
using System.ServiceModel.Description;

using Microsoft.Xrm.Sdk;

namespace Microsoft.Crm.Sdk.Samples
{
    /// <summary>
    /// A custom plug-in that can post the execution context of the current message to the Windows
    /// Azure Service Bus. The plug-in also demonstrates tracing which assist with
    /// debugging for plug-ins that are registered in the sandbox.
    /// </summary>
    /// <remarks>This sample requires that a service endpoint be created first, and its ID passed
    /// to the plug-in constructor through the unsecure configuration parameter when the plug-in
    /// step is registered.</remarks>
    public sealed class SandboxPlugin : IPlugin
    {
        private Guid serviceEndpointId; 

        /// <summary>
        /// Constructor.
        /// </summary>
        public SandboxPlugin(string config)
        {
            if (String.IsNullOrEmpty(config) || !Guid.TryParse(config, out serviceEndpointId))
            {
                throw new InvalidPluginExecutionException("Service endpoint ID should be passed as config.");
            }
        }

        public void Execute(IServiceProvider serviceProvider)
        {
            // Retrieve the execution context.
            IPluginExecutionContext context = (IPluginExecutionContext)serviceProvider.GetService(typeof(IPluginExecutionContext));

            // Extract the tracing service.
            ITracingService tracingService = (ITracingService)serviceProvider.GetService(typeof(ITracingService));
            if (tracingService == null)
                throw new InvalidPluginExecutionException("Failed to retrieve the tracing service.");

            IServiceEndpointNotificationService cloudService = (IServiceEndpointNotificationService)serviceProvider.GetService(typeof(IServiceEndpointNotificationService));
            if (cloudService == null)
                throw new InvalidPluginExecutionException("Failed to retrieve the service bus service.");

            try
            {
                tracingService.Trace("Posting the execution context.");
                string response = cloudService.Execute(new EntityReference("serviceendpoint", serviceEndpointId), context);
                if (!String.IsNullOrEmpty(response))
                {
                    tracingService.Trace("Response = {0}", response);
                }
                tracingService.Trace("Done.");
            }
            catch (Exception e)
            {
                tracingService.Trace("Exception: {0}", e.ToString());
                throw;
            }
        }
    }
}
```  
  
In your plug-in code, you can update the writeable data in the context before initiating the post. For example, you can add a key/value pair to the shared variables in the context.
  
<a name="bkmk_registration"></a>

## Plug-in registration

There are a few restrictions when you register a Azure-aware custom plug-in. The plug-in must be registered to execute in the sandbox. Because of this, the plug-in is limited to calling <xref:Microsoft.Xrm.Sdk.IOrganizationService> methods, Azure solution methods, or accessing a network using a web client. No other external access, such as access to a local file system, is allowed.  
  
For a plug-in registered to execute in asynchronous mode, this also means that the order of plug-in execution compared to other asynchronous plug-ins is not guaranteed. In addition, asynchronous plug-ins always execute after the Dynamics 365 core operation.  
  
<a name="bkmk_failure"></a>
 
## Handle a failed Service Bus post

The expected behavior from a failed Service Bus post is dependent on whether the plug-in was registered for synchronous or asynchronous execution. For asynchronous plug-ins, the system job that actually posts the execution context to the service bus will retry the post. For a synchronous registered plug-in, an exception is returned. More information [Management and Notification of Run-time Errors](azure-integration.md)  
  
> [!IMPORTANT]
> For asynchronous registered plug-ins only, when the asynchronous job that posts to the Azure Service Bus is retried after a post failure, the entire plug-in logic is executed again. Because of this, don't add any other logic to the custom Azure-aware plug-in other than just modifying the context and posting to the Service Bus.  
  
For a plug-in registered to execute asynchronously, the <xref:Microsoft.Xrm.Sdk.RemoteExecutionContext> contained in the body of the message that is sent over the Service Bus includes a <xref:Microsoft.Xrm.Sdk.RemoteExecutionContext.OperationId> property and a <xref:Microsoft.Xrm.Sdk.RemoteExecutionContext.OperationCreatedOn> property. These properties contain the same data as the `AsyncOperationId` and `CreatedOn` columns of the related System Job (`AsyncOperation`) record. These additional properties facilitate sequencing and duplicate detection if the Azure Service Bus post must be retried.  
  
### See also

[Azure extensions for Dynamics 365](azure-integration.md)<br />
[Send Dynamics 365 data over the Microsoft Azure Service Bus](work-data-azure-solution.md)<br />
[Write a plug-In](write-plug-in.md)<br />
[Event execution pipeline](event-framework.md)<br />
[Register and deploy plug-Ins](register-plug-in.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]