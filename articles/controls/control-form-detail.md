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

Displays, edits, and creates records in a data source.

## Description ##

The **Form** control is bound to a record of a data source through its **DataSource** and **Item** properties.    

The **Form** control is a container control for cards, and only cards.  Each card inside the form can be bound to a field of the record through its **DataField** property.  When bound:

* The value of the card's **Update** property for the card will be used to make changes to the data source when the **SubmitForm** is called.
* The value of the card's **Valid** property is aggregated with the other cards to determine the value of the form's **Valid** property.  

* If invalid, the **ValidError** property provided by the card is the string provided in the **Error** and **FieldErrors** propertie, and the **ErrorType** property indicates a validation issue.
* Controls within the card are reset and user input lost when the form's **Item** property changes or the **ResetForm** function is called.

Cards can also be unbound within the **Form** control (**DataField** property is blank).  **Valid** and **Update** values are ignored for unbound cards.

The **View form** control is the same as the **Form** control, but only has **DataSource** and **Item** properties in addition to the standard positioning, sizing, and formatting properties.  **SubmitForm** and **ResetForm** functions do not work with the **View form** forms.

Related functions: **NewForm**, **SubmitForm**, **ResetForm**, **Refresh**.

## Standard Properties ##

**Data**

* **DataSource**

	* Type: Data Source
	* Changeable: Yes
	* Readable: No
	* View form Control: Yes

	The data source to work with.  

	If left blank, the record cannot be edited and there is no additional metadata or validation provided.

* **Unsaved**

	* Type: Boolean
	* Changeable: No
	* Readable: Yes
	* View form Control: No

	True if the form contains user changes from the original **Item** that have not been saved to the underlying data source.  Use this property to warn the user before losing unsaved changes or to block a bound gallery from changing selection (Gallery.Enabled = !Form.Unsaved) or disable refresh operations.

* **Error**

	* Type: String
	* Changeable: No
	* Readable: Yes
	* View form Control: No

	Provides an error message for the user.  Usually this error message comes from the data source when the **SubmitForm** function is called.

	This property changes only as a result of calling the **SubmitForm**, **EditForm**, or **ResetForm** functions. 

	If there is a validation problem (**Form.Valid** is **False**) then this property will display a message that there is a validation problem.  As with other changes to this property, this will only be displayed or cleared when one of the Form functions is called.

	Error will be in the language of the user whenever possible.  If the error comes from the data source, it may not be in this language.

	This property will be blank if **ErrorKind = ErrorKind.None**.

* **ErrorKind**

	* Type: ErrorKind Enum
	* Changeable: No
	* Readable: Yes
	* View form Control: No

	Provides the type of error.

	As with the **Error** property, the **ErrorKind** property changes only as a result of calling the **SubmitForm**, **EditForm**, or **ResetForm** functions. 

	The **ErrorKind** enum is the same enumeration used by the **Errors** function.  The values of **ErrorKind** that may be returned in this context are:

	| ErrorKind Enum | Description |
	|----------|-------------|
	| ErrorKind.None | There is no error. |
	| ErrorKind.Record | There is a general problem with the record.  Check the **Error** string for more information. |
	| ErrorKind.ConstraintValidation | There is a validation problem with one or more of the fields.  This includes a required field not being present. |
	| ErrorKind.Conflict | There are conflicting changes to the record.  The user must reload the record and reapply their change. You can use this value to offer the user a "Reload" button to help them resolve the conflict. |

	Specifics of the problem are included in the **Error** property.  

* **Item**

	* Type: Record
	* Changeable: Yes
	* Readable: Yes
	* View form Control: Yes

	The item to display and/or edit.  **Item** typically comes from the gllery **Selected** property, where the gallery is used to select the record to edit.

	After an item has been successfully submitted, if the data source provides any information automatically such as an automatically generated primary key, that information will be available in the **Item**.

* **Mode**

	* Type: Enum FormMode
	* Changeable: No
	* Readable: Yes
	* View form Control: No

	Provides the mode of the Form control.

	| FormMode Enum | Description |
	|----------|-------------|
	| Edit | Form is editng an existing record.  The values in the form's controls were pre-populated with the existing record, for the user to change.  Calling SubmitForm() will cause an existing record to be modified. |
	| New | Form is editing a new record.  The values in the form's controls were pre-popoulated with the defaults for a record of the DataSource.  Calling SubmitForm() will cause a new record to be created. | 

	By default, the form control is in **Edit** mode.  To place it in **New** mode, call the **NewForm** function.  The form is automatically in **New** mode if the **Item** is blank (there is no item to edit).

	The form exits **New** mode when one of the following occurs: 

	* The form is successfully submitted and the new record has been created.  If the gallery is set to automatically move selection to this new record, then the form will be in edit mode for the created record for any subsequent changes.
	* The **Item** record changes.  Indicating that the user would like to edit a different record instead of creating a new one.
	* The **ResetForm** function is called.
<p>

* **Valid**

	* Type: Boolean
	* Changeable: No
	* Readable: Yes
	* View form Control: No

	Indicates if it is OK to submit a form.  It is a logical AND of all the Valid properties of cards within the Form control.  

	To provide a submit button that is only enabled when the form has not been submitted yet or is valid, use **SubmitButton.Enabled = IsBlank( Form.Error ) || Form.Valid**.
	
**Options**

* **Visible** - Determines if the form can be seen

**Formatting**

* **Fill** - Background color

* **BorderColor** - Border color

* **BorderStyle** - Border style

* **BorderThickness** - Border thickness

**Size & Position**

* **Height** - Height of the card

* **Width** - Width of the card

* **X** - Position relative to upper left of the fluid grid

* **Y** - Position relative to upper left of the fluid grid

## Behavior Properties ##

* **OnFailure**

	Executed after the **SubmitForm** function is called, and the server has determined there is a problem.  The **ErrorType**, **Error**, and possibly **FieldErrors** properties will contain the error information.

* **OnReset**

	Executed when the **Item** changes or the **ResetForm** or **NewForm** function is called.

* **OnSuccess**

	Executed after the **SubmitForm** function is called and no errors were found.

	If the data source provides any information automatically such as an automatically generated primary key, that information will be available in the **Item** and can be read in the **OnSuccess** behavior.

	If the form was in New mode, the created record will be available in the OnSuccess behavior.




