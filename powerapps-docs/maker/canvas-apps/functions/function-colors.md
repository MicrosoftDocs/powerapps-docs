---
title: Color enumeration and ColorFade, ColorValue, and RGBA functions | Microsoft Docs
description: Reference information for the Color enumeration and ColorFade, ColorValue, and RGBA functions in PowerApps, including syntax and examples
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: anneta
ms.date: 05/02/2019
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

The **ColorValue** function returns a color based on a CSS color string.  The string can be in one of three forms:
- CSS color names, such as "RoxyBrown" or "OliveDrab".  Spaces are omitted.  See the list of supported colors below.
- 6 digit hex value, such as "#ffd700" (which is the same as "Gold").  The string is in the format "#rrggbb" where *rr* is the two hexadecimal digit red portion, *gg* the green, and *bb* the blue.  
- 8 digit hex value, such as "#ff7f5080" (which is the same as "Coral" with a 50% alpha channel).  The string is in the format "#rrggbbaa" where *rr*, *gg*, and *bb* are identical to the 6 digit form.  Alpha channel is represented by *aa* with "00" representing fully transparent and "ff" representing fully opaque.   

The **RGBA** function returns a color based on Red, Green, and Blue color components.  It also includes an Alpha component used for mixing colors of objects layered on top of one another.  Alpha varies from 0 or 0% which is fully transparent and invisible to 1 or 100% which is fully opaque and completely blocks out layers below.

The **ColorFade** function returns a brighter or darker version of a color.  The amount of fade varies from -1 which fully darkens a color to black, to 0 which has no impact on the color, to 1 which fully brightens a color to white.  

## Syntax
**Color**.*ColorName*

* *ColorName* - Required.  A Cascading Style Sheet (CSS) color name.  See list below of possible enumeration values.

**ColorValue**( *CSSColor* )

* *CSSColor* - Required.  A Cascading Style Sheet (CSS) color definition.  Both names of CSS colors, such as "OliveDrab", and hex values, such as "#6b8e23" and "#7fffd420", may be used. Hex values can either be in the form "#rrggbb" or "#rrggbbaa". 

**RGBA**( *Red*, *Green*, *Blue*, *Alpha* )

* *Red*, *Green*, *Blue* - Required.  Color component values, ranging from 0 (no saturation) to 255 (full saturation).
* *Alpha* - Required.  Alpha component, ranging from 0 (fully transparent) to 1 (fully opaque).  You can also use a percentage, 0% to 100%.

**ColorFade**( *Color*, *FadeAmount* )

* *Color* - Required.  A color value such as **Color.Red** or the output from **ColorValue** or **RGBA**.
* *FadeAmount* - Required.  A number between -1 and 1.  -1 fully darkens a color to black, 0 has no impact on the color, and 1 fully brightens a color to white.  

## Built in colors

| Color enumeration | ColorValue with Hex Code | RGBA | Color Swatch |
| --- | --- | --- | --- |
| **Color.AliceBlue** |**ColorValue(&nbsp;"#f0f8ff"&nbsp;)**<br>**ColorValue(&nbsp;"aliceblue"&nbsp;)** |**RGBA(&nbsp;240,&nbsp;248,&nbsp;255,&nbsp;1&nbsp;)** |![aliceblue](./media/function-colors/color-aliceblue.png) |
| **Color.AntiqueWhite** |**ColorValue(&nbsp;"#faebd7"&nbsp;)**<br>**ColorValue(&nbsp;"AntiqueWhite"&nbsp;)** |**RGBA(&nbsp;250,&nbsp;235,&nbsp;215,&nbsp;1&nbsp;)** |![antiquewhite](./media/function-colors/color-antiquewhite.png) |
| **Color.Aqua** |**ColorValue(&nbsp;"#00ffff"&nbsp;)**<br>**ColorValue(&nbsp;"AQUA"&nbsp;)** |**RGBA(&nbsp;0,&nbsp;255,&nbsp;255,&nbsp;1&nbsp;)** |![aqua](./media/function-colors/color-aqua.png) |
| **Color.Aquamarine** |**ColorValue(&nbsp;"#7fffd4"&nbsp;)**<br>**ColorValue(&nbsp;"Aquamarine"&nbsp;)** |**RGBA(&nbsp;127,&nbsp;255,&nbsp;212,&nbsp;1&nbsp;)** |![aquamarine](./media/function-colors/color-aquamarine.png) |
| **Color.Azure** |**ColorValue(&nbsp;"#f0ffff"&nbsp;)**<br>**ColorValue(&nbsp;"azure"&nbsp;)** |**RGBA(&nbsp;240,&nbsp;255,&nbsp;255,&nbsp;1&nbsp;)** |![azure](./media/function-colors/color-azure.png) |
| **Color.Beige** |**ColorValue(&nbsp;"#f5f5dc"&nbsp;)**<br>**ColorValue(&nbsp;"Beige"&nbsp;)** |**RGBA(&nbsp;245,&nbsp;245,&nbsp;220,&nbsp;1&nbsp;)** |![beige](./media/function-colors/color-beige.png) |
| **Color.Bisque** |**ColorValue(&nbsp;"#ffe4c4"&nbsp;)**<br>**ColorValue(&nbsp;"BISQUE"&nbsp;)** |**RGBA(&nbsp;255,&nbsp;228,&nbsp;196,&nbsp;1&nbsp;)** |![bisque](./media/function-colors/color-bisque.png) |
| **Color.Black** |**ColorValue(&nbsp;"#000000"&nbsp;)**<br>**ColorValue(&nbsp;"Black"&nbsp;)** |**RGBA(&nbsp;0,&nbsp;0,&nbsp;0,&nbsp;1&nbsp;)** |![black](./media/function-colors/color-black.png) |
| **Color.BlanchedAlmond** |**ColorValue(&nbsp;"#ffebcd"&nbsp;)**<br>**ColorValue(&nbsp;"blanchedalmond"&nbsp;)** |**RGBA(&nbsp;255,&nbsp;235,&nbsp;205,&nbsp;1&nbsp;)** |![blanchedalmond](./media/function-colors/color-blanchedalmond.png) |
| **Color.Blue** |**ColorValue(&nbsp;"#0000ff"&nbsp;)**<br>**ColorValue(&nbsp;"Blue"&nbsp;)** |**RGBA(&nbsp;0,&nbsp;0,&nbsp;255,&nbsp;1&nbsp;)** |![blue](./media/function-colors/color-blue.png) |
| **Color.BlueViolet** |**ColorValue(&nbsp;"#8a2be2"&nbsp;)**<br>**ColorValue(&nbsp;"BLUEVIOLET"&nbsp;)** |**RGBA(&nbsp;138,&nbsp;43,&nbsp;226,&nbsp;1&nbsp;)** |![blueviolet](./media/function-colors/color-blueviolet.png) |
| **Color.Brown** |**ColorValue(&nbsp;"#a52a2a"&nbsp;)**<br>**ColorValue(&nbsp;"Brown"&nbsp;)** |**RGBA(&nbsp;165,&nbsp;42,&nbsp;42,&nbsp;1&nbsp;)** |![brown](./media/function-colors/color-brown.png) |
| **Color.Burlywood** |**ColorValue(&nbsp;"#deb887"&nbsp;)**<br>**ColorValue(&nbsp;"burlywood"&nbsp;)** |**RGBA(&nbsp;222,&nbsp;184,&nbsp;135,&nbsp;1&nbsp;)** |![burlywood](./media/function-colors/color-burlywood.png) |
| **Color.CadetBlue** |**ColorValue(&nbsp;"#5f9ea0"&nbsp;)**<br>**ColorValue(&nbsp;"CadetBlue"&nbsp;)** |**RGBA(&nbsp;95,&nbsp;158,&nbsp;160,&nbsp;1&nbsp;)** |![cadetblue](./media/function-colors/color-cadetblue.png) |
| **Color.Chartreuse** |**ColorValue(&nbsp;"#7fff00"&nbsp;)**<br>**ColorValue(&nbsp;"CHARTREUSE"&nbsp;)** |**RGBA(&nbsp;127,&nbsp;255,&nbsp;0,&nbsp;1&nbsp;)** |![chartreuse](./media/function-colors/color-chartreuse.png) |
| **Color.Chocolate** |**ColorValue(&nbsp;"#d2691e"&nbsp;)**<br>**ColorValue(&nbsp;"Chocolate"&nbsp;)** |**RGBA(&nbsp;210,&nbsp;105,&nbsp;30,&nbsp;1&nbsp;)** |![chocolate](./media/function-colors/color-chocolate.png) |
| **Color.Coral** |**ColorValue(&nbsp;"#ff7f50"&nbsp;)**<br>**ColorValue(&nbsp;"coral"&nbsp;)** |**RGBA(&nbsp;255,&nbsp;127,&nbsp;80,&nbsp;1&nbsp;)** |![coral](./media/function-colors/color-coral.png) |
| **Color.CornflowerBlue** |**ColorValue(&nbsp;"#6495ed"&nbsp;)**<br>**ColorValue(&nbsp;"CornflowerBlue"&nbsp;)** |**RGBA(&nbsp;100,&nbsp;149,&nbsp;237,&nbsp;1&nbsp;)** |![cornflowerblue](./media/function-colors/color-cornflowerblue.png) |
| **Color.Cornsilk** |**ColorValue(&nbsp;"#fff8dc"&nbsp;)**<br>**ColorValue(&nbsp;"CORNSILK"&nbsp;)** |**RGBA(&nbsp;255,&nbsp;248,&nbsp;220,&nbsp;1&nbsp;)** |![cornsilk](./media/function-colors/color-cornsilk.png) |
| **Color.Crimson** |**ColorValue(&nbsp;"#dc143c"&nbsp;)**<br>**ColorValue(&nbsp;"Crimson"&nbsp;)** |**RGBA(&nbsp;220,&nbsp;20,&nbsp;60,&nbsp;1&nbsp;)** |![crimson](./media/function-colors/color-crimson.png) |
| **Color.Cyan** |**ColorValue(&nbsp;"#00ffff"&nbsp;)**<br>**ColorValue(&nbsp;"cyan"&nbsp;)** |**RGBA(&nbsp;0,&nbsp;255,&nbsp;255,&nbsp;1&nbsp;)** |![cyan](./media/function-colors/color-cyan.png) |
| **Color.DarkBlue** |**ColorValue(&nbsp;"#00008b"&nbsp;)**<br>**ColorValue(&nbsp;"DarkBlue"&nbsp;)** |**RGBA(&nbsp;0,&nbsp;0,&nbsp;139,&nbsp;1&nbsp;)** |![darkblue](./media/function-colors/color-darkblue.png) |
| **Color.DarkCyan** |**ColorValue(&nbsp;"#008b8b"&nbsp;)**<br>**ColorValue(&nbsp;"DARKCYAN"&nbsp;)** |**RGBA(&nbsp;0,&nbsp;139,&nbsp;139,&nbsp;1&nbsp;)** |![darkcyan](./media/function-colors/color-darkcyan.png) |
| **Color.DarkGoldenRod** |**ColorValue(&nbsp;"#b8860b"&nbsp;)**<br>**ColorValue(&nbsp;"DarkGoldenRod"&nbsp;)** |**RGBA(&nbsp;184,&nbsp;134,&nbsp;11,&nbsp;1&nbsp;)** |![darkgoldenrod](./media/function-colors/color-darkgoldenrod.png) |
| **Color.DarkGray** |**ColorValue(&nbsp;"#a9a9a9"&nbsp;)**<br>**ColorValue(&nbsp;"darkgray"&nbsp;)** |**RGBA(&nbsp;169,&nbsp;169,&nbsp;169,&nbsp;1&nbsp;)** |![darkgray](./media/function-colors/color-darkgray.png) |
| **Color.DarkGreen** |**ColorValue(&nbsp;"#006400"&nbsp;)**<br>**ColorValue(&nbsp;"DarkGreen"&nbsp;)** |**RGBA(&nbsp;0,&nbsp;100,&nbsp;0,&nbsp;1&nbsp;)** |![darkgreen](./media/function-colors/color-darkgreen.png) |
| **Color.DarkGrey** |**ColorValue(&nbsp;"#a9a9a9"&nbsp;)**<br>**ColorValue(&nbsp;"DARKGREY"&nbsp;)** |**RGBA(&nbsp;169,&nbsp;169,&nbsp;169,&nbsp;1&nbsp;)** |![darkgrey](./media/function-colors/color-darkgrey.png) |
| **Color.DarkKhaki** |**ColorValue(&nbsp;"#bdb76b"&nbsp;)**<br>**ColorValue(&nbsp;"DarkKhaki"&nbsp;)** |**RGBA(&nbsp;189,&nbsp;183,&nbsp;107,&nbsp;1&nbsp;)** |![darkkhaki](./media/function-colors/color-darkkhaki.png) |
| **Color.DarkMagenta** |**ColorValue(&nbsp;"#8b008b"&nbsp;)**<br>**ColorValue(&nbsp;"darkmagenta"&nbsp;)** |**RGBA(&nbsp;139,&nbsp;0,&nbsp;139,&nbsp;1&nbsp;)** |![darkmagenta](./media/function-colors/color-darkmagenta.png) |
| **Color.DarkOliveGreen** |**ColorValue(&nbsp;"#556b2f"&nbsp;)**<br>**ColorValue(&nbsp;"DarkOliveGreen"&nbsp;)** |**RGBA(&nbsp;85,&nbsp;107,&nbsp;47,&nbsp;1&nbsp;)** |![darkolivegreen](./media/function-colors/color-darkolivegreen.png) |
| **Color.DarkOrange** |**ColorValue(&nbsp;"#ff8c00"&nbsp;)**<br>**ColorValue(&nbsp;"DARKORANGE"&nbsp;)** |**RGBA(&nbsp;255,&nbsp;140,&nbsp;0,&nbsp;1&nbsp;)** |![darkorange](./media/function-colors/color-darkorange.png) |
| **Color.DarkOrchid** |**ColorValue(&nbsp;"#9932cc"&nbsp;)**<br>**ColorValue(&nbsp;"DarkOrchid"&nbsp;)** |**RGBA(&nbsp;153,&nbsp;50,&nbsp;204,&nbsp;1&nbsp;)** |![darkorchid](./media/function-colors/color-darkorchid.png) |
| **Color.DarkRed** |**ColorValue(&nbsp;"#8b0000"&nbsp;)**<br>**ColorValue(&nbsp;"darkred"&nbsp;)** |**RGBA(&nbsp;139,&nbsp;0,&nbsp;0,&nbsp;1&nbsp;)** |![darkred](./media/function-colors/color-darkred.png) |
| **Color.DarkSalmon** |**ColorValue(&nbsp;"#e9967a"&nbsp;)**<br>**ColorValue(&nbsp;"DarkSalmon"&nbsp;)** |**RGBA(&nbsp;233,&nbsp;150,&nbsp;122,&nbsp;1&nbsp;)** |![darksalmon](./media/function-colors/color-darksalmon.png) |
| **Color.DarkSeaGreen** |**ColorValue(&nbsp;"#8fbc8f"&nbsp;)**<br>**ColorValue(&nbsp;"DARKSEAGREEN"&nbsp;)** |**RGBA(&nbsp;143,&nbsp;188,&nbsp;143,&nbsp;1&nbsp;)** |![darkseagreen](./media/function-colors/color-darkseagreen.png) |
| **Color.DarkSlateBlue** |**ColorValue(&nbsp;"#483d8b"&nbsp;)**<br>**ColorValue(&nbsp;"DarkSlateBlue"&nbsp;)** |**RGBA(&nbsp;72,&nbsp;61,&nbsp;139,&nbsp;1&nbsp;)** |![darkslateblue](./media/function-colors/color-darkslateblue.png) |
| **Color.DarkSlateGray** |**ColorValue(&nbsp;"#2f4f4f"&nbsp;)**<br>**ColorValue(&nbsp;"darkslategray"&nbsp;)** |**RGBA(&nbsp;47,&nbsp;79,&nbsp;79,&nbsp;1&nbsp;)** |![darkslategray](./media/function-colors/color-darkslategray.png) |
| **Color.DarkSlateGrey** |**ColorValue(&nbsp;"#2f4f4f"&nbsp;)**<br>**ColorValue(&nbsp;"DarkSlateGrey"&nbsp;)** |**RGBA(&nbsp;47,&nbsp;79,&nbsp;79,&nbsp;1&nbsp;)** |![darkslategrey](./media/function-colors/color-darkslategrey.png) |
| **Color.DarkTurquoise** |**ColorValue(&nbsp;"#00ced1"&nbsp;)**<br>**ColorValue(&nbsp;"DARKTURQUOISE"&nbsp;)** |**RGBA(&nbsp;0,&nbsp;206,&nbsp;209,&nbsp;1&nbsp;)** |![darkturquoise](./media/function-colors/color-darkturquoise.png) |
| **Color.DarkViolet** |**ColorValue(&nbsp;"#9400d3"&nbsp;)**<br>**ColorValue(&nbsp;"DarkViolet"&nbsp;)** |**RGBA(&nbsp;148,&nbsp;0,&nbsp;211,&nbsp;1&nbsp;)** |![darkviolet](./media/function-colors/color-darkviolet.png) |
| **Color.DeepPink** |**ColorValue(&nbsp;"#ff1493"&nbsp;)**<br>**ColorValue(&nbsp;"deeppink"&nbsp;)** |**RGBA(&nbsp;255,&nbsp;20,&nbsp;147,&nbsp;1&nbsp;)** |![deeppink](./media/function-colors/color-deeppink.png) |
| **Color.DeepSkyBlue** |**ColorValue(&nbsp;"#00bfff"&nbsp;)**<br>**ColorValue(&nbsp;"DeepSkyBlue"&nbsp;)** |**RGBA(&nbsp;0,&nbsp;191,&nbsp;255,&nbsp;1&nbsp;)** |![deepskyblue](./media/function-colors/color-deepskyblue.png) |
| **Color.DimGray** |**ColorValue(&nbsp;"#696969"&nbsp;)**<br>**ColorValue(&nbsp;"DIMGRAY"&nbsp;)** |**RGBA(&nbsp;105,&nbsp;105,&nbsp;105,&nbsp;1&nbsp;)** |![dimgray](./media/function-colors/color-dimgray.png) |
| **Color.DimGrey** |**ColorValue(&nbsp;"#696969"&nbsp;)**<br>**ColorValue(&nbsp;"DimGrey"&nbsp;)** |**RGBA(&nbsp;105,&nbsp;105,&nbsp;105,&nbsp;1&nbsp;)** |![dimgrey](./media/function-colors/color-dimgrey.png) |
| **Color.DodgerBlue** |**ColorValue(&nbsp;"#1e90ff"&nbsp;)**<br>**ColorValue(&nbsp;"dodgerblue"&nbsp;)** |**RGBA(&nbsp;30,&nbsp;144,&nbsp;255,&nbsp;1&nbsp;)** |![dodgerblue](./media/function-colors/color-dodgerblue.png) |
| **Color.FireBrick** |**ColorValue(&nbsp;"#b22222"&nbsp;)**<br>**ColorValue(&nbsp;"FireBrick"&nbsp;)** |**RGBA(&nbsp;178,&nbsp;34,&nbsp;34,&nbsp;1&nbsp;)** |![firebrick](./media/function-colors/color-firebrick.png) |
| **Color.FloralWhite** |**ColorValue(&nbsp;"#fffaf0"&nbsp;)**<br>**ColorValue(&nbsp;"FLORALWHITE"&nbsp;)** |**RGBA(&nbsp;255,&nbsp;250,&nbsp;240,&nbsp;1&nbsp;)** |![floralwhite](./media/function-colors/color-floralwhite.png) |
| **Color.ForestGreen** |**ColorValue(&nbsp;"#228b22"&nbsp;)**<br>**ColorValue(&nbsp;"ForestGreen"&nbsp;)** |**RGBA(&nbsp;34,&nbsp;139,&nbsp;34,&nbsp;1&nbsp;)** |![forestgreen](./media/function-colors/color-forestgreen.png) |
| **Color.Fuchsia** |**ColorValue(&nbsp;"#ff00ff"&nbsp;)**<br>**ColorValue(&nbsp;"fuchsia"&nbsp;)** |**RGBA(&nbsp;255,&nbsp;0,&nbsp;255,&nbsp;1&nbsp;)** |![fuchsia](./media/function-colors/color-fuchsia.png) |
| **Color.Gainsboro** |**ColorValue(&nbsp;"#dcdcdc"&nbsp;)**<br>**ColorValue(&nbsp;"Gainsboro"&nbsp;)** |**RGBA(&nbsp;220,&nbsp;220,&nbsp;220,&nbsp;1&nbsp;)** |![gainsboro](./media/function-colors/color-gainsboro.png) |
| **Color.GhostWhite** |**ColorValue(&nbsp;"#f8f8ff"&nbsp;)**<br>**ColorValue(&nbsp;"GHOSTWHITE"&nbsp;)** |**RGBA(&nbsp;248,&nbsp;248,&nbsp;255,&nbsp;1&nbsp;)** |![ghostwhite](./media/function-colors/color-ghostwhite.png) |
| **Color.Gold** |**ColorValue(&nbsp;"#ffd700"&nbsp;)**<br>**ColorValue(&nbsp;"Gold"&nbsp;)** |**RGBA(&nbsp;255,&nbsp;215,&nbsp;0,&nbsp;1&nbsp;)** |![gold](./media/function-colors/color-gold.png) |
| **Color.GoldenRod** |**ColorValue(&nbsp;"#daa520"&nbsp;)**<br>**ColorValue(&nbsp;"goldenrod"&nbsp;)** |**RGBA(&nbsp;218,&nbsp;165,&nbsp;32,&nbsp;1&nbsp;)** |![goldenrod](./media/function-colors/color-goldenrod.png) |
| **Color.Gray** |**ColorValue(&nbsp;"#808080"&nbsp;)**<br>**ColorValue(&nbsp;"Gray"&nbsp;)** |**RGBA(&nbsp;128,&nbsp;128,&nbsp;128,&nbsp;1&nbsp;)** |![gray](./media/function-colors/color-gray.png) |
| **Color.Green** |**ColorValue(&nbsp;"#008000"&nbsp;)**<br>**ColorValue(&nbsp;"GREEN"&nbsp;)** |**RGBA(&nbsp;0,&nbsp;128,&nbsp;0,&nbsp;1&nbsp;)** |![green](./media/function-colors/color-green.png) |
| **Color.GreenYellow** |**ColorValue(&nbsp;"#adff2f"&nbsp;)**<br>**ColorValue(&nbsp;"GreenYellow"&nbsp;)** |**RGBA(&nbsp;173,&nbsp;255,&nbsp;47,&nbsp;1&nbsp;)** |![greenyellow](./media/function-colors/color-greenyellow.png) |
| **Color.Grey** |**ColorValue(&nbsp;"#808080"&nbsp;)**<br>**ColorValue(&nbsp;"grey"&nbsp;)** |**RGBA(&nbsp;128,&nbsp;128,&nbsp;128,&nbsp;1&nbsp;)** |![grey](./media/function-colors/color-grey.png) |
| **Color.Honeydew** |**ColorValue(&nbsp;"#f0fff0"&nbsp;)**<br>**ColorValue(&nbsp;"Honeydew"&nbsp;)** |**RGBA(&nbsp;240,&nbsp;255,&nbsp;240,&nbsp;1&nbsp;)** |![honeydew](./media/function-colors/color-honeydew.png) |
| **Color.HotPink** |**ColorValue(&nbsp;"#ff69b4"&nbsp;)**<br>**ColorValue(&nbsp;"HOTPINK"&nbsp;)** |**RGBA(&nbsp;255,&nbsp;105,&nbsp;180,&nbsp;1&nbsp;)** |![hotpink](./media/function-colors/color-hotpink.png) |
| **Color.IndianRed** |**ColorValue(&nbsp;"#cd5c5c"&nbsp;)**<br>**ColorValue(&nbsp;"IndianRed"&nbsp;)** |**RGBA(&nbsp;205,&nbsp;92,&nbsp;92,&nbsp;1&nbsp;)** |![indianred](./media/function-colors/color-indianred.png) |
| **Color.Indigo** |**ColorValue(&nbsp;"#4b0082"&nbsp;)**<br>**ColorValue(&nbsp;"indigo"&nbsp;)** |**RGBA(&nbsp;75,&nbsp;0,&nbsp;130,&nbsp;1&nbsp;)** |![indigo](./media/function-colors/color-indigo.png) |
| **Color.Ivory** |**ColorValue(&nbsp;"#fffff0"&nbsp;)**<br>**ColorValue(&nbsp;"Ivory"&nbsp;)** |**RGBA(&nbsp;255,&nbsp;255,&nbsp;240,&nbsp;1&nbsp;)** |![ivory](./media/function-colors/color-ivory.png) |
| **Color.Khaki** |**ColorValue(&nbsp;"#f0e68c"&nbsp;)**<br>**ColorValue(&nbsp;"KHAKI"&nbsp;)** |**RGBA(&nbsp;240,&nbsp;230,&nbsp;140,&nbsp;1&nbsp;)** |![khaki](./media/function-colors/color-khaki.png) |
| **Color.Lavender** |**ColorValue(&nbsp;"#e6e6fa"&nbsp;)**<br>**ColorValue(&nbsp;"Lavender"&nbsp;)** |**RGBA(&nbsp;230,&nbsp;230,&nbsp;250,&nbsp;1&nbsp;)** |![lavender](./media/function-colors/color-lavender.png) |
| **Color.LavenderBlush** |**ColorValue(&nbsp;"#fff0f5"&nbsp;)**<br>**ColorValue(&nbsp;"lavenderblush"&nbsp;)** |**RGBA(&nbsp;255,&nbsp;240,&nbsp;245,&nbsp;1&nbsp;)** |![lavenderblush](./media/function-colors/color-lavenderblush.png) |
| **Color.LawnGreen** |**ColorValue(&nbsp;"#7cfc00"&nbsp;)**<br>**ColorValue(&nbsp;"LawnGreen"&nbsp;)** |**RGBA(&nbsp;124,&nbsp;252,&nbsp;0,&nbsp;1&nbsp;)** |![lawngreen](./media/function-colors/color-lawngreen.png) |
| **Color.LemonChiffon** |**ColorValue(&nbsp;"#fffacd"&nbsp;)**<br>**ColorValue(&nbsp;"LEMONCHIFFON"&nbsp;)** |**RGBA(&nbsp;255,&nbsp;250,&nbsp;205,&nbsp;1&nbsp;)** |![lemonchiffon](./media/function-colors/color-lemonchiffon.png) |
| **Color.LightBlue** |**ColorValue(&nbsp;"#add8e6"&nbsp;)**<br>**ColorValue(&nbsp;"LightBlue"&nbsp;)** |**RGBA(&nbsp;173,&nbsp;216,&nbsp;230,&nbsp;1&nbsp;)** |![lightblue](./media/function-colors/color-lightblue.png) |
| **Color.LightCoral** |**ColorValue(&nbsp;"#f08080"&nbsp;)**<br>**ColorValue(&nbsp;"lightcoral"&nbsp;)** |**RGBA(&nbsp;240,&nbsp;128,&nbsp;128,&nbsp;1&nbsp;)** |![lightcoral](./media/function-colors/color-lightcoral.png) |
| **Color.LightCyan** |**ColorValue(&nbsp;"#e0ffff"&nbsp;)**<br>**ColorValue(&nbsp;"LightCyan"&nbsp;)** |**RGBA(&nbsp;224,&nbsp;255,&nbsp;255,&nbsp;1&nbsp;)** |![lightcyan](./media/function-colors/color-lightcyan.png) |
| **Color.LightGoldenRodYellow** |**ColorValue(&nbsp;"#fafad2"&nbsp;)**<br>**ColorValue(&nbsp;"lightgoldenrodyellow"&nbsp;)** |**RGBA(&nbsp;250,&nbsp;250,&nbsp;210,&nbsp;1&nbsp;)** |![lightgoldenrodyellow](./media/function-colors/color-lightgoldenrodyellow.png) |
| **Color.LightGray** |**ColorValue(&nbsp;"#d3d3d3"&nbsp;)**<br>**ColorValue(&nbsp;"LightGray"&nbsp;)** |**RGBA(&nbsp;211,&nbsp;211,&nbsp;211,&nbsp;1&nbsp;)** |![lightgray](./media/function-colors/color-lightgray.png) |
| **Color.LightGreen** |**ColorValue(&nbsp;"#90ee90"&nbsp;)**<br>**ColorValue(&nbsp;"lightgreen"&nbsp;)** |**RGBA(&nbsp;144,&nbsp;238,&nbsp;144,&nbsp;1&nbsp;)** |![lightgreen](./media/function-colors/color-lightgreen.png) |
| **Color.LightGrey** |**ColorValue(&nbsp;"#d3d3d3"&nbsp;)**<br>**ColorValue(&nbsp;"LightGrey"&nbsp;)** |**RGBA(&nbsp;211,&nbsp;211,&nbsp;211,&nbsp;1&nbsp;)** |![lightgrey](./media/function-colors/color-lightgrey.png) |
| **Color.LightPink** |**ColorValue(&nbsp;"#ffb6c1"&nbsp;)**<br>**ColorValue(&nbsp;"LIGHTPINK"&nbsp;)** |**RGBA(&nbsp;255,&nbsp;182,&nbsp;193,&nbsp;1&nbsp;)** |![lightpink](./media/function-colors/color-lightpink.png) |
| **Color.LightSalmon** |**ColorValue(&nbsp;"#ffa07a"&nbsp;)**<br>**ColorValue(&nbsp;"LightSalmon"&nbsp;)** |**RGBA(&nbsp;255,&nbsp;160,&nbsp;122,&nbsp;1&nbsp;)** |![lightsalmon](./media/function-colors/color-lightsalmon.png) |
| **Color.LightSeaGreen** |**ColorValue(&nbsp;"#20b2aa"&nbsp;)**<br>**ColorValue(&nbsp;"lightseagreen"&nbsp;)** |**RGBA(&nbsp;32,&nbsp;178,&nbsp;170,&nbsp;1&nbsp;)** |![lightseagreen](./media/function-colors/color-lightseagreen.png) |
| **Color.LightSkyBlue** |**ColorValue(&nbsp;"#87cefa"&nbsp;)**<br>**ColorValue(&nbsp;"LightSkyBlue"&nbsp;)** |**RGBA(&nbsp;135,&nbsp;206,&nbsp;250,&nbsp;1&nbsp;)** |![lightskyblue](./media/function-colors/color-lightskyblue.png) |
| **Color.LightSlateGray** |**ColorValue(&nbsp;"#778899"&nbsp;)**<br>**ColorValue(&nbsp;"LIGHTSLATEGRAY"&nbsp;)** |**RGBA(&nbsp;119,&nbsp;136,&nbsp;153,&nbsp;1&nbsp;)** |![lightslategray](./media/function-colors/color-lightslategray.png) |
| **Color.LightSlateGrey** |**ColorValue(&nbsp;"#778899"&nbsp;)**<br>**ColorValue(&nbsp;"LightSlateGrey"&nbsp;)** |**RGBA(&nbsp;119,&nbsp;136,&nbsp;153,&nbsp;1&nbsp;)** |![lightslategrey](./media/function-colors/color-lightslategrey.png) |
| **Color.LightSteelBlue** |**ColorValue(&nbsp;"#b0c4de"&nbsp;)**<br>**ColorValue(&nbsp;"lightsteelblue"&nbsp;)** |**RGBA(&nbsp;176,&nbsp;196,&nbsp;222,&nbsp;1&nbsp;)** |![lightsteelblue](./media/function-colors/color-lightsteelblue.png) |
| **Color.LightYellow** |**ColorValue(&nbsp;"#ffffe0"&nbsp;)**<br>**ColorValue(&nbsp;"LightYellow"&nbsp;)** |**RGBA(&nbsp;255,&nbsp;255,&nbsp;224,&nbsp;1&nbsp;)** |![lightyellow](./media/function-colors/color-lightyellow.png) |
| **Color.Lime** |**ColorValue(&nbsp;"#00ff00"&nbsp;)**<br>**ColorValue(&nbsp;"LIME"&nbsp;)** |**RGBA(&nbsp;0,&nbsp;255,&nbsp;0,&nbsp;1&nbsp;)** |![lime](./media/function-colors/color-lime.png) |
| **Color.LimeGreen** |**ColorValue(&nbsp;"#32cd32"&nbsp;)**<br>**ColorValue(&nbsp;"LimeGreen"&nbsp;)** |**RGBA(&nbsp;50,&nbsp;205,&nbsp;50,&nbsp;1&nbsp;)** |![limegreen](./media/function-colors/color-limegreen.png) |
| **Color.Linen** |**ColorValue(&nbsp;"#faf0e6"&nbsp;)**<br>**ColorValue(&nbsp;"linen"&nbsp;)** |**RGBA(&nbsp;250,&nbsp;240,&nbsp;230,&nbsp;1&nbsp;)** |![linen](./media/function-colors/color-linen.png) |
| **Color.Magenta** |**ColorValue(&nbsp;"#ff00ff"&nbsp;)**<br>**ColorValue(&nbsp;"Magenta"&nbsp;)** |**RGBA(&nbsp;255,&nbsp;0,&nbsp;255,&nbsp;1&nbsp;)** |![magenta](./media/function-colors/color-magenta.png) |
| **Color.Maroon** |**ColorValue(&nbsp;"#800000"&nbsp;)**<br>**ColorValue(&nbsp;"MAROON"&nbsp;)** |**RGBA(&nbsp;128,&nbsp;0,&nbsp;0,&nbsp;1&nbsp;)** |![maroon](./media/function-colors/color-maroon.png) |
| **Color.MediumAquamarine** |**ColorValue(&nbsp;"#66cdaa"&nbsp;)**<br>**ColorValue(&nbsp;"MediumAquamarine"&nbsp;)** |**RGBA(&nbsp;102,&nbsp;205,&nbsp;170,&nbsp;1&nbsp;)** |![mediumaquamarine](./media/function-colors/color-mediumaquamarine.png) |
| **Color.MediumBlue** |**ColorValue(&nbsp;"#0000cd"&nbsp;)**<br>**ColorValue(&nbsp;"mediumblue"&nbsp;)** |**RGBA(&nbsp;0,&nbsp;0,&nbsp;205,&nbsp;1&nbsp;)** |![mediumblue](./media/function-colors/color-mediumblue.png) |
| **Color.MediumOrchid** |**ColorValue(&nbsp;"#ba55d3"&nbsp;)**<br>**ColorValue(&nbsp;"MediumOrchid"&nbsp;)** |**RGBA(&nbsp;186,&nbsp;85,&nbsp;211,&nbsp;1&nbsp;)** |![mediumorchid](./media/function-colors/color-mediumorchid.png) |
| **Color.MediumPurple** |**ColorValue(&nbsp;"#9370db"&nbsp;)**<br>**ColorValue(&nbsp;"MEDIUMPURPLE"&nbsp;)** |**RGBA(&nbsp;147,&nbsp;112,&nbsp;219,&nbsp;1&nbsp;)** |![mediumpurple](./media/function-colors/color-mediumpurple.png) |
| **Color.MediumSeaGreen** |**ColorValue(&nbsp;"#3cb371"&nbsp;)**<br>**ColorValue(&nbsp;"MediumSeaGreen"&nbsp;)** |**RGBA(&nbsp;60,&nbsp;179,&nbsp;113,&nbsp;1&nbsp;)** |![mediumseagreen](./media/function-colors/color-mediumseagreen.png) |
| **Color.MediumSlateBlue** |**ColorValue(&nbsp;"#7b68ee"&nbsp;)**<br>**ColorValue(&nbsp;"mediumslateblue"&nbsp;)** |**RGBA(&nbsp;123,&nbsp;104,&nbsp;238,&nbsp;1&nbsp;)** |![mediumslateblue](./media/function-colors/color-mediumslateblue.png) |
| **Color.MediumSpringGreen** |**ColorValue(&nbsp;"#00fa9a"&nbsp;)**<br>**ColorValue(&nbsp;"MediumSpringGreen"&nbsp;)** |**RGBA(&nbsp;0,&nbsp;250,&nbsp;154,&nbsp;1&nbsp;)** |![mediumspringgreen](./media/function-colors/color-mediumspringgreen.png) |
| **Color.MediumTurquoise** |**ColorValue(&nbsp;"#48d1cc"&nbsp;)**<br>**ColorValue(&nbsp;"MEDIUMTURQUOISE"&nbsp;)** |**RGBA(&nbsp;72,&nbsp;209,&nbsp;204,&nbsp;1&nbsp;)** |![mediumturquoise](./media/function-colors/color-mediumturquoise.png) |
| **Color.MediumVioletRed** |**ColorValue(&nbsp;"#c71585"&nbsp;)**<br>**ColorValue(&nbsp;"MediumVioletRed"&nbsp;)** |**RGBA(&nbsp;199,&nbsp;21,&nbsp;133,&nbsp;1&nbsp;)** |![mediumvioletred](./media/function-colors/color-mediumvioletred.png) |
| **Color.MidnightBlue** |**ColorValue(&nbsp;"#191970"&nbsp;)**<br>**ColorValue(&nbsp;"midnightblue"&nbsp;)** |**RGBA(&nbsp;25,&nbsp;25,&nbsp;112,&nbsp;1&nbsp;)** |![midnightblue](./media/function-colors/color-midnightblue.png) |
| **Color.MintCream** |**ColorValue(&nbsp;"#f5fffa"&nbsp;)**<br>**ColorValue(&nbsp;"MintCream"&nbsp;)** |**RGBA(&nbsp;245,&nbsp;255,&nbsp;250,&nbsp;1&nbsp;)** |![mintcream](./media/function-colors/color-mintcream.png) |
| **Color.MistyRose** |**ColorValue(&nbsp;"#ffe4e1"&nbsp;)**<br>**ColorValue(&nbsp;"MISTYROSE"&nbsp;)** |**RGBA(&nbsp;255,&nbsp;228,&nbsp;225,&nbsp;1&nbsp;)** |![mistyrose](./media/function-colors/color-mistyrose.png) |
| **Color.Moccasin** |**ColorValue(&nbsp;"#ffe4b5"&nbsp;)**<br>**ColorValue(&nbsp;"Moccasin"&nbsp;)** |**RGBA(&nbsp;255,&nbsp;228,&nbsp;181,&nbsp;1&nbsp;)** |![moccasin](./media/function-colors/color-moccasin.png) |
| **Color.NavajoWhite** |**ColorValue(&nbsp;"#ffdead"&nbsp;)**<br>**ColorValue(&nbsp;"navajowhite"&nbsp;)** |**RGBA(&nbsp;255,&nbsp;222,&nbsp;173,&nbsp;1&nbsp;)** |![navajowhite](./media/function-colors/color-navajowhite.png) |
| **Color.Navy** |**ColorValue(&nbsp;"#000080"&nbsp;)**<br>**ColorValue(&nbsp;"Navy"&nbsp;)** |**RGBA(&nbsp;0,&nbsp;0,&nbsp;128,&nbsp;1&nbsp;)** |![navy](./media/function-colors/color-navy.png) |
| **Color.OldLace** |**ColorValue(&nbsp;"#fdf5e6"&nbsp;)**<br>**ColorValue(&nbsp;"OLDLACE"&nbsp;)** |**RGBA(&nbsp;253,&nbsp;245,&nbsp;230,&nbsp;1&nbsp;)** |![oldlace](./media/function-colors/color-oldlace.png) |
| **Color.Olive** |**ColorValue(&nbsp;"#808000"&nbsp;)**<br>**ColorValue(&nbsp;"Olive"&nbsp;)** |**RGBA(&nbsp;128,&nbsp;128,&nbsp;0,&nbsp;1&nbsp;)** |![olive](./media/function-colors/color-olive.png) |
| **Color.OliveDrab** |**ColorValue(&nbsp;"#6b8e23"&nbsp;)**<br>**ColorValue(&nbsp;"olivedrab"&nbsp;)** |**RGBA(&nbsp;107,&nbsp;142,&nbsp;35,&nbsp;1&nbsp;)** |![olivedrab](./media/function-colors/color-olivedrab.png) |
| **Color.Orange** |**ColorValue(&nbsp;"#ffa500"&nbsp;)**<br>**ColorValue(&nbsp;"Orange"&nbsp;)** |**RGBA(&nbsp;255,&nbsp;165,&nbsp;0,&nbsp;1&nbsp;)** |![orange](./media/function-colors/color-orange.png) |
| **Color.OrangeRed** |**ColorValue(&nbsp;"#ff4500"&nbsp;)**<br>**ColorValue(&nbsp;"ORANGERED"&nbsp;)** |**RGBA(&nbsp;255,&nbsp;69,&nbsp;0,&nbsp;1&nbsp;)** |![orangered](./media/function-colors/color-orangered.png) |
| **Color.Orchid** |**ColorValue(&nbsp;"#da70d6"&nbsp;)**<br>**ColorValue(&nbsp;"Orchid"&nbsp;)** |**RGBA(&nbsp;218,&nbsp;112,&nbsp;214,&nbsp;1&nbsp;)** |![orchid](./media/function-colors/color-orchid.png) |
| **Color.PaleGoldenRod** |**ColorValue(&nbsp;"#eee8aa"&nbsp;)**<br>**ColorValue(&nbsp;"palegoldenrod"&nbsp;)** |**RGBA(&nbsp;238,&nbsp;232,&nbsp;170,&nbsp;1&nbsp;)** |![palegoldenrod](./media/function-colors/color-palegoldenrod.png) |
| **Color.PaleGreen** |**ColorValue(&nbsp;"#98fb98"&nbsp;)**<br>**ColorValue(&nbsp;"PaleGreen"&nbsp;)** |**RGBA(&nbsp;152,&nbsp;251,&nbsp;152,&nbsp;1&nbsp;)** |![palegreen](./media/function-colors/color-palegreen.png) |
| **Color.PaleTurquoise** |**ColorValue(&nbsp;"#afeeee"&nbsp;)**<br>**ColorValue(&nbsp;"PALETURQUOISE"&nbsp;)** |**RGBA(&nbsp;175,&nbsp;238,&nbsp;238,&nbsp;1&nbsp;)** |![paleturquoise](./media/function-colors/color-paleturquoise.png) |
| **Color.PaleVioletRed** |**ColorValue(&nbsp;"#db7093"&nbsp;)**<br>**ColorValue(&nbsp;"PaleVioletRed"&nbsp;)** |**RGBA(&nbsp;219,&nbsp;112,&nbsp;147,&nbsp;1&nbsp;)** |![palevioletred](./media/function-colors/color-palevioletred.png) |
| **Color.PapayaWhip** |**ColorValue(&nbsp;"#ffefd5"&nbsp;)**<br>**ColorValue(&nbsp;"papayawhip"&nbsp;)** |**RGBA(&nbsp;255,&nbsp;239,&nbsp;213,&nbsp;1&nbsp;)** |![papayawhip](./media/function-colors/color-papayawhip.png) |
| **Color.PeachPuff** |**ColorValue(&nbsp;"#ffdab9"&nbsp;)**<br>**ColorValue(&nbsp;"PeachPuff"&nbsp;)** |**RGBA(&nbsp;255,&nbsp;218,&nbsp;185,&nbsp;1&nbsp;)** |![peachpuff](./media/function-colors/color-peachpuff.png) |
| **Color.Peru** |**ColorValue(&nbsp;"#cd853f"&nbsp;)**<br>**ColorValue(&nbsp;"PERU"&nbsp;)** |**RGBA(&nbsp;205,&nbsp;133,&nbsp;63,&nbsp;1&nbsp;)** |![peru](./media/function-colors/color-peru.png) |
| **Color.Pink** |**ColorValue(&nbsp;"#ffc0cb"&nbsp;)**<br>**ColorValue(&nbsp;"Pink"&nbsp;)** |**RGBA(&nbsp;255,&nbsp;192,&nbsp;203,&nbsp;1&nbsp;)** |![pink](./media/function-colors/color-pink.png) |
| **Color.Plum** |**ColorValue(&nbsp;"#dda0dd"&nbsp;)**<br>**ColorValue(&nbsp;"plum"&nbsp;)** |**RGBA(&nbsp;221,&nbsp;160,&nbsp;221,&nbsp;1&nbsp;)** |![plum](./media/function-colors/color-plum.png) |
| **Color.PowderBlue** |**ColorValue(&nbsp;"#b0e0e6"&nbsp;)**<br>**ColorValue(&nbsp;"PowderBlue"&nbsp;)** |**RGBA(&nbsp;176,&nbsp;224,&nbsp;230,&nbsp;1&nbsp;)** |![powderblue](./media/function-colors/color-powderblue.png) |
| **Color.Purple** |**ColorValue(&nbsp;"#800080"&nbsp;)**<br>**ColorValue(&nbsp;"PURPLE"&nbsp;)** |**RGBA(&nbsp;128,&nbsp;0,&nbsp;128,&nbsp;1&nbsp;)** |![purple](./media/function-colors/color-purple.png) |
| **Color.Red** |**ColorValue(&nbsp;"#ff0000"&nbsp;)**<br>**ColorValue(&nbsp;"Red"&nbsp;)** |**RGBA(&nbsp;255,&nbsp;0,&nbsp;0,&nbsp;1&nbsp;)** |![red](./media/function-colors/color-red.png) |
| **Color.RosyBrown** |**ColorValue(&nbsp;"#bc8f8f"&nbsp;)**<br>**ColorValue(&nbsp;"rosybrown"&nbsp;)** |**RGBA(&nbsp;188,&nbsp;143,&nbsp;143,&nbsp;1&nbsp;)** |![rosybrown](./media/function-colors/color-rosybrown.png) |
| **Color.RoyalBlue** |**ColorValue(&nbsp;"#4169e1"&nbsp;)**<br>**ColorValue(&nbsp;"RoyalBlue"&nbsp;)** |**RGBA(&nbsp;65,&nbsp;105,&nbsp;225,&nbsp;1&nbsp;)** |![royalblue](./media/function-colors/color-royalblue.png) |
| **Color.SaddleBrown** |**ColorValue(&nbsp;"#8b4513"&nbsp;)**<br>**ColorValue(&nbsp;"SADDLEBROWN"&nbsp;)** |**RGBA(&nbsp;139,&nbsp;69,&nbsp;19,&nbsp;1&nbsp;)** |![saddlebrown](./media/function-colors/color-saddlebrown.png) |
| **Color.Salmon** |**ColorValue(&nbsp;"#fa8072"&nbsp;)**<br>**ColorValue(&nbsp;"Salmon"&nbsp;)** |**RGBA(&nbsp;250,&nbsp;128,&nbsp;114,&nbsp;1&nbsp;)** |![salmon](./media/function-colors/color-salmon.png) |
| **Color.SandyBrown** |**ColorValue(&nbsp;"#f4a460"&nbsp;)**<br>**ColorValue(&nbsp;"sandybrown"&nbsp;)** |**RGBA(&nbsp;244,&nbsp;164,&nbsp;96,&nbsp;1&nbsp;)** |![sandybrown](./media/function-colors/color-sandybrown.png) |
| **Color.SeaGreen** |**ColorValue(&nbsp;"#2e8b57"&nbsp;)**<br>**ColorValue(&nbsp;"SeaGreen"&nbsp;)** |**RGBA(&nbsp;46,&nbsp;139,&nbsp;87,&nbsp;1&nbsp;)** |![seagreen](./media/function-colors/color-seagreen.png) |
| **Color.SeaShell** |**ColorValue(&nbsp;"#fff5ee"&nbsp;)**<br>**ColorValue(&nbsp;"SEASHELL"&nbsp;)** |**RGBA(&nbsp;255,&nbsp;245,&nbsp;238,&nbsp;1&nbsp;)** |![seashell](./media/function-colors/color-seashell.png) |
| **Color.Sienna** |**ColorValue(&nbsp;"#a0522d"&nbsp;)**<br>**ColorValue(&nbsp;"Sienna"&nbsp;)** |**RGBA(&nbsp;160,&nbsp;82,&nbsp;45,&nbsp;1&nbsp;)** |![sienna](./media/function-colors/color-sienna.png) |
| **Color.Silver** |**ColorValue(&nbsp;"#c0c0c0"&nbsp;)**<br>**ColorValue(&nbsp;"silver"&nbsp;)** |**RGBA(&nbsp;192,&nbsp;192,&nbsp;192,&nbsp;1&nbsp;)** |![silver](./media/function-colors/color-silver.png) |
| **Color.SkyBlue** |**ColorValue(&nbsp;"#87ceeb"&nbsp;)**<br>**ColorValue(&nbsp;"SkyBlue"&nbsp;)** |**RGBA(&nbsp;135,&nbsp;206,&nbsp;235,&nbsp;1&nbsp;)** |![skyblue](./media/function-colors/color-skyblue.png) |
| **Color.SlateBlue** |**ColorValue(&nbsp;"#6a5acd"&nbsp;)**<br>**ColorValue(&nbsp;"SLATEBLUE"&nbsp;)** |**RGBA(&nbsp;106,&nbsp;90,&nbsp;205,&nbsp;1&nbsp;)** |![slateblue](./media/function-colors/color-slateblue.png) |
| **Color.SlateGray** |**ColorValue(&nbsp;"#708090"&nbsp;)**<br>**ColorValue(&nbsp;"SlateGray"&nbsp;)** |**RGBA(&nbsp;112,&nbsp;128,&nbsp;144,&nbsp;1&nbsp;)** |![slategray](./media/function-colors/color-slategray.png) |
| **Color.SlateGrey** |**ColorValue(&nbsp;"#708090"&nbsp;)**<br>**ColorValue(&nbsp;"slategrey"&nbsp;)** |**RGBA(&nbsp;112,&nbsp;128,&nbsp;144,&nbsp;1&nbsp;)** |![slategrey](./media/function-colors/color-slategrey.png) |
| **Color.Snow** |**ColorValue(&nbsp;"#fffafa"&nbsp;)**<br>**ColorValue(&nbsp;"Snow"&nbsp;)** |**RGBA(&nbsp;255,&nbsp;250,&nbsp;250,&nbsp;1&nbsp;)** |![snow](./media/function-colors/color-snow.png) |
| **Color.SpringGreen** |**ColorValue(&nbsp;"#00ff7f"&nbsp;)**<br>**ColorValue(&nbsp;"SPRINGGREEN"&nbsp;)** |**RGBA(&nbsp;0,&nbsp;255,&nbsp;127,&nbsp;1&nbsp;)** |![springgreen](./media/function-colors/color-springgreen.png) |
| **Color.SteelBlue** |**ColorValue(&nbsp;"#4682b4"&nbsp;)**<br>**ColorValue(&nbsp;"SteelBlue"&nbsp;)** |**RGBA(&nbsp;70,&nbsp;130,&nbsp;180,&nbsp;1&nbsp;)** |![steelblue](./media/function-colors/color-steelblue.png) |
| **Color.Tan** |**ColorValue(&nbsp;"#d2b48c"&nbsp;)**<br>**ColorValue(&nbsp;"tan"&nbsp;)** |**RGBA(&nbsp;210,&nbsp;180,&nbsp;140,&nbsp;1&nbsp;)** |![tan](./media/function-colors/color-tan.png) |
| **Color.Teal** |**ColorValue(&nbsp;"#008080"&nbsp;)**<br>**ColorValue(&nbsp;"Teal"&nbsp;)** |**RGBA(&nbsp;0,&nbsp;128,&nbsp;128,&nbsp;1&nbsp;)** |![teal](./media/function-colors/color-teal.png) |
| **Color.Thistle** |**ColorValue(&nbsp;"#d8bfd8"&nbsp;)**<br>**ColorValue(&nbsp;"THISTLE"&nbsp;)** |**RGBA(&nbsp;216,&nbsp;191,&nbsp;216,&nbsp;1&nbsp;)** |![thistle](./media/function-colors/color-thistle.png) |
| **Color.Tomato** |**ColorValue(&nbsp;"#ff6347"&nbsp;)**<br>**ColorValue(&nbsp;"Tomato"&nbsp;)** |**RGBA(&nbsp;255,&nbsp;99,&nbsp;71,&nbsp;1&nbsp;)** |![tomato](./media/function-colors/color-tomato.png) |
| **Color.Turquoise** |**ColorValue(&nbsp;"#40e0d0"&nbsp;)**<br>**ColorValue(&nbsp;"turquoise"&nbsp;)** |**RGBA(&nbsp;64,&nbsp;224,&nbsp;208,&nbsp;1&nbsp;)** |![turquoise](./media/function-colors/color-turquoise.png) |
| **Color.Violet** |**ColorValue(&nbsp;"#ee82ee"&nbsp;)**<br>**ColorValue(&nbsp;"Violet"&nbsp;)** |**RGBA(&nbsp;238,&nbsp;130,&nbsp;238,&nbsp;1&nbsp;)** |![violet](./media/function-colors/color-violet.png) |
| **Color.Wheat** |**ColorValue(&nbsp;"#f5deb3"&nbsp;)**<br>**ColorValue(&nbsp;"WHEAT"&nbsp;)** |**RGBA(&nbsp;245,&nbsp;222,&nbsp;179,&nbsp;1&nbsp;)** |![wheat](./media/function-colors/color-wheat.png) |
| **Color.White** |**ColorValue(&nbsp;"#ffffff"&nbsp;)**<br>**ColorValue(&nbsp;"White"&nbsp;)** |**RGBA(&nbsp;255,&nbsp;255,&nbsp;255,&nbsp;1&nbsp;)** |![white](./media/function-colors/color-white.png) |
| **Color.WhiteSmoke** |**ColorValue(&nbsp;"#f5f5f5"&nbsp;)**<br>**ColorValue(&nbsp;"whitesmoke"&nbsp;)** |**RGBA(&nbsp;245,&nbsp;245,&nbsp;245,&nbsp;1&nbsp;)** |![whitesmoke](./media/function-colors/color-whitesmoke.png) |
| **Color.Yellow** |**ColorValue(&nbsp;"#ffff00"&nbsp;)**<br>**ColorValue(&nbsp;"Yellow"&nbsp;)** |**RGBA(&nbsp;255,&nbsp;255,&nbsp;0,&nbsp;1&nbsp;)** |![yellow](./media/function-colors/color-yellow.png) |
| **Color.YellowGreen** |**ColorValue(&nbsp;"#9acd32"&nbsp;)**<br>**ColorValue(&nbsp;"YELLOWGREEN"&nbsp;)** |**RGBA(&nbsp;154,&nbsp;205,&nbsp;50,&nbsp;1&nbsp;)** |![yellowgreen](./media/function-colors/color-yellowgreen.png) |
