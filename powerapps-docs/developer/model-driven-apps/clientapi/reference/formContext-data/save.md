---
title: "formContext.data.save (Client API Reference) in Model-Driven Apps"
description: Learn how to use formContext.data.save to save a record asynchronously in model-driven apps and set callback functions to run after the save completes.
author: MitiJ
ms.author: mijosh
ms.date: 10/30/2026
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---

# formContext.data.save (Client API reference)

[!INCLUDE[./includes/save-description.md](./includes/save-description.md)]

By using `formContext.data.save`, you can set an object to control how [appointment](../../../../data-platform/reference/entities/appointment.md), [recurring appointment](../../../../data-platform/reference/entities/recurringappointmentmaster.md), or [service activity](/dynamics365/developer/reference/entities/serviceappointment) records are processed.

> [!NOTE]
> When working with forms and you call the `formContext.data.save` method, ensure that you also call the [preventDefault](../save-event-arguments/preventDefault.md) method to prevent triggering any default save operation when a user saves the form.

## Syntax

`formContext.data.save(saveOptions).then(successCallback, errorCallback);`

## Parameters

|Name|Type|Required|Description|
|--|--|--|--|
|`saveOptions`|[saveOptions](#saveoptions-parameter)|No|An object for specifying options for saving the record.|
|`successCallback`|Function|No|A function to call when the operation succeeds.|
|`errorCallback`|Function|No|A function to call when the operation fails. The function receives an object with the following properties:<br/><br/>- **`errorCode`**: Number. The error code.<br/><br/>- **`message`**: String. A localized error message.|


### saveOptions parameter

| Name | Type | Description |
| --- | --- | --- |
| `saveMode` | Number | (Optional) Specify a value that indicates how the save event was initiated. For a list of supported values, see the return value of the [getSaveMode](../save-event-arguments/getsavemode.md) method.<br /><br />Setting the `saveMode` doesn't actually take the corresponding action; it just provides information to the `OnSave` event handlers about the reason for the save operation. |
| `useSchedulingEngine` | Boolean | (Optional) Indicate whether to use the `Book` or `Reschedule` messages rather than the `Create` or `Update` messages.<br /><br />This option only applies when used with [appointment](../../../../data-platform/reference/entities/appointment.md), [recurring appointment](../../../../data-platform/reference/entities/recurringappointmentmaster.md), or [service activity](/dynamics365/developer/reference/entities/serviceappointment) records records.<br /><br />This property isn't supported in Unified Interface. |


### Related articles

[formContext.data.entity.save](../formContext-data-entity/save.md)   
[formContext](../../clientapi-form-context.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
