---
title: "Navigate to and from a Custom Page Using Client API" 
description: "Learn how to navigate to custom pages in model-driven apps using client API. Discover step-by-step examples for full-page, dialog, and pane navigation methods."
author: sriharibs-msft
ms.author: srihas
ms.date: 03/27/2026
ms.reviewer: jdaly
ms.subservice: mda-developer
ms.topic: "how-to"
search.audienceType: 
  - maker
  - developer
contributors: 
  - JimDaly
  - caburk
---

# Navigate to a custom page using client API

This article provides examples of navigating from a model-driven app page to a custom page using [Client API](../client-scripting.md). Learn how to open custom pages as full-page, dialog, or pane views in model-driven apps.

This article outlines the steps to use client API to open a custom page as a full-page, dialog, or pane. It provides examples of **custom** as a `pageType` value in [navigateTo (Client API reference)](reference/xrm-navigation/navigateto.md).

> [!IMPORTANT]
> Custom pages are a new feature with significant product changes. They currently have a number of known limitations outlined in [Custom Page Known Issues](../../../maker/model-driven-apps/model-app-page-issues.md).

## Find the logical name

Each of the following client API examples takes the logical name of the custom page as the required parameter. The logical name is the **Name** value of the page in the solution explorer. 

:::image type="content" source="../../../maker/model-driven-apps/media/navigate-page-examples/find-page-logical-name.png" alt-text="Find page logical name." lightbox="../../../maker/model-driven-apps/media/navigate-page-examples/find-page-logical-name.png":::

## Open as an inline full page without context

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

## Open as an inline full page with a record context

This example uses the `recordId` parameter within the [NavigateTo](reference/Xrm-Navigation/navigateTo.md) function to provide the custom page with the record to use.  

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

The `Param` function within the custom page retrieves the value and uses the Lookup function to retrieve the record.

```powerappsfl
App.OnStart=Set(RecordItem, 
    If(IsBlank(Param("recordId")),
        First(<entity>),
        LookUp(<entity>, <entityIdField> = GUID(Param("recordId"))))
    )
```

> [!IMPORTANT]
> The `recordId` parameter must be a GUID because it updates the URL and an app start from the URL validates the `recordId` is a GUID. 

## Open as a centered dialog

Within a model-driven app client API event handler, call the following code and update the **name** parameter to be the logical name of the custom page.  This mode supports the sizing parameters similar to the [Main form dialogs](../../../developer/model-driven-apps/customize-entity-forms.md#open-main-form-in-a-dialog-by-using-client-api).

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

## Open as a side dialog

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

## Open from a grid primary field link as a full page with record ID

This example uses the `recordId` parameter within the [navigateTo](reference/Xrm-Navigation/navigateTo.md) function to provide the custom page with the record to use. The `Param` function within the custom page retrieves the value and uses the `Lookup` function to retrieve the record.

You can find a more complete example at [Override the default open behavior of data rows in an entity-bound grid](../override-default-open-behavior-grids.md).

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

1. Customize the table ribbon **CommandDefinition** for **OpenRecordItem** to call the function earlier and include the **CrmParameter** with the value **SelectedControlSelectedItemReferences**.

    ```xml
        <CommandDefinition Id="Mscrm.OpenRecordItem">
            <Actions>
                <JavaScriptFunction FunctionName="run" Library="$webresource:cr62c_OpenCustomPage">
                    <CrmParameter Value="SelectedControlSelectedItemReferences" />
                </JavaScriptFunction>
            </Actions>
        </CommandDefinition>
    ```

1. In the custom page, override the **App**'s **OnStart** property to use the `Param` function to get the `recordId` and `lookup` record.

    ```powerappsfl
    App.OnStart=Set(RecordItem, 
        If(IsBlank(Param("recordId")),
            First(<entity>),
            LookUp(<entity>, <entityIdField> = GUID(Param("recordId"))))
        )
    ```

    > [!NOTE]
    > After changing the `OnStart` property, you need to run `OnStart` from the App context menu. This function performs only once within a session.

1. Then, the custom page can use the **RecordItem** parameter as a record. The following example shows how to use it in an [EditForm](../../../maker/canvas-apps/functions/function-form.md).

    ```powerappsfl
    EditForm.Datasource=<datasource name>
    EditForm.Item=RecordItem
    ```

## Open from a selected record in editable grid as a centered dialog with record ID

Use an editable grid to trigger the [OnRecordSelect](reference/events/grid-onrecordselect.md) event when you want to perform an action after selecting a particular record in a view. This example uses the `recordId` parameter within the [navigateTo](reference/Xrm-Navigation/navigateTo.md) function to provide the custom page with the record to use. The `getId` method in the [GridEntity](reference/grids/gridentity.md) object retrieves the record ID. The `Param` function within the custom page retrieves the value and uses the `lookup` function to retrieve the record. 

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

1. In the custom page, override the **App**'s **OnStart** property to use the `Param` function to get the `recordId` and `lookup` record.

    ```powerappsfl
    App.OnStart=Set(RecordItem, 
        If(IsBlank(Param("recordId")),
            First(<entity>),
            LookUp(<entity>, <entityIdField> = GUID(Param("recordId"))))
        )
    ```

    > [!NOTE]
    > After changing the `OnStart` property, you need to run `OnStart` from the App context menu. This function performs only once within a session.

1. Then, the custom page can use the **RecordItem** parameter as a record. The following example shows how to use it in an [EditForm](../../../maker/canvas-apps/functions/function-form.md).

    ```powerappsfl
    EditForm.Datasource=<datasource name>
    EditForm.Item=RecordItem
    ```

### Related articles

[Model-driven app custom page overview](../../../maker/model-driven-apps/model-app-page-overview.md)   
[Add a custom page to your model-driven app](../../../maker/model-driven-apps/add-page-to-model-app.md)   
[navigateTo (client API reference)](reference/xrm-navigation/navigateto.md)

