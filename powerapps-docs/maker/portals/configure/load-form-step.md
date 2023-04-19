---
title: Define a load form and load tab step type
description: Learn how to define a load form and load tab step type in a portal.
author: sandhangitmsft

ms.topic: conceptual
ms.custom: 
ms.date: 02/02/2022
ms.subservice: portals
ms.author: sandhan
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - sandhangitmsft
---

# Define a load form and load tab step type


[!INCLUDE[cc-pages-ga-banner](../../../includes/cc-pages-ga-banner.md)]

This step type allows the multistep form step to act as a basic form within the overall multistep form process. It loads a form with a similar set of options available as a Basic Form.

## Settings

| Name                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name                                  | The descriptive name of the record. Required                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Table Name                           | The name of the basic form which the form will be loaded from. Required                                                                                                                                                                                                                                                                                                                                                                                                             |
| Form Name                             | The name of the Form on the target table that is to be rendered. Required                                                                                                                                                                                                                                                                                                                                                                                                           |
| Tab Name                              | The name of a Tab on a Form for a specified table that is to be rendered. Optional                                                                                                                                                                                                                                                                                                                                                                                                  |
| Mode                                  | One of the following values:<br><ul><li>Insert</li><li>Edit</li><li>ReadOnly</li></ul>Selecting Insert indicates the form should insert a new record upon submission. Specifying Edit indicates the form should edit an existing record. Selecting ReadOnly indicates the form should display an existing record's noneditable form. Edit and ReadOnly requires that a source record exist and parameters specified in the 'Record Source Type' and 'Record ID Parameter Name' fields to select the appropriate record when the form is loaded in the portal.  |
| Auto Generate Steps From Tabs         | Checked indicates that multiple tabs on a basic form will be displayed with each tab as a sequential step starting with the first tab and continue until all tabs have been navigated to and upon final submission a record is inserted. Unchecked is the default behavior. Unchecked value indicates that only one tab or form is to be rendered for the current step. If the Tab Name isn't specified, the first tab is displayed.                                              |
| Record Source Type                    | One of the following values:<br><ul><li>Query String <br> Selecting Query String requires a parameter name that must be provided in the query string of the URL to the form. This can be specified in the 'Record ID Parameter Name' field.</li><li>Current Portal User <br> Selecting Current Portal User will retrieve the portal user record for the current authenticated user.</li></ul>                                                                                                                                                                                                                                                                                                                                                         |
| Record ID Parameter Name | A parameter name provided in the query string of the URL to the Web Page containing this Basic Form.                                                                                                                                                                                                                                                                                                                                                                                |
| Relationship Name                     | Required when Record Source Type is Record Associated to Current Portal User. The logical name of the relationship between the current portal user record and the target record. This must return the same table type specified by the Table Name field.                                                                                                                                                                                                                           |
| Enable Table Permissions             | Will cause the form to respect Table Permissions. The default is false for backwards compatibility reasons. If set to true, explicit permissions are REQUIRED for any user wanting to access the form. This only applies to the FIRST step of a form. <br> **NOTE**: This method of securing forms would be deprecated soon. Therefore, it shouldn't be used. Use proper [table permissions](entity-permissions-studio.md), and web role setup to provide access to users for any data instead. See next section [Secure your forms](#secure-your-forms) details. More information: [Table permission changes for forms and lists on new portals](../important-changes-deprecations.md#table-permission-changes-for-forms-and-lists-on-new-portals)                                                                                                                                                                                                                    |
||

## Secure your forms

>[!NOTE]
> This method of securing forms would be deprecated soon. Therefore, it shouldn't be used. Use proper [table permissions](entity-permissions-studio.md), and web role setup to provide access to users for any data instead. More information: [Table permission changes for forms and lists on new portals](../important-changes-deprecations.md#table-permission-changes-for-forms-and-lists-on-new-portals)

To secure your forms, you must create table permissions that determine access and ownership of the records according to web roles. If a user lands on a multistep form and doesn't have permissions, they'll receive an error message. In addition, you'll also see a warning when a form is configured with table permissions not enabled:

"Table permissions should be enabled for this record or anyone on the internet can view the data."

To enable permissions for a multistep form, select the checkbox to **Enable Table Permissions**. [!INCLUDE[proc-more-information](../../../includes/proc-more-information.md)] [Create web roles for portals](create-web-roles.md).  

## Other settings

|                Name                |                                                                                 Description                                                                                 |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|    Render Web Resources Inline     |                     Eliminates the IFrame that encompasses a web resource in a basic form.                     |
|          ToolTips Enabled          |                                               The tooltip is set using the description of the attribute on the target table.                                               |
|      Show Unsupported Fields       |       All fields are currently supported. This is reserved for potential changes may make to field types.       |
| Set Recommended Fields as Required |                                     Makes all attributes required that have the field requirement level set to 'Business Recommended'.                                      |
|      Make All Fields Required      |                                                    Makes all fields required regardless of the field requirement level.                                                     |
|    Validation Summary CSS Class    |                               CSS Class name assigned to the validation summary. Default: 'validation-summary alert alert-error alert-block'                                |
|  Enable Validation Summary Links   | A Boolean value of true or false that indicates whether anchor links should be rendered in the validation summary to scroll to the field containing an error. Default: true |
|    Validation Summary Link Text    |                                                   The label assigned to the validation summary links. Default: Click here                                                   |
|            Instructions            |                                                               Display a block of text at the top of the form.                                                               |
|      Record Not Found Message      |                          Message displayed when the source record can't be loaded. Default: The record you're looking for couldn't be found.                           |

## Form options

| Name                      | Description                                                                                                                                                                       |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Add Captcha               | Portal uses RadCaptcha by Telerik to prevent malicious spam attacks. The service requires a unique key to authenticate requests for your portal application. |
| Validation Group          | The group name assigned to input controls for evaluating valid input of named groups.                                                                                             |
| Previous Button CSS Class | CSS Class name assigned to the Previous button.                                                                                                                                   |
| Previous Button Text      | Label on the previous button.                                                                                                                                                     |
| Next Button CSS Class     | CSS Class name assigned to the next button.                                                                                                                                       |
| Submit Button Text        | Label on the next button.                                                                                                                                                         |
| Submit Button CSS Class   | CSS Class name assigned to the submit button. Default: button submit                                                                                                              |
| Submit Button Text        | Label on the submit button. Default is 'Submit'                                                                                                                                   |
| Submit Button Busy Text   | Label on the submit button during the running process. Default: Processing...                                                                                                     |
||

## Associate the current portal user with the creation of a record

These options are used to keep track of which portal contact creates a record through the portal UI

| Name                                       | Description                                                                                                                                                                             |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Associate Current Portal User              | Checked indicates the currently logged in user's record should be associated with the target table record.                                                                             |
| Portal User Lookup Column | The logical name of the attribute on the target table that stores the portal user.                                                                                                     |
| Is Activity Party                          | Boolean value indicating whether the Portal User Lookup Column is an Activity Party type. See [ActivityParty table](/previous-versions/dynamicscrm-2016/developers-guide/gg328549(v=crm.8)) |  
||

## Associated table reference

The following parameters pertain to setting an associated table reference when the form is saved.

This provides a way to associate the current record being created or updated by the form with another target record. This is useful if you have multiple steps with multiple table types and wish to relate the resulting records or if the page is passed a query string of a record ID that you would like associated. For example we have a careers page that lists job postings, each with a link to an application for the job that contains the id of the job posting to the application form so that when the application is created the job posting is associated with the record.

| Name                                 | Description                                                                                                                                                    |
|---------------------------------|------------|
| Set Table Reference On Save         | Yes or No. A value of yes indicates that an associated table reference should be assigned when the form is saved, otherwise none will be set.                                                                                                                 |
| Relationship Name                    | The Relationship Definition Name for a given relationship between two table types.<br>**Note**: Don't specify a relationship name if you specify a Target Lookup Attribute Logical Name. 
| Table Logical Name                  | The logical name of the reference table.                |
| Target Lookup Attribute Logical Name | Logical name of the lookup attribute on the target table being created or updated. <br>**Note**: Don't specify a relationship name if you specify a Target Lookup Attribute Logical Name.                                                                           |
| Populate Lookup Field                | If the lookup regarding the reference table is on the form, checking this value will populate the field on the form with the value retrieved using the setting below.                                                                                                                                                                                                                                                                               |
| Source Type                          | One of the following values:<ul><li>Query String <br> Selecting Query String requires a parameter name that must be provided in the query string of the URL to the form. This can be specified in the **Query String Name** field. If this parameter is the primary key, then select Yes for the **Query String Is Primary Key**, otherwise select No and provide the logical name of the attribute on the target table to query by specified in the **Query Attribute Logical Name** field.</li><li>Current Portal User <br> Selecting Current Portal User will retrieve the contact record for the current authenticated user. </li></ul>   |
| Reference Table Step                | The Multistep Form Step record of a previous step to retrieve the table created or edited in that step to associate it with the record for this current step.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Query String Name                    | Parameter name provided in the Query String of the URL to the Web Page containing the Multistep Form.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Query String Is Primary Key          | Yes indicates the Query String value is the Primary Key value. No indicates the Query String value is an attribute type other than the Primary Key.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Query Attribute Logical Name         | Logical name of the attribute to query the record.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Show ReadOnly Details                | Checked indicates that a form should be rendered at the top of the page displaying read-only information pertaining to the reference record. Requires a Form Name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Form Name                            | The name of the form on the reference table that should be used to display read-only details.                                                      |
||

## Other functionality

|                              Name                              |                                                                                                                                                                                                                   Description                                                                                                                                                                                                                   |
|----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                          Attach File                           |                                                                                                                                                          Check to have the form include a file upload control to the bottom of the form to allow a file to be attached to the record.                                                                                                                                                           |
|                      Allow Multiple Files                      |                                                                                                                                                                                 A Boolean value that indicates whether the user can upload more than one file.                                                                                                                                                                                  |
|                             Accept                             |                                                                                                                 The accept attribute specifies the MIME types of files that the server accepts through file upload. To specify more than one value, separate the values with a comma (for example, audio/\*,video/\*,image/\*).                                                                                                                 |
|                             Label                              |                                                                                          The text displayed next to the file upload control. For each language pack installed and enabled for the Microsoft Dataverse environment a field will be available to enter the message in the associated language.                                                                                           |
|                          Is Required                           |                                                                                                                                                                                           Checked makes the attachment of a file required to proceed.                                                                                                                                                                                           |
|                     Required Error Message                     |                                                               The message displayed during form validation if Is Required is true and the user hasn't attached a file. For each language pack installed and enabled for the Dataverse environment a field will be available to enter the message in the associated language.                                                                |
| Custom [!INCLUDE[pn-javascript](../../../includes/pn-javascript.md)] | A custom block of [!INCLUDE[pn-javascript](../../../includes/pn-javascript.md)] that will added to the bottom of the page just before the closing form tag element. The HTML input id of a table field is set to the logical name of the attribute. This makes selecting a field, setting values, or other client side manipulation easy with jQuery. ``` $(document).ready(function() { $(#address1_stateorprovince).val(Saskatchewan); });``` |

### See also

[Configure a portal](configure-portal.md)  
[Define basic forms](entity-forms.md)  
[Multistep Form steps for portals](web-form-steps.md)  
[Redirect step type](add-redirect-step.md)  
[Conditional step type](add-conditional-step.md)  
[Add custom JavaScript](add-custom-javascript.md)  



[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
