---
title: "Embed a canvas app on a model-driven form | MicrosoftDocs"
ms.custom: ""
ms.date: 06/25/2019
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "conceptual"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
ms.assetid: 00e62904-2ce9-4730-a113-02b1fedbf22e
author: "Aneesmsft"
ms.subservice: mda-maker
ms.author: "matp"
manager: "kvivek"
tags: 
  - "Power Apps maker portal impact"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---

# Embed a canvas app on a model-driven form

## What are canvas apps?
Canvas apps enable makers to easily design and create custom layouts using the low-code, WYSIWYG canvas app designer. Canvas apps also enable makers to connect and display data from over 400 data sources.

## How embedding canvas apps can help us build better solutions
With embedded canvas apps, makers can bring the power of canvas apps to their model-driven forms. Using embedded canvas apps, it is possible to create rich visual areas on a form and display data from a variety of sources right next to data from the Microsoft Dataverse.

   > [!div class="mx-imgBorder"] 
   > ![Embedded canvas app in a model-driven app form.](media/embed-canvas-app-in-form.png "Embedded canvas app in a model-driven app form")

Canvas apps are embedded in model-driven forms in the same way other custom controls are added. An embedded canvas app includes rich data integration capabilities that bring in contextual data from the host model-driven form to the embedded canvas app.

## Embedding using the modern designer (preview)

The **modern designer** permits apps built over Dataverse to be embedded into a model-driven app natively.  

Modern apps introduce the concept of [pages](model-driven-app-glossary.md#page) which can either be canvas apps or model-driven apps.
<br />[Learn more about building modern apps](app-designer-overview.md)

## Embedding using the classic designer (current)
We can add canvas apps from our environments into our model-driven apps that can either be contextually aware, or simply render the app within the model-driven experience. <br />[Learn how to add an embedded canvas app on a model-driven form - classic designer](embedded-canvas-app-add-classic-designer.md).

## Sharing canvas apps

After an embedded canvas app has been added to your model-driven form, learn how to share the embedded canvas app with other users. More information: [Learn how to share an embedded canvas app](share-embedded-canvas-app.md).

For guidelines on working with embedded canvas apps as well as helpful tips to troubleshoot any issues, please refer to: [Guidelines on working with embedded canvas apps](embedded-canvas-app-guidelines.md).

## See also
[What are canvas apps in Power Apps?](../canvas-apps/getting-started.md) <br />
[Add and configure a canvas-app control in Power Apps](../canvas-apps/add-configure-controls.md) <br />
[Overview of canvas-app connectors for Power Apps](../canvas-apps/connections-list.md) <br />
[Add an embedded canvas app on a model-driven form](embedded-canvas-app-add-classic-designer.md) <br />
[Edit a canvas app embedded on a model-driven form](embedded-canvas-app-edit-classic-designer.md) <br />
[Customize the screen size and orientation of a canvas app embedded on a model-driven form](embedded-canvas-app-customize-screen.md) <br />
[Perform predefined actions on the host form from within an embedded canvas app](embedded-canvas-app-actions.md) <br />
[ModelDrivenFormIntegration control's properties and actions](embedded-canvas-app-properties-actions.md) <br />
[Share an embedded canvas app](share-embedded-canvas-app.md) <br />
[Guidelines on working with embedded canvas apps](embedded-canvas-app-guidelines.md) <br />
[Migrating embedded canvas apps on model-driven forms created using the public preview release to latest](embedded-canvas-app-migrate-from-preview.md) <br />


[!INCLUDE[footer-include](../../includes/footer-banner.md)]