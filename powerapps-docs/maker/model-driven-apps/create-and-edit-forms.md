---
title: "Create and edit forms using the model-driven form designer | MicrosoftDocs"
ms.custom: ""
ms.date: 12/27/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "get-started-article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
author: "Aneesmsft"
ms.author: "matp"
manager: "kvivek"
tags: 
  - "PowerApps maker portal impact"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---

# Create and edit forms using the form designer 
[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Use the new form designer to create and design forms for model-driven apps.

> [!IMPORTANT]
> The new model-driven form designer currently supports creating and editing main forms only. More information: [Form types](types-forms.md)

## Create a form 
1. Sign in to [PowerApps](https://web.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc). 
2. On the left navigation pane, expand **Data**, and then select **Entities**. 
3. Select an entity, such as the account entity, and then select the **Forms** tab. 
4. Select **Add form**, and then select **Main form (preview)**.     
    The contents of the new form are filled using the existing main form definition. If multiple main forms exist, the form at the top of the list in the form order is used to fill the new form. 
5. Select **Save** to save the form, or select **Publish** if you want to save and make your changes visible to app users.  

## Edit a form 
1. Sign in to [PowerApps](https://web.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc). 
2. On the left navigation pane, expand, select **Data**, and then select **Entities**. 
3. Select an entity, such as the account entity, and then select the **Forms** tab.
4. Select the form that you want to edit, and then select **Edit form (preview)**.  
   Alternatively, select **...** next to the form you want, and then select **Edit form (preview)**. 
5. Select **Save** to save the form, or select **Publish** if you want to save and make your changes visible to app users. 

## Add and remove fields 
To add or remove fields from a form, use the **Fields** pane. The **Fields** pane lets you search and filter to help you quickly find fields. It also includes the option to show only unused fields. 

### Add a field
1. Open the form designer to create or edit a form. More information: [Create a form](#create-a-form) and [Edit a form](#edit-a-form)
2. On the form preview, select another existing field or a section. 
    - When you select an existing field, the new field is added below the existing field. 
    - When you select a section, the new field is added in an available space so as to evenly distribute fields across the columns. 
3. Select **Add field**, or in the left pane, select **Fields**.  
   The **Fields** pane is open by default when the form designer is opened. 
4. In the **Fields** pane, search, filter, or scroll to find the field you want to add. 
   If you can't find a field, it might already be on the form. Clear **Show only unused fields** to view all fields, including those already added to the form. 
5. In the **Fields** pane, select a field to add it to the form. <br />
   Alternatively, select **...** next to the field you want, and then select **Add to selected section**. 
6. Select **Save** to save the form, or select **Publish** if you want the save and make your changes visible to end-users. 

### Remove a field
1. Open the form designer to create or edit a form. More information: [Create a form](#create-a-form) and [Edit a form](#edit-a-form)
2. On the form preview, select the field that you want to remove from the form. 
3. Select **Delete**. <br />
4. Select **Save**. 

    > [!NOTE]
    >   -  If you remove a field by mistake, select **Undo** to revert the form to its previous state. 
    >   -  You can't remove a field that is required or locked. 

## Add and remove tabs and sections 
To add or remove a tab or section on a form, use the **Layouts** pane. 

### Add a tab
1. Open the form designer to create or edit a form. More information: [Create a form](#create-a-form) and [Edit a form](#edit-a-form) 
2. On the form preview, select another existing tab or the form. 
    - When you select an existing tab, the new tab will be added to the right of the existing tab. 
    - When you select the form, the new tab will be added as the right-most tab on the form. 
3. Select **Add control**, or in the left pane, select **Layouts**.  
4. In the **Layouts** pane, select a tab control, such as **2-column tab**, to add it to the form. <br />
   Alternatively, select **...** next to the tab control you want, and then select **Add to form**.  
5. Select **Save**. 


### Remove a tab
1. Open the form designer to create or edit a form. More information: [Create a form](#create-a-form) and [Edit a form](#edit-a-form)
2. In the form preview, select the tab that you want to delete, and then select **Delete**. 
3. Select **Save**. 
    > [!NOTE]
    >    - When you delete a tab by mistake, select **Undo** to revert the form to its previous state. 
    >     - A form must have at least one tab. You can't delete a tab that is the only tab on the form. 
    >    - You can't delete a tab that has locked sections. 
    >    - You can't delete a tab that has sections with required or locked fields. 

### Add a section 
1. Open the form designer to create or edit a form. More information: [Create a form](#create-a-form) and [Edit a form](#edit-a-form)
2. In the form preview, select another existing section or a tab. 
    - If you select an existing section, the new section is added below the existing section. 
    - If you select a tab, the new section is added at the bottom of the first column of the tab. 
3. Select **Add control**, or in the left pane, select **Layouts**.
4. In the **Layouts** pane, select a section control to add it to the form. <br />
   Alternatively, select **...** next to the section control you want, and then select **Add to selected tab**.      
5. Select **Save**. 
 

### Delete a section 
1. Open the form designer to create or edit a form. More information: [Create a form](#create-a-form) and [Edit a form](#edit-a-form) 
2. In the form preview, select the section that you want to delete, and then select **Delete**.  
3. Select **Save**. 
    > [!NOTE]
    >    - If you delete a section by mistake, select **Undo** to revert the form to its previous state. 
    >    - A tab needs to have at least one section in each column.  
    >    - You can't delete a section if it is the only one in the tab column. 
    >    - You can't delete a section that is locked. 
    >    - You can't delete a section that has required or locked fields. 
 
## Use the tree view 
The **Tree View** pane displays a visual hierarchy of the controls and fields on the form. The icons in the tree view help you quickly identify the type of field or control. 

You can also use the tree view to select fields and controls present on the form. The tree view is helpful when you want to select hidden elements that are not visible on the form preview. 

You can expand or collapse nodes in the tree view to see or hide the elements within a node. When you select an element in the tree view, it becomes highlighted in the form preview, and the property pane displays the properties for the element. 

   ![Tree view](media/tree-view.png)

### Open the tree view 
1. Open the form designer to create or edit a form. More information: [Create a form](#create-a-form) and [Edit a form](#edit-a-form)  
2. In the left pane, select **Tree View**.

## See also
[Overview of the model-driven form designer](form-designer-overview.md) <br />
[Create and edit fields](../common-data-service/create-edit-field-portal.md)
