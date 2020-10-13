---
title: Use the Measure in MR component in Power Apps (Preview)
description: Digitally measure distances and create areas and shapes in the real world with augmented reality features in Power Apps.
author: iaanw
manager: shellyha
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 5/4/2020
ms.author: iawilt
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Take measurements in mixed reality (Preview)

[!INCLUDE [cc-beta-prerelease-disclaimer.md](../../includes/cc-beta-prerelease-disclaimer.md)]

You can use the **Measure in MR** component in your app to let users measure distance, area, and volume. During measurement, you create two-dimensional and three-dimensional polygons that can be used to confirm how a certain-sized object would fit within a space.

The component creates a button in your app. When app users click the button, it shows a live camera feed of the device. App users can then identify a starting point and then individual points to measure from. The distances of measured segments are shown directly on the live camera feed.

An example of how the component works inside an app is shown in the following video:


> [!VIDEO https://www.microsoft.com/videoplayer/embed/RE4vyoW]


When the user exits the component, the measurements that were taken are captured in the **Measurements** and **MeasurementsDetailed** properties so they can be saved or stored.

Screenshots taken during the mixed reality experience are stored in the **Photos** property for viewing within the app.

To use the component, you need to [enable the mixed-reality features for each app](mixed-reality-overview.md#enable-the-mixed-reality-features-for-each-app) that you want to use it in.

Make sure to also [review the prerequisites for using mixed-reality components](mixed-reality-overview.md#prerequisites).

> [!TIP]
> The mixed-reality components work best in well-lit environments with flat-textured surfaces. When establishing tracking, point the device at the surface you would like to track and slowly pan the device from right to left in broad arm motions. If tracking fails, exit and enter the mixed-reality view to reset the tracking and try again.

## Use the component

Insert the component into your app as you normally would for any other button component.

With an app open for editing in [Power Apps Studio](https://create.powerapps.com):

1. Open the **Insert** tab.
2. Expand **Mixed reality**.
3. Select the component **Measure in MR** to place it in the center of the app screen, or drag and drop it to position it anywhere on the screen.

   > [!div class="mx-imgBorder"]
   > ![Select Measure in MR](./media/augmented-measure/augmented-measure.png "Select Measure in MR")

You can modify the component with a number of properties.

> [!NOTE]
> Your 3D content must be in the .glb file format. You can [convert your existing 3D models into the .glb file format](/dynamics365/mixed-reality/import-tool/) from a variety of 3D formats.


### Properties

The following properties are on the component's **Measure in MR** pane on the **Properties** and **Advanced** tabs.

> [!div class="mx-imgBorder"]
> ![The Measure in MR pane](./media/augmented-measure/augmented-measure-properties.png "The Measure in MR pane")

Note that some properties are only available under **More options** in the **Advanced** tab on the **Measure in MR** pane.

Property | Description | Type | Location
- | - | - | -
Text | Label for the button | String | **Properties** (also in **Advanced**)
Display type | Whether the button shows just an icon, text, or both | Drop-down selection | **Properties** (also in **Advanced**)
Unit of measurement | What unit the measurements should be shown and returned in | Drop-down selection | **Properties** (also in **Advanced**)
Measurement type | What type of measurement the user can make, whether point-to-point distance, a complete area, or a three-dimensional volume (area plus height or depth). | Drop-down selection | **Properties** (also in **Advanced**)
Measurements | Table containing the measured segments, composed of: <ul><li>Length - Number representing the length of the segment</li><li>Unit - String describing the unit of this measurement</li></ul> | String | Not applicable (output property only)
MeasurementsDetailed | Table describing the measured volumes and areas, composed of:<ul><li>Units - String describing the base unit of this measurement</li><li>Height - Number representing the height of the captured volume, or 0 if not a completed volume or 2D area</li><li>PathLength - Number representing the total length of the path</li><li>Segments - Table describing all segments in the given measurement object with the following properties:<ul><li>Distance - Number representing the total distance of a given segment in the given units of measure (for example, .52)</li><li>Direction - Vector describing the direction of the segment, normalized</li><li>X - Number specifying the X direction of the segment in world space (for example, 0.5)</li><li>Y - Number specifying the Y direction of the measurement in world space (typically 0)</li><li>Z - Number specifying the Z direction of the measurement in world space (for example, 0.5)</li></ul></li></li> | | Not applicable (output property only)
Photos | The photos captured during the mixed reality session | | Not applicable (output property only)

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
