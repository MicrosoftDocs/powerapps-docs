---
title: "Create a Custom API in Power Apps (Microsoft Dataverse)"
description: "Learn how to create a custom API in Power Apps for Microsoft Dataverse, define request and response properties, and test the API. Follow the steps to get started."
ms.date: 08/04/2026
ms.reviewer: jdaly
ms.topic: how-to
author: MsSQLGirl
ms.subservice: dataverse-developer
ms.author: jukoesma
search.audienceType: 
  - developer
---
# Create a custom API in Power Apps

This article explains how to create a custom API in Power Apps for Microsoft Dataverse by using a solution. Follow these steps to define request and response properties, test the custom API, and associate its plug-in type. If you're not familiar with solutions, first read [Create a solution](../../maker/data-platform/create-solution.md).

Your solution must be associated with a publisher. The publisher has a specific customization prefix associated with it. You must use a customization prefix when creating a custom API, and this prefix should be the same prefix used by the publisher of your solution. The following instructions use the value `sample` as the customization prefix because it's the one set for the publisher.

> [!IMPORTANT]
> - There's now a better experience for creating custom API. You can use a designer within the Plug-in registration tool. For more information, see [Create a custom API using the plug-in registration tool](create-custom-api-prt.md).
> - You can't change many fields related to creating custom API after you create them. Carefully plan the design of the custom API before you start. If you later decide that you need to change these fields, you might need to delete the existing record and re-create the custom API. For more information, see [CustomAPI tables](custom-api-tables.md).

## Create a custom API record

1. In your solution, select **New** > **More** > **Other** > **custom API** from the drop-down.
1. Edit the fields to set the properties of your custom API. Set values for the following fields. For more information, see [Custom API table columns](custom-api-tables.md#custom-api-table-columns).
    
    You can't set values for **Plug-in Type** before you create the plug-in. You can change this value later.

1. Select **Save**. Your form should look similar to the following image:
    :::image type="content" source="media/saved-customapi-form.png" alt-text="Screenshot of the saved custom API form with its configured properties.":::


## Create request parameters

A custom API doesn't require parameters. Create as many parameters as you need to pass data needed for your logic.

1. In your solution, select **New** > **More** > **Other** > **Custom API Request Parameter** from the drop-down.
1. Edit the fields to set the properties of your custom API request parameter. For more information, see [CustomAPIRequestParameter Table Columns](custom-api-tables.md#customapirequestparameter-table-columns).

1. Select **Save**. Your form should look similar to the following image:

    :::image type="content" source="media/customapi-request-parameter-form.png" alt-text="Screenshot of an example custom API request parameter form.":::


## Create response properties

A custom API that represents an Action doesn't require response properties. A Function must have at least one. If the operation succeeds, it returns a success response. If it fails, it returns an error. Define response properties for any data that your API returns.

If you define only a single **Entity** or **EntityCollection** response property, the response is of that type. If you define multiple properties, or one or more properties of a simple type, the API returns a complex type where each response property is a property of that complex type.

For example, if your custom API unique name is `sample_CustomAPIExample`, it returns a complex type named `sample_CustomAPIExampleResponse` with properties for each response property you define.

1. In your solution, select **New** > **More** > **Other** > **Custom API Response Property** from the drop-down.
1. Edit the fields to set the properties of your custom API response property. For more information, see [CustomAPIResponseProperty Table Columns](customapiresponseproperty-table-columns.md).

1. Select **Save**. Your form should look similar to the following image:

    :::image type="content" source="media/customapi-response-property-form.png" alt-text="Screenshot of an example custom API response property form.":::

## Observe the result in the service document

If you don't set the `IsPrivate` property for your custom API, you can retrieve the service definition from the [CSDL $metadata document](webapi/web-api-service-documents.md#csdl-metadata-document) by using a `GET` request, even from your browser. If the URL for your environment is `https://yourorg.crm.dynamics.com`, you can type this URL in your browser address field to retrieve the $metadata: `https://yourorg.crm.dynamics.com/api/data/v9.1/$metadata`.

Search the result to find the name of the custom API. For example, the API defined by using the preceding steps looks like this:

```xml
<ComplexType Name="sample_CustomAPIExampleResponse">
    <Property Name="StringProperty" Type="Edm.String" Unicode="false" />
</ComplexType>
<Action Name="sample_CustomAPIExample">
    <Parameter Name="StringParameter" Type="Edm.String" Nullable="false" Unicode="false" />
    <ReturnType Type="mscrm.sample_CustomAPIExampleResponse" Nullable="false" />
</Action>
```


## Test your custom API

After you create your custom API, you can try it. Even if you don't set a plug-in type to define the main operation, you can test it now to verify that you can call it correctly. Any response properties return their default value, such as null. For more information, see [Invoking custom APIs](custom-api.md#invoking-custom-apis).


## Update the custom API plug-in type

For information about how to write a plug-in for a custom api, see [Write a Plug-in for your custom API](custom-api.md#write-a-plug-in-for-your-custom-api).

After you register your assembly, you need to set the **Plugin Type** value for the custom API you created. This value is a lookup property, so you just need to find the Plug-in Type that represents the type created when you registered the assembly.

:::image type="content" source="media/set-custom-api-type.png" alt-text="Screenshot of the lookup used to set the custom API plug-in type.":::

After you set the **Plugin Type**, you can test your custom API to verify the correct results are returned.

## Other ways to create custom APIs

The plugin registration tool provides a custom API designer. For more information, see [Create a custom API using the plug-in registration tool](create-custom-api-prt.md).

You might have requirements to create a client application that allows creation of custom APIs outside of the designer. Because the data for custom APIs is stored in tables, you can create them by using code. For more information, see [Create a custom API with code](create-custom-api-with-code.md).

Your ALM process might be better served by creating custom APIs by editing solution files. For more information, see [Create a custom API with solution files](create-custom-api-solution.md).

### See also

[Create and use custom APIs](custom-api.md)<br />
[Create a custom API using the plug-in registration tool](create-custom-api-prt.md)<br />
[Create a custom API with code](create-custom-api-with-code.md)<br />
[Create a custom API with solution files](create-custom-api-solution.md)<br />
[Create your own messages](custom-actions.md)<br />


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
