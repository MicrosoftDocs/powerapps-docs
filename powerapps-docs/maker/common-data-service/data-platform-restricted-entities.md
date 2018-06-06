---
title: Restricted entities requiring Dynamics 365 licenses | Microsoft Docs
description: A list of restricted entities in Common Data Service (CDS) for Apps that require Dynamics 365 licenses.
author: clwesene
manager: kfile
ms.service: powerapps
ms.component: cds
ms.topic: reference
ms.date: 05/01/2018
ms.author: clwesene
---

# Restricted entities requiring Dynamics 365 licenses
App makers can use most of the entities available within Common Data Service (CDS) for Apps to create apps and flows for users who have only a PowerApps Plan 1 license. However, some entities contain complex business logic that requires app users to have a PowerApps Plan 2 or Microsoft Flow Plan 2 license (for more information, see [Entity license requirements](data-platform-entity-licenses.md)). An even smaller set of entities tied to Dynamics 365 products requires canvas and model-driven app users to have a license for the corresponding Dynamics 365 product if they need to create, update, or delete records within the entities. These are referred to as *restricted* entities.

Entities may be restricted to a Dynamics 365 license for the following reasons:

* The entity is used to store and maintain product-specific configuration data that is typically not used outside of the application.
* The entity is accompanied by advanced logic that creates and maintains data in a specific way when used within a Dynamics 365 product.

If an app or flow only reads information from an entity, a Dynamics 365 license is not required and an appropriate PowerApps or Microsoft Flow license is all that's needed. 

## Restricted entities for create, update, and delete operations
The following table lists the restricted entities and the associated Dynamics 365 licensing requirements for PowerApps and Microsoft Flow app users who create, update, or delete data stored within the entities. 

|Entity  |Logical name  |License required  |
|---------|---------|---------|
Actual |msdyn_actual |Dynamics 365 for Field Service <br> **or** Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Agreement Business Process |msdyn_bpf_baa0a411a239410cb8bded8b5fdd88e3 |Dynamics 365 for Field Service<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Booking journal | msdyn_bookingjournal|Dynamics 365 for Field Service<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Booking Setup Metadata | msdyn_bookingsetupmetadata|Dynamics 365 for Field Service <br> **or** Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Booking timestamp | msdyn_bookingtimestamp|Dynamics 365 for Field Service<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Case to Work Order Business Process |msdyn_bpf_989e9b1857e24af18787d5143b67523b |Dynamics 365 for Field Service<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Configuration |msdyn_configuration |Dynamics 365 for Field Service <br> **or** Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Entitlement | entitlement | Dynamics 365 for Customer Service, Enterprise edition <br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Estimate Line|msdyn_estimateline|Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Estimate|msdyn_estimate |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Fact|msdyn_fact |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Field service setting |msdyn_fieldservicesetting |Dynamics 365 for Field Service<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Field Service System Job |msdyn_fieldservicesystemjob |Dynamics 365 for Field Service<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Goal | goal | Dynamics 365 for Sales Professional, <br>**or** Dynamics 365 for Sales, Enterprise edition, <br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Incident | incident | Dynamics 365 for Customer Service, Enterprise edition <br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Inventory Journal |msdyn_inventoryjournal |Dynamics 365 for Field Service<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Invoice Process |msdyn_bpf_d8f9dc7f099f44db9d641dd81fbd470d |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Journey | journey | Dynamics 365 for Marketing <br> **or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Knowledge article | knowledgearticle | Dynamics 365 for Customer Service, Enterprise edition <br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Organizational Unit |msdyn_organizationalunit |Dynamics 365 for Field Service <br> **or** Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Product Inventory |msdyn_productinventory |Dynamics 365 for Field Service<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Project Parameter|msdyn_projectparameter |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Project Stages| msdyn_bpf_665e73aa18c247d886bfc50499c73b82|Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Project Task Dependency|msdyn_projecttaskdependency |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Project Task|msdyn_projecttask |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Project Team Member|msdyn_projecteam |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Purchase Order Business Process | msdyn_bpf_2c5fe86acc8b414b8322ae571000c799|Dynamics 365 for Field Service<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Resource Assignment Detail (Deprecated)|msdyn_resourceassignmentdetail |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Resource Assignment|msdyn_resourceassignment |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Resource Restriction (Deprecated) |msdyn_workorderresourcerestriction | Dynamics 365 for Field Service<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Routing rule set | routingrule | Dynamics 365 for Customer Service, Enterprise edition <br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Schedule Board Setting |msdyn_scheduleboardsetting |Dynamics 365 for Field Service <br> **or** Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Scheduling Parameter |msdyn_schedulingparameter |Dynamics 365 for Field Service <br> **or** Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
SLA| sla | Dynamics 365 for Customer Service, Enterprise edition <br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
System User Scheduler Setting |msdyn_systemuserschedulersetting|Dynamics 365 for Field Service <br> **or** Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Transaction Connection|msdyn_transactionconnection |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Transaction Origin|msdyn_transactionorigin |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Transaction Type|msdyn_transactiontype |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Unique Number|msdyn_uniquenumber |Dynamics 365 for Field Service<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Work Order Business Process |msdyn_bpf_d3d97bac8c294105840e99e37a9d1c39 |Dynamics 365 for Field Service<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Work Order Details Generation Queue (Deprecated)|msdyn_workorderdetailsgenerationqueue |Dynamics 365 for Field Service<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan

## Licensing
For more information on PowerApps and Dynamics 365 licenses, see [Licensing overview](../../administrator/pricing-billing-skus.md) page.

