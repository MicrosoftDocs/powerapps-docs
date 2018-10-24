---
title: Color enumeration and ColorFade, ColorValue, and RGBA functions | Microsoft Docs
description: Reference information for the Color enumeration and ColorFade, ColorValue, and RGBA functions in PowerApps, including syntax and examples
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: anneta
ms.date: 10/25/2015
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Color enumeration and ColorFade, ColorValue, and RGBA functions in PowerApps
Using built in color values, defining custom colors, and Alpha blending.

## Description
The **Color** enumeration is an easy way to access the colors defined by HTML's Cascading Style Sheets (CSS).  For example, **Color.Red** returns a pure red color.  The list of these colors is included at the end of this article.   

The **ColorValue** function returns a color based on a CSS color string.  Both names of CSS colors such as "RosyBrown" and hex values such as "#bc8f8f" may be used.

The **RGBA** function returns a color based on Red, Green, and Blue color components.  It also includes an Alpha component used for mixing colors of objects layered on top of one another.  Alpha varies from 0 or 0% which is fully transparent and invisible to 1 or 100% which is fully opaque and completely blocks out layers below.

The **ColorFade** function returns a brighter or darker version of a color.  The amount of fade varies from -1 which fully darkens a color to black, to 0 which has no impact on the color, to 1 which fully brightens a color to white.  

## Syntax
**Color**.*ColorName*

* *ColorName* - Required.  A Cascading Style Sheet (CSS) color name.  See list below of possible enumeration values.

**ColorValue**( *CSSColor* )

* *CSSColor* - Required.  A Cascading Style Sheet (CSS) color definition.  Both names of colors, such as "OliveDrab", and hex values, such as "#6b8e23", may be used.  

**RGBA**( *Red*, *Green*, *Blue*, *Alpha* )

* *Red*, *Green*, *Blue* - Required.  Color component values, ranging from 0 (no saturation) to 255 (full saturation).
* *Alpha* - Required.  Alpha component, ranging from 0 (fully transparent) to 1 (fully opaque).  You can also use a percentage, 0% to 100%.

**ColorFade**( *Color*, *FadeAmount* )

* *Color* - Required.  A color value such as **Color.Red** or the output from **ColorValue** or **RGBA**.
* *FadeAmount* - Required.  A number between -1 and 1.  -1 fully darkens a color to black, 0 has no impact on the color, and 1 fully brightens a color to white.  

## Built in colors

| Color enumeration | ColorValue with Hex Code | RGBA | Color Swatch |
| --- | --- | --- | --- |
| **Color.AliceBlue** |**ColorValue( "#f0f8ff" )** |**RGBA( 240, 248, 255, 1 )** |![aliceblue](./media/function-colors/color-aliceblue.png) |
| **Color.AntiqueWhite** |**ColorValue( "#faebd7" )** |**RGBA( 250, 235, 215, 1 )** |![antiquewhite](./media/function-colors/color-antiquewhite.png) |
| **Color.Aqua** |**ColorValue( "#00ffff" )** |**RGBA( 0, 255, 255, 1 )** |![aqua](./media/function-colors/color-aqua.png) |
| **Color.Aquamarine** |**ColorValue( "#7fffd4" )** |**RGBA( 127, 255, 212, 1 )** |![aquamarine](./media/function-colors/color-aquamarine.png) |
| **Color.Azure** |**ColorValue( "#f0ffff" )** |**RGBA( 240, 255, 255, 1 )** |![azure](./media/function-colors/color-azure.png) |
| **Color.Beige** |**ColorValue( "#f5f5dc" )** |**RGBA( 245, 245, 220, 1 )** |![beige](./media/function-colors/color-beige.png) |
| **Color.Bisque** |**ColorValue( "#ffe4c4" )** |**RGBA( 255, 228, 196, 1 )** |![bisque](./media/function-colors/color-bisque.png) |
| **Color.Black** |**ColorValue( "#000000" )** |**RGBA( 0, 0, 0, 1 )** |![black](./media/function-colors/color-black.png) |
| **Color.BlanchedAlmond** |**ColorValue( "#ffebcd" )** |**RGBA( 255, 235, 205, 1 )** |![blanchedalmond](./media/function-colors/color-blanchedalmond.png) |
| **Color.Blue** |**ColorValue( "#0000ff" )** |**RGBA( 0, 0, 255, 1 )** |![blue](./media/function-colors/color-blue.png) |
| **Color.BlueViolet** |**ColorValue( "#8a2be2" )** |**RGBA( 138, 43, 226, 1 )** |![blueviolet](./media/function-colors/color-blueviolet.png) |
| **Color.Brown** |**ColorValue( "#a52a2a" )** |**RGBA( 165, 42, 42, 1 )** |![brown](./media/function-colors/color-brown.png) |
| **Color.Burlywood** |**ColorValue( "#deb887" )** |**RGBA( 222, 184, 135, 1 )** |![burlywood](./media/function-colors/color-burlywood.png) |
| **Color.CadetBlue** |**ColorValue( "#5f9ea0" )** |**RGBA( 95, 158, 160, 1 )** |![cadetblue](./media/function-colors/color-cadetblue.png) |
| **Color.Chartreuse** |**ColorValue( "#7fff00" )** |**RGBA( 127, 255, 0, 1 )** |![chartreuse](./media/function-colors/color-chartreuse.png) |
| **Color.Chocolate** |**ColorValue( "#d2691e" )** |**RGBA( 210, 105, 30, 1 )** |![chocolate](./media/function-colors/color-chocolate.png) |
| **Color.Coral** |**ColorValue( "#ff7f50" )** |**RGBA( 255, 127, 80, 1 )** |![coral](./media/function-colors/color-coral.png) |
| **Color.CornflowerBlue** |**ColorValue( "#6495ed" )** |**RGBA( 100, 149, 237, 1 )** |![cornflowerblue](./media/function-colors/color-cornflowerblue.png) |
| **Color.Cornsilk** |**ColorValue( "#fff8dc" )** |**RGBA( 255, 248, 220, 1 )** |![cornsilk](./media/function-colors/color-cornsilk.png) |
| **Color.Crimson** |**ColorValue( "#dc143c" )** |**RGBA( 220, 20, 60, 1 )** |![crimson](./media/function-colors/color-crimson.png) |
| **Color.Cyan** |**ColorValue( "#00ffff" )** |**RGBA( 0, 255, 255, 1 )** |![cyan](./media/function-colors/color-cyan.png) |
| **Color.DarkBlue** |**ColorValue( "#00008b" )** |**RGBA( 0, 0, 139, 1 )** |![darkblue](./media/function-colors/color-darkblue.png) |
| **Color.DarkCyan** |**ColorValue( "#008b8b" )** |**RGBA( 0, 139, 139, 1 )** |![darkcyan](./media/function-colors/color-darkcyan.png) |
| **Color.DarkGoldenRod** |**ColorValue( "#b8860b" )** |**RGBA( 184, 134, 11, 1 )** |![darkgoldenrod](./media/function-colors/color-darkgoldenrod.png) |
| **Color.DarkGray** |**ColorValue( "#a9a9a9" )** |**RGBA( 169, 169, 169, 1 )** |![darkgray](./media/function-colors/color-darkgray.png) |
| **Color.DarkGreen** |**ColorValue( "#006400" )** |**RGBA( 0, 100, 0, 1 )** |![darkgreen](./media/function-colors/color-darkgreen.png) |
| **Color.DarkGrey** |**ColorValue( "#a9a9a9" )** |**RGBA( 169, 169, 169, 1 )** |![darkgrey](./media/function-colors/color-darkgrey.png) |
| **Color.DarkKhaki** |**ColorValue( "#bdb76b" )** |**RGBA( 189, 183, 107, 1 )** |![darkkhaki](./media/function-colors/color-darkkhaki.png) |
| **Color.DarkMagenta** |**ColorValue( "#8b008b" )** |**RGBA( 139, 0, 139, 1 )** |![darkmagenta](./media/function-colors/color-darkmagenta.png) |
| **Color.DarkOliveGreen** |**ColorValue( "#556b2f" )** |**RGBA( 85, 107, 47, 1 )** |![darkolivegreen](./media/function-colors/color-darkolivegreen.png) |
| **Color.DarkOrange** |**ColorValue( "#ff8c00" )** |**RGBA( 255, 140, 0, 1 )** |![darkorange](./media/function-colors/color-darkorange.png) |
| **Color.DarkOrchid** |**ColorValue( "#9932cc" )** |**RGBA( 153, 50, 204, 1 )** |![darkorchid](./media/function-colors/color-darkorchid.png) |
| **Color.DarkRed** |**ColorValue( "#8b0000" )** |**RGBA( 139, 0, 0, 1 )** |![darkred](./media/function-colors/color-darkred.png) |
| **Color.DarkSalmon** |**ColorValue( "#e9967a" )** |**RGBA( 233, 150, 122, 1 )** |![darksalmon](./media/function-colors/color-darksalmon.png) |
| **Color.DarkSeaGreen** |**ColorValue( "#8fbc8f" )** |**RGBA( 143, 188, 143, 1 )** |![darkseagreen](./media/function-colors/color-darkseagreen.png) |
| **Color.DarkSlateBlue** |**ColorValue( "#483d8b" )** |**RGBA( 72, 61, 139, 1 )** |![darkslateblue](./media/function-colors/color-darkslateblue.png) |
| **Color.DarkSlateGray** |**ColorValue( "#2f4f4f" )** |**RGBA( 47, 79, 79, 1 )** |![darkslategray](./media/function-colors/color-darkslategray.png) |
| **Color.DarkSlateGrey** |**ColorValue( "#2f4f4f" )** |**RGBA( 47, 79, 79, 1 )** |![darkslategrey](./media/function-colors/color-darkslategrey.png) |
| **Color.DarkTurquoise** |**ColorValue( "#00ced1" )** |**RGBA( 0, 206, 209, 1 )** |![darkturquoise](./media/function-colors/color-darkturquoise.png) |
| **Color.DarkViolet** |**ColorValue( "#9400d3" )** |**RGBA( 148, 0, 211, 1 )** |![darkviolet](./media/function-colors/color-darkviolet.png) |
| **Color.DeepPink** |**ColorValue( "#ff1493" )** |**RGBA( 255, 20, 147, 1 )** |![deeppink](./media/function-colors/color-deeppink.png) |
| **Color.DeepSkyBlue** |**ColorValue( "#00bfff" )** |**RGBA( 0, 191, 255, 1 )** |![deepskyblue](./media/function-colors/color-deepskyblue.png) |
| **Color.DimGray** |**ColorValue( "#696969" )** |**RGBA( 105, 105, 105, 1 )** |![dimgray](./media/function-colors/color-dimgray.png) |
| **Color.DimGrey** |**ColorValue( "#696969" )** |**RGBA( 105, 105, 105, 1 )** |![dimgrey](./media/function-colors/color-dimgrey.png) |
| **Color.DodgerBlue** |**ColorValue( "#1e90ff" )** |**RGBA( 30, 144, 255, 1 )** |![dodgerblue](./media/function-colors/color-dodgerblue.png) |
| **Color.FireBrick** |**ColorValue( "#b22222" )** |**RGBA( 178, 34, 34, 1 )** |![firebrick](./media/function-colors/color-firebrick.png) |
| **Color.FloralWhite** |**ColorValue( "#fffaf0" )** |**RGBA( 255, 250, 240, 1 )** |![floralwhite](./media/function-colors/color-floralwhite.png) |
| **Color.ForestGreen** |**ColorValue( "#228b22" )** |**RGBA( 34, 139, 34, 1 )** |![forestgreen](./media/function-colors/color-forestgreen.png) |
| **Color.Fuchsia** |**ColorValue( "#ff00ff" )** |**RGBA( 255, 0, 255, 1 )** |![fuchsia](./media/function-colors/color-fuchsia.png) |
| **Color.Gainsboro** |**ColorValue( "#dcdcdc" )** |**RGBA( 220, 220, 220, 1 )** |![gainsboro](./media/function-colors/color-gainsboro.png) |
| **Color.GhostWhite** |**ColorValue( "#f8f8ff" )** |**RGBA( 248, 248, 255, 1 )** |![ghostwhite](./media/function-colors/color-ghostwhite.png) |
| **Color.Gold** |**ColorValue( "#ffd700" )** |**RGBA( 255, 215, 0, 1 )** |![gold](./media/function-colors/color-gold.png) |
| **Color.GoldenRod** |**ColorValue( "#daa520" )** |**RGBA( 218, 165, 32, 1 )** |![goldenrod](./media/function-colors/color-goldenrod.png) |
| **Color.Gray** |**ColorValue( "#808080" )** |**RGBA( 128, 128, 128, 1 )** |![gray](./media/function-colors/color-gray.png) |
| **Color.Green** |**ColorValue( "#008000" )** |**RGBA( 0, 128, 0, 1 )** |![green](./media/function-colors/color-green.png) |
| **Color.GreenYellow** |**ColorValue( "#adff2f" )** |**RGBA( 173, 255, 47, 1 )** |![greenyellow](./media/function-colors/color-greenyellow.png) |
| **Color.Grey** |**ColorValue( "#808080" )** |**RGBA( 128, 128, 128, 1 )** |![grey](./media/function-colors/color-grey.png) |
| **Color.Honeydew** |**ColorValue( "#f0fff0" )** |**RGBA( 240, 255, 240, 1 )** |![honeydew](./media/function-colors/color-honeydew.png) |
| **Color.HotPink** |**ColorValue( "#ff69b4" )** |**RGBA( 255, 105, 180, 1 )** |![hotpink](./media/function-colors/color-hotpink.png) |
| **Color.IndianRed** |**ColorValue( "#cd5c5c" )** |**RGBA( 205, 92, 92, 1 )** |![indianred](./media/function-colors/color-indianred.png) |
| **Color.Indigo** |**ColorValue( "#4b0082" )** |**RGBA( 75, 0, 130, 1 )** |![indigo](./media/function-colors/color-indigo.png) |
| **Color.Ivory** |**ColorValue( "#fffff0" )** |**RGBA( 255, 255, 240, 1 )** |![ivory](./media/function-colors/color-ivory.png) |
| **Color.Khaki** |**ColorValue( "#f0e68c" )** |**RGBA( 240, 230, 140, 1 )** |![khaki](./media/function-colors/color-khaki.png) |
| **Color.Lavender** |**ColorValue( "#e6e6fa" )** |**RGBA( 230, 230, 250, 1 )** |![lavender](./media/function-colors/color-lavender.png) |
| **Color.LavenderBlush** |**ColorValue( "#fff0f5" )** |**RGBA( 255, 240, 245, 1 )** |![lavenderblush](./media/function-colors/color-lavenderblush.png) |
| **Color.LawnGreen** |**ColorValue( "#7cfc00" )** |**RGBA( 124, 252, 0, 1 )** |![lawngreen](./media/function-colors/color-lawngreen.png) |
| **Color.LemonChiffon** |**ColorValue( "#fffacd" )** |**RGBA( 255, 250, 205, 1 )** |![lemonchiffon](./media/function-colors/color-lemonchiffon.png) |
| **Color.LightBlue** |**ColorValue( "#add8e6" )** |**RGBA( 173, 216, 230, 1 )** |![lightblue](./media/function-colors/color-lightblue.png) |
| **Color.LightCoral** |**ColorValue( "#f08080" )** |**RGBA( 240, 128, 128, 1 )** |![lightcoral](./media/function-colors/color-lightcoral.png) |
| **Color.LightCyan** |**ColorValue( "#e0ffff" )** |**RGBA( 224, 255, 255, 1 )** |![lightcyan](./media/function-colors/color-lightcyan.png) |
| **Color.LightGoldenRodYellow** |**ColorValue( "#fafad2" )** |**RGBA( 250, 250, 210, 1 )** |![lightgoldenrodyellow](./media/function-colors/color-lightgoldenrodyellow.png) |
| **Color.LightGray** |**ColorValue( "#d3d3d3" )** |**RGBA( 211, 211, 211, 1 )** |![lightgray](./media/function-colors/color-lightgray.png) |
| **Color.LightGreen** |**ColorValue( "#90ee90" )** |**RGBA( 144, 238, 144, 1 )** |![lightgreen](./media/function-colors/color-lightgreen.png) |
| **Color.LightGrey** |**ColorValue( "#d3d3d3" )** |**RGBA( 211, 211, 211, 1 )** |![lightgrey](./media/function-colors/color-lightgrey.png) |
| **Color.LightPink** |**ColorValue( "#ffb6c1" )** |**RGBA( 255, 182, 193, 1 )** |![lightpink](./media/function-colors/color-lightpink.png) |
| **Color.LightSalmon** |**ColorValue( "#ffa07a" )** |**RGBA( 255, 160, 122, 1 )** |![lightsalmon](./media/function-colors/color-lightsalmon.png) |
| **Color.LightSeaGreen** |**ColorValue( "#20b2aa" )** |**RGBA( 32, 178, 170, 1 )** |![lightseagreen](./media/function-colors/color-lightseagreen.png) |
| **Color.LightSkyBlue** |**ColorValue( "#87cefa" )** |**RGBA( 135, 206, 250, 1 )** |![lightskyblue](./media/function-colors/color-lightskyblue.png) |
| **Color.LightSlateGray** |**ColorValue( "#778899" )** |**RGBA( 119, 136, 153, 1 )** |![lightslategray](./media/function-colors/color-lightslategray.png) |
| **Color.LightSlateGrey** |**ColorValue( "#778899" )** |**RGBA( 119, 136, 153, 1 )** |![lightslategrey](./media/function-colors/color-lightslategrey.png) |
| **Color.LightSteelBlue** |**ColorValue( "#b0c4de" )** |**RGBA( 176, 196, 222, 1 )** |![lightsteelblue](./media/function-colors/color-lightsteelblue.png) |
| **Color.LightYellow** |**ColorValue( "#ffffe0" )** |**RGBA( 255, 255, 224, 1 )** |![lightyellow](./media/function-colors/color-lightyellow.png) |
| **Color.Lime** |**ColorValue( "#00ff00" )** |**RGBA( 0, 255, 0, 1 )** |![lime](./media/function-colors/color-lime.png) |
| **Color.LimeGreen** |**ColorValue( "#32cd32" )** |**RGBA( 50, 205, 50, 1 )** |![limegreen](./media/function-colors/color-limegreen.png) |
| **Color.Linen** |**ColorValue( "#faf0e6" )** |**RGBA( 250, 240, 230, 1 )** |![linen](./media/function-colors/color-linen.png) |
| **Color.Magenta** |**ColorValue( "#ff00ff" )** |**RGBA( 255, 0, 255, 1 )** |![magenta](./media/function-colors/color-magenta.png) |
| **Color.Maroon** |**ColorValue( "#800000" )** |**RGBA( 128, 0, 0, 1 )** |![maroon](./media/function-colors/color-maroon.png) |
| **Color.MediumAquamarine** |**ColorValue( "#66cdaa" )** |**RGBA( 102, 205, 170, 1 )** |![mediumaquamarine](./media/function-colors/color-mediumaquamarine.png) |
| **Color.MediumBlue** |**ColorValue( "#0000cd" )** |**RGBA( 0, 0, 205, 1 )** |![mediumblue](./media/function-colors/color-mediumblue.png) |
| **Color.MediumOrchid** |**ColorValue( "#ba55d3" )** |**RGBA( 186, 85, 211, 1 )** |![mediumorchid](./media/function-colors/color-mediumorchid.png) |
| **Color.MediumPurple** |**ColorValue( "#9370db" )** |**RGBA( 147, 112, 219, 1 )** |![mediumpurple](./media/function-colors/color-mediumpurple.png) |
| **Color.MediumSeaGreen** |**ColorValue( "#3cb371" )** |**RGBA( 60, 179, 113, 1 )** |![mediumseagreen](./media/function-colors/color-mediumseagreen.png) |
| **Color.MediumSlateBlue** |**ColorValue( "#7b68ee" )** |**RGBA( 123, 104, 238, 1 )** |![mediumslateblue](./media/function-colors/color-mediumslateblue.png) |
| **Color.MediumSpringGreen** |**ColorValue( "#00fa9a" )** |**RGBA( 0, 250, 154, 1 )** |![mediumspringgreen](./media/function-colors/color-mediumspringgreen.png) |
| **Color.MediumTurquoise** |**ColorValue( "#48d1cc" )** |**RGBA( 72, 209, 204, 1 )** |![mediumturquoise](./media/function-colors/color-mediumturquoise.png) |
| **Color.MediumVioletRed** |**ColorValue( "#c71585" )** |**RGBA( 199, 21, 133, 1 )** |![mediumvioletred](./media/function-colors/color-mediumvioletred.png) |
| **Color.MidnightBlue** |**ColorValue( "#191970" )** |**RGBA( 25, 25, 112, 1 )** |![midnightblue](./media/function-colors/color-midnightblue.png) |
| **Color.MintCream** |**ColorValue( "#f5fffa" )** |**RGBA( 245, 255, 250, 1 )** |![mintcream](./media/function-colors/color-mintcream.png) |
| **Color.MistyRose** |**ColorValue( "#ffe4e1" )** |**RGBA( 255, 228, 225, 1 )** |![mistyrose](./media/function-colors/color-mistyrose.png) |
| **Color.Moccasin** |**ColorValue( "#ffe4b5" )** |**RGBA( 255, 228, 181, 1 )** |![moccasin](./media/function-colors/color-moccasin.png) |
| **Color.NavajoWhite** |**ColorValue( "#ffdead" )** |**RGBA( 255, 222, 173, 1 )** |![navajowhite](./media/function-colors/color-navajowhite.png) |
| **Color.Navy** |**ColorValue( "#000080" )** |**RGBA( 0, 0, 128, 1 )** |![navy](./media/function-colors/color-navy.png) |
| **Color.OldLace** |**ColorValue( "#fdf5e6" )** |**RGBA( 253, 245, 230, 1 )** |![oldlace](./media/function-colors/color-oldlace.png) |
| **Color.Olive** |**ColorValue( "#808000" )** |**RGBA( 128, 128, 0, 1 )** |![olive](./media/function-colors/color-olive.png) |
| **Color.OliveDrab** |**ColorValue( "#6b8e23" )** |**RGBA( 107, 142, 35, 1 )** |![olivedrab](./media/function-colors/color-olivedrab.png) |
| **Color.Orange** |**ColorValue( "#ffa500" )** |**RGBA( 255, 165, 0, 1 )** |![orange](./media/function-colors/color-orange.png) |
| **Color.OrangeRed** |**ColorValue( "#ff4500" )** |**RGBA( 255, 69, 0, 1 )** |![orangered](./media/function-colors/color-orangered.png) |
| **Color.Orchid** |**ColorValue( "#da70d6" )** |**RGBA( 218, 112, 214, 1 )** |![orchid](./media/function-colors/color-orchid.png) |
| **Color.PaleGoldenRod** |**ColorValue( "#eee8aa" )** |**RGBA( 238, 232, 170, 1 )** |![palegoldenrod](./media/function-colors/color-palegoldenrod.png) |
| **Color.PaleGreen** |**ColorValue( "#98fb98" )** |**RGBA( 152, 251, 152, 1 )** |![palegreen](./media/function-colors/color-palegreen.png) |
| **Color.PaleTurquoise** |**ColorValue( "#afeeee" )** |**RGBA( 175, 238, 238, 1 )** |![paleturquoise](./media/function-colors/color-paleturquoise.png) |
| **Color.PaleVioletRed** |**ColorValue( "#db7093" )** |**RGBA( 219, 112, 147, 1 )** |![palevioletred](./media/function-colors/color-palevioletred.png) |
| **Color.PapayaWhip** |**ColorValue( "#ffefd5" )** |**RGBA( 255, 239, 213, 1 )** |![papayawhip](./media/function-colors/color-papayawhip.png) |
| **Color.PeachPuff** |**ColorValue( "#ffdab9" )** |**RGBA( 255, 218, 185, 1 )** |![peachpuff](./media/function-colors/color-peachpuff.png) |
| **Color.Peru** |**ColorValue( "#cd853f" )** |**RGBA( 205, 133, 63, 1 )** |![peru](./media/function-colors/color-peru.png) |
| **Color.Pink** |**ColorValue( "#ffc0cb" )** |**RGBA( 255, 192, 203, 1 )** |![pink](./media/function-colors/color-pink.png) |
| **Color.Plum** |**ColorValue( "#dda0dd" )** |**RGBA( 221, 160, 221, 1 )** |![plum](./media/function-colors/color-plum.png) |
| **Color.PowderBlue** |**ColorValue( "#b0e0e6" )** |**RGBA( 176, 224, 230, 1 )** |![powderblue](./media/function-colors/color-powderblue.png) |
| **Color.Purple** |**ColorValue( "#800080" )** |**RGBA( 128, 0, 128, 1 )** |![purple](./media/function-colors/color-purple.png) |
| **Color.Red** |**ColorValue( "#ff0000" )** |**RGBA( 255, 0, 0, 1 )** |![red](./media/function-colors/color-red.png) |
| **Color.RosyBrown** |**ColorValue( "#bc8f8f" )** |**RGBA( 188, 143, 143, 1 )** |![rosybrown](./media/function-colors/color-rosybrown.png) |
| **Color.RoyalBlue** |**ColorValue( "#4169e1" )** |**RGBA( 65, 105, 225, 1 )** |![royalblue](./media/function-colors/color-royalblue.png) |
| **Color.SaddleBrown** |**ColorValue( "#8b4513" )** |**RGBA( 139, 69, 19, 1 )** |![saddlebrown](./media/function-colors/color-saddlebrown.png) |
| **Color.Salmon** |**ColorValue( "#fa8072" )** |**RGBA( 250, 128, 114, 1 )** |![salmon](./media/function-colors/color-salmon.png) |
| **Color.SandyBrown** |**ColorValue( "#f4a460" )** |**RGBA( 244, 164, 96, 1 )** |![sandybrown](./media/function-colors/color-sandybrown.png) |
| **Color.SeaGreen** |**ColorValue( "#2e8b57" )** |**RGBA( 46, 139, 87, 1 )** |![seagreen](./media/function-colors/color-seagreen.png) |
| **Color.SeaShell** |**ColorValue( "#fff5ee" )** |**RGBA( 255, 245, 238, 1 )** |![seashell](./media/function-colors/color-seashell.png) |
| **Color.Sienna** |**ColorValue( "#a0522d" )** |**RGBA( 160, 82, 45, 1 )** |![sienna](./media/function-colors/color-sienna.png) |
| **Color.Silver** |**ColorValue( "#c0c0c0" )** |**RGBA( 192, 192, 192, 1 )** |![silver](./media/function-colors/color-silver.png) |
| **Color.SkyBlue** |**ColorValue( "#87ceeb" )** |**RGBA( 135, 206, 235, 1 )** |![skyblue](./media/function-colors/color-skyblue.png) |
| **Color.SlateBlue** |**ColorValue( "#6a5acd" )** |**RGBA( 106, 90, 205, 1 )** |![slateblue](./media/function-colors/color-slateblue.png) |
| **Color.SlateGray** |**ColorValue( "#708090" )** |**RGBA( 112, 128, 144, 1 )** |![slategray](./media/function-colors/color-slategray.png) |
| **Color.SlateGrey** |**ColorValue( "#708090" )** |**RGBA( 112, 128, 144, 1 )** |![slategrey](./media/function-colors/color-slategrey.png) |
| **Color.Snow** |**ColorValue( "#fffafa" )** |**RGBA( 255, 250, 250, 1 )** |![snow](./media/function-colors/color-snow.png) |
| **Color.SpringGreen** |**ColorValue( "#00ff7f" )** |**RGBA( 0, 255, 127, 1 )** |![springgreen](./media/function-colors/color-springgreen.png) |
| **Color.SteelBlue** |**ColorValue( "#4682b4" )** |**RGBA( 70, 130, 180, 1 )** |![steelblue](./media/function-colors/color-steelblue.png) |
| **Color.Tan** |**ColorValue( "#d2b48c" )** |**RGBA( 210, 180, 140, 1 )** |![tan](./media/function-colors/color-tan.png) |
| **Color.Teal** |**ColorValue( "#008080" )** |**RGBA( 0, 128, 128, 1 )** |![teal](./media/function-colors/color-teal.png) |
| **Color.Thistle** |**ColorValue( "#d8bfd8" )** |**RGBA( 216, 191, 216, 1 )** |![thistle](./media/function-colors/color-thistle.png) |
| **Color.Tomato** |**ColorValue( "#ff6347" )** |**RGBA( 255, 99, 71, 1 )** |![tomato](./media/function-colors/color-tomato.png) |
| **Color.Turquoise** |**ColorValue( "#40e0d0" )** |**RGBA( 64, 224, 208, 1 )** |![turquoise](./media/function-colors/color-turquoise.png) |
| **Color.Violet** |**ColorValue( "#ee82ee" )** |**RGBA( 238, 130, 238, 1 )** |![violet](./media/function-colors/color-violet.png) |
| **Color.Wheat** |**ColorValue( "#f5deb3" )** |**RGBA( 245, 222, 179, 1 )** |![wheat](./media/function-colors/color-wheat.png) |
| **Color.White** |**ColorValue( "#ffffff" )** |**RGBA( 255, 255, 255, 1 )** |![white](./media/function-colors/color-white.png) |
| **Color.WhiteSmoke** |**ColorValue( "#f5f5f5" )** |**RGBA( 245, 245, 245, 1 )** |![whitesmoke](./media/function-colors/color-whitesmoke.png) |
| **Color.Yellow** |**ColorValue( "#ffff00" )** |**RGBA( 255, 255, 0, 1 )** |![yellow](./media/function-colors/color-yellow.png) |
| **Color.YellowGreen** |**ColorValue( "#9acd32" )** |**RGBA( 154, 205, 50, 1 )** |![yellowgreen](./media/function-colors/color-yellowgreen.png) |

