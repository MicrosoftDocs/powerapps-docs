---
title: "Types of calendars (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" #TODO: NoOwner
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Types of calendars

The calendar table was modified to support additional types of calendars in Microsoft Dataverse.  
  
The `Type` choice column contains the following options:  
  
|Value|Label|Description|  
|-----------|-----------|-----------------|  
|0|Default|All calendars that are not customer service, holiday schedule, or inner calendars.|  
|1|Customer Service|Service calendars for customer service.|  
|2|Holiday Schedule|Holiday schedule calendars for customer service.|  
|-1|Inner Calendar type|Inner Calendars are used by other calendars to build a graph of time slots available for customer service or service scheduling to be performed.|  
  
## Customer service calendars  
 Customer service calendars exist to calculate performance against service level agreements (SLAs). SLAs are frequently based on key performance indicators (KPIs) based on time, such as duration for first response or a time limit before escalation. When these time limits are restricted to periods when customer service operations are open, calculations to enforce these agreements must include data from the customer service calendar.  
  
 Customer service calendars define regular weekly schedules. Events that don’t fall into those regular schedules are usually holidays. A customer service calendar can be associated with a holiday schedule to provide a complete description of the times when customer services are available.  
  
## Service scheduling calendars  
 Service scheduling uses the default calendar type. Business closure calendars can be defined and shared on service and resource entities. The scheduling engine makes sure that all appropriate calendar rules are considered for an appointment request.  
  
 In addition to free/busy times, you can define effort (required/available) constraints on the `CalendarRule` entity. These constraints are defined as the effort that is available from a resource to perform, deliver, or repeat a particular service at a given time. Similarly, each service defines the effort that is required from the required pool of resources to complete one unit of service for its specified duration. The scheduling engine automatically computes the appropriate time blocks for an appointment when the total effort that is required for a given service is less than or equal to the total available effort for all the required resources.  
  
### See also  
 [Calendar table](reference/entities/calendar.md)<br/>   
 <xref:Microsoft.Dynamics.CRM.calendarrule>

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
