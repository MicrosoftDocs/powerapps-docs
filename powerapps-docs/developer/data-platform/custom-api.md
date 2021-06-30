---
title: "Create and use Custom APIs (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Custom API is a new code-first way to define custom messages for the Microsoft Dataverse" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 06/29/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "sunilg" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Create and use Custom APIs 

Use Custom APIs to create your own APIs in Dataverse. With a Custom API you can consolidate a group of operations into an API that you and other developers can call in their code. The Microsoft Dataverse connector enables calling Custom APIs actions in Power Automate. Custom API also can be used as business events to enable creating new integration capabilities such as exposing a new type of trigger event in the Microsoft Dataverse connector. More information: [Microsoft Dataverse business events (preview)](business-events.md)

Operations in Dataverse are defined as *messages*. Custom APIs offer a code-first way to define messages that you can add to Dataverse web services. Custom APIs are an alternative to Custom Process Actions that provide a no-code way to include custom messages.

Custom APIs provide a capabilities specifically for developers to define their logic in code. For a full comparison of Custom Process Action and Custom API, see [Compare Custom Process Action and Custom API](custom-actions.md#compare-custom-process-action-and-custom-api).

## Create a custom API

A Custom API may or may not include logic implemented with a plug-in. Using Dataverse business events, you may create a Custom API to pass data about an event that other subscribers will respond to.

However, in other cases it is expected that the message you create performs some kind of logic using a plug-in. You can approach the development of your custom API by:

- Write the plug-in first, and then define the Custom API for it.
- Define the Custom API first, then write the plug-in to implement it.

Your Custom API will be completed when the data defining the Custom API is saved and linked to the Plug-in type to define the main operation. In either case, you should understand the data that drives the Custom API.

There are several different ways to create a custom API:

- By manually entering data in available forms.  More information: [Create a Custom API in the maker portal](create-custom-api-maker-portal.md)
- By using the web services, such as the Web API or Organization Service. More information: [Create a Custom API with code](create-custom-api-with-code.md)
- By editing solution files. More information: [Create a Custom API with solution files](create-custom-api-solution.md).

> [!NOTE]
> Although Custom API data is stored in tables, we do not support creating a model-driven app for these tables. A designer is planned for a future release.
> 
> There are several tools created and supported by the community to work with Custom API:
> - [Dataverse Custom API Manager](https://www.xrmtoolbox.com/plugins/XTB.CustomApiManager/)
> - [Custom API Tester](https://www.xrmtoolbox.com/plugins/Rappen.XrmToolBox.CustomAPITester/)
> - [Custom Action to Custom API Converter](https://www.xrmtoolbox.com/plugins/MarkMpn.CustomActionToApiConverter/)

### Custom API Customization

When creating Custom API and related request parameters and response properties, it is important to understand that these API definitions are customizable by default. This is what allows you to iterate and make changes to these items in your unmanaged solution.

> [!IMPORTANT]
> When you ship or deploy your solution, you should use a managed solution and we recommend that you always set the **Is Customizable** managed property to these components to `false`. This will prevent people using your managed solution from modifying or deleting these components of your solution. Such changes could break code written for the original definition of the Custom API. More information [Managed properties](/power-platform/alm/managed-properties-alm)

Even when you have set the **Is Customizable** managed property to these components to `false`, new request parameters and response properties can be added to your Custom API. However, additional request parameters cannot be made required. If you choose to allow custom processing steps on your custom api, these additional parameters and properties added to the original definition can be used by other plug-ins registered for the message created by your custom api. Because custom request parameters can only be optional, the plug-in you provide for the main operation of the custom api can ignore them and is not responsible for setting any custom response properties.

## Custom API tables/entities

The data that defines Custom APIs is in the following tables/entities:

- [CustomAPI table/entity reference](reference/entities/customapi.md)
- [CustomAPIRequestParameter table/entity reference](reference/entities/customapirequestparameter.md)
- [CustomAPIResponseProperty table/entity reference](reference/entities/customapiresponseproperty.md)

See the following topics for detailed information about the columns/attributes you can set for these tables/entities. You should review this as you plan the behavior for your Custom API.

- [CustomAPI Table Columns](customapi-table-columns.md)
- [CustomAPIRequestParameter Table Columns](customapirequestparameter-table-columns.md)
- [CustomAPIResponseProperty Table Columns](customapiresponseproperty-table-columns.md)


## Invoking Custom APIs

A Custom API creates a new message which can be invoked via the Web API or Organization Service SDK.

### Invoking Custom APIs from the Web API

While testing, you can invoke your API using PostMan. Use the steps described in [Set up a Postman environment](webapi/setup-postman-environment.md) to set up a PostMan environment that will generate the access token you will need. Then, apply the steps described in [Use Web API actions](webapi/use-web-api-actions.md) if your API is an action. If it is a function, use the steps in [Use Web API functions](webapi/use-web-api-functions.md).

This is an example invoking a Custom API Action named `myapi_CustomUnboundAPI` which has a single string request parameter named `InputParameter`:

```http
POST [Organization URI]/api/data/v9.1/myapi_CustomUnboundAPI
OData-MaxVersion: 4.0
OData-Version: 4.0
Content-Type: application/json; charset=utf-8

{
  "InputParameter": "Value"
}
```

This is an example invoking a Custom API Function bound to the account entity named `myapi_CustomBoundAPI`:

```http
GET [Organization URI]/api/v9.1/accounts(ed5d4e42-850c-45b7-8b38-2677545107cc)/Microsoft.Dynamics.CRM.myapi_CustomBoundAPI()
OData-MaxVersion: 4.0
OData-Version: 4.0
Content-Type: application/json; charset=utf-8
```

This is an example invoking a Custom API Function bound to the account entity collection named `myapi_CustomEntityCollectionBoundAPI`:

```http
GET [Organization URI]/api/v9.1/accounts/Microsoft.Dynamics.CRM.myapi_CustomEntityCollectionBoundAPI()
OData-MaxVersion: 4.0
OData-Version: 4.0
Content-Type: application/json; charset=utf-8
```


More information:
 - [Use Web API actions](webapi/use-web-api-actions.md)
 - [Use Web API functions](webapi/use-web-api-functions.md)



### Invoking Custom APIs from the Organization Service

You can choose to use either early-bound or late-bound code to invoke your custom API. Use the [CrmSvcUtil](./org-service/generate-early-bound-classes.md) tool to generate helper request and response classes to mirror the request and response properties of your custom API.

For late-bound code, or for a Custom API that you have marked as private, create an `OrganizationRequest` with the unique name of your custom API and add parameters with names matching the unique names of the request properties.

Entity-bound custom APIs have an implicit request property named `Target` that should be set to an `EntityReference` of the record to invoke the API on.

You can access response properties from the parameters of the returned response.

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


## Write a Plug-in for your Custom API

Writing a plug-in to implement the main operation for your Custom API isn't different from writing any other kind of plug-in, except that you do not use the Plug-in Registration tool to set a specific step.
You need to know the following information:

- The name of the message
- The names and types of the parameters and properties.

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

For more information about writing plug-ins, see [Tutorial: Write and register a plug-in](tutorial-write-plug-in.md). You need to register the assembly, but you do not need to register a step.

After you have registered the assembly, make sure to add the assembly and any types to your solution.


## Retrieve data about Custom APIs

You can use the following queries to retrieve data about Custom APIs.

### Web API

 More information: [Query Data using the Web API](webapi/query-data-web-api.md)

```http
GET [Organization URI]/api/data/v9.1/customapis?$select=
    uniquename,
    allowedcustomprocessingsteptype,
    bindingtype,
    boundentitylogicalname,
    description,
    displayname,
    executeprivilegename,
    iscustomizable,
    isfunction,
    isprivate,
    workflowsdkstepenabled
  &$expand=
  CustomAPIRequestParameters($select=
    uniquename,
    name,
    description,
    displayname,
    type,
    logicalentityname,
    iscustomizable,
    isoptional),
  CustomAPIResponseProperties($select=
    uniquename,
    name,
    description,
    displayname,
    iscustomizable,
    type,
    logicalentityname),
  PluginTypeId($select=
    plugintypeid,
    typename,
    version,
    name,
    assemblyname)
```

### FetchXml

More information: [Use FetchXML to construct a query](use-fetchxml-construct-query.md)

```xml
<fetch>
  <entity name='customapi' >
    <attribute name='isprivate' />
    <attribute name='description' />
    <attribute name='displayname' />
    <attribute name='executeprivilegename' />
    <attribute name='iscustomizable' />
    <attribute name='isfunction' />
    <attribute name='allowedcustomprocessingsteptype' />
    <attribute name='boundentitylogicalname' />
    <attribute name='bindingtype' />
    <attribute name='uniquename' />
    <attribute name='workflowsdkstepenabled' />
    <link-entity name='customapirequestparameter' from='customapiid' to='customapiid' link-type='outer' alias='req' >
      <attribute name='description' />
      <attribute name='displayname' />
      <attribute name='iscustomizable' />
      <attribute name='logicalentityname' />
      <attribute name='name' />
      <attribute name='uniquename' />
      <attribute name='type' />
      <attribute name='isoptional' />
    </link-entity>
    <link-entity name='customapiresponseproperty' from='customapiid' to='customapiid' link-type='outer' >
      <attribute name='description' />
      <attribute name='displayname' />
      <attribute name='iscustomizable' />
      <attribute name='logicalentityname' />
      <attribute name='name' />
      <attribute name='uniquename' />
      <attribute name='type' />
    </link-entity>
    <link-entity name='plugintype' from='plugintypeid' to='plugintypeid' link-type='outer' alias='plugintype' >
      <attribute name='name' />
      <attribute name='assemblyname' />
      <attribute name='version' />
      <attribute name='plugintypeid' />
      <attribute name='typename' />
    </link-entity>
  </entity>
</fetch>
```

### Using SQL

More information: [Use SQL to query data (Preview)](dataverse-sql-query.md)

```sql
SELECT api.customapiid,
       api.uniquename,
       api.allowedcustomprocessingsteptype,
       api.bindingtype,
       api.boundentitylogicalname,
       api.description,
       api.displayname,
       api.executeprivilegename,
       api.iscustomizable,
       api.isfunction,
       api.isprivate,
       api.workflowsdkstepenabled,
       req.customapirequestparameterid,
       req.uniquename,
       req.name,
       req.description,
       req.displayname,
       req.type,
       req.logicalentityname,
       req.iscustomizable,
       req.isoptional,
       resp.customapiresponsepropertyid,
       resp.uniquename,
       resp.name,
       resp.description,
       resp.iscustomizable,
       resp.type,
       resp.logicalentityname,
       type.plugintypeid,
       type.typename,
       type.version,
       type.name,
       type.assemblyname
FROM   customapi AS api
       LEFT JOIN
       customapirequestparameter AS req
       ON api.customapiid = req.customapiid
       LEFT JOIN
       customapiresponseproperty AS resp
       ON api.customapiid = resp.customapiid
       LEFT JOIN
       plugintype AS type
       ON api.plugintypeid = type.plugintypeid
```

## Localized Label values

Custom APIs have some localizable labels. You can localize the label values using the steps documented here: [Translate localizable text for model-driven apps](../../maker/model-driven-apps/translate-localizable-text.md) and [Translating labels and display strings](/power-platform/alm/create-solutions-support-multiple-languages#translating-labels-and-display-strings).

This process involves exporting a file that contains the base language values and will include a column for each additional language enabled. You can then edit the values in Excel. After you complete the process to import the translations the labels will be included in your solution.

The following example shows editing the Excel worksheet to add Japanese translations for the English values.

:::image type="content" source="media/solution-strings-for-translation.png" alt-text="Shows how labels are localized":::

> [!TIP]
> If you are editing the solution files to create your Custom APIs, you can provide the localized labels directly. More information: [Providing Localized Labels with the solution](create-custom-api-solution.md#providing-localized-labels-with-the-solution)

### Setting localized values

If you prefer to set localized labels in code rather than using the manual process described above, you can use the `SetLocLabels` message using either the Web API [SetLocLabels Action](/dynamics365/customer-engagement/web-api/setloclabels) or the Organization Service <xref:Microsoft.Crm.Sdk.Messages.SetLocLabelsRequest>.

The following example shows how to use the Web API to set the localized labels for the `displayname` property of a custom API.


**Request**

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

**Response**

```http
HTTP/1.1 204 No Content
```


### Retrieving localized values

To retrieve the localized labels use the `RetrieveLocLabels` message using either the Web API [RetrieveLocLabels Function](/dynamics365/customer-engagement/web-api/retrieveloclabels) or the Organization Service <xref:Microsoft.Crm.Sdk.Messages.RetrieveLocLabelsRequest>.

The following example shows using the RetrieveLocLabels Function to retrieve the labels for the the `displayname` property of a Custom API with the `customapiid` of `88602189-183d-4584-ba4b-8b60f0f5b89f`

**Request**

```http
GET [Organization URI]/api/data/v9.1/RetrieveLocLabels(EntityMoniker=@p1,AttributeName=@p2,IncludeUnpublished=@p3)?
@p1={'@odata.id':'customapis(88602189-183d-4584-ba4b-8b60f0f5b89f)'}&
@p2='displayname'&
@p3=false HTTP/1.1

```

**Response**

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

### Q: Can I create a new privilege for my Custom API?

A: While Custom API has an Execute Privilege Name (`ExecutePrivilegeName`) property, there is currently no supported way for you to create a new privilege just for this API. This is planned for a future release. In the meantime, there are two options:

- You can use an existing [Privilege.Name](./reference/entities/privilege.md#BKMK_Name) value.
- You can create a custom entity and use one of the privileges created for that entity. For example, create an entity named `new_myaction` and privileges for CRUD operations will be generated for it. For example `prvCreatenew_myaction`. You will need to include this custom entity with the solution that includes the Custom API.

### Q: Can I activate or deactivate Custom API records?

A: You cannot. Although these records have the common **Status** and **Status Reason** columns found on most Microsoft Dataverse tables. Setting the values for these columns has no impact on the availability of the Custom API, the request parameters, or the response properties.

### Q: How can I use my private messages if they are not included in the Web API $metadata service document?

A: Yes. Your private messages will work regardless of whether they are advertised in the Web API [CSDL $metadata document](webapi/web-api-types-operations.md#csdl-metadata-document) or not. While you develop your solution, you can leave the `IsPrivate` value set to `false`. This way you can refer to the `$metadata` listing and use code generation tools that depend on this data. However, you should set the `CustomAPI.IsPrivate` value to `true` before you ship your solution for others to use. If you later decide that you wish to support other applications to use the message, you can change the `CustomAPI.IsPrivate` value to `false`. 

More information: [Private Messages](org-service/use-messages.md#private-messages) and [Private messages cannot be used in plug-ins](#private-messages-cannot-be-used-in-plug-ins)

## Known issues with Custom APIs

Custom API is now generally available, but there are still some related capabilities that we expect to change.

### Not able to use profiler for debugging

To debug using the Plug-in Registration tool and the Plug-in profiler solution, you need to be able to select a specific plug-in step. The main stage implementation for the plug-in is not currently available in the Plug-in Registration tool.

**Workaround**: Register the plug-in type on the `PostOperation` stage of the message created for the Custom API.

### A custom API created is not added to the current solution in the maker portal

When you create a Custom API in the maker portal ([https://make.powerapps.com/](https://make.powerapps.com/)), you should do so in the context of a solution. However, due to the current dependency on the legacy web application designer, the Custom API or any of the Custom API Request Parameters or Custom API Response Properties do not get added to the solution automatically. You must still manually add each part to the solution by selecting the **Add Existing** button.

This will be fixed when a modern designer is provided, or you may want to define your Custom APIs by writing code or with solution files. 

### Private messages cannot be used in plug-ins

If you define your custom API to be private, you cannot use that message in a plug-in. More information: [Private Messages](org-service/use-messages.md#private-messages)

### Next Steps

[Create a Custom API in the maker portal](create-custom-api-maker-portal.md)<br />

### See also

[Create and use Custom APIs](custom-api.md)<br />
[Create a Custom API with code](create-custom-api-with-code.md)<br />
[Create a Custom API with solution files](create-custom-api-solution.md)<br />
[Create your own messages](custom-actions.md)<br />
[CustomAPI Table Columns](customapi-table-columns.md)<br />
[CustomAPIRequestParameter Table Columns](customapirequestparameter-table-columns.md)<br />
[CustomAPIRequestParameter Table Columns](customapirequestparameter-table-columns.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
