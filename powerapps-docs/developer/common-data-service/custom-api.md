---
title: "Create and use Custom APIs (Common Data Service) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Custom API is a new code-first way to define custom messages for the Common Data Service" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/19/2020
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

Custom APIs offer a new code-first way to define messages that you can add to CDS web services. Conceptually, Custom APIs are an extension to Custom Actions that have provided a no-code way to include custom messages. To differentiate between the two different kinds of Custom Action, we will use *Workflow Custom Action* to refer to the no-code capabilities that depend on workflow. *Custom API* will refer to the type of custom action that depends on a developer to write a plug-in.

Custom APIs provide a capabilities specifically for developers to define their logic in code. For a full comparison of Workflow Custom Action and Custom API, see [Compare Workflow Custom Action and Custom API](custom-actions.md#compare-workflow-custom-action-and-custom-api).



## Create a custom API

Create a custom API
Because a Custom API requires a plug-in to implement any logic to be defined by the main operation, you can approach the development of your custom API by:

- Developing the plug-in first, and then define the Custom API for it.
- Define the Custom API first, then write the plug-in to implement it.

Your Custom API will be completed when the data defining the Custom API is saved and linked to the Plug-in type to define the main operation. In either case, you should understand the data that drives the Custom API.

There are several different ways to create a custom API:

- By manually entering data in available forms.  More information: [Create a Custom API in the maker portal](create-custom-api-maker-portal.md)
- By using the web services, such as the Web API or Organization Service. More information: [Create a Custom API with code](create-custom-api-with-code.md)
- By editing solution files. More information: [Create a Custom API with solution files](create-custom-api-solution.md).

Regardless of the process you use, the following information describes selected attributes for the three entities that contain the data for a Custom API. You should review this as you plan the behavior for your Custom API.

### CustomAPI entity attributes

This table includes attributes of the Custom API entity that you can set.


|Display Name<br />Schema Name  |Type  |Description |
|---------|---------|---------|
|**Allowed Custom Processing Step Type**<br />`AllowedCustomProcessingStepType`|Picklist|The type of custom processing steps allowed for this Custom API. This allows you to control whether other plug-ins can be registered<ul> <li>**Value**: 0 **Label**: None **Meaning**: No custom processing steps allowed.</li> <li>**Value**: 1 **Label**: Async Only **Meaning**: Only asynchronous custom processing steps allowed</li> <li>**Value**: 2 **Label**: Sync and Async **Meaning**: No restriction.</li> </ul> **Cannot be changed after it is saved.**|
|**Binding Type**<br />`BindingType`|Picklist|The binding type of the custom API.<ul><li>**Value**: 0 **Label**: Global</li><li>**Value**: 1 **Label**: Entity</li><li>**Value**: 2 **Label**: EntityCollection</li></ul>**Cannot be changed after it is saved.**|
|**Bound Entity Logical Name**<br />`BoundEntityLogicalName`|String|The logical name of the entity bound to the custom API if it is not Global.<br />**Cannot be changed after it is saved.**|
|**Custom API**<br />`CustomAPIId`|Uniqueidentifier|Unique identifier for custom API instances<br />**Cannot be changed after it is saved.**|
|**Description**<br />`Description`|String|Localized description for this Custom API. For use when the message is exposed to be called in an app. For example, as a [ToolTip](https://wikipedia.org/wiki/Tooltip).|
|**Display Name**<br />DisplayName|String|Localized display name for this Custom API. For use when the message is exposed to be called in an app.|
|**Execute Privilege Name**<br />`ExecutePrivilegeName`|String|(Optional) Name of the privilege that allows execution of the custom API|
|**Is Function**<br />`IsFunction`|Boolean|Indicates if the custom API is a function. A function requires the HTTP GET method. Otherwise the Http POST method is required.<ul> <li>**Value**: 0 **Label**: No</li> <li>**Value**: 1 **Label**: Yes</li> </ul>**Cannot be changed after it is saved.**|
|**Is Private**<br />`IsPrivate`|Boolean|Indicates if the custom API is private (hidden from metadata and documentation)<ul> <li>**Value**: 0 **Label**: No </li> <li>**Value**: 1 **Label**: Yes</li> </ul>|
|**Name**<br />`Name`|String|The primary name of the custom API. This will display in the list of custom apis when viewed in the solution.|
|**Owner**<br />`OwnerId`|Owner|A reference to the user or team that owns the API. |
|**Plugin Type**<br />`PluginTypeId`|Lookup|A reference to the plug-in type that provides the main operation for this Custom API|
|**Unique Name**<br />`UniqueName`|String|Unique name for the custom API. This will be the name of the message created.<br /> This value must include a customization prefix. It should match the prefix set for your solution publisher.<br />**Cannot be changed after it is saved.**|

> [!NOTE]
> Some values are not valid for update. They cannot be changed after the Custom API is saved. You should have a clear understanding of how your API should be before you begin. If you need to change any values that are not valid for update, you will have to delete the Custom API entity record and start over. Deleting the Custom API record will delete any Custom API Request Parameters or Custom API Response Properties associated with it.

Set the **Execute Privilege Name** property to the name of the privilege to require it. There is currently no supported way for developers outside of Microsoft to create new privileges, but an existing privilege can be used.

If you do not set the **Plugin Type** (`PluginTypeId`)  to specify main operation logic the API can still be called. You might need to do this as a testing step, but any output parameter values will return the default values for the type because there is no code to set them.

**Known Issues**:

- The **Is Private** property is not included in the form. If you want to make your Custom API private, you must update it using code.
- If you define your Custom API as a function by setting the **Is Function** property to true, you cannot bind the function to an entity or entity collection. You also cannot use any **Entity** or **EntityCollection** request parameters or output properties.

### CustomAPIRequestParameter entity attributes

A custom API isn’t required to have any parameters. There is no specified order for the parameters, they are identified by name. 

A parameter is related to a single Custom API. You cannot define multiple Custom APIs to use the same parameter definition. You can define multiple request parameter with the same UniqueName value if they are unique within the Custom API they are related to.

If you define a bound entity or entity collection for your Custom API, the parameter will be generated for you. You don’t need to create a parameter for bound entities.

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
|**Type**<br />`Type`|Picklist|The data type of the custom API request parameter.<ul> <li>**Value**: 0 **Label**: Boolean </li> <li>**Value**: 1 **Label**: DateTime</li> <li>**Value**: 2 **Label**: Decimal </li> <li>**Value**: 3 **Label**: Entity</li> <li>**Value**: 4 **Label**: EntityCollection </li> <li>**Value**: 5 **Label**: EntityReference</li> <li>**Value**: 6 **Label**: Float </li> <li>**Value**: 7 **Label**: Integer</li> <li>**Value**: 8 **Label**: Money </li> <li>**Value**: 9 **Label**: Picklist</li> <li>**Value**: 10 **Label**: String </li> </ul>**Cannot be changed after it is saved.**|
|**Unique Name** <br />`UniqueName`|String|Unique name for the custom API request parameter. This will be the name of the parameter when you call the Custom API.<br/>**Cannot be changed after it is saved.**|

> [!NOTE]
> Some values are not valid for update. They cannot be changed after the Custom API Request Parameter is saved. If you need to change one of these values, you must delete the Custom API Request Parameters and re-create it with the changes you want to make.

### CustomAPIResponseProperty entity attributes

The object returned for your Custom API message will include any response properties you define. It is not required for a Custom API to return any value, but if the custom API is defined as a function it is expected.

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
|**Type**<br />`Type`|Picklist|The data type of the custom API response property <ul> <li>**Value**: 0 **Label**: Boolean </li> <li>**Value**: 1 **Label**: DateTime</li> <li>**Value**: 2 **Label**: Decimal </li> <li>**Value**: 3 **Label**: Entity</li> <li>**Value**: 4 **Label**: EntityCollection </li> <li>**Value**: 5 **Label**: EntityReference</li> <li>**Value**: 6 **Label**: Float </li> <li>**Value**: 7 **Label**: Integer</li> <li>**Value**: 8 **Label**: Money </li> <li>**Value**: 9 **Label**: Picklist</li> <li>**Value**: 10 **Label**: String </li> </ul>**Cannot be changed after it is saved.**|
|**Unique Name** <br />`UniqueName`|String|Unique name for the custom API response property . This will be the name of the parameter when you call the Custom API.<br/>**Cannot be changed after it is saved.**|

> [!NOTE]
> Some values are not valid for update. They cannot be changed after the Custom API Response Property is saved. If you need to change one of these values, you must delete the Custom API Response Property and re-create it with the changes you want to make.

## Frequently Asked Questions (FAQs)

### Q: Do I have to provide localized display names and descriptions for my Custom API, parameters, and response properties?

A: No, you don’t but it is strongly recommended.

### Q: How to provide localized values for the localized display names? 

A: You don’t need to provide the localized values. These values are typically localized on a per environment case depending on the additional languages they have enabled. But if you wish to include them in your solution you can. More information: [Translating labels and display strings](/alm/create-solutions-support-multiple-languages#translating-labels-and-display-strings)

### Q: Can I activate or deactivate Custom API records?

A: You cannot. Although these records have the common **Status** and **Status Reason**fields found on most Common Data Service entities. Setting the values for these fields has no impact on the availability of the Custom API, the request parameters, or the response properties.

## Known issues with Custom APIs

Custom APIs are a preview feature and subject to change. Following are some known issues we expect to change.

### A custom API cannot be called from a workflow

A Workflow Custom Action can be called from another workflow. Currently, Custom APIs cannot.

### A custom API created is not added to the current solution

When you created a Custom API you should do so in the context of a solution. Normally, when you create a new solution component in the context of a solution, it is included in that solution. Currently, even when you create a Custom API in the context of a solution, you must still manually add each part to the solution by selecting the **Add Existing** button.

### The Is Private field is not included in the Custom API form

The **Is Private** field is not available in the form when you create a Custom API in the UI. You cannot add this field to the form. You must set this field programmatically or by editing the solution XML files.

### Custom API entities can be related to other entities

It is currently possible for entities to create relationships with the three Custom API entities. This capability will be removed. Do not create entity relationships between these entities and any other.

### The Name field value is displayed in the solution components view where the Display Name value should be shown

When viewing the Custom API entities in a solution, the **Display Name**column shows the **Name** value rather than the **Display Name** value.

### Custom API and related records cannot be created using one operation

It is not possible to create the Custom API, Custom API Request Parameter, and Custom API Response Properties in a single operation using 'deep-insert' as described in [Create related entity records in one operation](webapi/create-entity-web-api.md#create-related-entity-records-in-one-operation) and [Create related entities in one operation](org-service/entity-operations-create.md#create-related-entities-in-one-operation). Instead, each record must be created individually and be related to the Custom API record.

### Next Steps

[Create a Custom API in the maker portal](create-custom-api-maker-portal.md)<br />