---
title: "Controls in Model-Driven Apps for Dynamics 365"
description: Learn about controls in model-driven apps and the Client API methods available for each control type to change control presentation and behavior.
author: MitiJ
ms.author: mijosh
ms.date: 10/30/2026
ms.reviewer: jdaly
ms.topic: reference
ai-usage: ai-assisted
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# Controls (Client API reference)

In model-driven apps, a control represents an HTML element on the form. Some controls are bound to a specific column, while others represent unbound controls such as an IFRAME, web resource, or subgrid added to the form.

The **control** object provides methods to change the presentation or behavior of a control and identify the corresponding column. Access controls by using one of the following collections: 

- **formContext.ui.controls**
- **formContext.ui Section.controls**
- **formContext.data.entity** **Attribute.controls**

The **formContext**.[getControl](controls/getControl.md) method is a shortcut method to access **formContext.ui.controls.get**. 

> [!NOTE]
> When you perform actions on controls that are tied to a column, consider that the control might appear on the page more than once. Generally, you should perform the same actions for each control for the column. You can loop through the column [controls collection](attributes/controls-collection.md) and perform the actions on each control.

Controls are categorized by type. Use the [getControlType](controls/getControlType.md) method to determine the type of a control. Certain control methods are available only for specific types of controls.

This article provides information about the methods available for each control type. 

[!INCLUDE[cc-terminology](../../../data-platform/includes/cc-terminology.md)]

## Standard control type

These methods are available for a Standard control.

|Method|Description|
|---|---|
|[addNotification](controls/addNotification.md)|Displays an error or recommendation notification with optional actions.|
|[clearNotification](controls/clearNotification.md)|Removes a notification from the control.|
|[getAttribute](controls/getAttribute.md)|Returns the column that the control is bound to.|
|[getControlType](controls/getControlType.md)|Returns the type of the control.|
|[getDisabled](controls/getDisabled.md)|Returns whether the control is disabled.|
|[getLabel](controls/getLabel.md)|Returns the control's label.|
|[getName](controls/getName.md)|Returns the control's name.|
|[getOutputs](controls/getoutputs.md)|Returns a dictionary of the control's output properties.|
|[getParent](controls/getParent.md)|Returns the section that contains the control.|
|[getVisible](controls/getVisible.md)|Returns whether the control is visible.|
|[setDisabled](controls/setDisabled.md)|Enables or disables the control.|
|[setFocus](controls/setFocus.md)|Moves focus to the control.|
|[setLabel](controls/setLabel.md)|Changes the control's label.|
|[setNotification](controls/setNotification.md)|Displays an error message to indicate that data isn't valid.|
|[setVisible](controls/setVisible.md)|Shows or hides the control.|


The following methods for the Standard control are [deprecated](/power-platform/important-changes-coming#some-client-apis-are-deprecated): [addOnKeyPress](/previous-versions/dynamicscrm-2016/developers-guide/gg334266(v=crm.8)#addonkeypress), [fireOnKeyPress](/previous-versions/dynamicscrm-2016/developers-guide/gg334266(v=crm.8)#fireonkeypress), and [removeOnKeyPress](/previous-versions/dynamicscrm-2016/developers-guide/gg334266(v=crm.8)#removeonkeypress).

## IFRAME control type

These methods are available for an IFRAME control.

|Method|Description|
|---|---|
|[getContentWindow](controls/getContentWindow.md)|Returns the content window of the IFRAME or web resource.|
|[getControlType](controls/getControlType.md)|Returns the type of the control.|
|[getDisabled](controls/getDisabled.md)|Returns whether the control is disabled.|
|[getInitialUrl](controls/getInitialUrl.md)|Returns the default URL configured for the IFRAME.|
|[getLabel](controls/getLabel.md)|Returns the control's label.|
|[getName](controls/getName.md)|Returns the control's name.|
|[getObject](controls/getObject.md)|Returns the form object that represents the IFRAME or web resource.|
|[getParent](controls/getParent.md)|Returns the section that contains the control.|
|[getSrc](controls/getSrc.md)|Returns the URL currently displayed in the IFRAME or web resource.|
|[getVisible](controls/getVisible.md)|Returns whether the control is visible.|
|[setDisabled](controls/setDisabled.md)|Enables or disables the control.|
|[setFocus](controls/setFocus.md)|Moves focus to the control.|
|[setLabel](controls/setLabel.md)|Changes the control's label.|
|[setSrc](controls/setSrc.md)|Sets the URL to display in the IFRAME or web resource.|
|[setVisible](controls/setVisible.md)|Shows or hides the control.|

## Kbsearch (knowledge base search) control type

These methods are available for the knowledge base search control.

|Method|Description|
|---|---|
|[addOnPostSearch](controls/addOnPostSearch.md)|Adds an event handler that runs after a search completes.|
|[addOnResultOpened](controls/addOnResultOpened.md)|Adds an event handler that runs when a search result opens.|
|[addOnSelection](controls/addOnSelection.md)|Adds an event handler that runs when a search result is selected.|
|[getControlType](controls/getControlType.md)|Returns the type of the control.|
|[getDisabled](controls/getDisabled.md)|Returns whether the control is disabled.|
|[getLabel](controls/getLabel.md)|Returns the control's label.|
|[getName](controls/getName.md)|Returns the control's name.|
|[getParent](controls/getParent.md)|Returns the section that contains the control.|
|[getSearchQuery](controls/getSearchQuery.md)|Returns the text used as the search criteria.|
|[getSelectedResults](controls/getSelectedResults.md)|Returns the currently selected search result.|
|[getTotalResultCount](controls/getTotalResultCount.md)|Returns the number of search results.|
|[getVisible](controls/getVisible.md)|Returns whether the control is visible.|
|[openSearchResult](controls/openSearchResult.md)|Opens a specified search result.|
|[removeOnPostSearch](controls/removeOnPostSearch.md)|Removes an event handler for search completion.|
|[removeOnResultOpened](controls/removeOnResultOpened.md)|Removes an event handler for opening a search result.|
|[removeOnSelection](controls/removeOnSelection.md)|Removes an event handler for selecting a search result.|
|[setFocus](controls/setFocus.md)|Moves focus to the control.|
|[setLabel](controls/setLabel.md)|Changes the control's label.|
|[setSearchQuery](controls/setSearchQuery.md)|Sets the text used as the search criteria.|
|[setVisible](controls/setVisible.md)|Shows or hides the control.|



>[!NOTE]
>When you add the knowledge base search control to the social pane, the control name is `searchwidgetcontrol_notescontrol`. You can't change this name. 

## Lookup control type

These methods are available for a lookup control.

|Method|Description|
|---|---|
|[addCustomFilter](controls/addCustomFilter.md)|Adds a filter to the lookup results, combined with existing filters by using AND.|
|[addCustomView](controls/addCustomView.md)|Adds a view to the lookup dialog.|
|[addNotification](controls/addNotification.md)|Displays an error or recommendation notification with optional actions.|
|[addOnLookupTagClick](controls/addOnLookupTagClick.md)|Adds an event handler that runs when a lookup tag is clicked.|
|[addPreSearch](controls/addPreSearch.md)|Adds an event handler that runs before a lookup search.|
|[clearNotification](controls/clearNotification.md)|Removes a notification from the control.|
|[getAttribute](controls/getAttribute.md)|Returns the column that the control is bound to.|
|[getControlType](controls/getControlType.md)|Returns the type of the control.|
|[getDefaultView](controls/getDefaultView.md)|Returns the ID of the default lookup view.|
|[getDisabled](controls/getDisabled.md)|Returns whether the control is disabled.|
|[getEntityTypes](controls/getEntityTypes.md)|Returns the table types allowed in the lookup.|
|[getLabel](controls/getLabel.md)|Returns the control's label.|
|[getName](controls/getName.md)|Returns the control's name.|
|[getParent](controls/getParent.md)|Returns the section that contains the control.|
|[getVisible](controls/getVisible.md)|Returns whether the control is visible.|
|[removeOnLookupTagClick](controls/removeOnLookupTagClick.md)|Removes an event handler for lookup tag clicks.|
|[removePreSearch](controls/removePreSearch.md)|Removes an event handler that runs before a lookup search.|
|[setDefaultView](controls/setDefaultView.md)|Sets the default view in the lookup dialog.|
|[setDisabled](controls/setDisabled.md)|Enables or disables the control.|
|[setEntityTypes](controls/setEntityTypes.md)|Sets the table types allowed in the lookup.|
|[setFocus](controls/setFocus.md)|Moves focus to the control.|
|[setLabel](controls/setLabel.md)|Changes the control's label.|
|[setNotification](controls/setNotification.md)|Displays an error message to indicate that data isn't valid.|
|[setVisible](controls/setVisible.md)|Shows or hides the control.|


## Choices and choice control types

Choices and choice controls have the same set of methods available.

|Method|Description|
|---|---|
|[addNotification](controls/addNotification.md)|Displays an error or recommendation notification with optional actions.|
|[addOption](controls/addOption.md)|Adds an option to the control.|
|[clearNotification](controls/clearNotification.md)|Removes a notification from the control.|
|[clearOptions](controls/clearOptions.md)|Removes all options from the control.|
|[getAttribute](controls/getAttribute.md)|Returns the column that the control is bound to.|
|[getControlType](controls/getControlType.md)|Returns the type of the control.|
|[getDisabled](controls/getDisabled.md)|Returns whether the control is disabled.|
|[getLabel](controls/getLabel.md)|Returns the control's label.|
|[getName](controls/getName.md)|Returns the control's name.|
|[getOptions](controls/getOptions.md)|Returns the available options, including the blank option and excluding removed options.|
|[getParent](controls/getParent.md)|Returns the section that contains the control.|
|[getVisible](controls/getVisible.md)|Returns whether the control is visible.|
|[removeOption](controls/removeoption.md)|Removes an option from the control.|
|[setDisabled](controls/setDisabled.md)|Enables or disables the control.|
|[setFocus](controls/setFocus.md)|Moves focus to the control.|
|[setLabel](controls/setLabel.md)|Changes the control's label.|
|[setNotification](controls/setNotification.md)|Displays an error message to indicate that data isn't valid.|
|[setVisible](controls/setVisible.md)|Shows or hides the control.|


## Quick form control type

See [formContext.ui.quickForms](formcontext-ui-quickforms.md) for information about methods supported for this control type.

## Subgrid control type

See [Grids and subgrids](grids.md) for information about methods supported for this control type.

## Timeline wall control type

The timeline control presents the posts, activities, and notes in a unified view. These methods are available for this control type.

|Method|Description|
|---|---|
|[getControlType](controls/getControlType.md)|Returns the type of the control.|
|[getDisabled](controls/getDisabled.md)|Returns whether the control is disabled.|
|[getLabel](controls/getLabel.md)|Returns the control's label.|
|[getName](controls/getName.md)|Returns the control's name.|
|[getParent](controls/getParent.md)|Returns the section that contains the control.|
|[getVisible](controls/getVisible.md)|Returns whether the control is visible.|
|[refresh](controls/refresh.md)|Refreshes the data displayed in the timeline.|
|[setDisabled](controls/setDisabled.md)|Enables or disables the control.|
|[setFocus](controls/setFocus.md)|Moves focus to the control.|
|[setLabel](controls/setLabel.md)|Changes the control's label.|
|[setVisible](controls/setVisible.md)|Shows or hides the control.|

## Timer control type

These methods are available for the timer control.

|Method|Description|
|---|---|
|[getControlType](controls/getControlType.md)|Returns the type of the control.|
|[getDisabled](controls/getDisabled.md)|Returns whether the control is disabled.|
|[getLabel](controls/getLabel.md)|Returns the control's label.|
|[getName](controls/getName.md)|Returns the control's name.|
|[getParent](controls/getParent.md)|Returns the section that contains the control.|
|[getState](controls/getState.md)|Returns the current state of the timer.|
|[getVisible](controls/getVisible.md)|Returns whether the control is visible.|
|[refresh](controls/refresh.md)|Refreshes the data displayed in the timer.|
|[setDisabled](controls/setDisabled.md)|Enables or disables the control.|
|[setFocus](controls/setFocus.md)|Moves focus to the control.|
|[setLabel](controls/setLabel.md)|Changes the control's label.|
|[setVisible](controls/setVisible.md)|Shows or hides the control.|


## Web resource control type

A web resource control has the same set of methods available as the iframe control. See [iframe control type](#iframe-control-type).

## Form component control type

A form component control type has the same set of methods available as the [formContext](../clientapi-form-context.md) on a main form. See [Form component behavior > Client API](../../../../maker/model-driven-apps/form-component-control.md#client-api).

### Related articles

[Columns](attributes.md)


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
