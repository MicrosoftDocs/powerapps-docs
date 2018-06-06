---
title: "Preview feature: Use the Organization Insights dashboard to view metrics about your Dynamics 365 (online) instance | MicrosoftDocs"
description: ""
keywords: ""
ms.date: 10/30/2017
ms.service: crm-online
ms.custom: 
ms.topic: article
applies_to:
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
ms.assetid: f8f35728-62c8-4461-a7b8-2945360c1b3a
author: jimholtz
ms.author: jimholtz
manager: brycho
ms.reviewer: 
ms.suite: 
ms.tgt_pltfrm: 
caps.latest.revision: 4
topic-status: Drafting
---

# Preview feature: Use the Organization Insights dashboard to view metrics about your instance

[!INCLUDE[cc-applies-to-update-9-0-0](../../includes/cc_applies_to_update_9_0_0.md)]<br/>[!INCLUDE[cc-applies-to-update-8-2-0](../../includes/cc_applies_to_update_8_2_0.md)]

Use the Organization Insights dashboard to get a quick view of key [!INCLUDE[pn_crm_online_shortest](../../includes/pn-crm-online-shortest.md)] metrics such as the number of active users and page requests.  
  
> [!IMPORTANT]
>  The Organization Insights dashboard is a preview feature in [!INCLUDE[pn_crm_8_1_0_online](../../includes/pn-crm-8-1-0-online.md)]. A preview feature is a feature that is not complete, but is made available before it’s officially in a release so customers can get early access and provide feedback. Preview features aren’t meant for production use and may have limited or restricted functionality.  To use this feature, it must be turned on and the license terms must be accepted. [What are Preview features and how do I enable them?](https://docs.microsoft.com/dynamics365/customer-engagement/admin/what-are-preview-features-how-do-i-enable-them) [!INCLUDE[cc_preview_features_no_MS_support](../../includes/cc-preview-features-no-ms-support.md)]  
>   
>  Consider using the new [Organization Insights solution](use-organization-insights-solution-view-environment-metrics.md) for a richer view of your instance metrics. Organization Insights dashboard will remain a preview feature and will be deprecated once the Organization Insights solution is fully available.  
  
 Note the following:  
  
-   In all charts, you can select a two hour (2H), forty-eight hour (48H) or thirty-day (30D) time period for data to be included in the chart. Data is refreshed as shown in the following table.  
  
    |Lookback period|Data aggregation interval|  
    |---------------------|-------------------------------|  
    |2H|5 minutes|  
    |48H|1 hour|  
    |30D|1 day|  
  
-   Expect a data synchronization delay of approximately 45 minutes or more. For example, at 4:30 PM, a 2 hour (2H) lookback might show data in the chart for 1:45 PM to 3:45 PM.  
  
-   Aggregation intervals use the UTC time standard and not the user-defined time zone.  
  
-   If a chart has multiple elements such as Most Active Users, you can click the chart element to switch its display.  
  
## View the Organization Insights dashboard  
 To view the Organization Insights dashboard, go to any dashboard, click **Select** (![Drop-down button](../media/dropdown-button.png "Drop-down button")) next to the dashboard title, and then click **Organization Insights Dashboard**. The following charts are provided.  
  
<a name="BKMK_ActiveUsers"></a>   

## Active users
 ![Organization Insights Active Users chart](../media/organization-insights-active-users-chart.png "Organization Insights Active Users chart")
  
### What's included in this chart  
  
|Chart element|Description|  
|-------------------|-----------------|  
|Active Users|Total number of active users (unique users) who performed an operation that caused one of these SDK calls: `Retrieve`, `Retrieve Multiple`, `Delete`, `Create`, and `Update`.|  
  
### How to interpret this chart  
 This chart shows the adoption and usage of your [!INCLUDE[pn_crm_shortest](../../includes/pn-crm-shortest.md)] instance based on active users (unique users) with read, write, create, and update actions.  
  
## Most Active Users (Reads)  
 ![Organization Insights Most Active Users (Reads) chart](../media/organization-insights-most-active-users-reads-chart.png "Organization Insights Most Active Users (Reads) chart")  
  
### What's included in this chart  
  
|Chart element|Description|  
|-------------------|-----------------|  
|Reads|List of most active users who performed an operation that caused a `Retrieve` or `Retrieve Multiple` SDK call in your [!INCLUDE[pn_crm_shortest](../../includes/pn-crm-shortest.md)] instance over the selected time period.|  
  
### How to interpret this chart  
 This chart lists the top ten users who performed the most `Read` operations in your [!INCLUDE[pn_crm_shortest](../../includes/pn-crm-shortest.md)] instance.  
  
## Most Active Users (Changes)  
 ![Organization Insights Most Active Users (Changes) chart](../media/organization-insights-most-active-users-changes-chart.png "Organization Insights Most Active Users (Changes) chart")  
  
### What's included in this chart  
  
|Chart element|Description|  
|-------------------|-----------------|  
|Creates|List of most active users who performed an operation that caused a `Create` SDK call in the [!INCLUDE[pn_crm_shortest](../../includes/pn-crm-shortest.md)] instance over the selected time period.|  
|Updates|List of most active users who  performed an operation that caused an `Update` SDK call  in the [!INCLUDE[pn_crm_shortest](../../includes/pn-crm-shortest.md)] instance over the selected time period.|  
|Deletes|List of most active users who  performed an operation that caused a `Delete` SDK call  in the [!INCLUDE[pn_crm_shortest](../../includes/pn-crm-shortest.md)] instance over the selected time period.|  
  
### How to interpret this chart  
 This chart lists the top ten users who  performed the most change  operations (creates, updates, deletes) in your [!INCLUDE[pn_crm_shortest](../../includes/pn-crm-shortest.md)] instance.  
  
<a name="BKMK_SpecificOperations"></a>   
## Active Users Performing Specific Operations  
 ![Organization Insights Specific Operations chart](../media/organization-insights-specific-operations-chart.png "Organization Insights Specific Operations chart")  
  
### What's included in this chart  
  
|Chart element|Description|  
|-------------------|-----------------|  
|Updates|Total number of unique users who performed an operation that caused an `Update` SDK call. Updates for all entities are included.|  
|Creates|Total number of unique users who performed an operation that caused a `Create` SDK call. Creates for all entities are included.|  
|Reads|Total number of unique users who performed an operation that caused a `Retrieve` or `Retrieve Multiple` SDK call. Reads for all entities are included.|  
|Deletes|Total number of unique users who performed an operation that caused a `Delete` SDK call. Deletes for all entities are included.|  
  
### How to interpret this chart  
 This chart shows how many unique users are performing which types of operations (create, update, deletes, reads) in your [!INCLUDE[pn_crm_shortest](../../includes/pn-crm-shortest.md)] instance over the specified time.  
  
<a name="BKMK_TotalOperations"></a>   
## Total Operations  
 ![Organization Insights Total Operations chart](../media/organization-insights-total-operations-chart.png "Organization Insights Total Operations chart")  
  
### What's included in this chart  
  
|Chart element|Description|  
|-------------------|-----------------|  
|Updates|Total number of **Update** SDK calls. Updates for all entities are included.|  
|Creates|Total number of **Create** SDK calls. Creates for all entities are included.|  
|Deletes|Total number of **Delete** SDK calls. Deletes for all entities are included.|  
|Reads|Total number of **Retrieve** and **Retrieve Multiple** SDK calls. Reads for all entities are included.|  
  
### How to interpret this chart  
 This chart shows how many operations (create, update, deletes, reads) have occurred in the [!INCLUDE[pn_crm_shortest](../../includes/pn-crm-shortest.md)] instance over the specified time.  
  
<a name="BKMK_PageRequests"></a>   
## Total Page Requests  
 ![Organization Insights Total Page Requests chart](../media/organization-insights-total-page-requests-chart.png "Organization Insights Total Page Requests chart")  
  
### What's included in this chart  
  
|Chart element|Description|  
|-------------------|-----------------|  
|Forms|Number of requests for form loads.|  
|Dashboards|Number of requests for dashboards.|  
|Reports|Number of requests for reports.|  
  
### How to interpret this chart  
 This chart shows the number of page load requests for forms, dashboards, and reports.    This is a count of requests received by the [!INCLUDE[pn_crm_shortest](../../includes/pn-crm-shortest.md)] server. Pages that are cached while browsing won't be counted.  
  
### See also  
 [Use the Organization Insights solution to view metrics about your instance](use-organization-insights-solution-view-environment-metrics.md)  
 [Developer Guide for Dynamics 365 Customer Engagement](https://docs.microsoft.com/dynamics365/customer-engagement/developer/developer-guide)

