---
title: "Create a Custom API in the maker portal (Common Data Service) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Create a Custom API definition with the maker portal" # 115-145 characters including spaces. This abstract displays in the search result.
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
# Create a Custom API in the maker portal

In the future we intend that the designer for Custom Actions will provide a single experience that will include both Workflow Custom Actions and Custom APIs. For now, the only way to create Custom APIs with a user interface is to use the steps described here.


> [!IMPORTANT]
> Many fields related to creating Custom API cannot be changed after you create them. You should carefully plan the design of the Custom API before you start. If you later decide that you need to change things after you create the Custom API, you may need to delete the existing entity data and re-create the Custom API.
>
> Please review the following to understand which field values cannot be changed:
> - [CustomAPI entity attributes](custom-api.md#customapi-entity-attributes)
> - [CustomAPIRequestParameter entity attributes](custom-api.md#customapirequestparameter-entity-attributes)
> - [CustomAPIResponseProperty entity attributes](custom-api.md#customapiresponseproperty-entity-attributes)

When creating a Custom API it is expected that you will use a solution. Your solution must be associated with a publisher. The publisher will have a specific customization prefix associated with it. You must use a customization prefix when creating a Custom API and this prefix should be the same used by the publisher of your solution. The instructions below will use the value `sample` as the customization prefix because it is the one set for the following publisher:

:::image type="content" source="media/solution-publisher-with-sample-prefix.png" alt-text="Solution publisher with sample prefix":::

## Create a Custom API record

1. In your solution, click **New** and select **Custom API** from the drop-down.
1. Edit the fields to set the properties of your Custom API. You must set values for the following fields. For more information see [CustomAPI entity attributes](custom-api.md#customapi-entity-attributes)
    |Field  |Description  |
    |---------|---------|
    |**Unique Name**|Unique name for the custom API. This will be the name of the message created. This value must include a customization prefix. It should match the prefix set for your solution publisher.|
    |**Name**|The primary name of the custom API. This will display in the list of custom apis when viewed in the solution.|
    |**Display Name**|Localized display name for this Custom API. For use when the message is exposed to be called in an app.|
    |**Description**|Localized description for this Custom API. For use when the message is exposed to be called in an app. For example, as a [ToolTip](https://wikipedia.org/wiki/Tooltip).|
    |**Bound Entity Logical Name**|The logical name of the entity bound to the custom API if it is not Global. If **Binding Type**is Global, this can remain empty|
    |**Binding Type**|The binding type of the custom API. Options are: **Global**, **Entity**, **EntityCollection**.|
    |**Is Function**|Indicates if the custom API is a function. A function requires the HTTP GET method. Otherwise the Http POST method is required.|
    |**Allowed Custom Processing Step Type**|The type of custom processing steps allowed for this Custom API. This allows you to control whether other plug-ins can be registered. Options are **None**, **Async Only**, **Sync and Async**.|

    You cannot set values for **Plug-in Type** unless you have already created the plug-in. You can change this later.
1. Click **Save**. Your form should look something like this:
    :::image type="content" source="media/saved-customapi-form.png" alt-text="Saved Custom API form":::


> [!NOTE]
> If you delete the Custom API record, all request parameters and response properties will be deleted with it. Make sure that the Custom API field values are correct before proceeding. Otherwise you may need to repeat these steps to re-create your Custom API if you need to delete it.

### Known issue: Add your Custom API to your solution

After you create your Custom API, it will not appear in your solution. In your solution you must select **Add existing** and then select **Custom API** from the drop-down.

Then add your Custom API to your solution.

:::image type="content" source="media/add-existing-customapi.png" alt-text="Select your custom api and add it to the existing solution.":::

## Create any Request Parameters

A Custom API doesn't require parameters. Create as many parameters as you need to pass data needed for your logic.

If the Custom API is bound to an **Entity** or **EntityCollection**, that parameter will be created automatically. You do not need to create request parameters for bound parameters.

1. In your solution, click **New** and select **Custom API Request Parameter** from the drop-down.
1. Edit the fields to set the properties of your Custom API Request Parameter. You must set values for the following fields. For more information see [CustomAPIRequestParameter entity attributes](custom-api.md#customapirequestparameter-entity-attributes)
    |Field  |Description  |
    |---------|---------|
    |**Custom API**|Set the lookup to the Custom API that this parameter is for.|
    |**Unique Name**|Unique name for the request parameter. This value does not require a customization prefix. It only needs to be unique within the set of request parameters for this Custom API.|
    |**Name**|The primary name of the request parameter.  This will display in the list of custom api request parameters when viewed in the solution. Use this to differentiate this parameter from others that share a common Unique Name. This naming convention is recommended: `{Custom API Unique Name}.{Parameter UniqueName}`|
    |**Display Name**|Localized display name for this request parameter. For use when the message is exposed to be called in an app.|
    |**Description**|Localized description for this request parameter. For use when the message is exposed to be called in an app. For example, as a [ToolTip](https://wikipedia.org/wiki/Tooltip).|
    |**Type**|The data type of the request parameter. There are 11 different types to choose from. These are the same types available for Workflow Custom Actions today.|
    |**Entity Logical Name**|If the Type field is an Entity, an EntityCollection, or EntityReference, this represents the type of entity.|
    |**Is Optional**|Indicates if the request parameter is optional. If it is not optional, it is required to pass a value for this parameter when using the message.|
1. Click **Save**. Your form should look something like this:

:::image type="content" source="media/customapi-request-parameter-form.png" alt-text="Example of a Custom API Request Parameter Form":::

> [!NOTE]
> As noted earlier in [Known issue: Add your Custom API to your solution](#known-issue-add-your-custom-api-to-your-solution) you will have to manually add this request parameter record to your solution.

## Create any Response Properties

A Custom API doesn't require response properties. If the operation succeeds, it will return a success response. If it fails, it will return an error. You should define response properties for any data that your API will return.

If there is only a single **Entity** or **EntityCollection** response property defined, the response will be of that type. If there are multiple parameters, or one or more parameter of a simple type, the API will return a complex type where each response property will be a property of that complex type. For example, if your Custom API Unique name is `sample_CustomAPIExample`, it will return a complex type named `sample_CustomAPIExampleResponse` with properties for each response property you define.

1. In your solution, click **New** and select **Custom API Response Property** from the drop-down.
1. Edit the fields to set the properties of your Custom API Response Property. You must set values for the following fields. For more information see [CustomAPIResponseProperty entity attributes](custom-api.md#customapiresponseproperty-entity-attributes)
    |Field  |Description  |
    |---------|---------|
    |**Custom API**|Set the lookup to the Custom API that this property is for.|
    |**Unique Name**|Unique name for the response property. This value does not require a customization prefix. It only needs to be unique within the set of response properties for this Custom API.|
    |**Name**|The primary name of the custom API response property.  This will display in the list of custom api response properties when viewed in the solution. Use this to differentiate this property from others that share a common Unique Name. This naming convention is recommended: `{Custom API Unique Name}.{Property UniqueName}`|
    |**Display Name**|Localized display name for this response property. For use when the message is exposed to be called in an app.|
    |**Description**|Localized description for this response property. For use when the message is exposed to be called in an app. For example, as a [ToolTip](https://wikipedia.org/wiki/Tooltip).|
    |**Type**|The data type of the custom API response property. There are 11 different types to choose from. These are the same types available for Workflow Custom Actions today.|
    |**Entity Logical Name**|If the **Type** field is an **Entity**, an **EntityCollection**, or **EntityReference**, this represents the type of entity.|

1. Click **Save**. Your form should look something like this:

:::image type="content" source="media/customapi-response-property-form.png" alt-text="Custom API Response Property Form":::

> [!NOTE]
> As noted earlier in [Known issue: Add your Custom API to your solution](#known-issue-add-your-custom-api-to-your-solution) you will have to manually add this response property record to your solution.

## Observe the result in the service document

If you haven't set the `IsPrivate` property for your Custom API, you can now retrieve the service definition from the [CSDL $metadata document](webapi/web-api-types-operations.md#csdl-metadata-document) using a GET request, even from your browser. If the url for your environment is `https://yourorg.crm.dynamics.com`, you can type this URL in your browser address field to retrieve the $metadata: `https://yourorg.crm.dynamics.com/api/data/v9.1/$metadata`.

Search the result to find the name of the Custom API. For example, the API defined using the steps above looks like this:

```xml
<ComplexType Name="sample_CustomAPIExampleResponse">
    <Property Name="StringProperty" Type="Edm.String" Unicode="false" />
</ComplexType>
<Action Name="sample_CustomAPIExample">
    <Parameter Name="StringParameter" Type="Edm.String" Nullable="false" Unicode="false" />
    <ReturnType Type="mscrm.sample_CustomAPIExampleResponse" Nullable="false" />
</Action>
```

If you have set the `IsPrivate` property for your Custom API, you won't find it. But you can set the `IsPrivate` value back to `false` and retrieve the `$metadata`again. The API will work exactly the same whether it is private or not. You can always set it back to `true` before you ship your solution if you don't want to support others using your Custom API.


## Test your Custom API

Now that you have created your Custom API you can try it. Even if you haven't set a plug-in type to define the main operation, you can test it now to verify that you can call it correctly. Any response properties will return their default value, such as null.

You can test your API using PostMan. Use the steps described in [Set up a Postman environment](webapi/setup-postman-environment.md) to set up a PostMan environment that will generate the access token you will need. Then, apply the steps described in [Use Web API actions](webapi/use-web-api-actions.md) if your API is an action. If it is a function, use the steps in [Use Web API functions](webapi/use-web-api-functions.md).

The simple example included in this topic can be called as an action using the following:

**Request**

```http
POST https://yourorg.crm.dynamics.com/api/data/v9.1/sample_CustomAPIExample HTTP/1.1
Accept: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Authorization: Bearer [Redacted]

{
    
"StringParameter":"A Test String Parameter Value"

}
```

**Response**

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
REQ_ID: 8b0512c5-aa68-4815-9b3e-27072b6a8fec
OData-Version: 4.0

{
    "@odata.context":"https://yourorg.crm.dynamics.com/api/data/v9.1/$metadata#Microsoft.Dynamics.CRM.sample_CustomAPIExampleResponse",
    "StringProperty":null
}
```



## Next steps
