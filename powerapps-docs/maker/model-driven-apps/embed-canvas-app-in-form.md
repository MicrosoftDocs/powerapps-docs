---
title: "Embed a canvas app in a model-driven form | MicrosoftDocs"
ms.custom: ""
ms.date: 12/06/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "get-started-article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
ms.assetid: 00e62904-2ce9-4730-a113-02b1fedbf22e
author: "Mattp123"
ms.author: "matp"
manager: "kvivek"
tags: 
  - "PowerApps maker portal impact"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---

# Embed a canvas app in a model-driven form

Canvas apps enable makers to easily design and create custom layouts using the low-code, WYSIWYG canvas app designer. Canvas apps also enable makers to connect and display data from over 200 data sources on their forms.

> [!NOTE]
> This feature is currently in preview. <br />
> [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]

With embedded canvas apps, makers can bring the power of canvas apps to their model-driven forms. Using embedded canvas apps, makers can easily create rich visual areas on their form and also display data from a variety of data sources right next to their data from the Common Data Service.

   ![Embedded canvas app in a model-driven app form](media/embed-canvas-app-in-form.png)

Canvas apps are embedded in model-driven forms similar to how any other custom control is added. The embedded canvas apps also include rich data integration capabilities that brings in contextual data from the host model-driven form to the embedded canvas app.

The steps to embed a canvas app in your model-driven form vary based on the data context that you want the host model-driven form to provide to the embedded canvas app.
-	Pass the current record as data context. More information: (LINK TO ARTICLE #2)
-	Pass a list of records related to the current record as data context. More information:  (LINK TO ARTICLE #3)

After you have added an embedded canvas app to your model-driven form, learn how to share your embedded canvas app with other users (LINK TO ARTICLE #4).

For things to keep in mind when working with embedded canvas apps and to help troubleshoot any issues you might encounter, see (LINK TO ARTICLE #5).

## See also
[What are canvas apps in PowerApps?](../canvas-apps/getting-started.md) <br />
[Add and configure a canvas-app control in PowerApps](../canvas-apps/add-configure-controls.md) <br />
[Overview of canvas-app connectors for PowerApps](../canvas-apps/connections-list.md)
