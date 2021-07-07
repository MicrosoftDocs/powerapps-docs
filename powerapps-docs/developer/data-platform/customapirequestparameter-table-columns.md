---
title: "CustomAPIRequestParameter table columns (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Describes the table columns (entity attributes) to set when creating a Custom API Request Parameter" # 115-145 characters including spaces. This abstract displays in the search result.
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

# CustomAPIRequestParameter Table Columns

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

A custom API isn’t required to have any parameters. There is no specified order for the parameters, they are identified by name.

A parameter is related to a single Custom API. You cannot define multiple Custom APIs to use the same parameter definition. You can define multiple request parameter with the same `UniqueName` value if they are used by different Custom APIs.

> [!NOTE]
> If you define a bound table for your Custom API, the request parameter will be generated for you. You don’t need to create an input parameter for the table when the Custom API is bound to a table.
> 
> If you bind your Custom API to a table (entity) collection, there will not be a request parameter generated for you. Binding a Custom API to a entity collection requires that the Custom API be called using the entityset resource path.
>
> Binding to an entity collection only sets the expectation that the scope of the operation will apply more than one table of that type, or that it will return a collection of that type. It does not provide an entity collection input parameter for your plug-in to process.

The table shown below includes columns (attributes) of the Custom API Request Parameter table that you can set.

|Display Name<br />Schema Name<br />Logical Name  |Type  |Description |
|---------|---------|---------|
|**Custom API Request Parameter**<br />`CustomAPIRequestParameterId`<br />`customapirequestparameterid`|Unique Identifier<br />Guid|Unique identifier for custom API request parameter instances.<br/>**Cannot be changed after it is saved.**|
|**Custom API** <br />`CustomAPIId`<br />`customapiid`|Lookup|Unique identifier for the custom API that this custom API request parameter is associated with.<br/>**Cannot be changed after it is saved.**|
|**Description**<br />`Description`<br />`description`|Text<br />String|Localized description for custom API request parameter instances. For use when the message parameter is exposed to be called in an app. For example, as a [ToolTip](https://wikipedia.org/wiki/Tooltip).|
|**Display Name** <br />`DisplayName`<br />`displayname`|Text<br />String|Localized display name for custom API request parameter instances. For use when the message parameter is exposed to be called in an app.|
|**Is Customizable**<br />`IsCustomizable`<br />`iscustomizable`|ManagedProperty|Whether the custom api request parameter can be customized or deleted when part of a managed solution.|
|**Is Optional**<br />`IsOptional`<br />`isoptional`|Yes/No<br />Boolean|Indicates if the custom API request parameter is optional. If it is not optional, it is required to pass a value for this parameter when using the message.<ul> <li>**Value**: 0 **Label**: No </li> <li>**Value**: 1 **Label**: Yes</li> </ul>**Cannot be changed after it is saved.**|
|**Logical Entity Name**<br />`LogicalEntityName`<br />`logicalentityname`|Text<br />String|The logical name of the table bound to the custom API request parameter.<br/>**Cannot be changed after it is saved.**|
|**Name**<br />`Name`<br />`name`|Text<br />String|The primary name of the custom API request parameter.  This will display in the list of custom api request parameters when viewed in the solution. Use this to differentiate this parameter from others that share a common Unique Name. <br />This naming convention is recommended: `{Custom API Unique Name}.{Parameter UniqueName}`|
|**Owner** <br />`OwnerId`<br />`ownerid`|Owner|A reference to the user or team that owns the API.|
|**Type**<br />`Type`<br />`type`|Choice<br />Picklist|The data type of the custom API request parameter.<ul> <li>**Value**: 0 **Label**: Boolean </li> <li>**Value**: 1 **Label**: DateTime</li> <li>**Value**: 2 **Label**: Decimal </li> <li>**Value**: 3 **Label**: Entity</li> <li>**Value**: 4 **Label**: EntityCollection </li> <li>**Value**: 5 **Label**: EntityReference</li> <li>**Value**: 6 **Label**: Float </li> <li>**Value**: 7 **Label**: Integer</li> <li>**Value**: 8 **Label**: Money </li> <li>**Value**: 9 **Label**: Picklist</li> <li>**Value**: 10 **Label**: String </li> <li>**Value**: 11 **Label**: StringArray </li> <li>**Value**: 12 **Label**: Guid </li> </ul>**Cannot be changed after it is saved.**|
|**Unique Name** <br />`UniqueName`<br />`uniquename`|Text<br />String|Unique name for the custom API request parameter. This will be the name of the parameter when you call the Custom API.<br/>**Cannot be changed after it is saved.**|

> [!NOTE]
> Some values are not valid for update. They cannot be changed after the Custom API Request Parameter is saved. If you need to change one of these values, you must delete the Custom API Request Parameter and re-create it with the changes you want to make.

### See also

[CustomAPIRequestParameter table reference](reference/entities/customapirequestparameter.md)<br />
[Create and use Custom APIs](custom-api.md)<br />
[Create a Custom API with code](create-custom-api-with-code.md)<br />
[Create a Custom API with solution files](create-custom-api-solution.md)<br />
[Create your own messages](custom-actions.md)<br />

[!INCLUDE[footer-include](../../includes/footer-banner.md)]