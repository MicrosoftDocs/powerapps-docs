---
title: "Create and design model-driven app forms | MicrosoftDocs"
description: "Overview of model-driven forms in Power Apps"
ms.collection: get-started
ms.date: 08/15/2023
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "overview"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
ms.assetid: 99c795e0-9165-4112-85b1-6b5e1a4aa5ec
caps.latest.revision: 33
ms.subservice: mda-maker
ms.author: "matp"
author: "Mattp123"
tags: 
  - "Links to topic not migrated"
search.audienceType: 
  - maker
---
# Create and design model-driven app forms 

With Power Apps model-driven apps, forms provide the user interface that people use to interact with the data they need to do their work. It's important that the forms people use are designed to allow them to find or enter the information they need efficiently.

:::image type="content" source="../../maker/model-driven-apps/media/form-no-header.png" alt-text="Example model-driven App form":::

In the default solution or an unmanaged solution, it's possible to create new forms or edit existing forms for all tables that allow form customization.

## Model-driven app form UI enhancements

Form UI enhancements consist of multiple small changes to improve data presentation and usability of model-driven app forms:

- Forms have a light gray background, which removes the white-on-white section treatment that helps users by providing easier visual navigation.
- There's a better delineation between sections as white space is reduced and shadow and rounded corners to borders are added. 
- Form field dividers are removed and consistent font styling is used across section labels.
- The **Related** tab has an added chevron to indicate the dropdown flyout, which opens-ups when you select it.

   :::image type="content" source="media/form-ux1.png" alt-text="Form UI enhancements screenshot":::

Also, quick view form labels are displayed on top instead of icons.

:::image type="content" source="media/form-ux2.png" alt-text="Form UI enhancements screenshot of related records layout":::

## Forms and solutions

This section describes form customization when the form is in an unmanaged or managed solution.

### Forms inside unmanaged solutions

In an unmanaged solution, it's possible to edit the properties, including columns, views, and forms, for an unmanaged custom table that was created for the solution.  Unmanaged solutions are where app makers and developers go to author changes that they require and typically exist in a development environment.

### Forms inside managed solutions

In a managed solution, typically in a production environment, it isn't possible by default to create new forms or edit existing forms for tables. However, if the managed properties for a table in the managed solution are set to allow customization, you can add or edit forms for that table.

[Learn more about solutions](../../maker/data-platform/solutions-overview.md)

<a name="BKMK_TypesOfForms"></a>
## Form types
There are different types of forms, and each type has a specific functionality or use.  These include:

- Main (the main user interface).
- Quick create (rapid data entry).
- Quick view (to see related data).
- Card form (a compact view).
  
More information: [Types of forms in Power Apps](types-forms.md).  
 
<a name="BKMK_FormDifferencesByEntity"></a>   

## Create or edit a form

The fundamentals of building a model-driven app include creating a table, configuring data views, and creating and editing forms.

Before you begin to build forms, it's worth determining whether you have all the columns necessary to solve your business problem. Additionally, you should have an understanding how to lay these out in terms of sections and tabs.  Broadly speaking, the complexity of your forms are a reflection of the number of columns in your table in addition to the complexity of your business process.

[Learn to create, edit, or configure forms using the form designer](create-and-edit-forms.md)

## Delete a form

To delete a form, sign in to Power Apps and go to **Solutions** > Open the solution you want > select the table that you want > **Forms** area. Select the form, and then select **Delete** on the command bar.

There are a couple of reasons you may not be able to delete a form.

|Reason  |Work around  |
|---------|---------|
| Every table requires at least one main form and it's the only main form for the table.   |  Create a new main form for the table. Then delete the main form you tried earlier.  More information: [Create a form](create-and-edit-forms.md#create-a-form)   |
| Every table requires one designated fallback form and it's the only fallback form.   | Create a new form for the table and set as the fallback. Or designate another existing form as the fallback form. Then delete the form you tried earlier. More information: [Set the fallback form for a table](control-access-forms.md#set-the-fallback-form-for-a-table)     |

## Controlling the display of a form within an app

Tables can have multiple forms.  The use of a form is controlled through the model-driven app. This allows makers to use the same table in different ways depending on the audience, by controlling the display.

By default all forms are made available to users. However, through the app designer a specific form can be restricted.

### Change the forms displayed and form order

Makers change the forms displayed in an app from the app designer. More information: [Manage forms](create-add-remove-forms-views-dashboards.md#manage-forms)

Makers can also change the form order, fallback forms, and the default form for a table from the table hub. More information:  [Set the form order](assign-form-order.md#set-the-form-order)

## Updated versus classic tables

Power Apps provides many options for designing forms using the form designer.
  
There are still a number of tables, referred to here as classic tables, that retain the appearance and capabilities from earlier versions. These tables are used less often. They're listed here:  

:::row:::
   :::column span="":::
      Address
   :::column-end:::
   :::column span="":::
      Article
   :::column-end:::
   :::column span="":::
      Article Comment
   :::column-end:::
   :::column span="":::
      Bulk Delete Operation
   :::column-end:::
   :::column span="":::
      Connection
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      Discount
   :::column-end:::
   :::column span="":::
      Discount List
   :::column-end:::
   :::column span="":::
      Document Location
   :::column-end:::
   :::column span="":::
      Email Attachment
   :::column-end:::
   :::column span="":::
      Follow
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      Goal
   :::column-end:::
   :::column span="":::
      Goal Metric
   :::column-end:::
   :::column span="":::
      Import Source File
   :::column-end:::
   :::column span="":::
      Invoice Product
   :::column-end:::
   :::column span="":::
      Order Product
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      Price List
   :::column-end:::
   :::column span="":::
      Queue Item
   :::column-end:::
   :::column span="":::
      Quote Product
   :::column-end:::
   :::column span="":::
      Rollup Field
   :::column-end:::
   :::column span="":::
      Rollup Query
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      Saved View
   :::column-end:::
   :::column span="":::
      Service
   :::column-end:::
   :::column span="":::
      Service Activity
   :::column-end:::
   :::column span="":::
      SharePoint Site
   :::column-end:::
   :::column span="":::
      Site
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      Territory
   :::column-end:::
   :::column span="":::
      Unit
   :::column-end:::
   :::column span="":::
      Unit Group
   :::column-end:::
   :::column span="":::
             
   :::column-end:::
   :::column span="":::
           
   :::column-end:::
:::row-end:::

## Main form dialogs

With the client API, you can use main form dialogs so users can open a related row table on a parent or base form without navigating away from the form. More information: [Open main form in a dialog using client API](../../developer/model-driven-apps/customize-entity-forms.md#open-main-form-in-a-dialog-using-client-api)

## Next steps

[Understanding the form types available](types-forms.md)

[Assign form order](assign-form-order.md) <br />
[Control access to forms](control-access-forms.md) <br />
[How main forms appear in different clients](main-form-presentations.md) <br />


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
