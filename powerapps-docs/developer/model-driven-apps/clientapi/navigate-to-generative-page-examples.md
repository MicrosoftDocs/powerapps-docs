---
title: Navigate to and from a generative page using client API
description: "Learn how to use client API to navigate to and from generative pages in model-driven apps. Explore inline, dialog, and side dialog examples with input parameters like record IDs and custom data."
author: jasongre
ms.author: jasongre
ms.reviewer: jdaly
ms.date: 04/09/2026
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

This article provides examples of navigating to generative pages in model-driven apps by using the client API [navigateTo](reference/Xrm-Navigation/navigateTo.md) method. Learn how to open generative pages inline or in a dialog, and how to pass input parameters such as a record ID or custom data.

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
        function () {
            // Called when the dialog closes
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
        function () {
            // Called when the dialog closes
        }
    ).catch(
        function (error) {
            // Handle error
        }
    );
```

## Unsupported: Open a generative page in a side pane

> [!IMPORTANT]
> Opening a generative page by using `Xrm.App.sidePanes.createPane()` isn't currently supported. 
>
> ```javascript
> // Not supported — page content doesn't render
> const pane = await Xrm.App.sidePanes.createPane({
>     title: "My Generative Page",
>     paneId: "GenPage",
>     canClose: false,
>     width: 400
> });
> pane.navigate({ pageType: "generative", pageId: "<genPageID>" });
> ```
>
> Use a centered or side dialog via `Xrm.Navigation.navigateTo` instead.

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
