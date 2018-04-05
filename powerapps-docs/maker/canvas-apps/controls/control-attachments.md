---
title: 'Attachments control: reference | Microsoft Docs'
description: Information, including properties and examples, about the Attachments control
services: ''
suite: powerapps
documentationcenter: na
author: fikaradz
manager: anneta
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 09/29/2017
ms.author: fikaradz

---
# Attachments control in PowerApps
A control that allows users to download files to their device, as well as upload and delete files from a SharePoint list.

## Limitations
The attachment control has the following temporary limitations:
1. Attachment download is not supported in Internet Explorer.

1. Attachment upload only works with SharePoint list data sources.  Support for other data sources will be introduced incrementally, starting with CDS.

1. Upload and delete functionality only work inside a form.  Attachment control will look disabled when in Edit mode and not inside a form.   Note that in order to save the file additions and deletions to the back end, the end user must save the form.

1. You can only upload files up to 10 MB in size.  

## Description
An **Attachments** control lets you open files stored on a data source as well as add and delete files from a SharePoint list.

## Key properties
**[Items](properties-core.md)** – The source describing the files that can be downloaded.

**MaxAttachments** – The maximum number of files the control will accept.

**MaxAttachmentSize** – The maximum allowed file size in MB of each new attachment.  Currently there is a limit of 10 MB.

**OnAttach** – How the app responds when the user adds a new file attachment.

**OnRemove** – How the app responds when the user deletes an existing attachment.

**[OnSelect](properties-core.md)** – How the app responds when the user clicks on an attachment.

## Additional properties
**AccessibleLabel** – The label announced by screen readers.

**AddAttachmentText** – The label text for the link used to add a new attachment.

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[DisplayMode](properties-core.md)** – Whether the control allows adding and deleting files (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**MaxAttachmentsText** – The text that replaces the "Attach file" link when the control contains the maximum number of files allowed.

**NoAttachmentsText** – Informational text shown to the user when there are no files attached.

**[Visible](properties-core.md)** – Whether a control is visible or hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (or screen, if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (or screen, if no parent container).


## Example
1. Create an app from data using a SharePoint list as a data source.  Alternatively, add a form to your app and set a SharePoint list as its data source.

2. Select the **Form** control in the tree view on the left-hand side.

3. Click **Data** in the Properties tab in the options panel on the right.

4. Under **Fields**, enable the **Attachments** field.

    The Attachments field associated with the SharePoint list will appear in the form.

Don't know how to [add and configure a control](../add-configure-controls.md)?
