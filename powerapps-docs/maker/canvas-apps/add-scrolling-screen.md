---
title: Add a scrolling screen to a canvas app
description: In Power Apps, create a screen that users can scroll to show more types of content than the screen can show at a time in a canvas app.
author: emcoope-msft
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 03/07/2022
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

> [!TIP]
> To learn about working with forms, see [Understand canvas app forms](working-with-forms.md).

There are multiple different methods to configure scrolling with forms:

### Use Vertical Overflow property

This is the basic method of using a scrolling screen that has a form. To use a basic scrolling form:

1. Ensure you're using a blank screen, and not a scrollable screen.

1. Select **Insert** > **Layout**, and then select **Vertical container**.

1. From the right-side of the screen in the properties pane, select **Vertical Overflow** property drop-down, and choose **Scroll**.

    :::image type="content" source="media/add-scrolling-screen/vertical-overflow.png" alt-text="Vertical overflow property of the container set to Scroll.":::

1. Add the edit or display form with the required fields. When the list of fields exceeds the size of the container inside the screen, you'll be able to scroll inside the container using the scroll bar.

    :::image type="content" source="media/add-scrolling-screen/scrollable-vertical-container.png" alt-text="Scrollable vertical container using the Vertical Overflow property set to scroll having a display form.":::

### Use containers within Vertical container

For complex apps, you may consider adding containers within a vertical container control. And then, adjust the height of the form and the inner container as shown below.

1. Ensure you're using a blank screen, and not a scrollable screen.

1. Select **Insert** > **Layout**, and then select **Vertical container**.

1. From the right-side of the screen in the properties pane, select **Vertical Overflow** property drop-down, and choose **Scroll**.

1. Select **Insert** > **Layout**, and then select **Container**.

1. From the right-side of the screen in the properties pane, turn **Flexible height** property to **Off**.

    :::image type="content" source="media/add-scrolling-screen/flexible-height.png" alt-text="Flexible height property turned off for the container..":::

1. Add the edit or display form with the required fields.

1. To enable scrolling within the screen for the form, update the height of the container added in step 4, and the form.

    :::image type="content" source="media/add-scrolling-screen/x-y-positions.png" alt-text="Scrollable form that uses container and form height for scroll capability.":::

For more information about working with responsiveness of an app, see [Building responsive canvas apps](build-responsive-apps.md) and ]Responsive layouts](create-responsive-layout.md)

### See also

- [Horizontal container](controls/control-horizontal-container.md)
- [Vertical container](controls/control-vertical-container.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]