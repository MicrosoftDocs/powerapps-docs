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

In this topic you learn how to create or edit a main form for an table.

When you create a new form for a table, its form type is Main. When the new form opens, it is identical to the form named Information. You can add or edit columns, sections, tabs, navigation, and properties associated with the form, and then save the form.

Each main form is composed of one or more tabs. Each tab can have one or more sections. Each section contains one or more columns. If you want to base your new form on an existing one, you can clone a form. 

Make sure that you have the System Administrator or System Customizer security role or equivalent permissions to perform this task.

## How to create or edit a main form
  
1.   Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).

2.  Expand **Dataverse**, select **Tables**, select the table that you want, and then select the **Forms** tab. 

3. To create a new main form, on the toolbar select **Add form** > **Main Form**.  
    \-OR-
    To edit an existing main form, select any form with the **Type** of **Main**.
  
3.  Change the form design in any of the following ways, as needed:
    - Add a tab to a form
    - Add a section to a form
    - Add a column to a form
    - Add or edit a sub-grid on a form
    - Edit form headers and footers
    - Remove a tab section column
    
4.  Edit the properties for parts of the form, as needed:
    - Edit form properties
    - Edit form column properties
    - Edit tab properties
    - Edit section properties

5.    When you finish editing the form, select **Save** > **Save As**, enter a name for the form, and then select **OK**.

6.    When your customizations are complete, you can publish them: select **Publish**.
 
### Next steps  
[Overview of the model-driven form designer](form-designer-overview.md)

[Overview of the form editor user interface](form-editor-user-interface-legacy.md)
 


[!INCLUDE[footer-include](../../includes/footer-banner.md)]