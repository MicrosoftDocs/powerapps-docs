---
title: "Customize and organize reports (Dynamics 365 Customer Engagement) | MicrosoftDocs"
ms.custom: ""
ms.date: 06/20/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
ms.assetid: ea98ae5e-5dbc-4c23-b4c6-513774997226
caps.latest.revision: 47
author: "Mattp123"
ms.author: "matp"
manager: "kvivek"
---
# Customize and organize reports

Analyze data by using reports. Common Data Service for Apps includes default reports for many common business needs. However, most organizations customize the default reports and add custom reports for specific needs.  
  
<a name="ownership"></a>   
## Report ownership  
 System reports are available to all app users. App users who own reports can share them with specific colleagues or teams, or can make the reports available to the organization, so that all users can use them.  
  
<a name="types"></a>   
## Report types  
 Common Data Service for Apps supports two types of reports:  
  
- **Fetch-based Reporting Services reports.** These reports use FetchXML queries that are proprietary to Common Data Service for Apps instead of filtered views to retrieve data for reports. Reports that you create by using the Report Wizard in Common Data Service for Apps are Fetch-based reports. 

- - **SQL Server Reporting Services reports. (Dynamics 365 on-premises only)** These reports use SQL queries and filtered views to retrieve report data. Filtered views restrict the data to what is available to the security role of the person running the report. All the default reports included with PowerApps are SQL-based reports.  
  
     You cannot access filtered views in Common Data Service for Apps because access to the SQL database is not supported with Common Data Service for Apps. Use Fetch-based reports for custom reporting.  
  
  
The other reports can be:  
  
-   Links to webpages  
  
-   Static files  
  
-   Dynamic Office Excel files that read data from the Common Data Service for Apps database  
 
 
 For each report, you can edit the following properties:  
  
-   File name or URL  
  
-   Display name  
  
-   Description  
  
-   Information about where the report displays in the user interface  
  
<a name="security"></a>   
## Security of data in reports  
 All reports read Common Data Service for Apps data from filtered views that filter the data based on the user's security role. Reports only display data that the person running the report has permission to view.  
  
<a name="creating"></a>   
## Options for creating new reports  
 To create a new report, users with appropriate permissions can:  
  
-   Add a file or a link to a webpage as a report.  
  
-   Run the Report Wizard to create a new Reporting Services report. The Report Wizard can create table and chart reports, including drill-through reports and top N reports.  
  
-   Write a new Fetch-based Reporting Services report. To write custom fetch-based reports, you must install the Dynamics 365 Report Authoring Extension. More information: [Create a new report using SQL Server Data Tools](https://docs.microsoft.com/dynamics365/customer-engagement/analytics/create-a-new-report-using-sql-server-data-tools)  
  
<a name="modifying"></a>   
## Options for modifying existing reports  
 For existing reports, users with appropriate permissions can:  
  
-   Organize reports into categories to control which views in the reports area display for each report.  
  
-   Determine where a report is visible in the user interface, and edit other report properties.  
  
-   Edit a report created with the Report Wizard.  
  
-   Edit a default report. For example, if you customize Common Data Service for Apps entity assets, you might need to modify labels or add or remove fields in default reports. More information: [Report writing environment using SQL Server Data Tools](https://docs.microsoft.com/dynamics365/customer-engagement/analytics/report-writing-environment-using-sql-server-data-tools)  
  
-   Edit the default filter for a default report, a report created with the Report Wizard, or other Reporting Services reports.  
  
-   Create a one-time snapshot for a Reporting Services report or schedule a Reporting Services report to run at set intervals. Note that the Report Scheduling feature is currently only available with on-premises versions of Dynamics 365 customer engagement.  
  
-   Share a personal report with other users, or make it available to everyone in your organization.  
  
-   Publish a report so that it is available for use with external applications, such as SharePoint or custom programs.  
  
<a name="solutions"></a>   
## Reports in solutions  
 In Common Data Service for Apps, reports are solution aware. Adding a report as a component to a solution makes it become a single unit of software that extends Common Data Service for Apps functionality and the user interface. Only reports that are organization owned or visible to the organization can be added to solutions.  
  
> [!NOTE]
>  To find if a report is viewable to the organization: In the list of reports, select a report, and then click or tap **Edit**. On the **Administration** tab, see if **Viewable By** is set to **Organization**.  
  
 You can add, import, or export snapshots of reports as part of a solution. In Common Data Service for Apps, reports, sub reports, report category, report display area, and report-related record type are considered as components of a report set. When you import a solution update in non-overwrite mode, any updates by the solution to a report will be ignored if any component of the report set has been customized.  
  
## Next steps  
 [Create or edit a report using the Report Wizard](https://docs.microsoft.com/dynamics365/customer-engagement/basics/create-edit-copy-report-wizard)   <br/>

 [Introduction to reporting and analytics with Dynamics 365](https://docs.microsoft.com/dynamics365/customer-engagement/analytics/reporting-analytics-with-dynamics-365)
