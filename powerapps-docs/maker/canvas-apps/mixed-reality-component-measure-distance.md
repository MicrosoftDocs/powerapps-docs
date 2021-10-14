---
title: Use the Measure in MR component in Power Apps (Preview)
description: Digitally measure distances and create areas and shapes in the real world with augmented reality features in Power Apps.
author: iaanw
manager: shellyha
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 3/25/2021
ms.subservice: canvas-maker
ms.author: iawilt
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - iaanw
---
# Take measurements in mixed reality

You can use the **Measure in MR** component in your app to let users measure distance, area, and volume. During measurement, you create two-dimensional and three-dimensional polygons that can be used to confirm how a certain-sized object would fit within a space.

The component creates a button in your app. When app users click the button, it shows a live camera feed of the device. App users can then identify a starting point and then individual points to measure from. The distances of measured segments are shown directly on the live camera feed.


:::image type="content" source="./media/augmented-overview/measure-in-mixed-reality.png" alt-text="Photo showing a corner between two construction walls being measured with a mobile device.":::

When the user exits the component, the measurements that were taken are captured in the **Measurements** and **MeasurementsDetailed** properties so they can be saved or stored.

Screenshots taken during the mixed reality experience are stored in the **Photos** property for viewing within the app.


> [!TIP]
> The mixed-reality components work best in well-lit environments with flat-textured surfaces. When establishing tracking, point the device at the surface you would like to track and slowly pan the device from right to left in broad arm motions. If tracking fails, exit and enter the mixed-reality view to reset the tracking and try again.  
>
> LIDAR-enabled devices will also result in better tracking.

## Use the component

Insert the component into your app as you normally would for any other button component.

With an app open for editing in [Power Apps Studio](https://create.powerapps.com):

1. Open the **Insert** tab.
2. Expand **Mixed reality**.
3. Select the component **Measure in MR** to place it in the center of the app screen, or drag and drop it to position it anywhere on the screen.

:::image type="content" source="./media/augmented-measure/augmented-measure.png" alt-text="Select Measure in MR.":::


You can modify the component with a number of properties.


### Properties

The following properties are on the component's **Measure in MR** pane on the **Properties** and **Advanced** tabs.

:::image type="content" source="./media/augmented-measure/augmented-measure-properties.png" alt-text="The Measure in MR pane.":::

Note that some properties are only available under **More options** in the **Advanced** tab on the **Measure in MR** pane.

Property | Description | Type | Location
| - | - | - | -
Unit of measurement | What unit the measurements should be shown and returned in. | Drop-down selection | **Properties** (also in **Advanced**)
Measurement type | What type of measurement the user can make, whether point-to-point distance, a complete area, or a three-dimensional volume (area plus height or depth). | Drop-down selection | **Properties** (also in **Advanced**)
Expected Measurements (Items) | Data source (table) that lists a predefined set of measurements that you want the user to capture during a single session. You can map the labels you want to use for each measurement by using the _ItemsLabels_ property. | Not applicable | **Properties** (also in **Advanced**)
ItemsLabels  | A column in _Items_ with the strings you want to use as the labels for the measurements you want users to capture. | ColumnName | **Advanced**
Measurements | Table describing the measured distances, volumes and areas, composed of:<ul><li>Label - String that identifies the given measurement</li><li>Id - Number that uniquely identifies this measurement</li><li>Units - String describing the base unit of this measurement</li><li>Height - Number representing the height of the captured volume, or 0 if not a completed volume or 2D area</li><li>Length - Number representing the total length of the perimeter or path of the measurement </li><li>BoundingWidth - Number representing minimum width in units that bounds the shape </li><li>BoundingDepth - Number representing the minimum depth in units that bounds the shape  </li><li>Area - Number representing the estimated area of the enclosed shape in units squared </li><li>Volume - Number representing the estimated volume of the enclosed shape in units cubed </li><li>Segments - Table describing all segments in the given measurement object with the following properties:<ul><li>Distance - Number representing the total distance of a given segment in the given units of measure (for example, .52)</li><li>Direction - Vector describing the direction of the segment, normalized</li><li>X - Number specifying the X direction of the segment in world space (for example, 0.5)</li><li>Y - Number specifying the Y direction of the measurement in world space (typically 0)</li><li>Z - Number specifying the Z direction of the measurement in world space (for example, 0.5)</li></ul></li></ul> | Table | Not applicable (output property only)
Photos | The photos captured during the mixed reality session.<br/>You can [upload the mixed-reality photos to OneDrive and show them in a gallery](mixed-reality-take-upload-photos.md). | Not applicable | Not applicable (output property only)
OnMixedRealitySelect | Behavior that is triggered when exiting the MR experience with new results. | Defined action | **Advanced**
OnChange | Behavior that is triggered when any property on the button is changed. | Defined action | **Advanced**

### Additional properties

**[BorderColor](./controls/properties-color-border.md)** – The color of a control's border.

**[BorderStyle](./controls/properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](./controls/properties-color-border.md)** – The thickness of a control's border.

**[Color](./controls/properties-color-border.md)** – The color of text in a control.

**[DisplayMode](./controls/properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).


**[DisabledBorderColor](./controls/properties-color-border.md)** – The color of a control's border if the control's **[DisplayMode](./controls/properties-core.md)** property is set to **Disabled**.

**[DisabledColor](./controls/properties-color-border.md)** – The color of text in a control if its **[DisplayMode](./controls/properties-core.md)** property is set to **Disabled**.

**[DisabledFill](./controls/properties-color-border.md)** – The background color of a control if its **[DisplayMode](./controls/properties-core.md)** property is set to **Disabled**.

**[FillColor](./controls/properties-color-border.md)** – The background color of a control.

**[Font](./controls/properties-text.md)** – The name of the family of fonts in which text appears.

**[FontStyle](./controls/properties-text.md)** – The style of the text in the component: **None**, **Strikethrough**, **Underline**, or **Italic**.

**[FontSize](./controls/properties-text.md)** – The font size of the text that appears on a control.

**[FontWeight](./controls/properties-text.md)** – The weight of the text in a control: **Bold**, **Semibold**, **Normal**, or **Lighter**

**[Height](./controls/properties-size-location.md)** – The distance between a control's top and bottom edges.

**[HoverBorderColor](./controls/properties-color-border.md)** – The color of a control's border when the user keeps the mouse pointer on that control.

**[HoverColor](./controls/properties-color-border.md)** – The color of the text in a control when the user keeps the mouse pointer on it.

**[HoverFill](./controls/properties-color-border.md)** – The background color of a control when the user keeps the mouse pointer on it.

**[PaddingBottom](./controls/properties-size-location.md)** – The distance between text in a control and the bottom edge of that control.

**[PaddingLeft](./controls/properties-size-location.md)** – The distance between text in a control and the left edge of that control.

**[PaddingRight](./controls/properties-size-location.md)** – The distance between text in a control and the right edge of that control.

**[PaddingTop](./controls/properties-size-location.md)** – The distance between text in a control and the top edge of that control.

**[PressedBorderColor](./controls/properties-color-border.md)** – The color of a control's border when the user taps or clicks that control.

**[PressedColor](./controls/properties-color-border.md)** – The color of text in a control when the user taps or clicks that control.

**[PressedFill](./controls/properties-color-border.md)** – The background color of a control when the user taps or clicks that control.

**[TabIndex](./controls/properties-accessibility.md)** – Keyboard navigation order.

**[TextAlignment](./controls/properties-text.md)** – The alignment of the text: **Center**, **Left**, **Right**, or **Justify**

**[Tooltip](./controls/properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[VerticalAlign](./controls/properties-text.md)** – The location of text on a control in relation to the vertical center of that control: **Middle**, **Top**, or **Bottom**

**[Visible](./controls/properties-core.md)** – Whether a control appears or is hidden.

**[Width](./controls/properties-size-location.md)** – The distance between a control's left and right edges.

**[X](./controls/properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (or the screen if there's no parent container).

**[Y](./controls/properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (or the screen if there's no parent container).

## Other mixed reality components

- View 3D content with the **[View in 3D](mixed-reality-component-view-3d.md)** component.
- View images and 3D content in the real world with the **[View in mixed reality](mixed-reality-component-view-mr.md)** component.
- Create and view predefined 3D shapes with the **[View shape in mixed reality](mixed-reality-component-view-shape.md)** component


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
