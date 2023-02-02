---
title: Modern, refreshed look for model-driven apps (preview)
description: Learn about the updated, user interface that makes model-driven apps easier to use.
author: sericks007
ms.topic: overview
ms.date: 01/24/2023
ms.service: powerapps
ms.subservice: end-user
ms.author: sericks
manager: tapanm-MSFT
ms.custom: bap-template
ms.reviewer:
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
---

# Modern, refreshed look for model-driven apps (preview)

[This article is pre-release documentation and is subject to change.]

Model-driven apps have a modern, refreshed look when the **Try the new look and feel (preview)** feature has been [turned on by makers](modern-fluent-design.md#turn-on-the-new-look) of the apps.  This new look provides updated styling including fonts, colors, borders, shadows, and more that align to the latest [Microsoft Fluent design system](https://react.fluentui.dev/?path=/docs/concepts-introduction--page). The updated look makes model-driven apps easier to use so that users can accomplish their goals quickly and efficiently.

The Fluent design system provides consistency, quality, and Microsoft-wide platform coherence. It also provides a solid foundation for extensibility and allows support for dark mode in the future. 

> [!IMPORTANT]
> - This is a preview feature.
> - [!INCLUDE[cc_preview_features_definition](../includes/cc-preview-features-definition.md)]

## What’s included with the new look
Here's what you can expect in the modern, refreshed experience:

- Updated styling in forms and view pages, including the use of drop shadows and brighter background colors to create an elevated or "floating" appearance, which helps to visually seperate sections and focuses attention on primary content
- New Fluent-based controls in forms, business process flows, and dialogs
- A new Power Apps grid in place of the read-only grid in view pages

With the new look, Power Apps are moving away from the classic theme customizations and will introduce a new theming capability in the future that builds on the Fluent design system.  

### Command bar
The "floating" command bar aligns with the Microsoft 365 experience, with consistent spacing, rounded corners, and elevation. Notice how the command bar is in a separate section at the top of the page in the following example.

![Floating command bar](media/new-command-bar.png)

### View pages
View pages use the new command bar and have updated grid areas that take advantage of the elevation changes to help draw the user’s attention. 

The biggest change on view pages is the switch from the read-only grid to the [Power Apps grid control (preview)](../maker/model-driven-apps/the-power-apps-grid-control.md), which features infinite scrolling for a modern, data browsing experience. This grid also appears in subgrids and associated grids in main forms, but isn't yet supported in dashboards. The Power Apps grid control also supports inline editing using the **Enable filtering** property. Makers may manually configure their editable grids to use the Power Apps grid control. 

The following example shows a view page with the modern, refreshed look.

![A view page with the modern, refreshed look.](media/ViewPage.png)

### Form pages
Form pages use the new command bar and have refreshed headers, tabs, sections, and business process flows. Quick views, card forms, headers, sitemaps, and timeline controls also feature updating styling.

The following example shows a form page with the modern, refreshed look.

![A formm page with the modern, refreshed look.](media/FormPage.png)

### Field controls
Field controls such as text input, action input, lookup, and check box controls are built and designed using Fluent components. More field controls will be modernized using Fluent design in future updates.

Field sections, which are containers for the fields on a form, have a more streamlined design. Icons have been moved to the right side of the field labels. Some redundant icons have been removed for a cleaner layout. For example, the explicit lock icon isn't shown for read-only fields. Input and error message styling has also been refreshed based on Fluent design. 

The following example shows a set of fields with the modern, refreshed look.

![Fields in a model-driven app that has the modern, refreshed look.](media/modern-fields.png)

## Turn on the new look
The modern look is disabled by default. Makers can enable the new look for existing and new model-driven apps in the app designer by turning on the **Try the new look and feel (preview)** feature for each model-driven app. 

Model-driven apps that are part of the preview will automatically get incremental enhancements weekly. For more information about enabling the modern, refreshed look, see [Manage model-driven app settings in the app designer](../maker/model-driven-apps/app-properties.md#upcoming).

## Provide feedback on the new look
After using the modern, refreshed look in your model-driven apps, tell us what you think about it in the [Power Apps New Look Feedback discussion thread](https://go.microsoft.com/fwlink/?linkid=2221574).

## Known limitations
The modern, refreshed look for model-driven apps has some limitations:

- The mobile app, mail app, and embedded Teams mode don't support the modern, refreshed look and aren't part of the preview.
- The modern, refreshed look isn't validated for Dynamics 365 applications at this time. Don't try out the preview in any production, Dynamics 365 applications.

