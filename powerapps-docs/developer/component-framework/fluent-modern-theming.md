---
title: "Style components with modern theming (preview) | Microsoft Docs"
description: You can style your components based on the modern theme used in the app."
keywords: "Component Framework, code components, Power Apps controls"
author: jasongre
ms.author: jasongre
ms.date: 12/04/2024
ms.reviewer: jdaly
ms.custom:
  - "dyn365-a11y"
  - "dyn365-developer"
ms.topic: how-to
ms.subservice: pcf
contributors:
  - HemantGaur
  - JimDaly
---

# Style components with modern theming (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Developers need to be able to style their components so they look like the rest of the application they're included in. They can do this when modern theming is in effect for either a canvas app (via the [Modern controls and themes](../../maker/canvas-apps/controls/modern-controls/overview-modern-controls.md) feature) or model-driven app (through the [new refreshed look](../../user/modern-fluent-design.md)). Use modern theming, which is based on [Fluent UI React v9](https://react.fluentui.dev/), to style your component. This approach is recommended to get the best performance and theming experience for your component.

There are four different ways to apply modern theming to your component.

- [Fluent UI v9 controls](#fluent-ui-v9-controls)
- [Fluent UI v8 controls](#fluent-ui-v8-controls)
- [Non-Fluent UI controls](#non-fluent-ui-controls)
- [Custom theme providers](#custom-theme-providers)

## Fluent UI v9 controls

Wrapping Fluent UI v9 controls as a component is the easiest way to utilize modern theming because the modern theme is automatically applied to these controls. The only prerequisite is to ensure your component adds a dependency on the [React controls & platform libraries](react-controls-platform-libraries.md) as shown below. This approach allows your component to use the same React and Fluent libraries as the platform, and therefore share the same React context that passes the theme tokens down to the component.

```xml
<resources>
  <code path="index.ts" order="1"/>
  <!-- Dependency on React controls & platform libraries -->
  <platform-library name="React" version="16.14.0" />
  <platform-library name="Fluent" version="9.46.2" />
</resources>
```

## Fluent UI v8 controls

Fluent provides a migration path for applying v9 theme constructs when you use Fluent UI v8 controls in your component. Use the `createV8Theme` function included in the [Fluent's v8 to v9 migration package](https://www.npmjs.com/package/@fluentui/react-migration-v8-v9) to create a v8 theme based on v9 theme tokens, as shown in the following example:

```tsx
const theme = createV8Theme(
  context.fluentDesignLanguage.brand,
  context.fluentDesignLanguage.theme
);
return <ThemeProvider theme={theme}></ThemeProvider>;
```

## Non-Fluent UI controls

If your component doesn't use Fluent UI, you can take a dependency directly on the v9 theme tokens available through the `fluentDesignLanguage` context parameter. Use this parameter to get access to all [theme](reference/theming.md) tokens so it can reference any aspect of the theme to style itself.

```tsx
<span style={{ fontSize: context.fluentDesignLanguage.theme.fontSizeBase300 }}>
  {"Stylizing HTML with platform provided theme."}
</span>
```

## Custom theme providers

When your component requires styling that is different from the current theme of the app, create your own `FluentProvider` and pass your own set of theme tokens to be used by your component.

```tsx
<FluentProvider theme={context.fluentDesignLanguage.tokenTheme}>
  {/* your control */}
</FluentProvider>
```

## Sample controls

Examples for each of these use cases are available at [Modern Theming API control](./sample-controls/modern-theming-api-control.md).

## FAQ

This section contains frequently asked questions. If you have a question about this feature, use the **Feedback** for **This page** button at the bottom of this page to create a GitHub issue.

### Q: My control uses Fluent UI v9 and has a dependency on the platform libraries, but I don't want to utilize modern theming. How can I disable it for my component?

**A**: You can do this two different ways:

1. You can create your own component-level `FluentProvider`

   ```tsx
   <FluentProvider theme={customFluentV9Theme}>
     {/* your control */}
   </FluentProvider>
   ```

1. You can wrap your control inside `IdPrefixContext.Provider` and set your own `idPrefix` value. This prevents your component from getting theme tokens from the platform.

   ```tsx
   <IdPrefixProvider value="custom-control-prefix">
     <Label weight="semibold">This label is not getting Modern Theming</Label>
   </IdPrefixProvider>
   ```

### Q: Some of my Fluent UI v9 controls aren't getting styles

**A**: Fluent v9 controls that rely on the React Portal need to be rewrapped in the theme provider to ensure styling is properly applied. You can use `FluentProvider`.

### Q: How can I check if modern theming is enabled

**A**: You can check if tokens are available: `context.fluentDesignLanguage?.tokenTheme`. Or in model-driven applications you can check app settings: `context.appSettings.getIsFluentThemingEnabled()`.

## Related articles

[Theming (Power Apps component framework API reference)](../component-framework/reference/theming.md)   
[Modern Theming API control](./sample-controls/modern-theming-api-control.md)   
[Use modern themes in canvas apps (preview)](../../maker/canvas-apps/controls/modern-controls/modern-theming.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
