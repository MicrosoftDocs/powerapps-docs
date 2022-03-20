---
title: "CustomAPI table columns (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Describes the table columns (entity attributes) to set when creating a Custom API" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/14/2022
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

# CustomAPI Table Columns

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

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

> [!NOTE]
> Some values are not valid for update. They cannot be changed after the Custom API is saved. You should have a clear understanding of how your API should work before you begin. If you need to change any values that are not valid for update, you will have to delete the Custom API table record and start over. Deleting the Custom API record will delete any Custom API Request Parameters or Custom API Response Properties associated with it.

## Select a Custom Processing Step Type

The following table describes which **Custom Processing Step Type** (`AllowedCustomProcessingStepType`) you should use. 

|Option |When to use  |
|---------|---------|
|**None**|When the plug-in type set for this Custom API will the only logic that occurs when this operation executes.<br/>You will not allow another developer to register any additional steps that may trigger additional logic, modify the behavior of this operation, or cancel the operation.<br/>Use this when the Custom API provides some capability that will not be of interest to business processes.|
|**Async Only**|When you want to allow other developers to detect when this operation occurs, but you do not want them to be able to cancel the operation or customize the behavior of the operation.<br/> Other developers can register asynchronous steps to detect that this operation occurred and respond to it after it has completed.<br/>This is the option recommended if you are using the Business Events pattern. A Business event will create a trigger in Power Automate to you can use when this event occurs. More information: [Microsoft Dataverse business events](business-events.md)|
|**Sync and Async**|When you want to allow other developers to have the ability to change the behavior of the operation and even cancel it if their business logic dictates.<br/>If the operation succeeds, other developers can also detect this and add logic to run asynchronously.<br/>Most Dataverse messages enable extension in this manner.  Use this when your message represents a business process that should be customizable.|

## Select a Binding Type

Binding is an OData concept that associates an operation to a specific table. The following table describes the **Binding Type**(`BindingType`) you should use.

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

In OData a Function is an operation called using HTTP `GET` request which returns data without making any changes. With a `GET` request, all the parameters are passed as parameters in the URL when invoking the function.

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

If you are not willing to support other developers using your Custom API, you should set the **Is Private** (`IsPrivate`) property to true before you ship the managed solution containing your Custom API.

The **Is Private** property will block the Custom API from appearing within the $metadata service document and prevent Dataverse code generation tools from creating classes to use the messages for your Custom API.

This doesn't mean that other developers cannot use your message if they know about it and are able to compose a request to use it. Setting the **Is Private** property is a way to indicate that you do not support other developers using your message. 

You may want to keep a Custom API private until you are sure that you will not need to remove it or introduce some breaking change.

You can leave **Is Private** set to false in your development environment so you can see the output in the $metadata service document or generate classes for your own use. However, before you ship the Custom API in your managed solution, you should set **Is Private** to true.

More information: 
- [CSDL $metadata document](webapi/web-api-types-operations.md#csdl-metadata-document)
- [Generate early-bound classes for the Organization service](org-service/generate-early-bound-classes.md)
- [Private Messages](org-service/use-messages.md#private-messages)

## Execute Privilege Name

Set the **Execute Privilege Name** (`ExecutePrivilegeName`) property to the name of the privilege to require it. There is currently no supported way for developers outside of Microsoft to create new privileges, but an existing privilege can be used. More information: [Q: Can I create a new privilege for my Custom API?](custom-api.md#q-can-i-create-a-new-privilege-for-my-custom-api) 

## Plugin Type

If you do not set the **Plugin Type** (`PluginTypeId`)  to specify main operation logic the API can still be called. 

You may choose to not include any logic in the plug-in because you are using the Custom API as a business event. More information: [Microsoft Dataverse business events](business-events.md).

You might want to do this as a testing step, but any output parameter values will return the default values for the type because there is no code to set them.

## Enabled for Workflow

Set **Enabled for Workflow** (`WorkflowSdkStepEnabled`) to true when you need to enable calling a Custom API as a workflow action. However, when this is selected the following limitations are imposed so that the Custom API can be called in the workflow designer:

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
  

### See also

[CustomAPI table reference](reference/entities/customapi.md)<br />
[Create and use Custom APIs](custom-api.md)<br />
[Create a Custom API with code](create-custom-api-with-code.md)<br />
[Create a Custom API with solution files](create-custom-api-solution.md)<br />
[Create your own messages](custom-actions.md)<br />


[!INCLUDE[footer-include](../../includes/footer-banner.md)]