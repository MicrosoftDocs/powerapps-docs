---
title: "Create or edit model-driven app main forms in PowerApps | MicrosoftDocs"
description: "Learn how to create or edit a main form"
ms.custom: ""
ms.date: 05/23/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: <needs new guid>
caps.latest.revision: 18
ms.author: "matp"
manager: "kvivek"
---
# Create or edit a model-driven app main form for an entity 

In this topic you learn how to create or edit a main form for an entity.

When you create a new form for an entity, its form type is Main. When the new form opens, it is identical to the form named Information. You can add or edit fields, sections, tabs, navigation, and properties associated with the form, and then save the form.

Each main form is composed of one or more tabs. Each tab can have one or more sections. Each section contains one or more fields or IFRAMES. If you want to base your new form on an existing one, you can clone a form. 

Make sure that you have the System Administrator or System Customizer security role or equivalent permissions to perform this task.

## How to create or edit a main form
  
1.   On the [PowerApps](https://web.powerapps.com) site, select **Model-driven** (lower left of the navigation pane).  

     ![Model-driven design mode](media/model-driven-switch.png)

> [!IMPORTANT]
> “If the **Model-driven** design mode isn't available, you may need to [Create an environment](https://docs.microsoft.com/powerapps/administrator/create-environment).   
  
2.  Expand **Data**, select **Entities**, select the entity that you want, and then select the **Forms** tab. 

3. To create a new main form, on the toolbar select **Add form** > **Main Form**.  
    \-OR-
    To edit an existing main form, select any form with the **Type** of **Main**.
  
3.  Change the form design in any of the following ways, as needed:
    -	Add a tab to a form
    -	Add a section to a form
    -	Add a field to a form
    -	Add or edit a form IFRAME
    -	Add or edit a sub-grid on a form
    -	Add or edit a form web resource
    -	Add or edit form navigation for related entities
    -	Edit form headers and footers
    -	Remove a tab section field or IFRAME
    -	Enable or disable the Form Assistant
    
4.	Edit the properties for parts of the form, as needed:
    -	Edit form properties
    -	Edit form field properties
    -	Edit tab properties
    -	Edit section properties

5.	Add event scripts, as needed. 

6.	Determine which security roles will be able to see the form. More information: [Assign security roles to a form](https://docs.microsoft.com/dynamics365/customer-engagement/admin/assign-security-roles-form)

7.	Preview how the main form appears and how events function:
    - On the **Home** tab, select **Preview**, and then select **Create Form**, **Update Form**, or **Read-Only Form**.
    - To close the Preview form, on the **File** menu, select **Close**.

8.	When you finish editing the form, select **Save As**, enter a name for the form, and then select **OK**.

9.	When your customizations are complete, publish them:
    -	To publish customizations for only the component you are currently editing, under **Components**, click the entity you have been working on, and then click **Publish**.
    -	To publish customizations for all unpublished components at one time, under **Components**, click **Entities**, and then on the command bar, click **Publish All Customizations**.
    
 
### Next steps  
[Overview of the form editor user interface](form-editor-user-interface-legacy.md)
 
