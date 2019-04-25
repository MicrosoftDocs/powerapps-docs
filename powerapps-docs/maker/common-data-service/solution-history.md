---
title: "View the history of a solution | MicrosoftDocs"
description: "Learn how to view the history of a solution"
keywords: 
ms.date: 04/25/2019
ms.service: powerapps
ms.custom: 
ms.topic: article
applies_to: 
  - Dynamics 365 for Customer Engagement (online)
  - Dynamics 365 for Customer Engagement Version 9.x
  - powerapps
ms.assetid: 
author: Mattp123
ms.author: matp
manager: kvivek
ms.reviewer: 
ms.suite: 
ms.tgt_pltfrm: 
caps.latest.revision: 
topic-status: Drafting
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# View the history of a solution

You can view details about a system (internal) or custom solution operation from the Solutions area of a model-driven app. An operation can be either a solution import or delete. The solution history displays information such as solution version, solution publisher, type of operation, operation start and end time, and operation status.

> [!div class="mx-imgBorder"] 
> ![](media/solutions-history-custom-view.png "Solutions history custom view")

Each solution history record is read-only and includes the following properties: 
- **Start Time**. The time in which the operation started. 
- **End Time**: The time in which the operation ended. 
- **Solution Version**. The version of the solution. 
- **Publisher Name**. The name of the publisher that is associated with the operation. More information: [Change the solution publisher prefix](change-solution-publisher-prefix.md)  
- **Operation**. The operation, such as import, export, or delete. More information: [Import, update, and export solutions](import-update-export-solutions.md)
- **Suboperation**: Denotes the type of operation, such as a new solution import or an update to an existing solution. 
- **Status**. The status of the operation, such as Completed or Not completed. 
- **Result**. The result of the operation, such as Success or Failure. 

## View solution history
1.	From a PowerApps model-driven app, select **Settings** ![Settings](../model-driven-apps/media/powerapps-gear.png) on the app toolbar, and then select **Advanced Settings**. 
2.	Select **Settings**, and then select **Solutions History**.

     > [!div class="mx-imgBorder"] 
     > ![](media/solution-history-sitemap.png "Solution History area")

The following views are available from the **Solutions** area. 
- **All Solutions History**. Displays both system and custom solutions. 
- **Custom Solutions History**. Displays only custom solutions. 
- **Internal Solutions History**. Displays only system customizations. 

### See also
[Solutions overview](solutions-overview.md) < br/>
[View solution layers](solution-layers.md)

