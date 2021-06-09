---
title: Restricted tables requiring Dynamics 365 licenses | Microsoft Docs
description: A list of restricted tables in Microsoft Dataverse that require Dynamics 365 licenses.
author: KumarVivek
ms.service: powerapps
ms.topic: conceptual
ms.date: 06/08/2021
ms.author: kvivek
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Restricted tables requiring Dynamics 365 licenses

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

App makers, who are building custom apps, can use all of the Microsoft Dataverse tables available within [Common Data Model](/common-data-model/) to create apps and flows for users who have any version of Power Apps and Power Automate license.  

However, a smaller set of tables tied to Dynamics 365 apps (Dynamics 365 Sales, Customer Service, Field Service, Marketing, or Project Service Automation) require canvas and model-driven app users to have a license for the corresponding Dynamics 365 app if they need to create, update, or delete rows within the tables. These are referred to as restricted tables.

Tables may be restricted to a Dynamics 365 app license for the following reasons:
* The table is used to store and maintain product-specific configuration data that should typically be not used outside of the application.
* The table is accompanied by advanced logic that creates and maintains data in a specific way when used within a Dynamics 365 product.

If an app or flow only reads information from a table, a Dynamics 365 app license is not required and an appropriate Power Apps or Power Automate license is all that's needed.

## Restricted tables for create, update, and delete operations
The following table lists the restricted tables and the associated Dynamics 365 license requirements for users who create, update, or delete data stored within these tables. 

|Table  |Logical name  |License required  |
|---------|---------|---------|
Actual |msdyn_actual |Dynamics 365 for Field Service <br> **or** Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Agreement Business Process |msdyn_bpf_baa0a411a239410cb8bded8b5fdd88e3 |Dynamics 365 for Field Service<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Booking journal | msdyn_bookingjournal|Dynamics 365 for Field Service<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Booking Setup Metadata | msdyn_bookingsetupmetadata|Dynamics 365 for Field Service <br> **or** Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Booking timestamp | msdyn_bookingtimestamp|Dynamics 365 for Field Service<br> **or** Dynamics 365 Customer Engagement plan<br> **or** Dynamics 365 plan
Case<sup>1</sup> | incident | Dynamics 365 for Customer Service Professional edition <br>**or** Dynamics 365 for Customer Service Enterprise edition <br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Case to Work Order Business Process |msdyn_bpf_989e9b1857e24af18787d5143b67523b |Dynamics 365 for Field Service<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Configuration |msdyn_configuration |Dynamics 365 for Field Service <br> **or** Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Entitlement | entitlement | Dynamics 365 for Customer Service, Enterprise edition <br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Estimate Line|msdyn_estimateline|Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Estimate|msdyn_estimate |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Fact|msdyn_fact |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Field service setting |msdyn_fieldservicesetting |Dynamics 365 for Field Service<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Field Service System Job |msdyn_fieldservicesystemjob |Dynamics 365 for Field Service<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Goal | goal | Dynamics 365 for Sales Professional, <br>**or** Dynamics 365 for Sales, Enterprise edition, <br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
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
SLA| sla | Dynamics 365 for Customer Service Professional edition <br>**or** Dynamics 365 for Customer Service Enterprise edition <br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
System User Scheduler Setting |msdyn_systemuserschedulersetting|Dynamics 365 for Field Service <br> **or** Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Transaction Connection|msdyn_transactionconnection |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Transaction Origin|msdyn_transactionorigin |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Transaction Type|msdyn_transactiontype |Dynamics 365 for Project Service Automation<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Unique Number|msdyn_uniquenumber |Dynamics 365 for Field Service<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Work Order |msdyn_workorder |Dynamics 365 for Field Service<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan
Work Order Details Generation Queue (Deprecated)|msdyn_workorderdetailsgenerationqueue |Dynamics 365 for Field Service<br>**or** Dynamics 365 Customer Engagement plan <br> **or** Dynamics 365 plan

[1] *Case table actions permitted with only Power Apps, Power Automate, or Power Virtual Agents license:*  
Power Apps, Power Automate, or Power Virtual Agents licensed users can ‘create’ cases; can ‘read’, ‘update’ and ‘delete’ self-created cases to enable scenarios including employee self-service and case creation on behalf of customers. Power Apps, Power Automate, or Power Virtual Agents licensed users can only perform ‘read’ operation on cases created by other users. They cannot ‘update’, ‘resolve’, ‘route’, ‘close’,‘delete’,‘assign’,‘duplicate’, ‘merge’, ‘create child cases’ or perform any other custom operation on cases created by others. Users can't act as a customer service agent, can't manage cases.

> [!NOTE]
> Dynamics 365 Customer Engagement Plan and Dynamics 365 Plan licenses are no longer available for purchase and is referenced here only for the benefit of existing customers who have bought these licenses in the past.

## Licensing
For more information on Power Apps, Power Automate, Power Virtual Agents, and Dynamics 365 licenses, see [Licensing overview](/power-platform/admin/pricing-billing-skus) page.



[!INCLUDE[footer-include](../../includes/footer-banner.md)]
