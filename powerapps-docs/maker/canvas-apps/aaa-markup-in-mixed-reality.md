# Markup in mixed reality

You can use the **Markup in MR** component in your app to allow users to give guidance in their environment. Place arrows, add drawings, and take photos of your markup.

The component creates a button in your app. When app users click the button, it shows a live camera feed of the device. App users can then identify points of interest to begin inking or adding arrows directly on the object. Ink and arrows will scale appropriately depending on the distance from the objects.

When the user exits the component, if media was taken, it can be found in the Photo properties.

Tip: The mixed-reality (MR) controls work best in well-lit environments.

# How it works

Once the user presses the Markup in MR button, they will be prompted to move their phone side-to-side for better object or area detection.

After an object or area has been detected the user may make use of the markup toolbar.

## Adding an arrow

To position the arrow:

-   Make sure the arrow is selected in the markup toolbar.

-   Move your device around to position the dot on the object or area you want to highlight

-   Tap to place the ghost arrow on your device screen

-   To rotate the arrow, tap and drag the arrow in a circular motion (360 degrees)

## Inking

To determine where you start drawing:

-   Make sure the ink pen is selected in the markup toolbar.

-   Tap and drag on the screen to start drawing

# Use the component.

Insert the component into your app as you normally would for any other button component.

With an app open for editing in [<u>Power Apps Studio</u>](https://create.powerapps.com/):

1.  Open the **Insert** tab.

2.  Expand **Mixed reality**.

3.  Select the component **Markup in MR** to place it in the center of the app screen or drag and drop it to position it anywhere on the screen.

![Graphical user interface  application Description automatically generated](media/image1.png)

You can modify the component with several properties.

# Properties

Note that some properties are only available under **More options** in the **Advanced** tab on the **Markup in MR** pane.

![Graphical user interface  application Description automatically generated](media/image2.png)

| **Property** | **Description** | **Type** | **Location** |
|-------------------------|-------------------------|-------------------------|-------------------------|
| Photos | The photos captured during the mixed reality session.<br /></br>You can [upload the mixed-reality photos to OneDrive and show them in a gallery](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/mixed-reality-take-upload-photos). | Not Applicable | Not Applicable (Output property only) |
| OnMixedRealitySelect | Behavior that is triggered when exiting the MR experience with new results. | Defined Action | Advanced |
| OnChange | Behavior that is triggered when any property on the button is changed. | Defined Action | Advanced |


|     |
|-----|
|     |

## Additional properties

| **Property**                                                                                                             | **Description**                                                                                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BorderColor**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/properties-color-border)         | The color of a control's border.                                                                                                                                                           |
| [**BorderStyle**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/properties-color-border)         | Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.                                                                                                              |
| [**BorderThickness**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/properties-color-border)     | The thickness of a control's border.                                                                                                                                                       |
| [**Color**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/properties-color-border)               | The color of text in a control.                                                                                                                                                            |
| [**DisplayMode**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/properties-core)                 | Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).                                                                            |
| [**DisabledBorderColor**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/properties-color-border) | The color of a control's border if the control's [**DisplayMode**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/properties-core) property is set to **Disabled**. |
| [**DisabledColor**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/properties-color-border)       | The color of text in a control if its [**DisplayMode**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/properties-core) property is set to **Disabled**.            |
| [**DisabledFill**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/properties-color-border)        | The background color of a control if its [**DisplayMode**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/properties-core) property is set to **Disabled**.         |
| [**FillColor**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/properties-color-border)           | The background color of a control.                                                                                                                                                         |
| [**Font**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/properties-text)                        | The name of the family of fonts in which text appears.                                                                                                                                     |
| [**FontStyle**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/properties-text)                   | The style of the text in the component: **None**, **Strikethrough**, **Underline**, or **Italic**.                                                                                         |
| [**FontSize**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/properties-text)                    | The font size of the text that appears on a control.                                                                                                                                       |
| [**FontWeight**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/properties-text)                  | The weight of the text in a control: **Bold**, **Semibold**, **Normal**, or **Lighter**                                                                                                    |
| [**Height**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/properties-size-location)             | The distance between a control's top and bottom edges.                                                                                                                                     |
| [**HoverBorderColor**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/properties-color-border)    | The color of a control's border when the user keeps the mouse pointer on that control.                                                                                                     |
| [**HoverColor**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/properties-color-border)          | The color of the text in a control when the user keeps the mouse pointer on it.                                                                                                            |
| [**HoverFill**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/properties-color-border)           | The background color of a control when the user keeps the mouse pointer on it.                                                                                                             |
| [**PaddingBottom**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/properties-size-location)      | The distance between text in a control and the bottom edge of that control.                                                                                                                |
| [**PaddingLeft**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/properties-size-location)        | The distance between text in a control and the left edge of that control.                                                                                                                  |
| [**PaddingRight**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/properties-size-location)       | The distance between text in a control and the right edge of that control.                                                                                                                 |
| [**PaddingTop**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/properties-size-location)         | The distance between text in a control and the top edge of that control.                                                                                                                   |
| [**PressedBorderColor**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/properties-color-border)  | The color of a control's border when the user taps or clicks that control.                                                                                                                 |
| [**PressedColor**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/properties-color-border)        | The color of text in a control when the user taps or clicks that control.                                                                                                                  |
| [**PressedFill**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/properties-color-border)         | The background color of a control when the user taps or clicks that control.                                                                                                               |
| [**TabIndex**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/properties-accessibility)           | Keyboard navigation order.                                                                                                                                                                 |
| [**TextAlignment**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/properties-text)               | The alignment of the text: **Center**, **Left**, **Right**, or **Justify**                                                                                                                 |
| [**Tooltip**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/properties-core)                     | Explanatory text that appears when the user hovers over a control.                                                                                                                         |
| [**VerticalAlign**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/properties-text)               | The location of text on a control in relation to the vertical center of that control: **Middle**, **Top**, or **Bottom**                                                                   |
| [**Visible**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/properties-core)                     | Whether a control appears or is hidden.                                                                                                                                                    |
| [**Width**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/properties-size-location)              | The distance between a control's left and right edges.                                                                                                                                     |
| [**X**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/properties-size-location)                  | The distance between the left edge of a control and the left edge of its parent container (or the screen if there's no parent container).                                                  |
| [**Y**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/controls/properties-size-location)                  | The distance between the top edge of a control and the top edge of the parent container (or the screen if there's no parent container).                                                    |

## Output properties

| **Property** | **Description**                                                                                                                                                                                                                                 | **Type**       |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| Photos       | Collects the photos captured during the mixed reality session. You can [upload the mixed-reality photos to OneDrive and show them in a gallery](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/mixed-reality-take-upload-photos). | Not applicable |

# Other Mixed Reality Components

-   View 3D content with the [<u>View in 3D</u>](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/mixed-reality-component-view-3d) component.

-   View images and 3D content in the real world with the [<u>View in mixed reality</u>](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/mixed-reality-component-view-mr) component.

-   Create and view predefined 3D shapes with the [<u>View shape in mixed reality</u>](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/mixed-reality-component-view-shape) component

-   Measure distance, area, and volume with the [**Measure in mixed reality**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/mixed-reality-component-measure-distance) component.

![Text Description automatically generated](media/image3.png)
