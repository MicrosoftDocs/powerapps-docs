---
title: Test measurements in mixed reality
description: Learn about how to test measurements or fittings of objects with width, depth, and height using mixed reality components in canvas apps.
author: alex-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm-msft
ms.date: 11/17/2021
ms.subservice: canvas-maker
ms.author: altran
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - anuitz
  - alex-msft
---

# Test measurements in mixed reality

Using the [Measure in MR](mixed-reality-component-measure-distance.md) control, you can create a spatial test filter to validate whether an object with known width, depth, and height dimensions will fit in a space. This topic will guide you through creating a test app that you can use to validate the collected measurements, including:

- Inserting the **Measure In MR** component into an application to measure volumes.
- Setting up **Expected Measurements (Items)** to help users maintain context in the mixed reality experience.
- Creating a spatial test filter using the **Bounding Depth**, **Bounding Width**, and **Height** properties from the measurement outputs.

## Prerequisites

Create a blank canvas app using [Power Apps Studio](https://create.powerapps.com) by selecting **Phone layout** under **Blank app** inside **Start with a blank canvas or a template** section.

> [!TIP]
> - The MR components work best in well-lit environments with flat-textured surfaces. When establishing tracking, point the device at the surface you would like to track and slowly pan the device from right to left in broad arm motions. If tracking fails, exit and enter the MR view to reset the tracking and try again.
> - LIDAR-enabled devices will also result in better tracking.

## Set up minimum dimensions input fields

First, we’ll set up the dimensions to validate measurements.

1. Select the **Insert** tab, and insert three **Text labels** on the canvas.

    :::image type="content" source="media/augmented-measure-fit-test/fit-test-insert-text.png" alt-text="Screenshot showing how to insert a text label from the menu.":::

1. Change **Text** properties for the added labels to `"Minimum Width"`, `"Minimum Depth"`, and `"Minimum Height"`.

    :::image type="content" source="media/augmented-measure-fit-test/fit-test-completed-labels.png" alt-text="Screenshot showing placed text labels.":::

1. Select the **Insert** tab, insert three **Text Input** controls, and position them next to the three labels inserted in the previous step.

1. Rename Text Input controls to `minWidth`, `minDepth`, and `minHeight`.

1. For all three Text Input control added in the previous step, set the **Format** property to **Number** and set the **Default** property value to `1.0`.

    :::image type="content" source="media/augmented-measure-fit-test/fit-test-text-input.png" alt-text="Screenshot showing text inputs and properties.":::

## Insert and bind the Measure in MR component

Next, we’ll set up the **Measure in MR** component to allow users to capture measurements, and bind the output value we'll use to validate the measurement.

1. Select the **Insert** tab.

1. Expand **Mixed Reality**.

1. Select **Measure in MR**, and place it at the bottom of the application.

    :::image type="content" source="media/augmented-measure-fit-test/fit-test-insert-measure-in-mr.png" alt-text="Screenshot showing insertion of a Measure in MR control.":::

1. Update the following properties for **Measure in MR** component.

    | Property name | Value |
    | - | - |
    | Units of measurement | Feet or Meters |    
    | Measurement type | Volume |
    | Box Draw | True |

    :::image type="content" source="media/augmented-measure-fit-test/fit-test-units-and-type.png" alt-text="Screenshot showing Measurement Type and Units of Measurement property values.":::

1. Select the **Items** property from the upper-left side of the screen for the **Measure in MR** component, and update the formula to the following.

    ```powerapps-dot
    Table({label:"Test Volume"})
    ```

    This formula creates a table with the label of "Test Volume" as a single expected measurement output.

    :::image type="content" source="media/augmented-measure-fit-test/fit-test-formula-bar-items.png" alt-text="Screenshot showing formula bar settings for Items.":::

1. Set the **ItemsLabels** property of the **Measure in MR** component to `"lebel"`.

    :::image type="content" source="media/augmented-measure-fit-test/fit-test-advanced-properties-items.png" alt-text="Screenshot showing advanced property settings for Items and ItemsLabels.":::

1. Set the **OnMixedRealitySelect** property to the following formula.

    ```powerapps-dot
    Set(testVolume, LookUp(MeasureInMR1.Measurements, Label = "Test Volume"));
    ```

    This formula sets the "testVolume" variable with the value of the label looked up from the mixed reality component's measurements property.

    :::image type="content" source="media/augmented-measure-fit-test/fit-test-on-mixed-reality-select.png" alt-text="Screenshot showing property setting for OnMixedRealitySelect.":::

## Perform the measurement test and display the results

1. Select the **Insert** tab, and insert four **Text labels**.

    :::image type="content" source="media/augmented-measure-fit-test/fit-test-output-labels.png" alt-text="Screenshot showing four added text labels.":::

1. Set the **Text** property of the added labels as the following.

    1. First label:
    
        ```powerapps-dot
            If(IsBlankOrError(testVolume), "No Measurement captured",
            If(testVolume.Height >= Value(minHeight.Text) &&
            ((testVolume.BoundingWidth >= Value(minWidth.Text) && testVolume.BoundingDepth >= Value(minDepth.Text)) ||
            (testVolume.BoundingWidth >= Value(minDepth.Text) && testVolume.BoundingDepth >= Value(minWidth.Text))),
            "Fit Test Succeeded", "Fit Test Failed"))
        ```

        This formula determines whether the measurement tests succeeded, failed, or aren't captured depending on the height, width, and depth parameter values.

        :::image type="content" source="media/augmented-measure-fit-test/fit-test-spatial-test-formula.png" alt-text="Screenshot showing the formula for the spatial test predicate.":::

    1. Second label:
 
        ```powerapps-dot
        Concatenate("Bounding Width: ", Text(testVolume.BoundingWidth))
        ```

        This formula updates the label text and the relevant measurement parameter, in this case&mdash;"width".

    1. Third label:

        ```powerapps-dot
        Concatenate("Bounding Depth: ", Text(testVolume.BoundingDepth))
        ```

    1. Fourth label:

        ```powerapps-dot
          Concatenate("Bounding Height: ", Text(testVolume.Height))
        ```

    With all four label formulas updated, the screen should look like the following.

    :::image type="content" source="media/augmented-measure-fit-test/fit-test-completed-app.png" alt-text="Screenshot showing the final completed application.":::

## Test the app

Press **F5** on the keyboard, or select the preview button to run the app in preview mode. And then, select **Measure In MR** to get the labels populated with data.

You can verify that the bindings are working as expected by changing values in the three text input fields to check that the filter is updating properly.

The values for **Bounding Width** and **Bounding Depth** can be swapped when performing the test. After [saving and publishing](save-publish-app.md) the app, you can open it on a mixed reality-enabled device to test whether an object with the specified dimensions will fit within the bounds of any measurement captured.

## Filtering a data source

This sample application only tests for a single set of user specified dimensions. However, you can extend it to work as a filter for any data source by applying the formula as a **Filter** predicate.

For example, let's say that our app contains a reference to a Dataverse table named **Products** that includes three columns&mdash;**Width**, **Depth**, and **Height** (corresponding to each product's dimensions). To filter the collection to only those measurements that would fit within a measured volume, we can apply the following formula.

```powerapps-dot
If(IsBlankOrError(testVolume), Products,
    Filter(Products, testVolume.Height >= Height &&
        ((testVolume.BoundingWidth >= Width && testVolume.BoundingDepth >= Depth) ||
        (testVolume.BoundingWidth >= Depth && testVolume.BoundingDepth >= Width))))
```

### See also

- [View in 3D component](mixed-reality-component-view-3d.md)
- [Measure in MR component](mixed-reality-component-measure-distance.md)
- [View shape in MR component](mixed-reality-component-view-shape.md) 


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
