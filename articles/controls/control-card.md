
<properties
    pageTitle="Card controls: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the Card controls"
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

# Card controls in PowerApps #

## Standard Properties ##

* **Default**

* **Update**

* **DataField**

	* Data Type: String
	* Changeable: Yes
	* Readable: No
	* Locked: No

	When inside a Form, name of the field that this card is bound to.  The name must be in a single static string enclosed in double quotes and not a formula.

	The card will display and make editable the value of this field.  You can optionally transform the field before it is displayed with the **DataIn** property.

	When the **SubmitForm** function is executed, the value in this card will be written back to this data field.

* **DisplayName**
 
	* Type: String
	* Changeable: Yes
	* Readable: Yes
	* Locked: No

	You can specify the names to show the user when referring to a field.  By default, display names are taken from the data source which may supply a display name or may use the actual field name.  

	For example, a field may be named "FIRST_NAME" in a data source, that you may want to show as the more friendly "First Name".  To accomplish this **Card.DisplayName = "First Name"**

* **Required**

	* Type: Boolean
	* Changeable: Yes
	* Readable: Yes
	* Locked: Yes

	You can specify if a field needs to contain a value before it can be submitted.  By default, **Required** is filled with information taken from the data source.  

	For example, to force "LAST_NAME" to be a required field, specify **Card.Required = True**.  

* **Error**

	* Type: String
	* Changeable: No
	* Readable: Yes
	* Locked: N/A

	If there is a validation problem with this field, this property contains a user friendly error message to display.  

	**Error** is only populated if the form's **Error** property is also set to a value.  Validation errors will not be displayed until the user calls the **SubmitForm** function.  After this point, validation errors will be displayed and disappear as the user creates and fixes validation issues.

	For conditional formatting, such as making the border of a text box red if there is a problem, use **IsBlank( Card.Error )** to determine if an error is currently being shown for this field.  

* **Valid**


