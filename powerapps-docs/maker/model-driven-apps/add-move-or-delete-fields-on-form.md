---
title: "Add, configure, move, or delete fields on a form | MicrosoftDocs"
ms.custom: ""
ms.date: 08/26/2019
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
  - "Power Apps maker portal impact"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---

# Add, configure, move, or delete fields on a form  
Add, configure, move, or delete fields using the form designer.

## Add fields to a form
To add fields to a form, use the **Fields** pane. The **Fields** pane lets you search and filter to help you quickly find fields. It also includes the option to show only unused fields. 

> [!div class="mx-imgBorder"] 
>    ![](media/FormDesignerFieldsPane.png "Fields pane")

### Add fields to a form using drag and drop
> [!NOTE]
> When adding or moving fields using drag and drop be aware that the form preview is responsive and may be rendering multiple section columns as stacked. To ensure that the field being added or moved is in the correct section column, drop or paste it anchored to another field that is already in that section column.
1. Open the form designer to create or edit a form. More information: [Create a form](create-and-edit-forms.md#create-a-form) or [Edit a form](create-and-edit-forms.md#edit-a-form)
2. In the command bar, select **Add field**, or in the left pane, select **Fields**.  The **Fields** pane is open by default when the form designer is opened. 
3. In the **Fields** pane, search, filter, or scroll to find the field you want to add. If you can't find a field, it might already be on the form. Clear **Show only unused fields** to view all fields, including those already added to the form. 
4. In the **Fields** pane, select a field and drag it onto the form preview. As you drag the field on the form preview, you will see drop targets where you can add the field. 
5. Drop the field in the location you want. Note the following: 
    - Fields can be dropped before or after any existing field or component.
    - Fields can also be dropped in the empty area within a section. In this case the field will be added in an available space so as to evenly distribute fields and components across the section columns.
    - Hovering over a tab header when dragging a field changes the currently selected tab, allowing you to add the field to a different tab.   
6. Repeat steps 3-5 above if you want to add more fields.
7. In the command bar, select **Save** to save the form, or select **Publish** if you want to save and make your changes visible to users. 

### Add fields to a form using selection 

1. Open the form designer to create or edit a form. More information: [Create a form](create-and-edit-forms.md#create-a-form) or [Edit a form](create-and-edit-forms.md#edit-a-form)
2. In the form preview, select another existing field or section. Note the following:
    - When you select an existing field, the new field is added after the existing field. 
    - When you select a section, the new field is added in an available space so as to evenly distribute fields across the section columns. 
3. In the command bar, select **Add field**, or in the left pane, select **Fields**. The **Fields** pane is open by default when the form designer is opened. 
4. In the **Fields** pane, search, filter, or scroll to find the field you want to add. If you can't find a field, it might already be on the form. Clear **Show only unused fields** to view all fields, including those already added to the form. 
5. In the **Fields** pane, select a field to add it to the form. Alternatively, select **...** next to the field you want, and then select **Add to selected section**. 
6. Repeat steps 2-5 above if you want to add more fields.
7. In the command bar, select **Save** to save the form, or select **Publish** if you want to save and make your changes visible to users. 

## Configure fields on a form
These are the properties available to configure a field when you create or edite a form using the form designer.

## Field properties

|Area  |Name  |Description  |
|---------|---------|---------|
|**Display options** | **Field label** | By default the label will match the display name of the field. You can override that name for the form by entering a different label here. <br /><br />This property is required. |
|**Display options** |  **Field name** | The name of the field. This comes from the field properties on the entity and is read-only. |
|**Display options** | **Hide label** | When selected, the field label is hidden. |
|**Display options** | **Read-only field** | When selected, the field value is not editable. |
|**Display options** | **Lock field** |  Lock this field so it can't be removed. |
|**Display options** | **Hide field** | When selected, the field is hidden by default and can be shown using code. |
|**Display options** | **Hide on phone** | The field can be hidden to render a condensed version of the form on phone screens. |
|**Formatting** | **Field width** |  When the section containing the fields has more than one column you can set the field to occupy up to the number of columns that the section has. |

[!NOTE] 
> In the Unified Interface, label size is not used in the settings due to how a form ajusts width for all fields to ensure a proper UI experience for all view port sizes from very small to extra large.

## Move fields on a form
You can move a field on a form using drag and drop or cut and paste actions. 

### Move fields on a form using drag and drop
1. Open the form designer to create or edit a form. More information: [Create a form](create-and-edit-forms.md#create-a-form) or [Edit a form](create-and-edit-forms.md#edit-a-form)
2. In the form preview, select the field that you want to move and drag and drop it. As you drag the field on the form preview, you will see drop targets where you can move the field to. 
   Note the following:
    - Fields can be dropped before or after any existing field or component.
    - Fields can also be dropped in the empty area within a section. In this case the field will be added in an available space so as to evenly distribute fields and components across the section columns.
    - Hovering over a tab header when dragging a field changes the currently selected tab, allowing you to add the field to a different tab.   
3. Repeat step 2 above if you want to move more fields.
4. On the command bar, select **Save** to save the form, or select **Publish** if you want to save and make your changes visible to users. 

### Move fields on a form using cut and paste
1. Open the form designer to create or edit a form. More information: [Create a form](create-and-edit-forms.md#create-a-form) or [Edit a form](create-and-edit-forms.md#edit-a-form)
2. In the form preview, select the field that you want to move.
3. On the command bar, select **Cut**.
4. In the form preview, select another existing field, component or section. You can also switch to a different tab if needed.
5. On the command bar, select **Paste** or select the chevron, and then select **Paste before**.      Note the following:
     - When you select **Paste**, the field that is moved is pasted after the existing field or component. 
     - When you select **Paste before**, the field that is moved is pasted before the existing field or component.
     - When you select a section, the field that is moved is added in an available space so as to evenly distribute fields and components across the section columns. The **Paste before** action is not applicable and therefore not available in this case.
6. Repeat steps 2-5 above if you want to move more fields.
7. On the command bar, select **Save** to save the form, or select **Publish** if you want to save and make your changes visible to users. 

## Delete fields on a form
1. Open the form designer to create or edit a form. More information: [Create a form](create-and-edit-forms.md#create-a-form) or [Edit a form](create-and-edit-forms.md#edit-a-form)
2. In the form preview, select the field that you want to delete from the form. 
3. On the command bar, select **Delete**. 
4. Repeat steps 2-3 if you want to delete more fields.
5. On the command bar, select **Save** to save the form, or select **Publish** if you want to save and make your changes visible to users. 

     > [!NOTE]
     >   -  If you delete a field by mistake, on the command bar, select **Undo** to revert the form to its previous state. 
     >   -  You can't delete a field that is locked or is required and not present anywhere else on the form. 

## Create a new field on the entity when editing a form 
1. Open the form designer to create or edit a form. More information: [Create a form](create-and-edit-forms.md#create-a-form) or [Edit a form](create-and-edit-forms.md#edit-a-form)
2. On the command bar, select **Add field**, or in the left pane, select **Fields**. The **Fields** pane is open by default when the form designer is opened. 
3. In the **Fields** pane, select **+ New field**.
4. In the **New field** dialog, provide the **Display name** and **Name** for the field.
5. In the **New field** dialog, select the **Data type** and configure any other required properties of the field.

     > [!NOTE]
     >   -  Some field types are not available when you create a field from within the form designer. If a field type you want is not available, you can follow the steps outlined in [Create and edit fields for Common Data Service using Power Apps portal](../common-data-service/create-edit-field-portal.md)

6. Select **Done** to create a new field on the entity. The field appears in the **Fields** pane.
7. If you want to add the newly created field to the form, follow the steps outlined in the [**Add fields to a form**](add-move-or-delete-fields-on-form.md#add-fields-to-a-form) section.

     > [!NOTE]
     >  When a field is created on the entity, it is not limited to the current form and will be available for use in other places.

### See also
[Overview of the model-driven form designer](form-designer-overview.md)  
[Create, edit, or configure forms using the form designer](create-and-edit-forms.md)  
[Add, configure, move, or delete components on a form](add-move-configure-or-delete-components-on-form.md)  
[Add, configure, move, or delete sections on a form](add-move-or-delete-sections-on-form.md)  
[Add, configure, move, or delete tabs on a form](add-move-or-delete-tabs-on-form.md)  
[Configure header properties in the form designer](form-designer-header-properties.md)  
[Add and configure a sub-grid component on a form](form-designer-add-configure-subgrid.md)  
[Add and configure a quick view component on a form](form-designer-add-configure-quickview.md)  
[Configure a lookup component on a form](form-designer-add-configure-lookup.md)  
[Using the tree view in the form designer](using-tree-view-on-form.md)  
[Create and edit fields](../common-data-service/create-edit-field-portal.md)  
