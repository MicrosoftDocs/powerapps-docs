---
title: Components supported by the UI kit
description: Learn about different components supported by the Create Apps from Figma UI Kit.
author: mduelae
ms.topic: article
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 05/24/2022
ms.subservice: canvas-maker
ms.author: kaagar
search.audienceType: 
  - maker
contributors:
  - mduelae
---

# Components supported by the UI kit

[This article is pre-release documentation and is subject to change.]

The [Create Apps from Figma UI Kit](https://go.microsoft.com/fwlink/?linkid=2193981) supports certain components. In this article, you'll learn about these components.

For the latest information about the supported components and to view detailed examples, you can visit the **Supported components** page inside the [Create Apps from Figma UI Kit](https://go.microsoft.com/fwlink/?linkid=2193981).

> [!IMPORTANT]
> Don't rename components or change layers. Otherwise, the components won't convert property in Power Apps.

## Scrollable sections

A scrollable section is a section on a screen. If content extends beyond the section, it will still be accessible when the user scrolls.

The scrollable sections inside the UI kit are available in two different formats: **Phone**, and **Tablet**.

### Form

Use a Form section when you want to have users fill out fields and submit data.

In Power Apps, this section will be scrollable.

:::image type="content" source="media/form.png" alt-text="Form screen in the tablet and phone layout formats.":::

- Place only vertical or horizontal data card components in form section.
- Don't mix and match vertical and horizontal data cards.
- Don't use base components in form frames.

### Container (vertical)

Use the Container (vertical) sections when you want the content to scroll. For example, if you need a section of lengthy explanatory content.

> [!TIP]
> You can also add a small form inside a Container (vertical) section.

:::image type="content" source="media/container.png" alt-text="Vertical container in the tablet and phone layout formats.":::

- Use base components and forms in container frames.
- Don't place vertical or horizontal card components in Container (vertical) section.

## Vertical and horizontal data cards

Vertical and horizontal [data cards](../working-with-cards.md) are components that arrange themselves automatically on a form.

> [!NOTE]
> Ensure all data cards are placed directly inside a form component. Data cards can't be used outside of a form.

### Headers and dividers

:::image type="content" source="media/headers-dividers-horizontal.png" alt-text="Horizontal headers and dividers.":::

### Text input, drop down, and combo box

:::image type="content" source="media/textinput-dropdown-combo-horizontal.png" alt-text="Horizontal text input, drop down, and combo box.":::

### Toggle, check box, and radio

:::image type="content" source="media/toggle-checkbox-radio-horizontal.png" alt-text="Horizontal toggle, check box, and radio.":::

### Slider, rating

:::image type="content" source="media/slider-rating-horizontal.png" alt-text="Horizontal slider, rating.":::

### Date picker

:::image type="content" source="media/date-picker-horizontal.png" alt-text="Horizontal date picker.":::

### List box

:::image type="content" source="media/list-box-horizontal.png" alt-text="Horizontal list box.":::

### Rich text

:::image type="content" source="media/rich-text-horizontal.png" alt-text="Horizontal rich text.":::

### Timer

:::image type="content" source="media/timer-horizontal.png" alt-text="Horizontal timer.":::

## Component sizes, states and types

### Button sizes

:::image type="content" source="media/button-size.png" alt-text="Button size.":::

### Button states

:::image type="content" source="media/button-states.png" alt-text="Button states.":::

- If you want an outlined button with a stroke, set the stroke to Center in Figma since Power Apps only converts centered strokes.

### Labels sizes

:::image type="content" source="media/label-size.png" alt-text="Label size.":::

> [!NOTE]
> Use only one font and font size within a text label. If you want to use more than one font or font size within a text label, then make separate labels with those variations. Also, ensure that the text for the label doesn't extend beyond the bounding box, or it won't convert properly.

### Text input sizes

:::image type="content" source="media/text-input-size.png" alt-text="Text input sizes.":::

### Text input states

:::image type="content" source="media/text-input-state.png" alt-text="Text input states.":::

### Text input types

:::image type="content" source="media/text-input-type.png" alt-text="Text input types.":::

### Combo box sizes

:::image type="content" source="media/combo-box-sizes.png" alt-text="Combo box sizes.":::

### Combo box states

:::image type="content" source="media/combo-box-states.png" alt-text="Combo box states.":::

### Drop down sizes

:::image type="content" source="media/drop-downs-sizes.png" alt-text="Drop downs sizes.":::

### Drop down states

:::image type="content" source="media/drop-downs-states.png" alt-text="Drop downs states.":::

### Check box sizes

:::image type="content" source="media/check-box-size.png" alt-text="Check box sizes.":::

### Check box states

:::image type="content" source="media/check-box-state.png" alt-text="Check box states.":::

### Radio button sizes

:::image type="content" source="media/radio-button-size.png" alt-text="Radio button sizes.":::

### Radio button states

:::image type="content" source="media/radio-button-state.png" alt-text="Radio button states.":::

### Radio button types

:::image type="content" source="media/radio-button-type.png" alt-text="Radio button types.":::

- Keep all radio buttons and text the same color. When converting into an app, Power Apps will use the color of the first radio button for all the remaining buttons. It won't recognize any other colors you may have used.

### Toggle sizes

:::image type="content" source="media/toggle-size.png" alt-text="Toggle sizes.":::

### Toggle states

:::image type="content" source="media/toggles-state.png" alt-text="Toggle states.":::

### Toggle types

:::image type="content" source="media/toggle-type.png" alt-text="Toggle types.":::

### Date picker sizes

:::image type="content" source="media/date-picker-size.png" alt-text="Date picker sizes.":::

### Date picker states

:::image type="content" source="media/date-picker-state.png" alt-text="Date picker states.":::

### Date picker types

:::image type="content" source="media/date-picker-type.png" alt-text="Date picker types.":::

### Slider sizes

:::image type="content" source="media/slider-size.png" alt-text="Slider sizes.":::

### Slider states

:::image type="content" source="media/slider-state.png" alt-text="Slider states.":::

### Slider types

:::image type="content" source="media/slider-type.png" alt-text="Slider types.":::

### Rating sizes

:::image type="content" source="media/rating-size.png" alt-text="Ratings sizes.":::

### Rating states

:::image type="content" source="media/rating-state.png" alt-text="Ratings states.":::

### Rating types

:::image type="content" source="media/rating-type.png" alt-text="Ratings types.":::

- Keep all stars the same color while designing in Figma. When converting into an app, Power Apps will use the color of the first star for all the remaining stars. It won't recognize any other colors you may have used.

### List box sizes

:::image type="content" source="media/list-box-size.png" alt-text="List box sizes.":::

### List box states

:::image type="content" source="media/list-box-state.png" alt-text="List box states.":::

### List box types

:::image type="content" source="media/list-box-type.png" alt-text="List box types.":::

### Rich text sizes

:::image type="content" source="media/rich-text-size.png" alt-text="Rich text box sizes.":::

### Rich text states

:::image type="content" source="media/rich-text-state.png" alt-text="Rich text states.":::

### Timer sizes

:::image type="content" source="media/timer-size.png" alt-text="Timer sizes.":::

### Timer states

:::image type="content" source="media/timer-state.png" alt-text="Timer states.":::

## Content to ignore

Use these components to make notes, comments, or miscellaneous content that doesn't need to render in the final app. The content will then be ignored when you convert the design in Power Apps.

:::image type="content" source="media/ignore-content.png" alt-text="Content to ignore.":::

## Images and rectangles

Images and rectangles will render as-is when the design is converted into an app.

### Images

:::image type="content" source="media/images.png" alt-text="Images.":::

### Rectangles

:::image type="content" source="media/rectangles.png" alt-text="Rectangles.":::

- Only use rectangles with squared corners since Power Apps can only convert rectangles with squared corners. In Figma, this means the corner radius must be set to zero.

### See also

- [Create a canvas app from Figma](create-app-from-figma.md)
