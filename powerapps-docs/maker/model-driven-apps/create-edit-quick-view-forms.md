---
title: "Create or edit model-driven app quick view forms in Power Apps | MicrosoftDocs"
description: "Learn how to create or edit a quick view form"
ms.custom: ""
ms.date: 07/23/2020
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
ms.assetid: 9b101734-cc11-4d05-bd45-eb611eae9931
caps.latest.revision: 14
ms.subservice: mda-maker
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Create a quick view form to view information about a related table

This article describes how to create a quick view form and how to add a quick view control to a main form.

A quick view form can be added to another form as a quick view control. It provides a template to view information about a related table row within a form for another table row. This means app users do not need to navigate to a different row to see the information needed to do their work.

Note that while a quick view form can appear over a view or a form, it is authored as a form, rather than a view.

In the example below notice the module that relates to a given lesson within the quick view form.  A one-to-many relationship exists between the two tables for this to be possible.  We can see additional columns of metadata, including the image associated with the module. The form then continues with the metadata associated with the lesson table record.

:::image type="content" source="../../maker/model-driven-apps/media/quick-view-form-control.png" alt-text="view quick view form control":::
  
 Quick view controls are associated with a lookup column that is included in a form. If the lookup column value is not set, the quick view control will not be visible.  
  
> [!NOTE]
> - Data in quick view form controls can't be edited and they do not support form scripts. 
> - Because quick view forms are viewed using a quick view control in a form, they do not include header, footer, or navigation areas. Security roles can't be assigned to quick view forms and they can't be activated or deactivated. Subgrids inside quick view forms will also not display a command bar.
  
<a name="BKMK_CreateQFV"></a>

## Create a quick view form

 You create quick view forms using the form editor in a manner similar to the way you create other forms. Quick view forms are read-only. Use them to create forms that are for reading purposes only.  
  
1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).  

2. Expand **Data**, select **Tables**, select the table that you want, and then select the **Forms** tab.
  
3. On the toolbar, select **Add form** > **Quick View Form**.  
  
4. In the **Form** panel, enter a **Display Name** and **Description** to differentiate this quick view form from others.  
  
5. In the form designer, drag any columns from the **Columns Explorer** into the section on the form.

    > [!IMPORTANT]
    > Required columns can't be removed from a form. If you add a required column to the form and want to remove it, you must delete the form and then re-create it. When you set the required property for a column, a row can't be saved without data in the column.

7. To save the form select **Save**.  

8. Select **Publish** to see the new form in the app.
  
<a name="BKMK_EditQVF"></a>   
## Edit a quick view form

Quick view forms have a simplified layout because they are designed to be viewed within a form section. Only one single column tab is available. You can add only additional single column sections, columns, subgrids, and spacers.

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc)

1. Open the solution relevant to your table or access the table directly from the data option in the sidebar.

1. Open the table you want, and then select the **Forms** tab.

1. Either select the quick view form, or select **...** next to the form, and then select **Edit form in new tab**.

1. Add or remove the table columns you want.
  
  > [!IMPORTANT]
  > Required columns can't be deleted. If you add a required column to the form, you can't delete it. If you don't want the column in the form you must delete the form and then re-create it.
  
 When you edit a quick view form, you must publish your changes before they will be visible in the application.  
  
<a name="BKMK_AddQVF"></a>   
## Add a quick view control to a main form

Quick view forms can only be added to a main form where a lookup column exists that targets the table of the quick view form.  
  
1.  Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).  

2.  Expand **Data**, select **Tables**, select the table that you want, and then select the **Forms** tab.  

3. Select a form, which **Type** is **Main**
4. In the form designer, from the **Components** pane select **Quick view**.  
  
5.  In the **Select quick view forms** dialog box, select the **Lookup** column, and then select the lookup column value. More information: [Quick view control properties](quick-view-control-properties-legacy.md).  

    > [!div class="mx-imgBorder"] 
    > ![Add quick view control.](media/add-quick-view-control.png "Add quick view control to main form")

6.  Select **Done** to close the **Select quick View forms** dialog box. The quick view form appears on the form.

7.  To save the form select **Save**.  

    > [!IMPORTANT]
    > Be aware of the behavior that occurs when you create a parent relationship with the same table. For example, if Account has a relationship to Account and a lookup is created that is used by a quick create form that creates a parent row, the first row will not be saved with the lookup that has the parent row value. This is because of the circular reference introduced by using the same table. If this issue is experienced it can be resolved by removing the parent row id on the quick create form before saving the row.

## Quick view form properties

When the quick view form is used in a main form the following properties can be set or updated.

|Property|Description|  
|--------------|-----------------|  
|**Name**|**Required**: The unique name for the quick view form that is used when referencing it in scripts.|  
|**Label**|**Required**: A label to display for the quick view form.|  
|**Display label on the Form**|Displays the label on the form.|  
|**Lookup Column**|Choose one of the lookup columns included in the form.|  
|**Related table**|This value depends on the **Lookup Column** chosen. It is usually the primary table for the 1:N table relationship for the lookup.<br /><br /> If the table includes a **Potential Customer** lookup that can accept either an account or contact, in the **Quick View Form** column you can choose a quick view form for both account and contact by changing this value and then choosing another quick view form.|  
|**Quick View Form**|If the **Related table** has any quick view forms these can be selected here. Otherwise, select **New** to create one.<br />  

## Next steps
  
[Create and edit a card form](create-card-forms.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
