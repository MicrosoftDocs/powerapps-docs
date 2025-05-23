---
title: "Use modern themes in Power Apps"
description: Learn how to change the colors and font of apps including the app header in model-driven apps with the modern look in Power Apps.
ms.custom: ""
ms.date: 05/05/2025
ms.reviewer: "matp"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
author: "jasongre"
ms.subservice: mda-maker
ms.author: "jasongre"
search.audienceType: 
  - maker
contributors:
- adrianorth 
---

# Use modern themes in model-driven apps

Users of model-driven apps with the modern, refreshed look for model-driven apps enabled experience updated styling aligned to the Microsoft Fluent 2 design system. Because this modern refreshed look comes with a new theming system, [classic theming](#see-also) isn't honored; however, makers can modify the colors used by the app to help align with their organizational branding for users who have enabled the modern, refreshed look. In this article, you learn about the styling overrides available with the modern, refreshed look and how to implement them for your organization.

> [!NOTE]
>
> - Modern themes currently support providing a custom theme for the entire app and overriding the app header colors. Other customizations like customizing the business process flow control aren't available.
> - For modern themes to work, the model-driven app must be using the **New look**. More information: [Modern, refreshed look for model-driven apps](../../user/modern-fluent-design.md)

## Modify the app theme

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

With the [modern, refreshed look enabled](../../user/modern-fluent-design.md) in the app, makers can create a custom theme that helps align to their organizational branding. With a custom theme you can change the app header, hyperlinks, lookups, primary buttons,  active tab indicators, row selection, and hover effects. The custom theme also lets you change the font that is used in the application. To accomplish this, you encapsulate the desired theme information into an XML resource, use an app setting to point to this web resource, and then verify the new modern theme matches your expectations.  

> [!IMPORTANT]
>
> - This is a preview feature.
> - [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]
> - The majority of the UI reflects the custom theme; however, there are still areas in the app that don't use modern theming, such as the Timeline control, lookup dropdowns, legacy grids, and audit history.

### Overview of the custom theme XML resource

The first step to creating a custom modern theme is to create an XML file with your desired theme parameters, with one or more of the following attributes defined inside a `CustomTheme` tag.

- `BasePaletteColor` – The seed color (HEX code) used as a basis to generate a 16-slot color palette for the theme. 
- `LockPrimary` – A boolean that determines how the selected seed color is used to generate the 16-slot color palette.  
   -  False (Default): The palette is optimized for accessibility, but doesn't guarantee the seed color will appear in any slot of the generated palette. This is the default setting. Use the [Fluent theme generator](https://react.fluentui.dev/?path=/docs/theme-theme-designer--docs) to preview the generated palette based on your selections for `basePaletteColor`, `vibrancy`, and `hueTorsion`.  
   - True: The seed color is placed in primary (middle) slot of the palette. The remaining colors are generated by making the colors incrementally lighter on one side and darker on the other side. The generated palette might not meet contrast ratio accessibility requirements.
- `Font` – The font for your custom theme. The font being rendered by the custom theme is dependent on the browser and target machine’s ability to show that font. 
- `Vibrancy` – An optional parameter that impacts the muteness or brightness of the palette, especially the lighter colors. The allowed values are between -100 and 100, with a default value of 0. This option is only applicable when `lockPrimary="true"`. 
- `HueTorsion` – An optional parameter that impacts the tint, shade, or tone of the palette, especially the lighter colors. The allowed values are between -100 and 100, with a default value of 0. This option is only applicable when `lockPrimary="true"`.

#### Override the palette

Overriding individual slots in the theme palette provides the creator with full control over the slot colors, which is particularly useful when additional modifications are required beyond the standard theme parameters mentioned above. To override a specific slot, assign a value to the desired slot by its name. For instance, you can specify the HEX code for `darker70`, `primary`, or `lighter10` to tailor the appearance precisely to your preference. Setting values for all 16 slots completely overrides all the palette options described in the previous section, allowing for a highly customized and unique color scheme.

The slot names for the palette from darkest to lightest are: `darker70`, `darker60`, `…` `<>`, `darker10`, `primary`, `lighter10`, `lighter20`, `…`, `lighter80`. Refer to the [Fluent theme](https://react.fluentui.dev/?path=/docs/theme-theme-designer--docs) designer to find out how these slots are generally used in Fluent controls.

:::image type="content" source="../canvas-apps/controls/modern-controls/media/modern-themes-color-ramp.png" alt-text="Modern theme color slots.":::

#### Example XML for a custom theme

As an example, this XML specifies a custom theme that is green with a different font.

```xml
<CustomTheme 
    basePaletteColor="#00FF00"
    vibrancy="0"
    hueTorsion="-50"
    font="'GreatVibes', cursive"
/>
```

This XML specifies a custom theme using the alternate palette generation algorithm with an override for a single slot.

```xml
<CustomTheme 
    basePaletteColor="#00FF00"
    lockPrimary="false"
    font="'GreatVibes', cursive"

    lighter70="#FFFFFF"
/>
```

### Modify the app header colors

Makers can customize the styling of the app header to deviate from the app theme. This can be done by extending the XML created for the custom modern theme with one or more of the following attributes defined inside an `AppHeaderColors` tag.

- `Background` – The background color of the app header. This element must be defined for any changes to take effect.
- `Foreground` – The text color of the app header. If this isn't specified, the system attempts to calculate an appropriate color that has sufficient contrast to the provided background color.
- `BackgroundHover` – The background color of buttons on the app header when they're hovered over. If no value is specified, the system calculates a color based on the background color.
- `ForegroundHover` – The text color of buttons on the app header when they're hovered over. If no value is specified, the system attempts to calculate an appropriate color that has sufficient contrast to the `backgroundHover` color.
- `BackgroundPressed` – The background color of buttons on the app header when they're pressed. The defaulting logic is the same as `backgroundHover`. 
- `ForegroundPressed` – The text color of buttons on the app header when they're pressed. The defaulting logic is the same as `foregroundHover`.
- `BackgroundSelected` – The background color of buttons on the app header when they're selected. The defaulting logic is the same as `backgroundHover`.
- `ForegroundSelected` – The text color of buttons on the app header when they're selected. The defaulting logic is the same as `backgroundHover`.

#### Example XML for a modern theme

As an example, this XML extends the green custom theme with a black app header. For optimal usability, we recommend specifying different color values for each interaction state.

```xml
<CustomTheme
    basePaletteColor="#00FF00"
    vibrancy="0"
    hueTorsion="-50"
    font="'GreatVibes', cursive"
>  
  <AppHeaderColors
    background="#000000" 
    foreground="#FFFFFF" 
    backgroundHover="#313131" 
    foregroundHover="#FFFFFF"
    backgroundPressed="#494949"
    foregroundPressed="#FFFFFF"
    backgroundSelected="#717171" 
    foregroundSelected="#FFFFFF"  
  />
</CustomTheme>
```

> [!NOTE]
> These settings cause any colors specified in the **Override app header color** setting to be ignored.

### Create the web resource

1. Using a text or XML editor, save the XML that is used to create the web resource. [Example XML for a modern theme](#example-xml-for-a-modern-theme)
1. Sign into [Power Apps](https://make.powerapps.com/).
1. Select **Solutions** on the left navigation pane, and then create a **New solution**.
1. Select **New** > **More** > **Web resource**.
1. Select **Choose file**, browse to and select the XML text file you created earlier.
1. In the **New web resource** property pane, enter the following values:
   - **Display name**: Enter a display name, such as *Green custom theme*.
   - **Name**. Accept the automatically generated or enter a unique name for the web resource. 
   - Type: **Data (XML)**

1. Select **Save**. You publish this customization with the steps in the next section.

### Apply the custom theme to apps in your environment

After you select your colors and create the web resource, follow these steps to enable this app header styling for all the apps in your environment that have the **New look** enabled.

1. In the solution you used to [create the web resource](#create-the-web-resource), select **Add existing** > **More** > **Setting**.
1. Type *custom theme* in the **Search** box, select **Custom theme definition**, select **Next**, and then select **Add**.
1. In the solution, select **Custom theme definition**, and then select **Edit** on the command bar.
1. On the right **Edit Custom theme definition** properties pane, select **New environment value** under **Setting environment value** and enter the unique name of your web resource you created earlier (observe the **Name** column in the solution for the unique name). Remove the double quotes and make sure to add the publisher prefix for the web resource. For example, the name might appear as *contoso_green-custom-theme* as in this example.
   :::image type="content" source="media/environment-setting-theme.png" alt-text="Environment setting for a theme with web resource unique name contoso_green-custom-theme." lightbox="media/environment-setting-theme.png":::
1. Select **Save**.
1. Select **Settings** on the left **Objects** pane, and then select **Publish all customizations** on the command bar. (This command appears when no components in the solution are selected).

Custom model-driven app using the extended green theme sample.
:::image type="content" source="media/custom-green-theme-extended.png" alt-text="Custom model-driven app using custom green theme extended with great vibes font.":::

### Verifying new app header colors

After publishing your custom theme, you'll want to validate the application of the theme in the app to ensure everything appears as you expect. 

## Modify the app header colors only

Makers can choose to only customize the styling of the app header to deviate from the default app theme. This can be done by following these steps:

1. Create an XML file with your various color selections, with one or more of the attributes from [app header color overrides section](#modify-the-app-header-colors) defined inside an `AppHeaderColors` tag.
2. Create a web resource using the same process described for [custom themes](#create-the-web-resource), but be sure to give the XML resource an appropriate descriptive display name, such as *Green app header XML*.
3. Apply custom app header colors to apps in your environment by assigning this web resource to the environment or app in the **Override app header color** setting. Follow the steps from [Applying custom themes to your environment](#apply-the-custom-theme-to-apps-in-your-environment) but use the **Override app header color** setting instead.
    > [!NOTE]
    > Any configuration defined in the **Override app header color** setting is ignored if the **Custom theme definition** setting has been defined.  
4. Verify your custom app header visuals, including all button states, to ensure everything appears as you expect and there are sufficient contrast ratios for accessibility. You should verify the following color choices:
    - The desired colors are shown for the app header at rest and for each button interaction state.
    - There's a minimum of a 4.5:1 contrast ratio between foreground and background colors for the rest state and each button interaction state.

### Example XML for app header color override

As an example, this XML specifies a green background color for the app header with white text, with darker background colors for the various button interaction states. For optimal usability, we recommend specifying different color values for each state.

```xml
<AppHeaderColors 
  background="#12783F"
  foreground="#FFFFFF" 
  backgroundHover="#165A31" 
  foregroundHover="#FFFFFF"
  backgroundPressed="#0F1C12"
  foregroundPressed="#FFFFFF"
  backgroundSelected="#153D23" 
  foregroundSelected="#FFFFFF"
/>
```

With this configuration, the app header should look like the following when you play the app. You might need to refresh the browser tab to display the theme.  
:::image type="content" source="media/greenappheader-oct2023.png" alt-text="Green app header in a model-driven app" lightbox="media/greenappheader-oct2023.png":::

## See also

[Classic theming](create-themes-organization-branding.md)

[Modern refreshed look](../../user/modern-fluent-design.md)
[!INCLUDE[footer-include](../../includes/footer-banner.md)]
