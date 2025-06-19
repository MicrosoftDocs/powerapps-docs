---
title: "attribute.isValid (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the attribute.isValid method.
author: clromano
ms.author: clromano
ms.date: 03/21/2024
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors:
  - JimDaly
  - ericregnier
---
# attribute.isValid (Client API reference)

Returns a boolean value to indicate whether the value of a column is valid. 

## Column types supported

All

## Syntax

`formContext.getAttribute(arg).isValid();`

## Return Value

**Type**: Boolean

**Description**: `true` if the column value is valid; `false` otherwise.

The validity logic uses the properties of the [Dataverse column](../../../../data-platform/entity-attribute-metadata.md#column-types). Each type of column might have properties that limit valid values.

For example, a **Whole Number** column uses the [IntegerAttributeMetadata class](/dotnet/api/microsoft.xrm.sdk.metadata.integerattributemetadata) that provides the [MaxValue](/dotnet/api/microsoft.xrm.sdk.metadata.integerattributemetadata.maxvalue) and [MinValue](/dotnet/api/microsoft.xrm.sdk.metadata.integerattributemetadata.minvalue) properties. These properties are editable in the column definition in [Power Apps](https://make.powerapps.com) designer as **Maximum value** and **Minimum value** respectively.

If a **Whole Number** column has **Maximum value** of 0 and **Minimum value** of 100, the `isValid` function returns `false` when the current unsaved value on the form is 1000 and `true` whenever the current value falls between 0 and 100.

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
