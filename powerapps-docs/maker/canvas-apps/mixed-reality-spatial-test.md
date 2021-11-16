---
title: Test measurements in mixed reality
description: Learn about how to test measurements or fittings of objects with width, depth, and height using mixed reality components in canvas apps.
author: alex-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm-msft
ms.date: 8/26/2021
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
- Creating a spatial test filter using the **Bounding Width**, **Bounding Width**, and **Height** properties from the measurement outputs.

## Prerequisites

Create a blank canvas app using [Power Apps Studio](https://create.powerapps.com) by selecting **Phone layout** under **Blank app** inside **Start with a blank canvas or a template**.

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

Next, we’ll set up the **Measure in MR** component to allow users to capture measurements, and bind the output value we will use to validate fit.

1. Select the **Insert** tab.

1. Expand **Mixed Reality**.

1. Select **Measure in MR**, and place it at the bottom of the application.

    :::image type="content" source="media/augmented-measure-fit-test/fit-test-insert-measure-in-mr.png" alt-text="Screenshot showing insertion of a Measure in MR control.":::

1. Update the following properties for **Measure in MR** component.

    | Property name | Value |
    | - | - |
    | Units of Measurement | Feet or Meters |    
    | Measurement Type | Volume |
    | Box Draw | True |

    :::image type="content" source="media/augmented-measure-fit-test/fit-test-units-and-type.png" alt-text="Screenshot showing Measurement Type and Units of Measurement property values.":::

1. Select the **Items** property from the upper-left side of the screen for the **Measure in MR** component, and update the formula to the following.

    ```powerapps-dot
    `Table({label:"Test Volume"})`
    ```

    This formula creates a table with the label of "Test Volume" as a single expected measurement output.

Select the **ItemsLabels** property of the **Measure in MR** component to `"Value"`.

1. Define a table with a single expected measurement to provide an interaction hint during each user session. Under either the **Advanced** pane or the drop down menu on the **Formula Bar** at the top of the screen find the Items property and set it to: `Table({label:"Test Volume"})`
9. Also under the **Advanced** pane or the **Formula Bar** find the **ItemsLabels** property and set it to: `"Value"`

![Screenshot showing formula bar settings for Items.](./media/augmented-measure-fit-test/fit-test-formula-bar-items.png "Screenshot showing formula bar settings for Items.")

![Screenshot showing advanced property settings for Items and ItemsLabels.](./media/augmented-measure-fit-test/fit-test-advanced-properties-items.png "Screenshot showing advanced property settings for Items and ItemsLabels.")

10. Finally, in the **Advanced** pane set the OnMixedRealitySelect property to:
`Set(testVolume, LookUp(MeasureInMR1.Measurements, Label = "Test Volume"))`;

![Screenshot showing property setting for OnMixedRealitySelect.](./media/augmented-measure-fit-test/fit-test-on-mixed-reality-select.png "Screenshot showing property setting for OnMixedRealitySelect.")

## Perform fit test and display result
1. Open the **Insert** tab, and insert 4 more **Text labels**.

![Screenshot showing four added text labels.](./media/augmented-measure-fit-test/fit-test-output-labels.png "Screenshot showing four added text labels.")

2. Set the first label’s **Text** property to:
```
If(IsBlankOrError(testVolume), "No Measurement captured",
    If(testVolume.Height >= Value(minHeight.Text) &&
        ((testVolume.BoundingWidth >= Value(minWidth.Text) && testVolume.BoundingDepth >= Value(minDepth.Text)) ||
        (testVolume.BoundingWidth >= Value(minDepth.Text) && testVolume.BoundingDepth >= Value(minWidth.Text))),
    "Fit Test Succeeded", "Fit Test Failed"))
```

![Screenshot showing the formula for the spatial test predicate.](./media/augmented-measure-fit-test/fit-test-spatial-test-formula.png "Screenshot showing the formula for the spatial test predicate.")

3. Set the text property for the second label to:
 `Concatenate("Bounding Width: ", Text(testVolume.BoundingWidth))`
4. Set the text property for the third label to:
 `Concatenate("Bounding Depth: ", Text(testVolume.BoundingDepth))`
5. Set the text property for the fourth label to:
 `Concatenate("Bounding Height: ", Text(testVolume.Height))`

![Screenshot showing the final completed application.](./media/augmented-measure-fit-test/fit-test-completed-app.png "Screenshot showing the formula for the spatial test predicate.")

## Testing the application
Now, enter preview mode and click on the MeasureInMR button. You should see the labels above get populated with data. You can test that the bindings are working as expected by changing values in the three text input fields to verify that the filter is updating properly. The values for **Bounding Width** and **Bounding Depth** should be interchangeable and may be swapped when performing the test. After saving and publishing the application you can open it on a Mixed Reality enabled device to test whether an object with the specified dimensions will fit within the bounds of any measurement captured.

## Filtering a data source
This sample application only tests for a single set of user specified dimensions, but could be expanded to work as a filter for any data source by applying the formula as a **Filter** predicate. For example, let's say our app contains a reference to a Dataverse table named **Products** which includes three columns **Width**, **Depth**, and **Height** corresponding to each product's dimensions. To filter the collection to only those that would fit within a measured volume we can apply the following formula:
```
If(IsBlankOrError(testVolume), Products,
    Filter(Products, testVolume.Height >= Height &&
        ((testVolume.BoundingWidth >= Width && testVolume.BoundingDepth >= Depth) ||
        (testVolume.BoundingWidth >= Depth && testVolume.BoundingDepth >= Width))))
```

## Other mixed-reality controls

- View 3D content with the **[View in 3D](mixed-reality-component-view-3d.md)** component.
- Measure distance, area, and volume with the **[Measure in mixed reality](mixed-reality-component-measure-distance.md)** component.
- Create and view predefined 3D shapes with the **[View shape in mixed reality](mixed-reality-component-view-shape.md)** component


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
