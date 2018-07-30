---
title: "ActivityParty entity (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "An activity party represents a person or group associated with an activity. An activity can have multiple activity parties"
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# ActivityParty entity

An activity party represents a person or group associated with an activity. An activity can have multiple activity parties.  
  
<a name="ActivityPartyTypes"></a>   

## Activity Party Types  

 There are 11 activity party types in Common Data Service for Apps. The activity party type is stored as an integer value in the `ActivityParty.ParticipationTypeMask` attribute. The following table lists the different activity party types, the corresponding integer value for the `ActivityParty.ParticipationTypeMask` attribute, and the description.  
  
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
## Activity Party Types available for each activity  
 Not all activity party types are available for each activity in CDS for Apps, except for a custom activity. A custom activity supports all activity party types. You can associate an activity party type for an activity by using the respective attribute of an activity. For example, to associate an `Organizer` activity party type with an appointment activity, you must specify a value or an array of values of the `ActivityParty` type in the `Appointment.Organizer` attribute.  
  
 To control which email address should be used for sending emails to the activity party, or for replying to emails from the activity party, set the `ActivityParty.AddressUsed` attribute.  
  
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
 [Activity Entities](activity-entities.md)   
 [Task, fax, phone call, and letter activity entities](task-fax-phone-call-letter-activity-entities.md)   
 [ActivityParty Entity](reference/entities/activityparty.md)   
 [Sample: Book an Appointment](/dynamics365/customer-engagement/developer/sample-book-appointment)
 [Sample: Convert a Fax to a Task](/dynamics365/customer-engagement/developer/sample-convert-fax-task)   
 [Sample: Override Goal Total Count and Close the Goal](/dynamics365/customer-engagement/developer/sample-override-goal-total-count-close-goal)   
 [Sample: Roll Up Goal Data for a Fiscal Period Against the Stretch Target Count](/dynamics365/customer-engagement/developer/sample-rollup-goal-data-fiscal-period-stretch-target-count)   
 [Sample: Send an E-mail Using a Template](/dynamics365/customer-engagement/developer/sample-send-email-template.md)   
 [Sample: Validate an Appointment](/dynamics365/customer-engagement/developer/sample-validate-appointment.md)
