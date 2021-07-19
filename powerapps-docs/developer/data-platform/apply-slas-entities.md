---
title: "Apply SLAs to tables (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about applying SLAs to custom entities by enabling entities for applying SLAs. Also, you can create SLA KPIs."
ms.custom: ""
ms.date: 07/19/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" #TODO: NoOwner
ms.subservice: dataverse-developer
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Apply SLAs to tables

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

Service level agreements (SLAs) in Dataverse help you define the level of service or support that your organization agrees to offer a customer by including items to define metrics or key performance indicators (KPIs) to attain the service level. You can apply SLAs to custom tables and the following system tables:  
  
-   All activity tables (such as Email, Task, and Appointment) except recurring appointments (RecurringAppointmentMaster)  
  
-   Account  
  
-   Contact  
  
-   Invoice  
  
-   Incident (Case)  
  
-   Opportunity  
  
-   Quote  
  
-   Lead  
  
-   SalesOrder (Order)  

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

<a name="EnableSLAs"></a> 
  
## Enable tables for applying SLAs  

To apply SLAs to a table, you must set <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsSLAEnabled> to true for the table. You can’t change this setting after it’s been enabled. By default, the `Incident` table is enabled for SLAs.  
  
You can also use the customization tool to enable tables for SLAs. More information: [Enable entities for service level agreements](/dynamics365/customer-service/enable-entities-service-level-agreements)  
  
 After you have enabled a table for SLAs, new SLA-related columns, such as `SLAId` and `SLAInvokedId`, will be automatically added to the table.  
  
<a name="CreateSLAKPI"></a>   

## Create SLA KPIs  

To programmatically create SLA KPIs for a table, create a lookup column on any SLA-enabled table, and then set a relationship for that column to the `SLAKPIInstance` table.  
  
<a name="ApplySLA"></a>
   
## Apply SLAs to entity records  

Using the Dataverse web client, you can create SLAs for an SLA-enabled table, and set an SLA as default for the table so that it is applied automatically to any new row in the table.  
  
However, if you want to manually apply SLAs to rows based on any custom business requirement, you can programmatically update the row to set the `SLAId` column value to the desired active SLA row.  
  
<a name="Limitations"></a>   

## Limitations to applying SLAs  

 In Dataverse, the following limitations are applicable for SLAs per Dataverse environment:  
  
-   You can have a maximum of 7 tables that can have active SLAs. You will encounter an error on activating an SLA if this limit is exceeded.  
  
-   You can have a maximum of 5 SLA KPIs per table for active SLAs. You'll encounter an error on activating an SLA if this limit is exceeded. This limit is not applicable for the `Incident` table.  
  
### See also  
 [Define service-level agreements](/dynamics365/customer-service/define-service-level-agreements)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
