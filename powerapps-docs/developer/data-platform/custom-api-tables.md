---
title: "CustomAPI tables (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Describes the tables and column values to use when creating custom APIs." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 02/24/2023
ms.reviewer: jdaly
ms.topic: article
author: divkamath # GitHub ID
ms.subservice: dataverse-developer
ms.author: dikamath # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
contributors:
 - JimDaly
---
# CustomAPI tables

The data that defines custom APIs is in the following tables/entities:

- [CustomAPI Reference](reference/entities/customapi.md)
- [CustomAPIRequestParameter Reference](reference/entities/customapirequestparameter.md)
- [CustomAPIResponseProperty Reference](reference/entities/customapiresponseproperty.md)

The sections in this topic below provide detailed information about the column values you will use most.

- [custom API table columns](#custom-api-table-columns)
- [CustomAPIRequestParameter Table Columns](#customapirequestparameter-table-columns)
- [CustomAPIResponseProperty Table Columns](#customapiresponseproperty-table-columns)

This diagram shows how the tables are related to these tables as well as others:

:::image type="content" source="media/custom-api-data-model.png" alt-text="Diagram showing relationships between tables.":::

The relationship to the [CatalogAssignment table](reference/entities/catalogassignment.md) enables using custom API with [Microsoft Dataverse business events](business-events.md). More information: [Catalog and CatalogAssignment tables](catalog-catalogassignment.md).

## Retrieve data about custom APIs

You can use the following queries to retrieve data about custom APIs.

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

// using (var svc = new ServiceClient(conn))
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

## custom API table columns

The table below includes selected columns of a custom API table that you can set.  

|Display Name<br />Schema Name<br />Logical Name  |Type  |Description |
|---------|---------|---------|
|**Allowed Custom Processing Step Type**<br />`AllowedCustomProcessingStepType`<br />`allowedcustomprocessingsteptype`|Choice<br />Picklist|<ul> <li>**Value**: 0<br />**Label**: None<br />**Meaning**: No custom processing steps allowed.</li> <li>**Value**: 1<br />**Label**: Async Only<br />**Meaning**: Only asynchronous custom processing steps allowed</li> <li>**Value**: 2<br />**Label**: Sync and Async<br />**Meaning**: No restriction. 3rd party plug-ins can add synchronous logic to change the behavior of the message.</li> </ul>See [Select a Custom Processing Step Type](custom-api.md#select-a-custom-processing-step-type)<br/>**Cannot be changed after it is saved.**|
|**Binding Type**<br />`BindingType`<br />`bindingtype`|Choice<br />Picklist|<ul><li>**Value**: 0 **Label**: Global</li><li>**Value**: 1 **Label**: Entity</li><li>**Value**: 2 **Label**: EntityCollection</li></ul>See [Select a Binding Type](custom-api.md#select-a-binding-type)<br />**Cannot be changed after it is saved.**|
|**Bound Entity Logical Name**<br />`BoundEntityLogicalName`<br />`boundentitylogicalname`|Text<br />String|The logical name of the table bound to the custom API if it is not Global.<br />**Cannot be changed after it is saved.**|
|**custom API**<br />`CustomAPIId`<br />`customapiid`|Unique Identifier<br />Guid|Unique Identifier for custom API instances<br />**Cannot be changed after it is saved.**|
|**Description**<br />`Description`<br />`description`|Text<br />String|Localized description for this custom API. For use when the message is exposed to be called in an app. For example, as a [ToolTip](https://wikipedia.org/wiki/Tooltip).|
|**Display Name**<br />`DisplayName`<br />`displayname`|Text<br />String|Localized display name for this custom API. For use when the message is exposed to be called in an app.|
|**Execute Privilege Name**<br />`ExecutePrivilegeName`<br />`executeprivilegename`|Text<br />String|(Optional) Name of the privilege that allows execution of the custom API. See: [Secure your custom API with a privilege](custom-api.md#secure-your-custom-api-with-a-privilege)|
|**Is Customizable**<br />`IsCustomizable`<br />`iscustomizable`|ManagedProperty|Whether the custom API can be customized or deleted when part of a managed solution.|
|**Is Function**<br />`IsFunction`<br />`isfunction`|Yes/No<br />Boolean|<ul> <li>**Value**: 0 **Label**: No</li> <li>**Value**: 1 **Label**: Yes</li> </ul>See [When to create a Function](custom-api.md#when-to-create-a-function)<br />**Cannot be changed after it is saved.**|
|**Is Private**<br />`IsPrivate`<br />`isprivate`|Yes/No<br />Boolean|<ul> <li>**Value**: 0 **Label**: No </li> <li>**Value**: 1 **Label**: Yes</li></ul>See [When to make your custom API private](custom-api.md#when-to-make-your-custom-api-private)|
|**Name**<br />`Name`<br />`name`|Text<br />String|The primary name of the custom API. This will display in the list of custom apis when viewed in the solution.|
|**Owner**<br />`OwnerId`<br />`ownerid`|Owner|A reference to the user or team that owns the API. |
|**Plugin Type**<br />`PluginTypeId`<br />`plugintypeid`|Lookup|A reference to the plug-in type that provides the main operation for this custom API. See: [Use a plug-in to include logic in your custom API](custom-api.md#use-a-plug-in-to-include-logic-in-your-custom-api)|
|**Unique Name**<br />`UniqueName`<br />`uniquename`|Text<br />String|Unique name for the custom API. This will be the name of the message created.<br /> This value must include a customization prefix that matches the prefix set for your solution publisher.<br /> This value can't contain any special characters.<br />**Cannot be changed after it is saved.**|
|**Enabled for Workflow**<br />`WorkflowSdkStepEnabled`<br />`workflowsdkstepenabled`|Yes/No<br />Boolean|Indicates if the custom API is enabled as a workflow action. See: [Use a custom API in a workflow](custom-api.md#use-a-custom-api-in-a-workflow)<br />**Cannot be changed after it is saved.**|

## CustomAPIRequestParameter Table Columns

A custom API isn't required to have any parameters. There is no specified order for the parameters, they are identified by name.

A parameter is related to a single custom API. You cannot define multiple custom APIs to use the same parameter definition. You can define multiple request parameter with the same `UniqueName` value if they are used by different custom APIs.

> [!NOTE]
> If you define a bound table for your custom API, the request parameter will be generated for you. You don't need to create an input parameter for the table when the custom API is bound to a table. More information: [Select a Binding Type](custom-api.md#select-a-binding-type)

The table shown below includes columns (attributes) of the custom API Request Parameter table that you can set.

|Display Name<br />Schema Name<br />Logical Name  |Type  |Description |
|---------|---------|---------|
|**custom API Request Parameter**<br />`CustomAPIRequestParameterId`<br />`customapirequestparameterid`|Unique Identifier<br />Guid|Unique identifier for custom API request parameter instances.<br/>**Cannot be changed after it is saved.**|
|**custom API** <br />`CustomAPIId`<br />`customapiid`|Lookup|Unique identifier for the custom API that this custom API request parameter is associated with.<br/>**Cannot be changed after it is saved.**|
|**Description**<br />`Description`<br />`description`|Text<br />String|Localized description for custom API request parameter instances. For use when the message parameter is exposed to be called in an app. For example, as a [ToolTip](https://wikipedia.org/wiki/Tooltip).|
|**Display Name** <br />`DisplayName`<br />`displayname`|Text<br />String|Localized display name for custom API request parameter instances. For use when the message parameter is exposed to be called in an app.|
|**Is Customizable**<br />`IsCustomizable`<br />`iscustomizable`|ManagedProperty|Whether the custom api request parameter can be customized or deleted when part of a managed solution. See [custom API Customization](custom-api.md#custom-api-customization)|
|**Is Optional**<br />`IsOptional`<br />`isoptional`|Yes/No<br />Boolean|Indicates if the custom API request parameter is optional. If it is not optional, it is required to pass a value for this parameter when using the message.<ul> <li>**Value**: 0 **Label**: No </li> <li>**Value**: 1 **Label**: Yes</li> </ul>**Cannot be changed after it is saved.**|
|**Logical Entity Name**<br />`LogicalEntityName`<br />`logicalentityname`|Text<br />String|The logical name of the table bound to the custom API request parameter.<br/>**Cannot be changed after it is saved.**|
|**Name**<br />`Name`<br />`name`|Text<br />String|The primary name of the custom API request parameter.  This will display in the list of custom api request parameters when viewed in the solution. Use this to differentiate this parameter from others that share a common Unique Name. <br />This naming convention is recommended: `{custom API Unique Name}.{Parameter UniqueName}`|
|**Owner** <br />`OwnerId`<br />`ownerid`|Owner|A reference to the user or team that owns the API.|
|**Type**<br />`Type`<br />`type`|Choice<br />Picklist|The data type of the custom API request parameter.<ul> <li>**Value**: 0 **Label**: Boolean </li> <li>**Value**: 1 **Label**: DateTime</li> <li>**Value**: 2 **Label**: Decimal </li> <li>**Value**: 3 **Label**: Entity</li> <li>**Value**: 4 **Label**: EntityCollection </li> <li>**Value**: 5 **Label**: EntityReference</li> <li>**Value**: 6 **Label**: Float </li> <li>**Value**: 7 **Label**: Integer</li> <li>**Value**: 8 **Label**: Money </li> <li>**Value**: 9 **Label**: Picklist</li> <li>**Value**: 10 **Label**: String </li> <li>**Value**: 11 **Label**: StringArray </li> <li>**Value**: 12 **Label**: Guid </li> </ul>**Cannot be changed after it is saved.**|
|**Unique Name** <br />`UniqueName`<br />`uniquename`|Text<br />String|Unique name for the custom API request parameter. This will be the name of the parameter when you call the custom API.<br /> This value can't contain any special characters.<br/>**Cannot be changed after it is saved.**|

## CustomAPIResponseProperty Table Columns

The object returned for your custom API message will include any response properties you define. It is not required for a custom API Action to return any value, but it must return a value if defined as a Function.

If there is only a single **Entity** or **EntityCollection** response property defined, the response will be of that type. If there are multiple parameters, or one or more parameter of a simple type, the API will return a complex type where each response property will be a property of that complex type.

For example, if your custom API Unique name is `sample_CustomAPIExample`, it will return a complex type named `sample_CustomAPIExampleResponse` with properties for each response property you define.

The table below includes columns (attributes) of the custom API Response Property table that you can set.

|Display Name<br />Schema Name<br />Logical Name  |Type  |Description |
|---------|---------|---------|
|**custom API Response Property**<br />`CustomAPIResponsePropertyId`<br />`customapiresponsepropertyid`|Unique Identifier<br />Guid|Unique identifier for custom API response property instances.<br/>**Cannot be changed after it is saved.**|
|**custom API** <br />`CustomAPIId`<br />`customapiid`|Lookup|Unique identifier for the custom API that this custom API response property is associated with. <br/>**Cannot be changed after it is saved.**|
|**Description**<br />`Description`<br />`description`|Text<br />String|Localized description for custom API response property  instances. For use when the message parameter is exposed to be called in an app. For example, as a [ToolTip](https://wikipedia.org/wiki/Tooltip).|
|**Display Name** <br />`DisplayName`<br />`displayname`|Text<br />String|Localized display name for custom API response property  instances. For use when the message parameter is exposed to be called in an app.|
|**Is Customizable**<br />`IsCustomizable`<br />`iscustomizable`|ManagedProperty|Whether the custom api response property can be customized or deleted when part of a managed solution.|
|**Logical Entity Name**<br />`LogicalEntityName`<br />`logicalentityname`|Text<br />String|When **Entity** or **EntityReference** are selected as the **Type**, you can specify the logical name of the table bound to the custom API response property. You cannot specify a **Logical Entity Name** when you choose **EntityCollection** as the **Type**.<br/>**Cannot be changed after it is saved.**|
|**Name**<br />`Name`<br />`name`|String|The primary name of the custom API response property .  This will display in the list of custom api request parameters when viewed in the solution. Use this to differentiate this parameter from others that share a common Unique Name. <br />This naming convention is recommended: `{custom API Unique Name}.{Property UniqueName}`|
|**Owner** <br />`OwnerId`<br />`ownerid`|Owner|A reference to the user or team that owns the API.|
|**Type**<br />`Type`<br />`type`|Picklist|The data type of the custom API response property <ul> <li>**Value**: 0 **Label**: Boolean </li> <li>**Value**: 1 **Label**: DateTime</li> <li>**Value**: 2 **Label**: Decimal </li> <li>**Value**: 3 **Label**: Entity</li> <li>**Value**: 4 **Label**: EntityCollection </li> <li>**Value**: 5 **Label**: EntityReference</li> <li>**Value**: 6 **Label**: Float </li> <li>**Value**: 7 **Label**: Integer</li> <li>**Value**: 8 **Label**: Money </li> <li>**Value**: 9 **Label**: Picklist</li> <li>**Value**: 10 **Label**: String </li> <li>**Value**: 11 **Label**: StringArray </li> <li>**Value**: 12 **Label**: Guid </li> </ul>**Cannot be changed after it is saved.**|
|**Unique Name** <br />`UniqueName`<br />`uniquename`|Text<br />String|Unique name for the custom API response property . This will be the name of the parameter when you call the custom API.<br /> This value can't contain any special characters.<br/>**Cannot be changed after it is saved.**|

### See also


[Create and use custom APIs](custom-api.md)<br />
[Create a custom API using the plug-in registration tool](create-custom-api-prt.md)<br />
[Create a custom API in Power Apps](create-custom-api-maker-portal.md)<br />
[Create a custom API with code](create-custom-api-with-code.md)<br />
[Create a custom API with solution files](create-custom-api-solution.md)<br />
[Create your own messages](custom-actions.md)<br />


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
