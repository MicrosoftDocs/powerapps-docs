---
title: "Perform actions on the host form from within an embedded canvas app | MicrosoftDocs"
ms.custom: ""
ms.date: 03/29/2019
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
# Perform predefined actions on the host form from within an embedded canvas app
Embedded canvas apps provide the ability to perform predefined actions on the host form. These actions enable makers to navigate, refresh and save the host form. Using these actions, an embedded canvas app can act as a more integral part of the form and the model-driven app.  

> [!NOTE]
> This feature is currently in preview. <br />
> [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)] 

The **ModelDrivenFormIntegration** object now includes the following new methods to enable makers to perform actions on the host form.  
  
### NavigateToMainForm(entityName, mainFormName, recordId)
Navigates the host form to a main form and displays the specified record.  
* **entityName** - A required string parameter that specifies the parent entity of the main form.  
* **formName** - A required string parameter that specifies the name of the main form to navigate to.  
* **recordId** - A required string parameter, that specifies the ID of the record to display in the main form.  
 
Calling the NavigateToMainForm method can show the following error messages.
  
| Error message | Troubleshooting guidance |
|:--------------|:-------------------------|
|**Entity not found: *[EntityName]*** | Please check the value of the *entityName* parameter and ensure it is a valid entity name and that the user has access to it. |
|**Form not found: *[FormName]*** | Please check the value of the *mainFormName* parameter and ensure it is a valid main form name and that the user has access to it. |
|**There was a problem loading the record.** | Please check the value of the *recordId* parameter and ensure it is a valid record ID and that the user has access to it. |
  
  
### NavigateToView(entityName, viewName)
Navigates the host form to a view.  
* **entityName** - A required string parameter that specifies the parent entity of the view.  
* **viewName** - A required string parameter that specifies the name of the main form to navigate to.  
 
Calling the NavigateToView method can show the following error messages.
  
| Error message | Troubleshooting guidance |
|:--------------|:-------------------------|
|**Entity not found: *[EntityName]*** | Please check the value of the *entityName* parameter and ensure it is a valid entity name and that the user has access to it. |
|**View not found: *[ViewName]*** | Please check the value of the *viewName* parameter and ensure it is a valid view name and that the user has access to it. |
  
  
### OpenQuickCreateForm(entityName)  
Opens the default quick create form for an entity.  
* **entityName** - A required string parameter that specifies the parent entity of the quick create form.  
 
Calling the OpenQuickCreateForm method can show the following error messages.
  
| Error message | Troubleshooting guidance |
|:--------------|:-------------------------|
|**Entity not found: *[EntityName]*** | Please check the value of the *entityName* parameter and ensure it is a valid entity name and that the user has access to it. |
  
  
### RefreshForm(showPrompt)  
Refreshes the data on the host form.  
* **showPrompt** - A required boolean parameter that indicates if a confirmation prompt should be displayed to the user before saving any unsaved data on the host form. Values should be "true" or "false".
 
Calling the RefreshForm method can show the following error messages.
  
| Error message | Troubleshooting guidance |
|:--------------|:-------------------------|
|**Please use "true" or "false" as the parameter value.** | Please check the value of the *showPrompt* parameter and ensure that it is either "true" or "false". |
  
  
### SaveForm()  
Saves the data on the host form.  


> [!NOTE]
> Methods to perform predefined actions will not be available in embedded canvas apps that were created prior to this functionality being released. We are working on ways to have existing embedded canvas apps opt-in to new capabilities. In the meantime, here are some alternatives to bring over controls from existing embedded canvas apps to a new ones.
> - [Copy-paste controls](https://powerapps.microsoft.com/blog/copy-and-paste-controls-across-canvas-apps-available/) from the old app to your new app.  
> - Create and use [components for canvas apps](../canvas-apps/create-component.md) in your old app and import them in your new app.   

## See also
[Embed a canvas app on a model-driven form](embed-canvas-app-in-form.md) <br />
[Pass the current record as data context to an embedded canvas app](pass-current-embedded-canvas-app.md) <br />
[Pass a list of related records as data context to an embedded canvas app](pass-related-embedded-canvas-app.md) <br />
[Share an embedded canvas app](share-embedded-canvas-app.md) <br />
[Guidelines on working with embedded canvas apps](embedded-canvas-app-guidelines.md)
