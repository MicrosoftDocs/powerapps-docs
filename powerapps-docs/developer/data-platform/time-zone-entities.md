---
title: "Time zone entities (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "The time zone entities contain time zone information, such as supported time zone, time zone code, localized time zone, storing information on how times are calculated." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/27/2020
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Time zone entities

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

> [!NOTE]
> The *time zone rule* entity is deprecated. The time conversion calculation is now provided by Microsoft Windows. Refer to this article for more information: [Microsoft policy in response to daylight saving time and time zone changes](https://support.microsoft.com/help/22803/daylight-saving-time).

The *time zone* entities can be used when you write code that works in multiple time zones. The following two read-only entities in Microsoft Dataverse contain time zone information:  
  
- The *time zone definition entity* stores basic information about each supported time zone, including the time zone code and the standard time zone name.
  
- The *time zone localized name* entity stores the localized time zone names.  
  
The following table lists the messages that are related to time zones, but don’t refer to a specific entity.  
  
|Message|Description|  
|-------------|-----------------|  
|<xref:Microsoft.Crm.Sdk.Messages.GetTimeZoneCodeByLocalizedNameRequest>|Retrieves all the time zone definitions for the specified locale, returning only the display name attribute.|  
|<xref:Microsoft.Crm.Sdk.Messages.LocalTimeFromUtcTimeRequest>|Retrieves the local time for the specified UTC time.|  
|<xref:Microsoft.Crm.Sdk.Messages.UtcTimeFromLocalTimeRequest>|Retrieves the UTC time for the specified local time.|  
  
### See also  
 [Business Management Entities](/dynamics365/customer-engagement/developer/business-management-entities)   
 [Sample: Retrieve Time Zone Information](org-service/samples/retrieve-time-zone-information.md)   
 [timezonedefinition EntityType](reference/entities/timezonedefinition.md)   
 [timezonelocalizedname EntityType](reference/entities/timezonelocalizedname.md)   
 [timezonerule EntityType](reference/entities/timezonerule.md)   
 [Transaction Currency (Currency) Entity](transaction-currency-currency-entity.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]