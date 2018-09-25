---
title: "Export to an Excel PivotTable (Dynamics 365 Customer Engagement) | MicrosoftDocs"
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
ms.assetid: 5b798287-5c58-47da-a893-f00394d0ae94
caps.latest.revision: 46
author: "jimholtz"
ms.author: "jimholtz"
manager: "brycho"
search.audienceType: 
  - enduser
search.app: 
  - D365CE
---
# Export to an [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] PivotTable

[!INCLUDE[cc-applies-to-update-9-0-0](../includes/cc_applies_to_update_9_0_0.md)]

You can export [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)] data to a [!INCLUDE[pn_MS_Excel_Full](../includes/pn-ms-excel-full.md)] PivotTable to see patterns and trends in data. An [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] PivotTable is a great way to summarize, analyze, explore, and present your [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] data. You can export up to 100,000 records at a time.  
  
## Prerequisites  
  
- [!INCLUDE[pn_microsoft_dynamics_crm_for_outlook](../includes/pn-microsoft-dynamics-crm-for-outlook.md)] is required to export data to a PivotTable.  
  
- To view and refresh dynamic data, [!INCLUDE[pn_microsoft_dynamics_crm_for_outlook](../includes/pn-microsoft-dynamics-crm-for-outlook.md)] must be installed on the same computer you're using to view the [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] data.  
  
- On a default [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)] installation, before you export data to an [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] PivotTable, make sure that your [!INCLUDE[pn_MS_SQL_Server](../includes/pn-ms-sql-server.md)] allows remote connections.  
  
   ### Allow remote connections to SQL Server
  
  1. Start [!INCLUDE[pn_ms_SQL_Management_Studio_long](../includes/pn-ms-sql-management-studio-long.md)].  
  
  2. Connect to the [!INCLUDE[pn_SQL_Server_short](../includes/pn-sql-server-short.md)] instance.  
  
  3. Right-click the [!INCLUDE[pn_SQL_Server_short](../includes/pn-sql-server-short.md)] instance name, click **Properties**, click **Connections**, and then select the **Allow remote connections to this server** check box.  
  
- [!INCLUDE[pn_Windows_Firewall](../includes/pn-windows-firewall.md)] allows remote [!INCLUDE[pn_SQL_Server_short](../includes/pn-sql-server-short.md)] connections. [!INCLUDE[proc_more_information](../includes/proc-more-information.md)] [How to: Configure a Windows Firewall for Database Engine Access](https://msdn.microsoft.com/library/ms175043.aspx).  
  
## Export to an [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] PivotTable  
 The option to export data to an [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] PivotTable isn’t available in all [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] record types. If you don’t see the option, it’s not available for that record.  
  
1. Open a list of records in the [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] web application or in [!INCLUDE[pn_microsoft_dynamics_crm_for_outlook](../includes/pn-microsoft-dynamics-crm-for-outlook.md)]. In the web app, click the arrow to the right of **Export to [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)]**. In [!INCLUDE[pn_dyn_365_app_outlook](../includes/pn-dyn-365-app-outlook.md)], click **Data** > **Export to [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)]**.  
  
2. Click **Dynamic PivotTable**.  
  
3. In the **Select PivotTable Columns** list, select or clear the check boxes for the fields as needed, and then click **Export**.  
  
    By default, the **PivotTable Field List** includes only fields that are displayed in the **Select PivotTable Columns** list.  
  
4. Click **Save** and then save the .xlsx file. Make note of the location where you saved the file.  
  
   > [!NOTE]
   >  If you’re going to edit the data file later, it’s recommended that you save the file before you open it. Otherwise, you may get this error message: **[!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] cannot open or save any more documents because there is not enough available memory or disk space**.  
   > 
   >  To fix the issue do this:  
   > 
   > 1. Open [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] and go to **File** > **Options** > **Trust Center**  
   >    2.  Click **Trust Center Settings**, and then click **Protected View**.  
   >    3.  Under **Protected View**, clear the check boxes for all three items.  
   >    4.  Click **OK**, and then **OK**.  
   > 
   >    We still strongly recommend that you save and then open the data file, rather than disabling protected view, which may put your computer at risk.  
  
5. Open [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] and then open the .xlsx file you saved in the previous step.  
  
6. If you see the security warning **External Data Connections have been disabled**, click **Enable Content**.  
  
7. To refresh data in the file, on the **Data** tab click **Refresh from CRM**.  
  
   > [!NOTE]
   >  To view and refresh dynamic data, [!INCLUDE[pn_microsoft_dynamics_crm_for_outlook](../includes/pn-microsoft-dynamics-crm-for-outlook.md)] must be installed. If it is already installed and configured, click **Refresh from CRM** to sign in to [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)].  If you do not want to be prompted again to sign in, click **Save my email address and password** in the Sign-In page.  
  
8. Drag the fields from the PivotTable Field List to the PivotTable. For more information, see [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] Help.  
  
## Tips  
  
- If you export a list to a dynamic worksheet or PivotTable that you think will be useful to other [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)] users, you can add the list as a report, and then share it with others or make it available to all [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)] users.  
  
   If the recipients are in the same domain as you, and are [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)] users, you can email a dynamic [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] file, or store it as a shared file. When recipients open the dynamic file, they will see data they have permission to view in [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)], so the data they see may be different from what you see.  
  
- In [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)], money values are exported to [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] as numbers. After you have completed the export, to format the data as currency, see the [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)][!INCLUDE[pn_doc_help_long](../includes/pn-doc-help-long.md)] topic titled “Display numbers as currency.”  
  
- The data and time values that you see in [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)] show up as “Date” only when you export the file to [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] but the cell actually shows both the date and time.  
  
- If you’re going to make changes and import the data file back in to [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)], remember that secured, calculated, and composite fields (such as Full Name) are read-only and can’t be imported in to Dynamics 365. You’ll be able to edit these fields in Excel but when you import the data back in to [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)] these fields won’t be updated. If you want to update these fields such as a contact’s name, it’s recommend that you use that view to export your data, update them in [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)], and import them back to [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)] for changes.  
  
- Some system views, such as Accounts: No Campaign Activities in Last 3 Months, can be exported only to a static [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] worksheet.  
  
- For anyone who is not on [!INCLUDE[pn_crm_online_2015_update_1_shortest](../includes/pn-crm-online-2015-update-1-shortest.md)] or [!INCLUDE[pn_crm_2016](../includes/pn-crm-2016.md)] and you are using the [!INCLUDE[pn_Office_365](../includes/pn-office-365.md)][!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] web app, you must save the file, open the file using the [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] desktop application, and then resave the file to the . xlsx format. You can then reopen the [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] document in [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] Online.  
  
- Your operating system region settings (in Windows, **Control Panel** > **Region**) and [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)] region settings (**Settings** (![Settings button on the nav bar](../basics/media/settings-gear-icon.png "Settings button on the nav bar")) > **Options** > **Languages**) should be the same. If not, refreshing dynamic data with **Refresh from CRM** might cause data changes.  
  
## Privacy notice  
[!INCLUDE[cc_privacy_export_to_excel](../includes/cc-privacy-export-to-excel.md)]
  
### See also  
 [Export data to Excel](../basics/export-data-excel.md)   
 [Analyze with Excel Online](../basics/analyze-dynamics-365-data-excel-online.md)  
 [Export to Excel static worksheet](../basics/export-excel-dynamic-worksheet.md)  
 [Edit the default filter of a report](../basics/edit-default-filter-report.md)     
 [Create, edit, or save an Advanced Find search](../basics/save-advanced-find-search.md)  
