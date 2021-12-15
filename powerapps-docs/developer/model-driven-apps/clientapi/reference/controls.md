---
title: "Controls in model-driven apps for Dynamics 365| MicrosoftDocs"
description: A control represents an HTML element present on the form.
ms.date: 04/15/2021
ms.service: powerapps
ms.topic: "reference"
ms.assetid: 4d025f92-db16-440c-9f82-e40d71e09862
author: "Nkrb"
ms.subservice: mda-developer
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Controls (Client API reference)

A control represents an HTML element present on the form. Some controls are bound to a specific column, whereas others may represent unbound controls such as an IFRAME, web resource, or a subgrid that has been added to the form. 

The **control** object provides methods to change the presentation or behavior of a control and identify the corresponding column. You access controls using one of the following collections: 

- **formContext.ui.controls**
- **formContext.ui Section.controls**
- **formContext.data.entity** **Attribute.controls**

The **formContext**.[getControl](controls/getControl.md) method is a shortcut method to access **formContext.ui.controls.get**. 

Controls are categorized by type. You can determine the type of a control by using the [getControlType](controls/getControlType.md) method. Certain control methods are only available for specific types of controls.

This article provides information about the methods available per control type. 

[!INCLUDE[cc-terminology](../../../data-platform/includes/cc-terminology.md)]

## standard control type

These are the methods available for a Standard control.

<table>
<tr>
<td>
<ul>
<li><a href="controls/addNotification.md" data-raw-source="[addNotification](controls/addNotification.md)">addNotification</a></li>
<li><a href="controls/clearNotification.md" data-raw-source="[clearNotification](controls/clearNotification.md)">clearNotification</a></li>
<li><a href="controls/getAttribute.md" data-raw-source="[getAttribute](controls/getAttribute.md)">getAttribute</a></a></li>
<li><a href="controls/getControlType.md" data-raw-source="[getControlType](controls/getControlType.md)">getControlType</a></li>
<li><a href="controls/getDisabled.md" data-raw-source="[getDisabled](controls/getDisabled.md)">getDisabled</a></li>
</ul>
</td>
<td>
<ul>
<li><a href="controls/getLabel.md" data-raw-source="[getLabel](controls/getLabel.md)">getLabel</a></li>
<li><a href="controls/getName.md" data-raw-source="[getName](controls/getName.md)">getName</a></li>
<li><a href="controls/getParent.md" data-raw-source="[getParent](controls/getParent.md)">getParent</a></li>
<li><a href="controls/getVisible.md" data-raw-source="[getVisible](controls/getVisible.md)">getVisible</a></li>
<li><a href="controls/setDisabled.md" data-raw-source="[setDisabled](controls/setDisabled.md)">setDisabled</a></li>
</ul>
</td>
<td>
<ul>
<li><a href="controls/setFocus.md" data-raw-source="[setFocus](controls/setFocus.md)">setFocus</a></li>
<li><a href="controls/setLabel.md" data-raw-source="[setLabel](controls/setLabel.md)">setLabel</a></li>
<li><a href="controls/setNotification.md" data-raw-source="[setNotification](controls/setNotification.md)">setNotification</a></li>
<li><a href="controls/setVisible.md" data-raw-source="[setVisible](controls/setVisible.md)">setVisible</a></li>
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
<li><a href="controls/getContentWindow.md" data-raw-source="[getContentWindow](controls/getContentWindow.md)">getContentWindow</a></li>
<li><a href="controls/getControlType.md" data-raw-source="[getControlType](controls/getControlType.md)">getControlType</a></li>
<li><a href="controls/getDisabled.md" data-raw-source="[getDisabled](controls/getDisabled.md)">getDisabled</a></li>
<li><a href="controls/getInitialUrl.md" data-raw-source="[getInitialUrl](controls/getInitialUrl.md)">getInitialUrl</a></li>
<li><a href="controls/getLabel.md" data-raw-source="[getLabel](controls/getLabel.md)">getLabel</a></li>

</ul>
</td>
<td>
<ul>
<li><a href="controls/getName.md" data-raw-source="[getName](controls/getName.md)">getName</a></li>  
<li><a href="controls/getObject.md" data-raw-source="[getObject](controls/getObject.md)">getObject</a></li>
<li><a href="controls/getParent.md" data-raw-source="[getParent](controls/getParent.md)">getParent</a></li>
<li><a href="controls/getSrc.md" data-raw-source="[getSrc](controls/getSrc.md)">getSrc</a></li>
<li><a href="controls/getVisible.md" data-raw-source="[getVisible](controls/getVisible.md)">getVisible</a></li>

</ul>
</td>
<td>
<ul>
<li><a href="controls/setDisabled.md" data-raw-source="[setDisabled](controls/setDisabled.md)">setDisabled</a></li>
<li><a href="controls/setFocus.md" data-raw-source="[setFocus](controls/setFocus.md)">setFocus</a></li>
<li><a href="controls/setLabel.md" data-raw-source="[setLabel](controls/setLabel.md)">setLabel</a></li>
<li><a href="controls/setSrc.md" data-raw-source="[setSrc](controls/setSrc.md)">setSrc</a></li>
<li><a href="controls/setVisible.md" data-raw-source="[setVisible](controls/setVisible.md)">setVisible</a></li>
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
<li><a href="controls/addOnPostSearch.md" data-raw-source="[addOnPostSearch](controls/addOnPostSearch.md)">addOnPostSearch</a></li>
<li><a href="controls/addOnResultOpened.md" data-raw-source="[addOnResultOpened](controls/addOnResultOpened.md)">addOnResultOpened</a></li>
<li><a href="controls/addOnSelection.md" data-raw-source="[addOnSelection](controls/addOnSelection.md)">addOnSelection</a></li>
<li><a href="controls/getControlType.md" data-raw-source="[getControlType](controls/getControlType.md)">getControlType</a></li>
<li><a href="controls/getDisabled.md" data-raw-source="[getDisabled](controls/getDisabled.md)">getDisabled</a></li>
<li><a href="controls/getLabel.md" data-raw-source="[getLabel](controls/getLabel.md)">getLabel</a></li>
<li><a href="controls/getName.md" data-raw-source="[getName](controls/getName.md)">getName</a></li>
</ul>
</td>
<td>
<ul>
<li><a href="controls/getParent.md" data-raw-source="[getParent](controls/getParent.md)">getParent</a></li>
<li><a href="controls/getSearchQuery.md" data-raw-source="[getSearchQuery](controls/getSearchQuery.md)">getSearchQuery</a></li>
<li><a href="controls/getSelectedResults.md" data-raw-source="[getSelectedResults](controls/getSelectedResults.md)">getSelectedResults</a></li>
<li><a href="controls/getTotalResultCount.md" data-raw-source="[getTotalResultCount](controls/getTotalResultCount.md)">getTotalResultCount</a></li>
<li><a href="controls/getVisible.md" data-raw-source="[getVisible](controls/getVisible.md)">getVisible</a></li>
<li><a href="controls/openSearchResult.md" data-raw-source="[openSearchResult](controls/openSearchResult.md)">openSearchResult</a></li>
<li><a href="controls/removeOnPostSearch.md" data-raw-source="[removeOnPostSearch](controls/removeOnPostSearch.md)">removeOnPostSearch</a></li>

</ul>
</td>
<td>
<ul>
<li><a href="controls/removeOnResultOpened.md" data-raw-source="[removeOnResultOpened](controls/removeOnResultOpened.md)">removeOnResultOpened</a></li>
<li><a href="controls/removeOnSelection.md" data-raw-source="[removeOnSelection](controls/removeOnSelection.md)">removeOnSelection</a></li>
<li><a href="controls/setFocus.md" data-raw-source="[setFocus](controls/setFocus.md)">setFocus</a></li>
<li><a href="controls/setLabel.md" data-raw-source="[setLabel](controls/setLabel.md)">setLabel</a></li>
<li><a href="controls/setSearchQuery.md" data-raw-source="[setSearchQuery](controls/setSearchQuery.md)">setSearchQuery</a></li>
<li><a href="controls/setVisible.md" data-raw-source="[setVisible](controls/setVisible.md)">setVisible</a></li>
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
<li><a href="controls/addCustomFilter.md" data-raw-source="[addCustomFilter](controls/addCustomFilter.md)">addCustomFilter</a></li>
<li><a href="controls/addCustomView.md" data-raw-source="[addCustomView](controls/addCustomView.md)">addCustomView</a></li>
<li><a href="controls/addNotification.md" data-raw-source="[addNotification](controls/addNotification.md)">addNotification</a></li>
<li><a href="controls/addOnLookupTagClick.md" data-raw-source="[addOnLookupTagClick](controls/addOnLookupTagClick.md)">addOnLookupTagClick</a></li>
<li><a href="controls/addPreSearch.md" data-raw-source="[addPreSearch](controls/addPreSearch.md)">addPreSearch</a></li>
<li><a href="controls/clearNotification.md" data-raw-source="[clearNotification](controls/clearNotification.md)">clearNotification</a></li>
<li><a href="controls/getAttribute.md" data-raw-source="[getAttribute](controls/getAttribute.md)">getAttribute</a></a></li>
<li><a href="controls/getControlType.md" data-raw-source="[getControlType](controls/getControlType.md)">getControlType</a></li>

</ul>
</td>
<td>
<ul>
<li><a href="controls/getDefaultView.md" data-raw-source="[getDefaultView](controls/getDefaultView.md)">getDefaultView</a></li>
<li><a href="controls/getDisabled.md" data-raw-source="[getDisabled](controls/getDisabled.md)">getDisabled</a></li>
<li><a href="controls/getEntityTypes.md" data-raw-source="[getEntityTypes](controls/getEntityTypes.md)">getEntityTypes</a></li>
<li><a href="controls/getLabel.md" data-raw-source="[getLabel](controls/getLabel.md)">getLabel</a></li>
<li><a href="controls/getName.md" data-raw-source="[getName](controls/getName.md)">getName</a></li>
<li><a href="controls/getParent.md" data-raw-source="[getParent](controls/getParent.md)">getParent</a></li>
<li><a href="controls/getVisible.md" data-raw-source="[getVisible](controls/getVisible.md)">getVisible</a></li>
<li><a href="controls/removeOnLookupTagClick.md" data-raw-source="[removeOnLookupTagClick](controls/removeOnLookupTagClick.md)">removeOnLookupTagClick</a></li>
</ul>
</td>
<td>
<ul>
<li><a href="controls/removePreSearch.md" data-raw-source="[removePreSearch](controls/removePreSearch.md)">removePreSearch</a></li>
<li><a href="controls/setDefaultView.md" data-raw-source="[setDefaultView](controls/setDefaultView.md)">setDefaultView</a></li>
<li><a href="controls/setDisabled.md" data-raw-source="[setDisabled](controls/setDisabled.md)">setDisabled</a></li>
<li><a href="controls/setEntityTypes.md" data-raw-source="[setEntityTypes](controls/setEntityTypes.md)">setEntityTypes</a></li>
<li><a href="controls/setFocus.md" data-raw-source="[setFocus](controls/setFocus.md)">setFocus</a></li>
<li><a href="controls/setLabel.md" data-raw-source="[setLabel](controls/setLabel.md)">setLabel</a></li>
<li><a href="controls/setNotification.md" data-raw-source="[setNotification](controls/setNotification.md)">setNotification</a></li>
<li><a href="controls/setVisible.md" data-raw-source="[setVisible](controls/setVisible.md)">setVisible</a></li>
</ul>
</td>
</tr>
</table>

## choices and choice control types

Both choices and choice controls have the same set of methods available.

<table>
<tr>
<td>
<ul>
<li><a href="controls/addNotification.md" data-raw-source="[addNotification](controls/addNotification.md)">addNotification</a></li>
<li><a href="controls/addOption.md" data-raw-source="[addOption](controls/addOption.md)">addOption</a></li>
<li><a href="controls/clearNotification.md" data-raw-source="[clearNotification](controls/clearNotification.md)">clearNotification</a></li>
<li><a href="controls/clearOptions.md" data-raw-source="[clearOptions](controls/clearOptions.md)">clearOptions</a></li>
<li><a href="controls/getAttribute.md" data-raw-source="[getAttribute](controls/getAttribute.md)">getAttribute</a></a></li>
<li><a href="controls/getControlType.md" data-raw-source="[getControlType](controls/getControlType.md)">getControlType</a></li>
</ul>
</td>
<td>
<ul>
<li><a href="controls/getDisabled.md" data-raw-source="[getDisabled](controls/getDisabled.md)">getDisabled</a></li>
<li><a href="controls/getLabel.md" data-raw-source="[getLabel](controls/getLabel.md)">getLabel</a></li>
<li><a href="controls/getName.md" data-raw-source="[getName](controls/getName.md)">getName</a></li>
<li><a href="controls/getOptions.md" data-raw-source="[getOptions](controls/getOptions.md)">getOptions</a></li>
<li><a href="controls/getParent.md" data-raw-source="[getParent](controls/getParent.md)">getParent</a></li>
<li><a href="controls/getVisible.md" data-raw-source="[getVisible](controls/getVisible.md)">getVisible</a></li>

</ul>
</td>
<td>
<ul>
<li><a href="controls/removeoption.md" data-raw-source="[removeOption](controls/removeoption.md)">removeOption</a></li>
<li><a href="controls/setDisabled.md" data-raw-source="[setDisabled](controls/setDisabled.md)">setDisabled</a></li>
<li><a href="controls/setFocus.md" data-raw-source="[setFocus](controls/setFocus.md)">setFocus</a></li>
<li><a href="controls/setLabel.md" data-raw-source="[setLabel](controls/setLabel.md)">setLabel</a></li>
<li><a href="controls/setNotification.md" data-raw-source="[setNotification](controls/setNotification.md)">setNotification</a></li>
<li><a href="controls/setVisible.md" data-raw-source="[setVisible](controls/setVisible.md)">setVisible</a></li>

</ul>
</td>
</tr>
</table>

## quickform control type

See [formContext.ui.quickForms](formcontext-ui-quickforms.md) for information about methods supported for this control type.

## subgrid control type

See [Grids and subgrids](grids.md) for information methods supported for this control type.

## timelinewall control type

The timeline control presents the Posts, Activities, and Notes in a unified view. These are the methods available for this control type.

<table>
<tr>
<td>
<ul>
<li><a href="controls/getControlType.md" data-raw-source="[getControlType](controls/getControlType.md)">getControlType</a></li>
<li><a href="controls/getDisabled.md" data-raw-source="[getDisabled](controls/getDisabled.md)">getDisabled</a></li>
<li><a href="controls/getLabel.md" data-raw-source="[getLabel](controls/getLabel.md)">getLabel</a></li>
<li><a href="controls/getName.md" data-raw-source="[getName](controls/getName.md)">getName</a></li>
</ul>
</td>
<td>
<ul>

<li><a href="controls/getParent.md" data-raw-source="[getParent](controls/getParent.md)">getParent</a></li>
<li><a href="controls/getVisible.md" data-raw-source="[getVisible](controls/getVisible.md)">getVisible</a></li>
<li><a href="controls/refresh.md" data-raw-source="[refresh](controls/refresh.md)">refresh</a></li>
<li><a href="controls/setDisabled.md" data-raw-source="[setDisabled](controls/setDisabled.md)">setDisabled</a></li>
</ul>
</td>
<td>
<ul>
<li><a href="controls/setFocus.md" data-raw-source="[setFocus](controls/setFocus.md)">setFocus</a></li>
<li><a href="controls/setLabel.md" data-raw-source="[setLabel](controls/setLabel.md)">setLabel</a></li>
<li><a href="controls/setVisible.md" data-raw-source="[setVisible](controls/setVisible.md)">setVisible</a></li>
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

<li><a href="controls/getControlType.md" data-raw-source="[getControlType](controls/getControlType.md)">getControlType</a></li>
<li><a href="controls/getDisabled.md" data-raw-source="[getDisabled](controls/getDisabled.md)">getDisabled</a></li>
<li><a href="controls/getLabel.md" data-raw-source="[getLabel](controls/getLabel.md)">getLabel</a></li>
<li><a href="controls/getName.md" data-raw-source="[getName](controls/getName.md)">getName</a></li>
</ul>
</td>
<td>
<ul>

<li><a href="controls/getParent.md" data-raw-source="[getParent](controls/getParent.md)">getParent</a></li>
<li><a href="controls/getState.md" data-raw-source="[getState](controls/getState.md)">getState</a></li>
<li><a href="controls/getVisible.md" data-raw-source="[getVisible](controls/getVisible.md)">getVisible</a></li>
<li><a href="controls/refresh.md" data-raw-source="[refresh](controls/refresh.md)">refresh</a></li>

</ul>
</td>
<td>
<ul>
<li><a href="controls/setDisabled.md" data-raw-source="[setDisabled](controls/setDisabled.md)">setDisabled</a></li>
<li><a href="controls/setFocus.md" data-raw-source="[setFocus](controls/setFocus.md)">setFocus</a></li>
<li><a href="controls/setLabel.md" data-raw-source="[setLabel](controls/setLabel.md)">setLabel</a></li>
<li><a href="controls/setVisible.md" data-raw-source="[setVisible](controls/setVisible.md)">setVisible</a></li>
</ul>
</td>
</tr>
</table>

## web resource control type

A web resource control has the same set of methods available as the iframe control. See [iframe control type](#iframe-control-type)

The Sliverlight web resource has these additional methods: 
<table>
<tr>
<td>
<ul>
<li><a href="controls/getData.md" data-raw-source="[getData](controls/getData.md)">getData</a></li>
<li><a href="controls/setData.md" data-raw-source="[setData](controls/setData.md)">setData</a></li>
</ul>
</td>
</tr>
</table>

> [!TIP]
> If you want to modify all the controls bound to a column on a form, use the controls collection inside the column type. For example, to add notification to each control bound to the `name` column, you can do the following:
 >  ```JavaScript
 >   const notification = { messages: ['Sample Notification on Name Controls'], notificationLevel: 'RECOMMENDATION', uniqueId: 'my_unique_id'};
 >  formContext.getAttribute("name").controls.forEach(control => control.addNotification(notification));
 > ```


### Related topics

[Columns](attributes.md)


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]