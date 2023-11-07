---
title: "Modern theming API component | Microsoft Docs"
description: "This sample component demonstrates various ways of utiliznig the modern theming API capabilities to style your component."
author: lesyk
ms.author: vilesyk
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

This sample component showcases a variety of use cases for utilizing the modern theming API capabilities to style your component based on the current theme used in your app. The imported components will adhere to the default Power Apps modern theme initially, until the you have [enabled modern controls and themes for your app](../../../powerapps/maker/canvas-apps/controls/modern-controls/overview-modern-controls.md#enable-modern-controls-and-themes-for-your-app) and [applied a modern theme](../../../maker/canvas-apps/controls/modern-controls/modern-theming#apply-modern-theme).

> [!div class="mx-imgBorder"] > ![Modern Theming API component](../media/modern-theming-api-control.png "Modern Theming API component")

## Available for

Canvas apps

## Code

The sample component illustrates four different examples consuming the Power Apps modern theming API.

- Fluent v9 sample with automatic application of the current modern theme: [Automatic Modern Theming](../../component-framework/fluent-modern-theming.md#automatic-modern-theming)<br/>
- Fluent v8 sample styling itself by creating its own v8 ThemeProvider based on the v9 theme tokens passed via the PCF context parameters: [Modern Theming for Fluent UI v8 controls](../../component-framework/fluent-modern-theming.md#modern-theming-for-fluent-ui-v8-controls)<br/>
- Non-Fluent sample that applies styling to its HTML elements by directly referencing v9 theme tokens passed via the PCF context parameters: [Modern Theming for non-Fluent UI controls](../../component-framework/fluent-modern-theming.md#modern-theming-for-non-fluent-ui-controls)<br/>
- Fluent v9 sample creating its own custom v9 FluentProvider modifying the theme passed via the PCF context parameters. [Modern Theming via PCF context parameters](../../component-framework/fluent-modern-theming.md#modern-theming-via-pcf-context-parameters)<br/>

You can download the complete sample component from [here](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework/FluentThemingAPIControl).

### Related topics

[Download sample components](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework)<br/>
[How to use the sample components](../use-sample-components.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Style components with modern theming (Preview)](../../component-framework/fluent-modern-theming.md)<br/>
[Theming (Power Apps component framework API reference) | Microsoft Docs](../../../powerapps/developer/component-framework/reference/theming)
[Use modern themes in canvas apps (preview)](../../../maker/canvas-apps/controls/modern-controls/modern-theming)
[Overview of mdoern controls and themes (preview)](../../..//maker/canvas-apps/controls/modern-controls/overview-modern-controls)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
