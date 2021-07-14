---
title: "Link custom attributes of the recurring appointment master and appointment entities (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Link the custom attributes of the RecurringAppointmentMaster entity with custom attributes of the Appointment entity to automatically copy data." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
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
# Link custom attributes of the recurring appointment master and appointment entities

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

You can link the custom attributes created for the `RecurringAppointmentMaster` entity with the custom attributes created for the `Appointment` entity to automatically copy the data from the recurring appointment master custom attribute to the linked recurring appointment instances custom attribute, every time it is expanded.  
  
 There is a 1:1 mapping between the custom attributes, which implies that a custom attribute of the recurring appointment master entity can be linked to only one custom attribute of the appointment entity. Moreover, the custom attributes that are to be linked together must be of the same type. For example, you cannot link a custom attribute of type `string` with a `decimal` custom attribute. For information about different types of attributes, see [Customize Entity Attribute Metadata](/dynamics365/customer-engagement/developer/customize-entity-attribute-metadata).  
  
> [!NOTE]
>  You cannot link the custom attributes that have *field-level security* enabled. Similarly, you cannot enable field-level security for linked custom attributes.  
  
### Link custom attributes  
  
1. Create a custom attribute for the appointment entity using the <xref:Microsoft.Xrm.Sdk.Messages.CreateAttributeRequest> class.  
  
2. Create a custom attribute for the recurring appointment series (recurring appointment master) entity. While specifying the attribute metadata for the custom attribute, use the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.LinkedAttributeId> property to link to the custom attribute that you created in step 1.  
  
3. Publish the changes to the solution.  
  
   For sample code, see [Sample: Link Custom Attributes between Series and Instances](org-service/samples/link-custom-attributes-between-series-instances.md).  
  
### See also

 [Recurring Appointment Entities](/dynamics365/customer-engagement/developer/recurring-appointment-entities)   
 [RecurringAppointmentMaster Entity](/reference/entities/recurringappointmentmaster.md)   
 [Sample: Link Custom Attributes between Series and Instances](org-service/samples/link-custom-attributes-between-series-instances.md)   
 [Customize Entity Attribute Metadata](/dynamics365/customer-engagement/developer/customize-entity-attribute-metadata)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]