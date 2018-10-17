---
title: 'Attachments control: reference | Microsoft Docs'
description: Information, including properties and examples, about the Attachments control
author: fikaradz
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.date: 04/23/2018
ms.author: fikaradz
ms.reviewer: anneta
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Attachments control in PowerApps
A control that allows users to download files to their device, as well as upload and delete files from a SharePoint list or a Common Data Service for Apps entity.

## Limitations
The attachment control has these limitations:
1. Attachments are supported with SharePoint lists and CDS for Apps entities.

1. Upload and delete functionality only work inside a form.  Attachment control will look disabled when in Edit mode and not inside a form. Note that in order to save the file additions and deletions to the back end, the end user must save the form.

1. You can only upload files up to 10 MB in size.  

## Description
An **Attachments** control lets you open, add, and delete files from a SharePoint list or a CDS for Apps entity.

## Key properties
**[Items](properties-core.md)** – The source describing the files that can be downloaded.

**MaxAttachments** – The maximum number of files the control will accept.

**MaxAttachmentSize** – The maximum allowed file size in MB of each new attachment.  Currently there is a limit of 10 MB.

**OnAttach** – How the app responds when the user adds a new file attachment.

**OnRemove** – How the app responds when the user deletes an existing attachment.

**[OnSelect](properties-core.md)** – How the app responds when the user clicks on an attachment.

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

**[TabIndex](properties-accessibility.md)** – Keyboard navigation order in relation to other controls.

**[Visible](properties-core.md)** – Whether a control is visible or hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (or screen, if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (or screen, if no parent container).


## Example
1. Create an app from data using a SharePoint list as a data source. As an alternative, add a form to your app, and set a SharePoint list as its data source.

2. Select the **Form** control in the tree view on the left-hand side.

3. Click **Data** in the Properties tab in the options panel on the right.

4. Under **Fields**, enable the **Attachments** field.

    The Attachments field associated with the SharePoint list will appear in the form.

[Learn how to add and configure a control].(../add-configure-controls.md)


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
