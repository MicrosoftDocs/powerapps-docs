---
title: "Use messages with the Organization service (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Understand how messages are used to invoke operations using the organization service." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: intro-internal
ms.date: 05/27/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "pehecke" # MSFT alias of Microsoft employees only
manager: "sunilg" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Use messages with the Organization service

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

All data operations in the organization service are defined as messages. While the <xref:Microsoft.Xrm.Sdk.IOrganizationService> provides 7 methods to perform data operations (<xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>, <xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>, <xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>, <xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>, <xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>, <xref:Microsoft.Xrm.Sdk.IOrganizationService.Associate*>, and <xref:Microsoft.Xrm.Sdk.IOrganizationService.Disassociate*> ), each of these methods is a convenience wrapper around the underlying message which is ultimately invoked using the <xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*> method. The underlying organization service only has the <xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*> method which as a single parameter: an instance of the <xref:Microsoft.Xrm.Sdk.OrganizationRequest> class. The value returned by the `Execute` method is an instance of the <xref:Microsoft.Xrm.Sdk.OrganizationResponse> class.

To make your experience better when you write code, all the standard system data operations have a pair of `*Request` and `*Response` classes defined in the SDK assemblies. Each of these classes inherit from the respective <xref:Microsoft.Xrm.Sdk.OrganizationRequest> and <xref:Microsoft.Xrm.Sdk.OrganizationResponse> classes and provide a more productive experience for you when you write code.

The following examples show three different ways to create an account row defined this way:

```csharp
var account = new Account();
account.Name = "Test account";
```

Using <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>

```csharp
var id = svc.Create(account);
```

Using <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> with <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*>

```csharp
CreateRequest request = new CreateRequest()
{ Target = account };
var id = ((CreateResponse)svc.Execute(request)).id;
```

Using <xref:Microsoft.Xrm.Sdk.OrganizationRequest> with <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*>

```csharp
ParameterCollection parameters = new ParameterCollection();
parameters.Add("Target", account);

OrganizationRequest request = new OrganizationRequest() {
RequestName = "Create",
Parameters = parameters
};

OrganizationResponse response = svc.Execute(request);

var id = (Guid)response.Results["id"];
```

As you can see, common data operations have been streamlined using the <xref:Microsoft.Xrm.Sdk.IOrganizationService> methods and system messages are simplified by the `*Request` and `*Response` classes in the SDK assemblies. Most of the time you will not need to use the underlying <xref:Microsoft.Xrm.Sdk.OrganizationRequest> and <xref:Microsoft.Xrm.Sdk.OrganizationResponse> classes except for the following cases.

## Working with messages in plug-ins

The data describing an operation in a plug-in will be in the form of <xref:Microsoft.Xrm.Sdk.IExecutionContext>.<xref:Microsoft.Xrm.Sdk.IExecutionContext.InputParameters> and <xref:Microsoft.Xrm.Sdk.IExecutionContext>.<xref:Microsoft.Xrm.Sdk.IExecutionContext.OutputParameters>. These <xref:Microsoft.Xrm.Sdk.ParameterCollection> properties contain the values used for the <xref:Microsoft.Xrm.Sdk.OrganizationRequest> in the first two stages of the event execution pipeline and the <xref:Microsoft.Xrm.Sdk.OrganizationResponse> class in the stage after the main operation.

Understanding the structure of the messages will help you understand where to find the data you want to check or change within the plug-in.

More information: 

- [Write plug-ins to extend business processes](../plug-ins.md)
- [Event Framework](../event-framework.md)

## Using Custom actions

When you use a custom action there are no classes in the SDK assemblies for these operations. You can generate classes for them using the `CrmSvcUtil.exe` code generation tool by using the `generateActions` parameter, or you can instantiate an <xref:Microsoft.Xrm.Sdk.OrganizationRequest> instance and set the <xref:Microsoft.Xrm.Sdk.OrganizationRequest.RequestName> and <xref:Microsoft.Xrm.Sdk.OrganizationRequest.Parameters> to use them without the generated classes. To work with the results, you will need to parse the values returned from the <xref:Microsoft.Xrm.Sdk.OrganizationResponse>.<xref:Microsoft.Xrm.Sdk.OrganizationResponse.Results> property.

More information: 

- [Generate classes for early-bound programming using the Organization service](generate-early-bound-classes.md)
- [Custom Actions](../custom-actions.md)

## Passing optional parameters with a request

You can pass optional parameters in messages using the <xref:Microsoft.Xrm.Sdk.OrganizationRequest.Parameters> property that is exposed for all the *Request message classes in the SDK assemblies. There are several optional parameters you can pass with messages:

|Parameter|Description|Messages|  
|-----------------|-----------------|--------------|  
|`SolutionUniqueName`|A `String` that specifies the unique name of the solution to which the operation applies. More information: [Dependency tracking for solution components](/power-platform/alm/dependency-tracking-solution-components).|<xref:Microsoft.Crm.Sdk.Messages.AddPrivilegesRoleRequest> <br /> <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> <br /> <xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> <br /> <xref:Microsoft.Crm.Sdk.Messages.MakeAvailableToOrganizationTemplateRequest> <br /> <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest>|  
|`SuppressDuplicateDetection`|A `Boolean` used to disable duplicate detection on a create or update operation. More information: [Use SuppressDuplicateDetection parameter to throw errors when you create or update row](detect-duplicate-data.md#use-suppressduplicatedetection-parameter-to-throw-errors-when-you-create-or-update-row) .|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> <br /> <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest>|
|`tag`|A value to include within the `ExecutionContext` `SharedVariables` collection. |Any message that can have a plug-in step registered. More information: [Add a shared variable from the Organization Service](#add-a-shared-variable-from-the-organization-service)|
|`PartitionId`| A unique `String` value used to access non-relational table data in NoSql tables within a storage partition. Used to improve performance when accessing table data in Azure heterogenous storage. <p/>More information: [Improve performance when accessing table data using storage partitions](azure-storage-partitioning-sdk.md) |<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> <br /> <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest><br /> <xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> <br /> <xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> |
|`BypassCustomPluginExecution`|Bypasses custom plug-ins when included in a request sent by someone with the `prvBypassCustomPlugins` privilege. More information: [Bypass Custom Business Logic](../bypass-custom-business-logic.md)|Any request that could include custom plug-ins.|  
  
 The following sample shows how to pass an optional parameter:  
  
```csharp  
Account account = new Account();  
account.Name = "Fabrikam";  
CreateRequest req = new CreateRequest();  
req.Target = account;  
req["SuppressDuplicateDetection"] = true;  
CreateResponse response = (CreateResponse)svc.Execute(req);  
```  

### Add a shared variable from the Organization Service

You can set a string value that will be available to plug-ins within the ExecutionContext in the `SharedVariables` collection. More information: [Shared variables](../understand-the-data-context.md#shared-variables)

```csharp
var account = new Entity("account");
account["name"] = "Contoso";

var request = new CreateRequest() { Target = account };
request["tag"] = "This is a value passed.";

var response = (CreateResponse)svc.Execute(request);
```

Will result in the following value within the `SharedVariables` collection when sent using a webhook.

```json
{
"key": "tag",
"value": "This is a value passed."
}
```

This can also be done using the Web API: [Add a Shared Variable from the Web API](../webapi/compose-http-requests-handle-errors.md#add-a-shared-variable-from-the-web-api)

## Private Messages

Microsoft Dataverse contains some messages which are not intended for 3rd party developers to use. These messages are typically added by Microsoft to enable feature functionality, but can also be added by 3rd party solutions with the Custom API feature. Private messages are indicated by the [SdkMessage.IsPrivate](../reference/entities/sdkmessage.md#BKMK_IsPrivate) property.

> [!CAUTION]
> You should not use private messages unless you created them as a Custom API. By marking a message as private, the solution publisher is explicitly calling out that they do not support other apps to use the message. They may remove the message or introduce breaking changes at any time. Use of these messages by anyone other than the solution publisher are not supported.
> Calling private messages from plug-ins is not supported.

More information: [Create and use Custom APIs](../custom-api.md)

### See also

[Table operations using the Organization service](entity-operations.md)<br />
[Use ExecuteAsync to execute messages asynchronously](use-executeAsync.md)<br />
[Execute messages in a single database transaction](use-executetransaction.md)<br />
[Execute multiple requests using the Organization service](execute-multiple-requests.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]