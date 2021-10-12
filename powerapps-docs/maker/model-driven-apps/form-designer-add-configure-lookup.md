---
title: Configure a lookup component on a form | MicrosoftDocs"
description: Learn how to create a lookup for a form
ms.custom: ""
ms.date: 08/26/2019
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "conceptual"
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

# Configure a lookup component on a form  

Lookups helps a user to choose row(s) from a **related** table and is automatically added when a lookup column is added to a form.

For example we might pick the account that relates to a sales invoice.

:::image type="content" source="../../user/media/automatically-populate-matching-records.png" alt-text="Using a lookup column":::

[Learn more about the lookup field user experience](../../user/lookup-field.md)

## Configure a lookup component

Makers can configure a lookup component using the form designer.

These are the properties available to configure when using a lookup component on a form using the form designer.

|Area  |Name  |Description  |
|---------|---------|---------|
| **Display options** | **Table** |  The related table that the lookup column connects to. |
| **Display options** | **Default view** |  The view of the table selected in the **Table** property that can be used to get and display the list of rows that app users can select in the lookup drop-down list. |
| **Display options** | **Allow users to change view** |  When selected, app users can change from the **Default view** to another view of the table selected in the **Table** property. |
| **Display options** | **Show all views** |  When selected, app users can change from the **Default view** to all other views of the table selected in the **Table** property. <br /><br />This property is only available when **Allow users to change view** is selected. |
| **Display options** | **Selected views** |  A list of views of the table selected in the **Table** property that app users can change to from the **Default view**. <br /><br />This property is only available when **Allow users to change view** is selected and **Show all views** is unselected. |

The options manifest themselves within the app designer in the following way.

:::image type="content" source="../../maker/model-driven-apps/media/configure-lookup-component.png" alt-text="Advanced Settings":::

## See also
[Overview of the model-driven form designer](form-designer-overview.md)  
[Create, edit, or configure forms using the form designer](create-and-edit-forms.md)  
[Add, configure, move, or delete columns on a form](add-move-or-delete-fields-on-form.md)  
[Add, configure, move, or delete components on a form](add-move-configure-or-delete-components-on-form.md)  
[Add, configure, move, or delete sections on a form](add-move-or-delete-sections-on-form.md)  
[Add, configure, move, or delete tabs on a form](add-move-or-delete-tabs-on-form.md)  
[Configure header properties in the form designer](form-designer-header-properties.md)  
[Add and configure a sub-grid component on a form](form-designer-add-configure-subgrid.md)  
[Add and configure a quick view component on a form](form-designer-add-configure-quickview.md)  
[Using the tree view in the form designer](using-tree-view-on-form.md)  
[Create and edit columns](../data-platform/create-edit-field-portal.md)  


[!INCLUDE[footer-include](../../includes/footer-banner.md)]