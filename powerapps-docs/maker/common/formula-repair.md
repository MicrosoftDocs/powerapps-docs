---
title: "Formula repair in Power Apps (preview) | MicrosoftDocs"
description: Understand how to enable and use formula repair in Power Apps
ms.custom: ""
ms.date: 11/03/2022
ms.reviewer: tapanm-msft
ms.topic: overview
author: norliu
ms.subservice: common
ms.author: norliu
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - norliu
---

# Formula repair in Power Apps (preview)

[This article is pre-release documentation and is subject to change.]

When writing [Power Fx](/power-platform/power-fx/overview) formulas, errors are often unavoidable. And it's time-consuming to troubleshoot and fix. Power Apps Formula repair will automatically generate and fix suggestions for you when there's a formula error.

## Enable formula repair

Formula repair feature is available for [canvas apps](/power-apps/maker/canvas-apps/getting-started) and [custom pages](/power-apps/maker/model-driven-apps/model-app-page-overview).

Once you have Power Apps Studio open, go to the top menu bar, and select **Settings** > **Upcoming features** > **Preview**. You'll see the toggle for **Formula repair** feature. Select the toggle to turn the feature on to experience the advantage of automatic formula checks, and suggestions. 

:::image type="content" source="media/formula-repair/setting.png" alt-text="Formula repair - feature.":::

> [!IMPORTANT]
> - This is a preview feature.
> - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)]
> - This preview feature is in process of rolling out and might not be available in your region yet.

## Use formula repair

Once you have the focus inside the formula bar, if the formula has any errors that the formula repair feature finds suggestions for, you'll see a red dot next to the **fx** icon.

When you select this red dot, you'll be able to see suggested fix for your formula. After confirming the suggested change, select **Apply** to apply the change to your formula and fix the formula error.

For example, the following usage shows a typo when entering the name of the label from `Label1` to `Lable1`. The formula repair feature recognizes this mistake, and suggests the change. Upon confirming and applying the change, the error is fixed.

:::image type="content" source="media/formula-repair/example-repair-process.png" alt-text="Example of Label.Text.":::

## Scope of error discovery and suggestions

Several types of errors are discovered and suggested as a fix.

1. Missing parenthesis and missing quotes.

1. Typos, similar to the example for the label control shown earlier in this article.

1. Misuse of delimiters and missing operators.

    Example of a formula using a comma (",") instead of a semicolon (";"):

    :::image type="content" source="media/formula-repair/submitform.png" alt-text="Example of SubmitForm.":::

    Example of a formula with a missed reference to a comma (","):

    :::image type="content" source="media/formula-repair/complex-formula.png" alt-text="Example of complex formula.":::

## Limitations

- Formula repair won't be able to determine the expected values when you enter a complete incorrect control name. For example, if your control name is `MyLabel` and you try to enter `WrongLabel`. In this situation, formula repair feature won't be able to determine and suggest you to use the formula to reference `MyLabel` instead of `WrongLabel`.

- Formula repair won't trigger if your formula has only warnings, or isn't showing any errors (even when the formula is incorrect).

