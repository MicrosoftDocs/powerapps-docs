---
title: Improved keyboard navigation in canvas apps (Experimental)
description: Learn about how to use the improved keyboard navigation experience for better accessibility.
author: hemantgaur
ms.service: powerapps
ms.topic: article
ms.custom: canvas
ms.date: 08/04/2021
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

# Improved keyboard navigation in canvas apps (Experimental)

[This article is pre-release documentation and is subject to change.]

> [!IMPORTANT]
> - This is an experimental feature.
> - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)]

When you're nesting controls such as containers and component instances, the user input value for [TabIndex](controls/properties-accessibility.md#tabindex) isn't respected sometimes. **Improved keyboard navigation** experimental setting improves the navigation experience in this situation when **Tab** key is pressed on the keyboard helping focus on the desired container or control precisely and predictably.

This feature also adds support for handling accessibility for keyboard tabs inline with rest of the controls in canvas apps. And addresses manual TabIndex assignments for all controls.

> [!NOTE]
> This feature is added as "Experimental" to maintain backward compatibility and maintain existing app functionality.

When this feature is turned on, it also enables the following boolean properties for all child controls for the selected container or component instance in canvas apps:

| Property Name | Description |
| - | - |
| **Prioritize child controls** | Determines the order of navigation (**Z-order**) for child controls on canvas when pressing tab key on the keyboard. <ul> <li> **True** (Default): Pressing the tab key on the keyboard will first progress through all child controls before moving the focus outside of the selected container or component instance. This option is recommended for similarly nested HTML elements. </li> <li> **False**: Pressing the tab key on the keyboard will progress through all controls only based on Z-order, ignoring parent-child relationship between controls or containers for keyboard navigation. </li> </ul> **Note**: This property isn't applicable to [responsive or autolayout](create-responsive-layout.md) containers. |
| **Disable child control focus** | Determines the value of [TabIndex](controls/properties-accessibility.md#tabindex) for child controls on canvas when pressing tab key on the keyboard. <ul> <li> **False** (Default): Pressing the tab key behaves as per TabIndex values defined on each control. </li> <li> **True**: Pressing the tab key doesn't move focus to any child control within the selected container or component instance. Sets the TabIndex value to **-1** for all child controls. </li> </ul> |

## Configure improved keyboard navigation in your app

Follow these steps to enable this feature in your app, and set the properties mentioned earlier.

1. Sign in to [Power Apps](https://make.poweraps.com).

1. Select **Apps** from the left-pane.

1. Select your app, and then select **Edit**.

1. In Power Apps Studio, select **File** > **Settings** > **Upcoming features** > **Experimental**.

1. Select **Improved keyboard navigation** to turn on the feature. !![Screenshot to follow]!!

1. Close settings.

Now that you've enabled the experimental feature, you'll see two new properties for controls and containers&mdash;**Prioritize child controls**, and **Disable child control focus**. Change the property values as appropriate.

## Examples

Now that you understand the new feature with improved keyboard navigation, let's take a look at a few examples to understand the behavior when the tab key is pressed.

### Default improved keyboard navigation behavior

The following example shows multiple Text input controls, and several nesting scenarios. The number displayed in the input represents the value of the [TabIndex](controls/properties-accessibility.md#tabindex) property. There are two nested containers, and component controls overlaid on top of each other.

The default order is determined by the relative position of the controls. When focus enters a container or a component, tabs first traverse the children of the container before moving on to the next available control.

![Default behavior of the app](media\accessibility-tab-stops\default-behavior.gif "Default behavior of the app")

### When Prioritize child controls is set to False

In the following example, each container and component control has the **Prioritize child controls** property set to "False". All inputs are therefore considered to be on the same level of nesting, so the order is determined purely by their [X/Y position](controls/properties-size-location.md#position) relative to the screen.

![Don't prioritize child controls](media\accessibility-tab-stops\child-control-priority.gif "Don't prioritize child controls")

### Advanced configuration with mixed settings

In the following example, the orange outlined containers have **Prioritize child controls** property set to "False". All others controls have this property set to "True". Also, a custom [TabIndex](controls/properties-accessibility.md#tabindex) property has been set for some inputs, indicated by the number shown in each input.

Tab order first proceeds through the containers and controls with TabIndex value of greater than 0, and then proceeds through all others with value of 0. This behavior was also the in the earlier implementation.

![Advanced configuration with mixed settings](media\accessibility-tab-stops\hybrid-configuration.gif "Advanced configuration with mixed settings")

### See also

- [Create accessible apps](accessible-apps.md)
- [Accessible app structure](accessible-apps-structure.md)
- [Accessible colors in Power Apps](accessible-apps-color.md)
- [Use the Accessibility checker](accessibility-checker.md)
- [Accessibility limitations in canvas apps](accessible-apps-limitations.md)
- [Accessibility properties](controls/properties-accessibility.md)
