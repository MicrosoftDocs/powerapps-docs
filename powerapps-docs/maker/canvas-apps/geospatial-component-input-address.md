---
title: 
description: 
author: iaanw
manager: shellha
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 6/12/2020
ms.author: iawilt
search.audienceType: 
  - maker
search.app: 
  - PowerApps
ms.custom: ce06122020
---

# Address input component (Preview)

[!INCLUDE [cc-beta-prerelease-disclaimer.md](../../includes/cc-beta-prerelease-disclaimer.md)]

Entering addresses can be frustrating and error-prone, particularly in mobile scenarios. 

The address input component lets you see dynamic address suggestions as you type. Using fuzzy matching logic, the component suggests multiple potential address matches that the user can select&mdash;making it quicker and easier to enter accurate addresses.

The component returns the address as structured data, allowing your application to extract information like city, street, municipality, and even latitude and longitude. The data is in a format friendly to many locales and international address formats.

To use the component, you need to [enable geospatial features for the environment](geospatial-overview.md#enable-the-geospatial-features-for-the-environment) in addition to [enabling geospatial features for each app](geospatial-overview.md#enable-the-geospatial-features-for-each-app) that you want to use it in.

Make sure you also [review the prerequisites for using geospatial components](geospatial-overview.md#prerequisites).

## Use the component

Insert the component into your app as you normally would for any other control or component.

With an app open for editing in [Power Apps Studio](https://create.powerapps.com):

1. Open the **Insert** tab. 

2. Expand **Input**.

3. Select the component **Address input (preview)** to place it in the center of the app screen, or drag it to position it anywhere on the screen.

4. (Optional) Select **Allow** in the window that asks to know your location. This enables the component to bias results by the user's current location.

    ![Allow highlighted in the window that asks to know your location](./media/geospatial/address-allow.png "Allow highlighted in the window that asks to know your location")

You can modify the component by using a number of properties.

### Properties

The following properties are on the component's **Address Input** pane on the **Properties** and **Advanced** tabs.

![The properties are in the side panel](./media/geospatial/address-properties.png "The properties are in the side panel")

Some properties are only available on the **Advanced** tab, in the **More options** section.

| Property | Description | Type | Location |
| - | - | - | - |
| Enable autofill | Whether the component gives address suggestions. | Boolean | Properties |
| Search result limit | The number of suggested addresses the component displays. | Integer | Properties |
| Search within radius | Whether the component should suggest addresses within the user-defined **Radius** of the **Latitude** and **Longitude**. | Boolean | Properties |
| Latitude | The latitude of the center point used to geo-bias address suggestions. Requires **Search within radius** to be on. | Decimal from &ndash;180 through 180 | Properties |
| Longitude | The longitude of the center point used to geo-bias address suggestions. Requires **Search within radius** to be on. | Decimal from &ndash;180 through 180 | Properties |
| Radius | The radius, in meters, around **Latitude** and **Longitude** to constrain the address suggestions. Requires **Search within radius** to be on. | Decimal | Properties |
| Language | The language the address suggestions are returned in | String | Properties |
| Country set | Comma-separated list of countries to constrain the address suggestions to, in ISO 3166 alpha-2 country codes. For example, **US, FR, KW** | String | Properties |

### Additional properties

**[Default](./controls/properties-core.md)** – The initial value of a control before it's changed by the user.

**[Text](./controls/properties-core.md)** – Text that appears on a control or that the user types into a control.

**[BorderColor](./controls/properties-color-border.md)** – The color of a control's border.

**BorderRadius** – The radius of a control's border.

**[BorderStyle](./controls/properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](./controls/properties-color-border.md)** – The thickness of a control's border.

**[Color](./controls/properties-color-border.md)** – The color of text in a control.

**[DisplayMode](./controls/properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[DisabledBorderColor](./controls/properties-color-border.md)** – The color of a control's border if the control's **[DisplayMode](./controls/properties-core.md)** property is set to **Disabled**.

**[DisabledColor](./controls/properties-color-border.md)** – The color of text in a control if its **[DisplayMode](./controls/properties-core.md)** property is set to **Disabled**.

**[DisabledFill](./controls/properties-color-border.md)** – The background color of a control if its **[DisplayMode](./controls/properties-core.md)** property is set to **Disabled**.

**[Fill](./controls/properties-color-border.md)** – The background color of a control.

**[FocusedBorderColor](./controls/properties-color-border.md)** – The color of a control's border when the control is in focus.

**[FocusedBorderThickness](./controls/properties-color-border.md)** – The thickness of a control's border when the control is in focus.

**[Font](./controls/properties-text.md)** – The name of the family of fonts in which text appears.

**[FontWeight](./controls/properties-text.md)** – The weight of the text in a control: **Bold**, **Semibold**, **Normal**, or **Lighter**.

**[Height](./controls/properties-size-location.md)** – The distance between a control's top and bottom edges.

**HintText** – Light-gray text that appears in an input-text control if it's empty.

**[HoverBorderColor](./controls/properties-color-border.md)** – The color of a control's border when the user keeps the mouse pointer on that control.

**[HoverColor](./controls/properties-color-border.md)** – The color of the text in a control when the user keeps the mouse pointer on it.

**[HoverFill](./controls/properties-color-border.md)** – The background color of a control when the user keeps the mouse pointer on it.

**[Italic](./controls/properties-text.md)** – Whether the text in a control is italic.

**[LineHeight](./controls/properties-text.md)** – The vertical distance between lines of text&mdash;for example, between items in a list.

**[OnChange](./controls/properties-core.md)** – How the app responds when the user changes the value of a control (for example, by adjusting a slider).

**[PaddingBottom](./controls/properties-size-location.md)** – The distance between text in a control and the bottom edge of that control.

**[PaddingLeft](./controls/properties-size-location.md)** – The distance between text in a control and the leftmost edge of that control.

**[PaddingRight](./controls/properties-size-location.md)** – The distance between text in a control and the rightmost edge of that control.

**[PaddingTop](./controls/properties-size-location.md)** – The distance between text in a control and the top edge of that control.

**[PressedBorderColor](./controls/properties-color-border.md)** – The color of a control's border when the user taps or clicks that control.

**[PressedColor](./controls/properties-color-border.md)** – The color of text in a control when the user taps or clicks that control.

**[PressedFill](./controls/properties-color-border.md)** – The background color of a control when the user taps or clicks that control.

**[Size](./controls/properties-text.md)** – The font size of the text that appears on a control.

**[Strikethrough](./controls/properties-text.md)** – Whether a line appears through the text that appears on a control.

**[TabIndex](./controls/properties-accessibility.md)** – Keyboard navigation order in relation to other controls.

**[Tooltip](./controls/properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Underline](./controls/properties-text.md)** – Whether a line appears under the text that appears on a control.

**[Visible](./controls/properties-core.md)** – Whether a control appears or is hidden.

**[Width](./controls/properties-size-location.md)** – The distance between a control's leftmost and rightmost edges.

**[X](./controls/properties-size-location.md)** – The distance between the leftmost edge of a control and the leftmost edge of its parent container (or screen, if the control has no parent container).

**[Y](./controls/properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (or screen, if the control has no parent container).

## Other geospatial components

To visualize and interpret location data, use the **[Interactive map](geospatial-component-map.md)** component.
