---
title: Navigate to and from a generative page using client API
description: "Learn how to navigate to and from generative pages in model-driven apps. Explore inline, dialog, and side pane examples, pass input parameters, and return values from dialogs."
author: jasongre
ms.author: jasongre
ms.reviewer: jdaly
ms.date: 10/09/2026
ms.topic: how-to
ms.subservice: mda-developer
applies_to:
  - PowerApps
search.audienceType:
  - developer
ms.collection:
  - bap-ai-copilot
---

# Navigate to and from a generative page using client API

This article provides examples of navigating to generative pages in model-driven apps by using client APIs. Learn how to open generative pages inline, in a dialog, or in an app side pane; pass input parameters such as a record ID or custom data; and return values from a dialog to the calling script.

> [!NOTE]
> This method is supported only on Unified Interface.

## Find the page ID

Each of the following examples requires the ID of the target generative page. To find the page ID:

1. Open the model-driven app containing the generative page in the app designer.
1. Select the generative page in the pages list.
1. In the properties pane, copy the GUID shown in the **Generative page** field.

## Open a generative page inline without parameters

Opens a generative page as a full-page inline view with no input parameters.

```javascript
var pageInput = {
    pageType: "generative",
    pageId: "<genPageID>"
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

## Open a generative page inline with record context

Passes a `recordId` and `entityName` to the generative page so the page can load and display a specific record. The target generative page must be [set up to accept these parameters](../../../maker/model-driven-apps/generative-pages.md#set-up-a-page-to-accept-input-parameters).

```javascript
var pageInput = {
    pageType: "generative",
    pageId: "<genPageID>",
    entityName: "account",
    recordId: "00aa00aa-bb11-cc22-dd33-44ee44ee44ee" // replace with actual record GUID
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

## Open a generative page inline with custom data

Passes a `data` object containing custom key-value pairs to the generative page. The target generative page must be [set up to accept these parameters](../../../maker/model-driven-apps/generative-pages.md#set-up-a-page-to-accept-input-parameters).

```javascript
var pageInput = {
    pageType: "generative",
    pageId: "<genPageID>",
    data: { status: "active", category: "premium" }
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

## Open a generative page as a centered dialog

Opens a generative page in a centered dialog, passing both record context and custom data. Adjust `width` and `height` as needed.

```javascript
var pageInput = {
    pageType: "generative",
    pageId: "<genPageID>",
    entityName: "account",
    recordId: "00aa00aa-bb11-cc22-dd33-44ee44ee44ee", // replace with actual record GUID
    data: { view: "summary" }
};
var navigationOptions = {
    target: 2,
    position: 1,
    width: { value: 70, unit: "%" },
    height: { value: 80, unit: "%" },
    title: "<dialog title>"
};
Xrm.Navigation.navigateTo(pageInput, navigationOptions)
    .then(
        function (result) {
            // Called when the dialog closes.
            // result.returnValue contains the value set by dataApi.setPageOutput.
        }
    ).catch(
        function (error) {
            // Handle error
        }
    );
```

## Open a generative page as a side dialog

Opens a generative page as a side dialog using `position: 2`.

```javascript
var pageInput = {
    pageType: "generative",
    pageId: "<genPageID>"
};
var navigationOptions = {
    target: 2,
    position: 2,
    width: { value: 500, unit: "px" },
    title: "<dialog title>"
};
Xrm.Navigation.navigateTo(pageInput, navigationOptions)
    .then(
        function (result) {
            // Called when the dialog closes.
            // result.returnValue contains the value set by dataApi.setPageOutput.
        }
    ).catch(
        function (error) {
            // Handle error
        }
    );
```

## Open a generative page in a side pane

Use `Xrm.App.sidePanes.createPane()` to create an app side pane, and then use the pane's `navigate` method to display a generative page.

```javascript
const pane = await Xrm.App.sidePanes.createPane({
    title: "My Generative Page",
    paneId: "GenPage",
    canClose: true,
    width: 400
});

await pane.navigate({
    pageType: "generative",
    pageId: "<genPageID>",
    entityName: "account",
    recordId: "00aa00aa-bb11-cc22-dd33-44ee44ee44ee",
    data: { view: "summary" }
});
```

In the target generative page, read these inputs from `pageInput.entityName`, `pageInput.recordId`, and `pageInput.data`.

The calling script captures the inputs when you call `pane.navigate`. Changing the selected record in the calling page doesn't automatically update an open generative page. To update the side pane, call `pane.navigate` again with the new input values.

A side pane remains open independently of the calling script. Returning a value through a `navigateTo` promise is supported for dialogs, but not for app side panes.

## Return a value from a generative page dialog

A generative page opened as a dialog can return a value to the script that opened it. In the generated page, call `dataApi.setPageOutput(value)` before closing the dialog with `Xrm.Navigation.navigateBack()`.

For example, the generative page can return a selected record:

```typescript
async function handleSelection(accountId: string, accountName: string): Promise<void> {
    dataApi.setPageOutput({
        action: "selected",
        accountId,
        accountName
    });

    const xrm = (window as any).Xrm;
    await xrm.Navigation.navigateBack();
}
```

`setPageOutput` stores the value but doesn't close the dialog or update the calling page. When the dialog closes, the promise returned by `Xrm.Navigation.navigateTo` resolves with an object whose `returnValue` property contains the most recently stored value. If the page doesn't set an output value, closing the dialog by selecting **Cancel** or the close button results in an undefined `returnValue`.

The calling script can process the result:

```javascript
const result = await Xrm.Navigation.navigateTo(
    {
        pageType: "generative",
        pageId: "<genPageID>"
    },
    {
        target: 2,
        position: 1,
        width: { value: 70, unit: "%" },
        height: { value: 80, unit: "%" },
        title: "Select an account"
    }
);

const output = result?.returnValue;
if (
    output &&
    typeof output === "object" &&
    output.action === "selected" &&
    typeof output.accountId === "string" &&
    typeof output.accountName === "string"
) {
    console.log("Selected account: " + output.accountName);
}
```

### Use the returned value in form scripting

A form script can access the returned value and use it to update the current form. Returning a record from the dialog doesn't automatically change form values or the selected row in a grid. The calling script must explicitly apply the returned value.

```javascript
async function openAccountSelector(executionContext) {
    const formContext = executionContext.getFormContext();

    const result = await Xrm.Navigation.navigateTo(
        {
            pageType: "generative",
            pageId: "<genPageID>"
        },
        {
            target: 2,
            position: 1,
            width: { value: 70, unit: "%" },
            height: { value: 80, unit: "%" }
        }
    );

    const output = result?.returnValue;
    if (
        output &&
        typeof output === "object" &&
        output.action === "selected" &&
        typeof output.accountId === "string" &&
        typeof output.accountName === "string"
    ) {
        const attribute = formContext.getAttribute("new_selectedaccountid");
        attribute?.setValue([
            {
                id: output.accountId,
                name: output.accountName,
                entityType: "account"
            }
        ]);

        // Call attribute.fireOnChange() if form logic must respond
        // immediately to this programmatic update.
    }
}
```

## Navigate from within a generative page using client API

When you navigate from inside a generative page component, use `(window as any).Xrm` to access the Xrm object, since the React component scope doesn't provide direct access to it.

### Navigate to another generative page with record context and custom data

```typescript
const xrm = (window as any).Xrm;
xrm.Navigation.navigateTo({
    pageType: "generative",
    pageId: targetPageId,
    entityName: "account",
    recordId: selectedRecordId,
    data: { view: "summary" }
});
```

> [!NOTE]
> When you navigate within model-driven apps, avoid constructing raw URLs or manipulating `window.location`.

## Navigate to a generative page via URL (external callers only)

You can navigate to a generative page by constructing a URL with the following structure:

```
https://<your-org>.crm.dynamics.com/main.aspx?appid={app-id}&pagetype=genux&id={page-id}&recordid={recordId}&entityname={entityName}&data={encoded-json}
```

You must URL-encode the `data` parameter as JSON. For example, to pass a custom filter object:

```
https://<your-org>.crm.dynamics.com/main.aspx?appid={app-id}&pagetype=genux&id={page-id}&data=%7B%22status%22%3A%22active%22%7D
```

You must [set up the target generative page to accept these parameters](../../../maker/model-driven-apps/generative-pages.md#set-up-a-page-to-accept-input-parameters).

## Related articles

- [Generate a page using natural language](../../../maker/model-driven-apps/generative-pages.md)
- [navigateTo (Client API reference)](reference/Xrm-Navigation/navigateTo.md)
