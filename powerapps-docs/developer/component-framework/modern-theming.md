---
title: "Modern Theming (Preview) | Microsoft Docs"
description: Modern Theming enables your control to get theme styling based on the current theme of the app."
keywords: "Component Framework, code components, Power Apps controls"
ms.author: hemantg
author: HemantGaur
ms.date: 10/06/2023
ms.reviewer: jdaly
ms.custom:
  - "dyn365-a11y"
  - "dyn365-developer"
ms.topic: article
ms.subservice: pcf
contributors:
  - HemantGaur
  - noazarur-microsoft
  - JimDaly
---

# Modern Theming (Preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Modern Theming enables your control to get theme styling based on the current theme of the app.

PowerApps platform theming is based on the [Fluent UI React v9](https://react.fluentui.dev/) and therefore it is the most recommended way to build your control to get the best performance and theming experience.

## Automatic Modern theming

The simplest way is to use use Fluent UI v9 in your control then Modern theming will be applied to the control automatically.

### Prerequisites

In order to get Modern Theming for your control, you will need to add a dependency on the [React controls & platform libraries (Preview)](../../component-framework/react-controls-platform-libraries.md), as following:

```xml
<resources>
  <code path="index.ts" order="1"/>
  <!-- Dependency on React controls & platform libraries -->
  <platform-library name="React" version="16.8.6" />
  <platform-library name="Fluent" version="9.4.0" />
</resources>
```

This would enable control and the platform to share the same react and Fluent libraries and therefore share the same react context via which theme tokens are passed down to the control.

## Modern theming via PCF context parameters

Power platform passes down new context parameter to the PCF controls: `fluentDesignLanguage`: [Theming](../reference/theming.md). This parameter contains all theme tokens, so control can be styled based on the current theme of the app.

This enables to create your own `FluentProvider` and pass down theme tokens to the control.

```tsx
<FluentProvider theme={context.fluentDesignLanguage.tokenTheme}>
  {/* your control */}
</FluentProvider>
```

### Modern theming for Fluent UI v8 controls

Fluent UI has a migration npm package: [@fluentui/react-migration-v8-v9](https://www.npmjs.com/package/@fluentui/react-migration-v8-v9) that provides `createV8Theme` functions to create Fluent UI v8 theme from Fluent UI v9 theme tokens. So, it is possible to have v8 theme for your control based on the v9 platform theme.

```tsx
const theme = createV8Theme(
  context.fluentDesignLanguage.brand,
  context.fluentDesignLanguage.theme
);
return <ThemeProvider theme={theme}></ThemeProvider>;
```

### Modern theming for non-Fluent UI controls

For controls that are not using Fluent UI you can just take dependency on the direct tokens from the context parameter and apply them to the HTML elements.

```tsx
<span style={{ fontSize: context.fluentDesignLanguage.theme.fontSizeBase300 }}>
  {"Stylizing HTML with platform provided theme."}
</span>
```

## Sample controls

You can find new control added to the samples as part of this preview, [Fluent Theming API control](./sample-controls/fluent-theming-api-control.md).

## FAQ

### Q: My control uses Fluent UI v9 and has a dependency on the platform libraries, but I do not want to use Modern theming. How can I disable it for my control?

A: There are two ways how you can do it:

1. by creating your own control level `FluentProvider`

```tsx
<FluentProvider theme={customFluentV9Theme}>
  {/* your control */}
</FluentProvider>
```

2. by wrapping your control into `IdPrefixContext.Provider` and set your own `idPrefix` value. This will prevent your control from getting theme tokens from the platform.

```tsx
<IdPrefixProvider value="custom-control-prefix">
  <Label weight="semibold">This label is not getting Modern theming</Label>
</IdPrefixProvider>
```

## Related topics

???

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
