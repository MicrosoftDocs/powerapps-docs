---
title: "Navigating to and from a custom page in your model-driven app using client API" 
description: "This article provides examples of navigating from a model-driven app page using the client API to a custom page."
ms.date: 08/17/2021
ms.reviewer: ""
ms.service: powerapps
ms.subservice: mda-developer
ms.topic: "how-to"
author: "aorth"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - maker
  - developer
search.app: 
  - "PowerApps"
  - D365CE
---

# Navigating to and from a custom page using client API

This article provides examples of navigating from a model-driven app page to a custom page using [Client API](../client-scripting.md).

This article outlines the steps to use client API to open a custom page as a full-page, dialog, or pane.  It provides examples of **custom** as a `pageType` value in [navigateTo (Client API reference)](reference/xrm-navigation/navigateto.md).

> [!IMPORTANT]
> - The base functionality of custom pages has moved to General Availability in all regions.  However there are some specific or new capabilities that are still in public preview and are marked with _(preview)_.
> - [!INCLUDE[cc_preview_features_definition](../../../includes/cc-preview-features-definition.md)] 

## Navigating from a model page to a custom page

### Finding the logical name

Each of the following client API examples takes the logical name of the custom page as the required parameter. The logical name is the **Name** value of the page in the solution explorer. 

:::image type="content" source="../../../maker/model-driven-apps/media/navigate-page-examples/find-page-logical-name.png" alt-text="Find page logical name." lightbox="../../../maker/model-driven-apps/media/navigate-page-examples/find-page-logical-name.png":::

### Open as an inline full page without context

Within a model-driven app client API event handler, call the following code and update the **name** parameter to be the logical name of the page.

```javascript
// Inline Page
var pageInput = {
    pageType: "custom",
    name: "<logical name of the custom page>",
};
var navigationOptions = {
    target: 1
};
Xrm.Navigation.navigateTo(pageInput, navigationOptions)
    .then(
        function () {
            // Called when page opens
        }
    ).catch(
        function (error) {
            // Handle error
        }
    );
```

### Open as an inline full page with a record context

This example uses the `recordId` parameter within the [NavigateTo](reference/Xrm-Navigation/navigateTo.md) function to provide the custom page with the record to use.  The `Param` function within the custom page retrieves the value and uses the Lookup function to retrieve the record.

```javascript
// Inline Page
var pageInput = {
    pageType: "custom",
    name: "<logical name of the custom page>",
    entityName: "<logical name of the table>",
    recordId: "<record id>",
};
var navigationOptions = {
    target: 1
};
Xrm.Navigation.navigateTo(pageInput, navigationOptions)
    .then(
        function () {
            // Called when page opens
        }
    ).catch(
        function (error) {
            // Handle error
        }
    );
```

### Open as a centered dialog

Within a model-driven app client API event handler, call the following code and update the **name** parameter to be the logical name of the custom page.  This mode supports the sizing parameters similar to the [Main form dialogs](../../../developer/model-driven-apps/customize-entity-forms.md#open-main-form-in-a-dialog-using-client-api).

```javascript
// Centered Dialog
var pageInput = {
    pageType: "custom",
    name: "<logical custom page name>",
};
var navigationOptions = {
    target: 2, 
    position: 1,
    width: {value: 50, unit:"%"},
    title: "<dialog title>"
};
Xrm.Navigation.navigateTo(pageInput, navigationOptions)
    .then(
        function () {
            // Called when the dialog closes
        }
    ).catch(
        function (error) {
            // Handle error
        }
    );
```

### Open as a side dialog

Within a model-driven app client API event handler, call the following code and update the **name** parameter to be the logical name of the custom page.

```javascript
// Side Dialog
var pageInput = {
    pageType: "custom",
    name: "<logical page name>",
};
var navigationOptions = {
    target: 2, 
    position: 2,
    width: {value: 500, unit: "px"},
    title: "<dialog title>"
};
Xrm.Navigation.navigateTo(pageInput, navigationOptions)
    .then(
        function () {
            // Called when the dialog closes
        }
    ).catch(
        function (error) {
            // Handle error
        }
    );
```

### Open from a grid primary field link as a full page with record ID

This example uses the `recordId` parameter within the [navigateTo](reference/Xrm-Navigation/navigateTo.md) function to provide the custom page with the record to use.  The `Param` function within the custom page retrieves the value and uses the Lookup function to retrieve the record.

1. Create a web resource of type **JScript** and update the **name** parameter to be the logical page name. Add the following code to the web resource.

    ```javascript
    function run(selectedItems)
    {
        let selectedItem = selectedItems[0];
        
        if (selectedItem) {     
            let pageInput = {
                pageType: "custom",
                name: "<logical page name>",
                entityName: selectedItem.TypeName,
                recordId: selectedItem.Id,
            };
            let navigationOptions = {
                target: 1
            };
            Xrm.Navigation.navigateTo(pageInput, navigationOptions)
                .then(
                    function () {
                        // Handle success
                    }
                ).catch(
                    function (error) {
                        // Handle error
                    }
                );
        }
    }
    ```

1. Customize the table ribbon **CommandDefinition** for **OpenRecordItem** to call the function above and include the **CrmParameter** with the value **SelectedControlSelectedItemReferences**.

    ```xml
        <JavaScriptFunction FunctionName="run" Library="$webresource:cr62c_OpenCustomPage">
            <CrmParameter Value="SelectedControlSelectedItemReferences" />
        </JavaScriptFunction>
    ```

1. In the custom page, override the **App**'s **OnStart** property to use the `Param` function to get the `recordId` and lookup record.

    ```powerappsfl
    App.OnStart=Set(RecordItem, 
        If(IsBlank(Param("recordId")),
            First(<entity>),
            LookUp(<entity>, <entityIdField> = GUID(Param("recordId"))))
        )
    ```

    > [!NOTE]
    > After changing the `OnStart` property, you'll need to run `OnStart` from the App context menu. This function performs only once within a session.

1. Then, the custom page can use the **RecordItem** parameter as a record. Below is an example on how to use it in an [EditForm](../../../maker/canvas-apps/functions/function-form.md).

    ```powerappsfl
    EditForm.Datasource=<datasource name>
    EditForm.Item=RecordItem
    ```

### Open from a selected record in editable grid as a centered dialog with record ID

Editable grid can be used to trigger [OnRecordSelect](reference/events/grid-onrecordselect.md) event for scenarios where you want to perform an action when a particular record is selected in a view. This example uses the `recordId` parameter within the [navigateTo](reference/Xrm-Navigation/navigateTo.md) function to provide the custom page with the record to use. The record ID is retrieved using the `getId` method in [GridEntity](reference/grids/gridentity.md) object. The `Param` function within the custom page retrieves the value and uses the lookup function to retrieve the record. 

1. [Enable editable grid](../../../developer/model-driven-apps/use-editable-grids.md) control in the table.

1. Create a web resource of type **JScript** and update the **name** parameter to be the logical page name. Add the following code to the web resource.

    ```javascript
    function RunOnSelected(executionContext) {
    // Retrieves the record selected in the editable grid
    var selectedRecord = executionContext.getFormContext().data.entity;
    var Id = selectedRecord.getId().replace(/[{}]/g, ""); 

    // Centered Dialog
    var pageInput = {
        pageType: "custom",
        name: "<logical page name>",
        recordId: Id,
    };
    var navigationOptions = {
        target: 2,
        position: 1,
        width: { value: 50, unit: "%" },
        title: "<dialog title>"
    };
    Xrm.Navigation.navigateTo(pageInput, navigationOptions)
        .then(
            function () {
                // Called when the dialog closes
            }
        ).catch(
            function (error) {
                // Handle error
            }
        );
     }
    ```

1. In the custom page, override the **App**'s **OnStart** property to use the `Param` function to get the `recordId` and lookup record.

    ```powerappsfl
    App.OnStart=Set(RecordItem, 
        If(IsBlank(Param("recordId")),
            First(<entity>),
            LookUp(<entity>, <entityIdField> = GUID(Param("recordId"))))
        )
    ```

    > [!NOTE]
    > After changing the `OnStart` property, you'll need to run `OnStart` from the App context menu. This function performs only once within a session.

1. Then, the custom page can use the **RecordItem** parameter as a record. Below is how to use it in an [EditForm](../../../maker/canvas-apps/functions/function-form.md).

    ```powerappsfl
    EditForm.Datasource=<datasource name>
    EditForm.Item=RecordItem
    ```

## Related articles

[Model-driven app custom page overview](../../../maker/model-driven-apps/model-app-page-overview.md)

[Add a custom page to your model-driven app](../../../maker/model-driven-apps/add-page-to-model-app.md)

[navigateTo (client API reference)](reference/xrm-navigation/navigateto.md)

