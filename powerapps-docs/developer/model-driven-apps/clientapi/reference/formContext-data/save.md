---
title: "save (Client API reference) in model-driven apps| MicrosoftDocs"
description: Saves the record asynchronously with the option to set callback functions to be executed after the save operation is completed.
ms.date: 04/15/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 03e970ee-7ed3-4df2-9670-222d76a479fd
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# formContext.data.save (Client API reference)

[!INCLUDE[./includes/save-description.md](./includes/save-description.md)]

You can also set an object to control how appointment, recurring appointment, or service activity records are processed.

## Syntax

`formContext.data.save(saveOptions).then(successCallback, errorCallback);`

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Parameters

|Name|Type|Required|Description|
|--|--|--|--|
|saveOptions|Object|No|An object for specifying options for saving the record. The object has following parameters:<br/><br/>- **saveMode**: (Optional) Number. Specify a value indicating how the save event was initiated. For a list of supported values, see the return value of the [getSaveMode](../save-event-arguments/getsavemode.md) method. Note that setting the **saveMode** does not actually take the corresponding action; it is just to provide information to the **OnSave** event handlers about the reason for the save operation.<br/><br/>- **useSchedulingEngine**: (Optional) Boolean. Indicate whether to use the **Book** or **Reschedule** messages rather than the **Create** or **Update** messages. This option is only applicable when used with appointment, recurring appointment, or service activity records.<br/><br/> **NOTE**: `useSchedulingEngine` property is not supported in Unified Interface.|
|successCallback|Function|No|A function to call when the operation succeeds.|
|errorCallback|Function|No|A function to call when the operation fails. An object with the following properties will be passed:<br/><br/>- **errorCode**: Number. The error code.<br/><br/>- **message**: String. A localized error message.|

> [!NOTE]
> When working with forms, and you call the `formContext.data.save` method, make sure that you also call the [preventDefault](../save-event-arguments/preventDefault.md) to ensure that any default save operation is not triggered when a user saves the form.


### Related topics

[formContext.data.entity.save](../formContext-data-entity/save.md)

[formContext](../../clientapi-form-context.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]