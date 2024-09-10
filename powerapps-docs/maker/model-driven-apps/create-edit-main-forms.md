---
title: "Create or edit model-driven app main forms in Power Apps | MicrosoftDocs"
description: "Learn how to create or edit a main form"
ms.custom: ""
ms.date: 05/23/2018
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: <needs new guid>
caps.latest.revision: 18
ms.subservice: mda-maker
ms.author: "matp"
search.audienceType: 
  - maker
---
# Create or edit a model-driven app main form for a table

This article describes how to create or edit a main form for a table.

When a new form is created for a table, its form type is **Main**. When the new form opens, it is identical to the form named **Information**. Columns, sections, tabs, navigation, and properties associated with the form can be edited and the form can then be saved.

Each main form is composed of one or more tabs. Each tab can have one or more sections. Each section contains one or more columns, also called form fields. Forms can be cloned to provide a simpler starting point for form development. To clone a form, open the form you want to copy in the form editor, on the command bar select the down arrow next to **Save**, select **Save As**, enter the name for the new form, and then select **Save**.

> [!NOTE]
> Make sure that you have the System Administrator or System Customizer security role or equivalent permissions within your environment to perform this task.

## How to create or edit a main form
  
1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).

2. Select **Tables** on the left navigation pane, select the table you want, and then select the **Forms** area. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]

3. To create a new main form, on the toolbar select **Add form** > **Main Form**.  
    \-OR-
    To edit an existing main form, select any form with the **Type** of **Main**.
  
4.  Change the form design in any of the following ways, as needed:
    - [Add a column to or remove a column from a form](Add-move-or-delete-fields-on-form.md)
    - [Add a section to or remove a section from a form](add-move-or-delete-sections-on-form.md)
    - [Add a tab to or remove a tab from a form](add-move-or-delete-tabs-on-form.md)
    - [Add or edit a subgrid on a form](form-designer-add-configure-subgrid.md)
    - [Edit form headers](form-designer-header-properties.md)
    - Edit form footers
    
5.  Edit the properties for parts of the form, as needed:
    
    - [Edit form properties](create-and-edit-forms.md#form-properties)
    - [Edit form column properties](Add-move-or-delete-fields-on-form.md#configure-column-properties-on-a-form)  
    - [Edit tab properties](add-move-or-delete-tabs-on-form.md#configure-tabs-on-a-form)
    - [Edit section properties](add-move-or-delete-sections-on-form.md)

6.    When finished editing the form, select **Save** > **Save As**, enter a name for the form, and then select **OK**.

7.    When your customizations are complete, these can be [published](model-driven-app-glossary.md#publish): select **Publish**.
 
### Next steps

[Create and edit a main form walkthrough](create-and-edit-a-model-driven-form.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
