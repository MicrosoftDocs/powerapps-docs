---
title: "setSubmitMode (Client API reference)| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: d0728377-4365-4571-97af-9b99b2a39b65
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# setSubmitMode (Client API reference)



Sets whether data from the attribute will be submitted when the record is saved. 

## Attribute types supported

All

## Syntax

`formContext.getAttribute(arg).setSubmitMode(mode)`

## Parameters

**Type**: String. 

**Description**: Set one of the following mode values:
- **always**: The data is always sent with a save.
- **never**: The data is never sent with a save. When this is used, the field(s) in the form for this attribute cannot be edited.
- **dirty**: Default behavior. The data is sent with the save when it has changed.
 
## Remarks
Use this method to control when data for an attribute is submitted when a record is created or saved. For example, you may have a field on the form which is only intended to control logic in the form. You are not interested in capturing the data in it. You might set it so that the data is not saved. Or you may have a Plugin that depends on the value always being included. You may want to set the attribute so that it will always be included. 

Attributes that do not get updated after the initial save of the record, such as **createdby**, are set so that they will not be submitted on save. To force an attribute value to be submitted whether it has changed or not, use this method with the *mode* parameter set to “always”.

### Related topic
[getSubmitMode (Client API reference)](getSubmitMode.md)

