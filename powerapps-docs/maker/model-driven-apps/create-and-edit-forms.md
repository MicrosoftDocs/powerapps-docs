---
title: "Create, edit, or configure forms using the model-driven form designer | MicrosoftDocs"
description: Learn how to create and edit model-driven app forms
ms.custom: ""
ms.date: 05/29/2025
ms.update-cycle: 180-days
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: get-started
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
author: "Aneesmsft"
ms.subservice: mda-maker
ms.author: "matp"
ms.collection: bap-ai-copilot
tags: 
  - "Power Apps maker portal impact"
search.audienceType: 
  - maker
---
# Create, edit, or configure forms using the form designer

Use the form designer to create, edit, or configure forms for model-driven apps.

## Create a form

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc). 
1. On the left navigation pane, select **Solutions**, and open the solution you want. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Open a table, such as the account table, and then select the **Forms** area.
1. Select **New form**, and then select one of the following form types:
   - **Main form** The primary form type for interaction by users with record data.  The contents of the new form are filled using the existing main form definition. If multiple main forms exist, the form at the top of the list in the form order for your app is used to fill the new form.
   - **Quick view form** Quick view forms appear within a main form to display additional read-only data referencing a lookup column.
      [Learn more about main forms](create-edit-main-forms.md)
   - **Quick create form** Best for creating new records quickly where only essential columns are required. Appears in a side panel so users don't navigate away from the current screen.
   - **Card form** For displaying compact data in a layout that is good for small screens or areas in a subgrid or view.
 
1. Enter a **Form name**, and optionally enter a **Description**.
1. If you want to have suggestions from Copilot for the columns to create for the form based on the **Form name** and **Description** values, select **Get AI generated column suggestions**. For more information about using this AI feature, go to [Column suggestions by Copilot](#column-suggestions-by-copilot).
   :::image type="content" source="media/new-form.png" alt-text="Create a new form card in Power Apps" lightbox="media/new-form.png":::
1. Select **Create**.

## Edit a form

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. On the left navigation pane, select **Solutions**, and open the solution you want. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Open a table, such as the account table, and then select the **Forms** area.
1. Select the form that you want, and then on the command bar, select **Edit**.
1. Make changes such as adding columns or [configuring properties](#form-properties).
1. When you're done making changes to the form, select **Save only** to save the form, or select **Save and Publish** to save and have your changes available to app users.

## Column suggestions by Copilot

Use column suggestions by Copilot to select the best columns to display in your model-driven app form. Instead of using the default fields that Power Apps selects, makers can view suggestions from Copilot. The column suggestions are based on the form name and description. Makers review the suggestions and make adjustments as needed, saving time and improving the quality of the app.

### Prerequisites

- Prerequisites for Copilot in Power Apps features: [Copilot in Power Apps overview (preview)](../canvas-apps/ai-overview.md)
- See if this feature is available in your region: [Product availability report](https://releaseplans.microsoft.com/availability-reports/?report=productgeoreport)
- Learn how to turn on Copilots in your region: [Turn on copilots and generative AI features](/power-platform/admin/geographical-availability-copilot)

### How column suggestions work

Column suggestions are available when you create a new form or view for a Microsoft Dataverse table.

Column suggestions are available for the following form types:

- Quick view
- Quick create

To understand the AI impact of field suggestions by Copilot in Power Apps, go to [FAQs for field suggestions by Copilot](../common/faq-field-suggestions.md).

## Form properties

These are the properties available to configure a form when you create or edit a form using the form designer.

|Name  |Description  |
|---------|---------|
|**Title**  | Enter a name that is meaningful to other makers and app users. This name is shown to app users. If users have access to multiple forms for a table, they will use this name to differentiate between the available forms. <br /><br />This property is required. |
|**Description** |  Enter a description that explains how the form is different from other main forms. This description is only shown to makers in the list of forms for a table in the solution explorer. |
|**Max Width** | Set a maximum width (in pixels) to limit the width of the form. The default value is 1900. <br /><br />This property is required. |
|**Show image** | Show the table’s **Primary Image** if it has one set. This setting enables showing the image column in the header of the form. <br /><br /> More information: [Enable or disable table options](../data-platform/edit-entities.md#enable-or-disable-table-options) |

## See also

[Overview of the model-driven form designer](form-designer-overview.md)  
[Add, configure, move, or delete columns on a form](add-move-or-delete-fields-on-form.md)  
[Add, configure, move, or delete components on a form](add-move-configure-or-delete-components-on-form.md)  
[Add, configure, move, or delete sections on a form](add-move-or-delete-sections-on-form.md)  
[Add, configure, move, or delete tabs on a form](add-move-or-delete-tabs-on-form.md)  
[Configure header properties in the form designer](form-designer-header-properties.md)  
[Add and configure a subgrid component on a form](form-designer-add-configure-subgrid.md)
[Learn more about quick create forms](create-edit-quick-create-forms.md)
[Learn more about quick view forms](create-edit-quick-view-forms.md)
[Add and configure a quick view component on a form](form-designer-add-configure-quickview.md)  
[Configure a lookup component on a form](form-designer-add-configure-lookup.md)  

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
