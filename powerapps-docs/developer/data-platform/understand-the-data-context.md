---
title: "Understand the execution context (Microsoft Dataverse) | Microsoft Docs" 
description: "Learn about the data that is passed to your plug-in when it is executed." 
ms.custom: ""
ms.date: 03/12/2021
ms.reviewer: pehecke
ms.service: powerapps
ms.topic: "article"
author: JimDaly
ms.subservice: dataverse-developer
ms.author: pehecke
manager: sunilg
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Understand the execution context

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

The **Event Execution Pipeline** passes registered plug-ins a wealth of data about the current operation being processed and your custom code's execution environment. The following sections describe the data that is passed to your plug-in or custom workflow activity.

## For plug-ins

With plug-ins you can access this data in your code by setting a variable that implements the <xref:Microsoft.Xrm.Sdk.IPluginExecutionContext> interface:

```csharp
// Obtain the execution context from the service provider.  
IPluginExecutionContext context = (IPluginExecutionContext)
    serviceProvider.GetService(typeof(IPluginExecutionContext));
```

This <xref:Microsoft.Xrm.Sdk.IPluginExecutionContext> provides some information about the <xref:Microsoft.Xrm.Sdk.IPluginExecutionContext.Stage> that the plug-in is registered for as well as information about the <xref:Microsoft.Xrm.Sdk.IPluginExecutionContext.ParentContext>.

More information: [ParentContext](#parentcontext)

## For Custom Workflow Activities

With custom workflow activities you can access this data in your code by setting a variable that implements the <xref:Microsoft.Xrm.Sdk.Workflow.IWorkflowContext> interface:

```csharp
// Obtain the execution context using the GetExtension method.  
protected override void Execute(CodeActivityContext context)
{
 IWorkflowContext workflowContext = context.GetExtension<IWorkflowContext>();
...
```

This <xref:Microsoft.Xrm.Sdk.Workflow.IWorkflowContext> provides some information about the workflow that the custom workflow activity is running within.

|Property  |Description  |
|---------|---------|
|<xref:Microsoft.Xrm.Sdk.Workflow.IWorkflowContext.ParentContext>|Gets the parent context. See [ParentContext](#parentcontext)|
|<xref:Microsoft.Xrm.Sdk.Workflow.IWorkflowContext.StageName>|Gets the stage information of the process instance.|
|<xref:Microsoft.Xrm.Sdk.Workflow.IWorkflowContext.WorkflowCategory>|Gets the process category information of the process instance: Is it a workflow or dialog (deprecated).|
|<xref:Microsoft.Xrm.Sdk.Workflow.IWorkflowContext.WorkflowMode>|Indicates how the workflow is to be executed. 0 = asynchronous, 1 = synchronous|

## ParentContext

The `ParentContext` provides information about any operation that triggers the plug-in or custom workflow activity to run.

Except for specific documented cases, you should avoid taking a dependency on values that you find in the `ParentContext` to apply your business logic. The specific order in which operations occur is not guaranteed and may change over time.

If you do choose to take a dependency on values found in the `ParentContext`, you should take steps to ensure that your code is resilient to adapt to potential changes. You should test the logic regularly to verify that the conditions you depend on remain in effect over time.

## ExecutionContext

The rest of the information available is provided by the <xref:Microsoft.Xrm.Sdk.IExecutionContext> interface that the <xref:Microsoft.Xrm.Sdk.IPluginExecutionContext> and <xref:Microsoft.Xrm.Sdk.Workflow.IWorkflowContext> classes implement.

For plug-ins, all the properties of this execution context class provide useful information you may need to access in your code.

> [!NOTE]
> For custom workflow activities, these properties are generally not used.

Two of the most important are the <xref:Microsoft.Xrm.Sdk.IExecutionContext.InputParameters> and <xref:Microsoft.Xrm.Sdk.IExecutionContext.OutputParameters> properties.

Other frequently used properties are <xref:Microsoft.Xrm.Sdk.IExecutionContext.SharedVariables>, <xref:Microsoft.Xrm.Sdk.IExecutionContext.PreEntityImages>, and <xref:Microsoft.Xrm.Sdk.IExecutionContext.PostEntityImages>.

> [!TIP]
> A good way to visualize the data that is passed into the execution context is to install the Plug-in Profiler solution that is available as part of the Plug-in Registration tool. The profiler will capture the context information as well as information that allows for replaying event locally so you can debug. Within the Plug-in Registration tool, you can download an XML document with all the data from the event that triggered the workflow. More information: [View plug-in profile data](debug-plug-in.md#view-plug-in-profile-data)

## ParameterCollections

All the properties of the execution context are read-only. But the `InputParameters`, `OutputParameters`, and `SharedVariables` are <xref:Microsoft.Xrm.Sdk.ParameterCollection> values. You can manipulate the values of the items in these collections to change the behavior of the operation, depending on the stage in the event execution pipeline your plug-in is registered for.

The <xref:Microsoft.Xrm.Sdk.ParameterCollection> values are defined as <xref:System.Collections.Generic.KeyValuePair> structures. In order to access a property you will need to know the name of the property that is exposed by the message. For example, to access the <xref:Microsoft.Xrm.Sdk.Entity> property that is passed as part of the <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest>, you need to know that the name of that property is `Target`. Then you can access this value using code like this:

```csharp
var entity = (Entity)context.InputParameters["Target"];
```

Use the <xref:Microsoft.Xrm.Sdk.Messages> and <xref:Microsoft.Crm.Sdk.Messages> documentation to learn the names of the messages defined in the SDK assemblies. For custom actions, refer to the names of the parameters defined in the system.

## InputParameters

The `InputParameters` represent the value of the <xref:Microsoft.Xrm.Sdk.OrganizationRequest>.<xref:Microsoft.Xrm.Sdk.OrganizationRequest.Parameters> property that represents the operation coming in from the web services.

As described in [Use messages with the Organization service](org-service/use-messages.md), all operations that occur in the system are ultimately instances of the `OrganizationRequest` class being processed by the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*> method.

As described in [Event Framework](event-framework.md), operations go through a series of stages and you can register your plug-in on stages that occur before the data is written to the database. Within the **PreValidation** and **PreOperation** stages, you can read and change the values of the `InputParameters` so that you can control the expected outcome of the data operation.

If you find that the values in the `InputParameters` collection represent a condition that you cannot allow, you can throw an <xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException> (preferably in the **PreValidation** stage) that will cancel the operation and display an error to the user with a synchronous plug-in, or log the error if the plug-in is asynchronous. More information: [Cancelling an operation](handle-exceptions.md#cancelling-an-operation)

## OutputParameters

The `OutputParameters` represent the value of the <xref:Microsoft.Xrm.Sdk.OrganizationResponse>.<xref:Microsoft.Xrm.Sdk.OrganizationResponse.Results> property that represents the return value of the operation. Each of the message response classes that are derived from <xref:Microsoft.Xrm.Sdk.OrganizationResponse> contain specific properties. To access these properties you must use the key value that is *usually* the same as the name of the properties in the response class. However, this is not always true. The following table lists the message response class properties that have keys different from the name of the properties.

|Response Class  |Property  |Key Value  |
|---------|---------|---------|
|<xref:Microsoft.Crm.Sdk.Messages.BackgroundSendEmailResponse>|<xref:Microsoft.Crm.Sdk.Messages.BackgroundSendEmailResponse.EntityCollection>|`BusinessEntityCollection`|
|<xref:Microsoft.Crm.Sdk.Messages.CloneContractResponse>|<xref:Microsoft.Crm.Sdk.Messages.CloneContractResponse.Entity>|`BusinessEntity`|
|<xref:Microsoft.Crm.Sdk.Messages.CloneMobileOfflineProfileResponse>|<xref:Microsoft.Crm.Sdk.Messages.CloneMobileOfflineProfileResponse.CloneMobileOfflineProfile>|`EntityReference`|
|<xref:Microsoft.Crm.Sdk.Messages.CloneProductResponse>|<xref:Microsoft.Crm.Sdk.Messages.CloneProductResponse.ClonedProduct>|`EntityReference`|
|<xref:Microsoft.Crm.Sdk.Messages.ConvertSalesOrderToInvoiceResponse>|<xref:Microsoft.Crm.Sdk.Messages.ConvertSalesOrderToInvoiceResponse.Entity>|`BusinessEntity`|
|<xref:Microsoft.Crm.Sdk.Messages.CreateKnowledgeArticleTranslationResponse>|<xref:Microsoft.Crm.Sdk.Messages.CreateKnowledgeArticleTranslationResponse.CreateKnowledgeArticleTranslation>|`EntityReference`|
|<xref:Microsoft.Crm.Sdk.Messages.CreateKnowledgeArticleVersionResponse>|<xref:Microsoft.Crm.Sdk.Messages.CreateKnowledgeArticleVersionResponse.CreateKnowledgeArticleVersion>|`EntityReference`|
|<xref:Microsoft.Crm.Sdk.Messages.GenerateQuoteFromOpportunityResponse>|<xref:Microsoft.Crm.Sdk.Messages.GenerateQuoteFromOpportunityResponse.Entity>|`BusinessEntity`|
|<xref:Microsoft.Crm.Sdk.Messages.GetDefaultPriceLevelResponse>|<xref:Microsoft.Crm.Sdk.Messages.GetDefaultPriceLevelResponse.PriceLevels>|`BusinessEntityCollection`|
|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveResponse>|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveResponse.Entity>|`BusinessEntity`|
|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleResponse>|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleResponse.EntityCollection>|`BusinessEntityCollection`|
|<xref:Microsoft.Crm.Sdk.Messages.RetrievePersonalWallResponse>|<xref:Microsoft.Crm.Sdk.Messages.RetrievePersonalWallResponse.EntityCollection>|`BusinessEntityCollection`|
|<xref:Microsoft.Crm.Sdk.Messages.RetrieveRecordWallResponse>|<xref:Microsoft.Crm.Sdk.Messages.RetrieveRecordWallResponse.EntityCollection>|`BusinessEntityCollection`|
|<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedResponse>|<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedResponse.Entity>|`BusinessEntity`|
|<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedMultipleResponse>|<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedMultipleResponse.EntityCollection>|`BusinessEntityCollection`|
|<xref:Microsoft.Crm.Sdk.Messages.RetrieveUserQueuesResponse>|<xref:Microsoft.Crm.Sdk.Messages.RetrieveUserQueuesResponse.EntityCollection>|`BusinessEntityCollection`|


The `OutputParameters` are not populated until after the database transaction, so they are only available for plug-ins registered in the **PostOperation** stage. If you want to change the values returned by the operation, you can modify them within the `OutputParameters`.

## Shared variables

The <xref:Microsoft.Xrm.Sdk.IExecutionContext.SharedVariables> property allows for including data that can be passed from the API or a plug-in to a step that occurs later in the execution pipeline. Because this is a <xref:Microsoft.Xrm.Sdk.ParameterCollection> value, plug-ins can add, read, or modify properties to share data with subsequent steps.

The following example shows how a `PrimaryContact` value can be passed from a plug-in registered for a **PreOperation** step to a **PostOperation** step.

```csharp
public class PreOperation : IPlugin
{
    public void Execute(IServiceProvider serviceProvider)
    {
        // Obtain the execution context from the service provider.
        Microsoft.Xrm.Sdk.IPluginExecutionContext context = (Microsoft.Xrm.Sdk.IPluginExecutionContext)
            serviceProvider.GetService(typeof(Microsoft.Xrm.Sdk.IPluginExecutionContext));

        // Create or retrieve some data that will be needed by the post event
        // plug-in. You could run a query, create an entity, or perform a calculation.
        //In this sample, the data to be passed to the post plug-in is
        // represented by a GUID.
        Guid contact = new Guid("{74882D5C-381A-4863-A5B9-B8604615C2D0}");

        // Pass the data to the post event plug-in in an execution context shared
        // variable named PrimaryContact.
        context.SharedVariables.Add("PrimaryContact", (Object)contact.ToString());
    }
}

public class PostOperation : IPlugin
{
    public void Execute(IServiceProvider serviceProvider)
    {
        // Obtain the execution context from the service provider.
        Microsoft.Xrm.Sdk.IPluginExecutionContext context = (Microsoft.Xrm.Sdk.IPluginExecutionContext)
            serviceProvider.GetService(typeof(Microsoft.Xrm.Sdk.IPluginExecutionContext));

        // Obtain the contact from the execution context shared variables.
        if (context.SharedVariables.Contains("PrimaryContact"))
        {
            Guid contact =
                new Guid((string)context.SharedVariables["PrimaryContact"]);

            // Do something with the contact.
        }
    }
}
```

> [!IMPORTANT]
> Any type of data added to the shared variables collection must be serializable otherwise the server will not know how to serialize the data and plug-in execution will fail.  

> [!NOTE]
> For a plug-in registered for the **PreOperation** or **PostOperation** stages to access the shared variables from a plug-in registered for the  **PreValidation** stage that executes on **Create**, **Update**, **Delete**, or by a <xref:Microsoft.Crm.Sdk.Messages.RetrieveExchangeRateRequest>, you must access the <xref:Microsoft.Xrm.Sdk.IPluginExecutionContext.ParentContext>.**SharedVariables** collection. For all other cases, <xref:Microsoft.Xrm.Sdk.IPluginExecutionContext>.**SharedVariables** contains the collection.

### Passing a Shared Variable from the API

If you need to introduce a shared variable when you call an API, use the keyword `tag` from either the Web API or the Organization service to pass a string value.

This value will be accessible in the Shared Variable collection using the `tag` key. Once set, this value cannot be changed, it is immutable.

For information about how to set this see the following topics:

- [Add a Shared Variable from the Web API](webapi/compose-http-requests-handle-errors.md#add-a-shared-variable-from-the-web-api)
- [Add a Shared Variable from the Organization Service](org-service/use-messages.md#add-a-shared-variable-from-the-organization-service)



## Entity images

When you register a step for a plug-in that includes a table as one of the parameters, you have the option to specify that a copy of the table data be included as *snapshot* or image using the <xref:Microsoft.Xrm.Sdk.IExecutionContext.PreEntityImages> and/or <xref:Microsoft.Xrm.Sdk.IExecutionContext.PostEntityImages> properties.

This data provides a comparison point for table data as it flows through the event pipeline. Using these images provides much better performance than including code in a plug-in to retrieve a table just to compare the attribute values.

When you define an entity image, you specify an entity alias value you can use to access the specific image. For example, if you define a pre-entity image with the alias '`a`', you can use the following code to access the `name` attribute value.

```csharp
var oldAccountName = (string)context.PreEntityImages["a"]["name"];
```

More information:

- [Define entity images](register-plug-in.md#define-entity-images)
- [Entity images for workflow extensions](workflow/workflow-extensions.md#entity-images-for-workflow-extensions)

### See also

[Event Framework](event-framework.md)  
[Write a plug-in](write-plug-in.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]