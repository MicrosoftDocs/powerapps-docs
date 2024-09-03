---
title: Use code view for canvas app controls (preview)
description: Learn how to use the code view in Power Apps Studio to understand your canvas app's functionality.
author: marcelbf
ms.author: marcelbf
ms.date: 8/8/2024
ms.topic: conceptual
ms.reviewer: mkaur
ms.subservice: canvas-maker
ms.collection: get-started
search.audienceType: 
  - maker
  - developer
ai-usage: ai-assisted
ms.custom:
  - canvas
  - ai-gen-diyeditor
---

# Use code view for canvas app controls (preview)

[!INCLUDE [preview-banner](../../shared-content/shared/preview-includes/preview-banner.md)]

Use the code view feature to look at the underlying code for each control on your app's screens. The code uses an improved format that's a subset of YAML. Learn more in [Power Fx YAML formula grammar](/power-platform/power-fx/yaml-formula-grammar).

With code view you can:

- Look at the code for each control on your screen.
- Copy the code for a control and share it outside of Power Apps Studio.
- Paste the code for a control and create a new control based on it.

> [!IMPORTANT]
>
> - This is a preview feature and the format is subject to change. We don't guarantee compatibility with the final version.
> - The current code format isn't suitable for source control during the preview period.

## Prerequisites

Turn on the Power Fx formula bar to view the code for a control.

The formula bar is **ON** by default for new apps. To turn on the Power Fx formula bar for existing apps:

1. Open your app in Power Apps Studio.
1. Select **Settings** > **Upcoming features** > **Preview**, and then turn on the **Power Fx formula bar** toggle.

## View, copy, and paste code

Code view shows the code for the selected control and all its child controls. Use the keyboard shortcut Ctrl+F to find a specific string in the code.

### View code

1. Open your app for [editing](edit-app.md) in Power Apps Studio.

1. Right-click the control in the tree view or on the screen, and then select **View code (preview)**.

    :::image type="content" source="media/code-view/view-code.png" alt-text="Screenshot of the tree view in Power Apps Studio, with the View code option on a control's context menu highlighted.":::

### Copy code

1. In the code view, select **Copy code**, and then share it or paste it to create a duplicate of the selected control.

    - To share it, paste the copied code in any window.
    - To add a new control from the copied code, right-click the screen where you want to add the new control, and then select, **Paste code (preview)**.

    :::image type="content" source="media/code-view/paste-code.png" alt-text="Screenshot of the tree view in Power Apps Studio, with the Paste code option highlighted on a control's context menu.":::

    You must use the YAML format that Power Apps Studio generates. The code is validated before the new control is created.

## Known limitations

- You can't copy and paste or view the code for the **App Object**.
- You can't edit the code in the code view.
- You can only copy controls that are on a screen. You can't copy a screen.
- When you paste code, the new control is positioned at coordinates X=40, Y=40. In the future, the X and Y properties that you set will be respected.

## Related information

- [Get started with formulas in canvas apps](working-with-formulas.md)
- [Use Find and Replace in the formula bar](formula-bar-find-replace.md)
- [Formula reference - canvas apps](formula-reference.md)
- [Power Fx YAML formula grammar](/power-platform/power-fx/yaml-formula-grammar)
