---
title: "ModelDrivenFormIntegration control properties and actions | MicrosoftDocs"
description: Learn about ModelDrivenFormIntegration control properties and actions
ms.custom: ""
ms.date: 06/17/2021
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "conceptual"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
ms.assetid: 00e62904-2ce9-4730-a113-02b1fedbf22e
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
# ModelDrivenFormIntegration control properties and actions

Canvas apps embedded on model-driven forms contain a special control named **ModelDrivenFormIntegration**. This control is responsible for 
bringing contextual data from the host model-driven form to the embedded canvas app.  

This topic explains the properties and actions available on the ModelDrivenFormIntegration control.

| Property or action | Description |
|:--------------|:-------------------------|
|**DataSource** | Should be set to the data source connected to the parent table of the host model-driven form. <br />Automatically set when [embedding a new canvas app](embedded-canvas-app-add-classic-designer.md). |
|**Item** | Read-only property that enables the embedded canvas app to access the row from the host model-driven form. <br />As an example, to get the value of a column with the name accountnumber and display name Account Number, you can use ModelDrivenFormIntegration.Item.accountnumber or ModelDrivenFormIntegration.Item.'Account Number'. |
|**OnDataRefresh** | The formula in this property is evaluated when the host model-driven form saves data. <br />Use it to refresh the data source connected to the parent table of the host model-driven form and to perform other actions like setting or updating variables. <br /> As an example, setting it to the formula below will refresh the Accounts data source and set a variable named CurrentAccountNumber to the value of the Account Number column of the current row. <br /> Refresh(Accounts); Set(CurrentAccountNumber, ModelDrivenFormIntegration.Item.'Account Number') <br /> The OnDataRefresh action should only be used to refresh data within the embedded canvas app. We don’t recommend that you use the OnDataRefresh action to save changes within the embedded canvas app. More information: [Saving data in an embedded canvas app](embedded-canvas-app-guidelines.md#saving-data-in-an-embedded-canvas-app) |
|**RefreshForm** | Refreshes the data on the host model-driven form. <br />See [Perform predefined actions on the host form](embedded-canvas-app-actions.md#refreshformshowprompt) for details. |
|**SaveForm** | Saves the data on the host model-driven form. <br />See [Perform predefined actions on the host form](embedded-canvas-app-actions.md#saveform) for details.  |
|**NavigateToMainForm** | Navigates the host model-driven form to a main form and displays the specified row. <br />See [Perform predefined actions on the host form](embedded-canvas-app-actions.md#navigatetomainformentityname-mainformname-recordid) for details. |
|**NavigateToView** | Navigates the host model-driven form to a view. <br />See [Perform predefined actions on the host form](embedded-canvas-app-actions.md#navigatetoviewentityname-viewname) for details.  |
|**OpenQuickCreateForm** | Opens the default quick create form for an table.  <br />See [Perform predefined actions on the host form](embedded-canvas-app-actions.md#openquickcreateformentityname) for details.  |
|**Data** | Read-only property used by the framework to send some key data from the host model-driven form to the embedded canvas app.  <br /> Do not use this property. Use Item to access the row from the host model-driven form.  |

## See also
[Embed a canvas app on a model-driven form](embed-canvas-app-in-form.md) <br />
[Add an embedded canvas app on a model-driven form](embedded-canvas-app-add-classic-designer.md) <br />
[Edit a canvas app embedded on a model-driven form](embedded-canvas-app-edit-classic-designer.md) <br />
[Customize the screen size and orientation of a canvas app embedded on a model-driven form](embedded-canvas-app-customize-screen.md) <br />
[Perform predefined actions on the host form from within an embedded canvas app](embedded-canvas-app-actions.md) <br />
[Share an embedded canvas app](share-embedded-canvas-app.md) <br />
[Guidelines on working with embedded canvas apps](embedded-canvas-app-guidelines.md) <br />
[Migrating embedded canvas apps on model-driven forms created using the public preview release to latest](embedded-canvas-app-migrate-from-preview.md) <br />


[!INCLUDE[footer-include](../../includes/footer-banner.md)]