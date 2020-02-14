---
title: "navigateTo (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 11/04/2019
ms.service: powerapps
ms.topic: "reference"
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# navigateTo (Client API reference)

[!INCLUDE[./includes/navigateTo-description.md](./includes/navigateTo-description.md)]


> [!NOTE]
> This method is supported only on the Unified Interface.

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
<td><p>Input about the page to navigate to. The object definition changes depending on the type of page to navigate to: <i>entity record</i>, <i>entity list</i> or <i>HTML web resource</i>.</p>
<p><strong>Entity record</strong>
<p>The object contains the following attributes:</p>
<ul>
<li><strong>pageType</strong>: String. Specify "entityrecord".</li>
<li><strong>entityName</strong>: String. The logical name of the entity to load in the form.</li>
<li><strong>formType</strong>: (Optional) Integer. The ID of the form type. If you don't specify it, navigates to the create form.</li>
<li><strong>entityId</strong>: (Optional) String. The ID of the entity record to load. If you don't specify it, navigates to the create form.</li>
</ul>
<p><strong>Entity list</strong>
<p>The object contains the following attributes:</p>
<ul>
<li><strong>pageType</strong>: String. Specify "entitylist".</li>
<li><strong>entityName</strong>: String. The logical name of the entity to load in the list control.</li>
<li><strong>viewId</strong>: (Optional) String. The ID of the view to load. If you don't specify it, navigates to the default main view for the entity.</li>
<li><strong>viewType</strong>: (Optional) String. Type of view to load. Specify "savedquery" or "userquery".</li>
</ul>
<p><strong>HTML web resource</strong>
<p>The object contains the following attributes:</p>
<ul>
<li><strong>pageType</strong>: String. Specify "webresource".</li>
<li><strong>webresourceName</strong>: String. The name of the web resource to load.</li>
<li><strong>data</strong>: (Optional) String. The data to pass to the web resource.</li>
</ul></td>
</tr>
<tr>
<td>navigationOptions</td>
<td>Object</td>
<td>No</td>
<td><p>Options for navigating to a page: whether to open inline or in a dialog. If you don't specify this parameter, page is opened inline by default. The object contains the following attributes:</p>
<ul>
<li><strong>target</strong>: Number. Specify <strong>1</strong> to open the page inline; <strong>2</strong> to open the page in a dialog. <br/><i>Entity lists</i> can only be opened inline; <i>web resources</i> can be opened either inline or in a dialog.</li>
<li><strong>width</strong>: (Optional) Number or Object. The width of dialog. To specify the width in pixels, just type a numeric value. To specify the width in percentage, specify an object of type <b>SizeValue</b> with the following properties:
<ul><li><b>value</b>: Number. The numerical value.</li>
<li><b>unit</b>: String. The unit of measurement. Specify "%" or "px". Default value is "px".</li></ul></li>
<li><strong>height</strong>: (Optional) Number or Object. The height of dialog. To specify the height in pixels, just type a numeric value. To specify the width in percentage, specify an object of type <b>SizeValue</b> with the following properties:
<ul><li><b>value</b>: Number. The numerical value.</li>
<li><b>unit</b>: String. The unit of measurement. Specify "%" or "px". Default value is "px".</li></ul></li>
<li><strong>position</strong>: (Optional) Number. Specify <strong>1</strong> to open the dialog in center; <strong>2</strong> to open the dialog on the side. Default is 1 (center).</li>
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

## Example

The following example demonstrates how to navigate to an HTML web resource that is opened in a dialog:

```javascript
var pageInput = {
    pageType: "webresource", 
    webresourceName: "new_sample_webresource"
};
var navigationOptions = {
    target: 2,
    width: 400,
    height: 300,
    position: 1
};
Xrm.Navigation.navigateTo(pageInput, navigationOptions).then(
    function success() {
            // Handle dialog closed
    },
    function error() {
            // Handle errors
    }
);
```



### Related topics

[Xrm.Navigation](../xrm-navigation.md)

