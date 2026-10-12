---
title: "Style components with modern theming | Microsoft Docs"
description: You can style your components based on the modern theme used in the app."
keywords: "Component Framework, code components, Power Apps controls"
author: jasongre
ms.author: jasongre
ms.date: 09/28/2026
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

# Style components with modern theming

Code components should look and feel consistent with the apps that host them. Power Apps uses Fluent theme tokens to provide component authors with the current app colors, typography, spacing, and other styling values. In model-driven apps, Power Apps adjusts supported Fluent spacing tokens to reflect the current display density. By consuming these tokens instead of using fixed styling values, components can respond to both the current app theme and, where available, display density.

Modern theming is available in canvas apps through the [Modern controls and themes](../../maker/canvas-apps/controls/modern-controls/overview-modern-controls.md) feature and in model-driven apps through the [modern, refreshed look](../../user/modern-fluent-design.md). [Display density](#make-spacing-respond-to-display-density) is available only in model-driven apps with the [header and navigation refresh](../../user/modern-fluent-design.md#wave-2-header-and-navigation-refresh) enabled.

The platform theme uses Fluent UI v9 tokens. Components can inherit these tokens through the platform's Fluent provider or consume them through the theming API in the following ways:

- [Fluent UI v9 controls](#fluent-ui-v9-controls)
- [Fluent UI v8 controls](#fluent-ui-v8-controls)
- [Non-Fluent UI controls](#non-fluent-ui-controls)
- [Custom theme providers](#custom-theme-providers)

## Fluent UI v9 controls

Wrapping Fluent UI v9 controls as a component is the easiest way to utilize modern theming because the modern theme is automatically applied to these controls. The only prerequisite is to ensure your component adds a dependency on the [React controls & platform libraries](react-controls-platform-libraries.md) as shown in the following section. This approach allows your component to use the same React and Fluent libraries as the platform, and therefore share the same React context that passes the theme tokens down to the component. Using the platform React and Fluent libraries is the recommended approach for the best performance and theming experience.

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

## Make spacing respond to display density

In model-driven apps, display density adjusts spacing to show more or less information on screen. Code components participate through the existing modern theming API. When display density is available, the platform supplies the resolved spacing values in the Fluent theme. Your component doesn't need to read the app setting or the user's personal preference.

Use the following tokens for custom layout spacing that responds to display density:

| Token | Example uses |
| --- | --- |
| `spacingVerticalS` | Vertical padding around a field, detail row, or similarly compact element |
| `spacingVerticalM` | Separation around a section title or a medium vertical gap |
| `spacingVerticalL` | Padding around a card or another large vertical gap |
| `spacingHorizontalL` | Inline padding around a card or another large horizontal gap |

Only these spacing tokens currently receive display-density adjustments. Other spacing tokens, typography, control dimensions, icons, and interactive target sizes don't change automatically.

If your component uses Fluent UI v9 and inherits the platform Fluent provider, reference the tokens in your styles:

```tsx
import { makeStyles, tokens } from "@fluentui/react-components";

const useStyles = makeStyles({
  card: {
    paddingBlock: tokens.spacingVerticalL,
    paddingInline: tokens.spacingHorizontalL,
  },
  row: {
    paddingBlock: tokens.spacingVerticalS,
    rowGap: tokens.spacingVerticalM,
  },
});
```

If your component owns its styles or uses non-Fluent elements, use the corresponding values from the current token theme:

```tsx
const tokenTheme = context.fluentDesignLanguage.tokenTheme;

const rowStyle = {
  paddingBlock: tokenTheme.spacingVerticalS,
  paddingInline: tokenTheme.spacingHorizontalL,
  rowGap: tokenTheme.spacingVerticalM,
};
```

Don't copy the pixel values for a density level or infer the selected density from token values. The platform resolves app settings, personal preferences, and density availability before supplying the theme.

Choose tokens according to their layout role and compare their normal values with your current layout. Replacing a fixed value with a token that has a different normal value can unintentionally change the component at the default **Comfortable** density.

Process the current theme whenever the component's `updateView` method runs. Don't retain the initial theme or spacing values for the lifetime of the component. Validate the component at **Comfortable**, **Cozy**, and **Compact** density, including after the theme or density changes.

> [!NOTE]
> Display density adjusts supported spacing values; it doesn't provide **Comfortable**, **Cozy**, or **Compact** as a public value to code components. Use the supplied token values directly rather than inferring a density level and conditionally applying styles. Components with fixed row heights, virtualized layouts, or other component-specific sizing might require extra design work beyond consuming spacing tokens.

## Sample controls

For examples of the modern theming approaches, see [Modern Theming API control](./sample-controls/modern-theming-api-control.md).

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
