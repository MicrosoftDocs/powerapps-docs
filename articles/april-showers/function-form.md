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

### NewForm ###

**NewForm**( *Form Control* )

- *Form Control* - Required. Form control to submit.

	Places the Form into **New** mode.  Instead of editing an exisitng record, the form's input controls take their values from Defaults( Form.DataSource ) for creation of a new record.

### SubmitForm ###

**SubmitForm**( *Form Control* )

- *Form Control* - Required. Form control to submit.

	Submits the form.  Use this function in the **OnSubmit** property of a "Submit" button control.

	If the **Valid** property of the form is false, an appropriate validation error message will be placed in the **Error** proprety and no server communication will occur.  

### ResetForm ###

**ResetForm**( *Form Control* )

- *Form Control* - Required. Form control to reset.

	Clears any user changes and resets the form to when the **Item** was first loaded.  Use this function in the **OnSubmit** property of a "Reset" or "Cancel" button control.

	Calling this function will exit **New** mode.  If you wish to remain in new mode, set **Form.OnReset = NewForm( Form )**.