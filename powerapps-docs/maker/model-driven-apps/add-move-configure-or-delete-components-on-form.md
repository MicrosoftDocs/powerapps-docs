---
title: "Add, configure, move, or delete components on a form | MicrosoftDocs"
ms.custom: ""
ms.date: 08/20/2019
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

# Add, configure, move, or delete components on a form  
Using the new form designer makers can easily add and configure popular components such as sub-grid, quick view and even additional components such as arc knob, linear slider and more.

> [!NOTE]
> When adding or moving components using drag and drop be aware that the form preview is responsive and may be rendering multiple section columns as stacked. To ensure that the component being added or moved is in the correct section column, drop or paste it anchored to another field or component that is already in that section column.

## Add components to a form
To add components to a form, use the **Components** pane. The **Components** pane also lets you search to help you quickly find components.  

> [!div class="mx-imgBorder"] 
> ![](media/FormDesignerComponentsPane.png "Components pane")

### Add components to a form using drag and drop

1. Open the form designer to create or edit a form. More information: [Create a form](create-and-edit-forms.md#create-a-form) or [Edit a form](create-and-edit-forms.md#edit-a-form)
2. In the command bar, select **Add component**, or in the left pane, select **Components** to see a list of available components. You can also hover over a component in the list to see a preview image, description and other details of that component.
3. In the **Components** pane, search or scroll to find the component that you want to add.
4. In the **Components** pane, select a component and drag it onto the form preview. As you drag the component on the form preview, you will see drop targets where you can add the component. 
5. Drop the component in the location you want. Note the following: 
    - Components can be dropped before or after any existing component or field.
    - Components can also be dropped in the empty area within a section. In this case the component will be added in an available space so as to evenly distribute fields and components across the section columns.
    - Hovering over a tab header when dragging a component changes the currently selected tab, allowing you to add the component to a different tab.   
6. When you drop the component, in most cases, you will see a dialog to configure the properties of the component. Ensure that you have configured all the required properties of the component. 
7. In the dialog to configure the properties of the component, under **Show component on**, the **Web**, **Mobile** and **Tablet** options will be selected by default to ensure the component is used when the form is displayed on the web, mobile app and tablet app. Based on your requirements you can unselect some of these options to limit the usage of the component.
8. When you are done configuring the properties of the component, click on the **Done** button to add the component to your form.
9. Repeat steps 3-8 above if you want to add more components.
10. In the command bar, select **Save** to save the form, or select **Publish** if you want to save and make your changes visible to users. 

### Add components for a field on the form

1. Open the form designer to create or edit a form. More information: [Create a form](create-and-edit-forms.md#create-a-form) or [Edit a form](create-and-edit-forms.md#edit-a-form)
2. In the form preview, select an existing field.
3. In the property pane, under the **Components** area, select **+ Component**.
4. The **Add component** dialog will display a list of components that are available and applicable for the current field type. You can also hover over a component in the list to see a preview image, description and other details of that component.
5. In the **Add component** dialog, search or scroll to find the component you want to add and then select it.
6. In most cases, you will see a dialog to configure the properties of the component. Ensure that you have configured all the required properties of the component. 
7. In the dialog to configure the properties of the component, under **Show component on**, the **Web**, **Mobile** and **Tablet** options will be selected by default to ensure the component is used when the form is displayed on the web, mobile app and tablet app. Based on your requirements you can unselect some of these options to limit the usage of the component.
8. When you are done configuring the properties of the component, click on the **Done** button to add the component to your form.
9. Repeat steps 2-8 above if you want to add more components to the same or another field.
10. In the command bar, select **Save** to save the form, or select **Publish** if you want to save and make your changes visible to users.

## Configure components on a form

### Configure existing components for a field on the form

1. Open the form designer to create or edit a form. More information: [Create a form](create-and-edit-forms.md#create-a-form) or [Edit a form](create-and-edit-forms.md#edit-a-form)
2. In the form preview, select an existing field.
3. In the property pane, under the **Components** area, click on the component that you want to configure.
4. You should see a dialog to configure the properties of the component. Change the properties of the component as needed.
5. When you are done configuring the properties of the component, click on the **Done** button to save your changes.
6. Repeat steps 2-5 above if you want to configure more components on the same or another field.
7. In the command bar, select **Save** to save the form, or select **Publish** if you want to save and make your changes visible to users.

## Move components on a form

### Move components on a form using drag and drop

1. Open the form designer to create or edit a form. More information: [Create a form](create-and-edit-forms.md#create-a-form) or [Edit a form](create-and-edit-forms.md#edit-a-form)
2. In the form preview, select the component that you want to move and initiate the drag action. As you drag the component on the form preview, you will see drop targets where you can move the component to. 
3. Drop the component in the location you want. Note the following: 
    - Components can be dropped before or after any existing component or field.
    - Components can also be dropped in the empty area within a section. In this case the component will be added in an available space so as to evenly distribute components and fields across the section columns.
    - Hovering over a tab header when dragging a component changes the currently selected tab, allowing you to add the component to a different tab.   
4. Repeat steps 2-3 above if you want to move more components.
5. In the command bar, select **Save** to save the form, or select **Publish** if you want to save and make your changes visible to users. 

### Move components on a form using cut and paste

1. Open the form designer to create or edit a form. More information: [Create a form](create-and-edit-forms.md#create-a-form) or [Edit a form](create-and-edit-forms.md#edit-a-form)
2. In the form preview, select the component that you want to move.
3. In the command bar, select **Cut**.
4. In the form preview, select another existing component, field or section. You can also switch to a different tab if needed.
5. In the command bar, select **Paste** or select the chevron, and then select **Paste before**. Note the following:
    - When you select **Paste**, the component being moved is pasted after the existing component or field. 
    - When you select **Paste before**, the component being moved is pasted before the existing component or field.
    - When you select a section, the component being moved is added in an available space so as to evenly distribute components and fields across the section columns. The **Paste before** action is not applicable and therefore not available in this case.
6. Repeat steps 2-5 above if you want to move more components.
7. In the command bar, select **Save** to save the form, or select **Publish** if you want to save and make your changes visible to users. 

## Delete components on a form
1. Open the form designer to create or edit a form. More information: [Create a form](create-and-edit-forms.md#create-a-form) or [Edit a form](create-and-edit-forms.md#edit-a-form)
2. In the form preview, select the component that you want to delete from the form. 
3. In the command bar, select **Delete**. 
4. Repeat steps 2-3 above if you want to delete more components.
5. In the command bar, select **Save** to save the form, or select **Publish** if you want to save and make your changes visible to users. 

     > [!NOTE]
     >   -  If you delete a component by mistake, in the command bar, select **Undo** to revert the form to its previous state. 
     >   -  You can't delete a component that is locked or is using a required field that is not present anywhere else on the form. 

### See also
[Overview of the model-driven form designer](form-designer-overview.md)  
[Create or edit forms using the form designer](create-and-edit-forms.md)  
[Add, move or delete sections on a form using the form designer](add-move-or-delete-sections-on-form.md)  
[Add, move or delete tabs on a form using the form designer](add-move-or-delete-tabs-on-form.md)  
[Properties available in the form designer](form-designer-properties.md)  
[Configuring header properties in the form designer](form-designer-header-properties.md)  
[Using the tree view in the form designer](using-tree-view-on-form.md)  
[Create and edit fields](../common-data-service/create-edit-field-portal.md)
