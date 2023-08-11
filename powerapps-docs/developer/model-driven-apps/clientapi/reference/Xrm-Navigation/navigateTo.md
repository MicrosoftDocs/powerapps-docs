---
title: "navigateTo (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the navigateTo method.
author: adrianorth
ms.author: aorth
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# navigateTo (Client API reference)

[!INCLUDE[./includes/navigateTo-description.md](./includes/navigateTo-description.md)]

> [!NOTE]
> This method is supported only on Unified Interface.

## Syntax

`Xrm.Navigation.navigateTo(pageInput,navigationOptions).then(successCallback,errorCallback);`

## Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| [pageInput](#pageinput-parameter) | Object | Yes | Input about the page to navigate to. The object definition changes depending on the type of page to navigate to: [entity list](#entity-list), [entity record](#entity-record), [dashboard](#dashboard), [HTML web resource](#html-web-resource), or [custom page](#custom-page). |
| [navigationOptions](#navigationoptions-parameter) | Object | No | Options for navigating to a page: whether to open inline or in a dialog. If you don't specify this parameter, page is opened inline by default. |
| successCallback | function | No | A function to execute on successful navigation to the page when navigating inline and on closing the dialog when navigating to a dialog. |
| errorCallback | Function | No | A function to execute when the operation fails. |

### pageInput parameter

#### Entity list

The entity list object contains the following values.

| Name | Type | Description |
| --- | --- | --- |
| pageType | String | Specify "entitylist". |
| entityName | String | The logical name of the table to load in the list control. |
| viewId | String | (Optional) The ID of the view to load. If you don't specify it, navigates to the default main view for the table. |
| viewType | String | (Optional) Type of view to load. Specify "savedquery" or "userquery". |

#### Entity record

The entity record object contains the following values.

| Name | Type | Description |
| --- | --- | --- |
| pageType | String | Specify "entityrecord". |
| entityName | String | Logical name of the table to display the form for. |
| entityId | String | (Optional) ID of the table record to display the form for. If you don't specify this value, the form will be opened in create mode. |
| createFromEntity | Lookup | (Optional) Designates a record that will provide default values based on mapped column values. The lookup object has the following String properties: entityType, id, and name (optional). |
| data | Object | (Optional) A dictionary object that passes extra parameters to the form. <p/> The parameters can be table columns with default values that are set on new forms (see [Set column values using parameters passed to a form](/powerapps/developer/model-driven-apps/set-field-values-using-parameters-passed-form)), or custom parameters that are accessed on the form using `formContext.data.attributes` (see [Configure a form to accept custom querystring parameters](/powerapps/developer/model-driven-apps/configure-form-accept-custom-querystring-parameters), and [formContext.data](/powerapps/developer/model-driven-apps/clientapi/reference/formcontext-data)). Invalid parameters will cause an error. |
| formId | String | (Optional) ID of the form instance to be displayed. |
| isCrossEntityNavigate | Boolean | (Optional) Indicates whether the form is navigated to from a different table using cross-table business process flow. |
| isOfflineSyncError | Boolean | (Optional) Indicates whether there are any offline sync errors. |
| processId | String | (Optional) ID of the business process to be displayed on the form. |
| processInstanceId |  String | (Optional) ID of the business process instance to be displayed on the form. |
| [relationship](#relationship-object) | Object | (Optional) Define a relationship object to display the related records on the form. |
| selectedStageId | String | (Optional) ID of the selected stage in business process instance. |
| tabName | String | (Optional) Sets the focus on the tab of the form. |

##### Relationship object

The relationship object, used in the [Entity record](#entity-record), contains the following values.

| Name | Type | Description |
| --- | --- | --- |
| attributeName   | String | Name of the column used for relationship. |
| name | String | Name of the relationship. |
| navigationPropertyName | String | Name of the navigation property for this relationship. |
| relationshipType | Number | Relationship type. Specify one of the following values: *0*:OneToMany, *1*:ManyToMany. |
| roleType | Number | Role type in relationship. Specify one of the following values: *1*:Referencing, *2*:AssociationEntity. |

#### Dashboard

The dashboard object contains the following values.

| Name | Type | Description |
| --- | --- | --- |
| pageType | String | Specify "dashboard". |
| dashboardId | String | The ID of the dashboard to load. If you don't specify the ID, navigates to the default dashboard. |

#### HTML web resource

The HTML web resource object contains the following values.

| Name | Type | Description |
| --- | --- | --- |
| pageType | String | Specify "webresource". |
| webresourceName | String | The name of the web resource to load. |
| data | String | (Optional) The data to pass to the web resource. |

#### Custom page

The Custom page object contains the following values.

| Name | Type | Description |
| --- | --- | --- |
| pageType | String | Specify "custom". |
| name | String | The logical name of the custom page to open. |
| entityName | String | (Optional) The logical name of the table to be made available in the custom page via Param("entityName"). |
| recordId | String | (Optional) ID of the table record to be made available in the custom page via Param("recordId"). |

### navigationOptions parameter

The navigationOptions object contains the following values.

| Name | Type | Description |
| --- | --- | --- |
| target | Number | Specify 1 to open the page inline; 2 to open the page in a dialog. Also, rest of the values (width, height, and position) are valid only if you have specified 2 in this value (open page in a dialog).<p/>Note: Entity lists can only be opened inline; entity records and web resources can be opened either inline or in a dialog. |
| width | Number or Object | (Optional) The width of dialog. To specify the width in pixels, just type a numeric value. To specify the width in percentage, specify an object of type SizeValue with the following properties:<ul><li>value: The numerical value of type Number.<li>unit: The unit of measurement of type String. Specify "%" or "px". Default value is "px".</ul> |
| height | Number or Object | (Optional) The height of dialog. To specify the height in pixels, just type a numeric value. To specify the width in percentage, specify an object of type SizeValue with the following properties:<ul><li>value: The numerical value of type Number.<li>unit: The unit of measurement of type String. Specify "%" or "px". Default value is "px".</ul> |
| position | Number | (Optional) Specify 1 to open the dialog in center; 2 to open the dialog on the far side. Default is 1 (center). |
| title | String | (Optional) The dialog title on top of the center or side dialog. |

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

[Navigating to and from a custom page (preview)](../../navigate-to-custom-page-examples.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
