---
title: "Recurring appointment partial expansion model (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "The partial expansion model is an asynchronous job that runs at pre-specified intervals, defined at the organization level, and used to create recurring appointment instances." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/25/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Recurring appointment partial expansion model

Microsoft Dataverse implements a partial expansion model to create recurring appointment instances in the database. The recurrence information, specified when you create a `RecurringAppointmentMaster` row, is used to create or synchronize individual instances in a phased manner. This controls the creation of a large number of appointment rows in Dataverse due to the creation or synchronization of recurring appointments that have a large or infinite (no end date) recurrence range.  

 The partial expansion model is an asynchronous job in Dataverse that runs at pre-specified intervals, and is defined at the organization level using the `Organization.RecurrenceExpansionJobBatchInterval` column. Moreover, the instance expansion model depends on an organization-level parameter, for example, “N,” where “N” stands for the maximum number of instances that can be created synchronously. You can specify an appropriate value for this variable using the `Organization.RecurrenceExpansionSynchCreateMax` column. These properties are covered in detail in the [Parameters for the partial expansion job](#Parameter) section later.  

<a name="Scenario1"></a>   
## When the recurring appointment instances are less than or equal to “N”  
 If the number of instances to be generated because of the recurrence information is less than or equal to “N”, the actual number of instances are created synchronously from the effective start date of the appointment. Each instance is stored as an appointment row in Dataverse.  

<a name="Scenario2"></a>   

## When the recurring appointment instances are more than “N”  
 For each recurring appointment created in Dataverse, an asynchronous expansion job is created. The instances of the recurring appointment are expanded in the following phases:  

1. **Synchronous expansion**: The first “N” instances of the recurring appointment are created synchronously from the effective start date. Each instance is stored as an appointment row with the `Appointment.InstanceTypeCode` column set to “2” (Recurring Instance). The expansion of the rest of the instances is passed on to an asynchronous job. The effective start date is the date from which the recurring appointment series has to be expanded.  

2. **Asynchronous expansion**: Asynchronous jobs handle the rest of the expansion job and periodically expand the instances according to the recurrence information. The asynchronous expansion occurs only until the future expansion window (`Organization.FutureExpansionWindow`). After that, a new asynchronous job is created that handles expansion until the next future expansion window. The asynchronous service periodically expands the instances and stores them as appointment rows in the system.  

<a name="Parameter"></a>   
## Parameters for the partial expansion job  
 You must set appropriate values for these organization-level columns in the `Organization` row for the expansion model to work as per your requirements. You must have the System Administrator role or appropriate privilege to do this. The following table provides information about these properties.  


|                    Column                     |                                                                                                                                                                                                                    Description                                                                                                                                                                                                                    |
|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  Organization.RecurrenceExpansionSynchCreateMax  |                                                                                             This is the maximum number of appointment instances that is created at the time of creation or synchronization of a recurring appointment. You must specify an integer value that corresponds to the number of instances. This value corresponds to “N”.                                                                                              |
|         Organization.PastExpansionWindow         |    This is the maximum valid time period in the past up to which the recurring appointments can be expanded or synchronized with Dynamics 365 for Outlook. You must specify an integer value that corresponds to the number of months.<br /><br /> The value of this column determines the past instance cutoff date for expanding or synchronizing the recurring appointment instances.    |
|        Organization.FutureExpansionWindow        | This is the maximum valid time period in the future up to which the recurring appointments can be expanded or synchronized with Dynamics 365 for Outlook. You must specify an integer value that corresponds to the number of months.<br /><br /> The value of this column determines the future instance cutoff date for expanding or synchronizing the recurring appointment instances. |
| Organization.RecurrenceExpansionJobBatchInterval |                                                                                                                                                                               This is the frequency in seconds after which the partial expansion job is triggered.                                                                                                                                                                                |
|   Organization.RecurrenceExpansionJobBatchSize   |                                                                                                                                                                                  This is the number of instances expanded every time the asynchronous job runs.                                                                                                                                                                                   |

### See also  
    
 [Create a Recurring Appointment Series, Instance or Exception](create-recurring-appointment-series-instance-exception.md)<br/>   
 [Update a Recurring Appointment](update-recurring-appointment.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]