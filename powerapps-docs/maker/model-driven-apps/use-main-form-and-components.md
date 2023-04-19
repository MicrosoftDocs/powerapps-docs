---
title: Use the model-driven app main form and its components in Power Apps | Microsoft Docs
description: Know how to use the main form and its components in Unified Interface apps
keywords: Main forms; Customer service; Customer Service Hub; Dynamics 365
author: Mattp123
ms.subservice: mda-maker
ms.author: matp
ms.date: 06/06/2018

ms.topic: how-to
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
ms.assetid: 43bfface-4dc2-411d-99a1-83e934646989
search.audienceType: 
  - maker
---
# Use the model-driven app main form and its components



Forms in model-driven apps provide the primary means by which users can update records.  Forms associated with a table can be accessed via the table designer.

The most versatile form type of the new form is **Main**. However, in addition to main forms, app makers can build quick create, quick view, or card forms.  [Learn more about other types of forms](types-forms.md)

This article explains how to edit a main form, and add or change various elements of the form.

Below is an example of a main form within an app. It has several tabs, in addition to exposing the timeline component and a quick view form providing more details associated with the primary contact.

:::image type="content" source="../../maker/model-driven-apps/media/create-and-edit-a-model-driven-form/main-form-accounts_2.png" alt-text="Sample model-driven app":::

## Open the form designer

To edit a form, such as to add or change elements, use the form designer. The form designer lets a maker edit forms for all model-driven apps.

Follow the procedures given below to access the form designer.

> [!NOTE]
> If you create any new solution components in the process of editing the form, the names of the components will use the solution publisher customization prefix for the default solution and these components will only be included in the **default solution**. If you want any new solution components to be included in a **specific unmanaged solution**, open the form designer through that unmanaged solution.  This will help with the application management lifecycle.

### Access the form designer for an unmanaged solution

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. Select **Solutions** from the left navigation pane. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Open the unmanaged [solution](advanced-navigation.md#solutions) you want to work with. The solution type, managed or unmanaged, is displayed in the **Managed externally?** column.
1. In the list of components, locate the table with the form you want to edit. If the table isn’t there, you’ll need to add it.

#### Add a table to an unmanaged solution

1. With the unmanaged solution opened, on the command bar select **Add Existing** and then select **Table**.
1. All the available tables are listed.  Select the table, and then select **Next**.
1. Select the option that's most appropriate, and then select **Add**:
   - For a custom table, select **Include all components**.
   - For a standard table choose **Select components**, and then browse to and select the main form you want to customize, and then select **Add**.

1. The table is added to the solution. In the list of components, open the table, select the **Forms** area, and then open form of type **Main**.

6. In the form designer, make the changes you want.

7. **Save** the form.

#### Publish the changes for use in the app

Certain customizations that make changes to the user interface require that they be published before people can use them in the application. To publish your customization, on the solution explorer toolbar, select **Publish All Customizations**.

### Access the form designer through the default solution

1.  Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).  

2.  Expand **Data**, select **Tables**, select the table that you want, and then select the **Forms** area.  

3. In the list of forms, open the form of type **Main**.

> [!NOTE]
> If you have made other changes to the app, publish them using the app level publish option. See [Validate and publish an app using the app designer](validate-app.md) for more information.

## Form designer user interface

To understand in detail the form designer user interface, see [Overview of the model-driven form designer](form-designer-overview.md).

## Form properties

To learn more about the form properties, see [Form properties - legacy](form-properties-legacy.md).

## Visibility options

 Several types of form elements have the option to be shown or hidden by default. Tabs, sections, and columns all provide this option. Using form scripts or business rules, the visibility of these elements can be controlled to create a dynamic form to provide a user interface that adapts to conditions in the form.
  
> [!NOTE]
>  Hiding form elements is not a recommended way to enforce security. There are several ways people can view all the elements and data in the form when elements are hidden. To learn more, see [Show or hide form elements](visibility-options-legacy.md). 
  
## Tab properties  

In the body of a form, tabs provide horizontal separation. Tabs have a label that can be displayed. If the label is displayed, tabs can be expanded or collapsed to show or hide their content by choosing the label. To know in detail about the tab properties, see [Tab properties](tab-properties-legacy.md).


## Section properties  

A section in a form occupies the space available in a tab column. Sections have a label that can be displayed and a line may be shown below the label. To know in detail about the section properties, see [Section properties](section-properties-legacy.md).
  
## Timeline  
 The Timeline shows related activities for a specific table.  
  
 The following types of activities are supported: Task, appointment, phone call, email, social activity, custom activity.  
  
 The Timeline also shows notes and, system and user posts. It shows those activities that have **Regarding** column set to the table you’re viewing. For notes, the **Regarding** column isn’t shown to the user; It is implicit when created from the Timeline.  
  
 Each activity that’s shown in the Timeline, will have the same quick actions that are available on the activity’s command bar.  

## Common column properties  

To know in detail about the common column properties, see [Common column properties](common-field-properties-legacy.md). 
  
## Special column properties  
 All columns have the properties listed in [Common column properties - legacy](common-field-properties-legacy.md), but certain columns have additional properties. To know more, see [Special Column Properties - legacy](special-field-properties-legacy.md).

  
## Subgrid properties  

You can configure a subgrid on a form to display a list of rows or a chart. To know in detail about the subgrid properties, see [Subgrid properties - legacy](sub-grid-properties-legacy.md).

## Quick view control properties  

A quick view control on a form displays data from a row that is selected in a lookup on the form. To explore the quick view control properties, see [Quick view control properties - legacy](quick-view-control-properties-legacy.md).
  
## Web resource properties  

You can add or edit web resources on a form to make it more appealing or useful to app users. Form enabled web resources are images, HTML files, or Silverlight controls. Know in detail about the Web resource properties. Go to [Web resource properties - legacy](web-resource-properties-legacy.md). 
  
## IFRAME properties  

You can add iFrames to a form to integrate content from another website within a form. To know more about the IFRAME properties, see [IFRAME properties - legacy](iframe-properties-legacy.md). 
  
## Edit navigation  
 Navigation within the form allows people to view lists of related rows. Each table relationship has properties to control whether it should be shown. More information: [Navigation Pane Item for Primary Table](../data-platform/create-edit-1n-relationships-solution-explorer.md#navigation-pane-item-for-primary-table)
  
 Any table relationships that are configured to be displayed can be overridden within the form editor.  
  
 For step-by-step instructions, see [Add form navigation for related tables](add-edit-form-navigation-related-entities.md).
  
 To enable editing navigation, you must first select **Navigation** from the **Select** group on the **Home** tab.  
  
 In the Relationship Explorer, you can filter by 1:N (one-to-many) or N:N (many-to-many) relationships, or view all available relationships. The **Only show unused relationships checkbox** is disabled and selected. So you can only add each relationship one time.  
  
 To add a relationship from the **Relationship Explorer** just double-click it and it will be added below the currently selected relationship in the navigation area. Double-click a relationship in the navigation area and you can change the label on the **Display** tab. On the **Name** tab, you can see information about the relationship. Use the **Edit** button to open the definition of the table.  
  
 There are five groups in the navigation area. You can drag them to reposition them and double-click them to change the label, but you can’t remove them. These groups are displayed only when there is something in them. If you don’t want a group to appear, just don’t add anything to it.  
  
## Configure event handlers  

An event handler consists of a reference to a JavaScript web resource and a function defined within that web resource that will execute when the event occurs. To know more about configuring event handlers, see [Configure event handlers](configure-event-handlers-legacy.md). 
  
## Next steps  
 [Create and design forms](create-design-forms.md)   
 [Create and edit quick create forms](create-edit-quick-view-forms.md)   
 [Create and edit quick view forms](create-edit-quick-view-forms.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
