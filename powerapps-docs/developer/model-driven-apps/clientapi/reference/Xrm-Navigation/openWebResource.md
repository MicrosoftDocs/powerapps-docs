---
title: "openWebResource (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 798dc921-1e80-42bc-b8ca-2056728bcba4
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
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
|windowOptions|Object|No|Window options for opening the web resource. The object contains the following attributes:<br/>- **height**: (Optional) Number. Height of the window to open in pixels.<br/>- **openInNewWindow**: Boolean. Indicates whether to open the web resource in a new window.<br/>- **width**: (Optional) Number. Width of the window to open in pixels.|
|data|String|No|Data to be passed into the data parameter.|

## Remarks

You must use this method to display web resources instead of the deprecated [Xrm.Utility.openWebResource](https://msdn.microsoft.com/library/jj602956.aspx#BKMK_OpenWebResource) method.

An HTML web resource can accept the parameter values described in [Pass parameters to HTML web resources](../../../webpage-html-web-resources.md#BKMK_PassingParametersToWebResources). This function only provides for passing in the optional data parameter. To pass values for the other valid parameters, you must append them to the `webResourceName` parameter.

> [!NOTE]
> The **Xrm** object isn’t available in HTML web resources. Therefore, scripts containing `Xrm.*` methods aren’t supported in HTML web resources. `parent.Xrm.*` will work if the HTML web resource is loaded in a form container. However, for other places, such as loading an HTML web resource as part of the SiteMap, `parent.Xrm.*` also won’t work. More information: [GetGlobalContext function and ClientGlobalContext.js.aspx](../GetGlobalContext-ClientGlobalContext.js.aspx.md)



## Examples

- Open an HTML web resource named “new_webResource.htm”:
   
   `Xrm.Navigation.openWebResource("new_webResource.htm");`

- Open an HTML web resource, setting the windowOptions:

  ```
  var windowOptions = { openInNewWindow: true, height: 400, width: 400 }
  Xrm.Navigation.openWebResource("new_webResource.htm",windowOptions);
  ```

- Open an HTML web resource including a single item of data for the `data` parameter

  `Xrm.Navigation.openWebResource("new_webResource.htm",null,"dataItemValue");`

 ### Related topics

[Xrm.Navigation](../xrm-navigation.md)

