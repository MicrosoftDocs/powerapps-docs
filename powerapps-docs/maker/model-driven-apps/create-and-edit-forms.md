---
title: "Create and edit forms using the model-driven form designer | MicrosoftDocs"
ms.custom: ""
ms.date: 01/07/2019
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

# Create and edit forms using the form designer 
[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Use the new form designer to create and design forms for model-driven apps.

> [!IMPORTANT]
> The new model-driven form designer currently supports creating and editing main forms, quick create forms and quick view forms. More information: [Form types](types-forms.md)

## Create a form 
1. Sign in to [PowerApps](https://web.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc). 
2. On the left navigation pane, expand **Data**, and then select **Entities**. 
3. Select an entity, such as the account entity, and then select the **Forms** tab. 
4. Select **Add form**, and then select one of the following
    - **Main form (preview)**.     
    The contents of the new form are filled using the existing main form definition. If multiple main forms exist, the form at the top of the list in the form order is used to fill the new form. 
    - **Quick create form (preview)**
    - **Quick view form (preview)**
5. Select **Save** to save the form, or select **Publish** if you want to save and make your changes visible to app users.  

## Edit a form 
1. Sign in to [PowerApps](https://web.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc). 
2. On the left navigation pane, expand **Data**, and then select **Entities**. 
3. Select an entity, such as the account entity, and then select the **Forms** tab.
4. Select the form name that you want to edit.  
    - You can also select the row for a form, and then in the command bar, select **Edit form (preview)**
    - Another alternative is to select **...** next to the form name, and then in the menu, select **Edit form (preview)**. 
5. Select **Save** to save the form, or select **Publish** if you want to save and make your changes visible to app users. 

## Use the tree view 
The **Tree View** pane displays a visual hierarchy of the controls and fields on the form. The icons in the tree view help you quickly identify the type of field or control. 

You can also use the tree view to select fields and controls present on the form. The tree view is helpful when you want to select hidden elements that are not visible on the form preview. 

You can expand or collapse nodes in the tree view to see or hide the elements within a node. When you select an element in the tree view, it becomes highlighted in the form preview, and the property pane displays the properties for the element. 

   ![Tree view](media/tree-view.png)

### Open the tree view 
1. Open the form designer to create or edit a form. More information: [Create a form](#create-a-form) and [Edit a form](#edit-a-form)  
2. In the left pane, select **Tree View**.

## See also
[Overview of the model-driven form designer](form-designer-overview.md)  
[Add, move or delete fields on a form using form designer](add-move-or-delete-fields-on-form.md)  
[Add, move or delete sections on a form using form designer](add-move-or-delete-sections-on-form.md)  
[Add, move or delete tabs on a form using form designer](add-move-or-delete-tabs-on-form.md)  
[Create and edit fields](../common-data-service/create-edit-field-portal.md)
