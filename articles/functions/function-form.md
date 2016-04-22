<properties
	pageTitle="NewForm, SubmitForm, and ResetForm functions | Microsoft PowerApps"
	description="Reference information, including syntax and examples, for the NewForm, SubmitForm, and ResetForm functions in PowerApps"
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
   ms.date="04/21/2016"
   ms.author="gregli"/>

# NewForm, SubmitForm, and ResetForm functions in PowerApps #
Create an item, save the contents, and reset the controls in an [**Edit Form**](control-form-detail.md) control.

## Description ##
These functions are often invoked from the **OnSelect** formula of a [**Button**](control-button.md) or [**Image**](control-image.md) control so that the user can save edits, abandon edits, or create a record. You can also [use controls together](working-with-forms.md) to create a complete solution.

These functions return no values.

### SubmitForm ###
Use the **SubmitForm** function in the **OnSelect** property of a Button control to save any changes in a Form control to the data source. This function checks for validation issues before submitting the changes. Each fields that's marked as required or that has one or more constraints on its value is checked, just as it is with the **Validate** function.

**SubmitForm** also checks the **Valid** property of the Form, which is an aggregation of all the **Valid** properties of the  [**Card**](control-card.md) controls that the Form control contains. If a problem occurs, the data isn't submitted, and the **Error** and **ErrorKind** properties of the Form control are set accordingly.

If validation passes, **SubmitForm** submits the change to the data source. If successful, the Form's **OnSuccess** behavior runs, and the **Error** and **ErrorKind** properties are cleared. If unsuccessful, the Form's **OnFailure** behavior runs, and the **Error** and **ErrorKind** properties are set accordingly.  

### NewForm ###
The **NewForm** function changes the Form control's mode to **FormMode.New**. In this mode, the contents of the Form control's **Item** property are ignored, and the default values of the Form's **DataSource** property populate the form. When **SubmitForm** is called, an item is created instead of changed.

### ResetForm ###
The **ResetForm** function resets the contents of a form to their initial values, before the user made any changes. If the form is in **FormMode.New** mode, the form is reset to **FormMode.Edit** mode (unless nothing is present on the **Item** property). The **OnReset** behavior of the form control also runs.

## Syntax ##

**SubmitForm**( *FormName* )

- *FormName* - Required. Form control to submit to the data source.

**NewForm**( *FormName* )

- *FormName* - Required. Form control to switch to **FormMode.New** mode.

**ResetForm**( *FormName* )

- *FormName* - Required. Form control to reset to initial values. Also takes the form out of **FormMode.New** mode.

## Examples ##
See [Understand data forms](working-with-forms.md) for complete examples.

1. Add a Button control, set its **Text** property to show **Save**, and set its **OnSelect** property to this formula:

	**SubmitForm( EditForm )**

1. Set the **OnFailure** property of a Form control to blank and its **OnSuccess** property to this formula:
 	**Back()**

1. Name a [**Text box**](control-text-box.md) control **ErrorText**, and set its **Text** property to this formula:

	**EditForm.Error**

	When the user selects the **Save** button, any changes in the Form control are submitted to the underlying data source.
	- If the submission succeeds, any changes are saved or, if the Form control is in **New** mode, a record is created. **ErrorText** is *blank* and the previous screen reappears.
	- If the submission fails, **ErrorText** shows a user-friendly error message, and the current screen remains visible so that the user can correct the problem and try again.

1. Add a Button control, set its **Text** property to show **Cancel**, and set its **OnSelect** property to this formula:

	**ResetForm( EditForm ); Back()**

	When the user selects the **Cancel** button, the values in the Form control are reset to what they were before the user started to edit it, the previous screen reappears, and the Form control is returned to **Edit** mode if it was in **New** mode.

1. Add a Button control, set its **Text** property to show **New**, and set its **OnSelect** property to this formula:

	**NewForm( EditForm ); Navigate( EditScreen, None )**

	When the user selects the **New** button, the Form control switches to **New** mode, the default values for the Form control's data source populate that control, and the screen that contains the Form control appears. When the **SubmitForm** function runs, a record is created instead of updated.
