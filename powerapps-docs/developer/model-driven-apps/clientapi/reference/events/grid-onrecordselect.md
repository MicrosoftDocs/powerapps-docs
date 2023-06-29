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

The `OnRecordSelect` event occurs when a single row (record) is selected in the editable grid. This event won't occur if a user selects different cells in the same row, or selects multiple rows.

## Example: Override the default open behavior in model-driven grids

There might be situations where you don't want the table record to open (which is the default behavior), but want a custom action to be performed such as opening a URL using JavaScript functions. Here is an example to achieve this using the [Power Apps grid control](../../../../../maker/model-driven-apps/the-power-apps-grid-control.md) and the `OnRecordSelect` event.

### Step 1: Create a web resource

Create, save and publish a JavaScript (JS) web resource that contains the following code:

```JavaScript
function OnSelect(context) {
   var pageInput = {
         pageType: "entityrecord",
         entityName: "contact",
         entityId: context.getFormContext().data.entity.getId()   
   };
   Xrm.Navigation.navigateTo(pageInput);
}
```

More information: [Create or edit model-driven app web resources](../../../../../maker/model-driven-apps/create-edit-web-resources.md)

### Step 2: Enable Power Apps Grid Control

Follow these steps to enable the **Power Apps Grid Control** as the main grid (table view) or within a model-driven form subgrid:

- [Use as main grid](../../../../../maker/model-driven-apps/the-power-apps-grid-control.md#add-the-power-apps-grid-control-to-views-for-an-entity)
- [Use as subgrid](../../../../../maker/model-driven-apps/the-power-apps-grid-control.md#add-the-power-apps-grid-control-to-a-subgrid)

### Step 3: Register the custom behavior on OnRecordSelect Event

When enabling the **Power Apps Grid Control**, an **Events** tab appears. Select the **Events** tab:

1. Under the **Form Libraries** section, add the Form Library from the web resource just created.
1. Under the **Event Handlers** section, select the event **OnRecordSelect** and click **Add**, a popup will appear.
1. In the popup, select the form library just added and the function name **OnSelect**. This is the name of the JavaScript function created in the web resource.


More information: [Power Apps grid control](../../../../../maker/model-driven-apps/the-power-apps-grid-control.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
