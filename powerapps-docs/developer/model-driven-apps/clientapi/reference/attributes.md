---
title: "Columns in Model-Driven Apps Client API Reference"
description: "Learn how to access and manage columns in model-driven apps with the Client API, including methods available for each column type. Explore the reference now."
author: sriharibs-msft
ms.author: srihas
ms.date: 10/30/2026
ms.reviewer: jdaly
ms.topic: reference
ai-usage: ai-assisted
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# Columns in model-driven apps (Client API reference)

Columns contain data in the model-driven apps form or grids. Use the `formContext.data.entity.attributes` collection or the `formContext.getAttribute` shortcut method to access a collection of columns. For more information about collections, see [Collections (Client API reference)](collections.md). 

To access a column within the collection, pass either the name (string) or the index value (number) of the column as an argument to the method. For example: `formContext.getAttribute(arg)`. If you don't specify an argument, the method returns a collection of all attributes on the form.

Columns are categorized by type. Use the [getAttributeType](attributes/getAttributeType.md) method to determine the type of the column. Certain column methods are only available for specific types of columns.

This article provides information about the methods available for each column type. 

## All column types

The [controls](attributes/controls-collection.md) property provides a collection of [controls](controls.md) associated with the column.

The following methods are available for all column types:

| Method | Description |
|---|---|
| [addOnChange](attributes/addOnChange.md) | Adds a function to run when the column's `OnChange` event occurs. |
| [fireOnChange](attributes/fireOnChange.md) | Triggers the column's `OnChange` event. |
| [getAttributeType](attributes/getAttributeType.md) | Returns the column's type. |
| [getFormat](attributes/getFormat.md) | Returns the column's format. |
| [getIsDirty](attributes/getIsDirty.md) | Returns whether the column has unsaved changes. |
| [getName](attributes/getName.md) | Returns the column's logical name. |
| [getParent](attributes/getParent.md) | Returns the parent `formContext.data.entity` object. |
| [getRequiredLevel](attributes/getRequiredLevel.md) | Returns whether a column value is required or recommended. |
| [getSubmitMode](attributes/getSubmitMode.md) | Returns when the column's data is submitted on save. |
| [getUserPrivilege](attributes/getUserPrivilege.md) | Returns the user's privileges to create, read, or update the column's value. |
| [getValue](attributes/getValue.md) | Returns the column's data value. |
| [isValid](attributes/isValid.md) | Returns whether the column's value is valid. |
| [removeOnChange](attributes/removeOnChange.md) | Removes a function from the column's `OnChange` event handlers. |
| [setIsValid](attributes/setIsValid.md) | Sets the column's validity and an error message. |
| [setRequiredLevel](attributes/setRequiredLevel.md) | Sets whether a column value is required or recommended before saving. |
| [setSubmitMode](attributes/setSubmitMode.md) | Sets whether the column's data is submitted on save. |
| [setValue](attributes/setValue.md) | Sets the column's data value. |

## Boolean column type

In addition to the methods available for all column types, the **boolean** column type provides the following method:

| Method | Description |
|---|---|
| [getInitialValue](attributes/getInitialValue.md) | Returns the column's value when the form opened. |

## Lookup column type

In addition to the methods available for all column types, the **lookup** column type provides the following method:

| Method | Description |
|---|---|
| [getIsPartyList](attributes/getIsPartyList.md) | Returns whether the lookup allows multiple records as a party list lookup. |

## Choices and choice column types

In addition to the methods available for all column types, the **choices** and **choice** column types provide the following methods:

| Method | Description |
|---|---|
| [getInitialValue](attributes/getInitialValue.md) | Returns the column's value when the form opened. |
| [getOption](attributes/getOption.md) | Returns the option matching a specified label or value. |
| [getOptions](attributes/getOptions.md) | Returns the column's valid options. |
| [getSelectedOption](attributes/getSelectedOption.md) | Returns the selected option or options. |
| [getText](attributes/getText.md) | Returns the text of the selected option or options. |

## Number column type (decimal, double, integer, money)

The following methods are available only for the **decimal**,  **double**, and **integer** columns:

| Method | Description |
|---|---|
| [getMax](attributes/getMax.md) | Returns the column's maximum allowed value. |
| [getMin](attributes/getMin.md) | Returns the column's minimum allowed value. |
| [getPrecision](attributes/getPrecision.md) | Returns the number of digits allowed after the decimal point. |
| [setPrecision](attributes/setPrecision.md) | Sets the number of digits allowed after the decimal point. |

## String column type

In addition to the methods available for all column types as explained earlier, the following method is available only for the **string** column:

| Method | Description |
|---|---|
| [getMaxLength](attributes/getMaxLength.md) | Returns the column's maximum string length. |


### Related articles

[Understand Xrm object model](../understand-clientapi-object-model.md)<br/>
[Controls (Client API reference)](controls.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
