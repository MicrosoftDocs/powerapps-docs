---
title: "Clear the server-side cache for a portal in Dynamics 365 for Customer Engagement | MicrosoftDocs"
description: "Instructions to force the portal to refresh its cache immediately."
author: sbmjais
manager: shujoshi
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 07/15/2019
ms.author: shjais
ms.reviewer:
---

# Clear the server-side cache for a portal

As a portal administrator, you can clear the server-side cache for the entire portal so that updated data from [!INCLUDE[pn-dynamics-crm](../includes/pn-dynamics-crm.md)] is immediately reflected on the portal. Updates from [!INCLUDE[pn-dynamics-crm](../includes/pn-dynamics-crm.md)] are communicated to the portal in asynchronous mode, so there might be a lag between the time data is updated in [!INCLUDE[pn-dynamics-crm](../includes/pn-dynamics-crm.md)] and the time that updated data appears on the portal. To eliminate this delay&mdash;for example, when it interferes with portal configuration&mdash;you can force the portal to refresh its cache immediately.

> [!NOTE]
> The SLA for cache refresh (data transfer between [!INCLUDE[pn-dynamics-crm](../includes/pn-dynamics-crm.md)] and portal) is 15 minutes.

To clear the server-side cache

1.	Sign in to the portal as an administrator.

2.	Navigate to the URL as follows: `<portal_path>/_services/about`

3.	Select **Clear Cache**. 

The server-side cache is deleted, and data is reloaded from [!INCLUDE[pn-dynamics-crm](../includes/pn-dynamics-crm.md)]. Note that clearing the portal server-side cache will temporararily cause poor portal performance while data is being reloaded from [!INCLUDE[pn-dynamics-crm](../includes/pn-dynamics-crm.md)].
        
![Clear the portal cache](media/clear-portal-cache.png "Clear the portal cache")
