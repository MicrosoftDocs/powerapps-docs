---
title: "Modern Theming API component | Microsoft Docs"
description: "This sample component showcases Modern Theming API capabilities of the Power Apps control framework."
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

# Implementing a Modern Theming API component

This sample component showcases Modern Theming API capabilities of the Power Apps control framework. Out of the box after importing control it will use default PowerApps Modern Theme, in order to change it you need to [Enable modern controls and themes for your app](../../../powerapps/maker/canvas-apps/controls/modern-controls/overview-modern-controls.md#enable-modern-controls-and-themes-for-your-app), and then [Apply modern theme](../../../maker/canvas-apps/controls/modern-controls/modern-theming#apply-modern-theme).

> [!div class="mx-imgBorder"] > ![Modern Theming API component](../media/modern-theming-api-control.png "Modern Theming API component")

## Available for

Canvas apps

## Code

Control showcases four different examples of consuming PowerApps Modern Theming API:

- Fluent V9 out of the box inheritance of theme from the platform. [Automatic Modern Theming](../../component-framework/fluent-modern-theming.md#automatic-modern-theming)<br/>
- Fluent V9 sample of using pcf context parameters to create it's own FluentProvider (v9). [Modern Theming via PCF context parameters](../../component-framework/fluent-modern-theming.md#modern-theming-via-pcf-context-parameters)<br/>
- Fluent V8 sample of using pcf context parameters and using a shim to create it's own ThemeProvider (v8). [Modern Theming for Fluent UI v8 controls](../../component-framework/fluent-modern-theming.md#modern-theming-for-fluent-ui-v8-controls)<br/>
- Non fluent sample of using pcf context parameters and applying styles directly to the HTML elements. [Modern Theming for non-Fluent UI controls](../../component-framework/fluent-modern-theming.md#modern-theming-for-non-fluent-ui-controls)<br/>

You can download the complete sample component from [here](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework/FluentThemingAPIControl).

### Related topics

[Download sample components](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework)<br/>
[How to use the sample components](../use-sample-components.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Modern Theming (Preview)](../../component-framework/fluent-modern-theming.md)<br/>
[Theming (Power Apps component framework API reference) | Microsoft Docs](../../../powerapps/developer/component-framework/reference/theming)
[Use modern themes in canvas apps (preview)](../../../maker/canvas-apps/controls/modern-controls/modern-theming)
[Modern Theming (preview) - Power Apps | Microsoft Docs](../../..//maker/canvas-apps/controls/modern-controls/overview-modern-controls)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
