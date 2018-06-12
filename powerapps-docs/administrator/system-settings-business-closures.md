---
title: "System Settings - Business closures| MicrosoftDocs"
ms.custom: ""
ms.date: 09/30/2017
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
ms.assetid: 478b2c16-5827-4e1b-ae93-d3d19c3f6c8d
caps.latest.revision: 15
author: "jimholtz"
ms.author: "jimholtz"
manager: kvivek
---
# System Settings - Business closures

> [!NOTE]
> ![This page is under construction. Check back soon!](media/under_construction.png "Coming soon")  [!INCLUDE[cc-under-construction](../includes/cc-under-construction.md)]

Prevent scheduling resources on holidays and other nonworking days by defining business closures in [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)]. You can set both the days and times that your organization will be closed. 

These settings can be found in the Business Application Platform Admin center by going to **Environments** > [select an environment] > **Settings** > **Business closures**.

Make sure you have the Schedule Manager Security role or equivalent permissions to update the business closures.

**Check your security role**

- Follow the steps in [View your user profile](https://docs.microsoft.com/dynamics365/customer-engagement/basics/view-your-user-profile).
- Don’t have the correct permissions? Contact your system administrator.

|Settings|Description|  
|--------------|-----------------|  
|**Closure name**|The name for the business closure event. The first 12 characters of the name appear on each day of the closure on the calendar view of the affected resource's **Work Hours**.|  
|**Start date**|The date the closure event starts.|  
|**End date**|The date the closure event ends.|  
|**All day event**|Select if the closure event is for the whole day. In the **Duration** box, Dynamics 365 automatically enters the duration of 1 day.|  
|**Start time**|The time the closure event starts. Does not apply to all day events.|  
|**End time**|The time the closure event ends. Does not apply to all day events.|  
|**Duration**|If you want to enter duration instead of an end time, select the length of the closure in the **Duration** box. Dynamics 365 automatically calculates the end time for you.|  
