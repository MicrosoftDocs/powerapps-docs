---
title: Use the View in MR component in Power Apps (Preview)
description: View 3D models and 2D images in the real world with augmented reality features in Power Apps.
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

# View 3D content or images in the real word (Preview)

[!INCLUDE [cc-beta-prerelease-disclaimer.md](../../includes/cc-beta-prerelease-disclaimer.md)]

You can use the **View in MR** component in your app to let users see how a particular item might fit within a specified space.

The component creates a button in your app. When app users click the button, it overlays a selected 3D model (in the .glb file format) or image (in .jpg or .png file formats) onto the live camera feed of the device.

:::image type="content" source="./media/augmented-overview/view-in-mixed-reality.png" alt-text="Photo showing a 3D model of a forklift being overlaid onto the real world through a mobile device.":::

You can also take photos and [upload them to OneDrive](mixed-reality-take-upload-photos.md).

> [!IMPORTANT]
> Your 3D content must be in the .glb file format.  
> You can [convert your existing 3D models into the .glb file format](/dynamics365/mixed-reality/guides/3d-content-guidelines/) from a variety of 3D formats.

To use the component, you need to [enable the mixed reality (MR) features for each app](mixed-reality-overview.md#enable-the-mixed-reality-features-for-each-app) that you want to use it in.

Make sure to also [review the prerequisites for using MR components](mixed-reality-overview.md#prerequisites).

> [!TIP]
> The MR components work best in well-lit environments with flat-textured surfaces. When establishing tracking, point the device at the surface you would like to track and slowly pan the device from right to left in broad arm motions. If tracking fails, exit and enter the MR view to reset the tracking and try again.

## Use the component

Insert the component into your app as you normally would for any other button control or component.

With an app open for editing in [Power Apps Studio](https://create.powerapps.com):

1. Open the **Insert** tab.
2. Expand **Mixed reality**.
3. Select the component **View in MR** to place it in the center of the app screen, or drag and drop it to position it anywhere on the screen.

   ![Insert the View in MR component into the app](./media/augmented-view-mr/augmented-view-mr.png "Insert the View in MR component into the app")

You can modify the component with a number of properties.

### Properties

The following properties are on the component's **View in MR** pane on the **Properties** and **Advanced** tabs.

![Properties on the View in MR pane](./media/augmented-view-mr/augmented-view-mr-properties.png "Properties on the View in MR pane")

Some properties are only available under **More options** in the **Advanced** tab on the **View in MR** pane.

Property | Description | Type | Location
- | - | - | -
Text | Label for the button. | String | Properties (also in **Advanced**)
Display type | Whether the button shows just an icon, text, or both. | Drop-down selection | Properties (also in **Advanced**)
Source | Data source that identifies the .glb file to display. The **View in MR** component supports loading models from:<br/><ul><li>Publicly accessible, CORS-compliant URLs.</li><li>Base64-encoded URIs.</li><li>Attachments or media content accessed through data connectors.</li></ul><br/>For more information, see [Define where the 3D content is stored](mixed-reality-component-view-3d.md#define-where-the-3d-content-is-stored) in the **View in 3D** component's topic. | Not applicable | **Properties** (also in **Advanced**)
Object width | Width of the displayed image or 3D content. | Integer | **Properties** (also in **Advanced**)
Object height | Height of the displayed image or 3D content. | Integer | **Properties** (also in **Advanced**)
Object depth | The three-dimensional depth of the 3D content. | Integer | **Properties** (also in **Advanced**)
Units | The unit used for the object width, height, and depth fields. | Drop-down selection | **Properties** (also in **Advanced**)
Photos | The photos captured during the mixed reality session.<br/>You can [upload the mixed-reality photos to OneDrive and show them in a gallery](mixed-reality-take-upload-photos.md). | | Not applicable (output property only)

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

**[FontWeight](./controls/properties-text.md)** – The weight of the text in a control: **Bold**, **Semibold**, **Normal**, or **Lighter**.

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

**[TextAlignment](./controls/properties-text.md)** – The alignment of the text: **Center**, **Left**, **Right**, or Justify.

**[Tooltip](./controls/properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[VerticalAlign](./controls/properties-text.md)** – The location of text on a control in relation to the vertical center of that control: **Middle**, **Top**, or **Bottom**.

**[Visible](./controls/properties-core.md)** – Whether a control appears or is hidden.

**[Width](./controls/properties-size-location.md)** – The distance between a control's left and right edges.

**[X](./controls/properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (or the screen if there's no parent container).

**[Y](./controls/properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (or the screen if there's no parent container).

## Other mixed reality controls

- View 3D content with the **[View in 3D](mixed-reality-component-view-3d.md)** component.
- Measure distance, area, and volume with the **[Measure in mixed reality](mixed-reality-component-measure-distance.md)** component.
- Create and view predefined 3D shapes with the **[View shape in mixed reality](mixed-reality-component-view-shape.md)** component


[!INCLUDE[footer-include](../../includes/footer-banner.md)]