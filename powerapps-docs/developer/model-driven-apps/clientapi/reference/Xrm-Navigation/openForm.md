---
title: "openForm (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the openForm method.
author: sriharibs-msft
ms.author: srihas
ms.date: 12/01/2022
ms.reviewer: jdaly
ms.topic: reference
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# openForm (Client API reference)


[!INCLUDE[./includes/openForm-description.md](./includes/openForm-description.md)]

> [!NOTE]
> To open a main form as a dialog, use the [navigateTo](navigateTo.md) method instead. More information: [Open main form in a dialog using client API](../../../customize-entity-forms.md#open-main-form-in-a-dialog-using-client-api)

## Syntax

`Xrm.Navigation.openForm(entityFormOptions, formParameters).then(successCallback, errorCallback);`

## Parameters

|Name|Type|Required|Description|
|---|---|---|---|
|`entityFormOptions`|Object|Yes|Form options for opening the form. See [entityFormOptions object](#entityformoptions-object)|
|`formParameters`|Object|No|A dictionary object that passes extra parameters to the form. Invalid parameters will cause an error.<br /><br />For information about passing parameters to a form, see [Set column values using parameters passed to a form](../../../set-field-values-using-parameters-passed-form.md) and [Configure a form to accept custom querystring parameters](../../../configure-form-accept-custom-querystring-parameters.md).|
|`successCallback`|Function|No|A function to execute when the record is saved in the quick create form.This function is passed an object as a parameter. The object has a `savedEntityReference` array with the following properties to identify the record(s) displayed or created:<br /> - `entityType`: The logical name of the table.<br /> - `id`: A string representation of a GUID value for the record.<br /> - `name`: The primary column value of the record displayed or created.<br /><br />**NOTE**: <br /> - The `successCallback` function is not executed when you open a form for an existing or new record.<br /> - The `successCallback` function is executed only when you save a record in a quick create form that was opened using the openForm method.|
|`errorCallback`|Function|No|A function to execute when the operation fails.|



### entityFormOptions object

The object contains the following values:

|Name|Type|Required|Description|
|---|---|---|---|
|`entityName`|String|Yes|Logical name of the table to display the form for.|
|`entityId`|String|No|ID of the table record to display the form for.|
|`formId`|String|No|ID of the form instance to be displayed.|
|`cmdbar`|Bool|No| Indicates whether to display the command bar. If you do not specify this parameter, the command bar is displayed by default. Requires passing `openInNewWindow` parameter as true.|
|`createFromEntity`|Lookup|No|Designates a record that will provide default values based on mapped column values. The lookup object has the following String properties: `entityType`, `id`, and `name` (optional).|
|`openInNewWindow`|Bool|No|Indicates whether to display form in a new window or a new tab. If you specify `true` and do not specify values for height or width, the form will display in a new tab. Opening a form in a new window or a new tab makes the rendering of the form slow compared to opening the form on the same tab; consider opening a form in the main form dialog instead. This property is currently not supported for Quick Create forms, as they can not be opened in a new window or tab.|
|`height`|Number|No|Height of the form window to be displayed in pixels. Requires passing `openInNewWindow` parameter as true.|
|`width`|Number|No|Width of the form window to be displayed in pixels. Requires passing `openInNewWindow` parameter as true.|
|`navbar`|String|No|Controls whether the navigation bar is displayed and whether application navigation is available using the areas and subareas defined in the sitemap. Valid values are: `on`, `off`, or `entity`. Requires passing openInNewWindow parameter as true.<br />- `on`: The navigation bar is displayed. This is the default behavior if the navbar parameter is not used.<br />- `off`: The navigation bar is not displayed. People can navigate using other user interface elements or the back and forward buttons.<br />- `entity`: On a form, only the navigation options for related tables are available. After navigating to a related table, a back button is displayed in the navigation bar to allow returning to the original record.|
|`relationship`|Object|No|Define a relationship object to display the related records on the form. See [relationship object](#relationship-object)|
|`selectedStageId`|String|No|ID of the selected stage in business process instance.|
|`useQuickCreateForm`|Bool|No| Indicates whether to open a quick create form. The table must have the **Allow Quick Create** option enabled for the quick create form to be displayed and you must also add the table and the quick create form to your app. If you do not specify the value of `useQuickCreateForm`, the default will be set to `false`.|

### relationship object

The object has the following values.  

|Name|Type|Description|
|---|---|---|
|`attributeName`|String|Name of the column used for relationship.|
|`name`|String|Name of the column used for relationship.|
|`navigationPropertyName`|String|Name of the column used for relationship.|
|`relationshipType`|Number|Relationship type. Specify one of the following values:<br />- 0:OneToMany<br />- 1:ManyToMany|
|`roleType`|Number|Role type in relationship. Specify one of the following values:<br />- 1:Referencing<br />- 2:AssociationEntity|

## Remarks

You must use this method to open table or quick create forms instead of the deprecated  [Xrm.Utility.openEntityForm](/previous-versions/dynamicscrm-2016/developers-guide/jj602956(v=crm.8)#openEntityForm) and  [Xrm.Utility.openQuickCreate](/previous-versions/dynamicscrm-2016/developers-guide/jj602956(v=crm.8)#openQuickCreate) methods.

Use [setActiveProcess](../formcontext-data-process/activeprocess/setactiveprocess.md) to display a particular business process and [setActiveProcessInstance](../formcontext-data-process/setactiveprocessinstance.md) to display a particular business process instance on the form.
 

## Examples

### Example 1: Open a form for existing record

The following sample code opens a contact form to display an existing contact record:

```JavaScript
var entityFormOptions = {};
entityFormOptions["entityName"] = "contact";
entityFormOptions["entityId"] = "00aa00aa-bb11-cc22-dd33-44ee44ee44ee";

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

### Example 3: Open a form for new record (complex lookup)

The following sample code opens a activity form with some pre-populated values (including a complex lookup) to create a new record:

```JavaScript
var entityFormOptions = {};
entityFormOptions["entityName"] = "email";

// Set default values for the Contact form
var formParameters = {};
formParameters["subject"] = "Sample";
formParameters["description"] = "Default values for this record were set programmatically.";

// Set lookup column
formParameters["regardingobjectid"] = "3493e403-fc0c-eb11-a813-002248e258e0"; // ID of the user.
formParameters["regardingobjectidname"] = "Admin user"; // Name of the user.
formParameters["regardingobjectidtype"] = "systemuser"; // Table name. 
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

### Example 4: Open a quick create form

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

### Related articles

[Xrm.Navigation](../xrm-navigation.md)


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
