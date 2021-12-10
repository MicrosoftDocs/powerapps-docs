---
title: "openForm (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the openForm method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
ms.assetid: 0206c43b-b1fc-490d-a867-1d75331885a8
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# openForm (Client API reference)

[!INCLUDE[./includes/openForm-description.md](./includes/openForm-description.md)]

## Syntax

`Xrm.Navigation.openForm(entityFormOptions,formParameters).then(successCallback,errorCallback);`

## Parameters


<table style="width:100%">
  <tr>
    <th>Name</th>
    <th>Type</th> 
    <th>Required</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>entityFormOptions</td>
    <td>Object</td> 
    <td>Yes</td>
    <td>Form options for opening the form. The object contains the following values:<ul>
<li><b>entityName</b>: String. Logical name of the table to display the form for.</li>
<li><b>entityId</b>: (Optional) String. ID of the table record to display the form for.</li>
<li><b>formId</b>: (Optional) String. ID of the form instance to be displayed.</li>
<li><b>cmdbar</b>: (Optional) Boolean. Indicates whether to display the command bar. If you do not specify this parameter, the command bar is displayed by default.</li>
<li><b>createFromEntity</b>: (Optional) Lookup. Designates a record that will provide default values based on mapped column values. The lookup object has the following String properties: <code>entityType</code>, <code>id</code>, and <code>name</code> (optional).</li>
<li><b>height</b>: (Optional) Number. Height of the form window to be displayed in pixels.</li>
<li><b>navbar</b>: (Optional) String. Controls whether the navigation bar is displayed and whether application navigation is available using the areas and subareas defined in the sitemap. Valid values are: "on", "off", or "entity".<ul><li><code>on</code>: The navigation bar is displayed. This is the default behavior if the <b>navbar</b> parameter is not used.</li>
<li><code>off</code>: The navigation bar is not displayed. People can navigate using other user interface elements or the back and forward buttons.</li><li><code>entity</code>: On a form, only the navigation options for related tables are available. After navigating to a related table, a back button is displayed in the navigation bar to allow returning to the original record.</li></ul></li>
<li><b>openInNewWindow</b>: (Optional) Boolean. Indicates whether to display form in a new window or a new tab. If you specify <code>true</code> and do not specify values for height or width, the form will display in a new tab. Opening a form in a new window or a new tab makes the rendering of the form slow compared to opening the form on the same tab; consider opening a form in the main form dialog instead. This property is currently not supported for Quick Create forms, as they can not be opened in a new window or tab.</li>
<li><b>windowPosition</b>: (Optional) Number. Specify one of the following values for the position of the form on the screen:<ul><li><code>1:center</code></li><li><code>2:side</code></li></ul>
This does not apply to opening a new browser window.  
<li><b>relationship</b>: (Optional) Object. Define a relationship object to display the related records on the form. The object has the following values.
<table style="width:100%">
  <tr>
    <th>Name</th>
    <th>Type</th> 
    <th>Description</th>
<tr>
<td>attributeName</td>
<td>String</td>
<td>Name of the column used for relationship.</td>
</tr>
<tr>
<td>name</td>
<td>String</td>
<td>Name of the relationship.</td>
</tr>
<tr>
<td>navigationPropertyName</td>
<td>String</td>
<td>Name of the navigation property for this relationship.</td>
</tr>
<tr>
<td>relationshipType</td>
<td>Number</td>
<td>Relationship type. Specify one of the following values:
<ul><li><code>0:OneToMany</code></li><li><code>1:ManyToMany</code></li></ul></td>
</tr>
<tr>
<td>roleType</td>
<td>Number</td>
<td>Role type in relationship. Specify one of the following values:
<ul><li><code>1:Referencing</code></li><li><code>2:AssociationEntity</code></li></ul></td>
</tr>
</table>
</li>
<li><b>selectedStageId</b>: (Optional) String. ID of the selected stage in business process instance.</li>
<li><b>useQuickCreateForm</b>: (Optional) Boolean. Indicates whether to open a quick create form.  The table must have the <b>Allow Quick Create</b> option enabled for the quick create form to be displayed and you must also add the table and the quick create form to your app. If you do not specify the value of <code>useQuickCreateForm</code>, the default will be set to <b>false</b>.</li>
<li><b>width</b>: (Optional) Number. Width of the form window to be displayed in pixels.</li>
</ul>
</tr>
<tr>
<td>formParameters</td>
<td>Object</td>
<td>No</td>
<td>A dictionary object that passes extra parameters to the form. Invalid parameters will cause an error.<br/><br/>For information about passing parameters to a form, see <a href="/powerapps/developer/model-driven-apps/set-field-values-using-parameters-passed-form
">Set column values using parameters passed to a form</a> and <a href="/powerapps/developer/model-driven-apps/configure-form-accept-custom-querystring-parameters">Configure a form to accept custom querystring parameters</a></td>
</tr>
<tr>
<td>successCallback</td>
<td>Function</td>
<td>No</td>
<td>A function to execute when the record is saved in the quick create form.

This function is passed an object as a parameter. The object has a <b>savedEntityReference</b> array with the following properties to identify the record(s) displayed or created:
<ul>
<li><b>entityType</b>: The logical name of the table.</li>
<li><b>id</b>: A string representation of a GUID value for the record.</li>
<li><b>name</b>: The primary column value of the record displayed or created.</li></ul>

<b>NOTE</b>:
  <ul>
    <li>The <b>successCallback</b> function is not executed when you open a form for an existing or new record.</li>
    <li>The <b>successCallback</b> function is executed only when you save a record in a quick create form that was opened using the <strong>openForm</strong> method.</li>    
  </ul>
</td>
</tr>
<tr>
<td>errorCallback</td>
<td>Function</td>
<td>No</td>
<td>A function to execute when the operation fails.<br>
</td>
</tr>
</table>

## Remarks

You must use this method to open table or quick create forms instead of the deprecated  [Xrm.Utility.openEntityForm](/previous-versions/dynamicscrm-2016/developers-guide/jj602956(v=crm.8)#openEntityForm) and  [Xrm.Utility.openQuickCreate](/previous-versions/dynamicscrm-2016/developers-guide/jj602956(v=crm.8)#openQuickCreate) methods. 
Use [setActiveProcess](../formcontext-data-process/activeprocess/setactiveprocess.md) to display a particular business process and [setActiveProcessInstance](../formcontext-data-process/setactiveprocessinstance.md) to display a particular business process instance on the form.
 

## Examples

### Example 1: Open a form for existing record

The following sample code opens a contact form to display an existing contact record:

```JavaScript
var entityFormOptions = {};
entityFormOptions["entityName"] = "contact";
entityFormOptions["entityId"] = "8DA6E5B9-88DF-E311-B8E5-6C3BE5A8B200";

// Open the form.
Xrm.Navigation.openForm(entityFormOptions).then(
    function (success) {
        console.log(success);
    },
    function (error) {
        console.log(error);
    });
```

### Example 2: Open a form for new record

The following sample code opens a contact form with some pre-populated values to create a new record:

```JavaScript
var entityFormOptions = {};
entityFormOptions["entityName"] = "contact";

// Set default values for the Contact form
var formParameters = {};
formParameters["firstname"] = "Sample";
formParameters["lastname"] = "Contact";
formParameters["fullname"] = "Sample Contact";
formParameters["emailaddress1"] = "contact@adventure-works.com";
formParameters["jobtitle"] = "Sr. Marketing Manager";
formParameters["donotemail"] = "1";
formParameters["description"] = "Default values for this record were set programmatically.";

// Set lookup column
formParameters["preferredsystemuserid"] = "3493e403-fc0c-eb11-a813-002248e258e0"; // ID of the user.
formParameters["preferredsystemuseridname"] = "Admin user"; // Name of the user.
formParameters["preferredsystemuseridtype"] = "systemuser"; // Table name. 
// End of set lookup column

// Open the form.
Xrm.Navigation.openForm(entityFormOptions, formParameters).then(
    function (success) {
        console.log(success);
    },
    function (error) {
        console.log(error);
    });
```

### Example 3: Open a quick create form

The following sample code opens a quick create contact form with some pre-populated values:

```JavaScript
var entityFormOptions = {};
entityFormOptions["entityName"] = "contact";
entityFormOptions["useQuickCreateForm"] = true;

// Set default values for the Contact form
var formParameters = {};
formParameters["firstname"] = "Sample";
formParameters["lastname"] = "Contact";
formParameters["fullname"] = "Sample Contact";
formParameters["emailaddress1"] = "contact@adventure-works.com";
formParameters["jobtitle"] = "Sr. Marketing Manager";
formParameters["donotemail"] = "1";
formParameters["description"] = "Default values for this record were set programmatically.";

// Set lookup column
formParameters["preferredsystemuserid"] = "3493e403-fc0c-eb11-a813-002248e258e0"; // ID of the user.
formParameters["preferredsystemuseridname"] = " Admin user"; // Name of the user.
formParameters["preferredsystemuseridtype"] = "systemuser"; // Table name.
// End of set lookup column

// Open the form.
Xrm.Navigation.openForm(entityFormOptions, formParameters).then(
    function (success) {
        console.log(success);
    },
    function (error) {
        console.log(error);
    });
```

### Related topics

[Xrm.Navigation](../xrm-navigation.md)


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
