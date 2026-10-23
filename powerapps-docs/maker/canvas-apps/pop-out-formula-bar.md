---
title: Use the pop-out formula bar in canvas apps
description: Open the Power Fx formula bar in a separate window while keeping your canvas app visible.
author: azure-lm
ms.topic: how-to
ms.custom: canvas
ms.reviewer: joshuapa
ms.date: 10/08/2026
ms.subservice: canvas-maker
ms.author: lmcdaniel
search.audienceType:
  - maker
ai-usage: ai-assisted
contributors: joshuapartlow
---

# Use the pop-out formula bar in canvas apps

The pop-out formula bar opens the Power Fx editor in a separate browser window. Use it to work with longer formulas or move the editor to another monitor while keeping your app visible in Power Apps Studio.

## Prerequisites

- Create a canvas app or open an existing canvas app for editing.
- Allow pop-up windows for Power Apps Studio in your browser.

## Open the Formula editor in a separate window

1. In Power Apps Studio, select the control or screen that you want to configure.
1. In the property list, select the property that you want to edit.
1. On the right side of the formula bar, select the **Open formula bar in new window** icon button.

   :::image type="content" source="media/pop-out-formula-bar/pop-out-button.png" alt-text="Screenshot that shows the Open formula bar in new window icon button on the right side of the formula bar." lightbox="media/pop-out-formula-bar/pop-out-button.png":::

The **Formula editor** window opens with the selected control and property, and displays the formula.

:::image type="content" source="media/pop-out-formula-bar/formula-editor-window.png" alt-text="Screenshot that shows the Formula editor window with a formula." lightbox="media/pop-out-formula-bar/formula-editor-window.png":::

> [!TIP]
> Move or resize the Formula editor window like any other browser window. On a multimonitor setup, place Power Apps Studio on one monitor and the Formula editor on another.

## Work between Studio and the Formula editor

Power Apps Studio and the Formula editor stay synchronized:

- Select a different control in the canvas or **Tree view** to show that control in the Formula editor.
- Select a property in the Formula editor to edit it.
- Edit the formula in the Formula editor. Formula changes are shared with Studio.

The Formula editor doesn't include a separate control tree. Continue to select controls and screens in Power Apps Studio.

If you pin the Formula editor, it stays focused on the current control and property while you select other controls in Power Apps Studio. Unpin the Formula editor to resume following the current Studio selection. You can still select a different property inside the pinned Formula editor.

Keep the Power Apps Studio window open while you use the Formula editor. The **Synced** status indicates that formula changes are being shared with Studio.

> [!NOTE]
> The Formula editor doesn't include separate save or publish controls. Use the normal save, autosave, and publish controls in Power Apps Studio.

## Use formula editing tools

The Formula editor provides editing tools for the current formula:

- IntelliSense suggestions and function help.
- Syntax and error highlighting.
- Line numbers.
- Format text.
- Remove formatting.
- Find and replace.

Find and replace applies to the formula currently open in the editor. It doesn't search formulas across the entire app. For more information, see [Use Find and Replace in the formula bar](formula-bar-find-replace.md).

## Work in a coauthored app

The Formula editor follows the editing permissions and locks in Power Apps Studio. If the selected formula is read-only, you can view and search the formula, but you can't change or format it.

To edit another formula, select an available control or property in Power Apps Studio.

## Troubleshoot the Formula editor

### The Formula editor doesn't open

Your browser might be blocking the pop-up window. Allow pop-ups for Power Apps Studio, and then select the **Open formula bar in new window** icon button again.

### The Formula editor shows a connection error

Keep the Power Apps Studio window open. If the Formula editor can't reconnect, close it and open it again from the formula bar.

## Related information

- [Get started with formulas in canvas apps](working-with-formulas.md)
- [Understand Power Apps Studio](power-apps-studio.md)
- [Use Find and Replace in the formula bar](formula-bar-find-replace.md)
- [Understand coauthoring and copresence](copresence-power-apps-studio.md)
