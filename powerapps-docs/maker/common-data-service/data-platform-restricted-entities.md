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

PowerApps is licensed on a per-user basis, each user who accesses the service to create and run apps needs a license. The Common Data Service for Apps allows users to use entities from the Common Data Model and Dynamics 365 products to build apps using PowerApps and Flow. Specific entities which are closely tied to the Dynamics 365 products require users of those apps, who need to perform create, update, or delete actions on data stored within these entities to be licensed for the respective Dynamics 365 product and cannot be used with a standard PowerApps or Flow plan. Apps or Flows which only read data from these entities can still be used with the appropriate PowerApps plan. Please see the [PowerApps pricing page](https://powerapps.microsoft.com/pricing) for more information on available plans.

   > [!NOTE]
   > Apps or Flows which only read data from these entities can still be used with the appropriate PowerApps plan.

## Restricted entities for create, update and delete operations

The following entities require end users of Apps and Flows which perform create, update or delete operations against data stored within them. 


Entity | Logical name | License required
--- | --- | ---
Actual |msdyn_actual |Dynamics 365 for Field Service <br> **or** Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Booking journal | msdyn_bookingjournal|Dynamics 365 for Field Service<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Booking Setup Metadata | msdyn_bookingsetupmetadata|Dynamics 365 for Field Service <br> **or** Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Booking timestamp | msdyn_bookingtimestamp|Dynamics 365 for Field Service<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
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
Journey | journey | Dynamics 365 for Marketing <br> **or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Knowledge article | knowledgearticle | Dynamics 365 for Customer Service, Enterprise edition <br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Msdyn_bpf_*<br>*Multiple entities prefixed with "Msdyn_bpf_"* | |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Organizational Unit |msdyn_organizationalunit |Dynamics 365 for Field Service <br> **or** Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Product Inventory |msdyn_productinventory |Dynamics 365 for Field Service<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Project Parameter|msdyn_projectparameter |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Project Task Dependency|msdyn_projecttaskdependency |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Project Task|msdyn_projecttask |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Project Team Member|msdyn_projecteam |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Resource Assignment Detail (Deprecated)|msdyn_resourceassignmentdetail |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Resource Assignment|msdyn_resourceassignment |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Resource Restriction (Deprecated) |msdyn_workorderresourcerestriction | Dynamics 365 for Field Service<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Routing rule set | routingrule | Dynamics 365 for Customer Service, Enterprise edition <br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Schedule Board Setting |msdyn_scheduleboardsetting |Dynamics 365 for Field Service <br> **or** Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Scheduling Parameter |msdyn_schedulingparameter |Dynamics 365 for Field Service <br> **or** Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
SLA | sla | Dynamics 365 for Customer Service, Enterprise edition <br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
System User Scheduler Setting |msdyn_systemuserschedulersetting |Dynamics 365 for Field Service <br> **or** Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Transaction connection|msdyn_transactionconnection |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Transaction Origin|msdyn_transactionorigin |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Transaction Type|msdyn_transactiontype |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Unique Number |msdyn_uniquenumber |Dynamics 365 for Field Service<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan
Work Order Details Generation Queue (Deprecated) |msdyn_workorderdetailsgenerationqueue |Dynamics 365 for Field Service<br>**or** Dynamics 365 Customer Engagement Plan <br> **or** Dynamics 365 Plan






## Licensing

Please the [Licensing overview](../../administrator/pricing-billing-skus.md) page for more information on PowerApps and Dynamics 365 licenses.

