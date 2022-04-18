---
title: Property | Microsoft Docs
description: Interface for context.parameters.<property_key>
keywords:
ms.author: noazarur
author: noazarur-microsoft
manager: evchaki
ms.date: 04/17/2022
ms.reviewer: jdaly
ms.topic: "article"
contributor:
 - JimDaly
---

# Property

Interface for `context.parameters.<property_key>`

## Available for

Model-driven and canvas apps

## Properties

### error

**Type**: `boolean`
A boolean indicator to tell the control whether this parameter has either encountered an error in the population of its data, or that the data currently associated with this field is of an invalid format.

### errorMessage

**type**: `string`
The error message associated with the last encountered error, if applicable.

### formatted

**Type**: `string`
The formatted string value of this field. This is only set if the parameter is of usage=bound.


### security

**Type**: [SecurityValues](securityvalues.md)
Information concerning the field level security of the field to which this control was bound. This value is only present if the usage=bound.


### raw

**Type**: `any`
The raw, unformatted value of this field.

### attributes

**Type**: `FieldPropertyMetadata`
The attribute metadata associated with the field this property is configured against. This is only set when the parameter is of usage=bound.


### Related topics

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
