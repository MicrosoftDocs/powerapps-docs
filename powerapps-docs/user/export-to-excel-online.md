---
title: "Export your data to Excel Online in PowerApps| MicrosoftDocs"
ms.custom: ""
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 10/10/2018
ms.author: mduelae
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
  - D365CE
---
# Export your data to Excel Online 

You can quickly to a ad-hoc analysis of your data that is in Powerapps by exporting the data from your app to Microsoft Excel Online.
  
 When you make changes to your data in Microsoft Excel Online, you can save the updated information in PowerApps. Remember to keep the existing format of the Excel cells to prevent problems during import. Adding additional information to the spreadsheet, such as graphs, charts, or colors, will not be saved.  
  
## Prerequisites  
  
- This feature requires that you have an Office 365 subscription or a subscription to an online service such as SharePoint Online or Exchange Online.
  
- You need a Microsoft account.    
  
## Open PowerApps data in Excel Online  

 The option to open data in Excel Online isn’t available in all record types. If you don’t see the option, it’s not available for that record.  
  
> [!NOTE]
>  Updated data in Dynamics 365 won’t immediately be reflected in Excel Online if the same view was opened in the last two minutes in Excel Online. After that timeframe, any updated data should show in Excel Online.
  
To open a list of records in PowerApp, on the command bar click **Export to Excel** dropdown menu and then click **Open in Excel Online**.  
  
 ![Export to Excel Online](media/exportexcelonline.png "Export to Excel Online")  

  
## Save your data and import it back to PowerApps  (((((((((((( need to check))))))
  
1. On the top right, click **Save Changes to [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)]**.  
  
   > [!NOTE]
   > - The data for *ad-hoc* analysis with [!INCLUDE[pn_excel_online](../includes/pn-excel-online.md)] is stored temporarily. Any additions, such as charts, calculations, and columns won’t be saved from the ad-hoc analysis that you do in Excel Online back to [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)]. If you need to make lots of changes to your data and import it back to [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)], it’s recommended that you export the worksheet in [!INCLUDE[pn_microsoft_excel](../includes/pn-microsoft-excel.md)].  
   > 
   > - The file import might fail if you made a lot of changes or changed the format of the [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] file. If you need to make lots of changes to your data and import it back to [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)], it’s recommended that you export the worksheet in [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)].  
   > 
   > - By design, you can’t do a **File** > **Save As** in [!INCLUDE[pn_excel_online](../includes/pn-excel-online.md)]. If you do, you’ll get a **Can’t Save Workbook** error message.  
  
2. On the **Data Submitted for Import** dialog box, click **Close**.  
  
## Check the status of the data import  
 After you save your changes from [!INCLUDE[pn_excel_online](../includes/pn-excel-online.md)] to [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)], verify that the data has been imported back in to [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)].  
  
1. In the **Data Submitted for Import** dialog box, click **Imports**.  
  
    -OR-  
  
   [!INCLUDE[proc_settings_datamanagement](../includes/proc-settings-datamanagement.md)] Then click **Imports**.  
  
2. In the list of imported files, look for your imported file and check the status.  
  
## Watch this video  
 Find out how to analyze your data and transform it into meaningful knowledge with [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)][!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] integration.  

[What-if analysis using Excel](https://www.youtube.com/embed/NZNvWz9xuZ0)
  
 To see video captions, click the **Closed Caption (CC)** button ![YouTube Closed Caption button](media/youtube-closed-caption-button.png "YouTube Closed Caption button") in the lower-right corner of the [!INCLUDE[tn_youtube](../includes/tn-youtube.md)] window.  
  
 [![Banner for Dynamics 365 YouTube channel](media/see-more-videos-on-youtube.png "Banner for Dynamics 365 YouTube channel")](http://go.microsoft.com/fwlink/p/?LinkID=325001)  
<!-- The fwlink above is correct - updated to point to the how-to playlists
-->

## Community tools 

**Export to Excel** is a tool provided by the XrmToolbox community developed for [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)] Customer Engagement. See the [Developer tools](../developer/developer-tools.md) topic for community developed tools.

> [!NOTE]
> The community tools are not a product of [!include[pn_microsoft_dynamics](../includes/pn-microsoft-dynamics.md)] and does not extend support to the community tools. 
> If you have questions pertaining to the tool, please contact the publisher. More Information: [XrmToolBox](https://www.xrmtoolbox.com). 
     
### See also  
 [Export data to Excel](export-data-excel.md)   
 [Export to Excel PivotTable](export-excel-pivottable.md)   
 [Export to Excel static worksheet](export-excel-dynamic-worksheet.md)   
 [Import accounts, leads, or other data](import-accounts-leads-other-data.md) 
 
