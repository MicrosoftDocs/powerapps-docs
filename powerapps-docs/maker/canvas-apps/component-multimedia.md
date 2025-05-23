---
title: Add multimedia to a component
description: Learn about how to add multimedia to a canvas component.
author: jorisdg
ms.subservice: canvas-developer
ms.topic: article
ms.date: 06/01/2022
ms.author: jorisde
ms.reviewer: mkaur
search.audienceType:
  - maker
contributors:
  - jorisdg
  - mduelae
---

# Add multimedia to a component

You can add multimedia files to the components inside a library. These components can then be used by all apps in an environment and can be moved across environments using standard [component application lifecycle management](component-library-alm.md) (ALM) through solutions in Microsoft Dataverse.

To add multimedia to a component, use the same steps that you'd follow when adding multimedia files in a canvas app. More information: [Using multimedia files in canvas apps](add-images-pictures-audio-video.md)

After adding multimedia files to a component inside the component library, the files will appear under the media pane as they do for canvas apps:

:::image type="content" source="media/component-multimedia/add-multimedia.png" alt-text="Example of Power Apps Studio with a library and multimedia added.":::

Media resources in a component library are defined at the library level, and not tied to individual components. Importing any component from the component library will import all media resources from the library to the app. However, you can remove the unused media when app customization is complete. More information: [Remove unused media](add-images-pictures-audio-video.md#remove-unused-media)

> [!TIP]
> Prefix the media resources in a component library with a unique namespace or library name so that those names don't conflict with existing resources in an app during import.

During the component import to your app, if the component library multimedia has a resource with the same name as the multimedia that already exists inside your app, the import process adds an underscore ("_") and a random number to enforce name uniqueness.

## Example

Consider that you created a component library with a slider image that uses an icon with an [input property](map-component-input-fields.md) for the component named "value" to set it's `X` property.

:::image type="content" source="media/component-multimedia/slider-component.png" alt-text="Slider component using an input property named value.":::

To reuse this multimedia component in your app, all you have to do is import the component, and link the component's input property with the value you'll supply from within the app.

Start with importing the component to your app:

:::image type="content" source="media/component-multimedia/imported-component.png" alt-text="Component imported to your app.":::

After the import, you can insert a [slider](controls/control-slider.md) control, and set the imported component's value to the slider's value:

:::image type="content" source="media/component-multimedia/insert-slider.png" alt-text="Set component value to the slider's value.":::

When you play this app, the slider movement in the app would then move the imported slider component:

:::image type="content" source="media/component-multimedia/play-app.png" alt-text="App being played that will move slider inside component as slider control is moved":::

### See also

- [Canvas components](create-component.md)
- [Component library](component-library.md)
- [Component library application lifecycle management (ALM)](component-library.md)
- [Behavior formulas for components](component-behavior.md)
- [Power Apps component framework](../../developer/component-framework/component-framework-for-canvas-apps.md) 
- [Add canvas components to a custom page in a model-driven app](../model-driven-apps/page-canvas-components.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
