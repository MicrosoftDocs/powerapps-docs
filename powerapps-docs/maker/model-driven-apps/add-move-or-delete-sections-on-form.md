---
title: "Add, move or delete sections on a form using the form designer | MicrosoftDocs"
ms.custom: ""
ms.date: 04/21/2019
ms.reviewer: ""
ms.service: powerapps
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

# Add, move or delete sections on a form using the form designer 
[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

## Add sections to a form
To add sections to a form, use the **Layouts** pane. 

  > [!NOTE]
  >   - Sections can only be added on main forms and quick view forms. More information: [Form types](types-forms.md)

### Add sections to a form using drag and drop

1. Open the form designer to create or edit a form. 
    - More information: [Create a form](create-and-edit-forms.md#create-a-form) or [Edit a form](create-and-edit-forms.md#edit-a-form)
2. In the command bar, select **Add control**, or in the left pane, select **Layouts**. 
3. In the **Layouts** pane, select a section control and drag it onto the form preview. As you drag the section on the form preview, you will see drop targets where you can add the section. 
4. Drop the section in the location you want.
    - Sections can be dropped before or after any existing section.
    - Sections can also be dropped in the empty area within a tab. In this case the section will be added in an available space so as to evenly distribute sections across the tab columns.
    - Hovering over a tab header when dragging a section changes the currently selected tab, allowing you to add the section to a different tab.   
5. Repeat steps 3-4 above if you want to add more sections.
6. In the command bar, select **Save** to save the form, or select **Publish** if you want to save and make your changes visible to end-users. 

### Add sections to a form using selection 

1. Open the form designer to create or edit a form. 
    - More information: [Create a form](create-and-edit-forms.md#create-a-form) or [Edit a form](create-and-edit-forms.md#edit-a-form)
2. In the form preview, select another existing section or tab. 
    - When you select an existing section, the new section is added after the existing section. 
    - When you select a tab, the new section is added in an available space so as to evenly distribute sections across the tab columns. 
3. In the command bar, select **Add control**, or in the left pane, select **Layouts**.  
4. In the **Layouts** pane, select a section control to add it to the form. 
    - Alternatively, select **...** next to the section control you want, and then select **Add to selected tab**. 
5. Repeat steps 2-4 above if you want to add more sections.
6. In the command bar, select **Save** to save the form, or select **Publish** if you want to save and make your changes visible to end-users. 

## Move sections on a form

### Move sections on a form using drag and drop

1. Open the form designer to create or edit a form. 
    - More information: [Create a form](create-and-edit-forms.md#create-a-form) or [Edit a form](create-and-edit-forms.md#edit-a-form)
2. In the form preview, click on the section label or empty white-space within the section that you want to move and initiate the drag action. As you drag the section on the form preview, you will see drop targets where you can move the section to. 
3. Drop the section in the location you want.
    - Sections can be dropped before or after any existing section.
    - Sections can also be dropped in the empty area within a tab. In this case the section will be added in an available space so as to evenly distribute sections across the tab columns.
    - Hovering over a tab header when dragging a section changes the currently selected tab, allowing you to add the section to a different tab.   
4. Repeat steps 2-3 above if you want to move more sections.
5. In the command bar, select **Save** to save the form, or select **Publish** if you want to save and make your changes visible to end-users. 

### Move sections on a form using cut and paste

1. Open the form designer to create or edit a form. 
    - More information: [Create a form](create-and-edit-forms.md#create-a-form) or [Edit a form](create-and-edit-forms.md#edit-a-form)
2. In the form preview, select the section that you want to move.
3. In the command bar, select **Cut**.
4. In the form preview, select another existing section or tab. You can also switch to a different tab if needed.
5. In the command bar, select **Paste** or click on the chevron and then select **Paste before**.
    - When you select **Paste**, the section being moved is pasted after the existing section. 
    - When you select **Paste before**, the section being moved is pasted before the existing section.
    - When you select a tab, the section being moved is added in an available space so as to evenly distribute sections across the tab columns. The **Paste before** action is not applicable and therefore not available in this case.
6. Repeat steps 2-5 above if you want to move more sections.
7. In the command bar, select **Save** to save the form, or select **Publish** if you want to save and make your changes visible to end-users. 

## Delete sections on a form
1. Open the form designer to create or edit a form. 
    - More information: [Create a form](create-and-edit-forms.md#create-a-form) or [Edit a form](create-and-edit-forms.md#edit-a-form)
2. In the form preview, select the section that you want to delete from the form. 
3. In the command bar, select **Delete**.
4. Repeat steps 2-3 above if you want to delete more sections.
4. In the command bar, select **Save** to save the form, or select **Publish** if you want to save and make your changes visible to end-users. 

    > [!NOTE]
    >   - Sections can only be deleted on main forms and quick view forms. More information: [Form types](types-forms.md)
    >   - If you delete a section by mistake, in the command bar, select **Undo** to revert the form to its previous state. 
    >   - You can't delete a section that contains a field that is required or locked. 
    >   - You can't delete a section that is locked. 
    >   - A tab needs to have at least one section in each tab column. If you delete the last remaining section in a tab column a new section will be automatically added. 

## See also
[Overview of the model-driven form designer](form-designer-overview.md)  
[Create and edit forms using the form designer](create-and-edit-forms.md)  
[Add, move or delete fields on a form using the form designer](add-move-or-delete-fields-on-form.md)  
[Add, move or delete tabs on a form using the form designer](add-move-or-delete-tabs-on-form.md)  
[Properties available in the form designer](form-designer-properties.md)  
[Using the tree view in the form designer](using-tree-view-on-form.md)  
[Create and edit fields](../common-data-service/create-edit-field-portal.md) 
