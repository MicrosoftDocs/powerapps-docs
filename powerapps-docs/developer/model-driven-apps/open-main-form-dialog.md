---
title: "Open Main Form in a Dialog by Using Client API"
description: "Learn how to open a main form in a dialog in model-driven apps by using the Xrm.Navigation.navigateTo method, with examples for new and existing records."
author: MitiJ
ms.author: mijosh
ms.date: 10/30/2026
ms.reviewer: jdaly
ms.topic: how-to
ms.subservice: mda-developer
ai-usage: ai-assisted
search.audienceType:
  - developer
contributors:
 - JimDaly
---

# Open main form in a dialog by using client API

To open the main form in a dialog by using client API, call the [Xrm.Navigation.navigateTo](./clientapi/reference/xrm-navigation/navigateto.md) method. The [Xrm.Navigation.navigateTo](./clientapi/reference/xrm-navigation/navigateto.md) API method opens the dialog with several options, including the size and position.

> [!NOTE]
> The [Xrm.Navigation.openForm](./clientapi/reference/xrm-navigation/openform.md) method doesn't support opening a main form as a dialog.

|Example|Demonstrates|
|---|---|
|[Open a new record](#open-a-new-record-example)|How to open a new account form in a centered dialog with a width of 50% of the window.|
|[Open an existing record](#open-an-existing-record-example)|How to open an existing account record in a centered dialog by specifying its ID.|
|[Open a new record on the side pane](#open-a-new-record-on-the-side-pane-example)|How to open a new account form in a right-side dialog with a width of 500 pixels.|
|[Open main form in a dialog with callback method](#open-main-form-in-a-dialog-with-callback-method-example)|How to run a callback after saving a new record and closing the dialog, and access the saved record's ID and name.|

## Open a new record example

In this example, the dialog opens a new account form for creating a new record. The dialog pops up in the center by using up to 50% of the available window as a modal on top of the form it was invoked or called from.

```JavaScript
var pageInput = {
    pageType: "entityrecord",
    entityName: "account",
    formType: 2,
};
var navigationOptions = {
    target: 2,
    width: {value: 50, unit:"%"},
    position: 1
};
Xrm.Navigation.navigateTo(pageInput, navigationOptions);
```

:::image type="content" source="media/open-new-record-mfd.png" alt-text="Screenshot of a new account form opened in a centered modal dialog in a model-driven app.":::

## Open an existing record example

In this example, the dialog opens an existing account record by using the account ID value over the contact form. Replace the ID with any record ID value to open the record in the dialog.

```JavaScript
var pageInput = {
    pageType: "entityrecord",
    entityName: "account",
    formType: 2,
    entityId: "00aa00aa-bb11-cc22-dd33-44ee44ee44ee" //replace with actual ID
};
var navigationOptions = {
    target: 2,
    width: {value: 80, unit:"%"},
    position: 1
};
Xrm.Navigation.navigateTo(pageInput, navigationOptions);
```

:::image type="content" source="media/open-existing-record-mfd.png" alt-text="Screenshot of an existing account record opened in a modal dialog over the contact form.":::

## Open a new record on the side pane example

In this example, the dialog opens a new record in the right corner of the window. You can achieve this behavior by using the pixel options.

```JavaScript
var pageInput = {
    pageType: "entityrecord",
    entityName: "account",
    formType: 2,
};
var navigationOptions = {
    target: 2,
    width: {value: 500, unit:"px"},
    position: 2
};
Xrm.Navigation.navigateTo(pageInput, navigationOptions);
```

:::image type="content" source="media/open-record-side-pane-mfd.png" alt-text="Screenshot of a new account form opened in a side pane dialog on the right of the window.":::

## Open main form in a dialog with callback method example

This example shows how to invoke a main form dialog with a callback method after saving a record and closing the dialog.

```Javascript
var pageInput = {
    pageType: "entityrecord",
    entityName: "account",
    formType: 2
};
var navigationOptions = {
    target: 2,
    width: {value: 80, unit:"%"},
    position: 2
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

## Related content

[Create and design forms](../../maker/model-driven-apps/create-design-forms.md)  
[Customize forms in model-driven apps](customize-entity-forms.md)  
[Xrm.Navigation.navigateTo](./clientapi/reference/xrm-navigation/navigateto.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
