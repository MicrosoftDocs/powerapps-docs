<properties
	pageTitle="EditForm, NewForm, SubmitForm, and ResetForm functions | Microsoft PowerApps"
	description="Reference information, including syntax and examples, for the NewForm, SubmitForm, and ResetForm functions in PowerApps"
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="gregli-msft"
	manager="anneta"
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

# EditForm, NewForm, SubmitForm, and ResetForm functions in PowerApps #
Edit or create an item, save the contents, and reset the controls in an **[Edit Form](../controls/control-form-detail.md)** control.

## Description ##
These functions are often invoked from the **[OnSelect](../controls/properties-core.md)** formula of a **[Button](../controls/control-button.md)** or **[Image](../controls/control-image.md)** control so that the user can save edits, abandon edits, or create a record. You can [use controls and these functions together](../working-with-forms.md) to create a complete solution.

These functions return no values.

### SubmitForm ###
Use the **SubmitForm** function in the **[OnSelect](../controls/properties-core.md)** property of a Button control to save any changes in a Form control to the data source.

Before submitting any changes, this function checks for validation issues with any field that's marked as required or that has one or more constraints on its value. This behavior matches that of the **[Validate](function-validate.md)** function.

**SubmitForm** also checks the **[Valid](../controls/control-form-detail.md)** property of the Form, which is an aggregation of all the **[Valid](../controls/control-card.md)** properties of the **[Card](../controls/control-card.md)** controls that the Form control contains. If a problem occurs, the data isn't submitted, and the **[Error](../controls/control-form-detail.md)** and **[ErrorKind](../controls/control-form-detail.md)** properties of the Form control are set accordingly.

If validation passes, **SubmitForm** submits the change to the data source.

- If successful, the Form's **[OnSuccess](../controls/control-form-detail.md)** behavior runs, and the **[Error](../controls/control-form-detail.md)** and **[ErrorKind](../controls/control-form-detail.md)** properties are cleared.  If the form was in **FormMode.New** mode, it is returned to **FormMode.Edit** mode.
- If unsuccessful, the Form's **[OnFailure](../controls/control-form-detail.md)** behavior runs, and the **[Error](../controls/control-form-detail.md)** and **[ErrorKind](../controls/control-form-detail.md)** properties are set accordingly.  The mode of the form is unchanged.  

### EditForm ###
The **EditForm** function changes the Form control's mode to **FormMode.Edit**. In this mode, the contents of the Form control's **[Item](../controls/control-form-detail.md)** property are used to populate the form.  If the **SubmitForm** function runs when the form is in this mode, a record is changed, not created.  **FormMode.Edit** is the default for the Form control.

### NewForm ###
The **NewForm** function changes the Form control's mode to **FormMode.New**. In this mode, the contents of the Form control's **[Item](../controls/control-form-detail.md)** property are ignored, and the default values of the Form's **[DataSource](../controls/control-form-detail.md)** property populate the form. If the **SubmitForm** function runs when the form is in this mode, a record is created, not changed.

### ResetForm ###
The **ResetForm** function resets the contents of a form to their initial values, before the user made any changes. If the form is in **FormMode.New** mode, the form is reset to **FormMode.Edit** mode. The **[OnReset](../controls/control-form-detail.md)** behavior of the form control also runs.

## Syntax ##

**SubmitForm**( *FormName* )

- *FormName* - Required. Form control to submit to the data source.

**EditForm**( *FormName* )

- *FormName* - Required.  Form control to switch to **FormMode.Edit** mode.

**NewForm**( *FormName* )

- *FormName* - Required. Form control to switch to **FormMode.New** mode.

**ResetForm**( *FormName* )

- *FormName* - Required. Form control to reset to initial values. Also switches the form from **FormMode.New** mode to **FormMode.Edit** mode.

## Examples ##
See [Understand data forms](../working-with-forms.md) for complete examples.

1. Add a Button control, set its **[Text](../controls/properties-core.md)** property to show **Save**, and set its **[OnSelect](../controls/properties-core.md)** property to this formula:

	**SubmitForm( EditForm )**

1. Set the **[OnFailure](../controls/control-form-detail.md)** property of a Form control to blank and its **[OnSuccess](../controls/control-form-detail.md)** property to this formula:

	**Back()**

1. Name a **[Text box](../controls/control-text-box.md)** control **ErrorText**, and set its **[Text](../controls/properties-core.md)** property to this formula:

	**EditForm.Error**

	When the user selects the **Save** button, any changes in the Form control are submitted to the underlying data source.
	- If the submission succeeds, any changes are saved or, if the Form control is in **New** mode, a record is created. **ErrorText** is *blank* and the previous screen reappears.
	- If the submission fails, **ErrorText** shows a user-friendly error message, and the current screen remains visible so that the user can correct the problem and try again.

1. Add a Button control, set its **[Text](../controls/properties-core.md)** property to show **Cancel**, and set its **[OnSelect](../controls/properties-core.md)** property to this formula:

	**ResetForm( EditForm ); Back()**

	When the user selects the **Cancel** button, the values in the Form control are reset to what they were before the user started to edit it, the previous screen reappears, and the Form control is returned to **Edit** mode if it was in **New** mode.

1. Add a Button control, set its **[Text](../controls/properties-core.md)** property to show **New**, and set its **[OnSelect](../controls/properties-core.md)** property to this formula:

	**NewForm( EditForm ); Navigate( EditScreen, None )**

	When the user selects the **New** button, the Form control switches to **New** mode, the default values for the Form control's data source populate that control, and the screen that contains the Form control appears. When the **SubmitForm** function runs, a record is created instead of updated.
