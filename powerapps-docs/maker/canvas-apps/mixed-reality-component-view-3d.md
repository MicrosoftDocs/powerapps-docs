---
title: Use the View in 3D component in Power Apps (Preview)
description: View 3D models in Power Apps.
author: anuitz
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 3/25/2021
ms.subservice: canvas-maker
ms.author: anuitz
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - anuitz
---

# View 3D content in canvas apps

Add 3D content to your canvas apps. Use the **View in 3D** component to rotate and zoom into the model with simple gestures.

You can display a single 3D model, or you can let the user select from a gallery [by connecting to a **Gallery** control](mixed-reality-component-view-3d-store.md).

:::image type="content" source="./media/augmented-overview/view-in-3d.png" alt-text="Photo showing a 3D object being viewed in a mobile device.":::


> [!IMPORTANT]
> Your 3D content must be in the .glb, .obj, or .stl file formats.  
> You can [convert your existing 3D models into the .glb file format](/dynamics365/mixed-reality/guides/3d-content-guidelines/) from a variety of 3D formats.

> [!TIP]
> The MR components in Power Apps leverage Babylon and Babylon React Native. As a result of this shared MR platform, 3D content that works in the [Babylon sandbox](https://sandbox.babylonjs.com/) should work in Power Apps. For troubleshooting and help, submit a ticket in the Admin Center for Mixed Reality, or [post a question on the Power Apps community forum](https://powerusers.microsoft.com/t5/Get-Help-with-Power-Apps/ct-p/PA_General) (be sure to tag it with "mixed reality".)


## Use the component

Insert the component into your app as you normally would for any other control or component.

With an app open for editing in [Power Apps Studio](https://create.powerapps.com):

1. Open the **Insert** tab.
2. Expand **Media**.
3. Select the component **View in 3D** to place it in the center of the app screen, or drag and drop it to position it anywhere on the screen.


    :::image type="content" source="./media/augmented-3d/augmented-3d-insert.png" alt-text="Insert the View in 3D component into the app.":::

See the [Load models with the View in 3D component](mixed-reality-component-view-3d-store.md) topic for details on how to connect existing and external models with URLs, as media attachments, or as encoded URIs.

You can modify the component with a number of properties.

### Properties

The following properties are on the component's **View in 3D** pane on the **Properties** and **Advanced** tabs.



:::image type="content" source="./media/augmented-3d/augmented-3d-viewer-controls.png" alt-text="Properties on the component's View in 3D pane.":::

Some properties are only available in the **Advanced** tab on the **View in 3D** pane.

Property | Description | Type | Location
- | - | - | -
Source | Data source that identifies the .glb file to display. The **View in 3D** component supports loading models from:<br/><ul><li>Publicly accessible, CORS-compliant URLs</li><li>Base64-encoded URIs</li><li>Attachments or media content accessed through data connectors</li></ul>See the [Loading external 3D models topic](mixed-reality-component-view-3d-store.md) for more details. | Not applicable | **Properties** (also in **Advanced**)
Alternative text | Text to be displayed if the model can't load, or if the app user hovers on the model. | String | **Properties** (also in **Advanced** as **AltText**)
Background fill | Set the background color for the component. | Color picker | **Properties** (also in **Advanced** as **BackgroundFill**, where it accepts RGBA or HTML hexadecimal color codes)
Pins(Items) | [Add pins to specific coordinates on the 3D model](mixed-reality-add-pins-3d-model.md). | Data table | **Properties** (also in **Advanced** and the formula bar as **Items**)
Show pins | Show the pins defined in **Pins(Items)**. | Toggle | **Properties** (also in **Advanced** as **ShowPins**)
Show reset button | Enables or disables the reset button, which resets the camera view onto the model. | Toggle | **Properties** (also in **Advanced** as **ShowReset**)
OnModelLoad | Behavior that is triggered when a model is loaded into the component. | Defined action | **Advanced**
OnChange | Behavior that is triggered when any property of the component is changed. | Defined action | **Advanced**
OnSelect | Behavior that is triggered when a pin is selected or the user focuses on the component | Defined action | **Advanced**

### Additional properties

**[DisplayMode](./controls/properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[Height](./controls/properties-size-location.md)** – The distance between a control's top and bottom edges.

**[TabIndex](./controls/properties-accessibility.md)** – Keyboard navigation order.

**[Visible](./controls/properties-core.md)** – Whether a control appears or is hidden.

**[Width](./controls/properties-size-location.md)** – The distance between a control's left and right edges.

**[X](./controls/properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (or the screen if there's no parent container).

**[Y](./controls/properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (or the screen if there's no parent container).



## Performance considerations

Having multiple instances of the **View in 3D** component on one screen can lead to poor performance, as each version of the component will try to load the 3D models at the same time. 



## Other mixed reality components

- View 3D content and images in the real world with the **[View in mixed reality](mixed-reality-component-view-mr.md)** component.
- Measure distance, area, and volume with the **[Measure in mixed reality](mixed-reality-component-measure-distance.md)** component.
- Create and view predefined 3D shapes with the **[View shape in mixed reality](mixed-reality-component-view-shape.md)** component.


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
