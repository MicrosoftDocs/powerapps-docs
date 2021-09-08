---
title: "GetGlobalContext function and ClientGlobalContext.js.aspx in model-driven apps| MicrosoftDocs"
ms.date: 03/22/2021
ms.service: powerapps
ms.topic: "conceptual"
ms.assetid: b58e6173-e3cd-4a3b-b39a-334c295503ec
author: "Nkrb"
ms.subservice: mda-developer
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# GetGlobalContext function and ClientGlobalContext.js.aspx (Client API reference)

Use the **GetGlobalContext** function when programming with [web resources](../../web-resources.md) to gain access to the global context information such as the information specific to the client, organization or user for your model-driven apps instance. 

To get access to the **GetGlobalContext** function in your HTML web resource, include a reference to **ClientGlobalContext.js.aspx**.

> [!IMPORTANT]
> - The ClientGlobalContext.js.aspx page is deprecated and scheduled to be unavailable after April 1, 2022. Alternative methods to access global context information will be available by December, 2021.
> - Including a reference to **ClientGlobalContext.js.aspx** does not make the **Xrm** object available in HTML web resources. Therefore, scripts containing `Xrm.*` methods aren’t supported in HTML web resources. `parent.Xrm.*` will work if the HTML web resource is loaded in a form container. However, for other places, such as loading an HTML web resource as part of the SiteMap, `parent.Xrm.*` also won’t work.

## GetGlobalContext function

The **GetGlobalContext** function returns the same context object as returned by the **Xrm.Utility.getGlobalContext** method, which implies that the context object will have the same properties and methods as available for **Xrm.Utility.getGlobalContext**. More information: Xrm.Utility.[getGlobalContext](Xrm-Utility/getGlobalContext.md)

## ClientGlobalContext.js.aspx

You must include a reference to the **ClientGlobalContext.js.aspx** page located at the root of the web resources directory to be able to use the **GetGlobalContext** function.

- If you are not using slash characters in HTML web resource names to simulate a folder structure, you can include this script by directly referring to it. For example:

    ```HTML
    <head>
      <title>HTML Web Resource</title>
      <script src="ClientGlobalContext.js.aspx" type="text/javascript" ></script>
      
    </head>
    ```
- If you are using backslash characters in HTML web resource names to simulate a directory structure, you must reflect this in your script element. The following example is for an HTML web resource named **sdk_/Contoso.htm** and a JavaScript web resource named **sdk_/Scripts/ContosoScript.js** with a CSS web resource named **sdk_/Styles/ContosoStyles.css**.

    ```HTML
    <head>
      <title>HTML Web Resource</title>
      <script src="../ClientGlobalContext.js.aspx" type="text/javascript" ></script>

      <script src="Scripts/ContosoScript.js" type="text/javascript"></script>
      <link href="Styles/ContosoStyles.css" rel="stylesheet" type="text/css" />
    </head>

    ```

> [!NOTE]
> Using a relative path including the root WebResources folder, for example, /WebResources/ClientGlobalContext.js.aspx, is not recommended because it can cause the page to lose organization context in a multi-tenant environment.

The **ClientGlobalContext.js.aspx** page will include some global event handlers. These event handlers will cancel the [onselectstart](https://developer.mozilla.org/docs/Web/Events/selectstart), [contextmenu](https://developer.mozilla.org/docs/Web/Events/contextmenu), and [ondragstart](https://developer.mozilla.org/docs/Web/Events/dragstart) events. 

### Related topics

[Xrm.Utility.getGlobalContext](Xrm-Utility/getGlobalContext.md)

[Understand Client API object model](../understand-clientapi-object-model.md) 

[Web resources for model-driven apps](../../web-resources.md)



[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
