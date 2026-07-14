---
title: Use the 3D object control in Power Apps
description: View 3D models in Power Apps.
author: anuitz
ms.topic: how-to
ms.custom: canvas
ms.reviewer: mduelae
ms.date: 02/15/2022
ms.subservice: canvas-maker
ms.author: anuitz
search.audienceType: 
  - maker
contributors:
  - mduelae
  - anuitz
---

# View 3D content in Power Apps

Easily add interactive 3D content to your canvas apps. You can [select from a gallery of 3D content](mixed-reality-component-view-3d-store.md) then rotate and zoom into the model with simple gestures.

:::image type="content" source="./media/augmented-overview/view-in-3d.png" alt-text="A photo of two phones side by side, both of which show a 3D model of a forklift viewed in two mobile apps.":::

> [!IMPORTANT]
> Your 3D content must be in the .glb, .obj, or .stl file formats. You can [convert your existing 3D models into the .glb file format](/dynamics365/mixed-reality/guides/3d-content-guidelines/) from a variety of 3D formats.

> [!TIP]
> The mixed reality (MR) controls in Power Apps use Babylon and Babylon React Native. Mixed reality content that works in the [Babylon sandbox](https://sandbox.babylonjs.com/) should work in Power Apps through this shared MR platform. If your content works in Babylon but not in Power Apps, ask a question in the [Power Apps Community Forum](https://powerusers.microsoft.com/t5/Get-Help-with-Power-Apps/ct-p/PA_General). (Tag it with "mixed reality.")

## Add 3D object control to an app screen

With your app open for [editing](edit-app.md) in [Power Apps Studio](https://create.powerapps.com):

1. Open the **Insert** tab and expand **Media**.
2. Select **3D object** to place the control in the app screen, or drag the control to the screen to position it more precisely.

## Key properties


Change the 3D content control's behavior and appearance using properties. Some properties are only available on the **Advanced** tab.

:::image type="content" source="./media/augmented-3d/augmented-3d-viewer-controls.png" alt-text="A 3D content control displayed next to the properties tab in Power Apps Studio.":::

| Property | Description | Type | Location |
| - | - | - | - |
| Source | Identifies the object file to display. The **3D object** control supports loading models from various sources. See [Loading external 3D models](mixed-reality-component-view-3d-store.md) for details. | Not applicable | Properties; Advanced: **Source** |
| Alternative text | Specifies the text to be displayed if the model can't load or if the user hovers over the model. | String | Properties; Advanced: **AltText** |
| Background fill | Sets the control's background color. | Color picker | Properties; Advanced: **BackgroundFill** (accepts RGBA or HTML hexadecimal color codes) |
| Pins(Items) | [Shows pins on the model at specific coordinates](mixed-reality-add-pins-3d-model.md), provided in a data source (**Items**). If *None*, no pins are shown. | Data table | Properties; Advanced: **Items** |
| Show pins | Shows the pins described in **Items**. | Boolean | Properties; Advanced: **ShowPins** |
| MaxPins | Specifies the maximum number of pins that can be shown on the model. | Integer | Advanced |
| PinsX | Specifies the location of pins on the X axis in 3D coordinate space. | Floating point number | Advanced |
| PinsY | Specifies the location of pins on the Y axis in 3D coordinate space. | Floating point number | Advanced |
| PinsZ | Specifies the location of pins on the Z axis in 3D coordinate space. | Floating point number | Advanced |
| Show reset button | Shows or hides a button that resets the model to its initial state. | Boolean | Properties; Advanced; **ShowReset** |
| OnModelLoad | Contains behavior formula that runs when a model is loaded.| Event | Advanced |
| OnChange | Contains behavior formula that runs when any property of the control is changed. | Event | Advanced |
| OnSelect | Contains behavior formula that runs when the user selects a pin or the control. | Event | Advanced |

## Additional properties

| Property | Description | Type | Location |
| - | - | - | - |
| ContentLanguage | Determines the display language of the control, if it's different from the language used in the app. | String | Advanced |
| [DisplayMode](./controls/properties-core.md) |  Determines whether the control allows user input (*Edit*), only displays data (*View*), or is disabled (*Disabled*). | Dropdown list | Advanced |
| Position | Places the upper-left corner of the control at the screen coordinates specified in *x* and *y*. | Floating point number | Properties; Advanced: **[X](./controls/properties-size-location.md)**, **[Y](./controls/properties-size-location.md)** |
| Size | Determines the size of the control using the pixel values provided in *Width* and *Height*. | Integer | Properties; Advanced: **[Width](./controls/properties-size-location.md)**, **[Height](./controls/properties-size-location.md)** |
| [TabIndex](./controls/properties-accessibility.md) | Specifies the order the control is selected if the user navigates the app using the Tab key. | Integer |  Advanced |
| [Tooltip](./controls/properties-core.md) | Determines the text to display when the user hovers over a pin. | String | Advanced |
| [Visible](./controls/properties-core.md) | Shows or hides the control. | Boolean | Properties; Advanced: **Visible** |

## Performance considerations

We recommend that you use one 3D control on a screen for the best user experience. Multiple instances of the **3D object** control on one screen will try to load their 3D models at the same time, which can severely degrade the performance of your app.

## Other mixed reality controls

- View 3D content and images in the real world with the **[View in mixed reality](mixed-reality-component-view-mr.md)** control.
- Measure distance, area, and volume with the **[Measure in mixed reality](mixed-reality-component-measure-distance.md)** control.
- Create and view predefined 3D shapes with the **[View shape in mixed reality](mixed-reality-component-view-shape.md)** control.
- Paint 3D lines or draw 3D arrows to specify an area or asset in your environment with the **[Markup in MR](markup-in-mixed-reality.md)** control.

### See also

[Create an app with 3D and mixed reality controls](how-to/build-view-in-mr-3d-apps.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
