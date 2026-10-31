---
title: "Events in Forms and Grids in Model-Driven Apps"
description: Learn how to add or remove JavaScript event handlers for events in forms and grids in model-driven apps by using the UI or Client API methods.
author: MitiJ
ms.author: mijosh
ms.date: 10/30/2026
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - caburk
---
# Events in forms and grids in model-driven apps

Events in forms and grids initiate all client-side code in model-driven apps. You associate a specific function in a JavaScript library ([Script web resource](../script-jscript-web-resources.md)) to be executed when an event occurs. This function is called an *event handler*. Each event handler specifies a single function within a JavaScript library and any parameters that can be passed to the function.

You can associate event handlers to only some events by using the UI. For events that you can't associate through the UI, Client API provides methods that you can use to attach event handlers. 

[!INCLUDE[cc-terminology](../../data-platform/includes/cc-terminology.md)]

## Add or remove event handler functions in forms by using the UI



### [Unified Interface](#tab/add-event-handlers-unified-interface)

To add or remove event handler functions for events in the new Unified Interface:

1. Go to [Power Apps](https://make.powerapps.com).
1. In the left navigation pane, select **Data** and then select **Tables**. 
1. From the list of tables, select the table where you want to add the event handlers.
1. Select the **Forms** tab from the command bar and then select the form where you want to add the event handler.

    :::image type="content" source="../media/select-form-from-list.png" alt-text="Screenshot of the Forms tab showing the list of forms for a table in Power Apps.":::

1. Select the **Events** tab. You see both the **On Save** and **On Load** event handlers.

    :::image type="content" source="../media/form-event-handlers.png" alt-text="Screenshot of the Events tab showing the On Save and On Load form event handlers.":::

1. To add an event handler for the change event, select the column and then select the **Event** tab.

     :::image type="content" source="../media/onchange-event-handler.png" alt-text="Screenshot of the column Events tab showing the On Change event handler settings.":::

### [Legacy](#tab/add-event-handlers-legacy)

Use the **Event Handlers** section of the **Form Properties** dialog box to associate your script with an event for forms and columns.

:::image type="content" source="../media/Form-EventHandlers.png" alt-text="Screenshot of the Event Handlers section in the legacy Form Properties dialog box.":::

---

### Bulk edit forms

By default, event handlers don't run when a form is in bulk edit mode. 

To enable an event handler in bulk edit mode, modify the Form XML by finding the relevant `event` element and creating or setting the `BehaviorInBulkEditForm` attribute to `Enabled`. Currently, this behavior is supported only for [OnLoad events](reference/events/form-onload.md).

For more information about Form XML customization, see [When to edit the customizations file](../when-edit-customization-file.md), [Customize forms](../customize-entity-forms.md), and the [Form XML schema](../form-xml-schema.md).

To determine when an event handler runs on a form in bulk edit mode, use the [`getFormType`](reference/formContext-ui/getFormType.md) method.

## Add or remove event handler functions by using Client API code

Use the following methods to add and remove event handlers for events that you can't associate through the UI:

| Events | Event handler |
|-------|-------|
| Attribute [OnChange](reference/events/attribute-onchange.md) | [addOnChange](reference/attributes/addonchange.md) and [removeOnChange](reference/attributes/removeOnchange.md) methods |
| Form [OnLoad](reference/events/form-onload.md) | formContext.ui [addOnLoad](reference/formcontext-ui/addonload.md) and [removeOnLoad](reference/formcontext-ui/removeonload.md) methods |
| Form [Loaded](reference/events/form-loaded.md) | formContext.ui [addLoaded](reference/formcontext-ui/addloaded.md) and [removeLoaded](reference/formcontext-ui/removeloaded.md) methods |
| Form data [OnLoad](reference/events/form-data-onload.md) | formContext.data [addOnLoad](reference/formcontext-data/addonload.md) and [removeOnLoad](reference/formcontext-data/removeonload.md) methods |
| Form [OnSave](reference/events/form-onsave.md) | [addOnSave](reference/formcontext-data-entity/addonsave.md) and [removeOnSave](reference/formcontext-data-entity/removeonsave.md) methods |
| Lookup control [PreSearch](reference/events/presearch.md) | [addPreSearch](reference/controls/addpresearch.md) and [removePreSearch](reference/controls/removepresearch.md) methods |
| kbsearch control [OnResultOpened](reference/events/onresultopened.md) | [addOnResultOpened](reference/controls/addOnResultOpened.md) and [removeOnResultOpened](reference/controls/removeOnResultOpened.md) methods |
| kbsearch control [OnSelection](reference/events/onselection.md) | [addOnSelection](reference/controls/addOnSelection.md) and [removeOnSelection](reference/controls/removeOnSelection.md) methods |
| kbsearch control [PostSearch](reference/events/postsearch.md) | [addOnPostSearch](reference/controls/addOnPostSearch.md) and [removeOnPostSearch](reference/controls/removeOnPostSearch.md) methods |

>[!IMPORTANT]
> The execution context is automatically passed as the first parameter to functions that you set by using the code. For more information, see [Client API execution context](clientapi-execution-context.md). 

## Form event pipeline

You can define up to 50 event handlers for each event. The **Event Handlers** section in the **Events** tab of the **Form Properties** dialog box shows the order of event handlers, and each event handler runs in that order.

Use the [setSharedVariable](reference/executioncontext/setSharedVariable.md) and [getSharedVariable](reference/executioncontext/getSharedVariable.md) methods to pass a common variable between event handlers (functions). Use the execution context [getDepth](reference/executioncontext/getDepth.md) method to understand the sequence of event handler execution relative to other event handlers. 

### Related articles

[Understand the Client API object model](understand-clientapi-object-model.md)   
[Client API execution context](clientapi-execution-context.md)   
[Events (Client API reference)](reference/events.md)   

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
