---
title: "Embed a canvas app on a model-driven form"
description: "With embedded canvas apps, app makers can bring the power of canvas apps to their Power Apps model-driven app forms." 
ms.custom: "Steps to embedding a canvas app on a form"
ms.date: 01/22/2025
ms.reviewer: ""
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
tags: 
  - "Power Apps maker portal impact"
search.audienceType: 
  - maker
---
# Embed a canvas app on a model-driven form

Canvas apps enable makers to easily design and create custom layouts using the low-code, WYSIWYG Power Apps Studio. Canvas apps also enable makers to connect and display data from over 400 data sources.

## Embedded canvas apps can help you build better solutions

With embedded canvas apps, makers can bring the power of canvas apps to their model-driven app forms. Using embedded canvas apps, it's possible to create rich visual areas on a form and display data from a variety of sources right next to data from Microsoft Dataverse.

:::image type="content" source="media/embed-canvas-app-in-form.png" alt-text="Embedded canvas app in a model-driven app form.":::

Canvas apps are embedded in model-driven app forms in the same way other custom controls are added. An embedded canvas app includes rich data integration capabilities that bring in contextual data from the host model-driven form to the embedded canvas app.

## Integrate canvas apps using custom pages in the modern app designer

With the modern app designer, canvas apps can be accessed through a model-driven app by using a custom page.

The modern app designer introduced the concept of [pages](model-driven-app-glossary.md#page), which can contain either canvas apps or Dataverse components, such as tables, dashboards, and web resources.

## Embed using the modern designer

Select the **Canvas app** control to add a canvas app to a main form using the form designer. More information: [Add an embedded canvas app on a model-driven form](embedded-canvas-app-add-classic-designer.md)

## Embed using the classic designer

Add canvas apps from an environment into a model-driven app that can either be contextually aware, or simply render the app within the model-driven experience. More information: [Embed a canvas app using the classic experience](embedded-canvas-app-add-classic-designer.md#embed-a-canvas-app-using-the-classic-experience).

### Sharing embedded canvas apps

After an embedded canvas app is added to your model-driven form, learn how to share the embedded canvas app with other users. More information: [Learn how to share an embedded canvas app](share-embedded-canvas-app.md).

For guidelines on working with embedded canvas apps as well as helpful tips to troubleshoot any issues, go to: [Guidelines on working with embedded canvas apps](embedded-canvas-app-guidelines.md).

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
