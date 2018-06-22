---
title: "Controls in Customer Engagement for Dynamics 365| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 4d025f92-db16-440c-9f82-e40d71e09862
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# Controls (Client API reference)



A control represents an HTML element present on the form. Some controls are bound to a specific attribute, whereas others may represent unbound controls such as an IFRAME, Web resource, or a sub grid that has been added to the form. 

The **control** object provides methods to change the presentation or behavior of a control and identify the corresponding attribute. You access controls using one of the following collections: 
- **formContext.ui.controls**
- **formContext.ui Section.controls**
- **formContext.data.entity** **Attribute.controls**

The **formContext**.[getControl](controls/getControl.md) method is a shortcut method to access **formContext.ui.controls.get**. 

Controls are categorized by type. You can determine the type of a control by using the [getControlType](controls/getControlType.md) method. Certain control methods are only available for specific types of controls.

This topic provides information about the methods available per control type. 

## standard control type

These are the methods available for a Standard control.

<table>
<tr>
<td>
<ul>
<li>[addNotification](controls/addNotification.md)</li>
<li>[clearNotification](controls/clearNotification.md)</li>
<li>[getAttribute](controls/getAttribute.md)</a></li>
<li>[getControlType](controls/getControlType.md)</li>
<li>[getDisabled](controls/getDisabled.md)</li>
</ul>
</td>
<td>
<ul>
<li>[getLabel](controls/getLabel.md)</li>
<li>[getName](controls/getName.md)</li>
<li>[getParent](controls/getParent.md)</li>
<li>[getVisible](controls/getVisible.md)</li>
<li>[setDisabled](controls/setDisabled.md)</li>
</ul>
</td>
<td>
<ul>
<li>[setFocus](controls/setFocus.md)</li>
<li>[setLabel](controls/setLabel.md)</li>
<li>[setNotification](controls/setNotification.md)</li>
<li>[setVisible](controls/setVisible.md)</li>
</ul>
</td>
</tr>
</table>

The following methods for the Standard control are [deprecated](/dynamics365/get-started/whats-new/customer-engagement/important-changes-coming#some-client-apis-are-deprecated) in this release: addOnKeyPress, fireOnKeyPress, and removeOnKeyPress.

## iframe control type

These are the methods available for an IFRAME control.

<table>
<tr>
<td>
<ul>
<li>[getControlType](controls/getControlType.md)</li>
<li>[getDisabled](controls/getDisabled.md)</li>
<li>[getInitialUrl](controls/getInitialUrl.md)</li>
<li>[getLabel](controls/getLabel.md)</li>
<li>[getName](controls/getName.md)</li>
</ul>
</td>
<td>
<ul>
<li>[getObject](controls/getObject.md)</li>
<li>[getParent](controls/getParent.md)</li>
<li>[getSrc](controls/getSrc.md)</li>
<li>[getVisible](controls/getVisible.md)</li>
<li>[setDisabled](controls/setDisabled.md)</li>
</ul>
</td>
<td>
<ul>
<li>[setFocus](controls/setFocus.md)</li>
<li>[setLabel](controls/setLabel.md)</li>
<li>[setSrc](controls/setSrc.md)</li>
<li>[setVisible](controls/setVisible.md)</li>
</ul>
</td>
</tr>
</table>

## kbsearch (Knowledge base search) control type

These are the methods available for knowledge base search control.

<table>
<tr>
<td>
<ul>
<li>[addOnPostSearch](controls/addOnPostSearch.md)</li>
<li>[addOnResultOpened](controls/addOnResultOpened.md)</li>
<li>[addOnSelection](controls/addOnSelection.md)</li>
<li>[getControlType](controls/getControlType.md)</li>
<li>[getDisabled](controls/getDisabled.md)</li>
<li>[getLabel](controls/getLabel.md)</li>
<li>[getName](controls/getName.md)</li>
</ul>
</td>
<td>
<ul>
<li>[getParent](controls/getParent.md)</li>
<li>[getSearchQuery](controls/getSearchQuery.md)</li>
<li>[getSelectedResults](controls/getSelectedResults.md)</li>
<li>[getTotalResultCount](controls/getTotalResultCount.md)</li>
<li>[getVisible](controls/getVisible.md)</li>
<li>[openSearchResult](controls/openSearchResult.md)</li>
<li>[removeOnPostSearch](controls/removeOnPostSearch.md)</li>

</ul>
</td>
<td>
<ul>
<li>[removeOnResultOpened](controls/removeOnResultOpened.md)</li>
<li>[removeOnSelection](controls/removeOnSelection.md)</li>
<li>[setFocus](controls/setFocus.md)</li>
<li>[setLabel](controls/setLabel.md)</li>
<li>[setSearchQuery](controls/setSearchQuery.md)</li>
<li>[setVisible](controls/setVisible.md)</li>
</ul>
</td>
</tr>
</table>

>[!NOTE]
>When the knowledge base search control is added to the social pane, the name of the control will be "searchwidgetcontrol_notescontrol". This name can’t be changed. 

## lookup control type

These are the methods available for a lookup control.

<table>
<tr>
<td>
<ul>
<li>[addCustomFilter](controls/addCustomFilter.md)</li>
<li>[addCustomView](controls/addCustomView.md)</li>
<li>[addNotification](controls/addNotification.md)</li>
<li>[addPreSearch](controls/addPreSearch.md)</li>
<li>[clearNotification](controls/clearNotification.md)</li>
<li>[getAttribute](controls/getAttribute.md)</a></li>
<li>[getControlType](controls/getControlType.md)</li>
<li>[getDefaultView](controls/getDefaultView.md)</li>
</ul>
</td>
<td>
<ul>
<li>[getDisabled](controls/getDisabled.md)</li>
<li>[getEntityTypes](controls/getEntityTypes.md)</li>
<li>[getLabel](controls/getLabel.md)</li>
<li>[getName](controls/getName.md)</li>
<li>[getParent](controls/getParent.md)</li>
<li>[getVisible](controls/getVisible.md)</li>
<li>[removePreSearch](controls/removePreSearch.md)</li>
<li>[setDefaultView](controls/setDefaultView.md)</li>

</ul>
</td>
<td>
<ul>
<li>[setDisabled](controls/setDisabled.md)</li>
<li>[setEntityTypes](controls/setEntityTypes.md)</li>
<li>[setFocus](controls/setFocus.md)</li>
<li>[setLabel](controls/setLabel.md)</li>
<li>[setNotification](controls/setNotification.md)</li>
<li>[setVisible](controls/setVisible.md)</li>
</ul>
</td>
</tr>
</table>

## multiselectoptionset and optionset control types

Both multi-select option set and option set controls have the same set of methods available.

<table>
<tr>
<td>
<ul>
<li>[addNotification](controls/addNotification.md)</li>
<li>[addOption](controls/addOption.md)</li>
<li>[clearNotification](controls/clearNotification.md)</li>
<li>[clearOptions](controls/clearOptions.md)</li>
<li>[getAttribute](controls/getAttribute.md)</a></li>
<li>[getControlType](controls/getControlType.md)</li>
</ul>
</td>
<td>
<ul>
<li>[getDisabled](controls/getDisabled.md)</li>
<li>[getLabel](controls/getLabel.md)</li>
<li>[getName](controls/getName.md)</li>
<li>[getParent](controls/getParent.md)</li>
<li>[getVisible](controls/getVisible.md)</li>
<li>[removeOption](controls/removeoption.md)</li>
</ul>
</td>
<td>
<ul>
<li>[setDisabled](controls/setDisabled.md)</li>
<li>[setFocus](controls/setFocus.md)</li>
<li>[setLabel](controls/setLabel.md)</li>
<li>[setNotification](controls/setNotification.md)</li>
<li>[setVisible](controls/setVisible.md)</li>
</ul>
</td>
</tr>
</table>

## quickform control type

See [formContext.ui.quickForms](formcontext-ui-quickforms.md) for information about methods supported for this control type.

## subgrid control type

See [Grids and subgrids](grids.md) for information methods supported for this control type.

## timelinewall control type

The timeline control is a new control type introduced in Dynamics 365 (online), version 9.0 that presents the Posts, Activities, and Notes in a unified view. These are the methods available for this control type.

<table>
<tr>
<td>
<ul>
<li>[getControlType](controls/getControlType.md)</li>
<li>[getDisabled](controls/getDisabled.md)</li>
<li>[getLabel](controls/getLabel.md)</li>
<li>[getName](controls/getName.md)</li>
</ul>
</td>
<td>
<ul>

<li>[getParent](controls/getParent.md)</li>
<li>[getVisible](controls/getVisible.md)</li>
<li>[refresh](controls/refresh.md)</li>
<li>[setDisabled](controls/setDisabled.md)</li>
</ul>
</td>
<td>
<ul>
<li>[setFocus](controls/setFocus.md)</li>
<li>[setLabel](controls/setLabel.md)</li>
<li>[setVisible](controls/setVisible.md)</li>
</ul>
</td>
</tr>
</table>

## timer control type

These are the methods available for the timer control.

<table>
<tr>
<td>
<ul>
<li>[getControlType](controls/getControlType.md)</li>
<li>[getDisabled](controls/getDisabled.md)</li>
<li>[getLabel](controls/getLabel.md)</li>
<li>[getName](controls/getName.md)</li>
</ul>
</td>
<td>
<ul>

<li>[getParent](controls/getParent.md)</li>
<li>[getState](controls/getState.md)</li>
<li>[getVisible](controls/getVisible.md)</li>
<li>[refresh](controls/refresh.md)</li>

</ul>
</td>
<td>
<ul>
<li>[setDisabled](controls/setDisabled.md)</li>
<li>[setFocus](controls/setFocus.md)</li>
<li>[setLabel](controls/setLabel.md)</li>
<li>[setVisible](controls/setVisible.md)</li>
</ul>
</td>
</tr>
</table>

## webresource control type

A web resource control has the same set of methods available as the iframe control. See [iframe control type](#iframe-control-type)

### Related topics

[Attributes](attributes.md)