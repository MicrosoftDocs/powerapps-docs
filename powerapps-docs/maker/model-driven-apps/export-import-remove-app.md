---
title: "Export, import, or remove a model-driven app | MicrosoftDocs"
description: "Learn you can export, import, or remove a model-driven app"
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

# Tutorial: Export, import, or remove an app

In this tutorial, you learn how to complete these solution tasks: export, import, and remove an app.

Model-driven apps are distributed as solution components. After you have created a model-driven app, you can make it available for other environments to use by packaging the app into a solution and then exporting it into a zip file. After the solution (.zip file) is successfully imported by the environment, the packaged app is available for use.

More information: [Solutions overview](../common-data-service/solutions-overview.md).
  
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
  
## Remove (delete) an app  
Remove apps that are obsolete in your environment.

1. Sign in to [PowerApps](https://web.powerapps.com/).
2. Open [solution explorer](advanced-navigation.md#solution-explorer). 
3. In the solution window, under **Components**, select **Apps**.
4. Select the app that you want to delete, and then select **Delete** on the command bar.

    ![Delete an app](media/app-module-solution-window.png "Delete an app")

5. In the confirmation message that appears, select **Delete**.

   The app is deleted from your environment.
  
If the component has dependencies (such as relationships), you must remove the dependencies before you can delete the app. To see the dependencies of an app, select the app, and then select **Show Dependencies** on the command bar.

> [!NOTE]
> When you delete the app, we recommend that you delete its associated site map. If you do not delete the associated site map, the site map designer displays an error the first time you try to create another app with the same name. However, you can ignore the error, and the error will not appear when you try to create the app again.<br />

## Next steps  
 [Design custom business apps by using the app designer](design-custom-business-apps-using-app-designer.md)
