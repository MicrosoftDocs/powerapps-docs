---
title: "CustomAPIResponseProperty table columns (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Describes the table columns (entity attributes) to set when creating a Custom API Response Property" # 115-145 characters including spaces. This abstract displays in the search result.
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

# CustomAPIResponseProperty Table Columns

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

The object returned for your Custom API message will include any response properties you define. It is not required for a Custom API Action to return any value, but it must return a value if defined as a Function.

> [!IMPORTANT]
> A Custom API that represents a function with no response properties is not valid and will not appear in the Web API $metadata service document. If you try to use it, you will get a `404 Not Found` error similar to this: 
>
> `{"error":{"code":"0x8006088a","message":"Resource not found for the segment 'your_function_name'."}}`.
>
> You must also set the data to be returned in the plug-in for the function. If no data is set to be returned by the plug-in, the operation will return `204 No Content`.

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
|**Type**<br />`Type`<br />``|Picklist|The data type of the custom API response property <ul> <li>**Value**: 0 **Label**: Boolean </li> <li>**Value**: 1 **Label**: DateTime</li> <li>**Value**: 2 **Label**: Decimal </li> <li>**Value**: 3 **Label**: Entity</li> <li>**Value**: 4 **Label**: EntityCollection </li> <li>**Value**: 5 **Label**: EntityReference</li> <li>**Value**: 6 **Label**: Float </li> <li>**Value**: 7 **Label**: Integer</li> <li>**Value**: 8 **Label**: Money </li> <li>**Value**: 9 **Label**: Picklist</li> <li>**Value**: 10 **Label**: String </li> <li>**Value**: 11 **Label**: StringArray </li> <li>**Value**: 12 **Label**: Guid </li> </ul>**Cannot be changed after it is saved.**|
|**Unique Name** <br />`UniqueName`<br />`uniquename`|Text<br />String|Unique name for the custom API response property . This will be the name of the parameter when you call the Custom API.<br/>**Cannot be changed after it is saved.**|

> [!NOTE]
> Some values are not valid for update. They cannot be changed after the Custom API Response Property is saved. If you need to change one of these values, you must delete the Custom API Response Property and re-create it with the changes you want to make.

### See also

[CustomAPIResponseProperty table reference](reference/entities/customapiresponseproperty.md)<br />
[Create and use Custom APIs](custom-api.md)<br />
[Create a Custom API with code](create-custom-api-with-code.md)<br />
[Create a Custom API with solution files](create-custom-api-solution.md)<br />
[Create your own messages](custom-actions.md)<br />

[!INCLUDE[footer-include](../../includes/footer-banner.md)]