---
title: "Configure notes as attachments on entity forms and web forms for a portal | MicrosoftDocs"
description: "Instructions to add and configure notes as attachments on entity forms and web forms in a portal."
author: gitanjalisingh33msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 06/25/2020
ms.author: gisingh
ms.reviewer: tapanm
---

# Configure notes as attachments for entity forms and web forms on portals

Similar to subgrids, adding notes to your managed forms on the portal is easy&mdash;just add the notes control to the model-drive app forms through the [form designer](../model-driven-apps/create-design-forms.md) and you're done. You can configure the behavior of the notes control by using metadata.

> [!NOTE]
> Explicit [Entity Permissions](configure/assign-entity-permissions.md) are required for any notes to appear on the portal. For read and edit, the Read and Write privileges must be granted. For create, two permissions must exist: a permission with the Create and Append privileges must be granted for the note (annotation) entity, the second permission must be assigned to the entity type the note is being attached to with the Append To privilege granted. The **Enable Entity Permissions** check box must be selected on the corresponding entity form or web form step for the entity permissions to take effect.

## Notes configuration for Entity Forms

1. Open the [Portal Management](https://docs.microsoft.com/powerapps/maker/portals/configure/configure-portal) app.

1. Select **Entity Forms** under **Content** from left pane:

    ![Entity forms](media/configure-notes/entity-forms.png)

1. From the list of forms, select to open a record of the form to which you want to add note configuration.

1. From the available tabs in form settings, select **Entity Form Metadata**:

    ![Entity form metadata](media/configure-notes/entity-form-metadata.png)

1. Select **New Entity Form Metadata**:

    ![New entity form metadata](media/configure-notes/new-entity-form-metadata.png)

1. Select **Type** as **Note**:

    ![Type as Note](media/configure-notes/type-notes.png)

1. The notes configuration settings are displayed. Most of the settings are collapsed by default. You can expand a section to see additional settings:

    ![Notes options](media/configure-notes/notes-options.png)

1. Fill in the fields by entering appropriate values. [!include[](../../includes/proc-more-information.md)] [Attributes](#attributes), [Create dialog options](#create-dialog-options), [Edit dialog options](#edit-dialog-options), and [Delete dialog options](#delete-dialog-options)

1. Save the form.

After adding the configuration, the Note control will be rendered by using the appropriate options enabled on the portal.

## Attributes


| Name                  | Description                                                                                                                                                  |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Basic settings**    |                                                                                                                                                              |
| Create Enabled        | Enables the ability to add new notes to the entity.                                                                                                          |
| Create Dialog Options | Contains settings for configuring the dialog box when **Create Enabled** is true. See Create Dialog Options for more details.                                    |
| Edit Enabled          | Enables the ability to edit existing notes on the entity.                                                                                                    |
| Edit Dialog Options   | Contains settings for configuring the dialog box when **EditEnabled** is true. See Edit Dialog Options for more details.                                         |
| Delete Enabled        | Enables the ability to delete notes from the entity.                                                                                                         |
| Delete Dialog Options | Contains settings for configuring the dialog box when **DeleteEnabled** is true. See Delete Dialog Options for more details.                                     |
|File Attachment Location | Select the location of the file attachment:<ul><li>Note attachment</li><li>Azure Blob Storage</li></ul>|
|Accept MIME Type(s) | Allows you to specify a list of accepted MIME types. |
|Restrict MIME Types | Select whether to allow or restrict MIME types.|
|Maximum File Size (in KB) |Allows you to specify the maximum size of a file that can be attached. |
| **Advanced settings** |                                                                                                                                                              |
| List Title            | Overrides the title over the Notes area.                                                                                                                     |
| Add Note Button Label | Overrides the label on the Add Notes button.                                                                                                                 |
| Note Privacy Label    | Overrides the label denoting that a note is Private.                                                                                                         |
| Loading Message       | Overrides the message shown while the list of notes is loading.                                                                                              |
| Error Message         | Overrides the message shown when an error occurs while trying to load the list of notes.                                                                     |
| Access Denied Message | Overrides the message shown when the user doesn't have sufficient permissions to view the list of notes.                                                    |
| Empty Message         | Overrides the message shown when the current entity does not have any notes that can be viewed.                                                              |
| List Orders           | Allows you to set the order in which notes will be displayed. The List Orders setting allows you to set the following: <ul><li>Attribute: the logical name of the column by which you wish to sort</li><li>Alias: the alias for the attribute in the query</li><li>Direction: Ascending (smallest to largest, or first to last), or Descending (largest to smallest, or last to first).</li></ul>  ![Set attributes for list orders](media/set-attributes-list-orders.png "Set attributes for list orders") <br>  To add a sorting rule, select "Column" (4) and fill in the details. List Orders will be processed in order from the top of the list having highest priority.|
||

## Create Dialog Options

| Name                               | Description                                                                                                                                 |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Basic settings**                 |                                                                                                                                             |
| Display Privacy Options Field      | Enables a check box in the Add Note dialog box that allows the user to mark a note as Private.                                                   |
| Privacy Option Field Default Value | Specifies the default value for the Display Privacy Options Field check box. The default value of this field is False.                     |
| Display Attach File                | Enables a file upload field in the Add Note dialog box, allowing a user to attach a file to a note.                                             |
| Attach File Accept                 | The MIME type accepted by the file upload input.                                                                                            |
| **Advanced settings**              |                                                                                                                                             |
| Note Field Label                   | Overrides the label for the Note field in the Add Note dialog box.                                                                              |
| Note Field Columns                 | Sets the columns value in the Note &lt;textarea&gt;                                                                                            |
| Note Field Rows                    | Sets the rows value in the Note &lt;textarea&gt;                                                                                            |
| Privacy Option Field Label         | Overrides the label for the Privacy Option field (if enabled).                                                                              |
| Attach File Label                  | Overrides the label for the Attach File field (if enabled)                                                                                  |
| Left Column CSS Class              | Adds the CSS class or classes to the leftmost column containing labels in the Add Note dialog box.                                                  |
| Right Column CSS Class             | Adds the CSS class or classes to the rightmost column containing field inputs in the Add Note dialog box.                                           |
| Title                              | Overrides the HTML text in the header of the Add Note dialog box.                                                                               |
| Primary Button Text                | Overrides the HTML that appears in the Primary (Add Note) button in the dialog box.                                                           |
| Dismiss Button SR Text             | Overrides the screen reader text associated with the dialog box's dismiss button.                                                               |
| Close Button Text                  | Overrides the HTML that appears in the Close (Cancel) button in the dialog box.                                                               |
| Size                               | Specifies the size of the Add Note dialog box. The options are Default, Large, and Small. For the Add Note dialog box, the default size is Default. |
| CSS Class                          | Specify a CSS class or classes that will be applied to the resulting dialog box.                                                                |
| Title CSS Class                    | Specify a CSS class or classes that will be applied to the resulting dialog box's title bar.                                                    |
| Primary Button CSS Class           | Specify a CSS class or classes that will be applied to the dialog box's Primary (Add Note) button.                                            |
| Close Button CSS Class             | Specify a CSS class or classes that will be applied to the dialog box's Close (Cancel) button.                                                |
|||

## Edit Dialog Options

| Name                               | Description                                                                                                                                   |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| **Basic settings**                 |                                                                                                                                               |
| Display Privacy Options Field      | Enables a check box in the Edit Note dialog box that allows the user to mark a note as Private.  |
| Privacy Option Field Default Value | Specifies the default value for the Display Privacy Options Field check box. The default value of this field is False.   |
| Display Attach File                | Enables a file upload field in the Edit Note dialog box, allowing a user to attach a file to a note.                      |
| Attach File Accept                 | The MIME type accepted by the file upload input. |
| **Advanced settings**              |                                                                                              |
| Note Field Label                   | Overrides the label for the Note field in the Edit Note dialog box.|
| Note Field Columns                 | Sets the columns value in the Note &lt;textarea&gt;                                                                                             |
| Note Field Rows                    | Sets the rows value in the Note &lt;textarea&gt;                                                                                             |
| Privacy Option Field Label         | Overrides the label for the Privacy Option field (if enabled).                                                                                
| Attach File Label                  | Overrides the label for the Attach File field (if enabled)                                                                                   |
| Left Column CSS Class              | Adds the CSS class or classes to the leftmost column containing labels in the Edit Note dialog box.                                                  |
| Right Column CSS Class             | Adds the CSS class or classes to the rightmost column containing field inputs in the Edit Note dialog box.                                           |
| Title                              | Overrides the HTML text in the header of the Edit Note dialog box.                                                                               |
| Primary Button Text                | Overrides the HTML that appears in the Primary (Update Note) button in the dialog box.                                                         |
| Dismiss Button SR Text             | Overrides the screen reader text associated with the dialog box's dismiss button.                                                                |
| Close Button Text                  | Overrides the HTML that appears in the Close (Cancel) button on the dialog box.                                                                |
| Size                               | Specifies the size of the Edit Note dialog box. The options are Default, Large, and Small. For the Edit Note dialog box, the default size is Default.|
| CSS Class                          | Specify a CSS class or classes that will be applied to the resulting dialog box.                                                                 |
| Title CSS Class                    | Specify a CSS class or classes that will be applied to the resulting dialog's title bar.                                                     |
| Primary Button CSS Class           | Specify a CSS class or classes that will be applied to the dialog box's Primary (Update Note) button.                                          |
| Close Button CSS Class             | Specify a CSS class or classes that will be applied to the dialog box's Close (Cancel) button.                                                 |
|||

## Delete Dialog Options

| Name                     | Description                                                                                                                                       |
|--------------------------|------------------------------|
| **Basic settings**       |                                                                                                                                                   |
| Confirmation             | Override the confirmation message to delete the note.                                                                                             |
| **Advanced settings**    |                                                                                                                                                   |
| Title                    | Overrides the HTML text in the header of the Delete Note dialog box.                                                                                  |
| Primary Button Text      | Overrides the HTML that appears in the Primary (Delete) button in the dialog box.                                                                   |
| Dismiss Button SR Text   | Overrides the screen reader text associated with the dialog box's dismiss button.                                                                     |
| Close Button Text        | Overrides the HTML that appears in the Close (Cancel) button in the dialog box.                                                                     |
| Size                     | Specifies the size of the Delete Note dialog box. The options are Default, Large, and Small. For the Delete Note dialog box, the default size is Default. |
| CSS Class                | Specify a CSS class or classes that will be applied to the resulting dialog box.                                                                      |
| Title CSS Class          | Specify a CSS class or classes that will be applied to the resulting dialog box's title bar.                                                          |
| Primary Button CSS Class | Specify a CSS class or classes that will be applied to the dialog box's Primary (Delete) button.                                                    |
| Close Button CSS Class   | Specify a CSS class or classes that will be applied to the dialog box's Close (Cancel) button.                                                      |
|||

### Assign entity permissions

You must create and assign the appropriate entity permission to the records as follows, otherwise the **Add**, **Edit**, and **Delete** buttons for the note will be hidden:

- Read, Write, Create, Append, and Append To privileges for the **Annotation** entity with the scope as **Global**. This entity permission must be associated with a web role for the user.
- Read, Write, Create, Append, and Append To privileges for the entity that has the Notes control enabled in it. For example, Account, Contact or Lead entities that show notes on their entity forms. The scope should be set to **Global**. This entity permission must be associated with a web role for the user.

    ![Add entity permissions](media/configure-notes/entity-permission.png "Add entity permissions")

    ![Add web roles to an entity permission](media/entity-permission-web-roles.png "Add web roles to an entity permission")

> [!IMPORTANT]
> A user must sign-in and must be the creator of the note to edit or delete it using the portal. Users can't edit or delete a note created by others, even if you assign them entity permissions.

If you created a custom form and added the notes section to it, be sure to select **Notes** as the default tab you want to be visible.

![Notes in a custom form](media/notes-activities-tab.png "Notes in a custom form")

### Enable file attachment on form

You must enable **Attach File** option for the **Entity Form** to show the attachment option available with the notes. 

To enable attachment on an entity form:

1. Open the [Portal Management](https://docs.microsoft.com/powerapps/maker/portals/configure/configure-portal) app.

1. Select **Entity Forms** under **Content** from left pane:

    ![Entity forms](media/configure-notes/entity-forms.png)

1. From the list of forms, select to open a record of the form to which you want to add note configuration.

1. Select **Additional Settings** for the form. You need to configure the additional settings as per fields explained in the [attachment options](#additional-settings-for-file-attachment):

    ![Additional settings - attach file](media/configure-notes/additional-settings.png)

#### Additional settings for file attachment

| Name | Description
| - | - 
| Attach File | Check the box to enable file attachments on the form.
| Attach File Save Option | Select **Notes** or **Portal Comments** to save file attachments. For notes attachments, select **Notes**.
| Allow Multiple Files | Check the box to allow multiple file attachments.
| Label | Label for the attachment option.
| Attach File Storage Location | Select the location of the file attachment:<ul><li>Note attachment</li><li>Azure Blob Storage</li></ul>
| Accept MIME Types | Allows you to specify a list of accepted MIME types.
| Accept File Types | Only available when using **Portal Comment** option for **Attach File Save Option**. Allows you to specify a list of accepted file types.

### Attach File Option

After you configure the notes and enable notes attachments, you can see the **Attach File** option on the form:

![Attach file option](media/configure-notes/attach-file-option.png)

### Notes created with rich-text editor

You can view the notes created using the [rich-text editor in timeline](https://docs.microsoft.com/powerapps/maker/model-driven-apps/set-up-timeline-control#enable-or-disable-rich-text-editor-for-notes-in-timeline) on your portal web page. However, when you try to edit, you'll see the text in HTML markup format.

For example, the note shows rich-text format in the model-driven app.

![Dynamics 365 form](media/configure-notes/dynamics-365-form.png)

Portal web page shows the note in rich-text format.

![Portals form](media/configure-notes/portals-form.png)

However, when editing the note from portal web page, you'll see the note in HTML markup format.

![Portals form in HTML when editing](media/configure-notes/portals-form-edit.png)

> [!IMPORTANT]
> If you try to save a note with HTML markup using the portal, you'll see this error: *We're sorry, but something went wrong. Please try again, and if this persists, contact the website administrator.* To save the notes with HTML markup using the portal, you'll have to disable the request validation. However, disabling request validation applies to the entire web site. For the steps to disable the request validation, and to understand its impact, go to [request validation](configure/entity-forms.md#request-validation).

## Notes configuration for web forms

Web form notes are configured in the same way as [entity form notes](#notes-configuration-for-entity-forms). You must create a metadata record for the Web Form Step that has notes first, and then add the notes configuration metadata.

> [!NOTE]
> Notes description must be prefixed with **\*WEB\*** (*'WEB' keyword with an asterisk sign (\*) before and after*) in order to display on the portal.
