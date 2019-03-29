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
# Embedded canvas apps actions
**NavigateToMainForm(entityName, mainFormName, recordId)**  
Navigates the host form to a main form and displays the specified record.  
* **entityName** - A required string parameter that specifies the parent entity of the main form.  
* **formName** - A required string parameter that specifies the name of the main form to navigate to.  
* **recordId** - A required string parameter, that specifies the ID of the record to display in the main form.  
  
**NavigateToView(entityName, viewName)**  
Navigates the host form to a view.  
* **entityName** - A required string parameter that specifies the parent entity of the view.  
* **viewName** - A required string parameter that specifies the name of the main form to navigate to.  
  
**OpenQuickCreateForm(entityName)**  
Opens the default quick create form for an entity.  
* **entityName** - A required string parameter that specifies the parent entity of the quick create form.  
  
**RefreshForm(showPrompt)**  
Refreshes the data on the host form.  
* **showPrompt** - A required string parameter that indicates if a confirmation prompt should be displayed to the user before saving any unsaved data on the host form. Values should be "true" or "false".
  
**SaveForm()**  
Saves the data on the host form.  
