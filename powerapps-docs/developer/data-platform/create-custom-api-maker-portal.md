---
title: "Create a Custom API in the maker portal (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Create a Custom API definition with the maker portal" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/13/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Create a Custom API in the maker portal

The current experience creating Custom API within the maker portal is temporary. We intend to provide a modern experience in the future.


> [!IMPORTANT]
> Many fields related to creating Custom API cannot be changed after you create them. You should carefully plan the design of the Custom API before you start. If you later decide that you need to change things after you create the Custom API, you may need to delete the existing record and re-create the Custom API.
>
> Please review the following to understand which field values cannot be changed:
> - [CustomAPI Table Columns](customapi-table-columns.md)
> - [CustomAPIRequestParameter Table Columns](customapirequestparameter-table-columns.md)
> - [CustomAPIResponseProperty Table Columns](customapiresponseproperty-table-columns.md)

When creating a Custom API it is expected that you will use a solution. Your solution must be associated with a publisher. The publisher will have a specific customization prefix associated with it. You must use a customization prefix when creating a Custom API and this prefix should be the same used by the publisher of your solution. The instructions below will use the value `sample` as the customization prefix because it is the one set for the following publisher:

:::image type="content" source="media/solution-publisher-with-sample-prefix.png" alt-text="Solution publisher with sample prefix.":::

> [!NOTE]
> This topic assumes you are familar with solutions. If you are not, see [Create a solution](../../maker/data-platform/create-solution.md)

## Create a Custom API record

1. In your solution, click **New** and select **Custom API** from the drop-down.
1. Edit the fields to set the properties of your Custom API. You must set values for the following fields. For more information see [CustomAPI Table Columns](customapi-table-columns.md)
    
    You cannot set values for **Plug-in Type** unless you have already created the plug-in. You can change this later.

1. Click **Save**. Your form should look something like this:
    :::image type="content" source="media/saved-customapi-form.png" alt-text="Saved Custom API form.":::

> [!NOTE]
> If you delete the Custom API record, all request parameters and response properties will be deleted with it. Make sure that the Custom API field values are correct before proceeding. Otherwise you may need to repeat all of these steps to re-create your Custom API if you need to delete it.
>
> We recommend that you set the **IsCustomizable** managed property to false for all Custom API components. This property is not available in the form. For more information see [Managed properties](/power-platform/alm/managed-properties-alm)

### Known issue: Add your Custom API to your solution

Known issue: [A custom API created is not added to the current solution in the maker portal](custom-api.md#a-custom-api-created-is-not-added-to-the-current-solution-in-the-maker-portal)
After you create your Custom API, it will not appear in your solution. In your solution you must select **Add existing** and then select **Custom API** from the drop-down.

Then add your Custom API to your solution.

:::image type="content" source="media/add-existing-customapi.png" alt-text="Select your custom api and add it to the existing solution.":::

## Create any Request Parameters

A Custom API doesn't require parameters. Create as many parameters as you need to pass data needed for your logic.

> [!NOTE]
> If you define a bound entity for your Custom API action, the parameter will be generated for you. You don’t need to create an input parameter for the entity when the Custom API is bound to an entity.
> 
> If you bind your Custom API action to an entity collection, there will not be a parameter generated for you. Binding a Custom API action to an entity collection requires that the Custom API be called using the entityset resource path. 
>
> Binding to an entity collection only sets the expectation that the operation will be performed on more than one entity of that type or that it will return a collection of that type. It does not provide an entity collection input parameter for your plug-in to process.

1. In your solution, click **New** and select **Custom API Request Parameter** from the drop-down.
1. Edit the fields to set the properties of your Custom API Request Parameter. For more information see [CustomAPIRequestParameter Table Columns](customapirequestparameter-table-columns.md)

1. Click **Save**. Your form should look something like this:

    :::image type="content" source="media/customapi-request-parameter-form.png" alt-text="Example of a Custom API Request Parameter Form.":::

> [!NOTE]
> As noted earlier in [Known issue: Add your Custom API to your solution](#known-issue-add-your-custom-api-to-your-solution) you will have to manually add this request parameter record to your solution.
>
> As noted earlier, we recommend that you set the **IsCustomizable** managed property to false for all Custom API components. This property is not available in the form. For more information see [Managed properties](/power-platform/alm/managed-properties-alm)

## Create any Response Properties

A Custom API that represents an action doesn't require response properties. If the operation succeeds, it will return a success response. If it fails, it will return an error. You should define response properties for any data that your API will return.

> [!IMPORTANT]
> A Custom API that represents a function requires at least one response property to be valid.

If there is only a single **Entity** or **EntityCollection** response property defined, the response will be of that type. If there are multiple parameters, or one or more parameter of a simple type, the API will return a complex type where each response property will be a property of that complex type. 

For example, if your Custom API Unique name is `sample_CustomAPIExample`, it will return a complex type named `sample_CustomAPIExampleResponse` with properties for each response property you define.

1. In your solution, click **New** and select **Custom API Response Property** from the drop-down.
1. Edit the fields to set the properties of your Custom API Response Property. For more information see [CustomAPIResponseProperty Table Columns](customapiresponseproperty-table-columns.md)

1. Click **Save**. Your form should look something like this:

    :::image type="content" source="media/customapi-response-property-form.png" alt-text="Custom API Response Property Form.":::

> [!NOTE]
> As noted earlier in [Known issue: Add your Custom API to your solution](#known-issue-add-your-custom-api-to-your-solution) you will have to manually add this response property record to your solution.
>
> As noted earlier, we recommend that you set the **IsCustomizable** managed property to false for all Custom API components. This property is not available in the form. For more information see [Managed properties](/power-platform/alm/managed-properties-alm)

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

If you have set the `IsPrivate` property for your Custom API, you won't find your custom API in the results. But you can set the `IsPrivate` value back to `false` and retrieve the `$metadata` again. The API will work exactly the same whether it is returned by the $metadata or not. You can always set it back to `true` before you ship your solution if you don't want to support others using your Custom API.


## Test your Custom API

Now that you have created your Custom API you can try it. Even if you haven't set a plug-in type to define the main operation, you can test it now to verify that you can call it correctly. Any response properties will return their default value, such as null. More information: [Invoking Custom APIs](custom-api.md#invoking-custom-apis).


## Update the Custom API Type

For information about how to write a plug-in for a custom api, see [Write a Plug-in for your Custom API](custom-api.md#write-a-plug-in-for-your-custom-api).

After you have registered your assembly, you need to set the **Type** value for the Custom API you created. This is a lookup property, so you just need to find the Plug-in Type that represents the type created when you registered the assembly.

:::image type="content" source="media/set-custom-api-type.png" alt-text="Set the Custom API Type Lookup.":::

Once you have set the **Type**, you can test your Custom API to verify the correct results are returned.

## Other ways to create Custom APIs

You may have requirements to create a client application which will allow creation of Custom APIs outside of the designer. Because the data for Custom APIs is stored in tables, you can create them using code. More information: [Create a Custom API with code](create-custom-api-with-code.md).

Your ALM process may be better served by creating Custom APIs by editing solution files. More information: [Create a Custom API with solution files](create-custom-api-solution.md).

### See also

[Create and use Custom APIs](custom-api.md)<br />
[Create a Custom API with code](create-custom-api-with-code.md)<br />
[Create a Custom API with solution files](create-custom-api-solution.md)<br />
[Create your own messages](custom-actions.md)<br />


[!INCLUDE[footer-include](../../includes/footer-banner.md)]