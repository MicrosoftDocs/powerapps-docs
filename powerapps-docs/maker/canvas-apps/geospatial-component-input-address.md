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

Entering addresses is frustrating and error prone, particularly in mobile scenarios. With the new address input component, you can see dynamic address suggestions as you type. Using fuzzy matching logic, the component suggests multiple potential address matches that the user can select – making it quicker and easier to enter accurate addresses.

The component returns the address as structured data, allowing your application to extract information like city, street, municipality, and even latitude and longitude, in a format friendly to many locales and international address formats.

To use the component, you need to [enable the geospatial features for the environment](geospatial-overview.md#enable-the-geospatial-features-for-the-environment) as well as [enable the geospatial features for each app](geospatial-overview.md#enable-the-geospatial-features-for-each-app) that you want to use it in.

Make sure to also [review the prerequisites for using geospatial components](geospatial-overview.md#prerequisites).

## Use the component

Insert the component into your app as you normally would for any other control or component.

With an app open for editing in [Power Apps Studio](https://create.powerapps.com):

1. Open the **Insert** tab. 

2. Expand **Input**.

3. Select the component **Address input (preview)** to place it in the center of the app screen, or drag and drop it to position it anywhere on the screen.

4. (Optional) Select **Allow** on the prompt that asks to know your location. This enables the component to bias results by the user's current location.

    ![Allow highlighted on the window that asks to know your location](./media/geospatial/address-allow.png "Allow highlighted on the window that asks to know your location")

You can modify the component with a number of properties.

### Properties

The following properties are on the component's **Address Input** pane on the **Properties** and **Advanced** tabs.

![The properties are in the side panel](./media/geospatial/address-properties.png "The properties are in the side panel")

Some properties are only available in the **Advanced** tab, under the **More options** section.

Property | Description | Type | Location
- | - | - | -
Enable autofill | Whether the component gives address suggestions. | Boolean | Properties
Search result limit | The number of suggested addresses the component displays. | Integer | Properties
Search within radius | Whether the component should suggest addresses within the user-defined **Radius** of the **Latitude** and **Longitude**. | Boolean | Properties
Latitude | The latitude of the center point used to geobias address suggestions. Requires **Search within radius** to be on. | Decimal between -180 and 180 | Properties
Longitude | The longitude of the center point used to geobias address suggestions. Requires **Search within radius** to be on. | Decimal between -180 and 180 | Properties
Radius | The radius in meters around the **Latitude** and **Longitude** to constrain the address suggestions. Requires **Search within radius** to be on. | Decimal | Properties
Language | The language the address suggestions are returned in | String | Properties
Country set | Comma separate list of countries to constrain the address suggestions to, in ISO 3166 alpha-2 country codes - for example "US, FR, KW". | String | Properties

### Additional properties

**[Default](properties-core.md)** – The initial value of a control before it is changed by the user.

**[Text](properties-core.md)** – Text that appears on a control or that the user types into a control.

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**BorderRadius** – The radius of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[Color](properties-color-border.md)** – The color of text in a control.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[DisabledBorderColor](properties-color-border.md)** – The color of a control's border if the control's **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[DisabledColor](properties-color-border.md)** – The color of text in a control if its **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[DisabledFill](properties-color-border.md)** – The background color of a control if its **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[Fill](properties-color-border.md)** – The background color of a control.

**[FocusedBorderColor](properties-color-border.md)** – The color of a control's border when the control is focused.

**[FocusedBorderThickness](properties-color-border.md)** – The thickness of a control's border when the control is focused.

**[Font](properties-text.md)** – The name of the family of fonts in which text appears.

**[FontWeight](properties-text.md)** – The weight of the text in a control: **Bold**, **Semibold**, **Normal**, or **Lighter**.

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**HintText** – Light-grey text that appears in an input-text control if it's empty.

**[HoverBorderColor](properties-color-border.md)** – The color of a control's border when the user keeps the mouse pointer on that control.

**[HoverColor](properties-color-border.md)** – The color of the text in a control when the user keeps the mouse pointer on it.

**[HoverFill](properties-color-border.md)** – The background color of a control when the user keeps the mouse pointer on it.

**[Italic](properties-text.md)** – Whether the text in a control is italic.

**[LineHeight](properties-text.md)** – The distance between, for example, lines of text or items in a list.

**[OnChange](properties-core.md)** – How the app responds when the user changes the value of a control (for example, by adjusting a slider).

**[PaddingBottom](properties-size-location.md)** – The distance between text in a control and the bottom edge of that control.

**[PaddingLeft](properties-size-location.md)** – The distance between text in a control and the left edge of that control.

**[PaddingRight](properties-size-location.md)** – The distance between text in a control and the right edge of that control.

**[PaddingTop](properties-size-location.md)** – The distance between text in a control and the top edge of that control.

**[PressedBorderColor](properties-color-border.md)** – The color of a control's border when the user taps or clicks that control.

**[PressedColor](properties-color-border.md)** – The color of text in a control when the user taps or clicks that control.

**[PressedFill](properties-color-border.md)** – The background color of a control when the user taps or clicks that control.

**[Size](properties-text.md)** – The font size of the text that appears on a control.

**[Strikethrough](properties-text.md)** – Whether a line appears through the text that appears on a control.

**[TabIndex](properties-accessibility.md)** – Keyboard navigation order in relation to other controls.

**[Tooltip](properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Underline](properties-text.md)** – Whether a line appears under the text that appears on a control.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Other geospatial components

- Visualize and interpret location data with the **[Interactive map](geospatial-component-map.md)** component.
