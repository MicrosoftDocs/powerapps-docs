---
title: "Columns in model-driven apps"
description: "Learn about working with columns in model-driven apps using client API."
author: sriharibs-msft
ms.author: srihas
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# Columns (Client API reference)

Columns contain data in the model-driven apps form or grids. Use the `formContext.data.entity.attributes` collection or the `formContext.getAttribute` shortcut method to access a collection of columns. For more information about collections, see [Collections (Client API reference)](collections.md). 

To access a column within the collection, you pass either the name (string) or the index value (number) of the column as an argument to the method. For example: `formContext.getAttribute(arg)`. If no argument is specified, it will return a collection of all attributes on the form.

Columns are categorized by type. You can determine the type of the column by using the [getAttributeType](attributes/getAttributeType.md) method. Certain column methods are only available for specific types of columns.

[!INCLUDE[cc-terminology](../../../data-platform/includes/cc-terminology.md)]

This topic provides information about the methods available per column type. 

## All column types

:::row:::
   :::column:::
   [controls](attributes/controls-collection.md)
   :::column-end:::
   :::column:::
   [addOnChange](attributes/addOnChange.md)
   :::column-end:::
   :::column:::
   [fireOnChange](attributes/fireOnChange.md)
   :::column-end:::
   :::column:::
   [getAttributeType](attributes/getAttributeType.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column:::
   [getFormat](attributes/getFormat.md)
   :::column-end:::
   :::column:::
   [getIsDirty](attributes/getIsDirty.md)
   :::column-end:::
   :::column:::
   [getName](attributes/getName.md)
   :::column-end:::
   :::column:::
   [getParent](attributes/getParent.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column:::
   [getRequiredLevel](attributes/getRequiredLevel.md)
   :::column-end:::
   :::column:::
   [getSubmitMode](attributes/getSubmitMode.md)
   :::column-end:::
   :::column:::
   [getUserPrivilege](attributes/getUserPrivilege.md)
   :::column-end:::
   :::column:::
   [getValue](attributes/getValue.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column:::
   [isValid](attributes/isValid.md)
   :::column-end:::
   :::column:::
   [removeOnChange](attributes/removeOnChange.md)
   :::column-end:::
   :::column:::
   [setRequiredLevel](attributes/setRequiredLevel.md)
   :::column-end:::
   :::column:::
   [setSubmitMode](attributes/setSubmitMode.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column:::
   [setValue](attributes/setValue.md)
   :::column-end:::
   :::column:::
   [setIsValid](attributes/setIsValid.md)
   :::column-end:::
   :::column:::
   &nbsp;
   :::column-end:::
   :::column:::
   &nbsp;
   :::column-end:::
:::row-end:::

## Boolean column type

In addition to the methods available for all column types as explained earlier, the following method is available only for the **boolean** column:

- [getInitialValue](attributes/getInitialValue.md)

## Lookup column type

In addition to the methods available for all column types as explained earlier, the following method is available only for the **lookup** column:

- [getIsPartyList](attributes/getIsPartyList.md)

## Choices and choice column types

In addition to the methods available for all column types as explained earlier, the following methods are available only for the **choices** and **choice** columns:

:::row:::
   :::column:::
   [getInitialValue](attributes/getInitialValue.md)
   :::column-end:::
   :::column:::
   [getOption](attributes/getOption.md)
   :::column-end:::
   :::column:::
   [getOptions](attributes/getOptions.md)
   :::column-end:::
   :::column:::
   [getSelectedOption](attributes/getSelectedOption.md)
   :::column-end:::
   :::column:::
   [getText](attributes/getText.md)
   :::column-end:::
:::row-end:::

## Number column type (decimal, double, integer, money)

The following methods are available only for the **decimal**,  **double**, and **integer** columns:

:::row:::
   :::column:::
   [getMax](attributes/getMax.md)
   :::column-end:::
   :::column:::
   [getMin](attributes/getMin.md)
   :::column-end:::
   :::column:::
   [getPrecision](attributes/getPrecision.md)
   :::column-end:::
   :::column:::
   [setPrecision](attributes/setPrecision.md)
   :::column-end:::
:::row-end:::

## String column type

In addition to the methods available for all column types as explained earlier, the following method is available only for the **string** column:

- [getMaxLength](attributes/getMaxLength.md)


### Related articles

[Understand Xrm object model](../understand-clientapi-object-model.md)<br/>
[Controls (Client API reference)](controls.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
