---
title: "ModelDrivenFormIntegration control's properties and actions | MicrosoftDocs"
ms.custom: ""
ms.date: 06/24/2019
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "get-started-article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
ms.assetid: 00e62904-2ce9-4730-a113-02b1fedbf22e
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
# ModelDrivenFormIntegration control's properties and actions
Canvas apps embedded on model-driven forms contain a special control named **ModelDrivenFormIntegration**. This control is responsible for 
bringing contextual data from the host model-driven form to the embedded canvas app.  
This topic explains the properties and actions available on the ModelDrivenFormIntegration control.

| Property or action | Description |
|:--------------|:-------------------------|
|**DataSource** | Should be set to the data source connected to the parent entity of the host model-driven form. <br />Automatically set when [embedding a new canvas app](embedded-canvas-app-add-classic-designer.md#embedding-a-new-canvas-app-on-a-model-driven-form) but needs to be manually set when [embedding an existing canvas app](embedded-canvas-app-add-classic-designer.md#embedding-an-existing-canvas-app-on-a-model-driven-form). |
|**DataSource.Item** | Read-only property that enables the embedded canvas app to access the record from the host model-driven form. <br />As an example, to get the value of a field with the name accountnumber and display name Account Number, you can use ModelDrivenFormIntegration.Item.accountnumber or ModelDrivenFormIntegration.Item.'Account Number'. |
|**OnDataRefresh** | The formula in this property is evaluated when the host model-driven form saves data. <br />Use it to refresh the data source connected to the parent entity of the host model-driven form and to perform other actions like setting or updating variables. |
|**RefreshForm** | Refreshes the data on the host model-driven form. <br />See [Perform predefined actions on the host form](embedded-canvas-app-actions.md#refreshformshowprompt) for details. |
|**SaveForm** | Saves the data on the host model-driven form. <br />See [Perform predefined actions on the host form](embedded-canvas-app-actions.md#saveform) for details.  |
|**NavigateToMainForm** | Navigates the host model-driven form to a main form and displays the specified record. <br />See [Perform predefined actions on the host form](embedded-canvas-app-actions.md#navigatetomainformentityname-mainformname-recordid) for details. |
|**NavigateToView** | Navigates the host model-driven form to a view. <br />See [Perform predefined actions on the host form](embedded-canvas-app-actions.md#navigatetoviewentityname-viewname) for details.  |
|**OpenQuickCreateForm** | Opens the default quick create form for an entity.  <br />See [Perform predefined actions on the host form](embedded-canvas-app-actions.md#openquickcreateformentityname) for details.  |
|**DataSource.Data** | Read-only property that can be used by the embedded canvas app to access the data from the host model-driven form. |
|**DataSource.Data.ItemId** | Please check the value of the *entityName* parameter and ensure it is a valid entity name and that the user has access to it. |
|**DataSource.Data.RefreshedOn** | Please check the value of the *entityName* parameter and ensure it is a valid entity name and that the user has access to it. |

## See also
[Embed a canvas app on a model-driven form](embed-canvas-app-in-form.md) <br />
[Pass the current record as data context to an embedded canvas app](pass-current-embedded-canvas-app.md) <br />
[Pass a list of related records as data context to an embedded canvas app](pass-related-embedded-canvas-app.md) <br />
[Share an embedded canvas app](share-embedded-canvas-app.md) <br />
[Guidelines on working with embedded canvas apps](embedded-canvas-app-guidelines.md)
