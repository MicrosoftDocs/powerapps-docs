---
title: Review a canvas app for accessibility in Power Apps
description: Identify ways to make a canvas app more accessible to users who have vision, hearing, and other impairments
author: emcoope-msft
ms.service: powerapps
ms.topic: article
ms.date: 02/18/2021
ms.subservice: canvas-maker
ms.author: emcoope
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---

# Review a canvas app for accessibility in Power Apps

Users who have vision, hearing, or other impairments can use your canvas app more easily and successfully if you consider accessibility as you design how the app looks and behaves. If you're not sure how to make your app more accessible, you can run the Accessibility checker in Power Apps Studio. This tool not only finds potential accessibility issues but also explains why each might be a potential problem for users who have a specific disability and offers suggestions on how to resolve each issue.
The Accessibility checker detects screen-reader and keyboard issues for you, and you can find information about how to fix color-contrast issues  by using [accessible colors](accessible-apps-color.md).

The Accessibility checker helps you identify settings that you might want to change, but you should always consider the suggestions in the context of what your app needs to do. Many suggestions may be worthwhile, but you can ignore any that might do more harm than good.

## Find accessibility issues

1. In the upper-right corner of Power Apps Studio, select the icon for the App checker.

    ![App checker icon.](./media/accessibility-checker/app-checker-icon.png)

2. In the menu that appears, select **Accessibility**.

    ![App checker pane list of options.](./media/accessibility-checker/app-checker-menu.png)

    A list of issues appears, sorted first by severity and then by screen.

    ![Accessibility checker pane and list of items.](./media/accessibility-checker/accessibility-checker-pane.png)

3. Select the arrow next to an item to show details about it.

    ![Accessibility checker details.](./media/accessibility-checker/details-pane.png)

4. Select the back arrow to return to the list of items.

5. If you decide to address an issue, select it to open the affected property.

6. After you change one or more properties, select **Re-check** to update the list of issues.

    Resolved items disappear from the list, and new items may appear.

## Severity of issues

The Accessibility checker classifies each issue as an error, a warning, or a tip based the issue's severity.

- **Errors** identify issues that make the app difficult or impossible to use and understand for users who have a disability.
- **Warnings** identify issues that make the app difficult to use or understand for most but not all users who have a disability.
- **Tips** help you improve the experience of users who have a disability.

## Types of issues

| Issue Title                            | Severity | Issue Description  | How to fix | Why fix|
| ------------------------------         |:---------| -----| ------|------ |
| **Missing accessible label**           | Error    | When the accessible-label property of an interactive control contains no text. An interactive control can be inherently interactive, as a button is, or it has interactive properties. For example, you might have set the **OnSelect** property of an image or set its **TabIndex** property to 0 or higher.  | Edit the accessible-label property to describe the item. | If the accessible-label property contains no text, people who can’t see the screen won't understand what’s in images and controls. |
| **Focus isn't showing**                | Error    | When the **FocusBorderThickness** of a control is set to 0. It is good practice to ensure a proper color-contrast ratio between the focus border and the control itself so it's clearly visible. | Change the **FocusedBorderThickness** property to a value that's higher than 0.  | If the focus isn't visible, people who don't use a mouse can't see it when they interact with the app.   |
| **Missing captions**                   | Warning  | When the **ClosedCaptionsURL** property of an **Audio** or **Video** control is empty. | Set the **ClosedCaptionsURL** property to the URL for captions. | Without captions, people who have disabilities might not get any information from a video or audio segment. |
| **Missing helpful control settings**   | Warning  | When any of several settings (such as showing labels and markers for charts and showing default controls for **Audio**, **Video**, and **Pen input** controls) are turned off. | Select the warning, and then set the property to **true**. | By changing this property setting, you give the user better information about how the controls in your app function. |
| **HTML won't be accessible**           | Warning  | When a control other than an HTML text control contains HTML. In that case, Power Apps doesn't support accessibility of custom HTML elements. | Use a method other than HTML, or remove the HTML from this element. | Your app won't work correctly or be accessible if you add interactive HTML elements. |
| **Turn off autostart**                 | Warning  | When an **Audio** or **Video** control's **Autostart** property is set to **true**. | Set the control's **Autostart** property to **false**. | Video and audio files that play automatically can distract users. Let them choose whether to play a clip. |
| **Revise screen name**                 | Tip      | When a screen has a default name, which will be read out by screen readers when users navigate the app. | Give the screen a name that describes what's on the screen or what it's used for.| People who are blind, have low vision, or a reading disability rely on screen names to navigate using the screen reader. |
| **Add State indication text**          | Tip      |  When a control that has a state, such as a toggle, but the value labels are turned off. | Set the **ShowValue** property of the control to **true** to show its current state. | Users won't get confirmation of their actions if the state of the control doesn't appear. |
| **Check the order of the screen items**| Tip      | When the **TabIndex** property is greater than 0. App creators can set custom tab orders by setting the **TabIndex** property to a value greater than 0 but it is highly discouraged as it is hard to get right, maintain, and can break screen readers. | Set all **TabIndex** properties to 0 or -1 whenever possible.  Instead of using **TabIndex**, use the **Enhanced group** control to change the navigation order from the default.  If values of **TabIndex** greater than 0 must be used, make sure that your screen elements match the order in which you'd want to tab through them. | The navigation order should mirror the order in which controls appear on the screen, which is the default.  If manual adjustments are made, it is difficult to maintain the correct order especially in the presence of the browser's address bar and other controls outside of the app.  This can make a screen reader very difficult to use.  When read by the screen reader, the controls should be presented in the same order in which they are seen on the screen, instead of an order that's less intuitive.  |
| **Add another input method**           | Tip      | When an app contains a **Pen** control. This tip reminds you to include a separate method of input. | Add a **Text input** control in addition to the **Pen** control for an accessible experience. | Some users can't use a pen and require another way to provide information (for example, by typing a signature). |

## Next steps

[Accessibility limitations in canvas apps](accessible-apps-limitations.md)

### See also

- [Create accessible apps](accessible-apps.md)
- [Accessible app structure](accessible-apps-structure.md)
- [Accessible colors in Power Apps](accessible-apps-color.md)
- [Show or hide content from assistive technologies for canvas apps](accessible-apps-content-visibility.md)
- [Announce dynamic changes with live regions for canvas apps](accessible-apps-live-regions.md)
- [Accessibility properties](controls/properties-accessibility.md)
