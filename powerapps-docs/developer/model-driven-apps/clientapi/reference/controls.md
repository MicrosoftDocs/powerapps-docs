---
title: "Controls in model-driven apps for Dynamics 365"
description: A control represents an HTML element present on the form.
author: MitiJ
ms.author: mijosh
ms.date: 01/06/2023
ms.reviewer: jdaly
ms.topic: reference
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# Controls (Client API reference)

A control represents an HTML element present on the form. Some controls are bound to a specific column, whereas others might represent unbound controls such as an IFRAME, web resource, or a subgrid added to the form.

The **control** object provides methods to change the presentation or behavior of a control and identify the corresponding column. You access controls using one of the following collections: 

- **formContext.ui.controls**
- **formContext.ui Section.controls**
- **formContext.data.entity** **Attribute.controls**

The **formContext**.[getControl](controls/getControl.md) method is a shortcut method to access **formContext.ui.controls.get**. 

Controls are categorized by type. You can determine the type of a control by using the [getControlType](controls/getControlType.md) method. Certain control methods are only available for specific types of controls.

This article provides information about the methods available per control type. 

[!INCLUDE[cc-terminology](../../../data-platform/includes/cc-terminology.md)]

## Standard control type

These are the methods available for a Standard control.

:::row:::
   :::column:::
      [addNotification](controls/addNotification.md)
   :::column-end:::
   :::column:::
      [clearNotification](controls/clearNotification.md)
   :::column-end:::
   :::column:::
      [getAttribute](controls/getAttribute.md)
   :::column-end:::
   :::column:::
      [getControlType](controls/getControlType.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column:::
      [getDisabled](controls/getDisabled.md)
   :::column-end:::
   :::column:::
      [getLabel](controls/getLabel.md)
   :::column-end:::
   :::column:::
      [getName](controls/getName.md)
   :::column-end:::
   :::column:::
      [getOutputs](controls/getoutputs.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column:::
      [getParent](controls/getParent.md)
   :::column-end:::
   :::column:::
      [getVisible](controls/getVisible.md)
   :::column-end:::
   :::column:::
      [setDisabled](controls/setDisabled.md)
   :::column-end:::
   :::column:::
      [setFocus](controls/setFocus.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column:::
      [setLabel](controls/setLabel.md)
   :::column-end:::
   :::column:::
      [setNotification](controls/setNotification.md)
   :::column-end:::
   :::column:::
      [setVisible](controls/setVisible.md)
   :::column-end:::
   :::column:::
      &nbsp;
   :::column-end:::
:::row-end:::


The following methods for the Standard control are [deprecated](/dynamics365/get-started/whats-new/customer-engagement/important-changes-coming#some-client-apis-are-deprecated) in this release: `addOnKeyPress`, `fireOnKeyPress`, and `removeOnKeyPress`.

## IFRAME control type

These methods are available for an IFRAME control.

:::row:::
   :::column:::
      [getContentWindow](controls/getContentWindow.md)
   :::column-end:::
   :::column:::
      [getControlType](controls/getControlType.md)
   :::column-end:::
   :::column:::
      [getDisabled](controls/getDisabled.md)
   :::column-end:::
   :::column:::
      [getInitialUrl](controls/getInitialUrl.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column:::
      [getLabel](controls/getLabel.md)
   :::column-end:::
   :::column:::
      [getName](controls/getName.md)
   :::column-end:::
   :::column:::
      [getObject](controls/getObject.md)
   :::column-end:::
   :::column:::
      [getParent](controls/getParent.md)
   :::column-end:::   
:::row-end:::
:::row:::
   :::column:::
      [getSrc](controls/getSrc.md)
   :::column-end:::
   :::column:::
      [getVisible](controls/getVisible.md)
   :::column-end:::
   :::column:::
      [setDisabled](controls/setDisabled.md)
   :::column-end:::
   :::column:::
      [setFocus](controls/setFocus.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column:::
      [setLabel](controls/setLabel.md)
   :::column-end:::
   :::column:::
      [setSrc](controls/setSrc.md)
   :::column-end:::
   :::column:::
      [setVisible](controls/setVisible.md)
   :::column-end:::
   :::column:::
      &nbsp;
   :::column-end:::
:::row-end:::

## Kbsearch (Knowledge base search) control type

These methods are available for knowledge base search control.

:::row:::
   :::column:::
      [addOnPostSearch](controls/addOnPostSearch.md)
   :::column-end:::
   :::column:::
      [addOnResultOpened](controls/addOnResultOpened.md)
   :::column-end:::
   :::column:::
      [addOnSelection](controls/addOnSelection.md)
   :::column-end:::
   :::column:::
      [getControlType](controls/getControlType.md)
   :::column-end:::   
:::row-end:::
:::row:::
   :::column:::
      [getDisabled](controls/getDisabled.md)
   :::column-end:::
   :::column:::
      [getLabel](controls/getLabel.md)
   :::column-end:::
   :::column:::
      [getName](controls/getName.md)
   :::column-end:::
   :::column:::
      [getParent](controls/getParent.md)
   :::column-end:::   
:::row-end:::
:::row:::
   :::column:::
      [getSearchQuery](controls/getSearchQuery.md)
   :::column-end:::
   :::column:::
      [getSelectedResults](controls/getSelectedResults.md)
   :::column-end:::
   :::column:::
      [getTotalResultCount](controls/getTotalResultCount.md)
   :::column-end:::
   :::column:::
      [getVisible](controls/getVisible.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column:::
      [openSearchResult](controls/openSearchResult.md)
   :::column-end:::
   :::column:::
      [removeOnPostSearch](controls/removeOnPostSearch.md)
   :::column-end:::
   :::column:::
      [removeOnResultOpened](controls/removeOnResultOpened.md)
   :::column-end:::
   :::column:::
      [removeOnSelection](controls/removeOnSelection.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column:::
      [setFocus](controls/setFocus.md)
   :::column-end:::
   :::column:::
      [setLabel](controls/setLabel.md)
   :::column-end:::
   :::column:::
      [setSearchQuery](controls/setSearchQuery.md)
   :::column-end:::
   :::column:::
      [setVisible](controls/setVisible.md)
   :::column-end:::
:::row-end:::



>[!NOTE]
>When the knowledge base search control is added to the social pane, the name of the control will be `searchwidgetcontrol_notescontrol`. This name can't be changed. 

## Lookup control type

These methods are available for a lookup control.

:::row:::
   :::column:::
      [addCustomFilter](controls/addCustomFilter.md)
   :::column-end:::
   :::column:::
      [addCustomView](controls/addCustomView.md)
   :::column-end:::
   :::column:::
      [addNotification](controls/addNotification.md)
   :::column-end:::
   :::column:::
      [addOnLookupTagClick](controls/addOnLookupTagClick.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column:::
      [addPreSearch](controls/addPreSearch.md)
   :::column-end:::
   :::column:::
      [clearNotification](controls/clearNotification.md)
   :::column-end:::
   :::column:::
      [getAttribute](controls/getAttribute.md)
   :::column-end:::
   :::column:::
      [getControlType](controls/getControlType.md)
   :::column-end:::   
:::row-end:::
:::row:::
   :::column:::
      [getDefaultView](controls/getDefaultView.md)
   :::column-end:::
   :::column:::
      [getDisabled](controls/getDisabled.md)
   :::column-end:::
   :::column:::
      [getEntityTypes](controls/getEntityTypes.md)
   :::column-end:::
   :::column:::
      [getLabel](controls/getLabel.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column:::
      [getName](controls/getName.md)
   :::column-end:::
   :::column:::
      [getParent](controls/getParent.md)
   :::column-end:::
   :::column:::
      [getVisible](controls/getVisible.md)
   :::column-end:::
   :::column:::
      [removeOnLookupTagClick](controls/removeOnLookupTagClick.md)
   :::column-end:::   
:::row-end:::
:::row:::
   :::column:::
      [removePreSearch](controls/removePreSearch.md)
   :::column-end:::
   :::column:::
      [setDefaultView](controls/setDefaultView.md)
   :::column-end:::
   :::column:::
      [setDisabled](controls/setDisabled.md)
   :::column-end:::
   :::column:::
      [setEntityTypes](controls/setEntityTypes.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column:::
      [setFocus](controls/setFocus.md)
   :::column-end:::
   :::column:::
      [setLabel](controls/setLabel.md)
   :::column-end:::
   :::column:::
      [setNotification](controls/setNotification.md)
   :::column-end:::
   :::column:::
      [setVisible](controls/setVisible.md)
   :::column-end:::
:::row-end:::




## Choices and choice control types

Both choices and choice controls have the same set of methods available.

:::row:::
   :::column:::
      [addNotification](controls/addNotification.md)
   :::column-end:::
   :::column:::
      [addOption](controls/addOption.md)
   :::column-end:::
   :::column:::
      [clearNotification](controls/clearNotification.md)
   :::column-end:::
   :::column:::
      [clearOptions](controls/clearOptions.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column:::
      [getAttribute](controls/getAttribute.md)
   :::column-end:::
   :::column:::
      [getControlType](controls/getControlType.md)
   :::column-end:::
   :::column:::
      [getDisabled](controls/getDisabled.md)
   :::column-end:::
   :::column:::
      [getLabel](controls/getLabel.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column:::
      [getName](controls/getName.md)
   :::column-end:::
   :::column:::
      [getOptions](controls/getOptions.md)
   :::column-end:::
   :::column:::
      [getParent](controls/getParent.md)
   :::column-end:::
   :::column:::
      [getVisible](controls/getVisible.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column:::
      [removeOption](controls/removeoption.md)
   :::column-end:::
   :::column:::
      [setDisabled](controls/setDisabled.md)
   :::column-end:::
   :::column:::
      [setFocus](controls/setFocus.md)
   :::column-end:::
   :::column:::
      [setLabel](controls/setLabel.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column:::
      [setNotification](controls/setNotification.md)
   :::column-end:::
   :::column:::
      [setVisible](controls/setVisible.md)
   :::column-end:::
   :::column:::
      &nbsp;
   :::column-end:::
   :::column:::
      &nbsp;
   :::column-end:::
:::row-end:::


## Quickform control type

See [formContext.ui.quickForms](formcontext-ui-quickforms.md) for information about methods supported for this control type.

## Subgrid control type

See [Grids and subgrids](grids.md) for information methods supported for this control type.

## Timelinewall control type

The timeline control presents the Posts, Activities, and Notes in a unified view. These methods are available for this control type.

:::row:::
   :::column:::
      [getControlType](controls/getControlType.md)
   :::column-end:::
   :::column:::
      [getDisabled](controls/getDisabled.md)
   :::column-end:::
   :::column:::
      [getLabel](controls/getLabel.md)
   :::column-end:::
   :::column:::
      [getName](controls/getName.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column:::
      [getParent](controls/getParent.md)
   :::column-end:::
   :::column:::
      [getVisible](controls/getVisible.md)
   :::column-end:::
   :::column:::
      [refresh](controls/refresh.md)
   :::column-end:::
   :::column:::
      [setDisabled](controls/setDisabled.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column:::
      [setFocus](controls/setFocus.md)
   :::column-end:::
   :::column:::
      [setLabel](controls/setLabel.md)
   :::column-end:::
   :::column:::
      [setVisible](controls/setVisible.md)
   :::column-end:::
   :::column:::
      &nbsp;
   :::column-end:::
:::row-end:::

## Timer control type

These methods are available for the timer control.

:::row:::
   :::column:::
      [getControlType](controls/getControlType.md)
   :::column-end:::
   :::column:::
      [getDisabled](controls/getDisabled.md)
   :::column-end:::
   :::column:::
      [getLabel](controls/getLabel.md)
   :::column-end:::
   :::column:::
      [getName](controls/getName.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column:::
      [getParent](controls/getParent.md)
   :::column-end:::
   :::column:::
      [getState](controls/getState.md)
   :::column-end:::
   :::column:::
      [getVisible](controls/getVisible.md)
   :::column-end:::
   :::column:::
      [refresh](controls/refresh.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column:::
      [setDisabled](controls/setDisabled.md)
   :::column-end:::
   :::column:::
      [setFocus](controls/setFocus.md)
   :::column-end:::
   :::column:::
      [setLabel](controls/setLabel.md)
   :::column-end:::
   :::column:::
      [setVisible](controls/setVisible.md)
   :::column-end:::
:::row-end:::


## Web resource control type

A web resource control has the same set of methods available as the iframe control. See [iframe control type](#iframe-control-type)

The Silverlight web resource has these extra methods: 

- [getData](controls/getData.md)
- [setData](controls/setData.md)

> [!TIP]
> If you want to modify all the controls bound to a column on a form, use the controls collection inside the column type. For example, to add notification to each control bound to the `name` column, you can do the following:
 >  ```JavaScript
 >   const notification = { messages: ['Sample Notification on Name Controls'], notificationLevel: 'RECOMMENDATION', uniqueId: 'my_unique_id'};
 >  formContext.getAttribute("name").controls.forEach(control => control.addNotification(notification));
 > ```

## Form component control type

A form component control type has the same set of methods available as the [formContext](../clientapi-form-context.md) on a main form. See [Form component behavior > Client API](../../../../maker/model-driven-apps/form-component-control.md#client-api)

### Related articles

[Columns](attributes.md)


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
