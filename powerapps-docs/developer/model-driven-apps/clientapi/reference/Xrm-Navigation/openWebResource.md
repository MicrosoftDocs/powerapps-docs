---
title: "openWebResource (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the openWebResource method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# openWebResource (Client API reference)



[!INCLUDE[./includes/openWebResource-description.md](./includes/openWebResource-description.md)]

## Syntax

`Xrm.Navigation.openWebResource(webResourceName,windowOptions,data)`

## Parameters

|Name |Type |Required |Description |
|---|---|---|---|
|webResourceName|String|Yes|Name of the HTML web resource to open.|
|windowOptions|Object|No|Window options for opening the web resource. The object contains the following values:<br/>- **height**: (Optional) Number. Height of the window to open in pixels.<br/>- **width**: (Optional) Number. Width of the window to open in pixels.|
|data|String|No|Data to be passed into the data parameter.|

## Remarks

You must use this method to display web resources instead of the deprecated [Xrm.Utility.openWebResource](/previous-versions/dynamicscrm-2016/developers-guide/jj602956(v=crm.8)#BKMK_OpenWebResource) method.

An HTML web resource can accept the parameter values described in [Pass parameters to HTML web resources](../../../webpage-html-web-resources.md#BKMK_PassingParametersToWebResources). This function only provides for passing in the optional data parameter. To pass values for the other valid parameters, you must append them to the `webResourceName` parameter.

> [!NOTE]
> The **Xrm** object isn’t available in HTML web resources. Therefore, scripts containing `Xrm.*` methods aren’t supported in HTML web resources. `parent.Xrm.*` will work if the HTML web resource is loaded in a form container. However, for other places, such as loading an HTML web resource as part of the SiteMap, `parent.Xrm.*` also won’t work. More information: [GetGlobalContext function and ClientGlobalContext.js.aspx](../GetGlobalContext-ClientGlobalContext.js.aspx.md)



## Examples

- Open an HTML web resource named “new_webResource.htm”:
   
   `Xrm.Navigation.openWebResource("new_webResource.htm");`

- Open an HTML web resource, setting the windowOptions:

  ```JavaScript
  var windowOptions = { height: 400, width: 400 };
  Xrm.Navigation.openWebResource("new_webResource.htm",windowOptions);
  ```

- Open an HTML web resource including a single item of data for the `data` parameter

  `Xrm.Navigation.openWebResource("new_webResource.htm",null,"dataItemValue");`

 ### Related topics

[Xrm.Navigation](../xrm-navigation.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]