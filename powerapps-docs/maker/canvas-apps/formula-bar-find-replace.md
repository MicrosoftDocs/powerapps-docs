---
title: Find and Replace in the formula bar
description: Learn how to use the formula bar Find and Replace capability to search for words and character sequences and make changes to one or more matches.
author: tashas-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 05/12/2021
ms.subservice: canvas-maker
ms.author: tashas
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - tashas-msft
---
# Using Find and Replace in the formula bar

You can search for combinations of letters, numbers, words, and phrases within a formula in the formula bar using Find and Replace capability. In complex Power Apps, formulas can get lengthy and using Find and Replace can help you locate all instances of the specified word or sequence of characters, replace one or more matches, or replace all matches at once.

## Prerequisites

- [Sign up](../signup-for-powerapps.md) for Power Apps.
- Create an app or open an existing app in Power Apps.
- Learn how to [configure a control](add-configure-controls.md).


## Launch the Find and Replace control

You can launch the Find and Replace control in the formula bar using the Find and Replace button or quick keys. Additionally, you can pre-populate text in the search input.

### Using the Find and Replace button

1. Sign in to [Power Apps](https://make.powerapps.com).

1. Open an existing app, or select a sample app under Create > Start from template. The formula bar appears near the top of the screen.

1. Select the Expand button to expand the formula bar.

:::image type="content" source="media/formula-bar-find-replace/expand-button.png" alt-text="The expand button on the right hand side of the formula bar":::

1. Options appear beneath the formula bar, including the **Find and Replace** button.

:::image type="content" source="media/formula-bar-find-replace/find-replace-button.png" alt-text="The Find and Replace button underneath the formula bar":::

1. Selecting the Find and Replace button launches the Find and Replace control on the right hand side of the formula bar.

:::image type="content" source="media/formula-bar-find-replace/find-replace-formula-bar.png" alt-text="The Find and Replace control appears inside the formula bar":::

### Using Quick Keys

While your cursor is within the formula bar:

- Press **Ctrl+F** as a shortcut to find a specified word or sequence of characters in the current formula.
- Press **Ctrl+H** as a shortcut to find and replace a specified word or sequence of characters in the current formula.

:::image type="content" source="media/formula-bar-find-replace/quick-keys.gif" alt-text="An animation showing the Find and Replace control launching by pressing Ctrl + F to launch Find and pressing Ctrl + H to launch Find and Replace":::

### Launch Find and Replace with text pre-selected

You can also launch the control pre-populated with text from your formula that you wish to search for.

1. Select the desired text within the formula. The text will be highlighted to indicate it is selected.

:::image type="content" source="media/formula-bar-find-replace/select-text.png" alt-text="The selected text inside the formula bar with highlighting":::

1. Select the Find and Replace button beneath the formula bar, or press Ctrl + F or Ctrl + H on your keyboard to launch the control with the desired text already populated in the search input field.

:::image type="content" source="media/formula-bar-find-replace/prepopulated-text.png" alt-text="The search input field on the Find and Replace control is pre-populated with the previously selected text":::

## Working with Find and Replace

There are several ways you can use the Find and Replace Control to work with a formula.

### Find

Add text or characters to search for into the provided input area. You can then use the icons on the right hand side of the input area to help refine your search:

- **Match case** returns only matches with the specified case.
In the example below, instances of *TicketList* will appear as a match, but *ticketlist* would not.

:::image type="content" source="media/formula-bar-find-replace/match-case.png" alt-text="The Match Case refiner icon on the Find and Replace control":::

- **Match Whole Word** returns only exact matches of the entire sequence of characters.
In the example below, instances of *Ticket* returns no matches although the word *Ticket* appears within names several times in the formula.

:::image type="content" source="media/formula-bar-find-replace/match-whole-word.png" alt-text="The Match Whole Word refiner icon on the Find and Replace control":::

- **Use regular expression (RegEx)** returns only matches conforming to the regular expression specified within the input area. See [regular-expression syntax](/previous-versions/1400241x(v=vs.100)) for an introduction to the syntax.
In the example below, using the Regular Expression search capability with *Screen(Priority|Task)* returns matches for Screen when it appears together with either Priority or Task as in the control names shown below.

:::image type="content" source="media/formula-bar-find-replace/regex-highlighting.png" alt-text="The formula in the formula bar with matching results highlighted for the regular expression shown in the Find and Replace control":::

:::image type="content" source="media/formula-bar-find-replace/use-regular-expression.png" alt-text="The Use Regular Expression refiner icon on the Find and Replace control":::

- Use the **Previous Match** and **Next Match** arrow icons to move forward and backward through any matches the search returns. As you move through the matches, the match position updates and the row containing the match is highlighted to let you know which match you are currently working with.

:::image type="content" source="media/formula-bar-find-replace/match-highlighting.png" alt-text="The formula in the formula bar with a line highlighted for the match currently in focus from using the previous match and next match arrow icons":::

:::image type="content" source="media/formula-bar-find-replace/previous-next-arrow.png" alt-text="The previous match arrow and next match arrow icons in the center of the Find and Replace control":::

- **Find in selection** limits the search area within a formula to only the selected portion of a formula. To select part of the formula, Select and hold at the beginning of the desired searching area and then drag your cursor to highlight the entire desired area. To select using the keyboard, move cursor focus to the beginning of the desired search area, then hold shift and use the arrow keys to highlight the desired search area.  

In the example below, the search has been limited to the selected area, so the search now only returns two matches instead of the four matches returned previously.

:::image type="content" source="media/formula-bar-find-replace/selection-highlighting.png" alt-text="The formula in the formula bar showing a selected block of text":::

:::image type="content" source="media/formula-bar-find-replace/find-in-selection.png" alt-text="The Find in Selection icon near the right hand side of the Find and Replace control":::

### Replace

By default, the Find and Replace control opens in collapsed format and only displays the Find capability. To expand the control and show the Replace capability, select the icon to the left of the search input box, or press Ctrl + H on your keyboard. To collapse again, select the rotated icon.

:::image type="content" source="media/formula-bar-find-replace/toggle-replace-mode.png" alt-text="The Toggle Replace Mode icon on the left hand side of the Find and Replace control, before the text input areas":::

:::image type="content" source="media/formula-bar-find-replace/collapse-replace-mode.png" alt-text="The Collapse Replace Mode icon on the left hand side of the Find and Replace control, before the text input areas":::

In the Replace input area, specify the word or sequence of characters you’d like to replace the search text.

Use the Replace or Replace All icons to update one or all matches returned with the specified word/characters.

:::image type="content" source="media/formula-bar-find-replace/replace-one-replace-all.png" alt-text="The Replace and Replace All icons on the right hand side of the Find and Replace control, after the Replace text input field. The Replace icon is first, Replace All icon is second":::

### See also

[Get started with formulas in canvas apps](working-with-formulas.md)
[Add and configure controls](add-configure-controls.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
