---
title: "save (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 03e970ee-7ed3-4df2-9670-222d76a479fd
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# save (Client API reference)



[!INCLUDE[./includes/save-description.md](./includes/save-description.md)]

You can also set an object to control how appointment, recurring appointment, or service activity records are processed.

## Syntax

`formContext.data.save(saveOptions).then(successCallback, errorCallback);`

## Parameters

|Name|Type|Required|Description|
|--|--|--|--|
|saveOptions|Object|No|An object for specifying options for saving the record. The object has following attributes:<br/><br/>- **saveMode**: (Optional) Number. Specify a value indicating how the save event was initiated. For a list of supported values, see the return value of the [getSaveMode](../save-event-arguments/getsavemode.md) method. Note that setting the **saveMode** does not actually take the corresponding action; it is just to provide information to the **OnSave** event handlers about the reason for the save operation.<br/><br/>- **useSchedulingEngine**: (Optional) Boolean. Indicate whether to use the **Book** or **Reschedule** messages rather than the **Create** or **Update** messages. This option is only applicable when used with appointment, recurring appointment, or service activity records.|
|successCallback|Function|No|A function to call when the operation succeeds.|
|errorCallback|Function|No|A function to call when the operation fails. An object with the following properties will be passed:<br/><br/>- **errorCode**: Number. The error code.<br/><br/>- **message**: String. A localized error message.|


### Related topics

[formContext.data.entity.save](../formContext-data-entity/save.md)

[formContext](../../clientapi-form-context.md)

