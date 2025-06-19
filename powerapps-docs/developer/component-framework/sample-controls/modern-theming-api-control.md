---
title: "Modern theming API component | Microsoft Docs"
description: "This sample component demonstrates various ways to use the modern theming API capabilities to style your component."
author: jasongre
ms.author: jasongre
ms.date: 03/12/2023
ms.reviewer: jdaly
ms.topic: sample
ms.subservice: pcf
search.audienceType:
  - developer
contributors:
  - JimDaly
---

# Implementing a modern theming API component

This sample component shows use cases to use the modern theming API capabilities to style your component based on the current theme used in your app. The imported components adhere to the default Power Apps modern theme initially, until you [enable modern controls and themes for your app](../../../maker/canvas-apps/controls/modern-controls/overview-modern-controls.md#enable-modern-controls-and-themes-for-your-app) and [apply a modern theme](../../../maker/canvas-apps/controls/modern-controls/modern-theming.md#apply-modern-theme).

:::row:::
   :::column:::
      :::image type="content" source="../media/modern-theming-api-control-blue.png" alt-text="Modern Theming API component blue theme":::
   :::column-end:::
   :::column:::
      :::image type="content" source="../media/modern-theming-api-control-red.png" alt-text="Modern Theming API component red theme":::
   :::column-end:::
   :::column:::
      :::image type="content" source="../media/modern-theming-api-control-green.png" alt-text="Modern Theming API component green theme":::
   :::column-end:::
:::row-end:::

## Available for

Model-driven and canvas apps

## Code

The sample component demonstrates four different examples consuming the Power Apps modern theming API.

- Fluent v9 sample with automatic application of the current modern theme: [Fluent UI v9 controls](../fluent-modern-theming.md#fluent-ui-v9-controls)
- Fluent v8 sample styling itself by creating its own v8 ThemeProvider based on the v9 theme tokens passed via the PCF context parameters: [Fluent UI v8 controls](../fluent-modern-theming.md#fluent-ui-v8-controls)
- Non-Fluent sample that applies styling to its HTML elements by directly referencing v9 theme tokens passed via the PCF context parameters: [Non-Fluent UI controls](../fluent-modern-theming.md#non-fluent-ui-controls)
- Fluent v9 sample creating its own custom v9 FluentProvider modifying the theme passed via the PCF context parameters. [Custom theme providers](../fluent-modern-theming.md#custom-theme-providers)

You can download the sample component from [PowerApps-Samples/component-framework/FluentThemingAPIControl](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework/FluentThemingAPIControl).

### Related articles

[Download sample components](https://github.com/microsoft/PowerApps-Samples/blob/master/component-framework/README.md)   
[How to use the sample components](../use-sample-components.md)   
[Power Apps component framework API reference](../reference/index.md)   
[Style components with modern theming (Preview)](../../component-framework/fluent-modern-theming.md)   
[Theming reference](../reference/theming.md)   
[Use modern themes in canvas apps (preview)](../../../maker/canvas-apps/controls/modern-controls/modern-theming.md)   
[Overview of modern controls and themes in canvas apps](../../../maker/canvas-apps/controls/modern-controls/overview-modern-controls.md)   

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
