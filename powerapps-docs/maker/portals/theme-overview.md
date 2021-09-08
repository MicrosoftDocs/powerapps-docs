---
title: Themes overview
description: Overview of themes and basic themes in Power Apps portals.
author: neerajnandwana-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 05/10/2021
ms.subservice: portals
ms.author: nenandw
ms.reviewer: tapanm
contributors:
    - neerajnandwana-msft
    - tapanm-msft
---

# Themes overview

In Power Apps portals, the **Enable basic theme** feature is set to **Off**. When you turn on this feature, you can use default themes called **Presets**. You can also create copies of the preset themes for additional customization.

In this article, you'll walk through the basic themes feature. For advanced theme customization, see [Edit CSS](edit-css.md).

## Enable basic themes for existing portals

1. Sign in to [Power Apps](https://make.powerapps.com).

1. Select **Apps** from the left navigation pane, and then select the portal.

    ![Select Apps and a portal.](./media/theme-overview/select-app-portal.png "Select Apps and a portal")

1. Select **More Commands** (**...**), and then select **Edit**.

    ![Edit a portal.](./media/theme-overview/edit-portal.png "Edit a portal")

1. Select **Themes** from the left navigation pane, and then turn on the **Enable basic theme** toggle.

    ![Enable basic themes.](./media/theme-overview/enable-basic-theme.png "Enable basic themes")

## Change theme for your portal

You can set any existing theme in your portal to a default theme.

1. Sign in to [Power Apps](https://make.powerapps.com).

1. Select **Apps** from the left navigation pane, and then select the portal.

1. Select **More Commands** (**...**), and then select **Edit**.

1. Select **Theme** from the components pane.

    ![Select theme icon.](./media/theme-overview/select-theme.png "Select theme icon")

1. Select any default theme from the available presets (in our example, we selected **Green**).

    ![Select a default theme.](./media/theme-overview/basic-theme.png "Select a default theme")

The selected theme is applied to your portal.

![Applied theme.](./media/theme-overview/theme-applied.png "Applied theme")

> [!NOTE]
> After changing theme or theme properties such as colors inside the Studio, select **Browse website** to view the changes in a separate browser tab. If you make multiple changes using this method and switch to different pages inside the browser, the stale browser cache may cause your browser to show theme changes that aren't latest. If this happens, use **Ctrl+F5** to reload the page.

## Create a new theme

1. Sign in to [Power Apps](https://make.powerapps.com).

1. Select **Apps** from the left navigation pane, and then select the portal.

1. Select **More Commands** (**...**), and then select **Edit**.

1. Select **Theme** from the components pane.

1. Select **New Theme**.

    ![Create a new theme.](./media/theme-overview/new-theme.png "Create a new theme")

## Edit theme details

You can update theme name, description, color, and other typography settings in Power Apps Studio. 

1. Sign in to [Power Apps](https://make.powerapps.com).

1. Select **Apps** from the left navigation pane, and then select the portal.

1. Select **More Commands** (**...**), and then select **Edit**.

1. Select **Theme** from the components pane.

1. Select the theme that's currently applied, or select a new theme from the presets.
   Selecting a theme opens the details pane on the right side of your workspace.

    ![Theme details.](./media/theme-overview/theme-details.png "Theme details")

1. Edit theme details such as name, description, and color for different areas.

    |Color option | Affected area |
    | --- | ---  |
    | Primary | Button and link colors. |
    | Header | Header background color. |
    | Header menu text | Text color for the header menu. |
    | Header menu hover | Background color of menu items when they're hovered over. |
    | Body background |  Background color of the body section.​ |
    | Footer background | Background color for the footer.​ |
    | Footer text | Footer text color.​ |

1. Save and publish the changes.

## Copy a preset theme

1. Sign in to [Power Apps](https://make.powerapps.com).

1. Select **Apps** from the left navigation pane, and then select the portal.

1. Select **More Commands** (**...**), and then select **Edit**.

1. Select **Theme** from the components pane.

1. Select the theme from presets that you want to copy, select **...**, and then select **Customize**.

    ![Copy preset theme.](./media/theme-overview/copy-preset-theme.png "Copy a preset theme")

1. Update the theme details as described in the preceding section, and then save the theme.

## Sass variables

[Sass](https://sass-lang.com/) is a stylesheet language with fully CSS-compatible syntax. When you enable the basic theme feature, you can use [Sass variables](https://sass-lang.com/documentation/variables) instead of values to configure theme colors.

For example, if you want the **Header** color to be 25 percent lighter than the **Primary** color, you can use the following value instead of a specific color:

```
lighten($primaryColor, 25%);
```

![Sass example.](./media/theme-overview/sass-example.png "Sass example")

You can use the following Sass variables with basic themes:

|Color option | Sass variable name |
| - | - |
| Primary | ```$primaryColor``` |
| Header | ```$headerColor``` |
| Header menu text | ```$headerMenuTextColor``` |
| Header menu hover | ```$headerMenuHoverColor``` |
| Body background |  ```$bodyBackground``` |
| Footer background | ```$footerColor​``` |
| Footer text | ```$footerTextColor``` |

### Sass variable order

Sass variables work from top to bottom. You can set the *Header* color to ```lighten($primaryColor, 25%);```. But, you can't set the *Primary* color to ```lighten($headerColor, 25%);``` because *Header* is below *Primary* in the list of color options.

## Basic theme considerations

- You can't have two themes with the same theme name or the same theme file name. 
- Any color value you enter manually must be for a valid color.
- Changing the CSS for preset themes isn't supported.
- The recommended theme foreground and background color contrast ratio is 4.5:1, for accessibility.

## Next steps

[Edit theme CSS](edit-css.md)

### See also

[Power Apps portals Studio](portal-designer-anatomy.md) <br>
[Create and manage webpages](create-manage-webpages.md) <br>
[WYSIWYG editor](compose-page.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]