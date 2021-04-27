---
title: "Columns in model-driven apps| MicrosoftDocs"
description: "Learn about working with columns in model-driven apps using client API."
ms.date: 10/31/2018
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 32e8d1d0-4093-4588-a517-2930eec34dce
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Columns (Client API reference)

Columns contain data in the model-driven apps form or grids. Use the `formContext.data.entity.attributes` collection or the `formContext.getAttribute` shortcut method to access a collection of columns. For more information about collections, see [Collections (Client API reference)](collections.md). 

To access a column within the collection, you pass either the name (string) or the index value (number) of the column as an argument to the method. For example: `formContext.getAttribute(arg)`

Columns are categorized by type. You can determine the type of the column by using the [getAttributeType](attributes/getAttributeType.md) method. Certain column methods are only available for specific types of columns.

[!INCLUDE[cc-terminology](../../../data-platform/includes/cc-terminology.md)]

This topic provides information about the methods available per column type. 

## All column types

<table>
<tr>
<td>
<ul>
<li><a href="attributes/controls-collection.md" data-raw-source="[controls](attributes/controls-collection.md)">controls</a></li>
<li><a href="attributes/addOnChange.md" data-raw-source="[addOnChange](attributes/addOnChange.md)">addOnChange</a></li>
<li><a href="attributes/fireOnChange.md" data-raw-source="[fireOnChange](attributes/fireOnChange.md)">fireOnChange</a></a></li>
<li><a href="attributes/getAttributeType.md" data-raw-source="[getAttributeType](attributes/getAttributeType.md)">getAttributeType</a></li>
<li><a href="attributes/getFormat.md" data-raw-source="[getFormat](attributes/getFormat.md)">getFormat</a></li>
<li><a href="attributes/getIsDirty.md" data-raw-source="[getIsDirty](attributes/getIsDirty.md)">getIsDirty</a></li>
</ul>
</td>
<td>
<ul>
<li><a href="attributes/getName.md" data-raw-source="[getName](attributes/getName.md)">getName</a></li>
<li><a href="attributes/getParent.md" data-raw-source="[getParent](attributes/getParent.md)">getParent</a></li>
<li><a href="attributes/getRequiredLevel.md" data-raw-source="[getRequiredLevel](attributes/getRequiredLevel.md)">getRequiredLevel</a></li>
<li><a href="attributes/getSubmitMode.md" data-raw-source="[getSubmitMode](attributes/getSubmitMode.md)">getSubmitMode</a></li>
<li><a href="attributes/getUserPrivilege.md" data-raw-source="[getUserPrivilege](attributes/getUserPrivilege.md)">getUserPrivilege</a></li>
<li><a href="attributes/getValue.md" data-raw-source="[getValue](attributes/getValue.md)">getValue</a></li>
</ul>
</td>
<td>
<ul>

<li><a href="attributes/isValid.md" data-raw-source="[isValid](attributes/isValid.md)">isValid</a></li>
<li><a href="attributes/removeOnChange.md" data-raw-source="[removeOnChange](attributes/removeOnChange.md)">removeOnChange</a></li>
<li><a href="attributes/setRequiredLevel.md" data-raw-source="[setRequiredLevel](attributes/setRequiredLevel.md)">setRequiredLevel</a></li>
<li><a href="attributes/setSubmitMode.md" data-raw-source="[setSubmitMode](attributes/setSubmitMode.md)">setSubmitMode</a></li>
<li><a href="attributes/setValue.md" data-raw-source="[setValue](attributes/setValue.md)">setValue</a></li>
<li><a href="attributes/setIsValid.md" data-raw-source="[setIsValid](attributes/setIsValid.md)">setIsValid</a></li>
</ul>
</td>
</tr>
</table>


## Boolean column type

In addition to the methods available for all column types as explained earlier, the following method is available only for the **boolean** column:

- [getInitialValue](attributes/getInitialValue.md)

## Lookup column type
In addition to the methods available for all column types as explained earlier, the following method is available only for the **lookup** column:

- [getIsPartyList](attributes/getIsPartyList.md)

## Choices and choice column types

In addition to the methods available for all column types as explained earlier, the following methods are available only for the **choices** and **choice** columns:

<table>
<tr>
<td>
<ul>
<li><a href="attributes/getInitialValue.md" data-raw-source="[getInitialValue](attributes/getInitialValue.md)">getInitialValue</a></li>
<li><a href="attributes/getOption.md" data-raw-source="[getOption](attributes/getOption.md)">getOption</a></li>
<li><a href="attributes/getOptions.md" data-raw-source="[getOptions](attributes/getOptions.md)">getOptions</a></a></li>
<li><a href="attributes/getSelectedOption.md" data-raw-source="[getSelectedOption](attributes/getSelectedOption.md)">getSelectedOption</a></li>
<li><a href="attributes/getText.md" data-raw-source="[getText](attributes/getText.md)">getText</a></li>
</ul>
</td>
</tr>
</table>

## Number column type (decimal, double, integer, money)

The following methods are available only for the **decimal**,  **double**, and **integer** columns:

<table>
<tr>
<td>
<ul>
<li><a href="attributes/getMax.md" data-raw-source="[getMax](attributes/getMax.md)">getMax</a></li>
<li><a href="attributes/getMin.md" data-raw-source="[getMin](attributes/getMin.md)">getMin</a></li>
<li><a href="attributes/getPrecision.md" data-raw-source="[getPrecision](attributes/getPrecision.md)">getPrecision</a></a></li>
<li><a href="attributes/setPrecision.md" data-raw-source="[setPrecision](attributes/setPrecision.md)">setPrecision</a></li>
</ul>
</td>
</tr>
</table>

## String column type
In addition to the methods available for all column types as explained earlier, the following method is available only for the **string** column:

- [getMaxLength](attributes/getMaxLength.md)


### Related topics

[Composite columns](composite-attributes.md)<br/>
[Understand Xrm object model](../understand-clientapi-object-model.md)<br/>
[Controls (Client API reference)](controls.md)






[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]