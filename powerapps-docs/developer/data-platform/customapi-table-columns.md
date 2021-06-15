---
title: "CustomAPI table columns (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Describes the table columns (entity attributes) to set when creating a Custom API" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 04/15/2021
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

# CustomAPI Table Columns

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

The table below includes selected columns of a Custom API table that you can set.  

|Display Name<br />Schema Name<br />Logical Name  |Type  |Description |
|---------|---------|---------|
|**Allowed Custom Processing Step Type**<br />`AllowedCustomProcessingStepType`<br />`allowedcustomprocessingsteptype`|Choice<br />Picklist|The type of custom processing steps allowed for this Custom API. This allows you to control whether other plug-ins can be registered<ul> <li>**Value**: 0 **Label**: None **Meaning**: No custom processing steps allowed.</li> <li>**Value**: 1 **Label**: Async Only **Meaning**: Only asynchronous custom processing steps allowed</li> <li>**Value**: 2 **Label**: Sync and Async **Meaning**: No restriction. 3rd party plug-ins can add synchronous logic to change the behavior of the message.</li> </ul> **Cannot be changed after it is saved.**|
|**Binding Type**<br />`BindingType`<br />`bindingtype`|Choice<br />Picklist|The binding type of the custom API.<ul><li>**Value**: 0 **Label**: Global</li><li>**Value**: 1 **Label**: Entity</li><li>**Value**: 2 **Label**: EntityCollection</li></ul>**Cannot be changed after it is saved.**|
|**Bound Entity Logical Name**<br />`BoundEntityLogicalName`<br />`boundentitylogicalname`|Text<br />String|The logical name of the table bound to the custom API if it is not Global.<br />**Cannot be changed after it is saved.**|
|**Custom API**<br />`CustomAPIId`<br />`customapiid`|Unique Identifier<br />Guid|Unique Identifier for custom API instances<br />**Cannot be changed after it is saved.**|
|**Description**<br />`Description`<br />`description`|Text<br />String|Localized description for this Custom API. For use when the message is exposed to be called in an app. For example, as a [ToolTip](https://wikipedia.org/wiki/Tooltip).|
|**Display Name**<br />`DisplayName`<br />`displayname`|Text<br />String|Localized display name for this Custom API. For use when the message is exposed to be called in an app.|
|**Execute Privilege Name**<br />`ExecutePrivilegeName`<br />`executeprivilegename`|Text<br />String|(Optional) Name of the privilege that allows execution of the custom API|
|**Is Customizable**<br />`IsCustomizable`<br />`iscustomizable`|ManagedProperty|Whether the Custom API can be customized or deleted when part of a managed solution.|
|**Is Function**<br />`IsFunction`<br />`isfunction`|Yes/No<br />Boolean|Indicates if the custom API is a function. A function requires the HTTP GET method. Otherwise the Http POST method is required.<ul> <li>**Value**: 0 **Label**: No</li> <li>**Value**: 1 **Label**: Yes</li> </ul>**Important**: A function MUST include at least one Response Property to be valid.<br/>More information: [Use Web API functions](webapi/use-web-api-functions.md)<br />**Cannot be changed after it is saved.**|
|**Is Private**<br />`IsPrivate`<br />`isprivate`|Yes/No<br />Boolean|Indicates if the custom API is private (hidden from table definitions and documentation) More information: [Private Messages](org-service/use-messages.md#private-messages)<ul> <li>**Value**: 0 **Label**: No </li> <li>**Value**: 1 **Label**: Yes</li> </ul>|
|**Name**<br />`Name`<br />`name`|Text<br />String|The primary name of the custom API. This will display in the list of custom apis when viewed in the solution.|
|**Owner**<br />`OwnerId`<br />`ownerid`|Owner|A reference to the user or team that owns the API. |
|**Plugin Type**<br />`PluginTypeId`<br />`plugintypeid`|Lookup|A reference to the plug-in type that provides the main operation for this Custom API|
|**Unique Name**<br />`UniqueName`<br />`uniquename`|Text<br />String|Unique name for the custom API. This will be the name of the message created.<br /> This value must include a customization prefix that matches the prefix set for your solution publisher.<br />**Cannot be changed after it is saved.**|

> [!NOTE]
> Some values are not valid for update. They cannot be changed after the Custom API is saved. You should have a clear understanding of how your API should work before you begin. If you need to change any values that are not valid for update, you will have to delete the Custom API table record and start over. Deleting the Custom API record will delete any Custom API Request Parameters or Custom API Response Properties associated with it.

Set the **Execute Privilege Name** property to the name of the privilege to require it. There is currently no supported way for developers outside of Microsoft to create new privileges, but an existing privilege can be used. More information: [Q: Can I create a new privilege for my Custom API?](custom-api.md#q-can-i-create-a-new-privilege-for-my-custom-api) 

If you do not set the **Plugin Type** (`PluginTypeId`)  to specify main operation logic the API can still be called. You might want to do this as a testing step, but any output parameter values will return the default values for the type because there is no code to set them.

### See also

[CustomAPI table reference](reference/entities/customapi.md)<br />
[Create and use Custom APIs](custom-api.md)<br />
[Create a Custom API with code](create-custom-api-with-code.md)<br />
[Create a Custom API with solution files](create-custom-api-solution.md)<br />
[Create your own messages](custom-actions.md)<br />


[!INCLUDE[footer-include](../../includes/footer-banner.md)]