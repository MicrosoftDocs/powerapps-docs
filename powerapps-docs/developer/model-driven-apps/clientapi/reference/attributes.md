---
title: "Attributes in model-driven apps| MicrosoftDocs"
description: "Learn about working with attributes in model-driven apps using client API."
ms.date: 10/31/2018
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 32e8d1d0-4093-4588-a517-2930eec34dce
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Attributes (Client API reference)



Attributes contain data in the model-driven apps form or grids. Use the `formContext.data.entity.attributes` collection or the `formContext.getAttribute` shortcut method to access a collection of attributes. For more information about collections, see [Collections (Client API reference)](collections.md). 

To access an attribute within the collection, you pass either the name (string) or the index value (number) of the attribute as an argument to the method. For example: `formContext.getAttribute(arg)`

Attributes are categorized by type. You can determine the type of an attribute by using the [getAttributeType](attributes/getAttributeType.md) method. Certain attribute methods are only available for specific types of attributes.

This topic provides information about the methods available per attribute type. 

## All attribute types

<table>
<tr>
<td>
<ul>
<li>[controls](attributes/controls-collection.md)</li>
<li>[addOnChange](attributes/addOnChange.md)</li>
<li>[fireOnChange](attributes/fireOnChange.md)</a></li>
<li>[getAttributeType](attributes/getAttributeType.md)</li>
<li>[getFormat](attributes/getFormat.md)</li>
<li>[getIsDirty](attributes/getIsDirty.md)</li>
</ul>
</td>
<td>
<ul>
<li>[getName](attributes/getName.md)</li>
<li>[getParent](attributes/getParent.md)</li>
<li>[getRequiredLevel](attributes/getRequiredLevel.md)</li>
<li>[getSubmitMode](attributes/getSubmitMode.md)</li>
<li>[getUserPrivilege](attributes/getUserPrivilege.md)</li>
<li>[getValue](attributes/getValue.md)</li>
</ul>
</td>
<td>
<ul>

<li>[isValid](attributes/isValid.md)</li>
<li>[removeOnChange](attributes/removeOnChange.md)</li>
<li>[setRequiredLevel](attributes/setRequiredLevel.md)</li>
<li>[setSubmitMode](attributes/setSubmitMode.md)</li>
<li>[setValue](attributes/setValue.md)</li>
</ul>
</td>
</tr>
</table>


## Boolean attribute type
In addition to the methods available for all attribute types as explained ealier, the following method is available only for the **boolean** attribute:

- [getInitialValue](attributes/getInitialValue.md)

## Lookup attribute type
In addition to the methods available for all attribute types as explained ealier, the following method is available only for the **lookup** attribute:

- [getIsPartyList](attributes/getIsPartyList.md)

## MultiSelectOptionSet and OptionSet attribute types

In addition to the methods available for all attribute types as explained ealier, the following methods are available only for the **multiselectoption** and **optionset** attributes:

<table>
<tr>
<td>
<ul>
<li>[getInitialValue](attributes/getInitialValue.md)</li>
<li>[getOption](attributes/getOption.md)</li>
<li>[getOptions](attributes/getOptions.md)</a></li>
<li>[getSelectedOption](attributes/getSelectedOption.md)</li>
<li>[getText](attributes/getText.md)</li>
</ul>
</td>
</tr>
</table>

## Number attribute type (decimal, double, integer, money)
The following methods are available only for the **decimal**,  **double**, and **integer** attributes:

<table>
<tr>
<td>
<ul>
<li>[getMax](attributes/getMax.md)</li>
<li>[getMin](attributes/getMin.md)</li>
<li>[getPrecision](attributes/getPrecision.md)</a></li>
<li>[setPrecision](attributes/setPrecision.md)</li>
<li>[getText](attributes/getText.md)</li>
</ul>
</td>
</tr>
</table>

## String attribute type
In addition to the methods available for all attribute types as explained ealier, the following method is available only for the **string** attribute:

- [getMaxLength](attributes/getMaxLength.md)

### Related topics

[Composite attributes](composite-attributes.md)

[Understand Xrm object model](../understand-clientapi-object-model.md)

[Controls (Client API reference)](controls.md)




