---
title: "Create a Custom API in Power Apps (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Create a Custom API definition using Power Apps (make.powerapps.com)"
ms.custom: ""
ms.date: 04/19/2022
ms.reviewer: "jdaly"
ms.topic: "article"
author: "divkamath" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Create a Custom API in Power Apps

When creating a Custom API, you must use a solution. If you are not familiar with solutions, first read [Create a solution](../../maker/data-platform/create-solution.md).

Your solution must be associated with a publisher. The publisher will have a specific customization prefix associated with it. You must use a customization prefix when creating a Custom API and this prefix should be the same used by the publisher of your solution. The instructions below will use the value `sample` as the customization prefix because it is the one set for the publisher.

> [!IMPORTANT]
> - There is now a better experience for creating Custom API. You can use a designer within the Plug-in registration tool. More information: [Create a Custom API using the plug-in registration tool](create-custom-api-prt.md)
> - Many fields related to creating Custom API cannot be changed after you create them. You should carefully plan the design of the Custom API before you start. If you later decide that you need to change things after you create the Custom API, you may need to delete the existing record and re-create the Custom API. Review the information about the columns that cannot be changed here: [CustomAPI tables](custom-api-tables.md)

## Create a Custom API record

1. In your solution, click **New** > **More** > **Other** > **Custom API** from the drop-down.
1. Edit the fields to set the properties of your Custom API. You must set values for the following fields. For more information see  [Custom API table columns](custom-api-tables.md#custom-api-table-columns)
    
    You cannot set values for **Plug-in Type** unless you have already created the plug-in. You can change this later.

1. Click **Save**. Your form should look something like this:
    :::image type="content" source="media/saved-customapi-form.png" alt-text="Saved Custom API form.":::


## Create any Request Parameters

A Custom API doesn't require parameters. Create as many parameters as you need to pass data needed for your logic.

1. In your solution, click **New** > **More** > **Other** > **Custom API Request Parameter** from the drop-down.
1. Edit the fields to set the properties of your Custom API Request Parameter. For more information see [CustomAPIRequestParameter Table Columns](custom-api-tables.md#customapirequestparameter-table-columns)

1. Click **Save**. Your form should look something like this:

    :::image type="content" source="media/customapi-request-parameter-form.png" alt-text="Example of a Custom API Request Parameter Form.":::


## Create any Response Properties

A Custom API that represents an Action doesn't require response properties. A Function must have at least one.  If the operation succeeds, it will return a success response. If it fails, it will return an error. You should define response properties for any data that your API will return.

If there is only a single **Entity** or **EntityCollection** response property defined, the response will be of that type. If there are multiple properties, or one or more property of a simple type, the API will return a complex type where each response property will be a property of that complex type.

For example, if your Custom API Unique name is `sample_CustomAPIExample`, it will return a complex type named `sample_CustomAPIExampleResponse` with properties for each response property you define.

1. In your solution, click **New** > **More** > **Other** > **Custom API Response Property** from the drop-down.
1. Edit the fields to set the properties of your Custom API Response Property. For more information see [CustomAPIResponseProperty Table Columns](customapiresponseproperty-table-columns.md)

1. Click **Save**. Your form should look something like this:

    :::image type="content" source="media/customapi-response-property-form.png" alt-text="Custom API Response Property Form.":::

## Observe the result in the service document

If you haven't set the `IsPrivate` property for your Custom API, you can now retrieve the service definition from the [CSDL $metadata document](webapi/web-api-service-documents.md#csdl-metadata-document) using a `GET` request, even from your browser. If the url for your environment is `https://yourorg.crm.dynamics.com`, you can type this URL in your browser address field to retrieve the $metadata: `https://yourorg.crm.dynamics.com/api/data/v9.1/$metadata`.

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


## Test your Custom API

Now that you have created your Custom API you can try it. Even if you haven't set a plug-in type to define the main operation, you can test it now to verify that you can call it correctly. Any response properties will return their default value, such as null. More information: [Invoking Custom APIs](custom-api.md#invoking-custom-apis).


## Update the Custom API Plugin Type

For information about how to write a plug-in for a custom api, see [Write a Plug-in for your Custom API](custom-api.md#write-a-plug-in-for-your-custom-api).

After you have registered your assembly, you need to set the **Plugin Type** value for the Custom API you created. This is a lookup property, so you just need to find the Plug-in Type that represents the type created when you registered the assembly.

:::image type="content" source="media/set-custom-api-type.png" alt-text="Set the Custom API Plugin Type Lookup.":::

Once you have set the **Plugin Type**, you can test your Custom API to verify the correct results are returned.

## Other ways to create Custom APIs

The plugin registration tool provides a Custom API designer. More information: [Create a Custom API using the plug-in registration tool](create-custom-api-prt.md)

You may have requirements to create a client application which will allow creation of Custom APIs outside of the designer. Because the data for Custom APIs is stored in tables, you can create them using code. More information: [Create a Custom API with code](create-custom-api-with-code.md).

Your ALM process may be better served by creating Custom APIs by editing solution files. More information: [Create a Custom API with solution files](create-custom-api-solution.md).

### See also

[Create and use Custom APIs](custom-api.md)<br />
[Create a Custom API using the plug-in registration tool](create-custom-api-prt.md)<br />
[Create a Custom API with code](create-custom-api-with-code.md)<br />
[Create a Custom API with solution files](create-custom-api-solution.md)<br />
[Create your own messages](custom-actions.md)<br />


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
