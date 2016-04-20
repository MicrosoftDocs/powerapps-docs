<properties
    pageTitle="Form and View form controls: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the Form and View form controls"
    services=""
    suite="powerapps"
    documentationCenter="na"
    authors="gregli-msft"
    manager="erikre"
    editor=""
    tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="02/29/2016"
   ms.author="gregli"/>

# Form and View form controls in PowerApps #

Displays, edits, and creates a record in a data source.

## Description ##

The **Form** control is used to edit the fields of a record and save changes to a data source.  It is also used to create new records.  The **View form** control is similar but read-only, used to display the details of a record but not change them.

### Record selection ###

Both controls are bound to a record of a data source through their **DataSource** and **Item** properties.  

Often the **Item** property is set to the **SelectedItem** property of a **Gallery** control where the user can select which record to display and/or edit.  As the **Item** property changes, as the user changes the record that is selected, the form controls respond accordingly.

These controls are a container for **Card** controls.  Each card inside the form can be bound to a field of the record through its **DataField** property.  

### Creating new records ###

Normally, the **Form** control is in **Edit** mode, displaying and enabling the edit of an existing record provided by the **Item** property.  If inspected, the **Mode** property returns **Edit**.

The **Form** control can also be used to create new records.  Call the **NewForm** function to place the control into **New** mode, where the record displayed and edited contains the default values for the data source instead of an existing record.  In this case the **Item** property is ignored.  Calling **ResetForm** or successfully calling **SubmitForm** will cause the form to return to **Edit** mode. 

### Saving changes ###

After the user has made changes to a record, use the **SubmitForm** function to save those changes to the data source.  The **Error**, **ErrorKind**, **OnSuccess**, and **OnFailure** properties provide feedback on the outcome.

When invoked, the **SubmitForm** function first performs validation checks on the user's changes.  If there is an issue, the **Error** and **ErrorKind** properties will be set, and the **OnFailure** formula will be executed.  You can pre-check for validation issues with the **Valid** property and may not want to enable a "Save" or "Submit" button for the user until it is valid.  Note that **Error** and **ErrorKind** are set until the next call to **SubmitForm** or **ResetForm**, even if the user clears the validation issue.

Next, **SubmitForm** sends the changes to the data source.  This can take some time depending on network latency.  If the submission is successful, the **Error** property will be cleared, the **ErrroKind** property will be set to **ErrorKind.None**, and the **OnSuccess** formula will be executed.  If the form was previously in **New** mode, it will be reset to **Edit** mode, now ready to edit the newly created record.

If the submission is unsuccessful, the **Error** property will contain a user friendly error message that is provided by the data source, explaining to the user what is wrong.  The **ErrorKind** property will be set appropriately, depending on the issue, and the **OnFailure** formula will be executed.

Some data sources can detect conflicting edits - when two people edit the same record at the same time.  In this case, **ErrorKind** will be set to **ErrorKind.Conflict**.  The remedy is to refresh the the data source with the other user's changes and reapply the change made by this user.

If you offer "Cancel" button on your form, to abandon the user's changes, have the **OnSubmit** formula for the button call the **ResetForm** function even if you are changing screens.  Without a reset, the form will retain the user's changes.

## Key properties ##

**DataSource** The data source where the record to be view, edited, or created is stored.

- If left blank, the record cannot be edited and there is no additional metadata or validation provided.

**Item** The record in the **DataSource** that is to be viewed or edited.

- For the **Form** control, if this property is blank, the form will automatically be in **New** mode.  If bound to a **Gallery** control's **SelectedItem** property, blank is returned if their is no selection or the the gallery is empty (no records). 

**Error** A user friendly error message to display for this form when the **SubmitForm** function fails.

- Only applies to the **Form** control.
- This property changes only as a result of calling the **SubmitForm**, **EditForm**, or **ResetForm** functions. 
- This property will be *blank* if there is no error.  **ErrorKind** will also be set to **ErrorKind.None**.
- The error message returned will be in the user's language when possible.  Some error messages come from the data source directly and may not be in the user's language. 

**ErrorKind** The kind of error encountered when **SubmitForm** fails.

- Only applies to the **Form** control.
- The **ErrorKind** enum is shared with the **Errors** function.  The following values can be returned by the **Form** control:

| ErrorKind | Description |
|------------|-------------|
| ErrorKind.Conflict | Another change was made to the same record, resulting in a change conflict.  Use **[Refresh](function-refresh.md)** to reload the record and try the change again. |
| ErrorKind.None | The error is of an unknown kind. |
| ErrorKind.Sync | An error was reported by the data source.  Check the **Error** property for more information. |
| ErrorKind.Validation | There was a general validation issue detected. |

## All properties ##

**BorderColr**

**BorderStyle**

**BorderThickness**

**DataSource**

**Item**

**Error**

**ErrorKind**

**Fill**

**Height**

**LastSubmit** 

**Mode** The control is in either **Edit** or **New** mode.

| Mode | Description |
|----------|-------------|
| **FormMode.Edit** | Form is editng an existing record.  The values in the form's cards are pre-populated with the existing record, for the user to change.  Calling the **SubmitForm** function will cause an existing record to be modified. |
| **FormMode.New** | Form is editing a new record.  The values in the form's controls were pre-popoulated with the defaults for a record of the DataSource.  Calling **SubmitForm** function will cause a new record to be created. | 

- By default, the form control is in **Edit** mode.  To place it in **New** mode, call the **NewForm** function.  The form is automatically in **New** mode if the **Item** is blank (there is no item to edit).

The form exits **New** mode when one of the following occurs: 
* The form is successfully submitted and the new record has been created.  If the gallery is set to automatically move selection to this new record, then the form will be in edit mode for the created record for any subsequent changes.
* The **Item** record changes.  Indicating that the user would like to edit a different record instead of creating a new one.
* The **ResetForm** function is called.

**OnFailure**

**OnSucess**

**OnReset**

**Valid**

- The **Form** control's valid property is the aggregation of all the **Card** controls that it contains.  If all cards are reporting *true* through their **Valid** properties, then the form's **Valid** property is *true*; if any one card is reporting *false*, then this the form's **Valid** property is *false*.
- To provide a submit button that is only enabled when the form has not been submitted yet or is valid, use **SubmitButton.Enabled = IsBlank( Form.Error ) || Form.Valid**.

**Unsaved**  

- Use this property to warn the user before they lose any unsaved changes.  You can also block a selection from changing in a **Gallery** control by setting **Gallery.Disabled = Form.Unsaved** and likewise disable refresh operations.

**Width**

**Visible**

**X**

**Y**




	





