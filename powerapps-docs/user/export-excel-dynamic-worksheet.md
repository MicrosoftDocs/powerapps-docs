---
title: "Export to an Excel dynamic worksheet (Dynamics 365 Customer Engagement) | MicrosoftDocs"
ms.custom: ""
ms.date: 03/02/2017
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
ms.assetid: fd391660-beac-4f58-9499-90c8e807dc97
caps.latest.revision: 53
author: "jimholtz"
ms.author: "jimholtz"
manager: "brycho"
search.audienceType: 
  - enduser
search.app: 
  - D365CE
---
# Export to an Excel dynamic worksheet

[!INCLUDE[cc-applies-to-update-9-0-0](../includes/cc_applies_to_update_9_0_0.md)]

Export data to a [!INCLUDE[pn_MS_Excel_Full](../includes/pn-ms-excel-full.md)] worksheet so users can have the latest [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)] information any time they view the worksheet. Imagine the CEO of your company getting the critical information they need without having to navigate [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)] but instead, merely opening the [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] link on their desktop. You can export up to 100,000 records at a time.  
  
## Prerequisites  
 To view and refresh dynamic data, [!INCLUDE[pn_microsoft_dynamics_crm_for_outlook](../includes/pn-microsoft-dynamics-crm-for-outlook.md)] must be installed on the same computer you're using to view the [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] data.  
  
> [!IMPORTANT]
>  Your operating system region settings (in [!INCLUDE[pn_ms_Windows_short](../includes/pn-ms-windows-short.md)], **Control Panel** > **Region**) and [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)] organization language and locale (**Settings** > **Administration** > **System Settings** > **Formats tab** > **Current Format**) should be the same. If not, refreshing dynamic data with **Refresh from CRM** might cause data changes.  
  
## Export data to an Excel dynamic worksheet  
 You can’t export data to a dynamic worksheet in [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] for all [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)] record types. If you don’t see the option, it’s not available for that record.  
  
1. Open a list of records in the [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] web application or in [!INCLUDE[pn_microsoft_dynamics_crm_for_outlook](../includes/pn-microsoft-dynamics-crm-for-outlook.md)]. In the web app, click the arrow to the right of **Export to Excel**. In [!INCLUDE[pn_dyn_365_app_outlook](../includes/pn-dyn-365-app-outlook.md)], click **Data** > **Export to Excel**.  
  
2. Click **Dynamic Worksheet**.  
  
3. Under **Common Tasks**, configure the column settings and then click **Export**.  
  
4. Click **Save** and then save the .xlsx file. Make note of the location where you saved the file.  
  
   > [!NOTE]
   >  If you’re going to edit the data file later, it’s recommended that you save the file before you open it. Otherwise, you might get this error message: Microsoft **Excel cannot open or save any more documents because there is not enough available memory or disk space**.  
   > 
   >  To fix the issue do this:  
   > 
   > 1. Open Excel and go to **File** > **Options** > **Trust Center** **Settings Center Settings…** > **Protected View**.  
   >    2.  In **Protected View**, uncheck all three items.  
   >    3.  Then click **OK** > **OK**.  
   > 
   >    We still strongly recommend that you save and then open the data file, rather than disabling protected view which may put your computer at risk.  
  
5. Open [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] and then open the .xlsx file you saved in the previous step.  
  
6. If you see the security warning **External Data Connections have been disabled**, click **Enable Content**.  
  
7. To refresh data in the file, on the **Data** tab, click **Refresh from CRM**.  
  
   > [!NOTE]
   >  To view and refresh dynamic data, [!INCLUDE[pn_microsoft_dynamics_crm_for_outlook](../includes/pn-microsoft-dynamics-crm-for-outlook.md)] must be installed. If it is already installed and configured, click **Refresh from CRM** to sign in to [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)].  If you do not want to be prompted again to sign in, click **Save my email address and password** in the Sign-In page.  
   > 
   > [!NOTE]
   >  If you have a phone numbers that starts with **+** or **–**, for example +1-123-456-7890, when you refresh the dynamic worksheet the phone number field will not display the number correctly.   
   > To avoid the issue, use a space or parentheses **()**, like this: +1 123-456-7890 or +1 (123)-456-7890  
  
## Tips  
  
- You can email a dynamic [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] file or store it as a shared file if the recipients are in the same domain as you. When recipients open the dynamic file, they’ll see data they have permission to view in [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)], so the data they see may be different from what you see.  
  
- Some system views, such as Accounts: No Campaign Activities in Last 3 Months, can be exported only to a static [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] worksheet.  
  
- In [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)], money values are exported to [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] as numbers. After you have completed the export, to format the data as currency, see the [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)][!INCLUDE[pn_doc_help_long](../includes/pn-doc-help-long.md)] topic titled “Display numbers as currency.”  
  
- The data and time values that you see in [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)] show up as Date only when you export the file to [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] but the cell actually shows both the date and time.  
  
- If you’re going to make changes and import the data file back in to [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)], remember that secured, calculated, and composite fields (e.g. Full Name) are read-only and can’t be imported in to [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)]. You’ll be able to edit these fields in [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] but when you import the data back in to [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)] these fields will not be updated. If you want to update these fields such as a contact’s name then it’s recommend that you use that view to export your data, update them in Excel, and import them back to [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)] for changes.  
  
<!--   If you’re not on [!INCLUDE[pn_crm_online_2015_update_1_shortest](../includes/pn-crm-online-2015-update-1-shortest.md)] or [!INCLUDE[pn_crm_2016](../includes/pn-crm-2016.md)] and are using the [!INCLUDE[pn_Office_365](../includes/pn-office-365.md)][!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] web app, you must save the file, open the file using the [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] desktop application, and then resave the file to the . xlsx format. You can then reopen the [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] document in [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] Online.  
-->  
## Privacy notice  
[!INCLUDE[cc_privacy_export_to_excel](../includes/cc-privacy-export-to-excel.md)]
  
### See also  
 [Export data to Excel](export-data-excel.md)   
 [Analyze with Excel Online](analyze-dynamics-365-data-excel-online.md)   
 [Export to Excel PivotTable](export-excel-pivottable.md)   
 [Edit the default filter of a report](edit-default-filter-report.md)       
 [Create, edit, or save an Advanced Find search](save-advanced-find-search.md)
