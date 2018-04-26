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

PowerApps is licensed on a per-user basis, each user who accesses the service to create and run apps needs a license. The Common Data Service for Apps allows users to use entities from the Common Data Model and Dynamics 365 products to build apps using PowerApps and Flow. In some cases entities which have complex logic or are closely tied to the Dynamics 365 products require users of those apps, who need to perform create, update, or delete actions on data stored within these entities to require specific licenses. Apps or Flows which only read data from these entities can still be used with the appropriate PowerApps plan. Please see the [PowerApps pricing page](https://powerapps.microsoft.com/pricing) for more information on available plans.

Apps and Flows using Premium entities require the user who is using the app or Flow to be licensed appropriately and not the maker or developer of the app or flow.

## Premium entities with complex business logic

Entities which include advanced server-side logic require users of the app or flow, who need to perform create, update or delete operations to have a PowerApps Plan 2. Entities which have the following logic will require a PowerApps Plan 2:

- Code Plug-ins: See [Plug-in development](https://msdn.microsoft.com/library/gg328490.aspx) for more information.
- Real-time (Synchronous) workflows: See [Workflow processes](https://docs.microsoft.com/dynamics365/customer-engagement/customize/workflow-processes) for more information.

    > [!NOTE]
    >  Only workflows which are **converted to a real-time workflow** are considered real-time and synchronous with regards to Premium entities. Workflows which are run in the background can still be used with the appropriate PowerApps plan.


Standard entities do not include code plug-ins or synchronous workflows, however these can be added as a customization to standard and custom entities. When a code plug-in or real-time workflow is added to an entity, makers and developers need to ensure users of apps which included these entities have the correct licenses.

## Premium entities restricted to Dynamics 365 licenses

Selected entities which are closely tied to the functionality of the Dynamics 365 products require users to have the corresponding license for that product to perform create, update and delete operations, and cannot be run with PowerApps plans. You can find a full list of entities restricted to Dynamics 365 licenses [here](data-platform-premium-entities.md).

## Licensing example

Let's take a look at this example. Isaac is building a canvas app in PowerApps, using the Common Data Service for Apps to store the data for his app. Isaac also uses Dynamics 365 Enterprise Edition, and is using an environment with entities from both the Common Data Model, and his Dynamics 365 apps.

Isaac is going to build three Canvas apps;

- App 1 : uses the Contact entity, along with a custom entity used to store related information.
- App 2 : uses the Contact entity, along with a custom entity which Isaac has added a real-time workflow to.
- App 3 : uses the Contact entity, along with the Incident entity (which is a restricted entity)

Here's the types of licenses Isaac and his users are going to need :

- Issac needs a PowerApps Plan 2 license, to build apps against the Common Data Service for Apps.
- Users of App 1: need a PowerApps Plan 1 or Plan 2 license, as it doesn't contain any premium entities.
- Users of App 2: need a PowerApps Plan 2 license, as it includes a Premium entity with complex business logic.
- Users of App 3: need a Dynamics 365 for Customer Service, Enterprise Edition (or Dynamics 365, Enterprise Edition, Plan 1 or 2), as it includes a restricted entity. 

## Licensing

Please the [Licensing overview](../../administrator/pricing-billing-skus.md) page for more information on PowerApps and Dynamics 365 licenses.
