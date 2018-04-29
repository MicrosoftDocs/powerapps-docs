---
title: Premium entities | Microsoft Docs
description: Understanding license requirements for Premium entities
documentationcenter: na
author: clwesene
manager: kfile
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: conceptual
ms.component: cds
ms.date: 5/1/2018
ms.author: clwesene

---
# Understanding Premium entities

PowerApps and Flow users can use the Common Data Service for Apps to develop apps or flows against their data, in most cases users of Apps and Flows which connect to the Common Data Service for Apps only require a PowerApps Plan 1. In some cases, entities which have complex logic or are closely tied to the Dynamics 365 products require users of those apps to have a specific license. 

PowerApps Plan 1 allows users to run apps and flows which use entities from the Common Data Service for Apps, including custom entities and entities which are part of the Common Data Model. Please see the [PowerApps pricing page](https://powerapps.microsoft.com/pricing) for more information on available plans.

> [!NOTE]
> Apps and Flows using Premium entities require the user who is using the app or Flow to be licensed appropriately and not the maker or developer of the app or flow.

## Premium entities with complex business logic

Entities which include complex server-side logic require users of the app or flow to have a PowerApps Plan 2. Entities which have the following logic will require a PowerApps Plan 2 for all users of those Apps or Flow:

- Code Plug-ins: See [Plug-in development](https://msdn.microsoft.com/library/gg328490.aspx) for more information.
- Real-time workflows: See [Workflow processes](https://docs.microsoft.com/dynamics365/customer-engagement/customize/workflow-processes) for more information.

    > [!NOTE]
    >  Only workflows which are **converted to a real-time workflow** are considered real-time and synchronous with regards to Premium entities. Workflows which are run in the background can still be used with the appropriate PowerApps plan and do not require additional licenses.

Currently you need to manually check if you have added complex business logic to your entities by reviewing the list of Plug-in assemblies and workflows which have been configured in your environment.

## Impacting license requirements when adding complex business logic

Code plug-ins and Real-time workflows can be added to entities within the Common Data Service for Apps, by doing so you can change the licenses required by users of apps already deployed. Users should take care when adding complex business logic to entities by first checking which apps consume the entity and if your users have the appropriate licenses.

> [!NOTE]
> Adding a code plug-in or real-time workflow to an entity can impact the licenses required by users of apps and flows which already consume that entity.

## Premium entities restricted to Dynamics 365 licenses

Selected entities which are closely tied to the functionality of the Dynamics 365 products require users to have the corresponding license for that product to perform create, update and delete operations, and cannot be run with PowerApps plans. You can find a full list of entities restricted to Dynamics 365 licenses [here](data-platform-restricted-entities.md).

## Licensing example

Let's take a look at this example. Barb and Isaac are building apps in PowerApps, using the Common Data Service for Apps to store their data.

Barb is going to build two Canvas apps;

- App 1 : uses the Contact entity, along with a custom entity used to store related information.
- App 2 : uses the Contact entity, along with the Incident entity (which is a restricted entity)

Isaac is going to build two Model driven apps;

- App 3 : uses the Contact entity, along with a custom entity used to store related information.
- App 4 : uses the Contact entity, along with the Incident entity (which is a restricted entity)


Here are the types of licenses Barb, Isaac and their users are going to need:

- Barb needs a PowerApps Plan 1 license, to build a canvas app using the Common Data Service for Apps.
    - Barb can build an app against the Common Data Service with a PowerApps Plan 1, if she needed to create a database or create a custom entity, she would require a PowerApps Plan 2 license.
- Isaac needs a PowerApps Plan 2 license, to build model driven apps.
- Users of App 1: need a PowerApps Plan 1 or Plan 2 license, as it doesn't contain any premium entities.
- Users of App 2: need a Dynamics 365 for Customer Service, Enterprise Edition license (or Dynamics 365 Plan, Dynamics 365 Customer Engagement Plan), as it includes a restricted entity. 
- Users of App 3: need a PowerApps Plan 2 license, at it is a Model driven app.
- Users of App 4: need a Dynamics 365 for Customer Service, Enterprise Edition license (or Dynamics 365 Plan, Dynamics 365 Customer Engagement Plan), as it includes a restricted entity. 
    - Dynamics 365 for Customer Service includes a PowerApps Plan 2 license which allows users to run the Model driven app.

Now, let's see what would happen if Isaac added a real-time workflow to the custom entity that both Barb and Isaac are using in their apps.

Here are the types of licenses Barb, Isaac and their users are going to need :

- Barb still needs a PowerApps Plan 1 license, to build a canvas app using the Common Data Service for Apps.
- Isaac still needs a PowerApps Plan 2 license, to build model driven apps.
- **Users of App 1: now need a PowerApps Plan 2, as the app contains an entity with a real-time workflow.**
- Users of App 2: still need a Dynamics 365 for Customer Service, Enterprise Edition license (or Dynamics 365 Plan, Dynamics 365 Customer Engagement Plan), as it includes a restricted entity. 
- Users of App 3: still need a PowerApps Plan 2 license, at it is a Model driven app.
- Users of App 4: still need a Dynamics 365 for Customer Service, Enterprise Edition license (or Dynamics 365 Plan, Dynamics 365 Customer Engagement Plan), as it includes a restricted entity. 
    - Dynamics 365 for Customer Service includes a PowerApps Plan 2 license which allows users to run the Model driven app.

The only app impacted by this change was App 1, which previously required a PowerApps Plan 1, and now requires a PowerApps Plan 2 as it contains a premium entity. 

## Licensing

Please the [Licensing overview](../../administrator/pricing-billing-skus.md) page for more information on PowerApps and Dynamics 365 licenses.
