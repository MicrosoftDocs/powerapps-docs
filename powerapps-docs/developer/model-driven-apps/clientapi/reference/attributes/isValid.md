---
title: "attribute.isValid (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the attribute.isValid method.
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
# attribute.isValid (Client API reference)



Returns a boolean value to indicate whether the value of a column is valid. 

## Column types supported

All

## Syntax

`formContext.getAttribute(arg).isValid();`

## Return Value

**Type**: Boolean. 

**Description**: true if the column value is valid; false otherwise. <br />
The validity logic is performed against the properties of the [Dataverse column](../../maker/data-platform/types-of-fields). For instance, if the column is of type [whole number](../../maker/data-platform/types-of-fields) with a minimun of 0 and a maximum of 100, the `isValid` function will return `false` when the current unsaved value on the form is 1000 and `true` whenever the current value falls between 0 and 100.



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
