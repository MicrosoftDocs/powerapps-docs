<properties
    pageTitle="Display form and Edit form controls: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the Display form and Edit form controls"
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

# Edit form and Display form controls in PowerApps #
Display, edit, and create a record in a data source.

## Description ##
If you add a **Display form** control, the user can display all fields of a record or only the fields that you specify. If you add an **Edit form** control, the user can edit those fields, create a record, and save those changes to a data source.

![Example form and form view controls](media/control-form-detail/form-detail-intro.png)

If you add a **Gallery** control, you can configure it so that users can specify which record in a table to display or update. You can also add  one or more **Button** controls that the user can select to save edits, cancel edits, and create a record. By using controls together, you can [create a complete solution](working-with-forms.md).

### Record selection ###
For either type of form, you set its **DataSource** and **Item** properties to show a specific record in a data source.  

For example, you can set the **Item** property of a form to the **SelectedItem** property of a **Gallery** control. When the user selects a record in the gallery, the same record appears in the form, which is probably on a different screen. If the user returns to the gallery and selects a different record, the **SelectedItem** property of the gallery changes. This change updates the **Item** property of the form, which  then shows the newly selected item.

Each form control contains one or more [**Card**](control-card.md) controls. By setting the **DataField** property of a card, you [specify which field that card shows and other details](add-form.md).

### Create a record ###
When an **Edit Form** control is in **Edit** mode, the user can update values in each field of the record that the form's **Item** property determines. If inspected, the **Mode** property returns **Edit**.

When an **Edit form** control is in **New** mode, however, the **Item** property is ignored. The form doesn't show an existing record; instead, the values in each field match the default values of the data source with which you configured the form. The **NewForm** function causes a form to switch to this mode.

For example, you can set the **Text** property of a button to show **New** and its **OnSelect** property to a formula that includes the **NewForm** function. If the user selects that button, the form switches to **New** mode so that the user can create a record starting with known values.

A form switches back to **Edit** mode if either the **ResetForm** function runs or the **SubmitForm** function runs successfully.

- You can set the **Text** property of a button to show **Cancel** and its **OnSelect** property to a formula that includes the **ResetForm** function. If the user selects that button, any changes in progress are discarded, and the values in the form, once again, match the default values of the data source.
- You can set the **Text** property of a button to show **Save changes** and its **OnSelect** property to a formula that includes the **SubmitForm** function. If the user selects that button and the data source is updated, the values in the form are reset to the default values of the data source.

### Save changes ###
After the user has made changes to a record, use the **SubmitForm** function to save those changes to the data source.  The **Error**, **ErrorKind**, **OnSuccess**, and **OnFailure** properties provide feedback on the outcome.

When invoked, the **SubmitForm** function first performs validation checks on the user's changes.  If there is an issue, the **Error** and **ErrorKind** properties will be set, and the **OnFailure** formula will be executed.  You can pre-check for validation issues with the **Valid** property and may not want to enable a "Save" or "Submit" button for the user until it is valid.  Note that **Error** and **ErrorKind** are set until the next call to **SubmitForm** or **ResetForm**, even if the user clears the validation issue.

Next, **SubmitForm** sends the changes to the data source.  This can take some time depending on network latency.  If the submission is successful, the **Error** property will be cleared, the **ErrroKind** property will be set to **ErrorKind.None**, and the **OnSuccess** formula will be executed.  If the form was previously in **New** mode, it will be reset to **Edit** mode, now ready to edit the newly created record.

If the submission is unsuccessful, the **Error** property will contain a user friendly error message that is provided by the data source, explaining to the user what is wrong.  The **ErrorKind** property will be set appropriately, depending on the issue, and the **OnFailure** formula will be executed.

Some data sources can detect conflicting edits - when two people edit the same record at the same time.  In this case, **ErrorKind** will be set to **ErrorKind.Conflict**.  The remedy is to refresh the the data source with the other user's changes and reapply the change made by this user.

If you offer "Cancel" button on your form, to abandon the user's changes, have the **OnSubmit** formula for the button call the **ResetForm** function even if you are changing screens.  Without a reset, the form will retain the user's changes.

## Key properties ##

**DataSource** The data source where the record to be view, edited, or created is stored.

- If left blank, the record cannot be edited and there is no additional meta-data or validation provided.

**Item** The record in the **DataSource** that is to be viewed or edited.

- For the **Form** control, if this property is blank, the form will automatically be in **New** mode.  If bound to a **Gallery** control's **SelectedItem** property, blank is returned if their is no selection or the the gallery is empty (no records).

**Error** A user friendly error message to display if there is an issue when **SubmitForm** is invoked.

- Only applies to the **Form** control.
- This property changes only as a result of calling the **SubmitForm**, **EditForm**, or **ResetForm** functions.
- This property will be *blank* if there is no error.  **ErrorKind** will also be set to **ErrorKind.None**.
- The error message returned will be in the user's language when possible.  Some error messages come from the data source directly and may not be in the user's language.

## All properties ##

**BorderColr** The color of a control's border.

**BorderStyle** Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**BorderThickness** The thickness of a control's border.

**DataSource** The data source where the record to be view, edited, or created is stored.  See details under [key properties](#key-properties).

**ErrorKind** The kind of error encountered if there is an issue when **SubmitForm** is invoked.  

- Only applies to the **Edit form** control.
- The **ErrorKind** enum is shared with the **Errors** function.  The following values can be returned by the **Edit form** control:

| ErrorKind | Description |
|------------|-------------|
| ErrorKind.Conflict | Another change was made to the same record, resulting in a change conflict.  Use **[Refresh](function-refresh.md)** to reload the record and try the change again. |
| ErrorKind.None | The error is of an unknown kind. |
| ErrorKind.Sync | An error was reported by the data source.  Check the **Error** property for more information. |
| ErrorKind.Validation | There was a general validation issue detected. |

**Item** The record in the **DataSource** that is to be viewed or edited.  See details under [key properties](#key-properties).

**Error** A user friendly error message to display if there is an issue when **SubmitForm** is invoked.  See details under [key properties](#key-properties).

**Fill** The background color of a control.

**Height** The distance between a control's top and bottom edges.

**LastSubmit** The last successfully submitted record, including any server generated fields.

- If the data source automatically generates or calculates any fields, such an "ID" field with a unique number, the **LastSubmit** property will have this new value after **SubmitForm** has been successfully executed.
- The value of this property is available in the **OnSUccess** formula.

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

**OnFailure** How an app responds when a data operation has been unsuccessful.

**OnSucess** How an app responds when a data operation has been successful.

**OnReset** How an app responds when an **Edit form** control is reset.

**Valid** Whether a **Card** or **Form** control contains valid entries, ready to be submitted to the data source.

- The **Form** control's valid property is the aggregation of all the **Card** controls that it contains.  If all cards are reporting *true* through their **Valid** properties, then the form's **Valid** property is *true*; if any one card is reporting *false*, then this the form's **Valid** property is *false*.
- To provide a submit button that is only enabled when the form has not been submitted yet or is valid, use **SubmitButton.Enabled = IsBlank( Form.Error ) || Form.Valid**.

**Unsaved**  True if the **Edit form** control contains user changes that have not been saved.

- Use this property to warn the user before they lose any unsaved changes.  You can also block a selection from changing in a **Gallery** control by setting **Gallery.Disabled = Form.Unsaved** and likewise disable refresh operations.

**Width** The distance between a control's left and right edges.

**Visible** Whether a control appears or is hidden.

**X** The distance between the left edge of a control and the left edge of the screen.

**Y** The distance between the top edge of a control and the top edge of the screen.
