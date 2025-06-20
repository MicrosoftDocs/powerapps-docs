---
title: "Time zone tables (Microsoft Dataverse) | Microsoft Docs" 
description: "The time zone tables contain time zone information, such as supported time zone, time zone code, localized time zone, storing information on how times are calculated." 
ms.custom: ""
ms.date: 08/27/2020
ms.reviewer: "pehecke"

ms.topic: "article"
author: "mayadumesh" 
ms.subservice: dataverse-developer
ms.author: "jdaly"
search.audienceType: 
  - developer
---
# Time zone tables

> [!NOTE]
> The *time zone rule* table is deprecated. The time conversion calculation is now provided by Microsoft Windows. Refer to this article for more information: [Microsoft policy in response to daylight saving time and time zone changes](https://support.microsoft.com/help/22803/daylight-saving-time).

The *time zone* tables can be used when you write code that works in multiple time zones. The following two read-only tables in Microsoft Dataverse contain time zone information:  
  
- The *time zone definition table* stores basic information about each supported time zone, including the time zone code and the standard time zone name.
  
- The *time zone localized name* table stores the localized time zone names.  
  
[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

The following table lists the messages that are related to time zones, but don’t refer to a specific table.  
  
|Message|Description|  
|-------------|-----------------|  
|<xref:Microsoft.Crm.Sdk.Messages.GetTimeZoneCodeByLocalizedNameRequest>|Retrieves all the time zone definitions for the specified locale, returning only the display name attribute.|  
|<xref:Microsoft.Crm.Sdk.Messages.LocalTimeFromUtcTimeRequest>|Retrieves the local time for the specified UTC time.|  
|<xref:Microsoft.Crm.Sdk.Messages.UtcTimeFromLocalTimeRequest>|Retrieves the UTC time for the specified local time.|  
  
### See also  
 [Sample: Retrieve Time Zone Information](org-service/samples/retrieve-time-zone-information.md)   
 [timezonedefinition EntityType](reference/entities/timezonedefinition.md)   
 [timezonelocalizedname EntityType](reference/entities/timezonelocalizedname.md)   
 [timezonerule EntityType](reference/entities/timezonerule.md)   
 [Transaction Currency (Currency) Entity](transaction-currency-currency-entity.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
