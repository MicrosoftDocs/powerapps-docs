---
title: "setSubmitMode (Client API reference)| MicrosoftDocs"
description: Sets whether data from the column will be submitted when the record is saved. 
author: HemantGaur
ms.author: hemantg
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# setSubmitMode (Client API reference)



Sets whether data from the column will be submitted when the record is saved. 

## Column types supported

All

## Syntax

`formContext.getAttribute(arg).setSubmitMode(mode)`

## Parameters

**Type**: String. 

**Description**: Set one of the following mode values:

- **always**: The data is always sent with a save.
- **never**: The data is never sent with a save. When this value is used, the column(s) in the form for this column cannot be edited.
- **dirty**: Default behavior. The data is sent with the save when it has changed.
 
## Remarks

Use this method to control when data for a column is submitted when a record is created or saved. For example, you may have a column on the form that is only intended to control logic in the form. You are not interested in capturing the data in it. You might set it so that the data is not saved. Or you may have a Plugin that depends on the value always being included. You may want to set the column so that it will always be included. 

> [!NOTE]
> Data in a column will always be refreshed after save operation, even if the column's submit mode is set to `never`. For example, if a column's value in the server is null and the column's submit mode is set to `never`, and the column is modified with some value by the user, after the user saves the form the column's value will be replaced with null.

Columns that do not get updated after the initial save of the record, such as **createdby**, are set so that they will not be submitted on save. To force a column value to be submitted whether it has changed or not, use this method with the *mode* parameter set to "always".

### See also
[getSubmitMode (Client API reference)](getSubmitMode.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
