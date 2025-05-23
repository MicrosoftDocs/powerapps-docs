---
title: Use code view for canvas app controls (preview)
description: Learn how to use the code view in Microsoft Power Apps Studio to understand your canvas app's functionality.
author: marcelbf
ms.author: marcelbf
ms.date: 5/20/2025
ms.topic: how-to
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

# Use code view for canvas app controls 

Use the code view feature to look at the underlying code for each control on your app's screens. The code uses an improved format that's a subset of YAML.

With code view you can:

- View the code for each control on your screen.
- Copy the code for a control and share it outside of Power Apps Studio.
- Paste the code for a control and create a new control based on it.

## View, copy, and paste code

Code view shows the code for the selected control and all its child controls.

Code view lets you copy and paste code to any screen in your app or outside of Power Apps to duplicate the control. This feature is helpful when controls are highly customized and you want to share or duplicate them.

### View code

1. Open your app for [editing](edit-app.md) in Power Apps Studio.

1. Right-click the control in the tree view or on the screen, and then select **View code**.

    :::image type="content" source="media/code-view/view-code.png" alt-text="Screenshot of the tree view in Power Apps Studio, with the View code option on a control's context menu highlighted.":::

> [!TIP]
> Use the keyboard shortcut `Ctrl+F` to find a specific string in the code.

### Copy and paste code

1. To copy the code of a selected control:
   - Use the menu to copy.
   - Use the shortcut <kbd>Ctrl</kbd>+<kbd>C</kbd>.
   - When viewing your code in the code view popup, select **Copy code**.
1. To add a new control from the code:

   - Use the menu to paste.
   - Use the shortcut <kbd>Ctrl</kbd>+<kbd>V</kbd>.

     :::image type="content" source="media/code-view/paste-code.png" alt-text="Screenshot of the tree view in Power Apps Studio, with the Paste code option highlighted on a control's context menu.":::

  > [!IMPORTANT]
  > Use the YAML format that Power Apps Studio generates. The code is validated before the new control is created.

## Browser clipboard access required

To paste code into Power Apps Studio using code view, your browser must have access to the clipboard. If you encounter issues pasting code, check your browser settings and ensure clipboard permissions are enabled for the site.

The first time you paste code, your browser will prompt you to grant clipboard access. Approve this request to enable pasting functionality in Power Apps Studio.

:::image type="content" source="media/code-view/edge-clipboard-warning.png" alt-text="Screenshot of edge asking for permission to access the clipboard content.":::

> [!TIP]
> If pasting doesn't work, check if clipboard access to Power Apps is blocked in your browser. In Microsoft Edge, you can manually add **https://make.powerapps.com** to the allowed sites for clipboard access in your browser settings.

## Known limitations

- You can't copy and paste or view the code for the **App Object**.
- You can't edit the code in the code view.

## Related information

- [Get started with formulas in canvas apps](working-with-formulas.md)
- [Use Find and Replace in the formula bar](formula-bar-find-replace.md)
- [Formula reference - canvas apps](formula-reference.md)
- [Power Fx YAML formula grammar](/power-platform/power-fx/yaml-formula-grammar)
- [Understand app functionality through code view (video)](https://youtu.be/qwXfvs9wzFY?feature=shared)
