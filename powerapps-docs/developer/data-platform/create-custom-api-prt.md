---
title: "Create a Custom API using the plug-in registration tool (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Create a Custom API using the plug-in registration tool" # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 03/13/2022
ms.reviewer: "jdaly"
ms.topic: "article"
author: "marcelbf" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Create a Custom API using the plug-in registration tool

The plug-in registration tool (PRT) includes a designer to create Custom API. The PRT is a Windows client application that is part of the developer tools you can download from NuGet.  See [Download tools from NuGet](download-tools-nuget.md) for information about downloading these tools.

[!INCLUDE [cc-connect-plugin-registration-tool](includes/cc-connect-plugin-registration-tool.md)]

## Create a Custom API

In the **Register** menu, select the **Register new Custom API** command. This will open the form to create a Custom API.

:::image type="content" source="media/create-custom-api-prt.png" alt-text="PRT Custom API form":::

Use the information in the table below to create the Custom API. 

> [!IMPORTANT]
> Some options cannot be changed after you save the Custom API. Make sure you understand the purpose of each setting that cannot be changed. If you later need to change this setting, you must delete and re-create the Custom API. This will also delete any request parameters or response properties that are associated with it.


|Label|Description|Can be changed|
|---------|---------|---------|
|**Display Name**|A localizable name. |Yes|
|**Name**|A friendly, non-localizable name.|Yes|
|**Solution**|Create a new solution or select an existing one. Setting this value will set the appropriate customization prefix for the **Unique Name** field.|Yes|
|**Unique Name**|The name of the Custom API. This value should contain only alphanumeric characters and no spaces.<br/>The full name includes the customization prefix determined by selecting the solution.|**No**|
|**Description**|A localizable description. For use when the message is exposed to be called in an app. For example, as a [ToolTip](https://wikipedia.org/wiki/Tooltip).|Yes|
|**Assembly**|Optional. Select an assembly that contains a plug-in type that will define what the Custom API does.|Yes|
|**Plugin**|Optional. Select a plug-in type within the selected assembly. You may set this later.|Yes|
|**Allowed Custom Processing Step Type**|Which types of processing steps you will allow. More Information: [Select a Custom Processing Step Type](customapi-table-columns.md#select-a-custom-processing-step-type)|**No**|
|**Binding Type**|What kind of entity binding. More Information: [Select a Binding Type](customapi-table-columns.md#select-a-binding-type)|**No**|
|**Bound Entity Logical Name**|If you select **Binding Type** **Entity** or **EntityCollection** you should enter the logical name of the table representing that type.|**No**|
|**Execute Privilege Name**|The name of a privilege that will control whether someone can use the API. This must be a valid [Name](reference/entities/privilege.md#BKMK_Name) value from the [Privilege](reference/entities/privilege.md) table. |Yes|
|**Function**|Whether to create a Function. More Information: [When to create a Function](customapi-table-columns.md#when-to-create-a-function)|**No**|
|**Private**|Whether the Custom API should be private. More Information: [When to make your Custom API private](customapi-table-columns.md#when-to-make-your-custom-api-private)|Yes|

> [!NOTE]
> - The PRT Custom API designer doesn't expose the **Enabled For Workflow** (WorkflowSdkStepEnabled) property. If you want to create a Custom API that will work for Workflows, you need to use a different method.
> - The PRT Custom API designer doesn't expose the **Is Customizable** managed property. You can set this in Power Apps. More information [Custom API Customization](custom-api.md#custom-api-customization)

You can continue to add **Request Parameters** and **Response Properties**, or save the Custom API and add them later.

## Create Request parameters

A Custom API isn't required to have any request parameters. While creating a Custom API or when editing an existing one, you can create new request parameters by clicking **+ Add Request Parameter**. This will open the **Parameter** form.

:::image type="content" source="media/custom-api-request-parameter-create-form.png" alt-text="Custom API Request Parameter Create form":::

Use the information in the table below to create the Request Parameter


|Label|Description|Can be changed|
|---------|---------|---------|
|**Display Name**|Localizable display name.|Yes|
|**Name**|The primary name of the custom API request parameter. This naming convention is recommended to differentiate this parameter from others that share a common **Unique Name**: `{Custom API Unique Name}.{Parameter UniqueName}`|Yes|
|**Unique Name**|This will be the name of the parameter when you call the Custom API.|**No**|
|**Type**|Select the type of the parameter. <br/>Boolean<br/>DateTime<br/>Decimal<br/>Entity<br/>EntityCollection<br/>EntityReference<br/>Float<br/>Integer<br/>Money<br/>Picklist<br/>String<br/>StringArray<br/>Guid<br/>|**No**|
|**Logical Entity Name**|When **Entity**, **EntityCollection**, or **EntityReference** is selected as the **Type**, you can specify the table.|**No**|
|**Description**|Localizable description.|Yes|
|**Is Optional**|Whether a value for the parameter is required by the caller.|**No**|

## Create Response properties

A Custom API for an action isn't required to have any response properties. While creating a Custom API or when editing an existing one, you can create new response properties by clicking **+ Add Response Parameter**. This will open the **Parameter** form.

:::image type="content" source="media/custom-api-response-property-create-form.png" alt-text="Custom API Response Property Create form":::

Use the information in the table below to create the Response Property.

|Label|Description|Can be changed|
|---------|---------|---------|
|**Display Name**|Localizable display name.|Yes|
|**Name**|The primary name of the custom API response property. This naming convention is recommended to differentiate this parameter from others that share a common Unique Name: `{Custom API Unique Name}.{Property UniqueName}`|Yes|
|**Unique Name**|This will be the name of the property returned when you call the Custom API.|**No**|
|**Type**|Select the type of the property. <br/>Boolean<br/>DateTime<br/>Decimal<br/>Entity<br/>EntityCollection<br/>EntityReference<br/>Float<br/>Integer<br/>Money<br/>Picklist<br/>String<br/>StringArray<br/>Guid<br/>|**No**|
|**Logical Entity Name**|When **Entity**, **EntityCollection**, or **EntityReference** is selected as the **Type**, you can specify the table.|**No**|
|**Description**|Localizable description.|Yes|

## View a list of Custom API

To view a list of Custom API, from the **View** menu select the **Display by Message** command.

:::image type="content" source="media/custom-api-display-by-message.png" alt-text="The Display by Message command will show Custom API":::

Any messages that were created as Custom API will be prefixed by **(Custom API)**.

## Delete Custom API

When viewing a list of Custom API, select the one you want to delete and click the **Unregister** command.

:::image type="content" source="media/prt-custom-api-delete.png" alt-text="Delete a Custom API":::

Or right-click the item and select **Unregister** from the context menu.

## Update Custom API Request Parameters or Response Properties

In the list of **Request parameters** or **Response properties**, select this column to edit:

:::image type="content" source="media/prt-custom-api-parameter-edit.png" alt-text="Column to edit parameter":::

## Delete Custom API Request Parameters or Response Properties

In the list of **Request parameters** or **Response properties**, select this column to delete:

:::image type="content" source="media/prt-custom-api-parameter-delete.png" alt-text="Column to delete parameter":::

### See also

[Create and use Custom APIs](custom-api.md)<br />
[Create a Custom API in Power Apps](create-custom-api-maker-portal.md)<br />
[Create a Custom API with code](create-custom-api-with-code.md)<br />
[Create a Custom API with solution files](create-custom-api-solution.md)<br />
[Create your own messages](custom-actions.md)<br />
[CustomAPI Table Columns](customapi-table-columns.md)<br />
[CustomAPIRequestParameter Table Columns](customapirequestparameter-table-columns.md)<br />
[CustomAPIRequestParameter Table Columns](customapirequestparameter-table-columns.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]