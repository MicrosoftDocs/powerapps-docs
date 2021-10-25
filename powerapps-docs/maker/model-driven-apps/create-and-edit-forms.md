---
title: "Create, edit or configure forms using the model-driven form designer | MicrosoftDocs"
description: Learn how to create and edit model-driven app forms
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

# Create, edit, or configure forms using the form designer 
Use the new form designer to create, edit, or configure forms for model-driven apps.

> [!IMPORTANT]
> The new model-driven form designer does not currently support editing card forms. More information: [Form types](types-forms.md)

## Create a form 
1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc). 
2. On the left navigation pane, expand **Data**, and then select **Tables**.
> [!note]
> Many customisations to a table take place within [solutions](../model-driven-apps/model-driven-app-glossary.md#solution).  To update a form within a solution first navigate to your **Solution**, then select the **Table** followed by the **Forms** tab.

3. Select a table, such as the account table, and then select the **Forms** tab.

4. Select **Add form**, and then select one of the following
    - **Main form**  
    The primary form type for interaction by users with record data.  The contents of the new form are filled using the existing main form definition. If multiple main forms exist, the form at the top of the list in the form order for your app is used to fill the new form.
      [Learn more about main forms](create-edit-main-forms.md)
    - **Quick create form** [Learn more about quick create forms](create-edit-quick-create-forms.md)
    - **Quick view form** [Learn more about quick view forms](create-edit-quick-view-forms.md)
5. On completion of changes to the form, select **Save** to save the form, or select **Publish** if in order to save in addition to making changes visible to app users within the organization.  

An extract of this process is shown below.
:::image type="content" source="media/create-and-edit-a-model-driven-form/create-main-form.gif" alt-text="Sample model-driven app":::

## Edit a form 
1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
2. On the left navigation pane, expand **Data**, and then select **Tables**.  Alternatively, navigate to the table via a solution.
3. Select a table, such as the account table, and then select the **Forms** tab.
4. Select the form name where edits are required.  
    - The row in the grid that relates to a form can be selected, and then in the command bar, select **Edit form**
    - Another alternative is to select **...** next to the form name, and then in the menu, select **Edit form**.
5. On completion of changes to the form, select **Save** to save the form, or select **Publish** if in order to save in addition to making changes visible to app users within the organization.

## Configure a form
These are the properties available to configure a form when creating or editing a form using the form designer.

|Name  |Description  |
|---------|---------|
|**Title**  | Enter a name that is meaningful to other makers and app users. This name is shown to app users. If users have access to multiple forms for a table they will use this name to differentiate between the available forms. <br /><br />This property is required. |
|**Description** |  Enter a description that explains how the form is different from other main forms. This description is only shown to makers in the list of forms for a table in the solution explorer. |
|**Max Width** | Set a maximum width (in pixels) to limit the width of the form. The default value is 1900. <br /><br />This property is required. |
|**Show image** | Show the table’s **Primary Image** if it has one set. This setting will enable showing the image column in the header of the form. <br /><br /> See Enable or disable table options for more information about table options. |

## See also
[Overview of the model-driven form designer](form-designer-overview.md)  
[Add, configure, move, or delete columns on a form](add-move-or-delete-fields-on-form.md)  
[Add, configure, move, or delete components on a form](add-move-configure-or-delete-components-on-form.md)  
[Add, configure, move, or delete sections on a form](add-move-or-delete-sections-on-form.md)  
[Add, configure, move, or delete tabs on a form](add-move-or-delete-tabs-on-form.md)  
[Configure header properties in the form designer](form-designer-header-properties.md)  
[Add and configure a sub-grid component on a form](form-designer-add-configure-subgrid.md)
 [Learn more about quick create forms](create-edit-quick-create-forms.md)
 [Learn more about quick view forms](create-edit-quick-view-forms.md)
[Add and configure a quick view component on a form](form-designer-add-configure-quickview.md)  
[Configure a lookup component on a form](form-designer-add-configure-lookup.md)  
[Using the tree view in the form designer](using-tree-view-on-form.md)  
[Create and edit columns](../data-platform/create-edit-field-portal.md)  
[!INCLUDE[footer-include](../../includes/footer-banner.md)]