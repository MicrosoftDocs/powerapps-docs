---
title: Improved tab stops for the keyboard tab key in canvas apps (Experimental)
description: Learn about how to use the improved tab stops experience for better accessibility.
author: hemantgaur
ms.service: powerapps
ms.topic: article
ms.custom: canvas
ms.date: 08/03/2021
ms.subservice: canvas-maker
ms.author: hemantg
search.audienceType:
  - maker
search.app:
  - PowerApps
contributors:
  - tahoon-ms
  - tapanm-msft
  - hemantgaur
---

# Improved tab stops for the keyboard tab key in canvas apps (Experimental)

[This article is pre-release documentation and is subject to change.]

We've introduced a new experimental setting named **Improved tab stops** to improve the keyboard tab stop behavior when using composite or nested controls in canvas apps. This feature adds support for handling accessibility for keyboard tabs inline with rest of the controls in canvas apps. To maintain backward compatibility and not affect the functionality of the existing apps, this feature is added as an experimental feature.

In some scenarios, when nesting controls such as containers and component instances, a user input value for [TabIndex](controls/properties-accessibility.md#tabindex) isn't respected. This feature addresses manual TabIndex assignments for all controls and components.

> [!IMPORTANT]
> - This is an experimental feature.
> - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)]

When this feature is turned on, it also enables the following boolean properties for containers and component in canvas apps:

| Property Name | Description |
| - | - |
| **Prioritize child controls** | Determines the order of navigation (**Z-order**) on canvas when pressing tab key on the keyboard. <ul> <li> **True** (Default): Pressing the tab key on the keyboard will first progress through all child controls of the current container before moving to the next available control. This option is recommended for similarly nested HTML elements. </li> <li> **False**: Pressing the tab key on the keyboard will progress through all controls only based on Z-order, ignoring parent-child relationship between controls or containers. </li> </ul> **Note**: This property is not applicable to [responsive or auto-layout](create-responsive-layout.md) containers. |
| **Focus on child controls** | Determines the value of [TabIndex](controls/properties-accessibility.md#tabindex) for child controls. <ul> <li> **True** (Default): Pressing the tab key behaves as per TabIndex values defined on each control. </li> <li> **False**: Pressing the tab key doesn't move focus to any child control for the selected container or component. Sets the TabIndex value to **-1** for all child controls of the current container or component. |

## Tab stop examples

Now that you understand the new feature with improved tab stops, let's take a look at a few examples to understand the behavior when the tab key is pressed.

### Default behavior

On the following example screen, there are multiple  Text Input controls and various nesting scenarios. The number displayed in the input represents the value of the TabIndex property. There are two nested container controls, as well as two component controls overlayed on top of each other. 
The default order is determined by the relative position of the controls. When focus enters a container or component, tabs first traverse the children of the container before moving on to the next available control. 

![Default behavior of the app](media\accessibility-tab-stops\default-behavior.gif "Default behavior of the app")
 
### Prioritize child controls set to false

In the following example, every container and component has the “Child tab priority” property set to false. All inputs are therefore considered by the accessibility pipeline to be on the same level of nesting, so the order is determined purely by their X/Y position relative to the screen.

![Don't prioritize child controls](media\accessibility-tab-stops\child-control-priority.gif "Don't prioritize child controls")
 
### Mix and Match

In the following example, the Orange outlined containers have “Child tab priority” false. All others are true. Additionally, a custom TabIndex property has been set for some inputs, indicated by the number shown in each input.
Tab order first proceeds through all numbered TabIndexes greater than 0, and then proceeds through all 0 TabIndexes according to the above logic. This was the intended behavior in the original implementation.

![Mix and match](media\accessibility-tab-stops\hybrid-configuration.gif "Mix and match")

### See also

- [Create accessible apps](accessible-apps.md)
- [Accessible app structure](accessible-apps-structure.md)
- [Accessible colors in Power Apps](accessible-apps-color.md)
- [Use the Accessibility checker](accessibility-checker.md)
- [Accessibility limitations in canvas apps](accessible-apps-limitations.md)
- [Accessibility properties](controls/properties-accessibility.md)
