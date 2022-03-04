---
title: Add a scrolling screen to a canvas app
description: In Power Apps, create a screen that users can scroll to show more types of content than the screen can show at a time in a canvas app.
author: emcoope-msft
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 03/04/2022
ms.subservice: canvas-maker
ms.author: emcoope
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - emcoope-msft
---

# Add a scrolling screen to a canvas app

In a canvas app, create a screen that users can scroll to show different items. For example, create a phone app that shows data in several charts, which users can display if they scroll.

When you add multiple controls in a section, the controls maintain their relative positions within that section, regardless if it's a phone app or a tablet app. Note that the [screen size and orientation](set-aspect-ratio-portrait-landscape.md) may determine how the sections are arranged.  

[!INCLUDE [app-customization-requirements](../../includes/app-customization-requirements.md)]

## Create a scrolling screen

1. Select **New screen** below the top menu.

1. Select **Scrollable**.

    :::image type="content" source="media/add-scrolling-screen/new-scrollable-screen.png" alt-text="Select new screen and then choose scrollable screen type.":::

    A new scrollable screen is added to the app.

    :::image type="content" source="media/add-scrolling-screen/scrollable-screen.png" alt-text="A screenshot that shows the scrollable screen added to the app.":::

## Add controls

Scrollable screen includes one data card by default. Data cards help separate building blocks on the screen. To make screen scrollable with multiple controls, add more data cards. And then, add controls in data cards as required.

To add data cards, you can select **Add section** at the bottom of the scrollable screen.

:::image type="content" source="media/add-scrolling-screen/add-section-data-card.png" alt-text="Add section button highlighted on the scrollable screen on the canvas.":::

We'll start by adding controls on the data card available with the scrollable screen by default, and then add a new section that adds another data card. Once a new data card is available, we'll then add another control inside the new data card. Together, both data cards and the controls within the data cards would extend the default length of the screen, requiring the use of the scrolling ability of the screen.

> [!TIP]
> To learn more about data cards, see [Understand data cards](working-with-cards.md).

1. Select **+** (**Insert**) from the left-pane.

    :::image type="content" source="media/add-scrolling-screen/select-insert.png" alt-text="Alt text that describes the content of the image.":::

1. Expand **Charts**, and then select **Column chart**.

1. Resize the chart added on the screen to consume about two-thirds of the screen.

1. Reduce the size of the data card to the size of the added chart.

    :::image type="content" source="media/add-scrolling-screen/resize-data-card.png" alt-text="Resize the data card on the screen to consume two-thirds of the screen.":::

1. Select **Add section** on the screen to add another section.

    :::image type="content" source="media/add-scrolling-screen/second-data-card.png" alt-text="A new data card added to the screen.":::

1. Select **Insert** > **Charts** > **Line chart**.

1. Scroll down on the screen using the scroll bar on the right-side of the screen, and then select **Add section** to add a third data card.

1. Select **Insert** > **Input** > **Pen input**.

1. Resize the pen input control by increasing the width inside the data card.

    :::image type="content" source="media/add-scrolling-screen/resize-pen-input.png" alt-text="Pen input control resized to use more width on the screen.":::

1. Press **F5** on the keyboard to preview the app. Scroll down using the scroll bar to lower part of the screen.

    :::image type="content" source="media/add-scrolling-screen/preview-scrollable-screen.png" alt-text="Preview scrollable screen.":::

Now that you've demonstrated how to use scrollable screen, customize the app further as per your business requirements.

## Scrolling screen for forms

Since Power Apps uses data cards to create sections, [Display form and Edit form](controls/control-form-detail.md) controls can't be inserted on them. Nesting of such a combination of controls together may degrade the performance of the app. Hence, when using form controls, use layout containers such as a [vertical container](controls/control-vertical-container.md) control.

#### Examples

For Makers who want a basic "Scrollable Form", follow these steps:

1. In the insert pane under "Layout", select a "Vertical container".
1. Set the "Vertical Overflow" property of the container to "Scroll".
1. Add a View or Edit Form to the container.

For makers who wish to use X/Y positioning instead of the Layout Properties, they can get this effect by nesting a container inside of a layout container.

1. In the insert pane under "Layout", select a "Vertical container".
1. Set the "Vertical Overflow" property of the container to "Scroll".
1. In the insert pane under "Layout", select "Container".
1. In the properties of the inner container, uncheck the "Flexible Height" property.

You can then set the height of the inner container to a custom value, and the outer container will create a scrollbar for the overflow.

For more information on the Layout Containers and their capabilities, refer to the following documentation:
* [Building responsive canvas apps](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/build-responsive-apps)
* References for the [Horizontal](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/control-horizontal-container) and [Vertical](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/control-vertical-container) container controls
* [Broader information on responsive layouts](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/create-responsive-layout)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]