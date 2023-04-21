---
title: "Use messages with the Organization service (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Understand how messages are used to invoke operations using the organization service." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: intro-internal
ms.date: 04/20/2023
author: divkamath
ms.author: dikamath
ms.reviewer: pehecke
ms.topic: article
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - phecke
---
# Use messages with the Organization service

The Organization service is easy to use. But before we show the easy way, let's look at the hard way so you can better understand how Dataverse works. This will help you as you move on to writing plug-ins, creating custom APIs or troubleshooting errors.

It is important to understand that all data operations in Dataverse are defined as *messages*.

Every message has:

- A name
- A collection of input parameters
- A collection of output parameters

To perform a data operation, you can:

1. Use these the <xref:Microsoft.Xrm.Sdk.OrganizationRequest> class.

   - Set the [OrganizationRequest.RequestName](xref:Microsoft.Xrm.Sdk.OrganizationRequest.RequestName)
   - Set the items in the [OrganizationRequest.Parameters](xref:Microsoft.Xrm.Sdk.OrganizationRequest.Parameters) collection.

1. Send the request using the [IOrganizationService.Execute](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A) method, which will return an <xref:Microsoft.Xrm.Sdk.OrganizationResponse> instance.

   The items in the [OrganizationResponse.Results](xref:Microsoft.Xrm.Sdk.OrganizationResponse.Results) collection contains the results.

For example, if you want to create an account record, you could do it this way:

```csharp
public static Guid OrganizationRequestExample(IOrganizationService service) {

   // Instantiate an Entity instance of type 'account'
    var account = new Entity("account");
    account["name"] = "Test account";

   // Instantiate a collection of parameters with one item 'Target',
   // set to the account entity instance
    ParameterCollection parameters = new ParameterCollection
    {
        { "Target", account }
    };

   // Instantiate an OrganizationRequest instance setting the
   // RequestName and Parameters
    OrganizationRequest request = new OrganizationRequest()
    {
        RequestName = "Create",
        Parameters = parameters
    };

   // Send the request using the IOrganizationService.Execute method
    OrganizationResponse response = service.Execute(request);

   // Parse the output parameter 'id' from the Results
    return (Guid)response.Results["id"];
}
```

To create an account record using this method, you need to know:

- The name of the message: `Create`.
- The name and data type of each input parameter: A single parameter named `Target` that is an [Entity](xref:Microsoft.Xrm.Sdk.Entity).
- The name and data type of each output parameter: A single parameter named `id` that is a [Guid](xref:System.Guid).

This information stored in Dataverse. The [SdkMessage table/entity reference](../reference/entities/sdkmessage.md) contains information about all the messages.

Information about the input and output parameters is managed by Dataverse in private tables. You will not need to use it because there is an easier way.

## SDK Request and Response classes



## IOrganizationService methods

- <xref:Microsoft.Xrm.Sdk.OrganizationRequest> using these properties:
   - 
- <xref:Microsoft.Xrm.Sdk.OrganizationResponse>



The <xref:Microsoft.Xrm.Sdk.IOrganizationService> provides seven methods to perform data operations:

- <xref:Microsoft.Xrm.Sdk.IOrganizationService.Create%2A>
- <xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve%2A>
- <xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple%2A>
- <xref:Microsoft.Xrm.Sdk.IOrganizationService.Update%2A>
- <xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete%2A>
- <xref:Microsoft.Xrm.Sdk.IOrganizationService.Associate%2A>
- <xref:Microsoft.Xrm.Sdk.IOrganizationService.Disassociate%2A>

Each of these methods is a convenience wrapper around the underlying message that is ultimately invoked using the <xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A> method.

The organization service actually has just one method: <xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A>. The `Execute` methods has a single parameter: `request`, that accepts an instance of the <xref:Microsoft.Xrm.Sdk.OrganizationRequest> class. The value returned by the `Execute` method is an instance of the <xref:Microsoft.Xrm.Sdk.OrganizationResponse> class.

To make your experience better when you write code, all the standard system data operations have a pair of `*Request` and `*Response` classes defined in the SDK assemblies. Each of these classes inherits from the respective <xref:Microsoft.Xrm.Sdk.OrganizationRequest> and <xref:Microsoft.Xrm.Sdk.OrganizationResponse> classes and provide a more productive experience for you when you write code.

The following examples show three different ways to create an account row defined this way:

```csharp
var account = new Account();
account.Name = "Test account";
```

Using [IOrganizationService.Create](xref:Microsoft.Xrm.Sdk.IOrganizationService.Create%2A)

```csharp
var id = svc.Create(account);
```

Using <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> with [IOrganizationService.Execute](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A)

```csharp
CreateRequest request = new CreateRequest()
{ Target = account };
var id = ((CreateResponse)svc.Execute(request)).id;
```

Using <xref:Microsoft.Xrm.Sdk.OrganizationRequest> with [IOrganizationService.Execute](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A)

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

As you can see, common data operations have been streamlined using the <xref:Microsoft.Xrm.Sdk.IOrganizationService> methods and system messages are made easier to use with the `*Request` and `*Response` classes in the SDK assemblies. Most of the time you don't need to use the underlying <xref:Microsoft.Xrm.Sdk.OrganizationRequest> and <xref:Microsoft.Xrm.Sdk.OrganizationResponse> classes except for the following cases.

## Working with messages in plug-ins

The data describing an operation in a plug-in are in the form of <xref:Microsoft.Xrm.Sdk.IExecutionContext>.<xref:Microsoft.Xrm.Sdk.IExecutionContext.InputParameters> and <xref:Microsoft.Xrm.Sdk.IExecutionContext>.<xref:Microsoft.Xrm.Sdk.IExecutionContext.OutputParameters>. 

In the `PreValidation` and `PreOperation` stages before the main operation of the event pipeline, the <xref:Microsoft.Xrm.Sdk.IExecutionContext.InputParameters> represent the <xref:Microsoft.Xrm.Sdk.OrganizationRequest>.<xref:Microsoft.Xrm.Sdk.OrganizationRequest.Parameters>. After the main operation, in the `PostOperation` stage, the <xref:Microsoft.Xrm.Sdk.IExecutionContext.OutputParameters> represent the <xref:Microsoft.Xrm.Sdk.OrganizationResponse>.<xref:Microsoft.Xrm.Sdk.OrganizationResponse.Results>.

Understanding the structure of the messages helps you understand where to find the data you want to check or change within the plug-in.

More information: 

- [Write plug-ins to extend business processes](../plug-ins.md)
- [Event Framework](../event-framework.md)

## Using custom actions

When you use a custom action, there are no classes in the SDK assemblies for these operations. You can generate classes for them using:

- For .NET projects using [PowerPlatform.Dataverse.Client.ServiceClient](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient), use the [pac modelbuilder](/power-platform/developer/cli/reference/modelbuilder) command that is part of the [Power Platform CLI](/power-platform/developer/cli/introduction). Use the [--generateActions](/power-platform/developer/cli/reference/modelbuilder#--generateactions--a) parameter to generate classes for custom actions.
- For .NET Framework projects, such as plug-ins, use `CrmSvcUtil.exe` code generation tool by using the `generateActions` parameter.


Alternatively, you can instantiate an <xref:Microsoft.Xrm.Sdk.OrganizationRequest> instance and set the <xref:Microsoft.Xrm.Sdk.OrganizationRequest.RequestName> and <xref:Microsoft.Xrm.Sdk.OrganizationRequest.Parameters> to use them without the generated classes. To work with the results, you'll parse the values returned from the <xref:Microsoft.Xrm.Sdk.OrganizationResponse>.<xref:Microsoft.Xrm.Sdk.OrganizationResponse.Results> property.

More information:

- [Generate classes for early-bound programming using the Organization service](generate-early-bound-classes.md)
- [Create your own messages](../custom-actions.md)

## Passing optional parameters with a request

There are several optional parameters you can pass to apply special behaviors to messages. More information: [Use optional parameters](../optional-parameters.md)

## Private Messages

Microsoft Dataverse contains some messages that aren't intended for third party developers to use. Microsoft added these messages enable feature functionality, but third party solutions can also add them with the Custom API feature. The [SdkMessage.IsPrivate](../reference/entities/sdkmessage.md#BKMK_IsPrivate) property tells you which messages are private.

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
