---
title: Set up notes as attachments for basic and advanced forms
description: Adding notes to forms on your Power Apps portal is easy. This page explains how to add and configure notes as attachments on both basic and advanced forms.
author: gitanjalisingh33msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 08/12/2021
ms.subservice: portals
ms.author: gisingh
ms.reviewer: tapanm
contributors:
    - tapanm-msft
    - GitanjaliSingh33msft
    - nageshbhat-msft
---

# Configure notes as attachments for basic and advanced forms

Similar to subgrids, adding notes to your managed forms on the portal is easy. Just add the notes control to the model-drive app forms through the [form designer](../model-driven-apps/create-design-forms.md) and you're done. You can configure the behavior of the notes control by using metadata.

> [!NOTE]
> - You must enable attachments for the table in Microsoft Dataverse first before using this feature. More information: [Create a table](../data-platform/data-platform-create-entity.md#create-a-table)
> - Explicit [table permissions](configure/assign-entity-permissions.md) are required for any notes to appear on the portal. For the detailed steps on how to create and assign these, go to [Assign table permissions](#assign-table-permissions).
> - The description of each note must be prefixed with **\*WEB\*** (*'WEB' keyword with an asterisk sign (\*) before and after*) for the note to appear on the portal page.

## Notes configuration for basic forms

1. Open the [Portal Management](./configure/configure-portal.md) app.

1. Select **Basic Forms** under **Content** on the left pane.

    ![Basic forms.](media/configure-notes/entity-forms.png)

1. From the list of forms, select to open a record of the form to which you want to add note configuration.

1. From the available tabs in form settings, select **Basic Form Metadata**.

    ![Basic form metadata.](media/configure-notes/entity-form-metadata.png)

1. Select **New Basic Form Metadata**.

    ![New basic form metadata.](media/configure-notes/new-entity-form-metadata.png)

1. Select **Type** as **Note**.

    ![Type as Note.](media/configure-notes/type-notes.png)

1. The notes configuration settings are displayed. Most of the settings are collapsed by default. You can expand a section to see more settings.

    ![Notes options.](media/configure-notes/notes-options.png)

1. Fill in the fields by entering appropriate values. These settings are explained in more detail below under [Attributes](#attributes), [Create dialog options](#create-dialog-options), [Edit dialog options](#edit-dialog-options), and [Delete dialog options](#delete-dialog-options).

1. (Optional) If you created a custom form and added the notes section to it, be sure to select **Notes** as the default tab you want to be visible.

    ![Notes in a custom form.](media/notes-activities-tab.png "Notes in a custom form")

1. Save the form.

After adding the configuration, the note control will be rendered by using the appropriate options enabled on the portal.

### Attributes


| Name                  | Description                                                                                                                                                  |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Basic settings**    |                                                                                                                                                              |
| Create Enabled        | Enables the ability to add new notes to the table.                                                                                                          |
| Create Dialog Options | Contains settings for configuring the dialog box when **Create Enabled** is set to true. More information: [Create dialog options](#create-dialog-options).                                 |
| Edit Enabled          | Enables the ability to edit existing notes on the table.                                                                                                    |
| Edit Dialog Options   | Contains settings for configuring the dialog box when **EditEnabled** is set to true. More information: [Edit dialog options](#edit-dialog-options)                                         |
| Delete Enabled        | Enables the ability to delete notes from the table.                                                                                                         |
| Delete Dialog Options | Contains settings for configuring the dialog box when **DeleteEnabled** is set to true. More information: [Delete dialog options](#delete-dialog-options).           |
|File Attachment Location | Select the location of the file attachment:<ul><li>Note attachment</li><li>Azure Blob Storage</li></ul>|
|Accept MIME Type(s) | Allows you to specify a list of accepted MIME types. |
|Restrict MIME Types | Select whether to allow or restrict MIME types.|
|Maximum File Size (in KB) |Allows you to specify the maximum size of a file that can be attached. |
| **Advanced settings** |                                                                                                                                                              |
| List Title            | Overrides the title over the Notes area.                                                                                                                     |
| Add Note Button Label | Overrides the label on the Add Notes button.                                                                                                                 |
| Note Privacy Label    | Overrides the label denoting that a note is private.                                                                                                         |
| Loading Message       | Overrides the message shown while the list of notes is loading.                                                                                              |
| Error Message         | Overrides the message shown when an error occurs while trying to load the list of notes.                                                                     |
| Access Denied Message | Overrides the message shown when the user doesn't have sufficient permissions to view the list of notes.                                                    |
| Empty Message         | Overrides the message shown when the current table doesn't have any notes that can be viewed.                                                              |
| List Orders           | Allows you to set the order in which notes will be displayed. The List Orders setting allows you to set the following options: <ul><li>Attribute: The logical name of the column by which you wish to sort</li><li>Alias: The alias for the attribute in the query</li><li>Direction: Ascending (smallest to largest, or first to last), or Descending (largest to smallest, or last to first).</li></ul>  ![Set attributes for list orders.](media/set-attributes-list-orders.png "Set attributes for list orders") <br>  To add a sorting rule, select "Column" (4) and fill in the details. List Orders will be processed in order from the top of the list having highest priority.|
||

#### Create dialog options

| Name                               | Description                                                                                                                                 |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Basic settings**                 |                                                                                                                                             |
| Display Privacy Options Field      | Enables a checkbox in the Add Note dialog box that allows the user to mark a note as private.                                                   |
| Privacy Option Field Default Value | Specifies the default value for the Display Privacy Options Field. The default value of this field is false.                     |
| Display Attach File                | Enables a file upload field in the Add Note dialog box, allowing a user to attach a file to a note.  <br> **Note**: Only one file can be attached using this option.                                            |
| Attach File Accept                 | The MIME type accepted by the file upload input.                                                                                            |
| **Advanced settings**              |                                                                                                                                             |
| Note Field Label                   | Overrides the label for the Note field in the Add Note dialog box.                                                                              |
| Note Field Columns                 | Sets the columns value in the Note &lt;textarea&gt;.                                                                                            |
| Note Field Rows                    | Sets the rows value in the Note &lt;textarea&gt;.                                                                                            |
| Privacy Option Field Label         | Overrides the label for the Privacy Option Field (if enabled).                                                                              |
| Attach File Label                  | Overrides the label for the attached file (if enabled).                                                                                 |
| Left Column CSS Class              | Adds the CSS class or classes to the leftmost column containing labels in the Add Note dialog box.                                                  |
| Right Column CSS Class             | Adds the CSS class or classes to the rightmost column containing field inputs in the Add Note dialog box.                                           |
| Title                              | Overrides the HTML text in the header of the Add Note dialog box.                                                                               |
| Primary Button Text                | Overrides the HTML that appears in the Primary (Add Note) button in the dialog box.                                                           |
| Dismiss Button SR Text             | Overrides the screen reader text associated with the dialog box's dismiss button.                                                               |
| Close Button Text                  | Overrides the HTML that appears in the Close (Cancel) button in the dialog box.                                                               |
| Size                               | Specifies the size of the Add Note dialog box. The options are Default, Large, and Small.  |
| CSS Class                          | Specify a CSS class or classes that will be applied to the resulting dialog box.                                                                |
| Title CSS Class                    | Specifies a CSS class or classes that will be applied to the resulting dialog box's title bar.                                                    |
| Primary Button CSS Class           | Specifies a CSS class or classes that will be applied to the dialog box's Primary (Add Note) button.                                            |
| Close Button CSS Class             | Specifies a CSS class or classes that will be applied to the dialog box's Close (Cancel) button.                                                |
|||

#### Edit dialog options

| Name                               | Description                                                                                                                                   |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| **Basic settings**                 |                                                                                                                                               |
| Display Privacy Options Field      | Enables a checkbox in the Edit Note dialog box that allows the user to mark a note as private.  |
| Privacy Option Field Default Value | Specifies the default value for the Display Privacy Options Field. The default value of this field is false.   |
| Display Attach File                | Enables a file upload field in the Edit Note dialog box, allowing a user to attach a file to a note. <br> **Note**: Only one file can be attached using this option.                     |
| Attach File Accept                 | The MIME type accepted by the file upload input. |
| **Advanced settings**              |                                                                                              |
| Note Field Label                   | Overrides the label for the Note field in the Edit Note dialog box.|
| Note Field Columns                 | Sets the columns value in the Note &lt;textarea&gt;.                                                                                             |
| Note Field Rows                    | Sets the rows value in the Note &lt;textarea&gt;.                                                                                             |
| Privacy Option Field Label         | Overrides the label for the Privacy Option Field (if enabled).                                                                                
| Attach File Label                  | Overrides the label for the attached file (if enabled).                                                                                     |
| Left Column CSS Class              | Adds the CSS class or classes to the leftmost column containing labels in the Edit Note dialog box.                                                  |
| Right Column CSS Class             | Adds the CSS class or classes to the rightmost column containing field inputs in the Edit Note dialog box.                                           |
| Title                              | Overrides the HTML text in the header of the Edit Note dialog box.                                                                               |
| Primary Button Text                | Overrides the HTML that appears in the Primary (Update Note) button in the dialog box.                                                         |
| Dismiss Button SR Text             | Overrides the screen reader text associated with the dialog box's dismiss button.                                                                |
| Close Button Text                  | Overrides the HTML that appears in the Close (Cancel) button in the dialog box.                                                                |
| Size                               | Specifies the size of the Edit Note dialog box. The options are Default, Large, and Small. |
| CSS Class                          | Specifies a CSS class or classes that will be applied to the resulting dialog box.                                                                 |
| Title CSS Class                    | Specifies a CSS class or classes that will be applied to the resulting dialog's title bar.                                                     |
| Primary Button CSS Class           | Specifies a CSS class or classes that will be applied to the dialog box's Primary (Update Note) button.                                          |
| Close Button CSS Class             | Specifies a CSS class or classes that will be applied to the dialog box's Close (Cancel) button.                                                 |
|||

#### Delete dialog options

| Name                     | Description                                                                                                                                       |
|--------------------------|------------------------------|
| **Basic settings**       |                                                                                                                                                   |
| Confirmation             | Overrides the confirmation message to delete the note.                                                                                             |
| **Advanced settings**    |                                                                                                                                                   |
| Title                    | Overrides the HTML text in the header of the Delete Note dialog box.                                                                                  |
| Primary Button Text      | Overrides the HTML that appears in the Primary (Delete) button in the dialog box.                                                                   |
| Dismiss Button SR Text   | Overrides the screen reader text associated with the dialog box's dismiss button.                                                                     |
| Close Button Text        | Overrides the HTML that appears in the Close (Cancel) button in the dialog box.                                                                     |
| Size                     | Specifies the size of the Delete Note dialog box. The options are Default, Large, and Small.  |
| CSS Class                | Specifies a CSS class or classes that will be applied to the resulting dialog box.                                                                      |
| Title CSS Class          | Specifies a CSS class or classes that will be applied to the resulting dialog box's title bar.                                                          |
| Primary Button CSS Class | Specifies a CSS class or classes that will be applied to the dialog box's Primary (Delete) button.                                                    |
| Close Button CSS Class   | Specifies a CSS class or classes that will be applied to the dialog box's Close (Cancel) button.                                                      |
|||

### Assign table permissions

Notes, and the **Add**, **Edit**, and **Delete** buttons for the note control will be hidden on the basic or advanced form unless you create and assign the appropriate table permissions to the records as follows:

> [!IMPORTANT]
> A user must sign-in and be the creator of the note to edit or delete it using the portal. Users can't edit or delete a note created by others, even if you assign them table permissions.

1. Ensure the **Enable Table Permissions** checkbox is selected on the form for which you want notes to appear.

    ![Enable table permissions on a basic form.](media/configure-notes/enable-entity-permissions-form.png "Enable table permissions on a basic form")

1. For the table that has the notes control enabled, create a table permission with the required privileges. The scope should be appropriately set depending on the level of access required to end users.

    For example, create a table permission for a Lead table that shows notes on the basic form, with privileges including Read, Write, Create, Append, and Append To.

    ![Create new table permissions.](media/configure-notes/new-entity-permission.png "Create new table permissions")

1. [Associate the table permission with a web role](configure/assign-entity-permissions.md#add-table-permissions-to-a-web-role) for the user.

    For example, add the table permission created in the previous step to the Lead Manager web role.

    ![Add web roles to an table permission.](media/configure-notes/add-webrole-entity-permissions.png "Add web roles to an table permission")

1. Create a table permission for the **Annotation** table with the [Parental access type](configure/assign-entity-permissions.md#parental-access-type) and required privileges as explained in the table below. The **Parent Table Permission** must be set to the same table permissions created in step 2.

    | Note action | Required permissions |
    | - | - |
    | **Read** | Read |
    | **Add** | Create, Append (Append To required on Parent Table Permission) |
    | **Edit** | Write |
    | **Delete** | Delete |

    For example, create a table permission for the Annotation table, with the Leads table permission created in the previous steps set as the parent table.
    
    ![Add table permissions.](media/configure-notes/entity-permission.png "Add table permissions")

### Notes created with rich-text editor

You can view the notes created using the [rich-text editor in timeline](../model-driven-apps/set-up-timeline-control.md#enable-or-disable-rich-text-editor-for-notes-in-timeline) on your portal webpage. However, when you try to edit, you'll see the text in HTML markup format.

For example, this note shows rich-text format in the model-driven app.

![Dynamics 365 form.](media/configure-notes/dynamics-365-form.png)

The portal webpage shows the note in rich-text format.

![Portals form.](media/configure-notes/portals-form.png)

However, when editing the note from the portal webpage, you see the note in HTML markup format.

![Portals form in HTML when editing.](media/configure-notes/portals-form-edit.png)

> [!IMPORTANT]
> If you try to save a note with HTML markup using the portal, you'll receive this error: *We're sorry, but something went wrong. Please try again, and if this persists, contact the website administrator.* To save the notes with HTML markup using the portal, you'll have to disable the request validation. However, disabling request validation applies to the entire website. For the steps to disable the request validation, and to understand its impact, go to [request validation](configure/entity-forms.md#request-validation).

## Notes configuration for advanced forms

Advanced form notes are configured in the same way as [basic form notes](#notes-configuration-for-basic-forms). Create a metadata record for the Advanced Form Step that has notes first, and then add the notes configuration metadata.

## Enable file attachment on form

Enable **Attach File** option for the **Basic Form** to show the attachment option available with the notes.

To enable attachment on a basic form:

1. Open the [Portal Management](configure/configure-portal.md) app.

1. Select **Basic Forms** under **Content** on the left pane.

    ![Basic forms.](media/configure-notes/entity-forms.png)

1. From the list of forms, select to open a record of the form to which you want to add note configuration.

1. Select **Additional Settings** for the form. Configure the additional settings as per the fields explained in the section below.

    ![Additional settings - attach file.](media/configure-notes/additional-settings.png)

### Additional settings for file attachment

| Name | Description
| - | - 
| Attach File | Check the box to enable file attachments on the form.
| Attach File Save Option | Select **Notes** or **Portal Comments** to save file attachments. For notes attachments, select **Notes**.
| Allow Multiple Files | Check the box to allow multiple file attachments.
| Label | Specify a label for the attachment option.
| Attach File Storage Location | Select the location of the file attachment:<ul><li>Note attachment</li><li>Azure Blob Storage</li></ul>
| Accept MIME Types | Specify a list of accepted MIME types.
| Accept File Types | Specify a list of accepted file types. This option is only available when using the **Portal Comments** option for **Attach File Save Option**. 

### Attach a file option

After you configure the notes and enable notes attachments, you can see the **Attach File** option on the form.

![Attach file option.](media/configure-notes/attach-file-option.png)

