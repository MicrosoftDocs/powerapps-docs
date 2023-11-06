---
title: "Style components with modern theming (preview) | Microsoft Docs"
description: You can style your components based on the modern theme used in the app."
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

# Style components with modern theming (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Professional developers need to be able to style their components so they look like the rest of the application they are included in. This is particularly true when modern theming is in effort for either a canvas app (via the [Modern controls and themes](../../maker/canvas-apps/controls/modern-controls/overview-modern-controls.md) feature) or model app (through the [new refreshed look](../../user/modern-fluent-design.md)). Utilizing modern theming, which is based on [Fluent UI React v9](https://react.fluentui.dev/), to style your component is the recommended way to get the best performance and theming experience for your component.

In this article, we will describe 4 different ways to apply modern theming to your component.  
-  Fluent v9 controls
-  Fluent v8 controls
-  Non-Fluent controls
-  Custom theme providers

## Fluent UI v9 controls

Wrapping Fluent UI v9 controls as a component is the easiest way to utilize modern theming as the modern theme will be automatically applied to these controls. The only prerequisite is to ensure your component adds a dependency on the [React controls & platform libraries (Preview)](../../component-framework/react-controls-platform-libraries.md) as shown below. This allows your component to use the same React and Fluent libraries as the platform and therefore share the same React context through which the theme tokens are passed down to the component.

```xml
<resources>
  <code path="index.ts" order="1"/>
  <!-- Dependency on React controls & platform libraries -->
  <platform-library name="React" version="16.8.6" />
  <platform-library name="Fluent" version="9.4.0" />
</resources>
```

## Fluent UI v8 controls

When using Fluent UI v8 controls in your component, Fluent provides a migration path for applying v9 theme constructs. In particular, you can create a v8 theme based on v9 theme tokens using the `createV8Theme` function included in the [Fluent's v8 to v9 migration package](https://www.npmjs.com/package/@fluentui/react-migration-v8-v9) using the code pattern below.

```tsx
const theme = createV8Theme(
  context.fluentDesignLanguage.brand,
  context.fluentDesignLanguage.theme
);
return <ThemeProvider theme={theme}></ThemeProvider>;
```

### Non-Fluent UI controls

Components that are not using Fluent UI can take a dependency directly on the v9 theme tokens available through the `fluentDesignLanguage` context parameter. This parameter provides access to all [theme](../reference/theming.md) tokens, allowing a component to reference any aspect of the theme to  style itself. 

```tsx
<span style={{ fontSize: context.fluentDesignLanguage.theme.fontSizeBase300 }}>
  {"Stylizing HTML with platform provided theme."}
</span>
```

## Custom theme providers 

For components that require styling that is partially or completely different from the current theme of the app, developers can create your own `FluentProvider` and pass your own set of theme tokens to be uptaken by your component.  

```tsx
<FluentProvider theme={context.fluentDesignLanguage.tokenTheme}>
  {/* your control */}
</FluentProvider>
```

## Sample controls

Examples for each of these use cases are available at [Modern Theming API control](./sample-controls/modern-theming-api-control.md).

## FAQ

### Q: My control uses Fluent UI v9 and has a dependency on the platform libraries, but I do not want to utilize modern theming. How can I disable it for my component?

A: There are two ways to accomplish this:

1. You can create your own component-level `FluentProvider`

```tsx
<FluentProvider theme={customFluentV9Theme}>
  {/* your control */}
</FluentProvider>
```

2. You can wrap your control inside `IdPrefixContext.Provider` and set your own `idPrefix` value. This will prevent your component from getting theme tokens from the platform.

```tsx
<IdPrefixProvider value="custom-control-prefix">
  <Label weight="semibold">This label is not getting Modern Theming</Label>
</IdPrefixProvider>
```

### Q: Some of my Fluent UI v9 controls are not getting styles

A: Fluent v9 controls that rely on the React Portal will need to be rewrapped in the theme provider to ensure styling is properly applied. You can use `FluentProvider`.

### Q: How can I check if modern theming is enabled

A: You can check it in app settings: `context.appSettings.getIsFluentThemingEnabled()` or check if tokens are available: `context.fluentDesignLanguage?.tokenTheme`.

## Related topics

[Theming (Power Apps component framework API reference)](../component-framework/reference/theming.md)<br />
[Modern Theming API control](./sample-controls/modern-theming-api-control.md)
[Use modern themes in canvas apps (preview)](../../../maker/canvas-apps/controls/modern-controls/modern-theming)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
