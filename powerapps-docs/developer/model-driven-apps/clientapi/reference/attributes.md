---
title: "Attributes in model-driven apps| MicrosoftDocs"
description: "Learn about working with attributes in model-driven apps using client API."
ms.date: 10/31/2018
ms.service: powerapps
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


## Boolean attribute type

In addition to the methods available for all attribute types as explained earlier, the following method is available only for the **boolean** attribute:

- [getInitialValue](attributes/getInitialValue.md)

## Lookup attribute type
In addition to the methods available for all attribute types as explained earlier, the following method is available only for the **lookup** attribute:

- [getIsPartyList](attributes/getIsPartyList.md)

## MultiSelectOptionSet and OptionSet attribute types

In addition to the methods available for all attribute types as explained earlier, the following methods are available only for the **multiselectoption** and **optionset** attributes:

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

## Number attribute type (decimal, double, integer, money)
The following methods are available only for the **decimal**,  **double**, and **integer** attributes:

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

## String attribute type
In addition to the methods available for all attribute types as explained earlier, the following method is available only for the **string** attribute:

- [getMaxLength](attributes/getMaxLength.md)


### Related topics

[Composite attributes](composite-attributes.md)

[Understand Xrm object model](../understand-clientapi-object-model.md)

[Controls (Client API reference)](controls.md)




