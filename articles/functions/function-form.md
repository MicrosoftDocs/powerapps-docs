<properties
	pageTitle="PowerApps: NewForm, SubmitForm, and ResetForm functions"
	description="Reference information for the NewForm, SubmitForm, and ResetForm functions in PowerApps, including syntax and examples"
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="gregli-msft"
	manager="dwrede"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="11/07/2015"
   ms.author="gregli"/>

# NewForm, SubmitForm, and ResetForm functions in PowerApps #

Create a new item, saves the contents, and resets the controls of a Form control. 

## Description ##

These functions are used with the [**Edit form**](control-form-detail.md) control.  They are often invoked from the **OnSelect** formulas of **Button** or **Image** controls, giving users control over saving edits, abandoning edits, or creating new records.  See [Understand data forms](working-with-forms.md) for more details on how to use controls together to create a complete solution.

The **SubmitForm** function saves any changes in a Form control to the data source.  Use this function from a Button control's **OnSelect** property to "Save" or "Submit" the values in a form.  

### SubmitForm ##

**SubmitForm** will check for validation issues before submitting.  Fields that are marked as required or which have constraints on their value are checked, just as they are with the **Validate** function.  **SubmitForm** also checks the **Valid** property of the Form, which is an aggregation of all the **Valid** properties on the contained Cards.  If there is a problem, the submission will not be made, and the **Error** and **ErrorKind** properties of the Form control will be set accordingly.

After passing validation, **SubmitForm** will submit the data change to the data source.  If successful, the Form's **OnSuccess** behavior will be executed and the **Error** and **ErrorKind** properties will be cleared.  If unsuccessful, the Form's **OnFailure** behavior will be executed and the **Error** and **ErrorKind** properties will be set accordingly.  

### NewForm ###

The **NewForm** function places a Form control in **FormMode.New** mode.  In this mode, the contents of the Form control's **Item** property are ignored and the defaults of the Form's **DataSource** property are used to populate the form.  When **SubmitForm** is called, a new item will be created instead of changing an existing item.

### ResetForm ###

The **ResetForm** function resets the contents of a form to their initial values, before the user made any changes.  If the form is in **FormMode.New** mode, the form is reset to **FormMode.Edit** mode (unless there is nothing present on the **Item** property).  The **OnReset** behavior of the form control is also executed.

There are no return values from these functions.

## Syntax ##

**SubmitForm**( *Form Control* )

- *Form Control* - Required. Form control to submit to the data source.

**NewForm**( *Form Control* )

- *Form Control* - Required. Form control to place in **FormMode.New** mode.

**ResetForm**( *Form Control* )

- *Form Control* - Required. Form control to reset to initial values.  Also takes the form out of **FormMode.New** mode.

## Examples ##

See [Understand data forms](working-with-forms.md) for complete examples.

**SaveButton.OnSelect = SubmitForm( EditForm )**
**EditForm.OnSuccess = Back()**
**EditForm.OnFailure = *blank***
**ErrorLabel.Text = EditForm.Error**

- Saves any changes in **EditForm** to the underlying data source. If the form is in **New** mode, a new record is created.
- If the result is successful, **OnSuccess** will be executed and the user will be taken to the previous screen.  
- If the result is unsuccessful, **OnFailure** will be executed, which will do nothing as that formula is *blank*, and the user will remain on the current screen to correct the problem and try again.  
- If the result is successful, **ErrorLabel** will be *blank*.  If the result is unsuccessful, **ErrorLabel** will show a user friendly error message.

**CancelButton.OnSelect = ResetForm( EditForm ); Back()**

- Resets **EditForm** to the values of the record before it was edited by the user.  
- The **Back** function then returns to the previous screen.
- If the form was in **New** mode, it is returned to **Edit** mode.

**NewButton.OnSelect = NewForm( EditForm ); Navigate( EditScreen, None )**

- Places the **EditForm** into **New** mode.  The record on the **Item** property is ignored and the defaults for the form's data source are used to populate the controls of the form.  A subsequent call to **SubmitForm** will create a new record instead of editing an existing one.
- The **Navigate** function then takes the user to the screen hosting the **EditForm** control.  



