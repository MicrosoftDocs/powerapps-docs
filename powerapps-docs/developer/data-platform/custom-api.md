---
title: "Create and use custom APIs (Microsoft Dataverse) | Microsoft Docs"
description: "Custom API is a code-first way to define custom messages for Microsoft Dataverse"
author: MsSQLGirl
ms.author: jukoesma
ms.date: 01/09/2026
ms.reviewer: jdaly
ms.topic: how-to
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - SomaDaDe
---
# Create and use custom APIs

Use custom APIs to create your own APIs in Dataverse. You can consolidate one or more operations into a custom API that you and other developers can call in their code or from Power Automate. The [Microsoft Dataverse connector](/connectors/commondataserviceforapps/) enables calling  actions in Power Automate.

You can use custom API as business events to enable creating new integration capabilities such as exposing a new type of trigger event in the Microsoft Dataverse connector. [Learn more about Microsoft Dataverse business events](business-events.md).

Custom APIs are an alternative to custom process actions. Custom process actions provide a no-code way to include custom messages but have some limitations for developers. Custom APIs provide capabilities specifically for developers to define their logic in code with more options. For a full comparison of custom process action and custom API, see [Compare custom process action and custom API](custom-actions.md#compare-custom-process-action-and-custom-api).

## Create a custom API

A custom API usually includes logic implemented with a plug-in, but it isn't required. By using [Microsoft Dataverse business events](business-events.md), you can create a custom API without a plug-in to pass data about an event that other subscribers respond to.

Most of the time, you combine a custom API with a plug-in to define some operation that is delegated to Dataverse to compute and return the result.

You can create a custom API in several different ways:

|Method link|Benefit|
|---------|---------|
|[Plug-in registration tool](create-custom-api-prt.md)|An easy-to-use GUI tool integrated with tools used to develop plug-ins.|
|[Power Apps](create-custom-api-maker-portal.md)|Using forms to enter data. You don't need to install a separate tool, you must create a separate record for each part of the custom API.|
|[With Code](create-custom-api-with-code.md)|After you understand the data model, you can create custom API quickly using an API Client like Postman or [Insomnia](webapi/insomnia.md). Or you can build your own experience to create custom API.|
|[With solution files](create-custom-api-solution.md)|When you use Application Lifecycle Management (ALM) tools, you can create or modify custom API definitions with XML files in a solution that is included in your source code repository. The custom API is created when you import the solution generated from your source code.|

> [!NOTE]
> Although custom API data is stored in tables, creating a model-driven app for these tables isn't supported.
>
> These tools are created and supported by the community to work with custom API:
> - [Dataverse Custom API Manager](https://www.xrmtoolbox.com/plugins/XTB.CustomApiManager/)
> - [Custom API Tester](https://www.xrmtoolbox.com/plugins/Rappen.XrmToolBox.CustomAPITester/)
> - [Custom Action to Custom API Converter](https://www.xrmtoolbox.com/plugins/MarkMpn.CustomActionToApiConverter/)
>
> Microsoft doesn't support community-created tools. If you have questions or issues with community tools, contact the publisher of the tool.

## Custom API customization

When you create a custom API and related request parameters and response properties, understand that these API definitions are customizable by default. If they're customizable, you can iterate and make changes to these items in your unmanaged solution.

> [!IMPORTANT]
> When you ship or deploy your solution, use a managed solution and always set the **Is Customizable** managed property to `false` for these components. This setting prevents people using your managed solution from modifying or deleting these components. Such changes could break code written for the original definition of the custom API.

### Set Is Customizable to false

Set the **Is Customizable** managed property from the solution in Power Apps.

:::image type="content" source="media/set-custom-api-iscustomizable-managed-property.png" alt-text="Setting Is Customizable Managed Property":::

Set this property for each custom API, request parameter, and response property individually.

[Learn more about Managed properties](/power-platform/alm/managed-properties-alm).

### Add more request parameters and response properties

Even when you set the **Is Customizable** managed property to `false`, you can add new request parameters and response properties to your custom API. However, the people who add these request parameters can't make them required. If you [choose to allow custom processing steps on your custom API](#select-a-custom-processing-step-type), other plug-ins registered for the message created by your custom API can use them. Because custom request parameters are only optional, the plug-in you provide for the main operation of the custom API can ignore them and isn't responsible for using any custom request parameters or setting any custom response properties added to the custom API you specified.

## Custom API tables and entities

For information about the tables and column values to use when creating custom APIs, see [CustomAPI tables](custom-api-tables.md).


## Select a custom processing step type

The following table describes which custom API **Custom Processing Step Type** (`AllowedCustomProcessingStepType`) to use. 

|Option |When to use  |
|---------|---------|
|**None**|Use when the plug-in set for this custom API by using [CustomAPI.PluginTypeId](reference/entities/customapi.md#BKMK_PluginTypeId) is the only logic that occurs when this operation executes.<br/>You don't allow other developers to register any more steps that can trigger other logic, modify the behavior of this operation, or cancel the operation.<br/>Use this option when the custom API provides some capability that shouldn't be customizable.|
|**Async Only**|Use when you want to allow other developers to detect when this operation occurs, but you don't want them to be able to cancel the operation or customize the behavior of the operation.<br/> Other developers can register asynchronous steps to detect that this operation occurred and respond to it after it finishes.<br/>This option is recommended if you're using the business events pattern. A business event creates a trigger in Power Automate that you can use when this event occurs. [Learn about Microsoft Dataverse business events](business-events.md)|
|**Sync and Async**|Use when you want to allow other developers to change the behavior of the operation, and even cancel it if their business logic dictates.<br/>If the operation succeeds, other developers can also detect this event and add logic to run asynchronously.<br/>Most Dataverse messages enable extension in this manner.  Use this option when your message represents a business process that should be customizable.|

## Select a binding type

Binding is an OData concept that associates an operation to a specific table. The following table describes the custom API **Binding Type** (`BindingType`) you should use.

|Option |When to use  |
|---------|---------|
|**Global** |When the operation doesn't apply to a specific table.|
|**Entity**|When the operation accepts a single record of a specific table as a parameter.|
|**EntityCollection**|When the operation applies changes to, or returns a collection of a specific table.|

Selecting **Entity** or **EntityCollection** requires that you use the fully qualified name of the Function or Action when you use the Web API. The fully qualified name is `Microsoft.Dynamics.CRM.<UniqueName of the custom API>`. 

When you select **Entity**, a request parameter named `Target` with the type <xref:Microsoft.Xrm.Sdk.EntityReference>  is created automatically. You don't need to create it. This value is passed to any plug-ins registered for this message.

When you select **EntityCollection**, no parameter or response property representing the entity collection is included. Setting this binding simply adds the requirement that the operation be invoked appended to the entityset when using the Web API.

> [!NOTE]
> These binding types are available for you to use when composing your custom API, but it's not required that you bind to an entity or entity collection. You can compose all your custom API as **Global** and add whichever request parameters or response properties you need to achieve the same functionality as a bound Function or Action.

More information:
 - [Actions bound to a table](webapi/use-web-api-actions.md#actions-bound-to-a-table)
 - [Actions bound to a table collection](webapi/use-web-api-actions.md#actions-bound-to-a-table-collection)
 - [Bound functions](webapi/use-web-api-functions.md#bound-functions)

## When to create a Function

The custom API **Is Function** property controls whether the custom API is a *Function* or *Action*. In OData, a Function is an operation you call by using an HTTP `GET` request. It returns data without making any changes. By using a `GET` request, you pass all the parameters in the URL when you invoke the function.

You can more easily test `GET` requests by using your browser alone, but there's a 32 KB (32,768 characters) limit to the length of the URL you can send. If your custom API has many complex request parameters that could cause the length of the URL to be too long, it's acceptable to create an Action that performs the same operation and passes all the parameter data in the body by using a `POST` request.

> [!NOTE]
> - Functions must return some data. You must include at least one response property for the custom API to be valid.
>    - A function that doesn't include a response property doesn't appear within the Web API $metadata service document.
>    - If you try to use an invalid function, you get a `404 Not found` error similar to this:<br />`{"error":{"code":"0x8006088a","message":"Resource not found for the segment 'your_function_name'."}}`
> - You can't use a Function when you select the **Enabled for Workflow** option. See [Use a custom API in a workflow](#use-a-custom-api-in-a-workflow).
> - Currently, the [Microsoft Dataverse Connector](/connectors/commondataserviceforapps/) only enables performing actions. If you need the operation to be performed by using Power Automate, you should create your custom API as an Action.

[Learn to use Web API functions](webapi/use-web-api-functions.md)

## When to make your custom API private

By default, other developers can discover and use any custom API you create. As the custom API publisher, you're responsible for maintaining the public APIs you create. Don't remove your API or apply any changes that break other consumers.

If you aren't willing to support other developers using your custom API, set the custom API **Is Private** (`IsPrivate`) property to true before shipping the managed solution that contains your custom API.

The **Is Private** property blocks the custom API from appearing within the $metadata service document and prevents Dataverse code generation tools from creating classes to use the messages for your custom API.

Setting this property doesn't mean that other developers can't use your message if they know about it and can compose a request to use it. Setting the **Is Private** property indicates that you don't support other developers using your message. 

You might want to keep a custom API private until you're sure that you won't need to remove it or introduce some breaking change.

Leave **Is Private** set to false in your development environment so you can see the output in the $metadata service document or generate classes for your own use. However, set **Is Private** to true before shipping the custom API in your managed solution.

More information: 
- [CSDL $metadata document](webapi/web-api-service-documents.md#csdl-metadata-document)
- [Generate early-bound classes for the SDK for .NET](org-service/generate-early-bound-classes.md)
- [Private Messages](org-service/use-messages.md#private-messages)

## Secure your custom API by requiring a privilege

Set the custom API **Execute Privilege Name** (`ExecutePrivilegeName`) property to the name of the privilege to require it. Currently, there's no supported way for developers outside of Microsoft to create new privileges, but you can use an existing privilege. For more information, see [Q: Can I create a new privilege for my custom API?](custom-api.md#q-can-i-create-a-new-privilege-for-my-custom-api) 

## Use a plug-in to include logic in your custom API

If you don't set the custom API **Plugin Type** (`PluginTypeId`) to specify main operation logic, users can still invoke the custom API.

You might choose to not include any logic in the plug-in because you're using the custom API as a business event. [Learn about Microsoft Dataverse business events](business-events.md).

You might not want to add a plug-in as a testing step. Without a plug-in, any output parameter values return the default values for the type because there's no code to set them. Otherwise, see [Write a Plug-in for your custom API](#write-a-plug-in-for-your-custom-api).

> [!NOTE]
> You can't pass configuration data to the plug-in specified for the main operation logic. [There is a workaround for this](#secure-and-unsecure-configuration-cant-be-set-for-the-custom-api-main-operation-plug-in).

## Use a custom API in a workflow

Set the custom API **Enabled for Workflow** (`WorkflowSdkStepEnabled`) to true when you need to enable calling a custom API as a workflow action. However, this option adds the following limitations so that the custom API can be called in the workflow designer:

- The custom API can't be a function. **Is Function** must be false.
- The custom API can only have request parameter or response property types that workflow supports:
  - Boolean
  - DateTime
  - Decimal
  - EntityReference
    - EntityReference can only be used when the custom API is bound to an entity.
  - Float
  - Integer
  - Money
  - Picklist
  - String
  - Guid
  
  The following request parameter or response property types can't be used:
  - Entity
  - EntityCollection
  - StringArray



## Invoking custom APIs

A custom API creates a new message that users can invoke through the Web API or Dataverse SDK for .NET just like any other operation.

### Invoking custom APIs from the Web API

While testing, you can invoke your API by using an API client like Postman or Insomnia. To set up an Insomnia environment that generates the access token you need, see [Use Insomnia with Dataverse Web API](webapi/insomnia.md). If your API is an action, follow the steps in [Use Web API actions](webapi/use-web-api-actions.md). If your API is a function, follow the steps in [Use Web API functions](webapi/use-web-api-functions.md).

See the following examples:

#### Unbound action

This action is named `myapi_CustomUnboundAPI`. It has a single string request parameter named `InputParameter`:

```http
POST [Organization URI]/api/data/v9.1/myapi_CustomUnboundAPI
OData-MaxVersion: 4.0
OData-Version: 4.0
Content-Type: application/json; charset=utf-8

{
  "InputParameter": "Value"
}
```

#### Function bound to table

This function named `myapi_CustomBoundAPI` is bound to the account table:

```http
GET [Organization URI]/api/v9.1/accounts(ed5d4e42-850c-45b7-8b38-2677545107cc)/Microsoft.Dynamics.CRM.myapi_CustomBoundAPI()
OData-MaxVersion: 4.0
OData-Version: 4.0
Content-Type: application/json; charset=utf-8
```

#### Function bound to table collection

This function named `myapi_CustomEntityCollectionBoundAPI` is bound to the account table collection:

```http
GET [Organization URI]/api/v9.1/accounts/Microsoft.Dynamics.CRM.myapi_CustomEntityCollectionBoundAPI()
OData-MaxVersion: 4.0
OData-Version: 4.0
Content-Type: application/json; charset=utf-8
```

More information:

- [Use Web API actions](webapi/use-web-api-actions.md)
- [Use Web API functions](webapi/use-web-api-functions.md)

### Invoke custom APIs from the SDK for .NET

To invoke your custom API, use either early-bound or late-bound code. Use the [pac modelbuilder build](/power-platform/developer/cli/reference/modelbuilder#pac-modelbuilder-build) tool to generate helper request and response classes that expose the request parameters and response properties of your custom API. [Learn more about generating early-bound classes for the SDK for .NET](org-service/generate-early-bound-classes.md).

For late-bound code, or for a custom API that you mark as private, create an `OrganizationRequest` with the unique name of your custom API. Add parameters with names that match the unique names of the request properties.

Entity-bound custom APIs have an implicit request property named `Target`. Set this property to an `EntityReference` of the record to invoke the API on.

You can access response properties from the parameters of the returned response.

In this example, a custom API named `myapi_EscalateCase` is bound to the incident table to accept a record as the `Target` parameter together with another option set value request parameter named `Priority`. It has an `EntityReference` response property named `AssignedTo`    .

```csharp
var req = new OrganizationRequest("myapi_EscalateCase")
{
  ["Target"] = new EntityReference("incident", guid),
  ["Priority"] = new OptionSetValue(1)
};

var resp = svc.Execute(req);

var newOwner = (EntityReference) resp["AssignedTo"];
```

[Learn to use messages with the SDK for .NET](org-service/use-messages.md).

### Invoke custom API as a background operation

The logic to perform by using a background operation must be defined as a custom API.[Learn to use background operations (Preview)](background-operations.md)

## Write a plug-in for your custom API

Writing a plug-in to implement the main operation for your custom API isn't different from writing any other plug-in. However, don't use the Plug-in Registration tool to set a specific step, and [you can't specify configuration data to pass to the plug-in](#secure-and-unsecure-configuration-cant-be-set-for-the-custom-api-main-operation-plug-in).

You need to know the following information:

- The name of the message.
- The names and types of the request parameters and response properties.

The Request Parameter values are included in the [InputParameters](understand-the-data-context.md#inputparameters).

Set the values for the Response Properties in the [OutputParameters](understand-the-data-context.md#outputparameters).

The following code is a simple plug-in that reverses the characters in the `StringParameter` and returns the result as the `StringProperty`.

```csharp
using System;
using System.Linq;
using System.ServiceModel;
using Microsoft.Xrm.Sdk;

namespace CustomAPIExamples
{
    public class Sample_CustomAPIExample : IPlugin
    {
        public void Execute(IServiceProvider serviceProvider)
        {
            // Obtain the tracing service
            ITracingService tracingService =
            (ITracingService)serviceProvider.GetService(typeof(ITracingService));

            // Obtain the execution context from the service provider.  
            IPluginExecutionContext context = (IPluginExecutionContext)
                serviceProvider.GetService(typeof(IPluginExecutionContext));

            if (context.MessageName.Equals("sample_CustomAPIExample") && context.Stage.Equals(30)) {

                try
                {
                    string input = (string)context.InputParameters["StringParameter"];
                    
                    if (!string.IsNullOrEmpty(input)) {
                        //Simply reversing the characters of the string
                        context.OutputParameters["StringProperty"] = new string(input.Reverse().ToArray());
                    }
                }
                catch (Exception ex)
                {
                    tracingService.Trace("Sample_CustomAPIExample: {0}", ex.ToString());
                    throw new InvalidPluginExecutionException("An error occurred in Sample_CustomAPIExample.", ex);
                }
            }
            else
            {
                tracingService.Trace("Sample_CustomAPIExample plug-in is not associated with the expected message or is not registered for the main operation.");
            }
        }
    }
}

```

For more information about writing plug-ins, see [Tutorial: Write and register a plug-in](tutorial-write-plug-in.md). You need to register the assembly, but you don't need to register a step. [Learn to use a plug-in to include logic in your custom API](#use-a-plug-in-to-include-logic-in-your-custom-api).

See the example [Sample: IsSystemAdmin custom API](org-service/samples/issystemadmin-customapi-sample-plugin.md).

After you register the assembly, make sure to add the assembly and any types to your solution.



## Localized label values

Custom APIs have localizable labels. You can localize the label values by using the steps documented in [Translate localizable text for model-driven apps](../../maker/model-driven-apps/translate-localizable-text.md) and [Translating labels and display strings](/power-platform/alm/create-solutions-support-multiple-languages#translating-labels-and-display-strings).

This process involves exporting a file that contains the base language values and includes a column for each language enabled. You can then edit the values in Excel. After you complete the process to import the translations, the labels are included in your solution.

The following example shows editing the Excel worksheet to add Japanese translations for the English values.

:::image type="content" source="media/solution-strings-for-translation.png" alt-text="Shows how labels are localized.":::

> [!TIP]
> If you're editing the solution files to create your custom APIs, you can provide the localized labels directly. [Learn about providing Localized Labels with the solution](create-custom-api-solution.md#providing-localized-labels-with-the-solution)

### Setting localized values

If you prefer to set localized labels in code rather than using the manual process described earlier, use the `SetLocLabels` message by using either the Web API [SetLocLabels Action](xref:Microsoft.Dynamics.CRM.SetLocLabels) or the SDK for .NET <xref:Microsoft.Crm.Sdk.Messages.SetLocLabelsRequest>.

The following example shows how to use the Web API to set the localized labels for the `displayname` property of a custom API.

**Request:**

```http
POST [Organization URI]/api/data/v9.1/SetLocLabels HTTP/1.1
Accept: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
Content-Type: application/json

{
    "EntityMoniker": {
        "@odata.type": "Microsoft.Dynamics.CRM.customapi",
        "customapiid": "86bcd12e-2f30-eb11-a813-000d3a122b89"
    },
    "AttributeName": "displayname",
    "Labels": [
        {
            "Label": "例え",
            "LanguageCode": 1041
        },
        {
            "Label": "Beispiel",
            "LanguageCode": 1031
        },
        {
            "Label": "ejemplo",
            "LanguageCode": 1034
        }
    ]
}

```

**Response:**

```http
HTTP/1.1 204 No Content
```

### Retrieving localized values

To retrieve the localized labels, use the `RetrieveLocLabels` message by using either the Web API [RetrieveLocLabels Function](xref:Microsoft.Dynamics.CRM.RetrieveLocLabels) or the SDK for .NET [RetrieveLocLabelsRequest class](xref:Microsoft.Crm.Sdk.Messages.RetrieveLocLabelsRequest).

The following example shows how to use the RetrieveLocLabels Function to retrieve the labels for the `displayname` property of a custom API with the `customapiid` of `88602189-183d-4584-ba4b-8b60f0f5b89f`.

**Request:**

```http
GET [Organization URI]/api/data/v9.1/RetrieveLocLabels(EntityMoniker=@p1,AttributeName=@p2,IncludeUnpublished=@p3)?
@p1={'@odata.id':'customapis(88602189-183d-4584-ba4b-8b60f0f5b89f)'}&
@p2='displayname'&
@p3=false HTTP/1.1

```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
    "@odata.context": "[Organization URI]/api/data/v9.1/$metadata#Microsoft.Dynamics.CRM.RetrieveLocLabelsResponse",
    "Label": {
        "LocalizedLabels": [
            {
                "Label": "Custom API Example",
                "LanguageCode": 1033,
                "IsManaged": null,
                "MetadataId": null,
                "HasChanged": null
            },
            {
                "Label": "カスタムAPIの例",
                "LanguageCode": 1041,
                "IsManaged": null,
                "MetadataId": null,
                "HasChanged": null
            }
        ],
        "UserLocalizedLabel": {
            "Label": "Custom API Example",
            "LanguageCode": 1033,
            "IsManaged": null,
            "MetadataId": null,
            "HasChanged": null
        }
    }
}
```

## Frequently Asked Questions (FAQs)

The following questions and answers might help you:

### Q: Can I create a new privilege for my custom API?

A: While custom API has an **Execute Privilege Name** (`ExecutePrivilegeName`) property, there's currently no supported way to create a new privilege just for this API. This capability is planned for a future release. In the meantime, use one of the following options:

- Use an existing [Privilege.Name](./reference/entities/privilege.md#BKMK_Name) value.
- Create a custom entity and use one of the privileges created for that entity. For example, create an entity named `new_myaction` and privileges for CRUD operations generated for it. For example: `prvCreatenew_myaction`. Include this custom entity with the solution that includes the custom API.

### Q: Can I activate or deactivate custom API records?

A: You can't. Although these records have the common **Status** and **Status Reason** columns found on most Microsoft Dataverse tables, setting the values for these columns has no impact on the availability of the custom API, the request parameters, or the response properties.

### Q: How can I use my private messages if they aren't included in the Web API $metadata service document?

A: Your private messages work regardless of whether they're advertised in the Web API [CSDL $metadata document](webapi/web-api-service-documents.md#csdl-metadata-document) or not. While you develop your solution, set the `IsPrivate` value to `false`. You can refer to the `$metadata` listing and use code generation tools that depend on this data. However, set the `CustomAPI.IsPrivate` value to `true` before you ship your solution for others to use. If you later decide that you wish to support other applications to use the message, you can change the `CustomAPI.IsPrivate` value to `false`.

More information:

- [When to make your custom API private](#when-to-make-your-custom-api-private)
- [Private Messages](org-service/use-messages.md#private-messages)
- [Private messages can't be used in plug-ins](#private-messages-cant-be-used-in-plug-ins)

## Known issues with custom APIs

Custom APIs are now generally available, but some related capabilities might change.

### Not able to use profiler for debugging

To debug by using the Plug-in Registration tool and the Plug-in profiler solution, you need to select a specific plug-in step. The main stage implementation for the plug-in isn't currently available in the Plug-in Registration tool.

**Workaround**: Register the plug-in type on the `PostOperation` stage of the message created for the custom API.

### Private messages can't be used in plug-ins

If you define your custom API as private, you can't use that message in a plug-in. [Learn about private messages](org-service/use-messages.md#private-messages).

### You can't set secure and unsecure configuration for the custom API main operation plug-in

You can't pass [secure or unsecure configuration](write-plug-in.md#pass-configuration-data-to-your-plug-in) to the main operation plug-in for the custom API.

**Workaround**: Instead of associating the plug-in with the custom API, register the plug-in on the `PostOperation` stage by using the Plug-in Registration tool (PRT). By using this approach, you can [specify configuration data in the `PostOperation` plug-in step as you usually do](register-plug-in.md#set-configuration-data).

To use this workaround, you must configure your custom API to enable **Sync and Async** [custom processing step types](#select-a-custom-processing-step-type) when you create the custom API. You can't change this setting after you create it.

### Next Steps

[Create a custom API using the plug-in registration tool](create-custom-api-prt.md)

### See also

[Create and use custom APIs](custom-api.md)   
[Create a custom API with code](create-custom-api-with-code.md)   
[Create a custom API with solution files](create-custom-api-solution.md)  
[Create your own messages](custom-actions.md)   
[Custom API tables](custom-api-tables.md)   

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
