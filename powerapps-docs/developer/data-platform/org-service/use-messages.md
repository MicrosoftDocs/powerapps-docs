---
title: "Use messages with the Organization service (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Understand how messages are used to invoke operations using the organization service." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: intro-internal
ms.date: 03/10/2023
author: divkamath
ms.author: dikamath
ms.reviewer: pehecke
ms.topic: article
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
 - JimDaly
 - phecke
---
# Use messages with the Organization service

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

All data operations in the organization service are defined as messages. While the <xref:Microsoft.Xrm.Sdk.IOrganizationService> provides 7 methods to perform data operations (<xref:Microsoft.Xrm.Sdk.IOrganizationService.Create%2A>, <xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve%2A>, <xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple%2A>, <xref:Microsoft.Xrm.Sdk.IOrganizationService.Update%2A>, <xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete%2A>, <xref:Microsoft.Xrm.Sdk.IOrganizationService.Associate%2A>, and <xref:Microsoft.Xrm.Sdk.IOrganizationService.Disassociate%2A> ), each of these methods is a convenience wrapper around the underlying message which is ultimately invoked using the <xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A> method. The underlying organization service only has the <xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A> method which as a single parameter: an instance of the <xref:Microsoft.Xrm.Sdk.OrganizationRequest> class. The value returned by the `Execute` method is an instance of the <xref:Microsoft.Xrm.Sdk.OrganizationResponse> class.

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

## Using custom actions

When you use a custom action there are no classes in the SDK assemblies for these operations. You can generate classes for them using:

- For .NET projects using [PowerPlatform.Dataverse.Client.ServiceClient](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient), use the [pac modelbuilder](/power-platform/developer/cli/reference/modelbuilder) command that is part of the [Power Platform CLI](/power-platform/developer/cli/introduction). Use the [--generateActions](/power-platform/developer/cli/reference/modelbuilder#--generateactions--a) parameter to generate classes for custom actions.
- For .NET Framework projects, such as plug-ins, use `CrmSvcUtil.exe` code generation tool by using the `generateActions` parameter.


Alternatively, you can instantiate an <xref:Microsoft.Xrm.Sdk.OrganizationRequest> instance and set the <xref:Microsoft.Xrm.Sdk.OrganizationRequest.RequestName> and <xref:Microsoft.Xrm.Sdk.OrganizationRequest.Parameters> to use them without the generated classes. To work with the results, you will need to parse the values returned from the <xref:Microsoft.Xrm.Sdk.OrganizationResponse>.<xref:Microsoft.Xrm.Sdk.OrganizationResponse.Results> property.

More information:

- [Generate classes for early-bound programming using the Organization service](generate-early-bound-classes.md)
- [Create your own messages](../custom-actions.md)

## Passing optional parameters with a request

There are several optional parameters you can pass to apply special behaviors to messages. More information: [Use optional parameters](../optional-parameters.md)

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