---
title: "Create a custom API using the plug-in registration tool (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Create a custom API using the plug-in registration tool" # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 09/27/2022
ms.reviewer: jdaly
ms.topic: article
author: marcelbf # GitHub ID
ms.subservice: dataverse-developer
ms.author: marcelbf # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
contributors:
 - JimDaly
---
# Create a custom API using the plug-in registration tool

The plug-in registration tool (PRT) includes a designer to create custom API. The PRT is a Windows client application that is part of the developer tools you can download from NuGet.  See [Dataverse development tools](download-tools-nuget.md) for information about downloading these tools.

[!INCLUDE [cc-connect-plugin-registration-tool](includes/cc-connect-plugin-registration-tool.md)]

## Create a custom API

In the **Register** menu, select the **Register new Custom API** command. This will open the form to create a custom API.

:::image type="content" source="media/create-custom-api-prt.png" alt-text="PRT custom API form":::

Use the information in the table below to create the Custom API. For more details, see [Custom API table columns](custom-api-tables.md#custom-api-table-columns)

> [!IMPORTANT]
> Some options cannot be changed after you save the custom API. Make sure you understand the purpose of each setting that cannot be changed. If you later need to change this setting, you must delete and re-create the custom API. This will also delete any request parameters or response properties that are associated with it.


|Label|Description|Can be changed|
|---------|---------|---------|
|**Display Name**|A localizable name. |Yes|
|**Name**|A friendly, non-localizable name.|Yes|
|**Solution**|Create a new solution or select an existing one. Setting this value will set the appropriate customization prefix for the **Unique Name** field.|Yes|
|**Unique Name**|The name of the custom API. This value should contain only alphanumeric characters and no spaces.<br/>The full name includes the customization prefix determined by selecting the solution.|**No**|
|**Description**|A localizable description. For use when the message is exposed to be called in an app. For example, as a [ToolTip](https://wikipedia.org/wiki/Tooltip).|Yes|
|**Assembly**|Optional. Select an assembly that contains a plug-in type that will define what the custom API does.|Yes|
|**Plugin**|Optional. Select a plug-in type within the selected assembly. You may set this later.|Yes|
|**Allowed Custom Processing Step Type**|Which types of processing steps you will allow. More Information: [Select a Custom Processing Step Type](custom-api.md#select-a-custom-processing-step-type)|**No**|
|**Binding Type**|What kind of entity binding. More Information: [Select a Binding Type](custom-api.md#select-a-binding-type)|**No**|
|**Bound Entity Logical Name**|If you select **Binding Type** **Entity** or **EntityCollection** you should enter the logical name of the table representing that type.|**No**|
|**Execute Privilege Name**|The name of a privilege that will control whether someone can use the API. This must be a valid [Name](reference/entities/privilege.md#BKMK_Name) value from the [Privilege](reference/entities/privilege.md) table. More information: [Secure your custom API with a privilege](custom-api.md#secure-your-custom-api-with-a-privilege) |Yes|
|**Function**|Whether to create a Function. More Information: [When to create a Function](custom-api.md#when-to-create-a-function)|**No**|
|**Private**|Whether the custom API should be private. More Information: [When to make your custom API private](custom-api.md#when-to-make-your-custom-api-private)|Yes|

> [!NOTE]
> - The PRT custom API designer doesn't expose the **Enabled For Workflow** (`WorkflowSdkStepEnabled`) property. If you want to create a custom API that will work for Workflows, you need to use a different method.
> - The PRT custom API designer doesn't expose the **Is Customizable** managed property. You can set this in Power Apps. More information [Custom API Customization](custom-api.md#custom-api-customization)

You can continue to add **Request Parameters** and **Response Properties**, or save the custom API and add them later.

## Create Request parameters

A custom API isn't required to have any request parameters. While creating a custom API or when editing an existing one, you can create new request parameters by clicking **+ Add Request Parameter**. This will open the **Parameter** form.

:::image type="content" source="media/custom-api-request-parameter-create-form.png" alt-text="Custom API Request Parameter Create form":::

Use the information in the table below to create the Request Parameter. For more details see [CustomAPIRequestParameter Table Columns](custom-api-tables.md#customapirequestparameter-table-columns)


|Label|Description|Can be changed|
|---------|---------|---------|
|**Display Name**|Localizable display name.|Yes|
|**Name**|The primary name of the custom API request parameter. This naming convention is recommended to differentiate this parameter from others that share a common **Unique Name**: `{Custom API Unique Name}.{Parameter UniqueName}`|Yes|
|**Unique Name**|This will be the name of the parameter when you call the custom API.|**No**|
|**Type**|Select the type of the parameter. <br/>Boolean<br/>DateTime<br/>Decimal<br/>Entity<br/>EntityCollection<br/>EntityReference<br/>Float<br/>Integer<br/>Money<br/>Picklist<br/>String<br/>StringArray<br/>Guid<br/>|**No**|
|**Logical Entity Name**|When **Entity**, **EntityCollection**, or **EntityReference** is selected as the **Type**, you can specify the table.|**No**|
|**Description**|Localizable description.|Yes|
|**Is Optional**|Whether a value for the parameter is required by the caller.|**No**|

## Create Response properties

A custom API for an action isn't required to have any response properties. While creating a custom API or when editing an existing one, you can create new response properties by clicking **+ Add Response Parameter**. This will open the **Parameter** form.

:::image type="content" source="media/custom-api-response-property-create-form.png" alt-text="Custom API Response Property Create form":::

Use the information in the table below to create the Response Property. For more details see [CustomAPIResponseProperty Table Columns](custom-api-tables.md#customapiresponseproperty-table-columns)

|Label|Description|Can be changed|
|---------|---------|---------|
|**Display Name**|Localizable display name.|Yes|
|**Name**|The primary name of the custom API response property. This naming convention is recommended to differentiate this parameter from others that share a common Unique Name: `{Custom API Unique Name}.{Property UniqueName}`|Yes|
|**Unique Name**|This will be the name of the property returned when you call the custom API.|**No**|
|**Type**|Select the type of the property. <br/>Boolean<br/>DateTime<br/>Decimal<br/>Entity<br/>EntityCollection<br/>EntityReference<br/>Float<br/>Integer<br/>Money<br/>Picklist<br/>String<br/>StringArray<br/>Guid<br/>|**No**|
|**Logical Entity Name**|When **Entity** or **EntityReference** are selected as the **Type**, you can specify the table. You cannot specify a **Logical Entity Name** when you choose **EntityCollection** as the **Type**.|**No**|
|**Description**|Localizable description.|Yes|

## View a list of custom API

To view a list of custom API, from the **View** menu select the **Display by Message** command.

:::image type="content" source="media/custom-api-display-by-message.png" alt-text="The Display by Message command will show custom API":::

Any messages that were created as custom API will be prefixed by **(Custom API)**.

## Delete custom API

When viewing a list of custom API, select the one you want to delete and click the **Unregister** command.

:::image type="content" source="media/prt-custom-api-delete.png" alt-text="Delete a custom API":::

Or right-click the item and select **Unregister** from the context menu.

## Update custom API Request Parameters or Response Properties

In the list of **Request parameters** or **Response properties**, select this column to edit:

:::image type="content" source="media/prt-custom-api-parameter-edit.png" alt-text="Column to edit parameter":::

## Delete custom API Request Parameters or Response Properties

In the list of **Request parameters** or **Response properties**, select this column to delete:

:::image type="content" source="media/prt-custom-api-parameter-delete.png" alt-text="Column to delete parameter":::

## Next steps

If you haven't set the `IsPrivate` property for your custom API, after you have created your custom API you can retrieve the service definition from the [CSDL $metadata document](webapi/web-api-service-documents.md#csdl-metadata-document) using a `GET` request, even from your browser. If the url for your environment is `https://yourorg.crm.dynamics.com`, you can type this URL in your browser address field to retrieve the $metadata: `https://yourorg.crm.dynamics.com/api/data/v9.1/$metadata`.

Search the result to find the name of the custom API and you will find the Action or Function created together with any related ComplexType to represent the return value. For example:

```xml
<ComplexType Name="sample_CustomAPIExampleResponse">
    <Property Name="StringProperty"
        Type="Edm.String"
        Unicode="false"/>
</ComplexType>
<Action Name="sample_CustomAPIExample">
    <Parameter Name="StringParameter"
        Type="Edm.String"
        Nullable="false"
        Unicode="false"/>
    <ReturnType Type="mscrm.sample_CustomAPIExampleResponse"
        Nullable="false"/>
</Action>
```

Even if you haven't set a **Plugin** for your custom API, you can test it to verify the signature. Any response properties will return their default values because there is no plug-in to set the values. More information: [Invoking custom APIs](custom-api.md#invoking-custom-apis)

If you will add a plug-in, you must write it and register the assembly. Then update your custom API to set the **Assembly** and **Plugin** to specify what code to run in response to your custom API. More information: [Write a Plug-in for your custom API](custom-api.md#write-a-plug-in-for-your-custom-api)

### See also

[Create and use custom APIs](custom-api.md)<br />
[Create a custom API in Power Apps](create-custom-api-maker-portal.md)<br />
[Create a custom API with code](create-custom-api-with-code.md)<br />
[Create a custom API with solution files](create-custom-api-solution.md)<br />
[Create your own messages](custom-actions.md)<br />
[Custom API table columns](custom-api-tables.md)<br />

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
