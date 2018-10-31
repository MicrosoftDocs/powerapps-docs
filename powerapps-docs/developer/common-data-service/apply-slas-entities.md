---
title: "Apply SLAs to entities (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about applying SLAs to custom entities by enabling entities for applying SLAs. Also, you can create SLA KPIs."
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "JimDaly" #TODO: NoOwner
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Apply SLAs to entities

Service level agreements (SLAs) in Common Data Service for Apps help you define the level of service or support that your organization agrees to offer a customer by including items to define metrics or key performance indicators (KPIs) to attain the service level. You can apply SLAs to custom entities and the following system entities:  
  
-   All activity entities (such as Email, Task, and Appointment) except recurring appointments (RecurringAppointmentMaster)  
  
-   Account  
  
-   Contact  
  
-   Invoice  
  
-   Incident (Case)  
  
-   Opportunity  
  
-   Quote  
  
-   Lead  
  
-   SalesOrder (Order)  
  
<a name="EnableSLAs"></a> 
  
## Enable entities for applying SLAs  

 To apply SLAs to an entity, you must set the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsSLAEnabled> attribute to true for the entity. You can’t change this setting after it’s been enabled. By default, the `Incident` entity is enabled for SLAs.  
  
 You can also use the customization tool to enable entities for SLAs. More information: [Enable entities for service level agreements](/dynamics365/customer-engagement/customer-service/enable-entities-service-level-agreements)  
  
 After you have enabled an entity forSLAs, new SLA-related attributes, such as `SLAId` and `SLAInvokedId`, will be automatically added to the entity.  
  
<a name="CreateSLAKPI"></a>   

## Create SLA KPIs  

 To programmatically create SLA KPIs for an entity, create a lookup attribute on any SLA-enabled entity, and then set a relationship for that attribute to the `SLAKPIInstance` entity.  
  
<a name="ApplySLA"></a>
   
## Apply SLAs to entity records  

 Using the CDS for Apps web client, you can create SLAs for an SLA-enabled entity, and set an SLA as default for the entity so that it is applied automatically to any new entity records.  
  
 However, if you want to manually apply SLAs to entity records based on any custom business requirement, you can programmatically update the entity record to set the `SLAId` attribute value to the desired active SLA record.  
  
<a name="Limitations"></a>   

## Limitations to applying SLAs in Dynamics 365 (online)  

 In CDS for Apps, the following limitations are applicable for SLAs per CDS for Apps instance (organization):  
  
-   You can have a maximum of 7 entities that can have active SLAs. You will encounter an error on activating an SLA if this limit is exceeded.  
  
-   You can have a maximum of 5 SLA KPIs per entity for active SLAs. You will encounter an error on activating an SLA if this limit is exceeded. This limit is not applicable for the `Incident` entity.  
  
### See also  
 [Service entities in Customer Engagement](/dynamics365/customer-engagement/developer/service-entities)   
 [Enhanced service level agreements (SLAs)](/dynamics365/customer-engagement/admin/enhanced-service-level-agreements)