---
title: Metrics Card modern control in canvas apps - Power Apps
description: Learn about the properties and examples of the Metrics Card modern control in Power Apps.
author: yogeshgupta698
ms.topic: reference
ms.custom: canvas
ms.date: 11/02/2026
ai-usage: ai-generated
ms.subservice: canvas-maker
ms.author: yogupt
ms.reviewer: joshuapa
search.audienceType:
  - maker
---

# Metrics Card modern control in canvas apps

Display a key metric with a title, description, and optional comparison.

## Description

Use **Metrics Card** to show a formatted value, such as revenue, open requests, or a service-level percentage. Add **TrendValue** and **TrendText** to explain a change relative to another period.

The card displays the values you provide. It doesn't calculate an aggregate, compare periods, or infer whether a change is favorable. Use Power Fx formulas to calculate your metric and set its presentation.

## General

The following properties define the card's content.

| Property | Description |
| --- | --- |
| **Title** | Heading that identifies the metric. A blank value hides the heading. |
| **DisplayText** | Text displayed as the main metric. Format numbers or dates with Power Fx before displaying them, for example `"$128,450"`. A blank or empty value displays an em dash instead of zero. |
| **Description** | Supporting text below the metric, such as a period and region. A blank value hides this section. |
| **TrendValue** | Numeric change shown in the trend badge. Positive numbers include a plus sign, negative numbers include a minus sign, and zero remains visible without a sign. The initial sample value is `18.6`. Set it to `Blank()` to hide the numeric badge. |
| **TrendText** | Text beside the badge, such as `"% higher than last month"`. This text can appear even when **TrendValue** is blank. |
| **TrendType** | Meaning of the trend: `MetricCardTrendType.Positive`, `MetricCardTrendType.Negative`, or `MetricCardTrendType.Neutral`. Default is `MetricCardTrendType.Positive`. This property controls the badge's semantic styling independently of the numeric sign. |

For example, a reduction in unresolved requests can be favorable: use a negative **TrendValue** with `MetricCardTrendType.Positive`. Supply the percentage sign or other units in **TrendText**; the numeric badge doesn't add units.

New cards include localized sample text. Replace the sample content with formulas and descriptions for your app.

## Behavior

Use these properties to control visibility and interaction.

**OnSelect** – Action that runs when a user activates the card. The card becomes an activation target when this property has a formula and **DisplayMode** is `DisplayMode.Edit`. It doesn't run the action in view or disabled mode.

**DisplayMode** – Whether the card is interactive (`DisplayMode.Edit`), read-only (`DisplayMode.View`), or disabled (`DisplayMode.Disabled`).

**Visible** – Whether the control appears. Default is `true`.

## Size and position

Configure the card's dimensions and placement with these properties.

**X**, **Y** – Position of the control relative to its parent.

**Width** – Width of the control. Default is `250`.

**Height** – Height of the control. The authored default is `200`. When **AutoHeight** is `true`, the control measures its content and updates its height, subject to its parent layout.

**AutoHeight** – Whether height adjusts to the content. Default is `false`, so new cards use the authored **Height**. Set it to `true` to grow with the content.

**Overflow** - How a fixed-height card handles content that doesn't fit. `Overflow.Hidden` (default) clips the content. `Overflow.Scroll` allows vertical scrolling. This property doesn't limit content when **AutoHeight** is `true`.

For a fixed-height card with long content, set **AutoHeight** to `false`, choose a **Height**, and set **Overflow** to `Overflow.Scroll`. Check that users can reach the content with both a pointer and a keyboard. Scrolling doesn't increase the card's height.

## Style and theme

Use these properties to style the card's surface.

| Property | Description |
| --- | --- |
| **HighlightPosition** | Position of the accent strip: `MetricCardHighlightPosition.Top`, `.Right`, `.Bottom`, `.Left`, or `.None`. Default is `MetricCardHighlightPosition.Top`. |
| **HighlightColor** | Accent-strip color. When unset, uses the theme's brand background color. |
| **Fill** | Background color. When unset, uses the theme's neutral background. |
| **BorderColor** | Border color. When unset, uses the theme's neutral border color. |
| **BorderStyle** | Border style: `BorderStyle.Solid`, `.Dashed`, `.Dotted`, or `.None`. Set this explicitly when you customize the border. |
| **BorderThickness** | Width of the border. Set a positive value and a style other than `BorderStyle.None` to show a border. |
| **RadiusTopLeft**, **RadiusTopRight**, **RadiusBottomLeft**, **RadiusBottomRight** | Corner radii. Each defaults to `16`. |
| **DropShadow** | Shadow style: `DropShadow.None`, `.Light`, `.Semilight`, `.Regular`, `.Semibold`, `.Bold`, or `.ExtraBold`. Default is `DropShadow.Light`. |

### Text styling

Configure the title, main value, and description separately. Unset font, size, and weight properties use the control's default styling for that field. Size values are in points.

| Text field | Font family | Size | Font weight | Italic |
| --- | --- | --- | --- | --- |
| Title. | **TitleFont** | **TitleSize** | **TitleFontWeight** | **TitleItalic** |
| Main metric. | **DisplayTextFont** | **DisplayTextSize** | **DisplayTextFontWeight** | **DisplayTextItalic** |
| Description. | **DescriptionFont** | **DescriptionSize** | **DescriptionFontWeight** | **DescriptionItalic** |

The italic properties default to `false`. The control doesn't expose separate font overrides for **TrendValue** or **TrendText**, or per-field text-color properties.

## Accessibility

Use these properties to provide context for assistive technologies.

**AccessibleLabel** – A complete accessible description of the card. If you leave it blank, the control combines the title, metric, description, signed trend, trend meaning, and comparison text into a reading.

**ContentLanguage** – Language of the content. The control also uses this language to format the trend number's digits and decimal separator. It doesn't translate your text.

**Tooltip** – Additional information shown when a user points to the card. Include essential information in visible text or **AccessibleLabel**, not only in a tooltip.

Explain what the metric and comparison mean in words. Don't rely only on the badge color to communicate whether a result is favorable.

## Read values from the control

You can reference **DisplayText**, **Height**, **Width**, **X**, **Y**, **Visible**, and **DisplayMode** from another control. For example, `RevenueMetric.DisplayText` returns the displayed metric text.

There isn't a **Selected** record output or a calculated metric output. Keep the source formula available separately when another control needs the underlying number rather than its formatted display text.

## Example

This example displays a revenue metric without a data connection or external media. It supplies the metric and comparison explicitly and sets **AutoHeight** to `true`, overriding the fixed-height default so the card fits its content.

```yaml
- RevenueMetric:
    Control: ModernMetricCard@1.0.0
    Properties:
      Title: ="Monthly revenue"
      DisplayText: ="$128,450"
      Description: ="September - North America"
      TrendValue: =18.6
      TrendText: ="% higher than last month"
      TrendType: =MetricCardTrendType.Positive
      HighlightPosition: =MetricCardHighlightPosition.Top
      AutoHeight: =true
      AccessibleLabel: ="Monthly revenue is 128,450 dollars for September in North America, 18.6 percent higher than last month."
      Width: =320
      X: =40
      Y: =40
```

To show a metric without a comparison, set both **TrendValue** and **TrendText** to `Blank()`. Setting only **TrendValue** to blank leaves the comparison text visible.

## Limitations

Consider these behaviors when you design your app:

- The main value is text, not a numeric input. The card doesn't aggregate records or automatically format **DisplayText** as a currency or percentage.
- The numeric trend and its semantic meaning are independent. Set **TrendType** explicitly when the sign alone doesn't express a favorable or unfavorable change.
- Fixed-height cards clip content when **Overflow** is `Overflow.Hidden`. Use `Overflow.Scroll` or **AutoHeight** to make longer content available, and test the widths, text sizes, and languages your app supports.

## See also

- [Modern controls overview](overview-modern-controls.md)
- [Card modern control](modern-control-card.md)
- [Size and location properties](../properties-size-location.md)
- [Text function](/power-platform/power-fx/reference/function-text)
