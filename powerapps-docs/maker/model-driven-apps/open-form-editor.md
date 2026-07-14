---
title: "Open the model-driven app form editor in Power Apps"
description: Understand the ways you can open the model-driven app form editor.
ms.custom: ""
ms.date: 02/12/2026
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 8478a07a-c697-4784-874b-36958eb4f95d
caps.latest.revision: 63
ms.subservice: mda-maker
ms.author: "matp"
search.audienceType: 
  - maker
---
# Open the model-driven app form editor

Model-driven app forms let users update data within columns, or fields, associated with a given table record.

The form editor is where you design forms by dropping components such as sections, tabs, columns, and controls onto the form editor canvas. In this article, you learn how several different ways to access the form editor.

:::image type="content" source="../../maker/model-driven-apps/media/add-columns-drag-and-drop.gif" alt-text="Advanced Settings":::

If you create any new solution components in the process of editing the form, for example web resources, the names of the components will use the solution publisher customization prefix for the default solution and these components will only be included in the default solution. If you want any new solution components to be included in a specific unmanaged solution, you should open the form editor through that unmanaged solution.  

## Access the form editor from the Power Apps site

1. Sign in to [Power Apps](https://make.powerapps.com/).

2. Select **Tables** on the left navigation, and then open the table you want, such as the account table. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]

3. Select the **Forms** area and then open the form you want, such as the **Account** main form.

## Access the form editor for an unmanaged solution  
  
1. Select **Solutions**, on the left naviation pane. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)] 
  
2. Open the unmanaged solution you want to work with.  
  
3. Open the table with the form you want to edit. If the table isn't there, you'll need to add it. More information: [Add a table to an unmanaged solution](#add-a-table-to-an-unmanaged-solution)

4. Select the **Forms** area, and then open the form you want to edit.
  
### Add a table to an unmanaged solution  
  
1. While in an unmanaged solution, on the toolbar above the list, select **Add Existing** > **Table**.
  
2. In the **Add existing tables** pane, select the table you want to add, and then select **Next**.  
  
3. Choose the correct option for the table objects:
   - If this is a custom table that doesn't exist in other environments, select **Include all objects**.
   - If this table has been customized but already was exported or otherwise exists in target environments, select **Include table metadata** if only properties for the table have changed, or select **Edit objects** and select specific objects, such as columns, forms, or views that have been changed or added.
   - If no changes have been made, such as if you adding an out-of-box table, don't select any options.
  
4. Select **Add**.
  
## Access the form editor from the classic solution explorer
  
1. Open [solution explorer](advanced-navigation.md#solution-explorer).
  
2. Under **Components**, expand **Tables**, and then the table you want, and select **Forms**.  
  
3. In the list of forms, select the form you want to edit.

## Next steps

[Create or edit forms](create-and-edit-forms.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
