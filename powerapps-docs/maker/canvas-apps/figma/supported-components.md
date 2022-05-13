---
title: Controls supported by the UI kit (preview)
description: Learn about different controls supported by the canvas apps from Figma UI kit.
author: tapanm-msft
ms.topic: article
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 05/24/2022
ms.subservice: canvas-maker
ms.author: kaagar
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
---

# Controls supported by the UI kit (preview)

[This article is pre-release documentation and is subject to change.]

The [canvas apps from Figma UI kit](https://go.microsoft.com/fwlink/?linkid=2193981) supports certain controls. In this article, you'll learn about these controls.

For the latest information about the supported controls, and to see examples, you can also see the **Supported components** page inside the [canvas apps from Figma UI kit](https://go.microsoft.com/fwlink/?linkid=2193981).

> [!IMPORTANT]
> Don't rename controls, or change layers. Otherwise, the controls won't convert property in Power Apps.

## Screens

A [screen](../add-screen-context-variables.md) in canvas apps is the foundational base where you can place other controls such as data cards, labels, text inputs, and buttons. 

Screen inside the UI kit are available in two forms. **Phone**, and **Tablet**.

### Form screen

Use the form screen to fill out fields, edit or submit data to data sources such as Microsoft Dataverse, or SharePoint.

:::row:::
   :::column span="":::
      :::image type="content" source="media/screen-phone-form.png" alt-text="Form screen in the phone layout format.":::
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/screen-tablet-form.png" alt-text="Form screen in the tablet layout format.":::
   :::column-end:::
:::row-end:::

- Form screens are scrollable.
- Only use vertical or horizontal data cards on form screens.
- Don't mix vertical and vertical data cards on the same form.

### Scrollable screen

Use the scrollable screen when you want the content on the app to scroll and when you're not using a form. For example, a screen with lengthy explanatory content used to only display information without a form.

:::row:::
   :::column span="":::
      :::image type="content" source="media/screen-phone-scrollable.png" alt-text="Scrollable screen in the phone layout format.":::
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/screen-tablet-scrollable.png" alt-text="Scrollable screen in the tablet layout format.":::
   :::column-end:::
:::row-end:::

- Only use vertical or horizontal data cards on form screens.
- Don't add a form inside a scrollable screen.

### Non-scrollable screen

Use the non-scrollable screen when you want content on a screen, but you don't need that content to scroll. For example, when the content won't exceed a certain length.

:::row:::
   :::column span="":::
      :::image type="content" source="media/screen-phone-nonscrollable.png" alt-text="Non-scrollable screen in the phone layout format.":::
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/screen-tablet-nonscrollable.png" alt-text="Non-scrollable screen in the tablet layout format.":::
   :::column-end:::
:::row-end:::

- Don't add horizontal or vertical data cards on a non-scrollable screen.

## Vertical and horizontal data cards

Vertical and horizontal data cards are controls that vertically arrange themselves automatically on a form or a scrollable screen.

### Headers and dividers

:::row:::
   :::column span="":::
      :::image type="content" source="media/headers-dividers-horizontal.png" alt-text="Horizontal headers and dividers.":::
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/headers-dividers-vertical.png" alt-text="Vertical headers and dividers.":::
   :::column-end:::
:::row-end:::

### Text input, drop down, and combo box

:::row:::
   :::column span="":::
      :::image type="content" source="media/textinput-dropdown-combo-horizontal.png" alt-text="Horizontal text input, drop down, and combo box.":::
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/textinput-dropdown-combo-vertical.png" alt-text="Vertical text input, drop down, and combo box.":::
   :::column-end:::
:::row-end:::

### Toggle, check box, and radio

:::row:::
   :::column span="":::
      :::image type="content" source="media/toggle-checkbox-radio-horizontal.png" alt-text="Horizontal toggle, check box, and radio.":::
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/toggle-checkbox-radio-vertical.png" alt-text="Vertical toggle, check box, and radio.":::
   :::column-end:::
:::row-end:::

### Slider, rating

:::row:::
   :::column span="":::
      :::image type="content" source="media/slider-rating-horizontal.png" alt-text="Horizontal slider, rating.":::
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/slider-rating-vertical.png" alt-text="Vertical slider, rating.":::
   :::column-end:::
:::row-end:::

### Date picker

:::row:::
   :::column span="":::
      :::image type="content" source="media/date-picker-horizontal.png" alt-text="Horizontal date picker.":::
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/date-picker-vertical.png" alt-text="Vertical date picker.":::
   :::column-end:::
:::row-end:::

### List box

:::row:::
   :::column span="":::
      :::image type="content" source="media/list-box-horizontal.png" alt-text="Horizontal list box.":::
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/list-box-vertical.png" alt-text="Vertical list box.":::
   :::column-end:::
:::row-end:::

### Rich text

:::row:::
   :::column span="":::
      :::image type="content" source="media/rich-text-horizontal.png" alt-text="Horizontal rich text.":::
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/rich-text-vertical.png" alt-text="Vertical rich text.":::
   :::column-end:::
:::row-end:::

### Timer

:::row:::
   :::column span="":::
      :::image type="content" source="media/timer-horizontal.png" alt-text="Horizontal timer.":::
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/timer-vertical.png" alt-text="Vertical timer.":::
   :::column-end:::
:::row-end:::

## Control sizes, states and types

### Buttons

> [!NOTE]
> These controls can only be used on non-scrollable screens.

:::row:::
   :::column span="":::
      Sizes
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/button-size.png" alt-text="Button size.":::
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      States
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/button-states.png" alt-text="Button states.":::
   :::column-end:::
:::row-end:::

- If you want an outlined button with a stroke, set the stroke to Center in Figma since Power Apps only converts centered strokes.

### Labels

> [!NOTE]
> These controls can only be used on non-scrollable screens.

:::row:::
   :::column span="":::
      Sizes
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/label-size.png" alt-text="Label size.":::
   :::column-end:::
:::row-end:::

### Text inputs

> [!NOTE]
> These controls can only be used on non-scrollable screens.

:::row:::
   :::column span="":::
      Sizes
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/text-input-size.png" alt-text="Text input sizes.":::
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      States
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/text-input-state.png" alt-text="Text input states.":::
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      Types
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/text-input-type.png" alt-text="Text input types.":::
   :::column-end:::
:::row-end:::

### Combo boxes

> [!NOTE]
> These controls can only be used on non-scrollable screens.

:::row:::
   :::column span="":::
      Sizes
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/combo-box-sizes.png" alt-text="Combo box sizes.":::
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      States
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/combo-box-states.png" alt-text="Combo box states.":::
   :::column-end:::
:::row-end:::

### Drop downs

> [!NOTE]
> These controls can only be used on non-scrollable screens.

:::row:::
   :::column span="":::
      Sizes
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/drop-downs-sizes.png" alt-text="Drop downs sizes.":::
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      States
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/drop-downs-states.png" alt-text="Drop downs states.":::
   :::column-end:::
:::row-end:::

### Check boxes

> [!NOTE]
> These controls can only be used on non-scrollable screens.

:::row:::
   :::column span="":::
      Sizes
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/check-box-size.png" alt-text="Check box sizes.":::
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      States
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/check-box-state.png" alt-text="Check box states.":::
   :::column-end:::
:::row-end:::

### Radio buttons

> [!NOTE]
> These controls can only be used on non-scrollable screens.

:::row:::
   :::column span="":::
      Sizes
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/radio-button-size.png" alt-text="Radio button sizes.":::
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      States
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/radio-button-state.png" alt-text="Radio button states.":::
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      Types
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/radio-button-type.png" alt-text="Radio button types.":::
   :::column-end:::
:::row-end:::

- Keep all radio buttons and text with the same color. When converting into the app, Power Apps will use color of the first radio button for all remaining buttons. It won't recognize any other colors you may have used.

### Toggles

> [!NOTE]
> These controls can only be used on non-scrollable screens.

:::row:::
   :::column span="":::
      Sizes
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/toggle-size.png" alt-text="Toggle sizes.":::
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      States
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/toggles-state.png" alt-text="Toggle states.":::
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      Types
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/toggle-type.png" alt-text="Toggle types.":::
   :::column-end:::
:::row-end:::

### Date picker

> [!NOTE]
> These controls can only be used on non-scrollable screens.

:::row:::
   :::column span="":::
      Sizes
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/date-picker-size.png" alt-text="Date picker sizes.":::
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      States
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/date-picker-state.png" alt-text="Date picker states.":::
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      Types
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/date-picker-type.png" alt-text="Date picker types.":::
   :::column-end:::
:::row-end:::

### Slider

> [!NOTE]
> These controls can only be used on non-scrollable screens.

:::row:::
   :::column span="":::
      Sizes
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/slider-size.png" alt-text="Slider sizes.":::
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      States
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/slider-state.png" alt-text="Slider states.":::
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      Types
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/slider-type.png" alt-text="Slider types.":::
   :::column-end:::
:::row-end:::

### Ratings

> [!NOTE]
> These controls can only be used on non-scrollable screens.

:::row:::
   :::column span="":::
      Sizes
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/rating-size.png" alt-text="Ratings sizes.":::
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      States
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/rating-state.png" alt-text="Ratings states.":::
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      Types
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/rating-type.png" alt-text="Ratings types.":::
   :::column-end:::
:::row-end:::

- Keep all stars with the same color. When converting into the app, Power Apps will use color of the first star for all remaining stars. It won't recognize any other colors you may have used.

### List boxes

> [!NOTE]
> These controls can only be used on non-scrollable screens.

:::row:::
   :::column span="":::
      Sizes
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/list-box-size.png" alt-text="List box sizes.":::
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      States
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/list-box-state.png" alt-text="List box states.":::
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      Types
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/list-box-type.png" alt-text="List box types.":::
   :::column-end:::
:::row-end:::

### Rich text

> [!NOTE]
> These controls can only be used on non-scrollable screens.

:::row:::
   :::column span="":::
      Sizes
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/rich-text-size.png" alt-text="Rich text box sizes.":::
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      States
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/rich-text-state.png" alt-text="Rich text states.":::
   :::column-end:::
:::row-end:::

### Timer

> [!NOTE]
> These controls can only be used on non-scrollable screens.

:::row:::
   :::column span="":::
      Sizes
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/timer-size.png" alt-text="Timer sizes.":::
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      States
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/timer-state.png" alt-text="Timer states.":::
   :::column-end:::
:::row-end:::

## Content to ignore

Use these controls to make notes, comments, or miscellaneous content that doesn't need to render in the final app. The content will then be ignored when you convert the design in Power Apps.

:::image type="content" source="media/ignore-content.png" alt-text="Content to ignore.":::

## Images and rectangles

Images and rectangles will render as-is when the design is converted into an app.

:::row:::
   :::column span="":::
      Images
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/images.png" alt-text="Images.":::
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      Rectangles
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/rectangles.png" alt-text="Rectangles.":::
   :::column-end:::
:::row-end:::

- Only use rectangles with squared corners with corner radius set to zero since Power Apps can only convert rectangles with squared corners.

### See also

[Create a canvas app from Figma (preview)](create-app-from-figma.md)
