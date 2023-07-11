---
title: "Grid OnRecordSelect event (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the grid OnRecordSelect event.
author: jasongre
ms.author: jasongre
ms.date: 06/29/2023
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
  - ericregnier
---
# Grid OnRecordSelect event (Client API reference)

The `OnRecordSelect` event occurs when a single row (record) is selected in an editable grid. This event doesn't occur if a user selects different cells in the same row, or selects multiple rows.

## Example: Override the default open behavior in model-driven grids

When you want to customize the way that a table record opens from the [Power Apps grid control](../../../../../maker/model-driven-apps/the-power-apps-grid-control.md), you can control how this opens with a JavaScript function associated with the grid `OnRecordSelect` event.

The following example ensures that the record opens using the form specified by the `pageInput` `formId` value using the [Xrm.Navigation.navigateTo](../Xrm-Navigation/navigateTo.md) method. In this example, the form and grid must belong to the same entity.

### Step 1: Create a web resource

Create, save, and publish a JavaScript (JS) web resource that contains the following code:

```JavaScript
var Example = window.Example || {};
(function () {
this.OnSelect = function (executionContext) {
   var pageInput = {
      pageType: "entityrecord",
      entityName: executionContext.getEventSource().getEntityName(),
      entityId: executionContext.getEventSource().getId(),
      formId: "420786E3-D342-4A9A-914B-AA331FF2D25E"    
   };
   Xrm.Navigation.navigateTo(pageInput);
}
}).call(Example);
```

More information: [Create or edit model-driven app web resources](../../../../../maker/model-driven-apps/create-edit-web-resources.md)

### Step 2: Enable Power Apps Grid Control

Follow these steps to enable the **Power Apps grid control** as the main grid (table view) or within a model-driven form subgrid:

- [Use as main grid](../../../../../maker/model-driven-apps/the-power-apps-grid-control.md#add-the-power-apps-grid-control-to-views-for-an-entity)
- [Use as subgrid](../../../../../maker/model-driven-apps/the-power-apps-grid-control.md#add-the-power-apps-grid-control-to-a-subgrid)

### Step 3: Register the custom behavior on OnRecordSelect Event

When you enable the **Power Apps grid control**, an **Events** tab appears. Select the **Events** tab:

1. Under the **Form Libraries** section, add the Form Library from the web resource created.
1. Under the **Event Handlers** section, select the event **OnRecordSelect** and select **Add** and a popup appears.
1. In the popup, select the form library just added and the function name `Example.OnSelect`. This is the name of the JavaScript function created in the web resource. Make sure to check the option **Pass execution context as first parameter**.

More information: [Power Apps grid control](../../../../../maker/model-driven-apps/the-power-apps-grid-control.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
