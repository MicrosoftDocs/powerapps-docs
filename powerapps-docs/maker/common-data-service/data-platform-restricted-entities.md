---
title: Restricted entities | Microsoft Docs
description: Understanding restricted entities in the Common Data Service for Apps
documentationcenter: na
author: clwesene
manager: kfile
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: conceptual
ms.component: cds
ms.date: 3/21/2018
ms.author: clwesene

---
# Premium entities restricted to Dynamics 365 licenses

PowerApps is licensed on a per-user basis, each user who accesses the service to create and run apps needs a license. The Common Data Service for Apps allows users to use entities from the Common Data Model and Dynamics 365 products to build apps using PowerApps and Flow. Specific entities which are closely tied to the Dynamics 365 products require users of those apps, who need to perform create, update, or delete actions on data stored within theese entities to be licenced for the respective Dynamics 365 product and cannot be used with a standard PowerApps or Flow plan. Apps or Flows which only read data from these entities can still be used with the appropriate PowerApps plan. Please see the [PowerApps pricing page](https://powerapps.microsoft.com/pricing) for more information on available plans.

## Restricted entities for create, update and delete operations

The following entities require end users of Apps and Flows which perform create, update or delete operations against data stored within them. 


Entity | Logical name | Licence required
--- | --- | ---
Journey | journey | Dynamics 365 for Marketing <br> **or** Dynamics 365, Enterprise edition, Plan 1 <br>**or** Dynamics 365, Enterprise edition, Plan 2
Goal | goal | Dynamics 365 for Sales Professional, <br>**or** Dynamics 365 for Sales, Enterprise edition, <br>**or** Dynamics 365, Enterprise edition, Plan 1 <br>**or** Dynamics 365, Enterprise edition, Plan 2
Incident | incident | Dynamics 365 for Customer Service, Enterprise edition <br>**or** Dynamics 365, Enterprise edition, Plan 1 <br>**or** Dynamics 365, Enterprise edition, Plan 2
Knowledge article | knowledgearticle | Dynamics 365 for Customer Service, Enterprise edition <br>**or** Dynamics 365, Enterprise edition, Plan 1 <br>**or** Dynamics 365, Enterprise edition, Plan 2
SLA | sla | Dynamics 365 for Customer Service, Enterprise edition <br>**or** Dynamics 365, Enterprise edition, Plan 1 <br>**or** Dynamics 365, Enterprise edition, Plan 2
Entitlement | entitlement | Dynamics 365 for Customer Service, Enterprise edition <br>**or** Dynamics 365, Enterprise edition, Plan 1 <br>**or** Dynamics 365, Enterprise edition, Plan 2
Routing rule | routingrule | Dynamics 365 for Customer Service, Enterprise edition <br>**or** Dynamics 365, Enterprise edition, Plan 1 <br>**or** Dynamics 365, Enterprise edition, Plan 2


## Licensing

Please the [Licensing overview](../../administrator/pricing-billing-skus.md) page for more information on PowerApps and Dynamics 365 licences.

