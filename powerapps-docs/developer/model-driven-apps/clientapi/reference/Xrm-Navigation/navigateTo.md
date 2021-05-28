---
title: "navigateTo (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the navigateTo method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# navigateTo (Client API reference)


[!INCLUDE[./includes/navigateTo-description.md](./includes/navigateTo-description.md)]


> [!NOTE]
> This method is supported only on Unified Interface.

## Syntax

`Xrm.Navigation.navigateTo(pageInput,navigationOptions).then(successCallback,errorCallback);`

## Parameters

<table style="width:100%">
<tr>
<th>Name</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
<tr>
<td>pageInput</td>
<td>Object</td>
<td>Yes</td>
<td><p>Input about the page to navigate to. The object definition changes depending on the type of page to navigate to: <i>entity list</i>, <i>entity record</i>, <i> dashboard</i>, or <i>HTML web resource</i>.</p>
<p>----------------------------------------------------------------</p>
<p><strong>entity list</strong>
<p>The object contains the following values:</p>
<ul>
<li><strong>pageType</strong>: String. Specify "entitylist".</li>
<li><strong>entityName</strong>: String. The logical name of the table to load in the list control.</li>
<li><strong>viewId</strong>: (Optional) String. The ID of the view to load. If you don't specify it, navigates to the default main view for the table.</li>
<li><strong>viewType</strong>: (Optional) String. Type of view to load. Specify "savedquery" or "userquery".</li>
</ul>
<p>----------------------------------------------------------------</p>
<p><strong>entity record</strong>
<p>The object contains the following values:</p>
<ul>
<li><strong>pageType</strong>: String. Specify "entityrecord".</li>
<li><b>entityName</b>: String. Logical name of the table to display the form for.</li>
<li><b>entityId</b>: (Optional) String. ID of the table record to display the form for. If you don't specify this value, the form will be opened in create mode.</li>
<li><b>createFromEntity</b>: (Optional) Lookup. Designates a record that will provide default values based on mapped column values. The lookup object has the following String properties: <code>entityType</code>, <code>id</code>, and <code>name</code> (optional).</li>
<li><b>data</b>: (Optional) Object. A dictionary object that passes extra parameters to the form. Invalid parameters will cause an error.<br/>For information about passing parameters to a form, see <a href="/powerapps/developer/model-driven-apps/set-field-values-using-parameters-passed-form
">Set column values using parameters passed to a form</a> and <a href="/powerapps/developer/model-driven-apps/configure-form-accept-custom-querystring-parameters">Configure a form to accept custom querystring parameters</a>.</li>
<li><b>formId</b>: (Optional) String. ID of the form instance to be displayed.</li>
<li><b>isCrossEntityNavigate</b>: (Optional) Boolean. Indicates whether the form is navigated to from a different table using cross-table business process flow.</li>
<li><b>isOfflineSyncError</b>: (Optional) Boolean. Indicates whether there are any offline sync errors.</li>
<li><b>processId</b>: (Optional) String. ID of the business process to be displayed on the form.</li>
<li><b>processInstanceId</b>: (Optional) String. ID of the business process instance to be displayed on the form.</li>
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
</ul>
<p>----------------------------------------------------------------</p>
<p><strong>HTML web resource</strong>
<p>The object contains the following values:</p>
<ul>
<li><strong>pageType</strong>: String. Specify "webresource".</li>
<li><strong>webresourceName</strong>: String. The name of the web resource to load.</li>
<li><strong>data</strong>: (Optional) String. The data to pass to the web resource.</li>
</ul>
<p>----------------------------------------------------------------</p>
<p><strong>dashboard</strong>
<p>The object contains the following values:</p>
<ul>
<li><strong>pageType</strong>: String. Specify "dashboard".</li>
<li><strong>dashboardId</strong>: String. The ID of the dashboard to load. If you don't specify the ID, navigates to the default dashboard.</li>
</ul>
</td>
</tr>
<tr>
<td>navigationOptions</td>
<td>Object</td>
<td>No</td>
<td><p>Options for navigating to a page: whether to open inline or in a dialog. If you don't specify this parameter, page is opened inline by default. The object contains the following values:</p>
<ul>
<li><strong>target</strong>: Number. Specify <strong>1</strong> to open the page inline; <strong>2</strong> to open the page in a dialog. Also, rest of the values (<b>width</b>, <b>height</b>, and <b>position</b>) are valid only if you have specified <strong>2</strong> in this value (open page in a dialog). <p><b>NOTE</b>: <i>Entity lists</i> can only be opened inline; <i>entity records</i> and <i>web resources</i> can be opened either inline or in a dialog.</p></li>
<li><strong>width</strong>: (Optional) Number or Object. The width of dialog. To specify the width in pixels, just type a numeric value. To specify the width in percentage, specify an object of type <b>SizeValue</b> with the following properties:
<ul><li><b>value</b>: Number. The numerical value.</li>
<li><b>unit</b>: String. The unit of measurement. Specify "%" or "px". Default value is "px".</li></ul></li>
<li><strong>height</strong>: (Optional) Number or Object. The height of dialog. To specify the height in pixels, just type a numeric value. To specify the width in percentage, specify an object of type <b>SizeValue</b> with the following properties:
<ul><li><b>value</b>: Number. The numerical value.</li>
<li><b>unit</b>: String. The unit of measurement. Specify "%" or "px". Default value is "px".</li></ul></li>
<li><strong>position</strong>: (Optional) Number. Specify <strong>1</strong> to open the dialog in center; <strong>2</strong> to open the dialog on the side. Default is 1 (center).</li>
<li><strong>title</strong>: (Optional) String. The dialog title on top of the center or side dialog.</li>
</ul></td>
</tr>
<tr>
<td>successCallback</td>
<td>function</td>
<td>No</td>
<td><p>A function to execute on successful navigation to the page when navigating inline and on closing the dialog when navigating to a dialog.</p></td>
</tr>
<tr>
<td>errorCallback</td>
<td>Function</td>
<td>No</td>
<td><p>A function to execute when the operation fails.</p></td>
</tr>
</table>

## Return Value

Returns a promise. The value passed when the promise resolves is dependent on the target:

- *inline*: Promise resolves right away, and does not return any value.
- *dialog*: Promise resolves when the dialog is closed. An object is passed only if the **pageType** = **entityRecord** and you opened the form in create mode. The object has a <b>savedEntityReference</b> array with the following properties to identify the table record created:
    - **entityType**: The logical name of the table.
    - **id**: A string representation of a GUID value for the record.
    - **name**: The primary column value of the record displayed or created.

## Example

### Example 1: Open account list

```javascript
var pageInput = {
    pageType: "entitylist",
    entityName: "account"
};
Xrm.Navigation.navigateTo(pageInput).then(
    function success() {
            // Run code on success
    },
    function error() {
            // Handle errors
    }
);
```
### Example 2: Open an existing account record within a dialog

```javascript
var pageInput = {
    pageType: "entityrecord",
    entityName: "account",
    entityId: "5a57f2c3-5672-ea11-a812-000d3a339706" //replace with actual ID
};
var navigationOptions = {
    target: 2,
    height: {value: 80, unit:"%"},
    width: {value: 70, unit:"%"},
    position: 1
};
Xrm.Navigation.navigateTo(pageInput, navigationOptions).then(
    function success() {
            // Run code on success
    },
    function error() {
            // Handle errors
    }
);
```

### Example 3: Open an account form in the create mode within a dialog

```javascript
var pageInput = {
    pageType: "entityrecord",
    entityName: "account"    
};
var navigationOptions = {
    target: 2,
    height: {value: 80, unit:"%"},
    width: {value: 70, unit:"%"},
    position: 1
};
Xrm.Navigation.navigateTo(pageInput, navigationOptions).then(
    function success(result) {
            console.log("Record created with ID: " + result.savedEntityReference[0].id + 
            " Name: " + result.savedEntityReference[0].name)
            // Handle dialog closed
    },
    function error() {
            // Handle errors
    }
);
```

### Example 4: Open an HTML web resource in a dialog

```javascript
var pageInput = {
    pageType: "webresource",
    webresourceName: "new_sample_webresource.htm"
};
var navigationOptions = {
    target: 2,
    width: 500, // value specified in pixel
    height: 400, // value specified in pixel
    position: 1
};
Xrm.Navigation.navigateTo(pageInput, navigationOptions).then(
    function success() {
            // Run code on success
    },
    function error() {
            // Handle errors
    }
);
```

### Related topics

[Xrm.Navigation](../xrm-navigation.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]