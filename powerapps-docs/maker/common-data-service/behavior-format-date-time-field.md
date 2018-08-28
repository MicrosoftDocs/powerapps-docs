---
title: "Behavior and format of the Date and Time field in Common Data Service for Apps | MicrosoftDocs"
ms.custom: ""
ms.date: 05/25/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 73d691c7-344e-4c96-8979-c661c290bf81
caps.latest.revision: 47
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Behavior and format of the Date and Time field

In Common Data Service for Apps, the Date and Time data type is used in many standard entity fields. Depending on what kind of date the field represents, you can choose different field behaviors: **User Local**, **Date Only** or **Time-Zone Independent**.  
  
<a name="Behavior"></a>   

## Date and time field behavior and format  

The following table contains information about the date and time field behavior and format.  
  
|Behavior|Format|Description|  
|--------------|------------|-------------------------------|  
|**User Local** |**Date Only**<br />- or -<br />**Date and Time**|This is the default behavior of custom date and time fields.<br /><br />The field values are displayed in the current user’s local time.<br />In Web services, these values are returned using a common UTC time zone format.<br /><br />You can change this one time if you select the default behavior. More information [Change User Local Behavior](#change-user-local-behavior)|  
|**Date Only**|**Date Only**|No Time zone conversion.<br /><br />The time portion of the value is always 12:00AM.<br />The date portion of the value is stored and retrieved as specified in the UI and Web services.|  
|**Time-Zone Independent**|**Date Only**<br />- or -<br />**Date and Time**|No Time zone conversion.<br /><br />The date and time values are stored and retrieved as specified in the UI and Web services.|  

## Change User Local Behavior:

Unless the publisher of a managed solution prevents this, you can change the behavior of an existing custom Date fields from  **User Local** to **Date Only** or **Time-Zone Independent**. This is a one time change.

Changing the field behavior affects the field values that are added or modified after the field behavior was changed. The existing field values remain in the database in the UTC time zone format. To change the behavior of the existing field values from UTC to Date Only, you may need a help of a developer to do it programmatically. More Information:  [Convert behavior of existing date and time values in the database](/dynamics365/customer-engagement/developer/behavior-format-date-time-attribute#convert-behavior-of-existing-date-and-time-values-in-the-database). 

> [!WARNING]
> Before changing the behavior of an existing date and time field, you should review all the dependencies of the field, such as business rules, workflows, calculated fields, or rollup fields, to ensure that there are no issues as a result of changing the behavior. After changing the behavior of a date and time field, you should open each business rule, workflow, calculated field, and rollup field dependent on the field that you changed, review the information, and save it, to ensure that the latest date and time field’s behavior and value are used. 

### Change behavior during a solution import

When you import a solution that contains a Date field using the **User Local** behavior you may have the option to change the behavior to **Date Only** or **Time Zone Independent**.  

### Prevent changing behavior

If you are distributing a custom date field in a managed solution, you can prevent people using your solution from changing the behavior by setting the **CanChangeDateTimeBehavior** managed property to **False**. More information: [Field managed properties](set-managed-properties-metadata.md#field-managed-properties)
  
## Use cases

Consider the following use cases for **Date Only** and **Time-Zone Independent** behaviors.

### Date Only scenario: birthdays and anniversaries

The Date Only behavior is good for cases when information about the time of the day and the time zone isn’t required, such as birthdays or anniversaries. With this selection, all app users around the world see the exact same date value.  
  
### Time-Zone Independent scenario: hotel check-in

You can use this behavior when time zone information isn’t required, such as the hotel check-in time. With this selection, all app users around the world see the same date and time value.  


## Date and time query operators not supported for Date Only behavior  

The following date and time related query operators are invalid for the **Date Only** behavior. An invalid operator exception error is thrown when one of these operators is used in the query.  
  
- Older Than X Minutes  
- Older Than X Hours  
- Last X Hours  
- Next X Hours  

  
### See also

[Create and edit fields](create-edit-fields.md)<br />
[Define calculated fields to automate manual calculations](define-calculated-fields.md)<br />
[Field managed properties](set-managed-properties-metadata.md#field-managed-properties)<br />
[Managed properties](solutions-overview.md#managed-properties)

