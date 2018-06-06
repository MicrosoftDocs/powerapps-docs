---
title: "Use the Organization Insights solution to view metrics about your Dynamics 365 (online) instance | MicrosoftDocs"
ms.custom: ""
ms.date: 5/30/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
ms.assetid: 5e6f6b85-1a25-4c56-a92f-59f0a289e9c6
caps.latest.revision: 5
author: "jimholtz"
ms.author: "jimholtz"
manager: "kvivek"
---
# Use the Organization Insights solution to view metrics about your instance 

[!INCLUDE[cc-applies-to-update-9-0-0](../../includes/cc_applies_to_update_9_0_0.md)]<br/>[!INCLUDE[cc-applies-to-update-8-2-0](../../includes/cc_applies_to_update_8_2_0.md)]

Organization Insights for [!INCLUDE[pn_dyn_365_online](../../includes/pn-crm-online.md)] provides important adoption and use metrics for your [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] organization, and tools to help you stay ahead of performance and support issues.  
  
> [!IMPORTANT]
>  To comply with the [General Data Protection Regulation](https://www.microsoft.com/en-us/TrustCenter/Privacy/gdpr/default.aspx) (GDPR), we are changing the time the Organization Insights solution will retain data from 90 days to 30 days.
>
>  Check your version of the Organization Insights solution. In [!INCLUDE[pn_dyn_365_online](../../includes/pn-crm-online.md)], go to **Settings** > **Solutions**, and determine the version of OrganizationInsightsSolution.  
>   
>  Organization Insights solution version 1.3.1.0 is the officially supported version. If you have installed version 1.3.0.2, please upgrade to the latest version from [AppSource](https://appsource.microsoft.com/product/dynamics-365/mscrm.04931187-431c-415d-8777-f7f482ba8095?tab=Overview).
>   
>  If you have installed version 1.0.0.0, this is a preview feature in [!INCLUDE[pn_crm_8_2_0_online](../../includes/pn-crm-8-2-0-online.md)]. You can download the latest version from [AppSource](https://appsource.microsoft.com/product/dynamics-365/mscrm.04931187-431c-415d-8777-f7f482ba8095?tab=Overview). A preview feature is a feature that is not complete, but is made available before it’s officially in a release so customers can get early access and provide feedback. Preview features aren’t meant for production use and may have limited or restricted functionality.  
>   
>  To provide feedback for this feature, use the Feedback button. ![Organizations Insights Feedback button](../media/organizations-insights-feedback-button.png "Organizations Insights Feedback button")  
>   
> [!INCLUDE[cc_preview_features_no_MS_support](../../includes/cc-preview-features-no-ms-support.md)]  
  
 **Key highlights**  
  
- **Available as a solution**: Organization Insights is available as a preferred solution from [AppSource](https://appsource.microsoft.com/product/dynamics-365/mscrm.04931187-431c-415d-8777-f7f482ba8095?tab=Overview) and is compatible with [!INCLUDE[pn_crm_8_1_1_online_subsequent](../../includes/pn-crm-8-1-1-online-subsequent.md)] (8.1.1) or later.  
  
- **Customizable dashboards**: Set up your organization’s dashboard to provide a rich user experience and snapshots of your organization’s most important data.  
  
- **Monitor adoption and use**: Identify your most active users, the number and types of operations they’re performing, number of pages requests, most-used entities, workflows, plug-ins, and more, over a period of time as you work toward your adoption goals.  
  
- **Manage storage and performance**: Monitor storage quotas, storage use, and top tables by size to optimize performance.  
  
- **Troubleshoot effectively**: Drill down into the details of your top failing workflows and API calls to quickly diagnose and troubleshoot errors.
  
- **OData support**: Expose Organization Insights entities through OData for extension by independent software vendors.  
  
- **Original Organization Insights dashboard**: You can also view metrics using the Organization Insights dashboard released with [!INCLUDE[pn_crm_8_1_0_online](../../includes/pn-crm-8-1-0-online.md)]. <!-- See [Preview feature: Use the Organization Insights dashboard to view metrics about your instance](../admin/use-organization-insights-dashboard-view-instance-metrics.md).--> See [Preview feature: Use the Organization Insights dashboard to view metrics about your instance](https://technet.microsoft.com/library/mt703628.aspx). This dashboard does not have all the metrics available with the solution version.  
  
> [!TIP]
> ![Video symbol](../media/video-thumbnail-4.png "Video symbol") Check out the following video: [Monitor your Dynamics 365 (online) instance with Organization Insights](https://go.microsoft.com/fwlink/p/?linkid=835917).  
  
<a name="BKMK_InstallSolution"></a>   

## Install and view the Organization Insights solution  
 The new Organization Insights is a preferred solution that you can install from the Dynamics Marketplace.  
  
> [!NOTE]
>  If you are using a trial version of [!INCLUDE[pn_crm_online_shortest](../../includes/pn-crm-online-shortest.md)], you can install the new Organization Insights from [AppSource](https://appsource.microsoft.com/marketplace?page=1&product=dynamics-crm).  
  
1.  In [!INCLUDE[pn_crm_shortest](../../includes/pn-crm-shortest.md)], from the main menu, click **Settings** > **Dynamics Marketplace**.  
  
2.  In the search box, type "organization insights".  
  
3.  When you see the **Organization Insights** app, click **Try**, and then **Continue**.  
  
4.  In the **Add the application to Dynamics 365** dialog box, choose your organization.  
  
5.  Proceed through the terms of service and click **Agree**.  
  
6.  To verify that the solution is installed, go to **Settings** > **Solutions**. You will see Organization Insights in the list of solutions.  
  
    > [!NOTE]
    >  While the solution is installing, the status of the solution changes to "Installation pending". When it's installed and ready to use, the status will change to "Installed".  
  
7.  To view the new Organization Insights dashboard, go to **Settings** > **Organization Insights**.  
  
<a name="BKMK_Home"></a>   

## Home (default)  
 ![Organization Insights Home Section](../media/organization-insights-home-section.png "Organization Insights Home Section")  
  
### About this dashboard  
 This is the default dashboard that provides information on the number of active [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] users, storage usage, the most active workflows, and more.  
  
### What's included in this dashboard  
  
|Chart element|Description|  
|-------------------|-----------------|  
|Total Active Users|Total number of active users (unique users) who performed an operation that caused one of these SDK calls: `Retrieve`, `Retrieve Multiple`, `Delete`, `Create`, and `Update`.|  
|Total API Calls|Total number of API calls that were made by the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] instance for the selected time period.|  
|API Success Rate|This chart shows the API success rate as percentage of total API calls that were made in the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] instance over the specified time.|  
|Plug-in Executions|This chart shows how many plug-ins have been executed in the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] instance over the specified time.|  
|Total Operations|This chart shows how many operations (create, update, deletes, reads) have occurred in the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] instance over the specified time.|  
|Most Active Users Performing Operations|List of most active users who performed an operation that caused a `Create`, `Update`, `Read`, or `Delete` SDK call in the [!INCLUDE[pn_crm_shortest](../../includes/pn-crm-shortest.md)] instance over the selected time period.|  
|Top Plug-ins by Failures|This chart shows top 10 most failing plug-in in the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] instance over the specified time.|  
  
<a name="BKMK_ActiveUsage"></a>   

## Active Usage  
 ![Organization Insights Active Usage Section](../media/organization-insights-active-usage-section.png "Organization Insights Active Usage Section")  
  
### About this dashboard  
 Use this dashboard to find out how many [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] users there are, how many licenses are in use, what custom entities are used most frequently, and more.  
  
### What's included in this dashboard  
  
|Chart element|Description|ChartID|  
|-------------------|-----------------|-----------------|  
|Total Active Users|Total number of active users (unique users) who performed an operation that caused one of these SDK calls: `Retrieve`, `Retrieve Multiple`, `Delete`, `Create`, and `Update`.|4555801D-0EAF-4100-891C-DB34400AB102|  
|Most Used  Entities|Ten Entities which had the most `Retrieve`, `Retrieve Multiple`, `Delete`, `Create`, and `Update SDK Calls`.|F6F2B9FD-FCA8-427A-9A0D-CAC619A3EE74|  
|Total Page Requests|The number of page load requests for forms, dashboards, and reports. This is the count of requests received by the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] server. Pages that are cached while browsing won't be counted.|D0401D82-6E7F-4B84-8D86-825D72C68EE6|  
|Total Operations|This chart shows how many operations (create, update, deletes, reads) have occurred in the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] instance for the selected time period.|B13D7ED8-06BE-4B0E-B314-A16A84099F1E|  
|Active Users Performing Specific Operations|Total number of active users (unique users) over time who performed an operation that caused one of these SDK calls: `Retrieve`, `Retrieve Multiple`, `Delete`, `Create`, and `Update`.|35699BD6-6E49-463D-9DC0-4E968750778F|  
|Active Users|Number of active users (unique users) in your instance who performed an operation that caused one of these SDK calls: `Retrieve`, `Retrieve Multiple`, `Delete`, `Create`, and `Update` over time.|9725801D-0EAF-4100-891C-DB34400AB102|  
|Most Active Users Performing Operations|List of  most active users (unique users) over time who performed an operation that caused one of these SDK calls: `Retrieve`, `Retrieve Multiple`, `Delete`, `Create`, and `Update`.|B173E5EC-195E-4803-B79A-2B1C2704BCB7|  
|Most Used Custom Entities|List of custom entities which had the most `Retrieve`, `Retrieve Multiple`, `Delete`, `Create`, and `Update SDK Calls`.|5FD1EF3F-64C4-429C-83BC-95F0AD44B761|  
|Most Used OOB Entities|List of out-of-box entities which had the most `Retrieve`, `Retrieve Multiple`, `Delete`, `Create`, and `Update SDK Calls`.|46A47AF1-325D-4A00-9F7E-6059D5AAB722|  
|Usage Active Users by OS|The number of active users by operating system.|F37D4DEC-28E2-438A-977F-DD3F96203559|
|Active Users by Device Type|The number of active users by device type.|43771A31-6350-489C-AABD-F7EBB93320C4|
|Active Users by Browser|The number of active users by browser.|1259D071-A06D-4B3F-8D32-DCD39670F6FD|
|Active Users by Security Roles|The number of active users by security roles.|09062EF4-4195-4256-B84B-68E9CA3C737D|
|Users by Business Unit|The number of active users by business unit.|8B701B71-092E-4FCF-A9E3-A005EE865921|
|Number of Creates by Entity|How many create operations are performed by the selected user in the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] instance for the selected time period.|3AC63F0D-4661-4F19-9B31-DB5616187A88|
|Number of Updates by Entity|How many update operations are performed on different entities by the selected user in the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] instance for the selected time period.|C215FC98-BF5D-4AAB-BB0A-24E9F2A4F939|
|Number of Reads by Entity|How many read operations are performed on different entities by the selected user in the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] instance for the selected time period.|3DE3E899-4BCF-482B-8896-657D0C8FCAE7|
|Number of Deletes by Entity|How many delete operations are performed on different entities by the selected user in the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] instance for the selected time period.|8F92215B-C55D-451F-A546-48E1456E7056|
|Total Operations Over Time|The total operations performed by the selected user in the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] instance over the selected time period.|9AD78421-6D33-4463-8C17-B9C4DF52592D|
|Total Operations by Entity|The total operations performed on different entities by the selected user in the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] instance for the selected time period.|045F5B81-CF47-4819-A4F9-AE366565C591|
|Active Users by Entities|Show the active users distributed over different entities (refreshed hourly)|2C569F70-7FA8-4C2E-AFCE-E6126ED2CC52|
|Active Users by Client|The active users distributed by client type (refreshed hourly)|4D6F71A8-1710-4B0B-9D7A-9590BECE611C|
|Active Users Using More than One Client|The number of active users using more than one client, distributed over different client combinations (refreshed hourly)|149EFCC8-D336-4F51-A293-E173728EC587|
  
> [!NOTE]
> **Retrieve** and **RetrieveMultiple** SDK calls are reported as **Reads**.  
  
### Update frequency  
 Active usage chart data is updated as follows.  
  
|Chart|Update frequency|  
|-----------|----------------------|  
|Total Active Users|1 hour|  
|Most Used Entities|1 hour|  
|Most Active Users (Reads)|1 hour|  
|Total API Calls|1 hour|  
|Total Page Requests|1 hour|  
|Most Active Users (Changes)|1 hour|  
|Total Operations|1 hour|  
|Active Users Performing Specific Operations|1 hour|  
|Active Users|1 hour|  
|Most Active Users Performing Operations|1 hour|  
|Most Used Custom Entities|1 hour|  
|Most Used OOB Entities|1 hour|  
  
<a name="BKMK_SystemJobs"></a>   

## System Jobs  
 ![Organization Insights System Jobs Section](../media/organization-insights-system-jobs-section.png "Organization Insights System Jobs Section")  
  
### About this dashboard  
 Use this dashboard to monitor and troubleshoot workflows.  
  
### What's included in this dashboard  
  
|Chart element|Description|ChartID|  
|-------------------|-----------------|-----------------|  
|Workflow Executions|This chart shows how many workflows have been executed in the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] instance over the specified time.|3555801D-0EAF-4100-891C-DB34400AB102|  
|System Jobs Pass Rate|This chart shows the system job’s pass rate as percentage of system jobs that were executed in the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] instance over the specified time.|1355801D-0EAF-4100-891C-DB34400AB102|  
|System Jobs Throughput/Minute|This chart shows the average system jobs that have been executed per hour in the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] instance over the specified time.|090F51C1-7DBA-42BA-B031-FB1C0999EE28|  
|Executions and Backlog|This chart shows the number of executions and the backlog for system jobs in the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] instance over the specified time.|9D941442-759D-4C29-8348-ADCA2810A602|  
|Most Active Workflows|This chart shows top 10 most executed workflows in the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] instance over the specified time.|7128FF54-B377-4236-ACFF-EEDF696461AA|  
|Top Workflows by Failures|This chart shows top 10 most failing workflows in the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] instance over the specified time. Click on a workflow to see the failures and their number of occurrences.|7A7C0FEE-A7BB-4C14-AF2A-76AC00350F82|  
  
### Update frequency  
 System jobs chart data is updated as follows.  
  
|Chart|Update frequency|  
|-----------|----------------------|  
|Workflow Executions|1 hour|  
|System Jobs Pass Rate|1 hour|  
|System Jobs Throughput / Hour|1 hour|  
|Most Active Workflows|1 hour|  
|System Jobs Executions and Backlog|1 hour|  
|Top Workflows by Failures|1 hour|  
  
<a name="BKMK_Plugins"></a>   

## Plug-ins  
 ![Organization Insights Plugins Section](../media/organization-insights-plugins-section.png "Organization Insights Plugins Section")  
  
### About this dashboard  
 Use this dashboard to monitor and troubleshoot plug-ins.  
  
### What's included in this dashboard  
  
|Chart element|Description|ChartID|  
|-------------------|-----------------|-----------------|  
|Plug-in Success Rate|This chart shows the plug-in pass rate as percentage of total plug-in executions that were executed in the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] instance over the specified time.|190F51C1-7DBA-42BA-B031-FB1C0999EE28|  
|Plug-in Executions|This chart shows how many plug-ins have been executed in the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] instance over the specified time.|D48FF5C9-BFC9-4E1C-9215-E76FDBFF282E|  
|Average Plug-in Execution Time|This chart shows average time taken to successfully execute a plug-in in the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] instance over the specified time.|A4094693-8638-44B5-83B1-B7EC8C8BFFF6|  
|Most Active Plug-ins|This chart shows top 10 most executed plug-ins in the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] instance over the specified time.|E505BCFC-5B13-4190-842C-E47622BF0A40|  
|Top Plug-ins by Failures|This chart shows top 10 most failing plug-ins in the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] instance over the specified time.|1193CFAC-E8CF-48E9-9A22-A56AAFC1159C|  
  
### Update frequency  
 Plug-ins chart data is updated as follows.  
  
|Chart|Update frequency|  
|-----------|----------------------|  
|Plug-in Success Rate|1 hour|  
|Most Active Plug-ins|1 hour|  
|Plug-in Executions|1 hour|  
|Average Plug-in Execution Time|1 hour|  
|Top Plug-ins by Failures|1 hour|  
  
<a name="BKMK_Storage"></a>   

## Storage  
 ![Organization Insights Storage Section](../media/organization-insights-storage-section.png "Organization Insights Storage Section")  
  
### About this dashboard  
 This dashboard provides a look at storage used by your tenant and instances.
  
### What's included in this dashboard  
  
|Chart element|Description|ChartID|  
|-------------------|-----------------|-----------------|  
|[!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] Tenant Storage Utilization|This chart shows the storage used by all the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] instances of your tenant out of the total storage allocated to the tenant.|1C7B6699-9C07-478C-9C17-AF0D17160734|  
|Storage by [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] Instances (MB)|This chart shows the breakdown of the storage used by the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] instances of your tenant.|66BF5239-56EB-4979-AC92-177D98C5077B|  
|Top Tables by Size - Current [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] Instance|This chart shows top 10 largest tables by size and their row count in the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] instance database.|D37D16D2-C616-4F00-9E56-19E6AE218613|
|Top Tables by Row Count - Current [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] Instance|This chart shows top 10 largest tables by their row count in the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] instance database.|BE23542E-2E03-42A5-BDF4-70A53DFCB519|  
|Common Tables by Size - Current [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] Instance|This chart shows the size of some common tasks of tables in the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] instance database.|8614E00B-28D8-4C41-92E3-9F27AFD28AE7|
|Row Count of Common Tables - Current [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] Instance|This chart shows the number of rows of some common tasks of tables in the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] instance database.|BE5127CC-1919-4AB4-A582-C5C3B601D456|  
|Storage by Instance|Storage used by each [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] instance (refreshed daily)|5BE3A49A-90EF-43EB-8FFB-FD0FD449F196|
|Storage by Tenant|Storage used by the tenant (refreshed daily)|AEEE328E-8E4F-4E98-B5A5-1509E7A610A4|
  
### Update frequency  
 Storage chart data is updated as follows.  
  
|Chart|Update frequency|  
|-----------|----------------------|  
|[!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] Tenant Storage Utilization|1 day|  
|Storage Used by [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] Instances (MB)|1 day|  
|Top Tables by Size - Current [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] Instance|1 day|  
|Size of Common Tables - Current [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] Instance|1 day|  
  
<a name="BKMK_APICallStats"></a>   

## API Call Statistics  
 ![Organization Insights API Call Statistics Section](../media/organization-insights-api-call-statistics-section.png "Organization Insights API Call Statistics Section")  
  
### About this dashboard  
 Use this dashboard to monitor and troubleshoot API calls.  
  
### What's included in this dashboard  
  
|Chart element|Description|ChartID|  
|-------------------|-----------------|-----------------|   
|API Success Rate|This chart shows the API success rate as percentage of total API calls that were made in the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] instance over the specified time.|5555801D-0EAF-4100-891C-DB34400AB102|  
|Top API by Failures|This chart shows top 10 failing API calls in the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] instance over the specified time.|CCB98704-6E3F-4302-AC96-0A4E286061FA|
|Total API Calls|This chart shows how many API calls have been made in total in the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] instance over the specified time.|9555801D-0EAF-4100-891C-DB34400AB102|  
|Most Used API|This chart shows top 10 most executed API calls in the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] instance database.|C898F79D-D3D0-4894-B2E4-E94AC854007A|  
|API Calls|This chart shows how many API calls have been made over time in the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] instance over the specified time.|4C7B6699-9C07-478C-9C17-AF0D17160734|  
  
### Update frequency  
 API Call Statistics chart data is updated as follows.  
  
|Chart|Update frequency|  
|-----------|----------------------|  
|API Success Rate|1 hour|  
|Top API by Failures|1 hour|  
|Most Used API|1 hour|  
|Total API Calls|1 hour|  
|API Calls|1 hour|  
  
<a name="BKMK_MailboxUsage"></a>   

## Mailbox Usage  
 ![Organization Insights Mailbox Usage Section](../media/organization-insights-mailbox-usage-section.png "Organization Insights Mailbox Usage Section")  
  
### About this dashboard  
 Use this dashboard to monitor email mailbox usage.  
  
### What's included in this dashboard  
  
|Chart element|Description|ChartID|  
|-------------------|-----------------|-----------------|  
|Mailbox Details by GEO|This chart shows mailbox details like:<br /><br /> -   the number of server-side synch configured mailboxes<br />-   the number of server-side synch enabled mailboxes<br />-   the number of server-side synch Appointments, Contacts, and Tasks enabled mailboxes<br />-   the number of server-side synch incoming enabled mailboxes<br />-   the number of server-side synch outgoing enabled mailboxes categorized by the geo location the mailbox is hosted in|F90E2120-58B6-4D8B-B913-ADABE7EA4833|  
|Mailboxes by Server Type|This chart shows the mailbox distribution by server type.|AFBB2C1B-6405-4D6C-8D21-D808F796405A|  
|Active Email Server Profiles by Geo|This chart shows active server-side synch enabled mailboxes distributed over the geo location they are hosted in.|AE33B341-752B-4AC3-98F7-FC11EA8B5DE5|  
|Mailboxes by Exchange Configuration|This chart shows the number of mailboxes categorized by their [!INCLUDE[pn_Exchange](../../includes/pn-exchange.md)] configuration.|1AF79B4C-0F75-403B-973A-573E0FDF775E|  
|Number of Mailbox Configuration Errors|This chart shows the number of mailboxes configuration errors which occurred over the user-selected time frame.|DDFE9E31-41D9-4453-87EE-87A5C6D124F6|  
|Mailbox Usage|This chart shows the number of server-side synch mailboxes over the time range selected by the user.|9E5E51CE-9C47-40E4-9862-B8D17D58E0EC|  
|Number of Outlook Mailboxes|This chart shows the number of [!INCLUDE[pn_Outlook_short](../../includes/pn-outlook-short.md)] mailboxes configured for the organization.|BE94BA93-637E-4DEA-B8C6-50DFE57846B6|  
|Number of Active Email Server Profiles|This chart shows the number of active email server profiles for the time range configured by the user.|522D6D36-FDFE-4CF4-9086-93BAA8628425|  
  
### Update frequency  
 Mailbox Usage chart data is updated as follows.  
  
|Chart|Update frequency|  
|-----------|----------------------|  
|Mailbox Details by Geo|30 minutes average|  
|Active Email Server Profiles by Geo|5 minutes average|  
|Mailboxes by Server Type|5 minutes average|  
|Mailbox Usage|5 minutes average|  
|Number of Mailbox Configuration Errors|30 minutes average|  
|Number of Active Email Server Profiles|5 minutes average|  
|Number of Outlook Mailboxes|15 minutes average|  
|Mailboxes by Exchange Configuration|5 minutes average|  
  
<a name="BKMK_Download"></a>   

## Download  
 ![Organization Insights Download Section](../media/organization-insights-download-section.png "Organization Insights Download Section")  
  
### About this dashboard  
 Use this dashboard to download the data selected for the date range selected as an Excel spreadsheet.  
  
### What's included in this dashboard  
  
|Chart element|Description|  
|-------------------|-----------------|  
|Most Active Users Performing Operations|List of  most active users (unique users) over time who performed an operation that caused one of these SDK calls: `Retrieve`, `Retrieve Multiple`, `Delete`, `Create`, and `Update`.|  
|Most Used Custom Entities|List of custom entities which had the most `Retrieve`, `Retrieve Multiple`, `Delete`, `Create`, and `Update SDK Calls`.|  
|Most Used OOB Entities|List of out-of-box entities which had the most `Retrieve`, `Retrieve Multiple`, `Delete`, `Create`, and `Update SDK Calls`.|  
|Active Users by Device Type|List of active users by device type used to access [!INCLUDE [pn-dyn-365](../../includes/pn-dyn-365.md)] (refreshed hourly)|
|Active Users by Business Unit|List of active users by their business unit (refreshed hourly)|
|Active Users by Security Role|List of active users by their security roles (refreshed hourly)|
|Active Users by Client|List of active users, by client type used to access [!INCLUDE [pn-dyn-365](../../includes/pn-dyn-365.md)] (refreshed hourly)|
|Active Users by Entities|List of active users distributed by entity (refreshed hourly)|
  
### Update frequency  
 Download chart data is updated as follows.  
  
|Chart|Update frequency|  
|-----------|----------------------|  
|Most Active Users Performing Operations|1 hour|  
|Most Used Custom Entities|1 hour|  
|Most Used OOB Entities|1 hour|  
  
<a name="BKMK_CustomizeDashboard"></a>   

## Customize your Organization Insights dashboard  
 You can easily customize Organization Insights dashboards to meet your information requirements.  Look for these buttons in the upper-right corner of the [!INCLUDE[pn_dyn_365](../../includes/pn-dyn-365.md)] screen.  
  
|Control|Description|  
|-------------|-----------------|  
|Edit<br /><br /> ![Organizations Insights Edit button](../media/organizations-insights-edit-button.png "Organizations Insights Edit button")|Click to edit the dashboard. Once in edit mode, you can add, remove, resize, and reposition charts in the Home dashboard.<br /><br /> In other dashboards, you can reposition and resize charts. You cannot add or remove charts.|  
|Save<br /><br /> ![Organizations Insights Save button](../media/organizations-insights-save-button.png "Organizations Insights Save button")|Click **Save** to record all your dashboard changes.|  
|Add<br /><br /> ![Organizations Insights Add button](../media/organizations-insights-add-button.png "Organizations Insights Add button")|Click for a list of charts you can add to the dashboard. You cannot add multiple copies of the same chart in the Home dashboard.|  
|Chart menu<br /><br /> ![Add an Organization Insights chart](../media/organization-insights-add-chart-menu.png "Add an Organization Insights chart")|Charts you can add to a dashboard.|  
|Close<br /><br /> ![Organizations Insights Close button](../media/organizations-insights-close-button.png "Organizations Insights Close button")|Click to close the Chart menu.|  
|Feedback<br /><br /> ![Organizations Insights Feedback button](../media/organizations-insights-feedback-button.png "Organizations Insights Feedback button")|We want your feedback! Click **Feedback** to let us know how we're doing.|  
|More options<br /><br /> ![Organizations Insights More button](../media/organizations-insights-more-button.png "Organizations Insights More button")|Click **More options** > **Reset to default dashboard**  to revert all your dashboard changes.  This will reset all changes you've made to any dashboard to default values.|  
|Remove and Resize<br /><br /> ![Organization Insights Custom Controls](../media/organization-insights-custom-controls.png "Organization Insights Custom Controls")|When you click **Edit**, you can remove, resize, and move charts in the Home dashboard. In other dashboards, you can resize and move the charts but not remove them.|  
|Export<br /><br /> ![Organization Insights Export Data to Excel](../media/organization-insights-export-dataexcel.PNG "Organization Insights Export Data to Excel")|Click to export chart data to Excel. Not all charts can be exported.|  
  
<a name="BKMK_GrantAccess"></a>   

## Granting access to the Organization Insights dashboard  
 By default, the dashboard is  available to System Administrator and System Customizer security roles. Access can be granted to other security roles, by providing **Read** privilege to **Saved Organization Insights Configuration**.  
  
1.  Click **Settings** > **Security** > **Security Roles**.  
  
2.  Select a security role, and then click the **Core Records** tab.  
  
3.  Scroll down to **Saved Organization Insights Configuration** and click the **Read** privilege.  
  
4.  Click **Save and Close**.  
  
 ![Grant Read privilege to Salesperson security role](../media/organization-insights-grant-read-privilege-sales-person-security-role.png "Grant Read privilege to Salesperson security role")  
  
 To let other users make modifications to their dashboard layout, grant **Create**, **Read**, **Write**, and **Delete** privileges for the **OrgInsights User Dashboard Definition** custom entity.  
  
1.  Click **Settings** > **Security** > **Security Roles**.  
  
2.  Select a security role, and then click the **Custom Entities** tab.  
  
3.  For **OrgInsights User Dashboard Definition**, and click the **Create**, **Read**, **Write**, and **Delete** privileges .  
  
4.  Click **Save and Close**.  
  
 ![Organization Insights Custom entity](../media/organization-insights-custom-entity.PNG "Organization Insights Custom entity")  
  
<a name="BKMK_ViewData"></a>   

## View data for different time ranges  
 You can adjust the time range for the data presented in the dashboards charts. After selecting the From and To range, click the **Play** button (![Organization Insights Calendar Play button](../media/organization-insights-calendar-play-button.png "Organization Insights Calendar Play button")) to refresh your data.  
  
 ![Select the date range for your data](../media/organization-insights-calendar-control.png "Select the date range for your data")  
  
 Consider the following about the Organization Insights calendar:  
  
-   The Calendar control is not available for the  Storage dashboard and not applicable to any storage related chart as only the latest information is shown for those charts.  
  
-   Default time range is shown for the past 48 hours.  
  
-   Data is only shown for the applied time range.  
  
-   Data is available from the time of release of the solution in AppSource, and will be retained for 30 days.  
  
-   Data is shown for time series at an hourly aggregation interval.  
  
-   The data shown for a hourly aggregation interval represents the whole hour. For example, if the number of active users at 2:00 PM is 5, there were 5 active users between 1:00 and 2:00 PM.  
  
 ![Organization Insights active users chart](../media/organization-insights-active-users-chart.PNG "Organization Insights active users chart") 
 
<a name="BKMK_ODataSupport"></a>   

## OData Support
Organization Insights supports retrieving chart data through the Web API OData v4 web service. For information about the Web API, see [Use the Microsoft Dynamics 365 Web API](https://docs.microsoft.com/dynamics365/customer-engagement/developer/use-microsoft-dynamics-365-web-api).

The entity set name for the `SavedOrgInsightsConfiguration` entity is `savedorginsightsconfigurations` which needs the `SavedOrgInsightsConfigurationId`, `JSONDataStartTime` and `JSONDataEndTime` to return data in the given time range. The data can then be used to render custom charts or do further post-processing as required.

The following is the format by which data can be retrieved, using the ChartID GUID value for the charts listed above.

```  
[ClientUrl]/api/data/v8.1/savedorginsightsconfigurations?$filter=savedorginsightsconfigurationid eq [ChartID] and jsondatastarttime eq [StartTime] and jsondataendtime eq [EndTime]&$select=jsondata
```  

A sample query with GUID and time ranges populated would look something like the following:

```
[ClientUrl]/api/data/v8.1/savedorginsightsconfigurations?$filter=savedorginsightsconfigurationid eq 5187781c-da7c-4762-aeb3-85f908a2777c and jsondatastarttime eq 2017-07-11T18:30:00.000Z and jsondataendtime eq 2017-07-12T18:30:00.000Z&$select=jsondata
```

The following is a sample result for the query:

```
{
  "@odata.context":"https://[ClientUrl]/api/data/v8.1/$metadata#savedorginsightsconfigurations(jsondata)","value":[
    {
      "jsondata":"{\"RequestId\":\"101fa8c3-1221-4f3c-9cf7-1eb35cf2eeba\",\"Results\":[{\"Dates\":[\"7/10/2017 2:00 PM\",\"7/10/2017 3:00 PM\",\"7/10/2017 4:00 PM\",\"7/10/2017 5:00 PM\",\"7/10/2017 6:00 PM\",\"7/10/2017 7:00 PM\",\"7/10/2017 8:00 PM\",\"7/10/2017 9:00 PM\",\"7/10/2017 10:00 PM\",\"7/10/2017 11:00 PM\",\"7/11/2017 12:00 AM\",\"7/11/2017 1:00 AM\",\"7/11/2017 2:00 AM\",\"7/11/2017 3:00 AM\",\"7/11/2017 4:00 AM\",\"7/11/2017 5:00 AM\",\"7/11/2017 6:00 AM\",\"7/11/2017 7:00 AM\",\"7/11/2017 8:00 AM\",\"7/11/2017 9:00 AM\",\"7/11/2017 10:00 AM\",\"7/11/2017 11:00 AM\",\"7/11/2017 12:00 PM\",\"7/11/2017 1:00 PM\",\"7/11/2017 2:00 PM\",\"7/11/2017 3:00 PM\",\"7/11/2017 4:00 PM\",\"7/11/2017 5:00 PM\",\"7/11/2017 6:00 PM\",\"7/11/2017 7:00 PM\",\"7/11/2017 8:00 PM\",\"7/11/2017 9:00 PM\",\"7/11/2017 10:00 PM\",\"7/11/2017 11:00 PM\",\"7/12/2017 12:00 AM\",\"7/12/2017 1:00 AM\",\"7/12/2017 2:00 AM\",\"7/12/2017 3:00 AM\",\"7/12/2017 4:00 AM\",\"7/12/2017 5:00 AM\",\"7/12/2017 6:00 AM\",\"7/12/2017 7:00 AM\",\"7/12/2017 8:00 AM\",\"7/12/2017 9:00 AM\",\"7/12/2017 10:00 AM\",\"7/12/2017 11:00 AM\",\"7/12/2017 12:00 PM\",\"7/12/2017 1:00 PM\"],\"Rollup\":\"PT1H\",\"Metrics\":[{\"Name\":\"activeusers\",\"Values\":[728.0,645.0,531.0,473.0,528.0,542.0,526.0,498.0,461.0,497.0,557.0,578.0,580.0,585.0,569.0,635.0,786.0,819.0,877.0,855.0,783.0,708.0,690.0,678.0,638.0,540.0,452.0,437.0,452.0,492.0,496.0,434.0,452.0,454.0,503.0,545.0,541.0,526.0,520.0,576.0,742.0,840.0,872.0,806.0,753.0,692.0,671.0,0.0]}]}]}","_modifiedby_value":"42d582c5-4091-446c-a9ba-90e7f0a9bb9d","description":"Active Users","lookback":2,"isdefault":true,"isdrilldown":false,"_modifiedonbehalfby_value":"00000000-0000-0000-0000-000000000000","name":"Active Users","metrictype":1,"parameters":"<Parameters><MetricIds><MetricId>C1BCC999-D150-4591-B0A5-0684A6A0F618</MetricId></MetricIds><DisplayOptions><ColorOptions><Colors>['#A83D1E']</Colors></ColorOptions></DisplayOptions></Parameters>","_createdby_value":"42d582c5-4091-446c-a9ba-90e7f0a9bb9d","_createdonbehalfby_value":"00000000-0000-0000-0000-000000000000","plotoption":2,"savedorginsightsconfigurationid":"9725801d-0eaf-4100-891c-db34400ab102"
    }
  ]
}
```

### See also  
 [Preview feature: Use the Organization Insights dashboard to view metrics about your instance](use-organization-insights-dashboard-view-environment-metrics.md) [Developer Guide for Dynamics  365 Customer Engagement](https://docs.microsoft.com/dynamics365/customer-engagement/developer/developer-guide)
