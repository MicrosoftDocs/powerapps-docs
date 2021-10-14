---
title: "Update a recurring appointment (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Update a recurring appointment series by using the IOrganizationService.Entity method or the UpdateRequest message on the RecurringAppointmentMaster entity." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/25/2021
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
# Update a recurring appointment

You can either update the whole series or update an instance of a recurring appointment.  
  
## Update a recurring appointment series  
 You can update a recurring appointment series by using the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*> method or the <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> message on the `RecurringAppointmentMaster` table. You can update the *basic* or *recurrence* information.  
  
### Update basic information  
 When you update the basic information of a recurring appointment series, such as subject, location, or attendees, all instances in the recurring appointment series are updated except those that have exceptions on the same column.  
  
### Update recurrence information  
 When you update the recurring information of a recurring appointment series, such as pattern and range, the following things occur:  
  
1. A new series with a new `RecurringAppointmentMaster.ActivityId` is created that has the same information as the original series, and the date in the `RecurringAppointmentMaster.EffectiveEndDate` column of the new series is set to the last occurring past instance of the original series. All the future instances of the original series are deleted. In this manner, the original series is ended, and the history of the past instances is preserved in the system by storing it in a new series.  
  
2. The new information is used to create the future instances of the new series from the effective start date (`RecurringAppointmentMaster.EffectiveStartDate`).  
  
   Also, the `RecurringAppointmentMaster.GroupId` column for both the original and the new series  is populated with the same value. This implies that whenever you update the recurrence information in a recurring appointment series, all the new series’ that are created have the same value for the `RecurringAppointmentMaster.GroupId` column as the recurring appointment series that is updated, although each series has a unique series ID.  
  
> [!NOTE]
>  When you update the recurrence information of a recurring appointment series that has all the instances slated to occur in future, all instances are deleted and new recurrence information is used to create or expand new instances.  
  
 To see the sample code for updating a recurring appointment series, see [Sample: Update a Recurring Appointment](org-service/samples/reschedule-cancel-recurring-appointment.md).  
  
## Update a recurring appointment instance  
 Because the recurring appointment records are stored as appointment objects, you can use the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*> method on the `Appointment` table to update a recurring appointment instance. When you update a recurring appointment instance, the instance is marked as an exception to the recurring appointment series. More information: [Create a Recurring Appointment Exception](create-recurring-appointment-series-instance-exception.md#bkmk_createexception)  
  
 You can also use the <xref:Microsoft.Crm.Sdk.Messages.CreateExceptionRequest> class on the `Appointment` table to update a recurring appointment instance.  
  
> [!TIP]
>  Recurring appointment instances can be identified using the `Appointment.InstanceTypeCode` column, which will have a value of “2” (Recurring Instance). More information: [Appointment table](reference/entities/appointment.md)  
  
### See also  
    
 [Sample: Create, Retrieve, Update, and Delete (CRUD) a Recurring Appointment](org-service/samples/create-retrieve-update-delete-recurring-appointment.md) 
 [Sample: Reschedule and Cancel Recurring Appointment](org-service/samples/reschedule-cancel-recurring-appointment.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
