---
title: Theming (Power Apps component framework API reference) | Microsoft Docs
description: Provides the API for platform-provided modern theming.
author: jasongre
ms.author: jasongre
ms.date: 11/15/2023
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
  - JimDaly
---

# Theming

[!INCLUDE [theming-description](includes/theming-description.md)]

## Available for

Model-driven and canvas apps

## Syntax

`context.fluentDesignLanguage`

## Properties

### tokenTheme

Fluent v9 theme tokens provided by the platform.

**Type**: [Theme](https://github.com/microsoft/fluentui/blob/master/packages/tokens/src/types.ts)

### typographyTokens

Fluent v9 typography tokens provided by the platform.

**Type**: [TypographyStyles](https://github.com/microsoft/fluentui/blob/master/packages/tokens/src/global/typographyStyles.ts)

### brand

Fluent v9 BrandVariants based on which Fluent v9 theme was generated.

**Type**: [BrandVariants](https://github.com/microsoft/fluentui/blob/master/packages/tokens/src/types.ts)

### isDarkTheme

Indicates whether the current theme is dark or not.

**Type**: `boolean`

## Example

```tsx
const fluentDesignLanguage = props.context.fluentDesignLanguage;

return (
  <FluentProvider theme={props.theme}>
    <Label weight="semibold">{"Theming provided by the control."}</Label>
  </FluentProvider>
);

```

## Sample controls

[Modern Theming API control](../sample-controls/modern-theming-api-control.md)

### Related articles

[Use modern themes in canvas apps (preview)](../../../maker/canvas-apps/controls/modern-controls/modern-theming.md)   
[Power Apps component framework API reference](../reference/index.md)   
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
