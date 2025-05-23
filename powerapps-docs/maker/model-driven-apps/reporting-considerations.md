---
title: "Reporting considerations | MicrosoftDocs"
description: Learn about what the considerations are when you use reporting in model-driven apps
ms.custom: 
ms.date: 12/20/2023
ms.reviewer: 
ms.suite: 
ms.tgt_pltfrm: 
ms.topic: concept-article
applies_to: 
  - Dynamics 365 for Customer Engagement (online)
  - PowerApps
ms.assetid: cb1bb002-8300-43bb-ab75-99e7a9c9c35d
caps.latest.revision: 11
author: Mattp123
ms.subservice: mda-maker
ms.author: matp
tags: 
  - MigrationHO
search.audienceType: 
  - customizer
---
# Model-driven app reporting capabilities and considerations



Model-driven apps have many capabilities that allow customers to surface business data that helps them drive decisions and interact with their customers and their data more effectively.  

These are described in the [reporting overview](reporting-overview.md) and include
- [Views](model-driven-app-glossary.md#view).
- [Charts](model-driven-app-glossary.md#chart).
- [Dashboards](model-driven-app-glossary.md#dashboard).
- [SQL Server Reporting Services reports](add-reporting-to-app.md).
- Microsoft Excel integration that allows users to easily build self-service reports using the Power BI features [PowerView](https://support.office.com/article/power-view-overview-and-learning-5380e429-3ee0-4be2-97b7-64d7930020b6), [PowerPivot](https://support.office.com/article/power-pivot-overview-and-learning-f9001958-7901-4caa-ad80-028a6d2432ed), and [PowerQuery](https://support.office.com/article/power-query-overview-and-learning-ed614c81-4b00-4291-bd3a-55d80767f81d).
- [Power BI](model-driven-app-glossary.md#power-bi).
  
As the volume of data held in the app's database continues to grow it becomes more important than ever to think about your BI strategy and determine the most effective mechanisms for reporting and visualizing large datasets.  

## Reporting infrastructure

In an environment, the reporting infrastructure is shared and separate from the database. In this architecture, although customers share the resources required to run the report, each report runs against the customers' individual database instance. 
  
The reporting capabilities built in to Microsoft Dataverse are designed to let users run reports on datasets that span shorter periods of time. Considering this, note the following fixed settings:  
  
- Reports and queries can execute for up to five minutes. When the maximum period is reached, the report will time out and a message is returned to the user. Within the five-minute duration, reports and queries are allowed to span large datasets that are beyond 50,000 rows, which provide significant flexibility to satisfy most operational reporting needs. 
  
- To improve query response, we recommend that detailed reports minimize the display of large numbers of rows. To do this, apply suitable filtering to reduce the number of rows that are returned. When you create aggregated or summarized reports, queries should push the aggregation to the query rather than fetch detailed rows to perform aggregation in the report. More information: [Aggregate data using FetchXml](../../developer/data-platform/fetchxml/aggregate-data.md) and [report prefiltering](/dynamics365/customerengagement/on-premises/analytics/improve-report-performance-by-using-filters).

- The Report Viewer page is subject to the platform [API limits](../../developer/data-platform/api-limits.md). Multiple executions of a long-running report might result in an error, and the user can wait few minutes and try again. This is a per user limit and shouldn't affect the normal usage of reports by multiple users.
  
- For charts and grids displayed in dashboards, your apps allow users to run queries that have a dataset that has fewer than 50,000 rows. Should a user run a dashboard query that spans a dataset of 50,000 or more rows, the message "The maximum row limit is exceeded. Reduce the number of rows" is returned.  The dataset practical setting helps to ensure optimal performance of the app. 
  
<a name="BKMK_ReportTips"></a>

## Tips and solutions for reporting

 Typically, for most organizations' reporting needs, these settings are adequate. To make sure that your users don't exceed these settings and to improve report querying performance in general, consider the following best practices.  
  
- When creating custom reports or dashboards, design them to query smaller datasets over shorter periods of time by adding a time-based filter in the report, such as the current month or quarter, to limit the results.  
  
- Limit the number of tables that are needed to return the result. This helps reduce the time required to run the query and return the result set.  
  
- Reduce the rows in detailed reports. Suitable filtering can be used to reduce the number of rows returned by the query to reduce timeouts.  
  
- For aggregated or summarized reports, queries must be used to push the aggregation to the database and not fetch detailed rows and perform aggregation in the SQL Server Reporting Services report.  
  
- When appropriate for your business, users should run the default (out-of-the-box) reports and dashboards. These reports and dashboards are typically designed to query per user datasets, so in most cases won't exceed the dataset limit.  
  
If users must run reports that exceed these settings, we recommend that you review the following options for assistance with complex reporting needs. Both options effectively offload reporting workloads from Dataverse to another datastore by using a data integration solution.  
  
- [Adapters](reporting-considerations.md#BKMK_ThirdPartyAdapt) are used in conjunction with SQL Server Integration Services (SSIS) to extend the capabilities for integration with your apps data.  
  
- Extract transform load [(ETL) tools](reporting-considerations.md#BKMK_ETL) provide a new tool set for creating analysis of data by combining multiple data sources or extracting data to the data warehouse solution if SSIS isn't in use. ETL tools provide comprehensive solutions for connecting with Dataverse to move data.  
  
> [!IMPORTANT]
>  When you use these tools, we recommend that moving or synchronizing data takes place during nonbusiness hours.  
  
 If needed, there are many Microsoft partners who can help provide a solution for your specific reporting needs, such as creating an offline copy of the data specifically used for running large reports.  These partners are knowledgeable with the data integration tools available. More information: [Find a Dynamics 365 partner](https://dynamics.microsoft.com/partners/find-a-partner/)  
  
<a name="BKMK_ThirdPartyAdapt"></a>
## Third-party adapters for SSIS  
  
-   [CozyRoc SSIS+ component for Dynamics 365/CRM](https://www.cozyroc.com/ssis/dynamics-crm)  
  
-   [KingswaySoft SSIS Integration Toolkit for Dynamics 365](https://www.kingswaysoft.com/products/ssis-integration-toolkit-for-microsoft-dynamics-365)  
  
-   [CData SSIS components for Dynamics 365](https://www.cdata.com/ssis/components/)  
  
-   [Team4 SSIS Connector for Dynamics 365](https://www.team4.de/microsoft-dynamics-365-crm/)  
  
<!--    [PragmaticWorks TaskFactory SSIS Source/Destination for Dynamics CRM](https://pragmaticworks.com/Products/Task-Factory/Features/DynamicsCRMSource.aspx)  -->
  
<a name="BKMK_ETL"></a>   
## ETL tools  
  
-   [TIBCO Dynamics 365 integration](https://www.tibco.com/solutions/microsoft-dynamics-365-integration)  <br />
  
<!--   [Productivity tools from Informatica](https://community.informatica.com/community/search.jspa?peopleEnabled=true&userID=&containerType=14&container=2002&spotlight=true&resultTypes=solution&q=dynamics+CRM)  -->
  
### See also  
 [Report Authoring Extension (with SQL Server Data Tools support)](https://www.microsoft.com/download/details.aspx?id=45013) <br />
  
 [Introduction to Microsoft Power Query for Excel](https://office.microsoft.com/en-ca/excel-help/introduction-to-microsoft-power-query-for-excel-HA104003940.aspx?CTT=5&origin=HA104003813)   <br />
 [Dynamics 365 for Customer Engagement OData Feeds and Power Query: What's the &#91;Record&#93;?](https://community.dynamics.com/crm/b/survivingcrm/archive/2014/02/16/dynamics-crm-odata-feeds-and-power-query-what-s-the-record.aspx)   <br />
 



[!INCLUDE[footer-include](../../includes/footer-banner.md)]
