---
title: "Create or edit model-driven app main forms in Power Apps | MicrosoftDocs"
description: "Learn how to create or edit a main form"
ms.custom: ""
ms.date: 05/23/2018
ms.reviewer: ""
ms.service: powerapps
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
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Create or edit a model-driven app main form for a table 

This article describes how to create or edit a main form for an table.

When a new form is created for a table, its form type is **Main**. When the new form opens, it is identical to the form named **Information**. Columns, sections, tabs, navigation, and properties associated with the form can be edited and the form can then be saved.

Each main form is composed of one or more **tabs**. Each tab can have one or more **sections**. Each section contains one or more **columns**, or fields. Forms can be cloned to provide a simpler starting point for form development.

> [!NOTE]
> Make sure that the app developer has the System Administrator or System Customizer security role or equivalent permissions within your environment to perform this task.

## How to create or edit a main form
  
1.   Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).

2.  Expand **Data**, select **Tables**, select the table required, and then select the **Forms** tab.

3. To create a new main form, on the toolbar select **Add form** > **Main Form**.  
    \-OR-
    To edit an existing main form, select any form with the **Type** of **Main**.
  
3.  Change the form design in any of the following ways, as needed:
    - [Add a column to or remove a column from a form](Add-move-or-delete-fields-on-form)
    - [Add a section to or remove a section from a form](add-move-or-delete-sections-on-form)
    - [Add a tab to or remove a tab from a form](add-move-or-delete-tabs-on-form.md)
    - [Add or edit a sub-grid on a form](form-designer-add-configure-subgrid)
    - [Edit form headers](form-designer-header-properties)
    - Edit form footers
    
4.  Edit the properties for parts of the form, as needed:
    
    - [Edit form properties](create-and-edit-forms.md#configure-a-form)
    - [Edit form column properties](Add-move-or-delete-fields-on-form#configure-columns-on-a-form)  
    - [Edit tab properties](add-move-or-delete-tabs-on-form.md#configure-tabs-on-a-form)
    - [Edit section properties](add-move-or-delete-sections-on-form)

5.    When finished editing the form, select **Save** > **Save As**, enter a name for the form, and then select **OK**.

6.    When your customizations are complete, these can be [published](model-driven-app-glossary.md#publish): select **Publish**.
 
### Next steps  
[Overview of the model-driven form designer](form-designer-overview.md)

[Overview of the form editor user interface](form-editor-user-interface-legacy.md)
 


[!INCLUDE[footer-include](../../includes/footer-banner.md)]