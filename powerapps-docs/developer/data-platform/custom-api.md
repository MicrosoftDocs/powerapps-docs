---
title: "Create and use Custom APIs (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Custom API is a new code-first way to define custom messages for the Microsoft Dataverse" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/21/2022
ms.reviewer: "pehecke"
ms.topic: "article"
author: "divka78" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Create and use Custom APIs

Use Custom APIs to create your own APIs in Dataverse. You can consolidate one or more operations into a Custom API that you and other developers can call in their code or from Power Automate. The [Microsoft Dataverse connector](/connectors/commondataserviceforapps/) enables calling  actions in Power Automate.

You can use Custom API as business events to enable creating new integration capabilities such as exposing a new type of trigger event in the Microsoft Dataverse connector. More information: [Microsoft Dataverse business events](business-events.md)

Custom APIs are an alternative to Custom process actions. Custom process actions provide a no-code way to include custom messages but has some limitations for developers. Custom APIs provide capabilities specifically for developers to define their logic in code with more options. For a full comparison of Custom Process Action and Custom API, see [Compare Custom Process Action and Custom API](custom-actions.md#compare-custom-process-action-and-custom-api).

## Create a custom API

A Custom API may include logic implemented with a plug-in. Using [Microsoft Dataverse business events](business-events.md), you may create a Custom API without a plug-in to pass data about an event that other subscribers will respond to.

However, in other cases you will combine a Custom API with a plug-in to define some operation that will delegated to Dataverse to compute and return the result.

There are several different ways to create a custom API:

|Method|Benefit|
|---------|---------|
|[Plug-in registration tool](create-custom-api-prt.md)|An easy-to-use GUI tool integrated with tools used to develop plug-ins.|
|[Power Apps](create-custom-api-maker-portal.md)|Using forms to enter data. You don't need to install a separate tool, but the experience is not great.|
|[With Code](create-custom-api-with-code.md)|After you understand the data model, you can create Custom API very quickly using Postman. Or you can build your own experience to create Custom API.|
|[With solution files](create-custom-api-solution.md)|When you use Application Lifecycle Management (ALM) tools you can create or modify Custom API definitions with XML files in a solution that is included in your source code repository. The Custom API will be created when you import the solution generated from your source code.|

> [!NOTE]
> Although Custom API data is stored in tables, we do not support creating a model-driven app for these tables.
>
> There are several tools created and supported by the community to work with Custom API:
>
> - [Dataverse Custom API Manager](https://www.xrmtoolbox.com/plugins/XTB.CustomApiManager/)
> - [Custom API Tester](https://www.xrmtoolbox.com/plugins/Rappen.XrmToolBox.CustomAPITester/)
> - [Custom Action to Custom API Converter](https://www.xrmtoolbox.com/plugins/MarkMpn.CustomActionToApiConverter/)

## Custom API Customization

When creating Custom API and related request parameters and response properties, it is important to understand that these API definitions are customizable by default. This is what allows you to iterate and make changes to these items in your unmanaged solution.

> [!IMPORTANT]
> When you ship or deploy your solution, you should use a managed solution and we recommend that you always set the **Is Customizable** managed property to these components to `false`. This will prevent people using your managed solution from modifying or deleting these components of your solution. Such changes could break code written for the original definition of the Custom API.

### Set Is Customizable to false

You can set the **Is Customizable** managed property from the solution in Power Apps.

:::image type="content" source="media/set-custom-api-iscustomizable-managed-property.png" alt-text="Setting Is Customizable Managed Property":::

You will need to set this for each Custom API, Request Parameter, and Response Property individually.

More information [Managed properties](/power-platform/alm/managed-properties-alm)

### Add additional request parameters and response properties

Even when you have set the **Is Customizable** managed property to these components to `false`, new request parameters and response properties can be added to your Custom API. However, additional request parameters cannot be made required. If you choose to allow custom processing steps on your Custom API, these additional parameters and properties added to the original definition can be used by other plug-ins registered for the message created by your Custom API. Because custom request parameters can only be optional, the plug-in you provide for the main operation of the Custom API can ignore them and is not responsible for using any custom request parameters or setting any custom response properties.

## Custom API tables/entities

The data that defines Custom APIs is in the following tables/entities:

- [CustomAPI Reference](reference/entities/customapi.md)
- [CustomAPIRequestParameter Reference](reference/entities/customapirequestparameter.md)
- [CustomAPIResponseProperty Reference](reference/entities/customapiresponseproperty.md)

This diagram shows how the tables are related to these tables as well as others:

:::image type="content" source="media/custom-api-data-model.png" alt-text="Diagram showing relationships between tables.":::

The relationship to the [CatalogAssignment table](reference/entities/catalogassignment.md) enables using Custom API with [Microsoft Dataverse business events](business-events.md). More information: [Catalog and CatalogAssignment tables](catalog-catalogassignment.md).

### Retrieve data about Custom APIs

You can use the following queries to retrieve data about Custom APIs.

# [Web API](#tab/webapi)

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

# [QueryExpression](#tab/queryexpression)

More information: [Build queries with QueryExpression](org-service/build-queries-with-queryexpression.md)

```csharp
string conn = $@"
    Url = {url};
    AuthType = OAuth;
    UserName = {userName};
    Password = {password};
    AppId = 51f81489-12ee-4a9e-aaae-a2591f45987d;
    RedirectUri = app://58145B91-0C36-4500-8554-080854F2AC97;
    LoginPrompt=Auto;
    RequireNewInstance = True";

using (var svc = new CrmServiceClient(conn))
{

    // Instantiate QueryExpression query
    var query = new QueryExpression("customapi");

    // Add columns to query.ColumnSet
    query.ColumnSet.AddColumns("isprivate",
    "description",
    "displayname",
    "executeprivilegename",
    "iscustomizable",
    "isfunction",
    "allowedcustomprocessingsteptype",
    "boundentitylogicalname",
    "bindingtype",
    "uniquename",
    "workflowsdkstepenabled");

    // Add link-entity req
    var req = query.AddLink("customapirequestparameter",
    "customapiid",
    "customapiid",
    JoinOperator.LeftOuter);
    req.EntityAlias = "req";

    // Add columns to req.Columns
    req.Columns.AddColumns("description",
    "displayname",
    "iscustomizable",
    "logicalentityname",
    "name",
    "uniquename",
    "type",
    "isoptional");

    // Add link-entity query_customapiresponseproperty
    var query_customapiresponseproperty = query
        .AddLink("customapiresponseproperty",
    "customapiid",
    "customapiid",
    JoinOperator.LeftOuter);

    // Add columns to query_customapiresponseproperty.Columns
    query_customapiresponseproperty.Columns
        .AddColumns("description",
    "displayname",
    "iscustomizable",
    "logicalentityname",
    "name",
    "uniquename",
    "type");

    // Add link-entity plugintype
    var plugintype = query.AddLink("plugintype",
    "plugintypeid",
    "plugintypeid",
    JoinOperator.LeftOuter);

    plugintype.EntityAlias = "plugintype";

    // Add columns to plugintype.Columns
    plugintype.Columns.AddColumns("name",
    "assemblyname",
    "version",
    "plugintypeid",
    "typename");

    EntityCollection results = svc.RetrieveMultiple(query);

    Console.WriteLine("Press any key to exit.");
    Console.ReadLine();
}
```

# [FetchXML](#tab/fetchxml)

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

# [SQL](#tab/sql)

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

---

### Custom API table columns

The table below includes selected columns of a Custom API table that you can set.  

|Display Name<br />Schema Name<br />Logical Name  |Type  |Description |
|---------|---------|---------|
|**Allowed Custom Processing Step Type**<br />`AllowedCustomProcessingStepType`<br />`allowedcustomprocessingsteptype`|Choice<br />Picklist|<ul> <li>**Value**: 0<br />**Label**: None<br />**Meaning**: No custom processing steps allowed.</li> <li>**Value**: 1<br />**Label**: Async Only<br />**Meaning**: Only asynchronous custom processing steps allowed</li> <li>**Value**: 2<br />**Label**: Sync and Async<br />**Meaning**: No restriction. 3rd party plug-ins can add synchronous logic to change the behavior of the message.</li> </ul>See [Select a Custom Processing Step Type](#select-a-custom-processing-step-type)<br/>**Cannot be changed after it is saved.**|
|**Binding Type**<br />`BindingType`<br />`bindingtype`|Choice<br />Picklist|<ul><li>**Value**: 0 **Label**: Global</li><li>**Value**: 1 **Label**: Entity</li><li>**Value**: 2 **Label**: EntityCollection</li></ul>See [Select a Binding Type](#select-a-binding-type)<br />**Cannot be changed after it is saved.**|
|**Bound Entity Logical Name**<br />`BoundEntityLogicalName`<br />`boundentitylogicalname`|Text<br />String|The logical name of the table bound to the custom API if it is not Global.<br />**Cannot be changed after it is saved.**|
|**Custom API**<br />`CustomAPIId`<br />`customapiid`|Unique Identifier<br />Guid|Unique Identifier for custom API instances<br />**Cannot be changed after it is saved.**|
|**Description**<br />`Description`<br />`description`|Text<br />String|Localized description for this Custom API. For use when the message is exposed to be called in an app. For example, as a [ToolTip](https://wikipedia.org/wiki/Tooltip).|
|**Display Name**<br />`DisplayName`<br />`displayname`|Text<br />String|Localized display name for this Custom API. For use when the message is exposed to be called in an app.|
|**Execute Privilege Name**<br />`ExecutePrivilegeName`<br />`executeprivilegename`|Text<br />String|(Optional) Name of the privilege that allows execution of the custom API. See: [Execute Privilege Name](#execute-privilege-name)|
|**Is Customizable**<br />`IsCustomizable`<br />`iscustomizable`|ManagedProperty|Whether the Custom API can be customized or deleted when part of a managed solution.|
|**Is Function**<br />`IsFunction`<br />`isfunction`|Yes/No<br />Boolean|<ul> <li>**Value**: 0 **Label**: No</li> <li>**Value**: 1 **Label**: Yes</li> </ul>See [When to create a Function](#when-to-create-a-function)<br />**Cannot be changed after it is saved.**|
|**Is Private**<br />`IsPrivate`<br />`isprivate`|Yes/No<br />Boolean|<ul> <li>**Value**: 0 **Label**: No </li> <li>**Value**: 1 **Label**: Yes</li></ul>See [When to make your Custom API private](#when-to-make-your-custom-api-private)|
|**Name**<br />`Name`<br />`name`|Text<br />String|The primary name of the custom API. This will display in the list of custom apis when viewed in the solution.|
|**Owner**<br />`OwnerId`<br />`ownerid`|Owner|A reference to the user or team that owns the API. |
|**Plugin Type**<br />`PluginTypeId`<br />`plugintypeid`|Lookup|A reference to the plug-in type that provides the main operation for this Custom API. See: [Plugin Type](#plugin-type)|
|**Unique Name**<br />`UniqueName`<br />`uniquename`|Text<br />String|Unique name for the custom API. This will be the name of the message created.<br /> This value must include a customization prefix that matches the prefix set for your solution publisher.<br />**Cannot be changed after it is saved.**|
|**Enabled for Workflow**<br />`WorkflowSdkStepEnabled`<br />`workflowsdkstepenabled`|Yes/No<br />Boolean|Indicates if the custom API is enabled as a workflow action. See: [Enabled for Workflow](#enabled-for-workflow)<br />**Cannot be changed after it is saved.**|

### CustomAPIRequestParameter Table Columns

A custom API isn’t required to have any parameters. There is no specified order for the parameters, they are identified by name.

A parameter is related to a single Custom API. You cannot define multiple Custom APIs to use the same parameter definition. You can define multiple request parameter with the same `UniqueName` value if they are used by different Custom APIs.

> [!NOTE]
> If you define a bound table for your Custom API, the request parameter will be generated for you. You don’t need to create an input parameter for the table when the Custom API is bound to a table. More information: [Select a Binding Type](#select-a-binding-type)

The table shown below includes columns (attributes) of the Custom API Request Parameter table that you can set.

|Display Name<br />Schema Name<br />Logical Name  |Type  |Description |
|---------|---------|---------|
|**Custom API Request Parameter**<br />`CustomAPIRequestParameterId`<br />`customapirequestparameterid`|Unique Identifier<br />Guid|Unique identifier for custom API request parameter instances.<br/>**Cannot be changed after it is saved.**|
|**Custom API** <br />`CustomAPIId`<br />`customapiid`|Lookup|Unique identifier for the custom API that this custom API request parameter is associated with.<br/>**Cannot be changed after it is saved.**|
|**Description**<br />`Description`<br />`description`|Text<br />String|Localized description for custom API request parameter instances. For use when the message parameter is exposed to be called in an app. For example, as a [ToolTip](https://wikipedia.org/wiki/Tooltip).|
|**Display Name** <br />`DisplayName`<br />`displayname`|Text<br />String|Localized display name for custom API request parameter instances. For use when the message parameter is exposed to be called in an app.|
|**Is Customizable**<br />`IsCustomizable`<br />`iscustomizable`|ManagedProperty|Whether the custom api request parameter can be customized or deleted when part of a managed solution. See [Custom API Customization](custom-api.md#custom-api-customization)|
|**Is Optional**<br />`IsOptional`<br />`isoptional`|Yes/No<br />Boolean|Indicates if the custom API request parameter is optional. If it is not optional, it is required to pass a value for this parameter when using the message.<ul> <li>**Value**: 0 **Label**: No </li> <li>**Value**: 1 **Label**: Yes</li> </ul>**Cannot be changed after it is saved.**|
|**Logical Entity Name**<br />`LogicalEntityName`<br />`logicalentityname`|Text<br />String|The logical name of the table bound to the custom API request parameter.<br/>**Cannot be changed after it is saved.**|
|**Name**<br />`Name`<br />`name`|Text<br />String|The primary name of the custom API request parameter.  This will display in the list of custom api request parameters when viewed in the solution. Use this to differentiate this parameter from others that share a common Unique Name. <br />This naming convention is recommended: `{Custom API Unique Name}.{Parameter UniqueName}`|
|**Owner** <br />`OwnerId`<br />`ownerid`|Owner|A reference to the user or team that owns the API.|
|**Type**<br />`Type`<br />`type`|Choice<br />Picklist|The data type of the custom API request parameter.<ul> <li>**Value**: 0 **Label**: Boolean </li> <li>**Value**: 1 **Label**: DateTime</li> <li>**Value**: 2 **Label**: Decimal </li> <li>**Value**: 3 **Label**: Entity</li> <li>**Value**: 4 **Label**: EntityCollection </li> <li>**Value**: 5 **Label**: EntityReference</li> <li>**Value**: 6 **Label**: Float </li> <li>**Value**: 7 **Label**: Integer</li> <li>**Value**: 8 **Label**: Money </li> <li>**Value**: 9 **Label**: Picklist</li> <li>**Value**: 10 **Label**: String </li> <li>**Value**: 11 **Label**: StringArray </li> <li>**Value**: 12 **Label**: Guid </li> </ul>**Cannot be changed after it is saved.**|
|**Unique Name** <br />`UniqueName`<br />`uniquename`|Text<br />String|Unique name for the custom API request parameter. This will be the name of the parameter when you call the Custom API.<br/>**Cannot be changed after it is saved.**|

### CustomAPIResponseProperty Table Columns

The object returned for your Custom API message will include any response properties you define. It is not required for a Custom API Action to return any value, but it must return a value if defined as a Function.

If there is only a single **Entity** or **EntityCollection** response property defined, the response will be of that type. If there are multiple parameters, or one or more parameter of a simple type, the API will return a complex type where each response property will be a property of that complex type.

For example, if your Custom API Unique name is `sample_CustomAPIExample`, it will return a complex type named `sample_CustomAPIExampleResponse` with properties for each response property you define.

The table below includes columns (attributes) of the Custom API Response Property table that you can set.

|Display Name<br />Schema Name<br />Logical Name  |Type  |Description |
|---------|---------|---------|
|**Custom API Response Property**<br />`CustomAPIResponsePropertyId`<br />`customapiresponsepropertyid`|Unique Identifier<br />Guid|Unique identifier for custom API response property instances.<br/>**Cannot be changed after it is saved.**|
|**Custom API** <br />`CustomAPIId`<br />`customapiid`|Lookup|Unique identifier for the custom API that this custom API response property is associated with. <br/>**Cannot be changed after it is saved.**|
|**Description**<br />`Description`<br />`description`|Text<br />String|Localized description for custom API response property  instances. For use when the message parameter is exposed to be called in an app. For example, as a [ToolTip](https://wikipedia.org/wiki/Tooltip).|
|**Display Name** <br />`DisplayName`<br />`displayname`|Text<br />String|Localized display name for custom API response property  instances. For use when the message parameter is exposed to be called in an app.|
|**Is Customizable**<br />`IsCustomizable`<br />`iscustomizable`|ManagedProperty|Whether the custom api response property can be customized or deleted when part of a managed solution.|
|**Logical Entity Name**<br />`LogicalEntityName`<br />`logicalentityname`|Text<br />String|The logical name of the table bound to the custom API response property .<br/>**Cannot be changed after it is saved.**|
|**Name**<br />`Name`<br />`name`|String|The primary name of the custom API response property .  This will display in the list of custom api request parameters when viewed in the solution. Use this to differentiate this parameter from others that share a common Unique Name. <br />This naming convention is recommended: `{Custom API Unique Name}.{Property UniqueName}`|
|**Owner** <br />`OwnerId`<br />`ownerid`|Owner|A reference to the user or team that owns the API.|
|**Type**<br />`Type`<br />`type`|Picklist|The data type of the custom API response property <ul> <li>**Value**: 0 **Label**: Boolean </li> <li>**Value**: 1 **Label**: DateTime</li> <li>**Value**: 2 **Label**: Decimal </li> <li>**Value**: 3 **Label**: Entity</li> <li>**Value**: 4 **Label**: EntityCollection </li> <li>**Value**: 5 **Label**: EntityReference</li> <li>**Value**: 6 **Label**: Float </li> <li>**Value**: 7 **Label**: Integer</li> <li>**Value**: 8 **Label**: Money </li> <li>**Value**: 9 **Label**: Picklist</li> <li>**Value**: 10 **Label**: String </li> <li>**Value**: 11 **Label**: StringArray </li> <li>**Value**: 12 **Label**: Guid </li> </ul>**Cannot be changed after it is saved.**|
|**Unique Name** <br />`UniqueName`<br />`uniquename`|Text<br />String|Unique name for the custom API response property . This will be the name of the parameter when you call the Custom API.<br/>**Cannot be changed after it is saved.**|

## Select a Custom Processing Step Type

The following table describes which Custom API **Custom Processing Step Type** (`AllowedCustomProcessingStepType`) you should use. 

|Option |When to use  |
|---------|---------|
|**None**|When the plug-in type set for this Custom API will the only logic that occurs when this operation executes.<br/>You will not allow another developer to register any additional steps that may trigger additional logic, modify the behavior of this operation, or cancel the operation.<br/>Use this when the Custom API provides some capability that will not be of interest to business processes.|
|**Async Only**|When you want to allow other developers to detect when this operation occurs, but you do not want them to be able to cancel the operation or customize the behavior of the operation.<br/> Other developers can register asynchronous steps to detect that this operation occurred and respond to it after it has completed.<br/>This is the option recommended if you are using the Business Events pattern. A Business event will create a trigger in Power Automate to you can use when this event occurs. More information: [Microsoft Dataverse business events](business-events.md)|
|**Sync and Async**|When you want to allow other developers to have the ability to change the behavior of the operation and even cancel it if their business logic dictates.<br/>If the operation succeeds, other developers can also detect this and add logic to run asynchronously.<br/>Most Dataverse messages enable extension in this manner.  Use this when your message represents a business process that should be customizable.|

## Select a Binding Type

Binding is an OData concept that associates an operation to a specific table. The following table describes the Custom API **Binding Type**(`BindingType`) you should use.

|Option |When to use  |
|---------|---------|
|**Global** |When the operation does not apply to a specific table.|
|**Entity**|When the operation accepts a single record of a specific table as a parameter.|
|**EntityCollection**|When the operation applies changes to, or returns a collection of a specific table.|

Selecting **Entity** or **EntityCollection** will require that you use the fully qualified name of the Function or Action when you use the Web API. The fully qualified name is `Microsoft.Dynamics.CRM.<UniqueName of the Custom API>`. 

More information: 
 - [Actions bound to a table](webapi/use-web-api-actions.md#actions-bound-to-a-table)
 - [Actions bound to a table collection](webapi/use-web-api-actions.md#actions-bound-to-a-table-collection)
 - [Bound functions](webapi/use-web-api-functions.md#bound-functions)

When you select **Entity**, a request parameter named `Target` with the type <xref:Microsoft.Xrm.Sdk.EntityReference>  is created automatically. You do not need to create it. This value will be passed to any plug-ins registered for this message.

When you select **EntityCollection**, no parameter or response property representing the entity collection is included. Setting this binding simply adds the requirement that the operation be invoked appended to the entityset when using the Web API.

> [!NOTE]
> These binding types are available for you to use when composing your Custom API, but it is not required that you bind to an entity or entity collection. You can compose all your Custom API as **Global** and add whichever request parameters or response properties you need to achieve the same functionality as a bound Function or Action.

## When to create a Function

The Custom API **Is Function**property controls whether the Custom API will be a *Function* or *Action*. In OData a Function is an operation called using HTTP `GET` request which returns data without making any changes. With a `GET` request, all the parameters are passed as parameters in the URL when invoking the function.

You can more easily test `GET` requests using your browser alone, but there is a limit to the length of the URL that can be sent, usually around 2000 characters. More information: [Use Web API functions](webapi/use-web-api-functions.md)

> [!NOTE]
> - Functions must return some data. You must include at least one response property for the Custom API to be valid.
>    - A function that does not include a response property will not appear within the Web API $metadata service document.
>    - If you try to use an invalid function, you will get a `404 Not found` error similar to this:<br />`{"error":{"code":"0x8006088a","message":"Resource not found for the segment 'your_function_name'."}}`
> - A Function is not allowed when the **Enabled for Workflow**option is selected. See [Enabled for Workflow](#enabled-for-workflow)

If your Custom API has many complex request parameters which could cause the length of the URL to be too long, it is acceptable to create an Action that performs the same operation passing all the parameter data in the body using a `POST` request.

> [!IMPORTANT]
> Currently the [Microsoft Dataverse Connector](/connectors/commondataserviceforapps/) only enables performing actions. If you need the operation to be performed using Power Automate, you should create your Custom API as an Action.

## When to make your Custom API private

By default any Custom API you create will be available for other developers to discover and use. As the Custom API publisher, you have an obligation to maintain the public APIs you create. You should not remove your API or apply any changes which will break other consumers.

If you are not willing to support other developers using your Custom API, you should set the Custom API **Is Private** (`IsPrivate`) property to true before you ship the managed solution containing your Custom API.

The **Is Private** property will block the Custom API from appearing within the $metadata service document and prevent Dataverse code generation tools from creating classes to use the messages for your Custom API.

This doesn't mean that other developers cannot use your message if they know about it and are able to compose a request to use it. Setting the **Is Private** property is a way to indicate that you do not support other developers using your message. 

You may want to keep a Custom API private until you are sure that you will not need to remove it or introduce some breaking change.

You can leave **Is Private** set to false in your development environment so you can see the output in the $metadata service document or generate classes for your own use. However, before you ship the Custom API in your managed solution, you should set **Is Private** to true.

More information: 
- [CSDL $metadata document](webapi/web-api-types-operations.md#csdl-metadata-document)
- [Generate early-bound classes for the Organization service](org-service/generate-early-bound-classes.md)
- [Private Messages](org-service/use-messages.md#private-messages)

## Execute Privilege Name

Set the Custom API **Execute Privilege Name** (`ExecutePrivilegeName`) property to the name of the privilege to require it. There is currently no supported way for developers outside of Microsoft to create new privileges, but an existing privilege can be used. More information: [Q: Can I create a new privilege for my Custom API?](custom-api.md#q-can-i-create-a-new-privilege-for-my-custom-api) 

## Plugin Type

If you do not set the Custom API **Plugin Type** (`PluginTypeId`)  to specify main operation logic the API can still be called.

You may choose to not include any logic in the plug-in because you are using the Custom API as a business event. More information: [Microsoft Dataverse business events](business-events.md).

You might want to do this as a testing step, but any output parameter values will return the default values for the type because there is no code to set them.

## Enabled for Workflow

Set the Custom API **Enabled for Workflow** (`WorkflowSdkStepEnabled`) to true when you need to enable calling a Custom API as a workflow action. However, when this is selected the following limitations are imposed so that the Custom API can be called in the workflow designer:

- The Custom API cannot be a function, **Is Function** must be false.
- The Custom API can only have request parameter or response property types that workflow supports:
  - Boolean
  - DateTime
  - Decimal
  - EntityReference
    - EntityReference can only be used when the Custom API is bound to to an entity.
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



## Invoking Custom APIs

A Custom API creates a new message which can be invoked via the Web API or Organization Service SDK just like any other operation.

### Invoking Custom APIs from the Web API

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

#### Bound Action

This action named `myapi_CustomBoundAPI` is bound to the account table:

```http
GET [Organization URI]/api/v9.1/accounts(ed5d4e42-850c-45b7-8b38-2677545107cc)/Microsoft.Dynamics.CRM.myapi_CustomBoundAPI()
OData-MaxVersion: 4.0
OData-Version: 4.0
Content-Type: application/json; charset=utf-8
```

#### Bound Function

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

### Invoking Custom APIs from the Organization Service

You can choose to use either early-bound or late-bound code to invoke your custom API. Use the [CrmSvcUtil](./org-service/generate-early-bound-classes.md) tool to generate helper request and response classes to mirror the request and response properties of your custom API.

For late-bound code, or for a Custom API that you have marked as private, create an `OrganizationRequest` with the unique name of your custom API and add parameters with names matching the unique names of the request properties.

Entity-bound custom APIs have an implicit request property named `Target` that should be set to an `EntityReference` of the record to invoke the API on.

You can access response properties from the parameters of the returned response.

In this example a Custom API named `myapi_EscalateCase` is bound to the incident table to accept a record as the `Target` parameter together with another option set value request parameter named `Priority`. It has an `EntityReference` response property named `AssignedTo`    .

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

For more information about writing plug-ins, see [Tutorial: Write and register a plug-in](tutorial-write-plug-in.md). You need to register the assembly, but you do not need to register a step.

See the example [Sample: IsSystemAdmin Custom API](org-service/samples/issystemadmin-customapi-sample-plugin.md)

After you have registered the assembly, make sure to add the assembly and any types to your solution.



## Localized Label values

Custom APIs have some localizable labels. You can localize the label values using the steps documented here: [Translate localizable text for model-driven apps](../../maker/model-driven-apps/translate-localizable-text.md) and [Translating labels and display strings](/power-platform/alm/create-solutions-support-multiple-languages#translating-labels-and-display-strings).

This process involves exporting a file that contains the base language values and will include a column for each additional language enabled. You can then edit the values in Excel. After you complete the process to import the translations the labels will be included in your solution.

The following example shows editing the Excel worksheet to add Japanese translations for the English values.

:::image type="content" source="media/solution-strings-for-translation.png" alt-text="Shows how labels are localized.":::

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

A: Your private messages will work regardless of whether they are advertised in the Web API [CSDL $metadata document](webapi/web-api-types-operations.md#csdl-metadata-document) or not. While you develop your solution, you can leave the `IsPrivate` value set to `false`. This way you can refer to the `$metadata` listing and use code generation tools that depend on this data. However, you should set the `CustomAPI.IsPrivate` value to `true` before you ship your solution for others to use. If you later decide that you wish to support other applications to use the message, you can change the `CustomAPI.IsPrivate` value to `false`.

More information:

- [When to make your Custom API private](customapi-table-columns.md#when-to-make-your-custom-api-private)
- [Private Messages](org-service/use-messages.md#private-messages)
- [Private messages cannot be used in plug-ins](#private-messages-cannot-be-used-in-plug-ins)

## Known issues with Custom APIs

Custom API is now generally available, but there are still some related capabilities that we expect to change.

### Not able to use profiler for debugging

To debug using the Plug-in Registration tool and the Plug-in profiler solution, you need to be able to select a specific plug-in step. The main stage implementation for the plug-in is not currently available in the Plug-in Registration tool.

**Workaround**: Register the plug-in type on the `PostOperation` stage of the message created for the Custom API.

### Private messages cannot be used in plug-ins

If you define your custom API to be private, you cannot use that message in a plug-in. More information: [Private Messages](org-service/use-messages.md#private-messages)

### Next Steps

[Create a Custom API using the plug-in registration tool](create-custom-api-prt.md)<br />

### See also

[Create and use Custom APIs](custom-api.md)<br />
[Create a Custom API with code](create-custom-api-with-code.md)<br />
[Create a Custom API with solution files](create-custom-api-solution.md)<br />
[Create your own messages](custom-actions.md)<br />
[CustomAPI Table Columns](customapi-table-columns.md)<br />
[CustomAPIRequestParameter Table Columns](customapirequestparameter-table-columns.md)<br />
[CustomAPIRequestParameter Table Columns](customapirequestparameter-table-columns.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
