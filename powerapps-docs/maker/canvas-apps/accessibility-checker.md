---
title: Accessibility checker | Microsoft Docs
description: How to use the accessibility checker tool to make apps accessible
author: emcoope-msft

ms.service: powerapps
ms.topic: article
ms.date: 06/29/2018
ms.author: emcoope-msft

---

# The Accessibility Checker
An accessible app will allow users with vision, hearing and other impairments to successfully use the app.  To help ensure that your PowerApps apps are accessible, use the Accessibility Checker, a free tool available in the canvas studio. It finds accessibility issues and explains why each might be a potential problem for someone with a disability. It also offers suggestions on how to resolve each issue.
The Accessibility Checker will detect screen reader and keyboard issues, however it is not able to detect color contrast issues yet. Reference **[accessible colors in PowerApps](canvas-apps/accessible-apps-color.md)** documentation for more information on ensuring proper color contrast. 

## How to use the App checker for Accessibility
The Accessibility checker is intended to be for guidance rather than an absolute rule of what is wrong. There will always be scenarios where the author of the app will have to make some decisions about accessibility themselves. The following steps explain how to take advantage of the Accessibility Checker. 

1. Select the App Checker icon in the top right corner. 

    ![App checker icon](./media/accessibility-checker/app-checker-icon.png/)

2.  Select **Accessibility** in the list of options in the pane that opens.

    ![App checker pane list of options](./media/accessibility-checker/app-checker-pane.png/)

3. A list of the issues within your app will be displayed in a list according to severity, then ordered by Screen. Selecting the item will navigate to the property with the issue. This is a very useful shortcut. Select "Re-check" in order to update the list of issues. Resolved items will disappear from the list, and new items will appear.

    ![Accessibility checker pane and list of items](./media/accessibility-checker/accessibility-checker-pane.png/)

4. Select the chevron on the item to open up more details about the issue in the pane. Select the back arrow to return to the list of items. 

    ![Accessibility checker details](./media/accessibility-checker/details-pane.png/)


## Severity of issues
The Accessibility Checker verifies your app against a set of rules that identify possible issues for people who have disabilities. Depending on how severe the issue is, the Accessibility Checker classifies each issue as an error, warning, or tip.
- **Error.** App items that makes the app difficult or impossible to use and understand for people with disabilities
- **Warning.** App items that in most (but not all) cases makes the app difficult to use or understand for people with disabilities
- **Tip.** App items that people with disabilities can use or understand but that could be created in a different way to improve the user’s experience

## List of Accessibility issues
These are the list of issues raised by the Accessibility Checker. 
| Issue Title                            | Severity | Issue Description  | How to fix | Why fix|
| ------------------------------         |:---------| -----| ------|------ |
| **Missing accessible label**           | Error    | When there is no text in the accessible label property of an interactive control, this error is raised. An interactive control is one that is either inherently interactive like a button, or a control that has interactive properties (its OnSelect property is set or it has a TabIndex of 0 or higher.)  | Edit the accessible label property to describe the item. | If there's no accessible text, people who can’t see the screen won't understand what’s in images and controls. |
| **Focus isn't showing**                | Error    | This error is raised when there the ForcusBorderThickness is 0. It is good practise to ensure a proper color contrast ratio between the focus border and the control itself so it is clearly visible.  | Change the FocusedBorderThickness property to be more than 0.  | If the focus isn't visible, people who don't use a mouse won't be able to see it when they're interacting with the app.   |
| **Missing captions**                   | Warning  | On the audio and video controls, there is a ClosedCaptionsURL property, and if it is empty this warning will appear. | Use the ClosedCaptionsURL property to add the URL for captions. | Without captions, people with disabilities may not get any of the information in a video or audio segment. |
| **Missing helpful control settings**   | Warning  | There are several settings such as showing labels and markers for charts, showing default controls for audio, video, and  pen input controls. Turning on these settings improves the usability of your app.  | Select the warning and set the item property to true to enable control setting.  | Changing this property setting will give the user better information about the function of the controls in your app. |
| **HTML won't be accessible**           | Warning  | The HTML text control is capable of having HTML code. This warning will be raised as the accessibility for custom elements is not supported through this control. | Use another method instead of HTML, or remove the HTML from this element. | Your app won't work correctly and will not be accessible if you place interactive HTML elements. |
| **Turn off autostart**                 | Warning  | The app creator has the option to have video and audio play automatically and when this setting is true, this warning will be raised.  | Set autostart for video and audio to False.  | Autostart of video and audio files can be distracting. Let users choose whether to play or not. |
| **Revise screen name**                 | Tip      | The name of the screen is read out by the screen reader when navigating the app. This tip is raised if there is a default screen name used. | Give the screen a title that describes what's on the screen or what it's used for.| People who are blind, have low vision, or a reading disability rely on screen titles to navigate using the screen reader. |
| **Add State indication text**          | Tip      |  For controls that have a state, such as a toggle, this tip is raised if the value labels are turned off. | Set ShowValue = true to show the current state of the control. | Users won't get confirmation of their actions if the of the state of the control isn't showing. |
| **Check the order of the screen items**| Tip      | App creators are able to set custom tab orders by setting numerical values 1, 2, 3, 4 etc... in the TabIndex property. This tip is raised when TabIndex is greater than 1 to ensure that you review the interactive order for this screen. To maximize not only accessiblity but also general usability, lay out controls in a logical sequence, both left to right and top to bottom. If you then set the **[TabIndex](controls/properties-accessibility.md)** property of all interactive elements to 0, users can press the Tab key to activate each element in the same logical sequence.  | Make sure that your screen elements match the order in which you'd want to tab through them. | When a screen reader reads the elements of aan app, it's important that they appear in the order that a user would see them, instead of a different non-intuitive order.  |
| **Add another input method**           | Tip      | If there is a pen control, this tip will be raised as a reminder to include a separate method of input. | Add a text input in addition to the pen control for an accessible experience. | Some users can't use a pen and require another way to input information. Example: Typing in a signature. |



Related:
- [Create accessible apps](canvas-apps/accessible-apps.md)
- [Accessible colors in PowerApps](canvas-apps/accessible-apps-color.md)
- [Accessibility properties](controls/properties-accessibility.md)
