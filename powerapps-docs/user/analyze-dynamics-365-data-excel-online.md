---
title: "Analyze your Dynamics 365 Customer Engagement data in Excel Online | MicrosoftDocs"
ms.custom: ""
ms.date: 09/15/2017
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
ms.assetid: 0762789a-7cae-49a2-b2aa-8346115c2b9e
caps.latest.revision: 30
author: "jimholtz"
ms.author: "jimholtz"
manager: "sakudes"
search.audienceType: 
  - enduser
search.app: 
  - D365CE
---
# Analyze your Customer Engagement data in [!INCLUDE[pn_excel_online](../includes/pn-excel-online.md)]

[!INCLUDE[cc-applies-to-update-9-0-0](../includes/cc_applies_to_update_9_0_0.md)]

 No need to leave [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)] to analyze your data. Now you can do a quick *ad-hoc* analysis using [!INCLUDE[pn_microsoft_excel_online](../includes/pn-microsoft-excel-online.md)] in [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)].  
  
 For example, if you’re a sales manager, you might want to analyze the opportunities your team owns and review key performance indicators (KPIs) to see how you can assist your team members. If you’re a sales rep, you can open your opportunities in [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] and conduct what-if analysis for different incentive scenarios. Or, you may want to quickly open the data in [!INCLUDE[pn_excel_online](../includes/pn-excel-online.md)] so that you can copy it somewhere else such as an email.  
  
 When you make changes to your data in [!INCLUDE[pn_excel_online](../includes/pn-excel-online.md)], you can save the updated information in [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)]. Remember to keep the existing format of the [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] cells to prevent problems during import. Adding additional information to the spreadsheet, such as graphs, charts, or colors, will not be saved.  
  
## Prerequisites  
  
- [!INCLUDE[cc_feature_requires_office_365](../includes/cc-feature-requires-office-365.md)]  
  
- You need a [!INCLUDE[cc_Microsoft](../includes/cc-microsoft.md)] account.  
  
- You need export to [!INCLUDE[pn_excel_short](../includes/pn-excel-short.md)] privileges in [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)].  
  
## Open [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] data in [!INCLUDE[pn_excel_online](../includes/pn-excel-online.md)]  
 The option to open data in [!INCLUDE[pn_excel_online](../includes/pn-excel-online.md)] isn’t available in all [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] record types. If you don’t see the option, it’s not available for that record.  
  
> [!NOTE]
>  Updated data in [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] won’t immediately be reflected in [!INCLUDE[pn_excel_online](../includes/pn-excel-online.md)] if the same view was opened in the last two minutes in [!INCLUDE[pn_excel_online](../includes/pn-excel-online.md)]. After that timeframe, any updated data should show in [!INCLUDE[pn_excel_online](../includes/pn-excel-online.md)].  
  
To open a list of records in [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)], click **Export to Excel** > **Open in [!INCLUDE[pn_excel_online](../includes/pn-excel-online.md)]**.  
  
 ![Export Dynamics 365 data to Excel Online](media/export-to-excel-online.png "Export Dynamics 365 data to Excel Online")  
  
> [!NOTE]
>  By default, you can’t open your [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] data in [!INCLUDE[pn_excel_online](../includes/pn-excel-online.md)] in the **Advanced Find** view. However, you can save your advanced find as a personal view and then go to your personal view to do an ad-hoc analysis in [!INCLUDE[pn_excel_online](../includes/pn-excel-online.md)].  
  
## Save your data and import it back to [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)]  
  
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
 
