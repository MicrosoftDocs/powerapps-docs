---
title: Use the model-driven app main form and its components in Power Apps
description: Know how to use the main form and its component in model-driven apps in Power Apps.
keywords: Main forms; Customer service; Customer Service Hub; Dynamics 365
author: Mattp123
ms.subservice: mda-maker
ms.author: matp
ms.date: 02/27/2025
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

Forms in model-driven apps provide the primary means by which users can update records. Forms associated with a table can be accessed via the table designer.

The most versatile form type of the new form is **Main**. However, in addition to main forms, app makers can build quick create, quick view, or card forms. [Learn more about other types of forms](types-forms.md)

This article explains how to edit a main form, and add or change various elements of the form.

Here's an example of a main form within an app. It has several tabs, in addition to exposing the timeline component and a quick view form providing more details associated with the primary contact.

:::image type="content" source="../../maker/model-driven-apps/media/create-and-edit-a-model-driven-form/main-form-accounts_2.png" alt-text="Sample model-driven app":::

## Open the form designer

To edit a form, such as to add or change elements, use the form designer. The form designer lets a maker edit forms for all model-driven apps.

Follow the procedures given below to access the form designer.

> [!NOTE]
> If you create any new solution components in the process of editing the form, the names of the components use the solution publisher customization prefix for the default solution and these components are only be included in the **default solution**. If you want any new solution components to be included in a **specific unmanaged solution**, open the form designer through that unmanaged solution. This helps with the application management lifecycle.

### Access the form designer for an unmanaged solution

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. Select **Solutions** from the left navigation pane. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Open the unmanaged [solution](advanced-navigation.md#solutions) you want to work with. The solution type, managed or unmanaged, is displayed in the **Managed externally?** column.
1. In the list of components, locate the table with the form you want to edit. If the table isn’t there, you need to add it.

#### Add a table to an unmanaged solution

1. With the unmanaged solution opened, on the command bar select **Add Existing** and then select **Table**.
1. All the available tables are listed. Select the table, and then select **Next**.
1. Select the option that's most appropriate, and then select **Add**:
   - For a custom table, select **Include all components**.
   - For a standard table choose **Select components**, and then browse to and select the main form you want to customize, and then select **Add**.

1. The table is added to the solution. In the list of components, open the table, select the **Forms** area, and then open form of type **Main**.
1. In the form designer, make the changes you want.
1. **Save** the form.

#### Publish the changes for use in the app

Certain customizations that make changes to the user interface require that they be published before people can use them in the application. To publish your customization, on the solution **Objects** area command bar, select **Publish all customizations**.

### Access the form designer through the default solution

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).  
1. Select **Tables** on the left navigation pane.
1. Select the table that you want, and then select the **Forms** area.  
1. In the list of forms, open the form of type **Main**.

> [!NOTE]
> If you have made other changes to the app, publish them using the app level publish option. Go to [Validate and publish an app using the app designer](validate-app.md) for more information.

## Form designer user interface

To understand in detail the form designer user interface, go to [Overview of the model-driven form designer](form-designer-overview.md).

## Form properties

To learn more about the form properties, go to [Form properties](create-and-edit-forms.md#form-properties).

## Visibility options

 Several types of form elements have the option to be shown or hidden by default. Tabs, sections, and columns all provide this option. When you use form scripts or business rules, the visibility of these elements can be controlled to create a dynamic form to provide a user interface that adapts to conditions in the form.
  
> [!NOTE]
> Hiding form elements isn't a recommended way to enforce security. There are several ways people can view all the elements and data in the form when elements are hidden. To learn more, go to [Show or hide form elements](visibility-options-legacy.md).
  
## Tab properties  

In the body of a form, tabs provide horizontal separation. Tabs have a label that can be displayed. If the label is displayed, tabs can be expanded or collapsed to show or hide their content by choosing the label. To know in detail about the tab properties, go to [Configure tabs on a form](add-move-or-delete-tabs-on-form.md#configure-tabs-on-a-form).

## Section properties  

A section in a form occupies the space available in a tab column. Sections have a label that can be displayed and a line might be shown below the label. To know in detail about the section properties, go to [Configure sections on a form](add-move-or-delete-sections-on-form.md#configure-sections-on-a-form).
  
## Timeline

The timeline shows related activities for a specific table.  
  
The types of activities supported are task, appointment, phone call, email, social activity, and custom activity.  
  
The timeline also shows notes and, system, and user posts. Timelines show those activities that have the **Regarding** column set to the table you’re viewing. For notes, the **Regarding** column isn’t shown to the user; It's implicit when created from the timeline.  
  
Each activity that’s shown in the timeline, has the same quick actions that are available on the activity’s command bar.  

## Common column properties  

To know in detail about the common column properties, go to [Configure column properties on a form](add-move-or-delete-fields-on-form.md#configure-column-properties-on-a-form).
  
## Special column properties

All columns have the properties listed in [Common column properties - legacy](common-field-properties-legacy.md), but certain columns have additional properties. To know more, go to [Special Column Properties - legacy](special-field-properties-legacy.md).

## Subgrid properties  

You can configure a subgrid on a form to display a list of rows or a chart. To know in detail about the subgrid properties, go to [Add and configure a subgrid component on a form](form-designer-add-configure-subgrid.md).

## Quick view control properties  

A quick view control on a form displays data from a row that is selected in a lookup on the form. To explore the quick view control properties, go to [Add and configure a quick view component on a form](form-designer-add-configure-quickview.md).
  
## Web resource properties

You can add or edit web resources on a form to make it more appealing or useful to app users. Form enabled web resources are images or HTML files. These items are under found on the **Components** tab under **Display** in the form designer.

## External website

You can add website content as an inline frame (iframe) to a form to integrate content from another website within the form. More information: [Add an iframe to a model-driven app main form](iframe-properties-legacy.md)

## Edit navigation

Navigation within the form allows people to view lists of related rows. Each table relationship has properties to control whether it should be shown. More information: [Table relationships advanced options](../data-platform/create-edit-nn-relationships-portal.md#advanced-options)
  
Any table relationships that are configured to  display can be overridden within the form editor.  
  
For step-by-step instructions, go to [Add form navigation for related tables](add-edit-form-navigation-related-entities.md).
  
To enable editing navigation, you must first select **Navigation** from the **Select** group on the **Home** tab.  
  
In the Relationship Explorer, you can filter by 1:N (one-to-many) or N:N (many-to-many) relationships, or view all available relationships. The **Only show unused relationships checkbox** is disabled and selected. So you can only add each relationship one time.  
  
To add a relationship from the **Relationship Explorer** just double-click it and it will be added below the currently selected relationship in the navigation area. Double-click a relationship in the navigation area and you can change the label on the **Display** tab. On the **Name** tab, you can see information about the relationship. Use the **Edit** button to open the definition of the table.  
  
There are five groups in the navigation area. You can drag them to reposition them and double-click them to change the label, but you can’t remove them. These groups are displayed only when there's something in them. If you don’t want a group to appear, just don’t add anything to it.  
  
## Configure event handlers  

An event handler consists of a reference to a JavaScript web resource and a function defined within that web resource that will execute when the event occurs. To know more about configuring event handlers, go to [Configure event handlers](configure-event-handlers-legacy.md).
  
## Next steps

[Create and design forms](create-design-forms.md)

[Create and edit quick create forms](create-edit-quick-view-forms.md)   

[Create and edit quick view forms](create-edit-quick-view-forms.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
