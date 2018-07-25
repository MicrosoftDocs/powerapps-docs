---
title: License requirements for entities| Microsoft Docs
description: An explanation of license requirements for entities within Common Data Service (CDS) for Apps.
author: clwesene
manager: kfile
ms.service: powerapps
ms.component: cds
ms.topic: conceptual
ms.date: 07/25/2018
ms.author: clwesene
---

# License requirements for entities
App makers can use most of the entities available within Common Data Service (CDS) for Apps (including custom entities and entities that are part of the Common Data Model) to create apps and flows for users who have a PowerApps Plan 1 or Microsoft Flow Plan 1 license. In some cases, entities contain complex business logic or are tied to Dynamics 365 applications that require app users to have a specific license. 


|Entity  |Description  |Requirement  |
|---------|---------|---------|
|Entities with complex business logic  | These are entities that use complex server-side business logic. For example, any entity that uses a real-time workflow or code plug-in.     | [PowerApps Plan 2](https://powerapps.microsoft.com/pricing/) or [Flow Plan 2](https://flow.microsoft.com/pricing/)  | 
|Restricted entities    | These are entities that are not standard with Common Data Service for Apps but are included in a Dynamics 365 customer engagement application or third-party solution. For example, the knowledge article, goal, and entitlement entities.    | [A Dynamics 365 plan](https://dynamics.microsoft.com/pricing/)    |


> [!NOTE]
> Apps and flows that use these entities require the app and flow user to be licensed appropriately-not the maker or developer of the app or flow.

## Entities with complex business logic
Entities that include the following complex server-side logic require users of an app or flow that uses these entities to have a PowerApps Plan 2 or Microsoft Flow Plan 2 license:

* Code plug-ins (for more information, see [Plug-in development](https://docs.microsoft.com/dynamics365/customer-engagement/developer/plugin-development))
* Real-time workflows (for more information, see [Workflow processes](https://docs.microsoft.com/dynamics365/customer-engagement/customize/workflow-processes))

    > [!NOTE]
    >  Only workflows that are converted to a real-time workflow are considered real-time and synchronous. Workflows that are run in the background can still be used with the appropriate PowerApps plan and do not require additional licenses.

To know whether or not you added complex business logic to your entities, review the list of plug-in assemblies and workflows configured in your environment. For the list of entities which may contain server side logic after installing a Dynamics 365 application, see [Complex entities requiring PowerApps Plan 2 licenses](data-platform-complex-entities.md) 

### Impacting license requirements when adding complex business logic
App makers can add code plug-ins and real-time workflows to entities within CDS for Apps, but doing so could change the license requirements for users of apps already deployed. App makers should be cautious when adding complex business logic to an entity and should first check which apps use the entity and whether users of those apps have the appropriate licenses.

## Restricted entities
Certain entities that are tied to the functionality of Dynamics 365 applications require app users to have the corresponding license for that application if they want to create, update, or delete records within the entities. For a full list of restricted entities, see [Restricted entities requiring Dynamics 365 licenses](data-platform-restricted-entities.md).

## Licensing examples
Barb and Isaac are creating apps in PowerApps using CDS for Apps to store their data.

Barb is creating two canvas apps:

* App 1 &ndash; uses the Contact entity along with a custom entity that stores related information
* App 2 &ndash; uses the Contact entity along with the Incident entity, which is a restricted entity

Isaac is creating two model-driven apps:

* App 3 &ndash; uses the Contact entity along with a custom entity that stores related information
* App 4 &ndash; uses the Contact entity along with the Incident entity, which is a restricted entity

Barb and Isaac need the following licenses:
* Barb needs a PowerApps Plan 1 license to create canvas apps using CDS for Apps. If she needs to create a database or create a custom entity, she would need a PowerApps Plan 2 license.

* Isaac needs a PowerApps Plan 2 license to build model- driven apps.

App users need the following licenses:
* App 1 users only need a PowerApps Plan 1 or Plan 2 license, since the app doesn't contain any entities with complex business logic or restricted entities.

* App 2 users need a Dynamics 365 for Customer Service, Enterprise edition license (or a Dynamics 365 or Dynamics 365 Customer Engagement plan), since the app includes a restricted entity.

* App 3 users need a PowerApps Plan 2 license, since it's a model-driven app.

* App 4 users need a Dynamics 365 for Customer Service, Enterprise edition license (or a Dynamics 365 or Dynamics 365 Customer Engagement plan), since the app includes a restricted entity.

    The Dynamics 365 for Customer Service plan includes a PowerApps Plan 2 license, which allows users to run model-driven apps.

Now, let's see what happens when Isaac adds a real-time workflow to the custom entity that both Barb and Isaac are using in their apps.

Barb and Isaac need the following licenses:
* Barb still needs a PowerApps Plan 1 license to create canvas apps using CDS for Apps.

* Isaac still needs a PowerApps Plan 2 license to build model-driven apps.

App users need the following licenses:
* App 1 users now need a PowerApps Plan 2 license, since the app contains an entity with a real-time workflow.

* App 2 users still need a Dynamics 365 for Customer Service, Enterprise edition license (or a Dynamics 365 or Dynamics 365 Customer Engagement plan), since the app includes a restricted entity. 

* App 3 users still need a PowerApps Plan 2 license, since it's a model-driven app.

* App 4 users still need a Dynamics 365 for Customer Service, Enterprise edition license (or a Dynamics 365 or Dynamics 365 Customer Engagement plan), since the app includes a restricted entity.

    The Dynamics 365 for Customer Service plan includes a PowerApps Plan 2 license, which allows users to run model-driven apps.

The only app impacted by this change is App 1, which previously required a PowerApps Plan 1 license, but now requires a PowerApps Plan 2 license, since it contains an entity with complex business logic. 

## More about licensing
For more information about PowerApps and Dynamics 365 licenses, see [Licensing overview](../../administrator/pricing-billing-skus.md).
