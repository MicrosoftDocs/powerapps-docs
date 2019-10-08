---
title: "Solutions best practices in PowerApps | MicrosoftDocs"
description: "Learn about best practices when you work with solutions"
ms.custom: ""
ms.date: 10/08/2019
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 
caps.latest.revision: 55
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Best practices when working with solutions (new topic)
This topic describes best practices when you work with solutions. 

## Use a single managed solution to manage a model-driven app 
To update the app that was included in the managed solution, use update or patch solutions. Don’t install different managed solutions into an environment that have the same model-driven app. More information: [Import, update, and export solutions](import-update-export-solutions.md#update-solutions) and [Use segmented solutions and patches to export selected entity assets](use-segmented-solutions-patches-simplify-updates.md) 

## Use security roles to manage app access
Model-driven apps should have security roles assigned to control user access. More information: [Add security roles to a model-driven app](../model-driven-apps/share-model-driven-app.md#add-security-roles-to-the-app) 

## Delete the managed solution to delete a model-driven app 
To delete a model-driven app that was installed in the default solution as part of a managed solution, delete the managed solution. 
Don’t directly delete an app or app’s site map from the default environment that was installed as part of a managed solution. Doing so can cause solution upgrade or solution updates for the solution used to install the app to fail. An example of directly deleting a model-driven app includes opening the default solution in solution explorer and go to Model-driven Apps > select the app > select Delete.

### See also
[Solutions overview](solutions-overview.md)