---
title: Property (Power Apps component framework API reference) | Microsoft Docs
description: Interface for context.parameters.<property_key>
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# Property

Interface for `context.parameters.<property_key>`

## Available for

Model-driven and canvas apps

## Properties

### error

Whether this parameter has either encountered an error in the population of its data, or that the data currently associated with this field is of an invalid format.

**Type**: `boolean`

### errorMessage

The error message associated with the last encountered error, if applicable.

**type**: `string`

### formatted

The formatted string value of this field. 

Only set if the corresponding manifest [property element](../manifest-schema-reference/property.md) `usage` attribute value is `bound`, indicating that the component can change the value.

**Type**: `string`


### security

Information concerning the field level security of the field to which this control was bound. 

This value is only present if the corresponding manifest [property element](../manifest-schema-reference/property.md) `usage` attribute value is `bound`, indicating that the component can change the value.

**Type**: [SecurityValues](securityvalues.md)


### raw

The raw, unformatted value of this field.

**Type**: `any`

### attributes

The attribute metadata associated with the field this property is configured against. 

This is only set when the corresponding manifest [property element](../manifest-schema-reference/property.md) `usage` attribute value is `bound`, indicating that the component can change the value.

**Type**:  `FieldPropertyMetadata`


### Related articles

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
