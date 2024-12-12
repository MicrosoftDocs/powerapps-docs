---
title: "Column OnChange Event in model-driven apps"
description: Learn about how to set the column OnChange event.
author: MitiJ
ms.author: mijosh
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---

# Column OnChange event (Client API reference)

The `OnChange` event occurs in the following situations:

- Data in a form column has changed and focus is lost. There is an exception to this behavior that applies to Yes/No columns that are formatted to use radio buttons or check boxes. In these cases the event occurs immediately.
- Data changes on the server are retrieved to update a column when the form is refreshed, such as after a record is saved.
- The [attribute.fireOnchange](../attributes/fireOnChange.md) method is used.

All columns support the `OnChange` event. Data in the column is validated before and after the `OnChange` event.

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

The `OnChange` event does not occur if the column is changed programmatically using the [attribute.setValue](../attributes/setValue.md) method. If you want event handlers for the `OnChange` event to run after you set the value you must use the `formContext.data.entity attribute.`[fireOnchange](../attributes/fireOnChange.md) method in your code. The `OnChange` event also does not occur if the column is changed programatically when discarding changes if the user is navigating away from a dirty form.

> [!NOTE]
> Although the **Status** column supports the`OnChange` event, the column is read-only on the form so the event cannot occur through user interaction. Another script could cause this event to occur by using the [fireOnchange](../attributes/fireOnChange.md) method on the column.

> [!NOTE]
> `OnChange` events are synchronous. You should **not** use asynchronous code in an `OnChange` event handler that needs an action to be taken or handled on the resolution of the async code. This causes issues if the resolution handler expects the app context to remain the same as it was when the asynchronous code was started. You should also **not** make synchronous network requests in an OnChange event handler. This can cause an unresponsive app.

## Methods supported for this event

There are three methods you can use to work with the `OnChange` event for a column:

- [addOnChange](../attributes/addOnChange.md)
- [fireOnChange](../attributes/fireOnChange.md)
- [removeOnChange](../attributes/removeOnChange.md)

### Related articles

[Columns (Client API reference)](../attributes.md)   
[Events (Client API reference)](../events.md)   
[Events in forms and grids in model-driven apps](../../events-forms-grids.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
