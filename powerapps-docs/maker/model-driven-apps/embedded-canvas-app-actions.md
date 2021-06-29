---
title: "Perform actions on the host model-driven form from within an embedded canvas app | MicrosoftDocs"
description: Learn how to perform predefined actions in an embedded canvas app
ms.custom: ""
ms.date: 06/25/2019
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "reference"
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
# Perform predefined actions on the host model-driven form from within an embedded canvas app

[!INCLUDE [cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

Embedded canvas apps provide the ability to perform predefined actions on the host model-driven form. These actions enable makers to navigate, refresh and save the host model-driven form. Using these actions, an embedded canvas app can act as a more integral part of the model-driven form and the model-driven app.  

The **ModelDrivenFormIntegration** object now includes the following new methods to enable makers to perform actions on the host model-driven form.  
  
### NavigateToMainForm(entityName, mainFormName, recordId)
Navigates the host model-driven form to a main form and displays the specified row.  
* **entityName** - A required string parameter that specifies the parent table of the main form.  
* **formName** - A required string parameter that specifies the name of the main form to navigate to.  
* **recordId** - A required string parameter, that specifies the ID of the row to display in the main form.  
 
Calling the NavigateToMainForm method can show the following error messages.
  
| Error message | Troubleshooting guidance |
|:--------------|:-------------------------|
|**Table not found: *[EntityName]*** | Please check the value of the *entityName* parameter and ensure it is a valid table name and that the user has access to it. |
|**Form not found: *[FormName]*** | Please check the value of the *mainFormName* parameter and ensure it is a valid main form name and that the user has access to it. |
|**There was a problem loading the row.** | Please check the value of the *recordId* parameter and ensure it is a valid row ID and that the user has access to it. |
  
  
### NavigateToView(entityName, viewName)
Navigates the host model-driven form to a view.  
* **entityName** - A required string parameter that specifies the parent table of the view.  
* **viewName** - A required string parameter that specifies the name of the main form to navigate to.  
 
Calling the NavigateToView method can show the following error messages.
  
| Error message | Troubleshooting guidance |
|:--------------|:-------------------------|
|**Table not found: *[EntityName]*** | Please check the value of the *entityName* parameter and ensure it is a valid table name and that the user has access to it. |
|**View not found: *[ViewName]*** | Please check the value of the *viewName* parameter and ensure it is a valid view name and that the user has access to it. |
  
  
### OpenQuickCreateForm(entityName)  
Opens the default quick create form for an table.  
* **entityName** - A required string parameter that specifies the parent table of the quick create form.  
 
Calling the OpenQuickCreateForm method can show the following error messages.
  
| Error message | Troubleshooting guidance |
|:--------------|:-------------------------|
|**Table not found: *[EntityName]*** | Please check the value of the *entityName* parameter and ensure it is a valid table name and that the user has access to it. |
  
  
### RefreshForm(showPrompt)  
Refreshes the data on the host model-driven form.  
* **showPrompt** - A required boolean parameter that indicates if a confirmation prompt should be displayed to the user before saving any unsaved data on the host model-driven form. Values should be "true" or "false".
 
Calling the RefreshForm method can show the following error messages.
  
| Error message | Troubleshooting guidance |
|:--------------|:-------------------------|
|**Please use "true" or "false" as the parameter value.** | Please check the value of the *showPrompt* parameter and ensure that it is either "true" or "false". |
  
  
### SaveForm()  
Saves the data on the host model-driven form.  


> [!NOTE]
> If you do not see the IntelliSense for the methods to perform predefined actions in embedded canvas apps that were created prior to the functionality being made available; save, close and re-open the app. 

## See also
[Embed a canvas app on a model-driven form](embed-canvas-app-in-form.md) <br />
[Add an embedded canvas app on a model-driven form](embedded-canvas-app-add-classic-designer.md) <br />
[Edit a canvas app embedded on a model-driven form](embedded-canvas-app-edit-classic-designer.md) <br />
[Customize the screen size and orientation of a canvas app embedded on a model-driven form](embedded-canvas-app-customize-screen.md) <br />
[ModelDrivenFormIntegration control's properties and actions](embedded-canvas-app-properties-actions.md) <br />
[Share an embedded canvas app](share-embedded-canvas-app.md) <br />
[Guidelines on working with embedded canvas apps](embedded-canvas-app-guidelines.md) <br />
[Migrating embedded canvas apps on model-driven forms created using the public preview release to latest](embedded-canvas-app-migrate-from-preview.md) <br />


[!INCLUDE[footer-include](../../includes/footer-banner.md)]