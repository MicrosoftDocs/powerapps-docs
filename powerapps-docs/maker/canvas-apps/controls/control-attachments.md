---
title: Attachments control in Power Apps
description: Learn about the details, properties and examples of the attachments control in Power Apps.
author: yogeshgupta698
ms.topic: reference
ms.custom: canvas
ms.date: 12/16/2025
ms.subservice: canvas-maker
ms.author: yogupt
ms.reviewer: mkaur
search.audienceType: 
  - maker
contributors:
  - mduelae
  - yogupt
---

# Attachments control in Power Apps

A control that allows users to download files to their device, as well as upload and delete files from a list created using Microsoft Lists, or a Microsoft Dataverse table.

## Description
An **Attachments** control lets you open, add, and delete files from a list or a Dataverse table.

## Limitations

The attachment control has these limitations:

1. The attachment control only supports lists and Dataverse tables as the data sources. Expressions that transform these data sources into Tables, for example, with the **ForAll** function, are not supported.

1. Upload and delete functionality work only inside a form. The Attachment control appears disabled when in Edit mode and not inside a form. To save file additions and deletions, the app user must save the form. Because of this limitation, the Attachment control isn't available from the **Insert** tab but appears in the form when the Attachment form field is enabled in a SharePoint or Dataverse form.

1. Attachments control on a web browser lets you select multiple files, and allows use of drag and drop functionality. However, when using attachments control on [Power Apps Mobile](https://powerapps.microsoft.com/downloads/), you can only add files one at a time.

1. Files stored in OneDrive or any other cloud storage may not be attached correctly. Try downloading these files to the device before attaching them using the device's file picker.

1. The Power Apps mobile app doesn't support capturing videos directly from the camera or selecting videos from the photo library when using the **Attachments** control. To add a video, users must use the **Browse** option.
   - **On Android**: The **Browse** option displays all file types, including videos, letting you to select and attach your video files.
   - **On iOS**: The **Browse** option only shows files stored in the Files app. If your video isn't already saved there, you need to move it to the Files app before you attach it.
   
   If a video doesn't appear as an option to attach, first save the video to your device’s Files app and then try again.

## Key properties
**[Items](properties-core.md)** – The **Attachment** column of the list or Dataverse table. [Collections](../create-update-collection.md) and [Tables](../working-with-tables.md) are not supported.

**MaxAttachments** – The maximum number of files the control will accept.

**MaxAttachmentSize** – The maximum allowed file size in MB of each new attachment. 1 MB here is 1,000,000 bytes (10<sup>6</sup> B) or 1,000 KB.

**OnAddFile** – Actions to perform when the user adds a new file attachment.

**OnRemoveFile** – Actions to perform when the user deletes an existing attachment.

**OnUndoRemoveFile** – Actions to perform when the user restores a deleted attachment.

## Additional properties
**[AccessibleLabel](properties-accessibility.md)** – Label for screen readers. Should describe the purpose of the attachments.

**AddAttachmentText** – The label text for the link used to add a new attachment.

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[Color](properties-color-border.md)** – The color of a control's text.

**[DisabledBorderColor](properties-color-border.md)** – The color of a control's border if the control's **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[DisabledColor](properties-color-border.md)** – The color of text in a control if its **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[DisabledFill](properties-color-border.md)** – The background color of a control if its **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[DisplayMode](properties-core.md)** – Whether the control allows adding and deleting files (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[DropTargetBackgroundColor]** – The color of the control's drop target background.

**[DropTargetBorderColor]** – The color of the control's drop target border.

**[DropTargetBorderStyle]** – Whether the control's drop target border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[DropTargetBorderThickness]** – The thickness of the control's drop target border.

**[DropTargetTextColor]** – The color of the control's drop target text.

**[Fill](properties-color-border.md)** – The background color of a control.

**[FocusedBorderColor](properties-color-border.md)** – The color of a control's border when the control is focused.

**[FocusedBorderThickness](properties-color-border.md)** – The thickness of a control's border when the control is focused.

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**[Font](properties-text.md)** – The name of the family of fonts in which text appears.

**[FontWeight](properties-text.md)** – The weight of the text in a control: **Bold**, **Semibold**, **Normal**, or **Lighter**.

**[HoverBorderColor](properties-color-border.md)** – The color of a control's border when the user keeps the mouse pointer on that control.

**[HoverColor](properties-color-border.md)** – The color of the text in a control when the user keeps the mouse pointer on it.

**[HoverFill](properties-color-border.md)** – The background color of a control when the user keeps the mouse pointer on it.

**[Italic](properties-text.md)** – Whether the text in a control is italic.

**MaxAttachmentsText** – The text that replaces the "Attach file" link when the control contains the maximum number of files allowed.

**NoAttachmentsText** – Informational text shown to the user when there are no files attached.

**[Padding](properties-size-location.md)** – The distance between the text on an import or export button and the edges of that button.

**[PressedBorderColor](properties-color-border.md)** – The color of a control's border when the user selects that control.

**[PressedColor](properties-color-border.md)** – The color of text in a control when the user selects that control.

**[PressedFill](properties-color-border.md)** – The background color of a control when the user selects that control.

**Reset** – Reverts all changes to the attachments control returning to the previously saved state.

**[Size](properties-text.md)** – The font size of the text that appears on a control.

**[Strikethrough](properties-text.md)** – Whether a line appears through the text that appears on a control.

**[TabIndex](properties-accessibility.md)** – Keyboard navigation order in relation to other controls.

**[Tooltip](properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Underline](properties-text.md)** – Whether a line appears under the text that appears on a control.

**[Visible](properties-core.md)** – Whether a control is visible or hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (or screen, if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (or screen, if no parent container).


## Example
1. Add a form to your app, and set a list as its data source.

2. Select the **Display Form** control in the tree view on the left-hand side. You can also use **Edit Form** instead.

3. Select **Data Source** in the Properties tab in the options panel on the right and then select the list you connected to.

4. Select **Edit fields** in *Fields* section and select **Add field**. 

5. Select the **Attachments** field and select **Add**.

    The Attachments field associated with the list will appear in the form.

[Learn how to add and configure a control](../add-configure-controls.md)


## Accessibility guidelines
### Color contrast
There must be adequate color contrast between:
* **ItemColor** and **ItemFill**
* **ItemHoverColor** and **ItemHoverFill**
* **ItemPressedColor** and **ItemPressedFill**
* **AddedItemColor** and **AddedItemFill**
* **RemovedItemColor** and **RemovedItemFill**
* **ItemErrorColor** and **ItemErrorFill**
* **AddAttachmentColor** and **Fill**
* **MaxAttachmentsColor** and **Fill**
* **NoAttachmentsColor** and **Fill**

This requirement is in addition to the [standard color contrast requirements](../accessible-apps-color.md).

### Screen reader support
The following properties must be present:
* **[AccessibleLabel](properties-accessibility.md)**
* **AddAttachmentsText**
* **MaxAttachmentsText**
* **NoAttachmentsText**

### Keyboard support
* **[TabIndex](properties-accessibility.md)** must be zero or greater so that keyboard users can navigate to it.
* Focus indicators must be clearly visible. Use **[FocusedBorderColor](properties-color-border.md)** and **[FocusedBorderThickness](properties-color-border.md)** to achieve this clarity.


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]


