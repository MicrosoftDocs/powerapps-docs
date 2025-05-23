---
title: Use Find and Replace in the formula bar
description: Learn how to use the find and Replace to search for strings and make changes to one or more matches.
author: TashasEv

ms.topic: how-to
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 12/11/2023
ms.subservice: canvas-maker
ms.author: tashas
search.audienceType: 
  - maker
contributors:
  - mduelae
  - TashasEv
---

# Use Find and Replace in the formula bar

In complex Power Apps, formulas can get lengthy. Locating and replacing portions of large formulas can become difficult. You can now use the **Find and Replace** capability for the selected control or property to easily find and replace the specified word or sequence of characters.

With **Find and Replace** capability, you can search for combinations of letters, numbers, words, and phrases within a formula in the formula bar. This capability also allows you to use text casing, whole words, and regular expressions to find and replace text inside formulas.

## Prerequisites

- [Sign up](../signup-for-powerapps.md) for Power Apps.
- [Create an app](get-started-test-drive.md) or [open an existing app](edit-app.md) in Power Apps.
- Learn how to [configure a control](add-configure-controls.md).

## Launch Find and Replace

You can launch the **Find and Replace** control in the formula bar using the **Find and replace** button, or shortcut keys. You can also pre-populate text in the search input.

To get started, [create a new app](get-started-test-drive.md), or [edit an existing app](edit-app.md) in Power Apps Studio. Once open, use any of the following methods to launch the **Find and Replace** control.

### Method 1: Use the Find and Replace button

1. Select the control or property that you want to edit.

1. Select the drop-down on the right-side of the formula bar to show the **Find and Replace** control.

    :::image type="content" source="media/formula-bar-find-replace/expand-button.png" alt-text="The expand button on the right hand side of the formula bar":::

    > [!TIP]
    > You can also drag the formula bar down to expand the formula bar making it easier to read complex expressions.

1. Select **Find and replace** from the bottom of the formula bar.

    :::image type="content" source="media/formula-bar-find-replace/find-replace-button.png" alt-text="The Find and Replace button underneath the formula bar":::

    **Find and Replace** control appears on the upper-right hand side of the formula bar.

    :::image type="content" source="media/formula-bar-find-replace/find-replace-formula-bar.png" alt-text="The Find and Replace control appears inside the formula bar":::

### Method 2: Use shortcut keys

1. Select the control or property that you want to edit.

1. While your cursor is within the formula bar, press **Ctrl+F** to find, or **Ctrl+H** to find and replace the specified word or sequence of characters in the formula.

    :::image type="content" source="media/formula-bar-find-replace/shortcut-keys.gif" alt-text="An animation showing the Find and Replace control launching by pressing Ctrl + F to launch Find and pressing Ctrl + H to launch Find and Replace":::

### Method 3: Launch Find and Replace with text already selected

You can also launch the control pre-populated with text from your formula that you wish to search for.

To do this, select or keep the cursor inside the formula bar over the section that you want to find or replace. And then, use **Find and replace** button, or the shortcut keys as described earlier to launch **Find and Replace** control.

:::image type="content" source="media/formula-bar-find-replace/select-find-replace.png" alt-text="Cursor placed on the portion of the formula to find and replace, and another screen with the Find and Replace control open.":::

## Working with Find and Replace

When working with **Find**, you have three options to search the formula. When working with **Replace**, you have two options to choose from. We'll take a look at the options for both **Find** and **Replace**.

### Find

Add text or characters to search for into the provided input area. And then, use the icons on the right-hand side of the input area to help refine your search:

- **Match case** returns only matches with the specified case.

    In the example below, instances of `TicketList` will appear as a match, but `ticketlist` wouldn't.
    
    :::image type="content" source="media/formula-bar-find-replace/match-case.png" alt-text="The Match Case refiner icon on the Find and Replace control":::

- **Match whole word** returns only exact matches of the entire sequence of characters.

    In the example below, instances of `Ticket` returns no matches although the word `Ticket` appears within the names several times in the formula.

    :::image type="content" source="media/formula-bar-find-replace/match-whole-word.png" alt-text="The Match Whole Word refiner icon on the Find and Replace control":::

- **Use regular expression** (RegEx) returns only matches conforming to the regular expression specified within the input area. More information: [Regular expressions](functions/function-ismatch.md#regular-expressions)

    In the example below, using the Regular Expression search capability with `Screen(Priority|Task)` returns matches for `Screen` when it appears together with either `Priority` or `Task` as shown below.

    :::image type="content" source="media/formula-bar-find-replace/regex-highlighting.png" alt-text="The formula in the formula bar with matching results highlighted for the regular expression shown in the Find and Replace control":::

- **Previous match** or **Next match** arrows allow you to move forward and backward through any matches the search returns. As you move through the matches, the match position updates and the row containing the match is highlighted to let you know which match you're currently working with.

    :::image type="content" source="media/formula-bar-find-replace/match-highlighting.png" alt-text="The formula in the formula bar with a line highlighted for the match currently in focus from using the previous match and next match arrow arrows":::

- **Find in selection** limits the search area within a formula to only the selected portion of a formula. To select part of the formula, select and hold at the beginning of the desired searching area and then drag your cursor to highlight the entire desired area. To select using the keyboard, move cursor focus to the beginning of the desired search area, then hold **Shift** key, and use the arrow keys to highlight the desired search area.  

    In the example below, the search has been limited to the selected area, so the search now only returns two matches instead of the four matches returned previously.

    :::image type="content" source="media/formula-bar-find-replace/selection-highlighting.png" alt-text="The formula in the formula bar showing a selected block of text":::

### Replace

By default, the **Find and replace** control opens in collapsed format and only displays the Find capability. To expand the control and show the Replace capability, select the icon to the left of the search input box, or press **Ctrl+H** on your keyboard. To collapse again, select the rotated icon.

Collapsed replace mode:

:::image type="content" source="media/formula-bar-find-replace/toggle-replace-mode.png" alt-text="The Toggle Replace Mode icon on the left hand side of the Find and Replace control, before the text input areas":::

Expanded replace mode:

:::image type="content" source="media/formula-bar-find-replace/collapse-replace-mode.png" alt-text="The Collapse Replace Mode icon on the left hand side of the Find and Replace control, before the text input areas":::

In the Replace input area, specify the word or sequence of characters you’d like to replace the search text.

Use the **Replace** or **Replace all** icons to update one or all matches returned with the specified word or characters.

:::row:::
   :::column span="":::

        **Replace**

      :::image type="content" source="media/formula-bar-find-replace/replace-one.png" alt-text="The Replace icon on the right-hand side of the Find and Replace control, after the Replace text input field.":::
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::

        **Replace all**

      :::image type="content" source="media/formula-bar-find-replace/replace-all.png" alt-text="The Replace All icon on the right-hand side of the Find and Replace control, after the Replace text input field.":::
   :::column-end:::
:::row-end:::

### See also

- [Use the Search pane (preview)](search.md)
- [Get started with formulas in canvas apps](working-with-formulas.md)
- [Add and configure controls](add-configure-controls.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
 
