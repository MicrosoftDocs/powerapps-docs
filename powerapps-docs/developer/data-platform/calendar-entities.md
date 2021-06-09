---
title: "Calendar tables (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Read how you can store data for customer service calendars and holiday schedules using calendar tables." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 05/04/2021
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
# Calendar tables

The calendar table stores data for customer service calendars and holiday schedules in addition to business. Each calendar is set for a specific time zone. 

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]
  
A calendar describes the availability of a service or a resource. Calendars are related to `calendarrule` rows, which include details about the duration, start and end times, and recurring patterns of events included in the calendar.  
  
 There are two types of calendar rules in Microsoft Dataverse:  
  
- **Root**: A calendar rule that contains an inner calendar or that has nested (leaf) rules. You can specify an inner calendar for a root calendar rule by using the `CalendarRule.InnerCalendarId` column. The column value of `CalendarRule.InnerCalendarId` of a root rule is the same as the column value of `CalendarRule.CalendarId` of its leaf rules.  
  
- **Leaf**: A calendar rule that doesn’t contain an inner calendar, and therefore, is the end of the "branch."  
  
 Calendar rules are ordered, or ranked, to describe their precedence, and rules can overlap. The nested rules expansion defines the time span, or extent, of a rule. You can use the `CalendarRule.ExtentCode` attribute to define how rule expansion overlap is handled, for example, whether both time span or extent of a rule are shown or if only one is included. These features provide for recurrence patterns, for example, different shift schedules for winter and summer months in a single service calendar.  
  
 A calendar can be a complex tree of rules and nested calendars that represent a high-level abstraction of the work schedule. The calendar table supports the <xref:Microsoft.Crm.Sdk.Messages.ExpandCalendarRequest> message to convert to a simple view, which is an array of time blocks that determine availability over specific ranges.  
  
### See also  
 [Types of calendars](types-calendars.md)  
  
 [Calendar table](/reference/entities/calendar.md)  



[!INCLUDE[footer-include](../../includes/footer-banner.md)]
