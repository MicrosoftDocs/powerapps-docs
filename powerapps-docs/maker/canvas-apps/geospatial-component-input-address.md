---
title: Enter and resolve addresses in maps
description: Use the address input control in Power Apps to quickly and easily enter accurate addresses.
author: anuitz
ms.topic: conceptual
ms.custom: canvas, ce06122020
ms.reviewer: mduelae
ms.date: 3/3/2022
ms.subservice: canvas-maker
ms.author: anuitz
search.audienceType: 
  - maker
contributors:
  - mduelae
  - anuitz
---

# Use the address input control to easily enter addresses

Entering addresses can be frustrating and error-prone, particularly in mobile apps. Use the address input control to make address entry easier. The control uses fuzzy logic to suggest potential matches as you type. Select the one you want to quickly and easily enter an accurate address.

The control returns the address as structured data. Your app can extract information such as city, street, municipality, and even latitude and longitude coordinates. The data is in a format that's friendly to many locales and international address formats.

## Prerequisites

Before you can use the control in your apps, you'll need to [enable geospatial features for the environment](geospatial-overview.md#enable-geospatial-features-for-the-environment). Make sure you also [review the prerequisites for using geospatial controls](geospatial-overview.md#prerequisites-for-full-support). Refer to the [privacy and security table](geospatial-overview.md#privacy-and-security-considerations) for more details on the address input control's data usage.

## Add an address input control to your app

With your app open for [editing](./edit-app.md) in [Power Apps Studio](https://create.powerapps.com):

1. Open the **Insert** tab and expand **Input**.
1. Select **Address input** to place an address input box in the app screen, or drag the control to the screen to position it more precisely. You must enter at least three characters including one number for the address input control.

## Set a default search radius

By default, the control will search around the user's location. You can refine the default search area to help narrow the initial results.

1. On the address input control's **Properties** tab, turn on the **Search within radius** property.
1. Enter a longitude, latitude, and radius in meters.

The control will start searching at the given latitude and longitude, out to the distance specified.

## Use the map control with the address input control

You can add a button to your app to save entered addresses as a data collection. Then you can retrieve the addresses and display them in [the map control](geospatial-component-map.md).

1. Add a map control and an address input control to your app.

1. Insert and place a **Button** control.

1. Change the **OnSelect** property of the button control as follows. (Hint: Copy the formula and paste it in the formula bar or on the **Advanced** properties tab, whichever you prefer.)

1. Enter a longitude, latitude, and radius (in meters).

    The control will start searching at the latitude and longitude, out to the distance specified in the radius field.


    ```powerapps-dot
    If(IsBlank(AddressInput1.SearchResultJson), "", Collect(locations, {Latitude: AddressInput1.SelectedLatitude, Longitude: AddressInput1.SelectedLongitude}))
    ```

    The formula saves the current latitude and longitude to a collection named *locations*, as long as the search results aren't blank.

    :::image type="content" source="./media/geospatial/input-code.png" alt-text="A screenshot of the button under construction in Power Apps Studio, shown with its OnSelect property.":::

1. Select the map control. Change its properties as follows:

    | Property name | Value | Where |
    | - | - | - |
    | Items | "Locations" | **Properties** tab |
    | ItemsLatitudes | "Latitude" | **Advanced** tab |
    | ItemsLongitudes | "Longitude" | **Advanced** tab |

When the user selects the button, the result from the address input control is added to the map as a new pin.

## Properties

Change an address input control's behavior and appearance using properties. Some properties are only available on the **Advanced** tab.

| Property | Description | Type | Tab |
| - | - | - | - |
| Default | Sets the initial value of the control. | String | Properties; Advanced: **[Default](./controls/properties-core.md)** |
| Hint text | Sets the hint that appears in the control before the user enters text. | String | Properties; Advanced: **HintText** |
| Font | Sets the name of the family of fonts used for the control text. | Dropdown list | Properties; Advanced: **[Font](./controls/properties-text.md)** |
| Font size | Sets the size of the control text. | Floating point number | Properties; Advanced: **[FontSize](./controls/properties-text.md)** |
| Font weight | Sets the weight of the control text, either *Bold*, *Lighter*, *Normal*, or *Semibold*. | Dropdown list | Properties; Advanced: **[FontWeight](./controls/properties-text.md)** |
| Text alignment | Sets the horizontal alignment of the control text, either *Center*, *Justify*, *Left*, or *Right*. | Dropdown list | Properties; Advanced: **[TextAlignment](./controls/properties-text.md)** |
| Line height | Sets the vertical distance between lines of text in the control. | Floating point number |  Properties; Advanced: **[LineHeight](./controls/properties-text.md)** |
| Display mode |  Determines whether the control allows user input (*Edit*), only displays data (*View*), or is disabled (*Disabled*). | Dropdown list | Properties; Advanced: **[DisplayMode](./controls/properties-core.md)** |
| Font style | Sets the style of the control text, either *Italic*, *Underline*, *Strikethrough*, or none. | Dropdown list | Properties; Advanced: **Italic**, **Underline**, **Strikethrough** |
| Search result limit | Sets the number of suggested addresses the control displays. | Integer | Properties; Advanced: **SearchResultLimit** |
| Search within radius | Determines whether the control should suggest addresses within the **Radius** of the **Latitude** and **Longitude**. | Boolean | Properties; Advanced: **SearchWithinRadius** |
| Latitude | Sets the latitude coordinate of the center point used for address suggestions. Requires **Search within radius** to be on. | Floating point number from -90 to 90 | Properties; Advanced: **Latitude** |
| Longitude | Sets the longitude coordinate of the center point used for address suggestions. Requires **Search within radius** to be on. | Floating point number from -180 to 180 | Properties; Advanced: **Longitude** |
| Radius | Sets the radius, in meters, around **Latitude** and **Longitude** to constrain address suggestions. Requires **Search within radius** to be on. | Floating point number | Properties; Advanced: **Radius** |
| Language | Sets the language that address suggestions are returned in. | String | Properties; Advanced: **Language** |
| Country set | Identifies a comma-separated list of countries/regions to constrain address suggestions to, in ISO 3166 alpha-2 format; for example, *US,CA,MX*. | String | Properties; Advanced: **CountrySet** |
| Visible | Shows or hides the control. | Boolean | Properties; Advanced: **[Visible](./controls/properties-core.md)** |
| Padding top | Sets the distance between the control text and the top of the control. | Floating point number | Properties; Advanced: **[PaddingTop](./controls/properties-size-location.md)** |
| Padding bottom | Sets the distance between the control text and the bottom of the control. | Floating point number | Properties; Advanced: **[PaddingBottom](./controls/properties-size-location.md)** |
| Padding left | Sets the distance between the control text and the left edge of the control. | Floating point number | Properties; Advanced: **[PaddingLeft](./controls/properties-size-location.md)** |
| Padding right | Sets the distance between the control text and the right edge of the control. | Floating point number | Properties; Advanced: **[PaddingRight](./controls/properties-size-location.md)** |
 Position | Places the upper-left corner of the control at the screen coordinates specified in *X* and *Y*. | Integer | Properties; Advanced: **[X](./controls/properties-size-location.md)**, **[Y](./controls/properties-size-location.md)** |
| Size | Determines the size of the control using the pixel values provided in *Width* and *Height*. | Integer | Properties; Advanced: **[Width](./controls/properties-size-location.md)**, **[Height](./controls/properties-size-location.md)** |
| Border radius | Determines the corner radius of the control border. | Floating point number | Properties; Advanced: **BorderRadius** |
| [Color](./controls/properties-color-border.md) | Sets the colors of the control text and the control background. | Not applicable | Properties; Advanced: **FillColor**, **TextColor** |
| Border | Determines the style, width, and color of the control border. | Not applicable | Properties; Advanced: **[BorderStyle](./controls/properties-color-border.md)**, **[BorderThickness](./controls/properties-color-border.md)**, **[BorderColor](./controls/properties-color-border.md)** |
| Tab index | Specifies the order the control is selected if the user navigates the app using the Tab key. | Integer | Properties; Advanced: **[TabIndex](./controls/properties-accessibility.md)** |
| Tooltip | Determines the text to display when the user hovers over the control. | String | Properties; Advanced: **[Tooltip](./controls/properties-core.md)** |
| Hover color | Sets the colors of the control text, the control background, and the control border when the user hovers the mouse pointer over it. | Not applicable | Properties; Advanced: **HoverFontColor**, **HoverFillColor**, **HoverBorderColor** |
| Disabled color | Sets the colors of the control text, the control background, and the control border if **DisplayMode** is *Disabled*. | Not applicable | Properties; Advanced: **DisabledFontColor**, **DisabledFillColor**, **DisabledBorderColor** |
| Pressed color | Sets the colors of the control text, the control background, and the control border when the user selects the control. | Not applicable | Properties; Advanced: **PressedFontColor**, **PressedFillColor**, **PressedBorderColor** |
| ContentLanguage | Determines the display language of the control, if it's different from the language that's used in the app. | String | Advanced |
| OnAddressSelect | Contains code that runs when the user selects a suggested address. | Event | Advanced |
| OnChange | Contains code that runs when a control property is changed. | Event | Advanced |

### Output properties

Other properties become available when a user interacts with the address input control. You can use these *output properties* in other controls or to customize the app experience.

| Property | Description |
| - | - |
| UserInput | The text the user typed in the input box |
| SelectedLatitude | The latitude of the address that the user selected |
| SelectedLongitude | The longitude of the address that the user selected |
| SearchResultJson | The search result, based on **UserInput**, displayed as a string in JSON format |
| FreeformAddress | The address that the user selected from the list of suggested addresses |
| LocalName | The name of a geographic area or locality that groups a number of addressable objects for addressing purposes, without being an administrative unit |
| PostalCode | The postal code |
| ExtendedPostalCode | The extended postal code |
| CountryCode | The country code |
| Country | The country/region name |
| CountryCodeISO3 | The country code in ISO alpha-3 format |
| CountrySubdivisionName | The country/region subdivision name |
| StreetName | The street name |
| StreetNumber | The street number |
| Municipality | The municipality |
| MunicipalitySubdivision | The municipality subdivision |
| CountryTertiarySubdivision | The country/region tertiary subdivision |
| CountrySecondarySubdivision | The country/region secondary subdivision |
| CountrySubdivision | The country/region subdivision |

## Other geospatial controls

To visualize and interpret location data, use the **[interactive map](geospatial-component-map.md)** control.

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
