---
title: "Grid OnRecordSelect event (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the grid OnRecordSelect event.
author: jasongre
ms.author: jasongre
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# Grid OnRecordSelect event (Client API reference)

The `OnRecordSelect` event occurs when a single row (record) is selected in the editable grid. This event won't occur if a user selects different cells in the same row, or selects multiple rows. 

## Example: Override the default open behavior in model-driven grids 
There might be situations where you don't want the table record to open (which is the default behavior), but want a custom action to be performed such as opening a URL using JavaScript functions. Here is an example to acheive this using the [Power Apps Grid Control](../../../../../maker/model-driven-apps/the-power-apps-grid-control) and the `OnRecordSelect` event. In this example it simply navigates to a specific contact form.

### Step 1: Create a web resource

Create, save and publish a JavaScript (JS) web resource that contains the following code. It automatically gets the entity name and entity ID from [execution context](power-apps/developer/model-driven-apps/clientapi/reference/execution-context).

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

More information: [Create or edit model-driven app web resources ](../../../../../maker/model-driven-apps/create-edit-web-resources.md)

### Step 2: Enable Power Apps Grid Control 
Follow these steps to enable the **Power Apps Grid Control** as the main grid (table view) or within a model-driven form subgrid.
- [Use as main grid](../../../../../maker/model-driven-apps/the-power-apps-grid-control#add-the-power-apps-grid-control-to-views-for-an-entity)
- [Use as subgrid](../../../../../maker/model-driven-apps/the-power-apps-grid-control#add-the-power-apps-grid-control-to-a-subgrid)


### Step 3: Register the custom behavior on OnRecordSelect Event
When enabling the **Power Apps Grid Control**, an **Events** tab appears. Select the **Events** tab:
  1. Under the **Form Libraries** section, add the Form Libary from the web resource just created.
  2. Under the **Event Handlers** section, select the event **OnRecordSelect** and click Add, a popup will appear.
  3. In the popup, select the form library just added and the Function name **Example.OnSelect**. This is the name of the JavaScript function created in the web resource, and make sure to check the option **Pass execution context as first parameter**.


For more infomation, see [Power Apps Grid Control](../../../../../maker/model-driven-apps/the-power-apps-grid-control)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
