---
title: "Create and use custom APIs (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "custom API is a code-first way to define custom messages for Microsoft Dataverse" # 115-145 characters including spaces. This abstract displays in the search result.
author: divkamath
ms.author: dikamath
ms.date: 04/28/2023
ms.reviewer: jdaly
ms.topic: article
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
---
# Create and use custom APIs

Use custom APIs to create your own APIs in Dataverse. You can consolidate one or more operations into a custom API that you and other developers can call in their code or from Power Automate. The [Microsoft Dataverse connector](/connectors/commondataserviceforapps/) enables calling  actions in Power Automate.

You can use custom API as business events to enable creating new integration capabilities such as exposing a new type of trigger event in the Microsoft Dataverse connector. More information: [Microsoft Dataverse business events](business-events.md)

Custom APIs are an alternative to custom process actions. Custom process actions provide a no-code way to include custom messages but has some limitations for developers. Custom APIs provide capabilities specifically for developers to define their logic in code with more options. For a full comparison of custom process action and custom API, see [Compare custom process action and custom API](custom-actions.md#compare-custom-process-action-and-custom-api).

## Create a custom API

A custom API may include logic implemented with a plug-in. Using [Microsoft Dataverse business events](business-events.md), you may create a custom API without a plug-in to pass data about an event that other subscribers will respond to.

However, in other cases you will combine a custom API with a plug-in to define some operation that will delegated to Dataverse to compute and return the result.

There are several different ways to create a custom API:

|Method link|Benefit|
|---------|---------|
|[Plug-in registration tool](create-custom-api-prt.md)|An easy-to-use GUI tool integrated with tools used to develop plug-ins.|
|[Power Apps](create-custom-api-maker-portal.md)|Using forms to enter data. You don't need to install a separate tool, you must create a separate record for each part of the custom API.|
|[With Code](create-custom-api-with-code.md)|After you understand the data model, you can create custom API very quickly using Postman. Or you can build your own experience to create custom API.|
|[With solution files](create-custom-api-solution.md)|When you use Application Lifecycle Management (ALM) tools you can create or modify custom API definitions with XML files in a solution that is included in your source code repository. The custom API will be created when you import the solution generated from your source code.|

> [!NOTE]
> Although custom API data is stored in tables, we do not support creating a model-driven app for these tables.
>
> These are some of the tools created and supported by the community to work with custom API:
> - [Dataverse Custom API Manager](https://www.xrmtoolbox.com/plugins/XTB.CustomApiManager/)
> - [Custom API Tester](https://www.xrmtoolbox.com/plugins/Rappen.XrmToolBox.CustomAPITester/)
> - [Custom Action to Custom API Converter](https://www.xrmtoolbox.com/plugins/MarkMpn.CustomActionToApiConverter/)
>
> Tools created by the community are not supported by Microsoft. If you have questions or issues with community tools, contact the publisher of the tool.

## Custom API Customization

When creating custom API and related request parameters and response properties, it is important to understand that these API definitions are customizable by default. This is what allows you to iterate and make changes to these items in your unmanaged solution.

> [!IMPORTANT]
> When you ship or deploy your solution, you should use a managed solution and we recommend that you always set the **Is Customizable** managed property to these components to `false`. This will prevent people using your managed solution from modifying or deleting these components of your solution. Such changes could break code written for the original definition of the custom API.

### Set Is Customizable to false

You can set the **Is Customizable** managed property from the solution in Power Apps.

:::image type="content" source="media/set-custom-api-iscustomizable-managed-property.png" alt-text="Setting Is Customizable Managed Property":::

You will need to set this for each custom API, Request Parameter, and Response Property individually.

More information [Managed properties](/power-platform/alm/managed-properties-alm)

### Add additional request parameters and response properties

Even when you have set the **Is Customizable** managed property to these components to `false`, new request parameters and response properties can be added to your custom API. However, additional request parameters cannot be made required. If you choose to allow custom processing steps on your custom API, these additional parameters and properties added to the original definition can be used by other plug-ins registered for the message created by your custom API. Because custom request parameters can only be optional, the plug-in you provide for the main operation of the custom API can ignore them and is not responsible for using any custom request parameters or setting any custom response properties.

## Custom API tables/entities

See [CustomAPI tables](custom-api-tables.md) for information about the tables and column values to use when creating Custom APIs.


## Select a Custom Processing Step Type

The following table describes which custom API **Custom Processing Step Type** (`AllowedCustomProcessingStepType`) you should use. 

|Option |When to use  |
|---------|---------|
|**None**|When the plug-in set for this custom API using [CustomAPI.PluginTypeId](reference/entities/customapi.md#BKMK_PluginTypeId) will be the only logic that occurs when this operation executes.<br/>You will not allow another developer to register any additional steps that may trigger additional logic, modify the behavior of this operation, or cancel the operation.<br/>Use this when the custom API provides some capability that should not be customizable.|
|**Async Only**|When you want to allow other developers to detect when this operation occurs, but you do not want them to be able to cancel the operation or customize the behavior of the operation.<br/> Other developers can register asynchronous steps to detect that this operation occurred and respond to it after it has completed.<br/>This is the option recommended if you are using the business events pattern. A business event will create a trigger in Power Automate to you can use when this event occurs. More information: [Microsoft Dataverse business events](business-events.md)|
|**Sync and Async**|When you want to allow other developers to have the ability to change the behavior of the operation and even cancel it if their business logic dictates.<br/>If the operation succeeds, other developers can also detect this and add logic to run asynchronously.<br/>Most Dataverse messages enable extension in this manner.  Use this when your message represents a business process that should be customizable.|

## Select a Binding Type

Binding is an OData concept that associates an operation to a specific table. The following table describes the custom API **Binding Type** (`BindingType`) you should use.

|Option |When to use  |
|---------|---------|
|**Global** |When the operation does not apply to a specific table.|
|**Entity**|When the operation accepts a single record of a specific table as a parameter.|
|**EntityCollection**|When the operation applies changes to, or returns a collection of a specific table.|

Selecting **Entity** or **EntityCollection** will require that you use the fully qualified name of the Function or Action when you use the Web API. The fully qualified name is `Microsoft.Dynamics.CRM.<UniqueName of the custom API>`. 

When you select **Entity**, a request parameter named `Target` with the type <xref:Microsoft.Xrm.Sdk.EntityReference>  is created automatically. You do not need to create it. This value will be passed to any plug-ins registered for this message.

When you select **EntityCollection**, no parameter or response property representing the entity collection is included. Setting this binding simply adds the requirement that the operation be invoked appended to the entityset when using the Web API.

> [!NOTE]
> These binding types are available for you to use when composing your custom API, but it is not required that you bind to an entity or entity collection. You can compose all your custom API as **Global** and add whichever request parameters or response properties you need to achieve the same functionality as a bound Function or Action.

More information:
 - [Actions bound to a table](webapi/use-web-api-actions.md#actions-bound-to-a-table)
 - [Actions bound to a table collection](webapi/use-web-api-actions.md#actions-bound-to-a-table-collection)
 - [Bound functions](webapi/use-web-api-functions.md#bound-functions)

## When to create a Function

The custom API **Is Function** property controls whether the custom API will be a *Function* or *Action*. In OData a Function is an operation called using HTTP `GET` request which returns data without making any changes. With a `GET` request, all the parameters are passed as parameters in the URL when invoking the function.

You can more easily test `GET` requests using your browser alone, but there is a limit to the length of the URL that can be sent, usually around 2000 characters. If your custom API has many complex request parameters which could cause the length of the URL to be too long, it is acceptable to create an Action that performs the same operation passing all the parameter data in the body using a `POST` request.

> [!NOTE]
> - Functions must return some data. You must include at least one response property for the custom API to be valid.
>    - A function that does not include a response property will not appear within the Web API $metadata service document.
>    - If you try to use an invalid function, you will get a `404 Not found` error similar to this:<br />`{"error":{"code":"0x8006088a","message":"Resource not found for the segment 'your_function_name'."}}`
> - A Function is not allowed when the **Enabled for Workflow** option is selected. See [Use a custom API in a workflow](#use-a-custom-api-in-a-workflow)
> - Currently the [Microsoft Dataverse Connector](/connectors/commondataserviceforapps/) only enables performing actions. If you need the operation to be performed using Power Automate, you should create your custom API as an Action.

More information: [Use Web API functions](webapi/use-web-api-functions.md)

## When to make your custom API private

By default any custom API you create will be available for other developers to discover and use. As the custom API publisher, you have an obligation to maintain the public APIs you create. You should not remove your API or apply any changes which will break other consumers.

If you are not willing to support other developers using your custom API, you should set the custom API **Is Private** (`IsPrivate`) property to true before you ship the managed solution containing your custom API.

The **Is Private** property will block the custom API from appearing within the $metadata service document and prevent Dataverse code generation tools from creating classes to use the messages for your custom API.

This doesn't mean that other developers cannot use your message if they know about it and are able to compose a request to use it. Setting the **Is Private** property is a way to indicate that you do not support other developers using your message. 

You may want to keep a custom API private until you are sure that you will not need to remove it or introduce some breaking change.

You can leave **Is Private** set to false in your development environment so you can see the output in the $metadata service document or generate classes for your own use. However, before you ship the custom API in your managed solution, you should set **Is Private** to true.

More information: 
- [CSDL $metadata document](webapi/web-api-service-documents.md#csdl-metadata-document)
- [Generate early-bound classes for the Organization service](org-service/generate-early-bound-classes.md)
- [Private Messages](org-service/use-messages.md#private-messages)

## Secure your custom API with a privilege

Set the custom API **Execute Privilege Name** (`ExecutePrivilegeName`) property to the name of the privilege to require it. There is currently no supported way for developers outside of Microsoft to create new privileges, but an existing privilege can be used. More information: [Q: Can I create a new privilege for my custom API?](custom-api.md#q-can-i-create-a-new-privilege-for-my-custom-api) 

## Use a plug-in to include logic in your custom API

If you do not set the custom API **Plugin Type** (`PluginTypeId`)  to specify main operation logic you can still invoke the custom API.

You may choose to not include any logic in the plug-in because you are using the custom API as a business event. More information: [Microsoft Dataverse business events](business-events.md).

You might want to do this as a testing step, but any output parameter values will return the default values for the type because there is no code to set them.

## Use a custom API in a workflow

Set the custom API **Enabled for Workflow** (`WorkflowSdkStepEnabled`) to true when you need to enable calling a custom API as a workflow action. However, when this is selected the following limitations are imposed so that the custom API can be called in the workflow designer:

- The custom API cannot be a function, **Is Function** must be false.
- The custom API can only have request parameter or response property types that workflow supports:
  - Boolean
  - DateTime
  - Decimal
  - EntityReference
    - EntityReference can only be used when the custom API is bound to to an entity.
  - Float
  - Integer
  - Money
  - Picklist
  - String
  - Guid
  
  The following request parameter or response property types cannot be used:
  - Entity
  - EntityCollection
  - StringArray



## Invoking custom APIs

A custom API creates a new message which can be invoked via the Web API or Dataverse SDK for .NET just like any other operation.

### Invoking custom APIs from the Web API

While testing, you can invoke your API using PostMan. Use the steps described in [Set up a Postman environment](webapi/setup-postman-environment.md) to set up a PostMan environment that will generate the access token you will need. Then, apply the steps described in [Use Web API actions](webapi/use-web-api-actions.md) if your API is an action. If it is a function, use the steps in [Use Web API functions](webapi/use-web-api-functions.md).

See the following examples:

#### Unbound Action

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

### Invoking custom APIs from the Organization Service

You can choose to use either early-bound or late-bound code to invoke your custom API. Use the [CrmSvcUtil](./org-service/generate-early-bound-classes.md) tool to generate helper request and response classes to expose the request parameters and response properties of your custom API.

For late-bound code, or for a custom API that you have marked as private, create an `OrganizationRequest` with the unique name of your custom API and add parameters with names matching the unique names of the request properties.

Entity-bound custom APIs have an implicit request property named `Target` that should be set to an `EntityReference` of the record to invoke the API on.

You can access response properties from the parameters of the returned response.

In this example a custom API named `myapi_EscalateCase` is bound to the incident table to accept a record as the `Target` parameter together with another option set value request parameter named `Priority`. It has an `EntityReference` response property named `AssignedTo`    .

```csharp
var req = new OrganizationRequest("myapi_EscalateCase")
{
  ["Target"] = new EntityReference("incident", guid),
  ["Priority"] = new OptionSetValue(1)
};

var resp = svc.Execute(req);

var newOwner = (EntityReference) resp["AssignedTo"];
```

More information: [Use messages with the Organization service](org-service/use-messages.md).

### Invoke custom API as a background operation

The logic to be performed using a background operation must be defined as a custom API. More information:[Background operations (Preview)](background-operations.md)

## Write a Plug-in for your custom API

Writing a plug-in to implement the main operation for your custom API isn't different from writing any other kind of plug-in, except that you do not use the Plug-in Registration tool to set a specific step.

You need to know the following information:

- The name of the message
- The names and types of the request parameters and response properties.

The Request Parameter values will be included in the [InputParameters](understand-the-data-context.md#inputparameters).

You need to set the values for the Response Properties in the [OutputParameters](understand-the-data-context.md#outputparameters).

The following is a simple plug-in that reverses the characters in the `StringParameter` and returns the result as the `StringProperty`.

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

For more information about writing plug-ins, see [Tutorial: Write and register a plug-in](tutorial-write-plug-in.md). You need to register the assembly, but you do not need to register a step. More information: [Use a plug-in to include logic in your custom API](#use-a-plug-in-to-include-logic-in-your-custom-api)

See the example [Sample: IsSystemAdmin custom API](org-service/samples/issystemadmin-customapi-sample-plugin.md)

After you have registered the assembly, make sure to add the assembly and any types to your solution.



## Localized Label values

Custom APIs have some localizable labels. You can localize the label values using the steps documented here: [Translate localizable text for model-driven apps](../../maker/model-driven-apps/translate-localizable-text.md) and [Translating labels and display strings](/power-platform/alm/create-solutions-support-multiple-languages#translating-labels-and-display-strings).

This process involves exporting a file that contains the base language values and will include a column for each additional language enabled. You can then edit the values in Excel. After you complete the process to import the translations the labels will be included in your solution.

The following example shows editing the Excel worksheet to add Japanese translations for the English values.

:::image type="content" source="media/solution-strings-for-translation.png" alt-text="Shows how labels are localized.":::

> [!TIP]
> If you are editing the solution files to create your custom APIs, you can provide the localized labels directly. More information: [Providing Localized Labels with the solution](create-custom-api-solution.md#providing-localized-labels-with-the-solution)

### Setting localized values

If you prefer to set localized labels in code rather than using the manual process described above, you can use the `SetLocLabels` message using either the Web API [SetLocLabels Action](/dynamics365/customer-engagement/web-api/setloclabels) or the Organization Service <xref:Microsoft.Crm.Sdk.Messages.SetLocLabelsRequest>.

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

To retrieve the localized labels use the `RetrieveLocLabels` message using either the Web API [RetrieveLocLabels Function](/dynamics365/customer-engagement/web-api/retrieveloclabels) or the Organization Service <xref:Microsoft.Crm.Sdk.Messages.RetrieveLocLabelsRequest>.

The following example shows using the RetrieveLocLabels Function to retrieve the labels for the `displayname` property of a custom API with the `customapiid` of `88602189-183d-4584-ba4b-8b60f0f5b89f`

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

The following represent questions you may have:

### Q: Can I create a new privilege for my custom API?

A: While custom API has an **Execute Privilege Name** (`ExecutePrivilegeName`) property, there is currently no supported way for you to create a new privilege just for this API. This is planned for a future release. In the meantime, there are two options:

- You can use an existing [Privilege.Name](./reference/entities/privilege.md#BKMK_Name) value.
- You can create a custom entity and use one of the privileges created for that entity. For example, create an entity named `new_myaction` and privileges for CRUD operations will be generated for it. For example `prvCreatenew_myaction`. You will need to include this custom entity with the solution that includes the custom API.

### Q: Can I activate or deactivate custom API records?

A: You cannot. Although these records have the common **Status** and **Status Reason** columns found on most Microsoft Dataverse tables. Setting the values for these columns has no impact on the availability of the custom API, the request parameters, or the response properties.

### Q: How can I use my private messages if they are not included in the Web API $metadata service document?

A: Your private messages will work regardless of whether they are advertised in the Web API [CSDL $metadata document](webapi/web-api-service-documents.md#csdl-metadata-document) or not. While you develop your solution, you can leave the `IsPrivate` value set to `false`. This way you can refer to the `$metadata` listing and use code generation tools that depend on this data. However, you should set the `CustomAPI.IsPrivate` value to `true` before you ship your solution for others to use. If you later decide that you wish to support other applications to use the message, you can change the `CustomAPI.IsPrivate` value to `false`.

More information:

- [When to make your custom API private](#when-to-make-your-custom-api-private)
- [Private Messages](org-service/use-messages.md#private-messages)
- [Private messages cannot be used in plug-ins](#private-messages-cannot-be-used-in-plug-ins)

## Known issues with custom APIs

Custom API is now generally available, but there are still some related capabilities that we expect to change.

### Not able to use profiler for debugging

To debug using the Plug-in Registration tool and the Plug-in profiler solution, you need to be able to select a specific plug-in step. The main stage implementation for the plug-in is not currently available in the Plug-in Registration tool.

**Workaround**: Register the plug-in type on the `PostOperation` stage of the message created for the custom API.

### Private messages cannot be used in plug-ins

If you define your custom API to be private, you cannot use that message in a plug-in. More information: [Private Messages](org-service/use-messages.md#private-messages)

### Next Steps

[Create a custom API using the plug-in registration tool](create-custom-api-prt.md)<br />

### See also

[Create and use custom APIs](custom-api.md)<br />
[Create a custom API with code](create-custom-api-with-code.md)<br />
[Create a custom API with solution files](create-custom-api-solution.md)<br />
[Create your own messages](custom-actions.md)<br />
[Custom API tables](custom-api-tables.md)<br />

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
