---
title: License requirements for entities| Microsoft Docs
description: An explanation of license requirements for entities with complex business logic and restricted entities in Common Data Service.
author: MicroSri
ms.service: powerapps
ms.topic: conceptual
ms.date: 08/28/2020
ms.author: sriknair
ms.reviewer: kvivek
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# License requirements for entities

App makers can use most of the entities available within Common Data Service (including custom entities and entities that are part of the Common Data Model) to create apps and flows for users who have a Power Apps or Power Automate license. 

In some cases, entities contain complex business logic or are tied to customer engagement apps in Dynamics 365 (Dynamics 365 Sales, Customer Service, Field Service, Marketing, or Project Service Automation) that require app users to have a specific license. This topic provides licensing information for entities with complex business logic and entities that are tied to Dynamics 365 apps (termed as restricted entities).

## Entities with complex business logic
Entities that include the following complex server-side logic require users of an app or flow that uses these entities to have a [Power Apps](https://powerapps.microsoft.com/pricing/) or [Power Automate](https://flow.microsoft.com/pricing/) license:

- Code plug-ins (for more information, see [Plug-in development](/powerapps/developer/common-data-service/plug-ins))
- Real-time workflows (for more information, see [Workflow processes](/flow/workflow-processes))

    > [!NOTE]
    >  Only workflows that are converted to a real-time workflow are considered real-time and synchronous. Workflows that are run in the background can still be used with the appropriate Power Apps plan and do not require additional licenses.

To know whether or not you added complex business logic to your entities, review the list of plug-in assemblies and workflows configured in your environment. For the list of entities which may contain server side logic after installing a Dynamics 365 app (such as Dynamics 365 Sales or Dynamics 365 Customer Service), see [Complex entities requiring Power Apps or Power Automate licenses](data-platform-complex-entities.md)  

### Impacting license requirements when adding complex business logic

App makers can add code plug-ins and real-time workflows to entities within Common Data Service, but doing so could change the license requirements for users of apps already deployed. App makers should be cautious when adding complex business logic to an entity and should first check which apps use the entity and whether users of those apps have the appropriate licenses.

## Restricted entities

Restricted entities are not standard entities within Common Data Service, but are included in one of the customer engagement apps in Dynamics 365 (Dynamics 365 Sales, Customer Service, Field Service, Marketing, or Project Service Automation) or a third-party solution. For example, the knowledge article, goal, and entitlement entities.

> [!NOTE]
> Apps and flows that use these entities require the app and flow user to be licensed appropriately-not the maker or developer of the app or flow.

Entities that are tied to the functionality of Dynamics 365 apps (such as Dynamics 365 Sales or Dynamics 365 Customer Service) require app users to have the corresponding license for that application if they want to create, update, or delete records within the entities. For a full list of restricted entities, see [Restricted entities requiring Dynamics 365 licenses](data-platform-restricted-entities.md).

## Licensing examples
Barb and Isaac are creating apps in Power Apps using Common Data Service to store their data.

### Entity creation

-	No user can create a new restricted entity; Microsoft reserves the right to create and define them for Dynamics 365 apps (such as Dynamics 365 Sales or Dynamics 365 Customer Service)

-	Users can create custom entities with Dynamics 365, Power Apps, or Power Automate license

-	For existing restricted entities, a user can add rows with the appropriate Dynamics 365 app license

### Create apps using Power Apps

-	Barb and Isaac can create a canvas or model-driven app accessing restricted entities with a Dynamics 365 license

-	Barb and Isaac can create a canvas or model driven app accessing custom entities with either Dynamics 365 or Power Apps license

### Use apps

Barb wants to use two canvas apps:
-	App 1 &ndash; uses the Appointment entity along with a custom entity that stores related information

-	App 2 &ndash; uses the Appointment entity along with the Work Order entity, which is a restricted entity

Isaac wants to use two model-driven apps:
-	App 3 &ndash; uses the Appointment entity along with a custom entity that stores related information

-	App 4 &ndash; uses the Appointment entity along with the Work Order entity, which is a restricted entity

Barb and Isaac need the following licenses:
- Barb can use App 1 with a Dynamics 365 app license or a Power Apps license.

-	Barb can use App 2 only with a Dynamics 365 app license because there is a restricted entity accessed by the app.

-	Isaac can use App 3 with a Dynamics 365 app license or a Power Apps license. 

-	Isaac can use App 4 only with a Dynamics 365 app license because there is a restricted entity accessed by the app.

### Create flows using Power Automate

Now, let's see what happens when Isaac adds a real-time workflow to the custom entity that both Barb and Isaac are using in their apps.
-	Isaac can create a workflow accessing restricted entities with a Dynamics 365 app license

-	Barb and Isaac can create a workflow accessing custom entities with either Dynamics 365 app or Power Automate license 

### Use flows
-	Barb or Isaac can run the workflow accessing restricted entities with a Dynamics 365 app license

-	Barb or Isaac can run the workflow accessing custom entities with either Dynamics 365 app or Power Automate license


## More about licensing

For more information about licensing, see [Licensing overview](/power-platform/admin/pricing-billing-skus).

For the latest information on licensing requirements for entities, see the [Power Apps licensing guide](https://go.microsoft.com/fwlink/p/?linkid=2085130).
