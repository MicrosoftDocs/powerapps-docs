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
ms.date: 5/1/2018
ms.author: clwesene

---
# Understanding Restricted entities


Most of the entities available within the Common Data Service for Apps can be used to build PowerApps and Flows, and only require the user to have a PowerApps Plan 1. Some entities with complex business logic added to the entity require users of the app to have a PowerApps Plan 2 (For more information see [Premium entities](data-platform-premium-entities.md)). While all entities can be to used to read data in apps with these licenses, a small set of entities require users to have a corresponding license for the Dynamics 365 product if they need to create, update or delete records, these are referred to as Restricted entities.

Entities may be restricted to a Dynamics 365 license for the following reasons:

- **Configuration data** : if the entity is used to store and maintain product specific configuration that is typically not used outside of the application.
- **Supported by advanced logic** : if the entity is accompanied by advanced logic to create and maintain data in a specific way when being used in a Dynamics 365 product.

Users of Canvas and Model Driven apps will only require a corresponding Dynamics 365 license if they need to create, update or delete data within these entities in their app. If their app or flow only reads information from the entity, they only require the appropriate PowerApps or Flow license.

   > [!NOTE]
   > Apps or Flows which only read data from these entities can still be used with the appropriate PowerApps or Flow plan.

## Restricted entities for create, update and delete operations

The following entities require end users of Apps and Flows which perform create, update or delete operations against data stored within them. 


Entity | Logical name | License required
--- | --- | ---
Actual |msdyn_actual |Dynamics 365 for Field Service <br> **or** Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Agreement Business Process |msdyn_bpf_baa0a411a239410cb8bded8b5fdd88e3 |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Booking journal | msdyn_bookingjournal|Dynamics 365 for Field Service<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Booking Setup Metadata | msdyn_bookingsetupmetadata|Dynamics 365 for Field Service <br> **or** Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Booking timestamp | msdyn_bookingtimestamp|Dynamics 365 for Field Service<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Case to Work Order Business Process |msdyn_bpf_989e9b1857e24af18787d5143b67523b |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Configuration |msdyn_configuration |Dynamics 365 for Field Service <br> **or** Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Entitlement | entitlement | Dynamics 365 for Customer Service, Enterprise edition <br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Estimate Line|msdyn_estimateline|Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Estimate|msdyn_estimate |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Fact|msdyn_fact |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Field service setting |msdyn_fieldservicesetting |Dynamics 365 for Field Service<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Field Service System Job |msdyn_fieldservicesystemjob |Dynamics 365 for Field Service<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Goal | goal | Dynamics 365 for Sales Professional, <br>**or** Dynamics 365 for Sales, Enterprise edition, <br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Incident | incident | Dynamics 365 for Customer Service, Enterprise edition <br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Inventory Journal |msdyn_inventoryjournal |Dynamics 365 for Field Service<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Invoice Process |msdyn_bpf_d8f9dc7f099f44db9d641dd81fbd470d |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Journey | journey | Dynamics 365 for Marketing <br> **or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Knowledge article | knowledgearticle | Dynamics 365 for Customer Service, Enterprise edition <br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Organizational Unit |msdyn_organizationalunit |Dynamics 365 for Field Service <br> **or** Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Product Inventory |msdyn_productinventory |Dynamics 365 for Field Service<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Project Parameter|msdyn_projectparameter |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Project Stages| msdyn_bpf_665e73aa18c247d886bfc50499c73b82|Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Project Task Dependency|msdyn_projecttaskdependency |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Project Task|msdyn_projecttask |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Project Team Member|msdyn_projecteam |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Purchase Order Business Process | msdyn_bpf_2c5fe86acc8b414b8322ae571000c799|Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Resource Assignment Detail (Deprecated)|msdyn_resourceassignmentdetail |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Resource Assignment|msdyn_resourceassignment |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Resource Restriction (Deprecated) |msdyn_workorderresourcerestriction | Dynamics 365 for Field Service<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Routing rule set | routingrule | Dynamics 365 for Customer Service, Enterprise edition <br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Schedule Board Setting |msdyn_scheduleboardsetting |Dynamics 365 for Field Service <br> **or** Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Scheduling Parameter |msdyn_schedulingparameter |Dynamics 365 for Field Service <br> **or** Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Work Order Business Process |msdyn_bpf_d3d97bac8c294105840e99e37a9d1c39 |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan







## Licensing

Please the [Licensing overview](../../administrator/pricing-billing-skus.md) page for more information on PowerApps and Dynamics 365 licenses.

