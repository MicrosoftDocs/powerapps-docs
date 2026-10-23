---
title: "Page methods for generative pages"
description: "Learn how to use the dataApi page methods in generative pages."
ms.date: 10/19/2026
author: jasongre
ms.author: jasongre
ms.reviewer: jdaly
ms.topic: reference
search.audienceType: 
  - developer
contributors:
  - JimDaly
  - ruxyrezidenttm
ai-usage: ai-assisted
---
# Page methods for generative pages

Use the page methods of the `dataApi` object to control the generative page itself, such as returning a value when the page is used as a dialog. At this time, there is only one page method.

## `setPageOutput` method

Sets the value returned to the calling script when a generative page opened as a dialog closes. This method is available only in hosts that support returning values from generative page dialogs. It isn't part of the shared `dataApi` contract, so check that it exists before calling it.

### Parameters

|Name|Type|Description|
|---|---|---|
|`value`|unknown|The value to return to the script that opened the dialog. The value can be a primitive, object, or array.|

### Returns

No value.

### setPageOutput example

```typescript
dataApi.setPageOutput?.({
    action: "selected",
    recordId: selectedRecordId
});

const xrm = (window as any).Xrm;
await xrm.Navigation.navigateBack();
```

Calling `setPageOutput` doesn't close the dialog or update the calling page. Close the dialog with `Xrm.Navigation.navigateBack()`. The promise returned by `Xrm.Navigation.navigateTo` then resolves with an object whose `returnValue` property contains the most recently stored value. The calling script must explicitly apply the returned value to its form, grid, or other state.

This method applies to generative pages opened as dialogs. Generative pages opened inline or in an app side pane don't return a value to the calling script.
