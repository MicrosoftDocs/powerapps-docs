---
title: "Use messages with the Organization service (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Understand how messages are used to invoke operations using the organization service." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Use messages with the Organization service

All data operations in the organization service are defined as messages. While the <xref:Microsoft.Xrm.Sdk.IOrganizationService> provides 7 methods to perform data operations (<xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>, <xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>, <xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>, <xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>, <xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>, <xref:Microsoft.Xrm.Sdk.IOrganizationService.Associate*>, and <xref:Microsoft.Xrm.Sdk.IOrganizationService.Disassociate*> ), each of these methods is a convenience wrapper around the underlying message which is ultimately invoked using the <xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*> method. The underlying organization service only has the <xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*> method which as a single parameter: an instance of the <xref:Microsoft.Xrm.Sdk.OrganizationRequest> class. The value returned by the `Execute` method is an instance of the <xref:Microsoft.Xrm.Sdk.OrganizationResponse> class.

To make your experience better when you write code, all the standard system data operations have a pair of `*Request` and `*Response` classes defined in the SDK assemblies. Each of these classes inherit from the respective <xref:Microsoft.Xrm.Sdk.OrganizationRequest> and <xref:Microsoft.Xrm.Sdk.OrganizationResponse> classes and provide a more productive experience for you when you write code.

The following examples show three different ways to create an account entity record defined this way:

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

As you can see, common data operations have been streamlined using the <xref:Microsoft.Xrm.Sdk.IOrganizationService> methods and system messages are simplified by the `*Request` and `*Response` classes  in the SDK assemblies. Most of the time you will not need to use the underlying <xref:Microsoft.Xrm.Sdk.OrganizationRequest> and <xref:Microsoft.Xrm.Sdk.OrganizationResponse> classes except for the following cases.

## Working with messages in Plug-ins

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

You can pass optional parameters in messages using the <xref:Microsoft.Xrm.Sdk.OrganizationRequest.Parameters> property that is exposed for all the *Request message classes in the SDK assemblies. There are two optional parameters you can pass with messages

|`Parameter`|Description|Messages|  
|-----------------|-----------------|--------------|  
|`SolutionUniqueName`|A `String` that specifies the unique name of the solution to which the operation applies. More information: [Dependency tracking for solution components](../dependency-tracking-solution-components.md).|<xref:Microsoft.Crm.Sdk.Messages.AddPrivilegesRoleRequest> <br /> <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> <br /> <xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> <br /> <xref:Microsoft.Crm.Sdk.Messages.MakeAvailableToOrganizationTemplateRequest> <br /> <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest>|  
|`SuppressDuplicateDetection`|A `Boolean` used to disable duplicate detection on a create or update operation. More information: [Use SuppressDuplicateDetection parameter to throw errors when you create or update record](detect-duplicate-data.md#use-suppressduplicatedetection-parameter-to-throw-errors-when-you-create-or-update-record) .|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> <br /> <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest>|  
  
 The following sample shows how to pass an optional parameter:  
  
```csharp  
Account account = new Account();  
account.Name = "Fabrikam";  
CreateRequest req = new CreateRequest();  
req.Target = account;  
req["SuppressDuplicateDetection"] = true;  
CreateResponse response = (CreateResponse)svc.Execute(req);  
```  

### See also

[Entity Operations using the Organization service](entity-operations.md)<br />
[Use ExecuteAsync](use-executeAsync.md)<br />
[Use ExecuteTransaction](use-executetransaction.md)<br />
[Execute multiple requests using the Organization service](execute-multiple-requests.md)



