---
title: Configure advanced form metadata for portals
description: Learn how to add and configure advanced form metadata for a portal.
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 06/22/2021
ms.subservice: portals
ms.author: sandhan
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - sandhangitmsft
---

# Configure advanced form metadata for portals

The Advanced Form Metadata contains additional behavior modification logic to augment or override the functionality of form fields that is otherwise not possible with native basic form editing capabilities.

## Add a new record

1. On the Advanced Form Step that has fields that you would like to modify, go to **Related** > **Metadata** 

2. Select **New Advanced Form Metadata**.

## Advanced form metadata properties

The following attributes provide additional styling and capabilities for elements on a form.

| Name          | Description                                                                                                                                                                                                                                                                                                                                          |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Advanced Form Step | The Advanced Form Step associated with the Advanced Form Metadata record.                                                                                                                                                                                                                                                                                      |
| Type          | Available options are:<ul><li>Attribute</li><li>Section</li><li>Tab</li></ul>Selecting Attribute as the Type value displays the appropriate options for modifying fields on the current form rendered for the related step. Selecting Section as the Type value displays the options available for modifying a section on the form. Selecting Tab as the Type value displays the options available for modifying a tab on a form.  |

## Advanced form metadata type = Attribute

The following properties are displayed when the Type selected is 'Attribute'.


|          Name          |                                                                                                                                                    Description                                                                                                                                                     |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Attribute Logical Name |                                                                                                                              The logical name of the attribute field to be modified.                                                                                                                               |
|         Label          | Replaces the default label assigned to the attribute on the table with the text specified in this input. For each language pack installed and enabled for the Microsoft Dataverse environment a field will be available to enter the message in the associated language. |

### Control style

The following options modify the style and functionality of an attribute's field.


|                      Name                       |                                                                                                                                                                                                                                                                                                                                       Description                                                                                                                                                                                                                                                                                                                                       |
|-------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                      Style                      | One of the following:<ul><li>Option Set as Vertical Radio Button List</li><li>Option Set as Horizontal Radio Button List</li><li>Single Line of Text as Geolocation Lookup Validator (requires [!INCLUDE[pn-bing](../../../includes/pn-bing.md)] Maps Settings - details found here)</li><li>Group Whole Number as Constant Sum (requires Group Name)</li><li>Group Whole Number as Rank Order Scale No Ties (requires Group Name)</li><li>Group Whole Number as Rank Order Scale Allow Ties (requires Group Name)</li><li>Multiple Choice Matrix (requires Group Name)</li><li>Multiple Choice (requires Group Name)</li><li>Group Whole Number as Stack Rank (requires Group Name)</li><li>Code component</li><li>Render Lookup as Dropdown</li></u> |
|                   Group Name                    |                                                                                                                                                                                                                                                                                                             A name used to group controls together as a composite control.                                                                                                                                                                                                                                                                                                              |
| Multiple Choice Minimum Required Selected Count |                                                                                                                                                                                                                                                                      This is the required minimum values selected in the multiple choice question. Only necessary if 'Multiple Choice' Control Style is selected.                                                                                                                                                                                                                                                                       |
|       Multiple Choice Max Selected Count        |                                                                                                                                                                                                                                                          This is the maximum number of values that is permitted to be selected in the multiple choice question. Only necessary if 'Multiple Choice' Control Style is selected.                                                                                                                                                                                                                                                          |
|           Constant Sum Minimum Total            |                                                                                                                                                                                                                                                             This is the required minimum value applied to a constant sum response field. Only necessary if 'Group Whole Number as Constant Sum' Control Style is selected.                                                                                                                                                                                                                                                              |
|           Constant Sum Maximum Total            |                                                                                                                                                                                                                                                 This is the maximum number of value that is permitted to be applied to a constant sum response field. Only necessary if 'Group Whole Number as Constant Sum' Control Style is selected.                                                                                                                                                                                                                                                 |
|           Randomize Option Set Values           |                                                                                                                                                                                                                                                                     Specifying Yes results in randomly ordered options listed for an Option Set control. Only applicable to attributes that are of type Option Set.                                                                                                                                                                                                                                                                     |
|                    CSS Class                    |                                                                                                                                                                                                                                                                                                                      Adds a custom CSS class name to the control.                                                                                                                                                                                                                                                                                                                       |

### Prepopulate field

The following options provide a default value for fields on the form.


|         Name         |                                                                                                                                                                                                                                                                Description                                                                                                                                                                                                                                                                 |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ignore Default Value |                                                                              Ignores the default value of the specified attribute field. Useful for attributes that are Two Option fields that are rendered as Yes and No radio buttons. Because a value of yes or no is automatically assigned by default, this option makes it possible to display Yes/No questions without a predefined response.                                                                               |
|         Type         | One of the following:<ul><li>Value</li><li>Today's Date</li><li>Current User's Contact</li></ul>Selecting Value requires a value to be specified in the **Value** field that will be assigned to the field when the form is loaded. Selecting Today's Date will assign the current date and time to the attribute field. Selecting Current User's Contact requires a **From Attribute** that is an attribute on the contact table that will be retrieved from the current user's contact record and set on the attribute field specified. |
|        Value         |                                                                                                                                                                                                                                        A value to be assigned to the field when the form is loaded.                                                                                                                                                                                                                                        |
|    From Attribute    |                                                                                                                                                                                             An attribute on the contact table that will be retrieved from the current portal user's record and assigned to the field when the form is loaded.                                                                                                                                                                                             |

### Set Value On Save

The following options specify a value to be set when the form is saved.

| Name              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Set Value On Save | Yes indicates that a value should be assigned to the attribute using the input provided in the **Value** field. <br>**Note**: All attribute types are supported except the following: Unique Identifier.       |
| Type              | One of the following:<ul><li>Value</li><li>  Today's Date</li><li>Current User's Contact</li></ul>Selecting Value requires a value to be specified in the **Value** field that will be assigned to the field when the form is loaded. Selecting Today's Date will assign the current date and time to the attribute field. Selecting Current User's Contact requires a **From Attribute** that is an attribute on the contact table that will be retrieved from the current user's contact record and set on the attribute field specified.  |
| Value             | Value assigned to the attribute when the form is being saved.<br>For Two Option (Boolean) fields use true or false.<br>For Option Set field use the integer value for the option.<br>For Lookup (TableReference) fields, use the GUID.<br>**Note**: If the attribute is also on the form the user's value will be overwritten with this value.|
| From Attribute    | An attribute on the contact table that will be retrieved from the current portal user's record and assigned to the field during save. |

### Lookup Settings

The lookup setting **Basic form for Create** is used to populate the Basic Form for creating a new record from the lookup when the metadata created for an attribute is of lookup type.

### Validation

The following section contains properties that modify various validation parameters and error messages.

For each language pack installed and enabled for the Dataverse environment, a field will be available to enter the message in the associated language.

| Name                                        | Description                                                                                                                                                                                                                                                      |
|---------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Validation Error Message                    | Overrides the default validation error message for the field.                                                                                                                                                                                                    |
| Regular Expression                          | A regular expression to be added to validate the field.                                                                                                                                                                                                          |
| Regular Expression Validation Error Message | The validation error message to display if the regular expression validated fails.                                                                                                                                                                               |
| Field is Required                           | Check to make the attribute field required to contain a value.                                                                                                                                                                                                   |
| Required Field Validation Error Message     | Overrides the default required field error message if the field does not contain a value.                                                                                                                                                                        |
| Range Validation Error Message              | Overrides the default range validation error message displayed if the field's value is outside of the appropriate minimum and maximum values specified on the table attribute that are of type Whole Number, Decimal Number, Floating Point Number or Currency. |
| Geolocation Validator Error Message         | Applicable if the attribute is a Single Line of Text and the Control Style specified is Single Line of Text as Geolocation Lookup Validator then this will override the default error message displayed if input validation fails. |
| Constant Sum Validation Error Message       | Applicable if the attribute is a Whole Number type and the Control Style specified is Group Whole Number as Constant Sum then this will override the default error message displayed if input validation fails.                    |
| Multiple Choice Validation Error Message    | Applicable if the attribute is a Two Option type and the Control Style specified is Multiple Choice then this will override the default error message displayed if input validation fails.                                         |
| Rank Order No Ties Validation Error Message | Applicable if the attribute is a Whole Number type and the Control Style specified is Group Whole Number as Rank Order No Ties then this will override the default error message displayed if input validation fails.              |

### Description and instructions

The following properties specify the location and content of custom description or instructions.


|                 Name                 |                                                                                                                                                           Description                                                                                                                                                           |
|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|           Add Description            |                                                                                                                        Yes results in custom text being displayed on the form in the position specified.                                                                                                                        |
|               Position               |                                                                                                             One of the following:<ul><li>Above the field</li><li>Below the field</li><li>Above the label</li></ul>                                                                                                              |
| Use Attribute's Description Property |                                                                                       Select 'Yes' to use the description assigned to the attribute metadata on the table. Select 'No' to provide a custom description. Default is 'No'.                                                                                       |
|             Description              | Custom text to be displayed on the form. Used in conjunction when Use Attribute's Description Property is set to 'No'. For each language pack installed and enabled for the Dataverse environment a field will be available to enter the message in the associated language. |

## Advanced Form metadata type = Section

The following properties are displayed when the Type selected equals 'Section'.


|     Name     |                                                                                                                                                   Description                                                                                                                                                    |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Section Name |                                                                                           The name of the section on the table's form to be modified.                                                                                            |
|    Label     | Replaces the default label assigned to the section on the table with the text specified in this input. For each language pack installed and enabled for the Dataverse environment a field will be available to enter the message in the associated language. |

## Advanced Form metadata type = Tab

The following properties are displayed when the Type selected equals 'Tab'


|   Name   |                                                                                                                                                 Description                                                                                                                                                  |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Tab Name |                                                                                           The name of the tab on the table's form to be modified.                                                                                            |
|  Label   | Replaces the default label assigned to the tab on the table with the text specified in this input. For each language pack installed and enabled for the Dataverse environment a field will be available to enter the message in the associated language. |

### See also

[Configure a portal](configure-portal.md)  
[Define basic forms](entity-forms.md)  
[Advanced Form properties for portals](web-form-properties.md)  
[Advanced Form steps for portals](web-form-steps.md)  
[Advanced Form subgrid configuration for portals](configure-web-form-subgrid.md)  
[Notes configuration for Advanced Forms for portals](../configure-notes.md)  



[!INCLUDE[footer-include](../../../includes/footer-banner.md)]