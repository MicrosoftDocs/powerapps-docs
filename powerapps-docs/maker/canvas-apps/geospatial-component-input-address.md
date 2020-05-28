---
title: 
description: 
author: iaanw
manager: shellha
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 3/19/2020
ms.author: iawilt
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---

# Address input component

Easily bring dynamic mapping capabilities into your canvas apps. View the physical position of entities by linking to a data source, or by inputting new physical locations. Customize your map view by changing its default location and adding map components. Pan, tilt, zoom, and drag to center your map view.




To use the component, you should [review the prerequisites](geospatial-overview.md#prerequisites).


## Use the component

Insert the component into your app as you normally would for any other control or component.

With an app open for editing in [Power Apps Studio](https://create.powerapps.com):

1. Open the **Insert** tab. 

2. Expand **Input**.

3. Select the component **Address input (preview)** to place it in the center of the app screen, or drag and drop it to position it anywhere on the screen.

4. Select **Allow** on the prompt that asks to know your location

    ![Allow highlighted on the window that asks to know your location](./media/geospatial/address-allow.png "Allow highlighted on the window that asks to know your location")

You can modify the component with a number of properties.

### Properties

The following properties are on the component's **Address Input** pane on the **Properties** and **Advanced** tabs.

![The properties are in the side panel](./media/geospatial/address-properties.png "The properties are in the side panel")

Some properties are only available in the **Advanced** tab, under the **More options** section.

Property | Description | Type | Location
- | - | - | -
Data source(Items) | Data source (table) that lists a pre-defined set of longitudes and latitudes to display as map pin on the map when it's loaded. Map each of the columns in your data with the *ItemsLongitudes*, *ItemsLatitudes*, and *ItemLabels*. | Not applicable | Properties
Transparency | Set the transparency of the map. | Percentage | Properties
Visible | Whether the map should show or not. | Boolean | Properties
Position | Location of the map component (top left corner) on the app's screen, in pixels from the top left corner of the app screen. | Pixels | Properties
Size | The size of the map component on the app's screen. | Pixels | Properties
Use custom location | Whether the map initializes at a custom location set by the user or not. | Boolean | Properties
Custom longitude | Longitude at which the map would go to when it's loaded if **Use custom location** is enabled. | Floating point number | Properties
Custom latitude | Latitude at which the map would go to when it's loaded if **Use custom location** is enabled. | Floating point number | Properties
Custom zoom level | Zoom level at which the map would be set to when it's loaded if **Use custom location** is enabled. | Integer | Properties
Satellite view | Whether the style of the map is a satellite view or a road view. | Boolean | Properties
Cluster pins | Whether the map pins are clustered or not. | Boolean | Properties
Zoom control | Whether the zoom component appears on the map or not. | Boolean | Properties
Compass control | Whether the compass component appears on the map or not. | Boolean | Properties
Pitch control | Whether the pitch component appears on the map or not. | Boolean | Properties
Maximum map pins | Maximum number of pins displayed on the map | Integer | Properties
Border radius | How curved the corners of the map component should appear; higher numbers result in a more distinct curve. | Integer | Properties
Border | Style, thickness, and color of the border. | Multiple | Properties
Tab index | Order in which items on the app screen be tabbed between. | Integer | Properties
ItemsLabels | A column in Items with the strings you want to use as labels for the pins. | TableName.ColumnName | Advanced
ItemsLongitudes | Name of the column in the table in your data source with floating-point numbers that represent the longitude position of the pins. | TableName.ColumnName | Advanced
ItemsLatitudes | Name of the column in the table in your data source with floating-point numbers that represent the latitude position of the pins. | TableName.ColumnName | Advanced
Items_Items | Name of the table in your data source that contains all the records that you want to plot in the map using pins. Each row must have an entry for the label, longitude, and latitude for each row. | TableName | Advanced



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


## Known issues

- Localization is not yet supported.
- Model-driven apps are not yet supported.




## Other geospatial components
- [Map](geospatial-component-map.md)

## Next steps
Explore [example AR apps](augmented-reality-example-apps.md) and see what sorts of scenarios AR controls can help solve