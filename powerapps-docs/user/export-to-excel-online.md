---
title: "Export your data to Excel Online in model-driven Power Apps| MicrosoftDocs"
description: How to export your data to Excel Online in model-driven Power App
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 8/27/2020
ms.author: mkaur
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---
# Export your data to Excel Online 

You can quickly do an ad-hoc analysis of your data that is in your app by exporting the data from the app to Excel Online.
  
When you make changes to your data in Excel Online, you can save the updated information in the app. Remember to keep the existing format of the Excel cells to prevent problems during import. Any information added to the spreadsheet, such as graphs, charts, or colors, will not be saved.  
  
## Prerequisites  
  
- This feature requires that you have an Office 365 subscription or a subscription to an online service such as SharePoint Online or Exchange Online.
  
- You need a Microsoft account.    
  
## Open app data in Excel Online  

The option to open data in Excel Online isn’t available in all row types. If you don’t see the option, it’s not available for that row.  
  
> [!NOTE]
> Updated data in an app won’t immediately be reflected in Excel Online if the same view was opened in the last two minutes in Excel Online. After that time frame, any updated data should show in Excel Online.
  
To open a list of rows in an app, on the command bar select the **Export to Excel** menu and then select **Open in Excel Online**. 

   > [!div class="mx-imgBorder"] 
   > ![Export to excel](media/export_to_excel.png "Select export to Excel")

  
## Save your data and import it back to the app  
  
1. Once you are done making any changes, select **Save**.  
  
   > [!NOTE]
   > - The data for *ad-hoc* analysis with Excel Online is stored temporarily. Any additions, such as charts, calculations, and columns, won’t be saved back to the app from the ad-hoc analysis in Excel Online.  
   > 
   > - The file import might fail if you make a lot of changes. If you need to make a lot of changes to your data and import it back to the app, it’s recommended that you export the worksheet in Excel instead.  
   > 
   > - By design, you can’t do a **File** > **Save As** in Excel Online. If you do, you’ll get a **Can’t Save Workbook** error message.   
2. On the **Data Submitted for Import** dialog box, select **Close**.  
  

  

 


[!INCLUDE[footer-include](../includes/footer-banner.md)]