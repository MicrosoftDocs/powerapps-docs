---
title: Premium entities | Microsoft Docs
description: Understanding licence requirements for Premium entities
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
# Understanding Premium entities

PowerApps is licensed on a per-user basis, each user who accesses the service to create and run apps needs a license. The Common Data Service for Apps allows users to use entities from the Common Data Model and Dynamics 365 products to build apps using PowerApps and Flow. In some cases entities which have complex logic or are closely tied to the Dynamics 365 products require users of those apps, who need to perform create, update, or delete actions on data stored within these entities to require specific licences. Apps or Flows which only read data from these entities can still be used with the appropriate PowerApps plan. Please see the [PowerApps pricing page](https://powerapps.microsoft.com/pricing) for more information on available plans.

Apps and Flows using Premium entities require the user who is consuming the app or Flow to be licenced appropriately and not the maker or developer of the app or flow.

## Premium entities with complex business logic

Entities which include advanced server-side logic require users or players of the app or flow, who need to perform create, update or delete operations to have a PowerApps Plan 2. Entities which have the following logic will require a PowerApps Plan 2:

- Code Plug-ins : See [Plug-in development](https://msdn.microsoft.com/library/gg328490.aspx) for more information.
- Real-time (Syncronous) workflows : See [Workflow processes](https://docs.microsoft.com/dynamics365/customer-engagement/customize/workflow-processes) for more information.

        > [!NOTE]
        >  Only workflows which are **converted to a real-time workflow** are considered real-time and syncronous with regards to Premium licenses. Workflows which are run in the background can still be used with the appropriate PowerApps plan.


Standard entities do not include code plug-ins or syncrouns workflows, however these can be added as a customization to standard and custom entities. When a code plug-in or real-time workflow is added to an entity, makers and developers need to ensure users of apps which included these entities have the correct licenses.

## Premium entities restricted to Dynamics 365 licences

Selected entities which are closely tied to the functionality of the Dynamics 365 products require users to have the corresponding license for that product to perform create, update and delete operations, and cannot be run with PowerApps plans. You can find a full list of entities retricted to Dynamics 365 licences [here](data-platform-premium-entities.md).

## Licensing example



## Licensing

Please the [Licensing overview](../../administrator/pricing-billing-skus.md) page for more information on PowerApps and Dynamics 365 licences.
