---
title: "ActivityParty table (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "An activity party represents a person or group associated with an activity. An activity can have multiple activity parties"
ms.custom: ""
ms.date: 03/25/2018
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
# ActivityParty table

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

An activity party represents a person or group associated with an activity. An activity can have multiple activity parties.  
  
<a name="ActivityPartyTypes"></a>   

## Activity Party Types  

 There are 11 activity party types in Microsoft Dataverse. The activity party type is stored as an integer value in the `ActivityParty.ParticipationTypeMask` column. The following table lists the different activity party types, the corresponding integer value for the `ActivityParty.ParticipationTypeMask` column, and the description.  
  
|Activity party type|Value|Description|  
|-------------------------|-----------|-----------------|  
|Sender|1|Specifies the sender.|  
|ToRecipient|2|Specifies the recipient in the To field.|  
|CCRecipient|3|Specifies the recipient in the Cc field.|  
|BccRecipient|4|Specifies the recipient in the Bcc field.|  
|RequiredAttendee|5|Specifies a required attendee.|  
|OptionalAttendee|6|Specifies an optional attendee.|  
|Organizer|7|Specifies the activity organizer.|  
|Regarding|8|Specifies the regarding item.|  
|Owner|9|Specifies the activity owner.|  
|Resource|10|Specifies a resource.|  
|Customer|11|Specifies a customer.|  
  
<a name="SupportedActivityPartyTypes"></a>   

## Activity Party types available for each activity  
 
Not all activity party types are available for each activity in Dataverse, except for a custom activity. A custom activity supports all activity party types. You can associate an activity party type for an activity by using the respective column of an activity. For example, to associate an `Organizer` activity party type with an appointment activity, you must specify a value or an array of values of the `ActivityParty` type in the `Appointment.Organizer` column.  
  
 To control which email address should be used for sending emails to the activity party, or for replying to emails from the activity party, set the `ActivityParty.AddressUsed` column.  
  
 The following table lists the activity party types that are supported for each activity, and the corresponding activity properties to specify those activity party types.  
  
|Activity entity name|Supported activity party type|Activity attribute|  
|--------------------------|-----------------------------------|------------------------|  
|Appointment|OptionalAttendee<br />Organizer<br />RequiredAttendee|Appointment.OptionalAttendees<br />Appointment.Organizer<br />Appointment.RequiredAttendees|  
|CampaignActivity|Sender|CampaignActivity.Partners<br />CampaignActivity.From|  
|CampaignResponse|Customer|CampaignResponse.Customer<br />CampaignResponse.Partner<br />CampaignResponse.From|  
|Email|BccRecipient<br />CcRecipient<br />Sender<br />ToRecipient|Email.Bcc<br />Email.Cc<br />Email.From<br />Email.To|  
|Fax|Sender<br />ToRecipient|Fax.From<br />Fax.To|  
|Letter|BccRecipient<br />Sender<br />ToRecipient|Letter.Bcc<br />Letter.From<br />Letter.To|  
|PhoneCall|Sender<br />ToRecipient|PhoneCall.From<br />PhoneCall.To|  
|RecurringAppointmentMaster|OptionalAttendee<br />Organizer<br />RequiredAttendee|RecurringAppointmentMaster.OptionalAttendees<br />RecurringAppointmentMaster.Organizer<br />RecurringAppointmentMaster.RequiredAttendees|  
|ServiceAppointment|Customer<br />Resource|ServiceAppointment.Customers<br />ServiceAppointment.Resources|  
  
### See also  
 [Activity tables](activity-entities.md)   

 [ActivityParty table](reference/entities/activityparty.md)   
 

[!INCLUDE[footer-include](../../includes/footer-banner.md)]