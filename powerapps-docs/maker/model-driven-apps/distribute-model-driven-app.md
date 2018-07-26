---
title: "Distribute a model-driven app | MicrosoftDocs"
description: "Learn how you distribute a model-driven app using solutions"
keywords: ""
ms.date: 05/31/2018
ms.service: crm-online
ms.custom: 
ms.topic: article
applies_to:
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
ms.assetid: e82e7f64-37ad-41e5-acd7-16309881c6a2
author: "Mattp123"
ms.author: "matp"
manager: "kvivek"
ms.reviewer: 
ms.suite: 
ms.tgt_pltfrm: 
caps.latest.revision: 9
topic-status: Drafting
---

# Distribute a model-driven app

Model-driven apps are distributed as solution components. After you have created a model-driven app, you can make it available for other environments to use by packaging the app into a solution and then exporting it into a zip file. After the solution (.zip file) is successfully imported in the target environment, the packaged app is available for use. More information about solutions: [Solutions overview](../common-data-service/solutions-overview.md).
  
## Export an app  
 Export an app into a solution when you want other environments to use it. The process of exporting a solution includes:  

1. [Create a solution](../common-data-service/create-solution.md).
2. [Add apps to the solution](../common-data-service/import-update-export-solutions.md).
3. [Export the solution to a zip file](../common-data-service/import-update-export-solutions.md).

	> [!NOTE]
	> When you export an app by using a solution, the app URL is not exported.

Now you can share the created solution zip file with other environments to import and use the app.
  
## Import an app  
When you receive the solution zip file which contains the app that you want to import, open the solutions component page and import the solution. When the solution has been successfully imported, the app will be available in your environment.

More information: [Import, update, and export solutions](../common-data-service/import-update-export-solutions.md). 
