---
title: Attachments control in Power Apps
description: Learn about the details, properties and examples of the attachments control in Power Apps.
author: chmoncay
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.date: 07/06/2021
ms.author: chmoncay
ms.reviewer: tapanm
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---

# Attachments control in Power Apps

A control that allows users to download files to their device, as well as upload and delete files from a SharePoint list or a Microsoft Dataverse table.

## Limitations

The attachment control has these limitations:
1. Attachments are supported with SharePoint lists and Dataverse tables.

1. Upload and delete functionality work only inside a form. The Attachment control appears disabled when in Edit mode and not inside a form. To save file additions and deletions, the app user must save the form. Because of this limitation, the Attachment control isn't available from the **Insert** tab but appears in the form when the Attachment form field is enabled in a SharePoint or Dataverse form.

## Description
An **Attachments** control lets you open, add, and delete files from a SharePoint list or a Dataverse table.

## Key properties
**[Items](properties-core.md)** – The source describing the files that can be downloaded.

**MaxAttachments** – The maximum number of files the control will accept.

**MaxAttachmentSize** – The maximum allowed file size in MB of each new attachment.  Currently there is a limit of 50 MB.

**OnAddFile** – Actions to perform when the user adds a new file attachment.

**OnRemoveFile** – Actions to perform when the user deletes an existing attachment.

**OnUndoRemoveFile** – Actions to perform when the user restores a deleted attachment.

## Additional properties
**[AccessibleLabel](properties-accessibility.md)** – Label for screen readers. Should describe the purpose of the attachments.

**AddAttachmentText** – The label text for the link used to add a new attachment.

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[DisplayMode](properties-core.md)** – Whether the control allows adding and deleting files (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[FocusedBorderColor](properties-color-border.md)** – The color of a control's border when the control is focused.

**[FocusedBorderThickness](properties-color-border.md)** – The thickness of a control's border when the control is focused.

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**MaxAttachmentsText** – The text that replaces the "Attach file" link when the control contains the maximum number of files allowed.

**NoAttachmentsText** – Informational text shown to the user when there are no files attached.

**Reset** – Reverts all changes to the attachments control returning to the previously saved state.

**[TabIndex](properties-accessibility.md)** – Keyboard navigation order in relation to other controls.

**[Visible](properties-core.md)** – Whether a control is visible or hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (or screen, if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (or screen, if no parent container).


## Example
1. Add a form to your app, and set a SharePoint list as its data source.

2. Select the **Display Form** control in the tree view on the left-hand side. You can also use **Edit Form** instead.

3. Select **Data Source** in the Properties tab in the options panel on the right and then select the SharePoint list you connected to.

4. Select **Edit fields** in *Fields* section and select **Add field**. 

5. Select the **Attachments** field and select **Add**.

    The Attachments field associated with the SharePoint list will appear in the form.

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

This is in addition to the [standard color contrast requirements](../accessible-apps-color.md).

### Screen reader support
The following properties must be present:
* **[AccessibleLabel](properties-accessibility.md)**
* **AddAttachmentsText**
* **MaxAttachmentsText**
* **NoAttachmentsText**

### Keyboard support
* **[TabIndex](properties-accessibility.md)** must be zero or greater so that keyboard users can navigate to it.
* Focus indicators must be clearly visible. Use **[FocusedBorderColor](properties-color-border.md)** and **[FocusedBorderThickness](properties-color-border.md)** to achieve this.


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
