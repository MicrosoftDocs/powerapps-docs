---
title: "Calendar entities (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Read how you can store data for customer service calendars and holiday schedules using calendar entities." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "JimDaly" #TODO: NoOwner
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Calendar entities

The calendar entity stores data for customer service calendars and holiday schedules in addition to business. Each calendar is set for a specific time zone.  
  
 A calendar describes the availability of a service or a resource. Calendars are related to `calendarrule` records, which include details about the duration, start and end times, and recurring patterns of events included in the calendar.  
  
 There are two types of calendar rules in Common Data Service for Apps:  
  
- **Root**: A calendar rule that contains an inner calendar or that has nested (leaf) rules. You can specify an inner calendar for a root calendar rule by using the `CalendarRule.InnerCalendarId` attribute. The attribute value of `CalendarRule.InnerCalendarId` of a root rule is the same as the attribute value of `CalendarRule.CalendarId` of its leaf rules.  
  
- **Leaf**: A calendar rule that doesn’t contain an inner calendar, and therefore, is the end of the "branch."  
  
 Calendar rules are ordered, or ranked, to describe their precedence, and rules can overlap. The nested rules expansion defines the time span, or extent, of a rule. You can use the `CalendarRule.ExtentCode` attribute to define how rule expansion overlap is handled, for example, whether both time span or extent of a rule are shown or if only one is included. These features provide for recurrence patterns, for example, different shift schedules for winter and summer months in a single service calendar.  
  
 A calendar can be a complex tree of rules and nested calendars that represent a high-level abstraction of the work schedule. The calendar entity supports the <xref:Microsoft.Crm.Sdk.Messages.ExpandCalendarRequest> message to convert to a simple view, which is an array of time blocks that determine availability over specific ranges.  
  
## In This Section  
 [Types of Calendars](types-calendars.md)  
  
 [Calendar Entity](/reference/entities/calendar.md)  
  
## Related Sections  
 [Appointment Entities](/dynamics365/customer-engagement/developer/appointment-entities)  
  
 [Recurring Appointment Entities](/dynamics365/customer-engagement/developer/recurring-appointment-entities)  
  
 [Resource Entities](/dynamics365/customer-engagement/developer/resource-entities)  
  
 [Service Entity](/dynamics365/customer-engagement/developer/service-entity)  
  
 [Sample Code for Schedule and Appointment Entities](/dynamics365/customer-engagement/developer/sample-code-schedule-appointment-entities)