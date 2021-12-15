---
title: "Link custom columns of the recurring appointment master and appointment tables (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Link the custom columns of the RecurringAppointmentMaster table with custom columns of the Appointment entity to automatically copy data." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 07/19/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Link custom columns of the recurring appointment master and appointment tables

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

You can link the custom columns created for the `RecurringAppointmentMaster` table with the custom columns created for the `Appointment` table to automatically copy the data from the recurring appointment master custom column to the linked recurring appointment instances custom column, every time it is expanded.  

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]
  
There is a 1:1 mapping between the custom columns, which implies that a custom column of the recurring appointment master table can be linked to only one custom column of the appointment table. Moreover, the custom columns that are to be linked together must be of the same type. For example, you cannot link a custom column of type `string` with a `decimal` custom column. For information about different types of columns, see [Column definitions](entity-attribute-metadata.md).  
  
> [!NOTE]
> You cannot link the custom columns that have *field-level security* enabled. Similarly, you cannot enable field-level security for linked custom columns. 

  
### Link custom columns  
  
1. Create a custom column for the appointment table using the <xref:Microsoft.Xrm.Sdk.Messages.CreateAttributeRequest> class.  
  
2. Create a custom column for the recurring appointment series (recurring appointment master) table. While defining the custom column, use the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.LinkedAttributeId> property to link to the custom column that you created in step 1.  
  
3. Publish the changes to the solution.  
  
   For sample code, see [Sample: Link Custom Columns between Series and Instances](org-service/samples/link-custom-attributes-between-series-instances.md).  
  
[!INCLUDE[footer-include](../../includes/footer-banner.md)]
