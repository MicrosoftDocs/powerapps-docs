---
title: Attachments modern control in canvas apps (preview) - Power Apps
description: Add, download, and remove attachments in canvas apps with the modern Attachments control, inside a form or with Power Fx.
author: yogeshgupta698
ms.topic: reference
ms.custom: canvas
ms.date: 10/01/2026
ms.subservice: canvas-maker
ms.author: yogupt
ms.reviewer: joshuapa
ai-usage: ai-generated
search.audienceType:
  - maker
---

# Attachments modern control in canvas apps (preview)

The modern **Attachments** control lets users add, download, and remove files associated with a record. Use it to collect supporting documents for a request, attach receipts to an expense, or review files without leaving your canvas app.

> [!IMPORTANT]
> This is a preview feature. Preview features aren't meant for production use and might have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.

## Modern and classic attachments

Unlike the [classic Attachments control](../control-attachments.md), the modern control can work outside a form. Its **Attachments** output can be passed directly to **Patch**. Inside a form, use **SubmitForm** to save the record and its attachments.

The modern control provides:

- A file picker and a web drag-and-drop area for adding files.
- File-count, file-size, and file-type restrictions for new attachments.
- Indicators that distinguish saved files, unsaved additions, and files marked for removal.
- File-type icons and styling that follows the app's modern theme.
- Per-file events for responding to additions and removals.

> [!IMPORTANT]
> Adding a file to the control stages it in the app. It doesn't save the file to the data source. Save additions and removals explicitly with **Patch** or **SubmitForm**.

## Key properties

Use these properties to bind the control and configure file selection.

| Property | Description |
| --- | --- |
| **Items** | The files to display. Bind to a record's attachment table for SharePoint or Dataverse attachments. For a standalone upload to a Dataverse file column, see [Dataverse file column](#dataverse-file-column). |
| **MaxAttachments** | The maximum number of attachments the control accepts. This limit is separate from the size limit for each file. |
| **MaxAttachmentSize** | The maximum size of each new attachment, in MB. The data source can also enforce its own limits. |
| **AcceptedFileTypes** | A single-column table of accepted file extensions, such as `[".pdf", ".docx"]`. It doesn't invalidate existing saved attachments. |
| **DisplayMode** | **Edit** allows additions and removals. **View** hides the drop area and upload actions and displays existing files for download. **Disabled** prevents interaction. |
| **AccessibleLabel** | A screen-reader label that describes the purpose of the attachments, such as `"Supporting documents for this request"`. |
| **BasePaletteColor** | The base color used for the control's palette. |

File-type restrictions guide file selection; they don't replace data-source validation or your organization's file-security policies.

## Events and outputs

Use events to respond to user actions and outputs to save changes or show status.

| Property | Description |
| --- | --- |
| **Attachments** | The attachment table to save to the record's attachment column. Pass this output directly to **Patch** for attachment columns. For a Dataverse file column, build a single record with **FileName** and **Value** from the selected file, as shown in [Dataverse file column](#dataverse-file-column). |
| **AttachmentsCount** | The current attachment count, excluding files marked for removal. |
| **IsUploading** | Whether files are being added to the control's in-memory state. This isn't confirmation that **Patch** or **SubmitForm** has saved the files. |
| **OnAddFile** | Actions to run for each added file. Adding multiple files triggers this event once per file, not once per batch. |
| **OnRemoveFile** | Actions to run when a user removes an attachment. |
| **OnSelect** | Actions to run when a user selects a file. The default action downloads or opens the file; you can customize the action. |
| **OnError** | Actions to run when adding a file fails, such as when the file exceeds a configured limit. Handle data-source save failures separately. |

## Examples

The following examples cover Dataverse attachments, a Dataverse file column, and SharePoint attachments. Before you begin, enable [modern controls and themes](overview-modern-controls.md) in your canvas app.

### Dataverse attachments

Use an edit form to manage multiple attachments on a Dataverse record. This example uses a table named `Projects` and a gallery named `ProjectsGallery`.

1. [Enable attachments on the Dataverse table](../../../data-platform/create-edit-entities-portal.md), add at least one record, and connect the table to your app. When you enable attachments, you can attach notes and files to records. This feature isn't the same as adding a file column.
2. Set the gallery's **Items** property to `Projects`. Add an **Edit form** named `ProjectForm`, set its **DataSource** to `Projects`, and set its **Item** to `ProjectsGallery.Selected`.
3. In the form's properties pane, select **Edit fields** > **Add field**, and add **Attachments**. Keep the generated data card's binding and update formulas.
4. Select the modern **Attachments** control in the data card. Set **MaxAttachments** to `5` and **MaxAttachmentSize** to `10`.
5. Add a **Save** button and set its **OnSelect** property to:

   ```power-fx
   SubmitForm(ProjectForm)
   ```

6. Set the **Save** button's **DisplayMode** to `If(IsBlank(ProjectsGallery.Selected), DisplayMode.Disabled, DisplayMode.Edit)`. Set the form's **OnSuccess** property to `Notify("Project saved.", NotificationType.Success)` and its **OnFailure** property to `Notify(ProjectForm.Error, NotificationType.Error)`.
7. Add a **Cancel** button with **OnSelect** set to `ResetForm(ProjectForm)` to discard unsaved form edits.
8. Run the app, select a project, add files, and select **Save**. Reopen the record to confirm the files were saved. To delete a saved attachment, remove it in the control and save the form again.

For more information, see [Form modern control](modern-control-form.md).

### Dataverse file column

A Dataverse file column stores one file per record. Unlike an attachment column, it accepts a single file record rather than the control's entire **Attachments** table.

This example uploads a file to an existing record without a form. It uses a Dataverse table named `'Project Documents'`, a file column named `'Document File'`, and a gallery named `DocumentsGallery`.

1. [Create a file column](../../../data-platform/types-of-fields.md#file-columns), add a record to the table, and connect the table to your app. Set the gallery's **Items** property to `'Project Documents'`.
2. Insert a modern **Attachments** control named `FileUpload1`. Set **Items** to `Blank()` so the control stages new uploads rather than displaying the saved file.
3. Set **MaxAttachments** to `1` and **MaxAttachmentSize** to `10`. Keep this size limit within the file column's configured maximum.
4. Add a **Save file** button and set its **OnSelect** property to:

   ```power-fx
   If(
       IsBlank(DocumentsGallery.Selected),
       Notify("Select a record before saving.", NotificationType.Warning),
       IsEmpty(FileUpload1.Attachments),
       Notify("Choose a file before saving.", NotificationType.Warning),
       IfError(
           Patch(
               'Project Documents',
               DocumentsGallery.Selected,
               {
                   'Document File': {
                       FileName: First(FileUpload1.Attachments).Name,
                       Value: First(FileUpload1.Attachments).Value
                   }
               }
           ); true,
           Notify("File couldn't be saved. " & FirstError.Message, NotificationType.Error),
           Reset(FileUpload1);
           Notify("File saved.", NotificationType.Success)
       )
   )
   ```

5. Run the app, select a record, choose a file, and select **Save file**. Check the record's **Document File** column to confirm the upload.

The formula maps the selected file's **Name** to **FileName** and its **Value** to the file content. Saving replaces any file already in that column. After a successful save, it clears the staged upload. Clearing the upload control doesn't delete a file already stored in the column.

### SharePoint attachments

Use the control's **Attachments** output to update a SharePoint list item's attachments directly with **Patch**, without an intermediary form.

Connect your app to a SharePoint list with attachments enabled and at least one item. This example uses a list named `Requests` and a gallery named `RequestsGallery` whose **Items** property is `Requests`.

1. Insert the modern **Attachments** control and name it `Attachments1`.
2. Set its **Items** property to the selected record's attachments:

   ```power-fx
   RequestsGallery.Selected.Attachments
   ```

3. Set **MaxAttachments** to `5` and **MaxAttachmentSize** to `10`. These are example limits; choose values appropriate for your data source and business requirements.
4. Add a **Save attachments** button. Set its **OnSelect** property to:

   ```power-fx
   If(
       IsBlank(RequestsGallery.Selected),
       Notify("Select a request before saving.", NotificationType.Warning),
       IfError(
           Patch(
               Requests,
               RequestsGallery.Selected,
               {Attachments: Attachments1.Attachments}
           ); true,
           Notify("Attachments couldn't be saved. " & FirstError.Message, NotificationType.Error),
           Notify("Attachments saved.", NotificationType.Success)
       )
   )
   ```

5. Run the app, select an existing request, and add a file. The file appears as unsaved. Select **Save attachments**, then reopen the record to confirm that the file was saved.
6. Remove a saved file and save again. Reopen the record to confirm that the removal was saved.

Keep the selected record unchanged while the user has unsaved attachment edits. Before letting users navigate to another record, provide a way to save or discard those edits.

For **Patch** error handling, see [IfError, IsError, IsBlankOrError, and Error functions](/power-platform/power-fx/reference/function-iferror).

#### Example YAML

The following control definition uses the SharePoint connection and `RequestsGallery` from this example. It accepts PDF and Word files, limits uploads to five files of 10 MB each, and disables editing when no request is selected. Use the **Save attachments** button and formula above to persist changes; this YAML only defines the attachment control.

```yaml
- Attachments1:
    Control: ModernAttachments@1.3.0
    Properties:
      Items: =RequestsGallery.Selected.Attachments
      MaxAttachments: =5
      MaxAttachmentSize: =10
      AcceptedFileTypes: =[".pdf", ".docx"]
      AccessibleLabel: ="Supporting documents for the selected request"
      DisplayMode: =If(IsBlank(RequestsGallery.Selected), DisplayMode.Disabled, DisplayMode.Edit)
      Width: =Min(Parent.Width, 480)
      Height: =300
      OnError: =Notify(Self.LastError.Message, NotificationType.Error)
```

## File limits, removal, and duplicate names

Explain these behaviors to your app's users:

| Action | Result |
| --- | --- |
| Add more files than the available attachment slots. | The control accepts files up to the limit and reports the files it couldn't add. Check the accepted files before saving. |
| Add a file that exceeds the size limit or doesn't match the accepted file types. | The control rejects the file and reports an error. |
| Remove a newly added, unsaved file. | The file is discarded from the staged additions. |
| Remove a saved file. | The file is marked for removal. Save the changes to delete it from the data source. |
| Add a file with the same name as an existing attachment. | The control adds a suffix to avoid a name collision. Don't treat a same-name upload as a replacement of the saved file. |

## Limitations

- Drag and drop is available on the web. On mobile, use the device's file picker.
- Mobile file availability and download behavior depend on the device and client. Validate downloads on your target devices; file-size metadata might not be available for every file.
- Dataverse file columns accept one file per record. Don't pass the entire **Attachments** table to a file column.
- Control limits don't override the data source's file-size restrictions or file-type policies.

## Related information

- [Classic Attachments control](../control-attachments.md).
- [Form modern control](modern-control-form.md).
- [Patch function](/power-platform/power-fx/reference/function-patch).
- [Modern controls overview](overview-modern-controls.md).
