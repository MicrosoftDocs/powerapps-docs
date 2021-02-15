---
title: "Create and use Custom APIs (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Custom API is a new code-first way to define custom messages for the Microsoft Dataverse" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 01/19/2021
ms.reviewer: "pehecke"
ms.service: powerapps
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
# Create and use Custom APIs 

[This topic is pre-release documentation and is subject to change.] 

Custom APIs offer a new code-first way to define messages that you can add to Dataverse web services. Conceptually, Custom APIs are an extension to Custom Actions that have provided a no-code way to include custom messages. To differentiate between the two different kinds of Custom Action, we will use *Workflow Custom Action* to refer to the no-code capabilities that depend on workflow. *Custom API* will refer to the type of custom action that depends on a developer to write a plug-in.

Custom APIs provide a capabilities specifically for developers to define their logic in code. For a full comparison of Workflow Custom Action and Custom API, see [Compare Workflow Custom Action and Custom API](custom-actions.md#compare-workflow-custom-action-and-custom-api).

## Create a custom API

Because a Custom API requires a plug-in to implement any logic to be defined by the main operation, you can approach the development of your custom API by:

- Write the plug-in first, and then define the Custom API for it.
- Define the Custom API first, then write the plug-in to implement it.

Your Custom API will be completed when the data defining the Custom API is saved and linked to the Plug-in type to define the main operation. In either case, you should understand the data that drives the Custom API.

There are several different ways to create a custom API:

- By manually entering data in available forms.  More information: [Create a Custom API in the maker portal](create-custom-api-maker-portal.md)
- By using the web services, such as the Web API or Organization Service. More information: [Create a Custom API with code](create-custom-api-with-code.md)
- By editing solution files. More information: [Create a Custom API with solution files](create-custom-api-solution.md).

> [!NOTE]
> Although Custom API data is stored in entities, we do not support creating a model-driven app for these entities. A designer is planned for a future release.

Regardless of the process you use, the following information describes selected attributes for the three entities that contain the data for a Custom API. You should review this as you plan the behavior for your Custom API.

### CustomAPI entity attributes

This table includes attributes of the Custom API entity that you can set.


|Display Name<br />Schema Name  |Type  |Description |
|---------|---------|---------|
|**Allowed Custom Processing Step Type**<br />`AllowedCustomProcessingStepType`|Picklist|The type of custom processing steps allowed for this Custom API. This allows you to control whether other plug-ins can be registered<ul> <li>**Value**: 0 **Label**: None **Meaning**: No custom processing steps allowed.</li> <li>**Value**: 1 **Label**: Async Only **Meaning**: Only asynchronous custom processing steps allowed</li> <li>**Value**: 2 **Label**: Sync and Async **Meaning**: No restriction. 3rd party plug-ins can add synchronous logic to change the behavior of the message.</li> </ul> **Cannot be changed after it is saved.**|
|**Binding Type**<br />`BindingType`|Picklist|The binding type of the custom API.<ul><li>**Value**: 0 **Label**: Global</li><li>**Value**: 1 **Label**: Entity</li><li>**Value**: 2 **Label**: EntityCollection</li></ul>**Cannot be changed after it is saved.**|
|**Bound Entity Logical Name**<br />`BoundEntityLogicalName`|String|The logical name of the entity bound to the custom API if it is not Global.<br />**Cannot be changed after it is saved.**|
|**Custom API**<br />`CustomAPIId`|Uniqueidentifier|Unique identifier for custom API instances<br />**Cannot be changed after it is saved.**|
|**Description**<br />`Description`|String|Localized description for this Custom API. For use when the message is exposed to be called in an app. For example, as a [ToolTip](https://wikipedia.org/wiki/Tooltip).|
|**Display Name**<br />`DisplayName`|String|Localized display name for this Custom API. For use when the message is exposed to be called in an app.|
|**Execute Privilege Name**<br />`ExecutePrivilegeName`|String|(Optional) Name of the privilege that allows execution of the custom API|
|**Is Function**<br />`IsFunction`|Boolean|Indicates if the custom API is a function. A function requires the HTTP GET method. Otherwise the Http POST method is required.<ul> <li>**Value**: 0 **Label**: No</li> <li>**Value**: 1 **Label**: Yes</li> </ul>**Important**: A function MUST include at least one Response Property to be valid.<br/>More information: [Use Web API functions](webapi/use-web-api-functions.md)<br />**Cannot be changed after it is saved.**|
|**Is Private**<br />`IsPrivate`|Boolean|Indicates if the custom API is private (hidden from metadata and documentation) More information: [Private Messages](org-service/use-messages.md#private-messages)<ul> <li>**Value**: 0 **Label**: No </li> <li>**Value**: 1 **Label**: Yes</li> </ul>|
|**Name**<br />`Name`|String|The primary name of the custom API. This will display in the list of custom apis when viewed in the solution.|
|**Owner**<br />`OwnerId`|Owner|A reference to the user or team that owns the API. |
|**Plugin Type**<br />`PluginTypeId`|Lookup|A reference to the plug-in type that provides the main operation for this Custom API|
|**Unique Name**<br />`UniqueName`|String|Unique name for the custom API. This will be the name of the message created.<br /> This value must include a customization prefix that matches the prefix set for your solution publisher.<br />**Cannot be changed after it is saved.**|

> [!NOTE]
> Some values are not valid for update. They cannot be changed after the Custom API is saved. You should have a clear understanding of how your API should work before you begin. If you need to change any values that are not valid for update, you will have to delete the Custom API entity record and start over. Deleting the Custom API record will delete any Custom API Request Parameters or Custom API Response Properties associated with it.

Set the **Execute Privilege Name** property to the name of the privilege to require it. There is currently no supported way for developers outside of Microsoft to create new privileges, but an existing privilege can be used. More information: [Q: Can I create a new privilege for my Custom API?](#q-can-i-create-a-new-privilege-for-my-custom-api)

If you do not set the **Plugin Type** (`PluginTypeId`)  to specify main operation logic the API can still be called. You might want to do this as a testing step, but any output parameter values will return the default values for the type because there is no code to set them.

**Known Issues**:

- [The Is Private field is not included in the Custom API form](#the-is-private-field-is-not-included-in-the-custom-api-form)
- [Custom API functions cannot use Entity or EntityCollection Request Parameters](#custom-api-functions-cannot-use-entity-or-entitycollection-request-parameters)

### CustomAPIRequestParameter entity attributes

A custom API isn’t required to have any parameters. There is no specified order for the parameters, they are identified by name.

A parameter is related to a single Custom API. You cannot define multiple Custom APIs to use the same parameter definition. You can define multiple request parameter with the same `UniqueName` value if they are used by different Custom APIs.

> [!NOTE]
> If you define a bound entity or entity collection for your Custom API, the parameter will be generated for you. You don’t need to create a parameter for bound entities.

This table includes attributes of the Custom API Request Parameter entity that you can set.

|Display Name<br />Schema Name  |Type  |Description |
|---------|---------|---------|
|**Custom API Request Parameter**<br />`CustomAPIRequestParameterId`|Uniqueidentifier|Unique identifier for custom API request parameter instances.<br/>**Cannot be changed after it is saved.**|
|**Custom API** <br />`CustomAPIId`|Lookup|Unique identifier for the custom API that this custom API request parameter is associated with.<br/>**Cannot be changed after it is saved.**|
|**Description**<br />`Description`|String|Localized description for custom API request parameter instances. For use when the message parameter is exposed to be called in an app. For example, as a [ToolTip](https://wikipedia.org/wiki/Tooltip).|
|**Display Name** <br />`DisplayName`|String|Localized display name for custom API request parameter instances. For use when the message parameter is exposed to be called in an app.|
|**Is Optional**<br />`IsOptional`|Boolean|Indicates if the custom API request parameter is optional. If it is not optional, it is required to pass a value for this parameter when using the message.<ul> <li>**Value**: 0 **Label**: No </li> <li>**Value**: 1 **Label**: Yes</li> </ul>**Cannot be changed after it is saved.**|
|**Logical Entity Name**<br />`LogicalEntityName`|String|The logical name of the entity bound to the custom API request parameter.<br/>**Cannot be changed after it is saved.**|
|**Name**<br />`Name`|String|The primary name of the custom API request parameter.  This will display in the list of custom api request parameters when viewed in the solution. Use this to differentiate this parameter from others that share a common Unique Name. <br />This naming convention is recommended: `{Custom API Unique Name}.{Parameter UniqueName}`|
|**Owner** <br />`OwnerId`|Owner|A reference to the user or team that owns the API.|
|**Type**<br />`Type`|Picklist|The data type of the custom API request parameter.<ul> <li>**Value**: 0 **Label**: Boolean </li> <li>**Value**: 1 **Label**: DateTime</li> <li>**Value**: 2 **Label**: Decimal </li> <li>**Value**: 3 **Label**: Entity</li> <li>**Value**: 4 **Label**: EntityCollection </li> <li>**Value**: 5 **Label**: EntityReference</li> <li>**Value**: 6 **Label**: Float </li> <li>**Value**: 7 **Label**: Integer</li> <li>**Value**: 8 **Label**: Money </li> <li>**Value**: 9 **Label**: Picklist</li> <li>**Value**: 10 **Label**: String </li> <li>**Value**: 11 **Label**: StringArray </li> <li>**Value**: 12 **Label**: Guid </li> </ul>**Cannot be changed after it is saved.**|
|**Unique Name** <br />`UniqueName`|String|Unique name for the custom API request parameter. This will be the name of the parameter when you call the Custom API.<br/>**Cannot be changed after it is saved.**|

> [!NOTE]
> Some values are not valid for update. They cannot be changed after the Custom API Request Parameter is saved. If you need to change one of these values, you must delete the Custom API Request Parameter and re-create it with the changes you want to make.

### CustomAPIResponseProperty entity attributes

The object returned for your Custom API message will include any response properties you define. It is not required for a Custom API to return any value, but if the custom API is defined as a function it is required.

> [!IMPORTANT]
> A Custom API that represents a function with no response properties is not valid and will not appear in the Web API $metadata service document. If you try to use it, you will get a `404 Not Found` error similar to this: 
>
> `{"error":{"code":"0x8006088a","message":"Resource not found for the segment 'your_function_name'."}}`.
>
> You must also set the data to be returned in the plug-in for the function. If no data is set to be returned by the plug-in, the operation will return `204 No Content`.

If there is only a single **Entity** or **EntityCollection** response property defined, the response will be of that type. If there are multiple parameters, or one or more parameter of a simple type, the API will return a complex type where each response property will be a property of that complex type. For example, if your Custom API Unique name is `sample_CustomAPIExample`, it will return a complex type named `sample_CustomAPIExampleResponse` with properties for each response property you define.

This table includes attributes of the Custom API Response Property entity that you can set.

|Display Name<br />Schema Name  |Type  |Description |
|---------|---------|---------|
|**Custom API Response Property**<br />`CustomAPIResponsePropertyId`|Uniqueidentifier|Unique identifier for custom API response property instances.<br/>**Cannot be changed after it is saved.**|
|**Custom API** <br />`CustomAPIId`|Lookup|Unique identifier for the custom API that this custom API response property is associated with. <br/>**Cannot be changed after it is saved.**|
|**Description**<br />`Description`|String|Localized description for custom API response property  instances. For use when the message parameter is exposed to be called in an app. For example, as a [ToolTip](https://wikipedia.org/wiki/Tooltip).|
|**Display Name** <br />`DisplayName`|String|Localized display name for custom API response property  instances. For use when the message parameter is exposed to be called in an app.|
|**Logical Entity Name**<br />`LogicalEntityName`|String|The logical name of the entity bound to the custom API response property .<br/>**Cannot be changed after it is saved.**|
|**Name**<br />`Name`|String|The primary name of the custom API response property .  This will display in the list of custom api request parameters when viewed in the solution. Use this to differentiate this parameter from others that share a common Unique Name. <br />This naming convention is recommended: `{Custom API Unique Name}.{Property UniqueName}`|
|**Owner** <br />`OwnerId`|Owner|A reference to the user or team that owns the API.|
|**Type**<br />`Type`|Picklist|The data type of the custom API response property <ul> <li>**Value**: 0 **Label**: Boolean </li> <li>**Value**: 1 **Label**: DateTime</li> <li>**Value**: 2 **Label**: Decimal </li> <li>**Value**: 3 **Label**: Entity</li> <li>**Value**: 4 **Label**: EntityCollection </li> <li>**Value**: 5 **Label**: EntityReference</li> <li>**Value**: 6 **Label**: Float </li> <li>**Value**: 7 **Label**: Integer</li> <li>**Value**: 8 **Label**: Money </li> <li>**Value**: 9 **Label**: Picklist</li> <li>**Value**: 10 **Label**: String </li> <li>**Value**: 11 **Label**: StringArray </li> <li>**Value**: 12 **Label**: Guid </li> </ul>**Cannot be changed after it is saved.**|
|**Unique Name** <br />`UniqueName`|String|Unique name for the custom API response property . This will be the name of the parameter when you call the Custom API.<br/>**Cannot be changed after it is saved.**|

> [!NOTE]
> Some values are not valid for update. They cannot be changed after the Custom API Response Property is saved. If you need to change one of these values, you must delete the Custom API Response Property and re-create it with the changes you want to make.

## Invoking Custom APIs

A Custom API creates a new message which can be invoked via the SDK or Web API.

### Invoking Custom APIs from SDK based applications or plug-ins

You can choose to use either early-bound or late-bound code to invoke your custom API. Use the [CrmSvcUtil](/dynamics365/customer-engagement/developer/org-service/create-early-bound-entity-classes-code-generation-tool) tool to generate helper request and response classes to mirror the request and response properties of your custom API.

For late-bound code, create an `OrganizationRequest` with the unique name of your custom API and add parameters with names matching the unique names of the request properties.

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

### Invoking Custom APIs from the Web API

Custom APIs can be called in the same way as any standard Web API [functions](webapi/use-web-api-functions.md) or [actions](webapi/use-web-api-actions.md). If your custom API has the `IsFunction` field set to `true` then it needs to be invoked as a function using a `GET` request, otherwise it needs to be used as an action using a `POST` request:

```http
POST [Organization URI]/api/data/v9.1/myapi_CustomUnboundAPI
OData-MaxVersion: 4.0
OData-Version: 4.0
Content-Type: application/json; charset=utf-8

{
  "InputParameter": "Value"
}
```

```http
GET [Organization URI]/api/v9.1/accounts(ed5d4e42-850c-45b7-8b38-2677545107cc)/Microsoft.Dynamics.CRM.myapi_CustomBoundAPI()
OData-MaxVersion: 4.0
OData-Version: 4.0
Content-Type: application/json; charset=utf-8
```

```http
GET [Organization URI]/api/v9.1/accounts/Microsoft.Dynamics.CRM.myapi_CustomEntityCollectionBoundAPI()
OData-MaxVersion: 4.0
OData-Version: 4.0
Content-Type: application/json; charset=utf-8
```

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
    isfunction,
    isprivate
  &$expand=
  CustomAPIRequestParameters($select=
    uniquename,
    name,
    description,
    displayname,
    type,
    logicalentityname,
    isoptional),
  CustomAPIResponseProperties($select=
    uniquename,
    name,
    description,
    displayname,
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
    <attribute name='isfunction' />
    <attribute name='allowedcustomprocessingsteptype' />
    <attribute name='boundentitylogicalname' />
    <attribute name='bindingtype' />
    <attribute name='uniquename' />
    <link-entity name='customapirequestparameter' from='customapiid' to='customapiid' link-type='outer' alias='req' >
      <attribute name='description' />
      <attribute name='displayname' />
      <attribute name='logicalentityname' />
      <attribute name='name' />
      <attribute name='uniquename' />
      <attribute name='type' />
      <attribute name='isoptional' />
    </link-entity>
    <link-entity name='customapiresponseproperty' from='customapiid' to='customapiid' link-type='outer' >
      <attribute name='description' />
      <attribute name='displayname' />
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
       api.isfunction,
       api.isprivate,
       req.customapirequestparameterid,
       req.uniquename,
       req.name,
       req.description,
       req.displayname,
       req.type,
       req.logicalentityname,
       req.isoptional,
       resp.customapiresponsepropertyid,
       resp.uniquename,
       resp.name,
       resp.description,
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

## Localized values

You can localize the values using the steps documented here: [Translate localizable text for model-driven apps](../../maker/model-driven-apps/translate-localizable-text.md) and [Translating labels and display strings](/power-platform/alm/create-solutions-support-multiple-languages#translating-labels-and-display-strings).

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

- You can use an existing [Privilege.Name](/powerapps/developer/data-platform/reference/entities/privilege#BKMK_Name) value.
- You can create a custom entity and use one of the privileges created for that entity. For example, create an entity named `new_myaction` and privileges for CRUD operations will be generated for it. For example `prvCreatenew_myaction`. You will need to include this custom entity with the solution that includes the Custom API.

### Q: Can I activate or deactivate Custom API records?

A: You cannot. Although these records have the common **Status** and **Status Reason** fields found on most Microsoft Dataverse entities. Setting the values for these fields has no impact on the availability of the Custom API, the request parameters, or the response properties.

### Q: How can I use my private messages if they are not included in the Web API $metadata service document?

A: Your private messages will work regardless of whether they are advertised in the Web API [CSDL $metadata document](webapi/web-api-types-operations.md#csdl-metadata-document) or not. While you develop your solution, you can leave the `IsPrivate` value set to `false`. This way you can refer to the `$metadata` listing and use code generation tools that depend on this data. However, you should set the `CustomAPI.IsPrivate` value to `false` before you ship your solution for others to use. If you later decide that you wish to support other applications to use the message, you can change the `CustomAPI.IsPrivate` value to `true`. 

More information: [Private Messages](org-service/use-messages.md#private-messages) and [Private messages cannot be used in plug-ins](#private-messages-cannot-be-used-in-plug-ins)

## Known issues with Custom APIs

Custom APIs are a preview feature and subject to change. Following are some known issues we expect to change.

### Not able to use profiler for debugging

To debug using the Plug-in Registration tool and the Plug-in profiler solution, you need to be able to select a specific plug-in step. The main stage implementation for the plug-in is not available in the Plug-in Registration tool. 

**Workaround**: Register the plug-in type on the PostOperation stage of the message created for the Custom API.

### A custom API cannot be called from a workflow

A Workflow Custom Action can be called from another workflow. Currently, Custom APIs cannot.

### A custom API created is not added to the current solution

When you create a Custom API you should do so in the context of a solution. Normally, when you create a new solution component in the context of a solution, it is included in that solution. Currently, even when you create a Custom API in the context of a solution, you must still manually add each part to the solution by selecting the **Add Existing** button.

### The Is Private field is not included in the Custom API form

The **Is Private** field is not available in the form when you create a Custom API in the UI. You cannot add this field to the form. You must set this field programmatically or by editing the solution XML files.

### Custom API entities can be related to other entities

It is currently possible for entities to create relationships with the three Custom API entities. Other than to create 1:N relationships with `CustomAPIRequestParameter` and `CustomAPIResponseProperty` as the primary entity, this ability may be removed in a future release. Entities related to `CustomAPIRequestParameter` and `CustomAPIResponseProperty` allow for definition of  entities that may provide further metadata about the respective parameters and response properties.

### The Name field value is displayed in the solution components view where the Display Name value should be shown

When viewing the Custom API entities in a solution, the **Display Name** column shows the **Name** value rather than the **Display Name** value.

### Custom API and related records cannot be created using one operation

It is not possible to create the Custom API, Custom API Request Parameter, and Custom API Response Properties in a single operation using 'deep-insert' as described in [Create related entity records in one operation](webapi/create-entity-web-api.md#create-related-entity-records-in-one-operation) and [Create related entities in one operation](org-service/entity-operations-create.md#create-related-entities-in-one-operation). Instead, each record must be created individually and be related to the Custom API record.

### Custom API functions cannot use Entity or EntityCollection Request Parameters

If you define your Custom API as a function by setting the **Is Function** property to true, you cannot bind the function to an entity or entity collection. You also cannot use any **Entity** or **EntityCollection** request parameters.

If you attempt this with a function bound to the account entity, you can expect a `400 Bad Request` error like this:

`GET [Organization URL]/api/data/v9.1/accounts/Microsoft.Dynamics.CRM.new_CollectionBoundFunction()`

```json
{
    "error": {
        "code": "0x8006088a",
        "message": "The request URI is not valid. Since the segment 'accounts' refers to a collection, this must be the last segment in the request URI or it must be followed by an function or action that can be bound to it otherwise all intermediate segments must refer to a single resource."
    }
}
```

### Private messages cannot be used in plug-ins

If you define your custom API to be private, you cannot use that message in a plug-in. More information: [Private Messages](org-service/use-messages.md#private-messages)

### Next Steps

[Create a Custom API in the maker portal](create-custom-api-maker-portal.md)<br />

### See also

[Create and use Custom APIs](custom-api.md)<br />
[Create a Custom API with code](create-custom-api-with-code.md)<br />
[Create a Custom API with solution files](create-custom-api-solution.md)<br />
[Create your own messages](custom-actions.md)<br />


[!INCLUDE[footer-include](../../includes/footer-banner.md)]