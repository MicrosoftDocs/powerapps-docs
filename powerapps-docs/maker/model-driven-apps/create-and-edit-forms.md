---
title: "Create and edit forms using the model-driven form designer | MicrosoftDocs"
ms.custom: ""
ms.date: 12/13/2018
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
Use the new form designer to create and design forms for model-driven apps.

> [!NOTE]
> This feature is currently in preview. <br />
> [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]
>  The new model-driven form designer currently only supports creating and editing main forms. To create and edit other form types, see [Create a model-driven app quick view form to view information about a related entity](create-edit-quick-view-forms.md) and [Create or edit model-driven app quick create forms for a streamlined data entry experience](create-edit-quick-create-forms.md). 

## Create a form 
1. Sign in to [PowerApps](https://web.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc). 
2. On the left navigation pane, expand **Data** and then select **Entities**. 
3. Select an entity, such as the account entity, and then select the **Forms** tab. 
4. Select **Add form**, and then select **Main form**.     
    The contents of the new form are filled using the existing main form definition. If multiple main forms exist, the form at the top of the list in the form order use to fill the new form. 
5. Select **Save** to save the form or select **Publish** if you want the save and make your changes visible to end-users.  

## Edit a form 
1. Sign in to [PowerApps](https://web.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc). 
2. On the left navigation pane, expand, select **Data**, and then select **Entities**. 
3. Select an entity, such as the account entity, and then select the **Forms** tab.
4. Select the main form that you want to edit and then in the command bar, select **Edit form**.  
   Alternatively, select **...** next to the form you want, and then select **Edit form**. 
5. Select **Save** to save the form or select **Publish** if you want the save and make your changes visible to end-users. 

## Add and remove fields 
To add or remove fields on a form, use the fields pane. The fields pane lets you search and filter to help you quickly find fields. It also includes the option to show only unused fields. 

### Add a field 
1. Open the form designer to create or edit a form. 
2. In the form preview, select another existing field or a section. 
   <br /> When you select an existing field, the new field is added below the existing field. When you select a section, the new field is added at the bottom in the first column of the section. 
3. In the command bar, select **Add field** or in the panes area on the left, select **Fields**.  
   The fields pane is open by default when the form designer is opened. 
4. In the **Fields** pane, search, filter, or scroll to find the field you want to add. 
   If you can't find a field, it may already be on the form. Clear **Show only unused fields** to view all field including the ones already added to the form. 
5. In the **Fields** pane, select a field to add it to the form. 
   Alternatively, select **...** next to the form you want, and then select **Edit form**. 
6. On the **Fields** pane select **Close** or in the left pane area, select **Fields** to close the fields pane. 
7. Select **Save** to save the form or select **Publish** if you want the save and make your changes visible to end-users. 

### Delete a field 
1. Open the form designer to create or edit a form. <!-- (LINK TO ARTICLE #2). -->
2. In the form preview, select the field that you want to remove from the form and delete. 
3. Select **Delete**. 
   If you delete a field by mistake, select **Undo** to revert the delete action. 
   You can't delete a field that is required or locked. 

## See also
[Overview of the model-driven form designer](form-designer-overview.md)