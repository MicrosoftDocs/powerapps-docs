---
title: "Add, configure, move, or delete components on a form | MicrosoftDocs"
description: Learn how to use the form designer to work with form components.
ms.custom: ""
ms.date: 08/26/2019
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
author: "Aneesmsft"
ms.subservice: mda-maker
ms.author: "matp"
manager: "kvivek"
tags: 
  - "Power Apps maker portal impact"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---

# Add, configure, move, or delete components on a form

By using the form designer, makers can easily add and configure popular components such as [subgrid](form-designer-add-configure-subgrid.md), [quick view](form-designer-add-configure-quickview.md), arc knob, linear slider, and more.

## Add components to a form

To add components to a form, use the **Components** pane. Components can be found easily using the search in the  **Components** pane.  

> [!div class="mx-imgBorder"]
> ![Components pane.](media/FormDesignerComponentsPane.PNG "Components pane")

### Add components to a form using drag and drop

> [!NOTE]
> When adding or moving components using drag and drop, be aware that the form preview is responsive and might render multiple section columns as stacked. To ensure that the component that's added or moved is in the correct section column, drop or paste it anchored to another column or component that is already in that section column.

1. Open the form designer to create or edit a form. More information: [Create a form](create-and-edit-forms.md#create-a-form) or [Edit a form](create-and-edit-forms.md#edit-a-form)
1. On the command bar, select **Add component**, or in the left pane, select **Components** to see a list of available components. Hover over a component in the list to see a preview image, description, and other details of that component.
1. In the **Components** pane, search or scroll to find the required component then select to add the component.
1. Drag and drop the component onto the form preview. As the component is dragged on the form preview, drop targets will appear.

    > [!NOTE]
    >
    > - Components can be dropped before or after any existing component or column.
    > - Components can also be dropped in the empty area within a section. In this case the component will be added in an available space so as to evenly distribute columns and components across the section columns.
    > - Hovering over a tab header when dragging a component changes the currently selected tab, allowing the component to be added to a different tab.
    > - When the component is dropped, in most cases, a dialog to configure the properties of the component will appear. Ensure that all the required properties of the component are configured.
  
1. In the dialog to configure the properties of the component, under **Show component on**, the **Web**, **Mobile**, and **Tablet** options are selected by default to ensure the component is used when the form is displayed on the web, mobile app, and tablet app. Based on the  requirements some of these options to limit the usage of the component can be cleared.
1. Select **Done**.
1. Repeat steps 3-6 above to add more components.
1. On the command bar, select **Save** to save the form, or select **Publish** to make the changes visible to users.

### Add components for a column on the form

1. Open the form designer to create or edit a form. More information: [Create a form](create-and-edit-forms.md#create-a-form) or [Edit a form](create-and-edit-forms.md#edit-a-form)
1. In the form preview, select an existing column.
1. In the property pane, under the **Components** area, select **+ Component**.
1. The **Add component** dialog displays a list of components that are available for the current column type. Hover over a component in the list to see a preview image, description, and other details of that component.
1. In the **Add component** dialog, search, or scroll to find the required component to add and then select it.
   In most cases, a dialog is displayed to configure the properties of the component. Ensure that all the required properties of the component have been configured.
1. In the dialog to configure the properties of the component, under **Show component on**, the **Web**, **Mobile**, and **Tablet** options are selected by default to ensure the component is used when the form is displayed on the web, mobile app, and tablet app. Based on the requirements some of these options to limit the usage of the component can be cleared.
1. Select  **Done**.
1. Repeat steps 2-7 above to add more components to the same or another column.
1. On the command bar, select **Save** to save the form, or select **Publish** to save and make the changes visible to users.

## Configure components on a form

1. Open the form designer to create or edit a form. More information: [Create a form](create-and-edit-forms.md#create-a-form) or [Edit a form](create-and-edit-forms.md#edit-a-form)
1. In the form preview, select an existing column.
1. In the property pane, under the **Components** area, select the component that you want configured.
1. A dialog might appear to configure the properties of the component. Change the properties of the component as needed, and then select **Done**.
1. Repeat steps 2-4 to configure more components on the same or another column.
1. On the command bar, select **Save** to save the form, or select **Publish** to save and make the changes visible to users.

## Move components on a form

To move components on a form, either use drag-and-drop or cut-and-paste actions.

### Move components on a form using drag and drop

1. Open the form designer to create or edit a form. More information: [Create a form](create-and-edit-forms.md#create-a-form) or [Edit a form](create-and-edit-forms.md#edit-a-form)
1. In the form preview, select the component to move and drag and drop it. As the component is dragged onto the form preview, drop targets appear where it can be moved.

  > [!NOTE]
  >
  > - Components can be dropped before or after any existing component or column.
  > - Components can also be dropped in the empty area within a section. In this case the component will be added in an available space to evenly distribute components and columns across the section columns.
  > - Hover over a tab header while using drag and drop to add the component to a different tab.

1. Repeat steps 2-3 above to move more components.
1. On the command bar, select **Save** to save the form, or select **Publish** to save and make the changes visible to users.

### Move components on a form using cut and paste

1. Open the form designer to create or edit a form. More information: [Create a form](create-and-edit-forms.md#create-a-form) or [Edit a form](create-and-edit-forms.md#edit-a-form)
1. In the form preview, select the required component to move.
1. On the command bar, select **Cut**.
1. In the form preview, select another existing component, column, or section. It is possible to switch to a different tab if needed.
1. On the command bar, select **Paste** or select the chevron, and then select **Paste before**.

   >  [!NOTE]
   >
   > - When **Paste** is selected, the component being moved is pasted after the existing component or column.
   > - When **Paste before** is selected, the component being moved is pasted before the existing component or column.
   > - When a section is selected, the component being moved is added in an available space so as to evenly distribute components and columns across the section columns.

1. Repeat steps 2-5 above if to move more components.
1. On the command bar, select **Save** to save the form, or select **Publish** to save and make the changes visible to users.

## Delete components on a form

1. Open the form designer to create or edit a form. More information: [Create a form](create-and-edit-forms.md#create-a-form) or [Edit a form](create-and-edit-forms.md#edit-a-form)
2. In the form preview, select the component that you want to delete from the form, and then on the command bar, select **Delete**.
3. Repeat step 2 to delete more components.
4. On the command bar, select **Save** to save the form, or select **Publish** to save and make the changes visible to users.

     > [!NOTE]
     >
     > - If a component is deleted by mistake, select **Undo** on the command bar to revert the form to its previous state.
     > - A component can't be deleted when it is locked or is using a required column that is not present anywhere else on the form.

### See also

[Overview of the model-driven form designer](form-designer-overview.md)  
[Create, edit, or configure forms using the form designer](create-and-edit-forms.md)  
[Add, configure, move, or delete columns on a form](add-move-or-delete-fields-on-form.md)  
[Add, configure, move, or delete sections on a form](add-move-or-delete-sections-on-form.md)  
[Add, configure, move, or delete tabs on a form](add-move-or-delete-tabs-on-form.md)  
[Configure header properties in the form designer](form-designer-header-properties.md)  
[Add and configure a subgrid component on a form](form-designer-add-configure-subgrid.md)  
[Add and configure a quick view component on a form](form-designer-add-configure-quickview.md)  
[Configure a lookup component on a form](form-designer-add-configure-lookup.md)  
[Using the tree view in the form designer](using-tree-view-on-form.md)  
[Create and edit columns](../data-platform/create-edit-field-portal.md)  

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
