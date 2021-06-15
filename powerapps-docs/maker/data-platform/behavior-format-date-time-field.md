---
title: "Behavior and format of the Date and Time column in Microsoft Dataverse | MicrosoftDocs"
description: Understand the format of date and time columns. 
ms.custom: ""
ms.date: 05/25/2018
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "conceptual"
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
# Behavior and format of the Date and Time column

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

In Microsoft Dataverse, the Date and Time data type is used in many standard table columns. Depending on what kind of date the column represents, you can choose different column behaviors: **User Local**, **Date Only**, or **Time-Zone Independent**.  
  
<a name="Behavior"></a>   

## Date and time column behavior and format  

The following table contains information about the date and time column behavior and format.  
  
|Behavior|Format|Description|  
|--------------|------------|-------------------------------|  
|**User Local** |**Date Only**<br />- or -<br />**Date and Time**|This is the default behavior of custom date and time columns.<br /><br />The column values are displayed in the current user's local time.<br />In Web services, these values are returned using a common UTC time zone format.<br /><br />You can change this one time if you select the default behavior. More information [Change User Local Behavior](#change-user-local-behavior)|  
|**Date Only**|**Date Only**|No Time zone conversion.<br /><br />The time portion of the value is always 12:00AM.<br />The date portion of the value is stored and retrieved as specified in the UI and Web services.|  
|**Time-Zone Independent**|**Date Only**<br />- or -<br />**Date and Time**|No Time zone conversion.<br /><br />The date and time values are stored and retrieved as specified in the UI and Web services.|  

## Change User Local Behavior:

Unless the publisher of a managed solution prevents this, you can change the behavior of an existing custom Date columns from  **User Local** to **Date Only** or **Time-Zone Independent**. This is a one time change.

Changing the column behavior affects the column values that are added or modified after the column behavior was changed. The existing column values remain in the database in the UTC time zone format. To change the behavior of the existing column values from UTC to Date Only, you may need a help of a developer to do it programmatically. More Information:  [Convert behavior of existing date and time values in the database](/dynamics365/customer-engagement/developer/behavior-format-date-time-attribute#convert-behavior-of-existing-date-and-time-values-in-the-database). 

> [!WARNING]
> Before changing the behavior of an existing date and time column, you should review all the dependencies of the column, such as business rules, workflows, calculated columns, or rollup columns, to ensure that there are no issues as a result of changing the behavior. After changing the behavior of a date and time column, you should open each business rule, workflow, calculated column, and rollup column dependent on the column that you changed, review the information, and save it, to ensure that the latest date and time column's behavior and value are used. 

### Change behavior during a solution import

When you import a solution that contains a Date column using the User Local behavior, you may have the option to change the behavior to **Date Only** or **Time Zone Independent**.  

### Prevent changing behavior

If you are distributing a custom date column in a managed solution, you can prevent people using your solution from changing the behavior by setting the **CanChangeDateTimeBehavior** managed property to **False**. More information: [Set  managed properties for columns](set-managed-properties-for-field.md)
  
## Use cases 

Consider the following use cases for **Date Only** and **Time-Zone Independent** behaviors.

### Date Only scenario: birthdays and anniversaries

The Date Only behavior is good for cases when information about the time of the day and the time zone isn't required, such as birthdays or anniversaries. With this selection, all app users around the world see the exact same date value.  
  
### Time-Zone-Independent scenario: hotel check-in

You can use this behavior when time zone information isn't required, such as the hotel check-in time. With this selection, all app users around the world see the same date and time value.  


## Best practices for using time zone

### For my Date/Time column I was expecting (UTC/Local) and I am seeing the opposite value

This is caused by a lack of parity between the table column setting and the app form setting. When a table column is configured for Time Zone Independent or User Local, it determines if the time zone offset is honored or not when the data is being retrieved from the store. However, the app form also has a setting of UTC or Local. 
 
This tells the form how to interpret the data it receives from the Dataverse. If the data retrieved from the store is time zone independent, but the form is set to local, the UTC data will be displayed as user local time based on the user’s time zone in their profile. The reverse is also true, a user local value from the store will be displayed as UTC if the form is set to UTC. Fortunately, the form’s date time zone values can be modified without disrupting the existing rows.

### I picked Date Only in my table column, but my form is showing a time picker along with the date

This would happen if you chose a behavior of time zone independent or user local for your date only column. In the Dataverse it will store a time of 00:00:00 by default, but if you add the column to a form it will assume you need to set the time as well. If you leave the time pickers in the form, users can enter a time and it will be saved as something other than 00:00:00. How can you fix this
* Edit the form and remove the time picker and associated formulas. This will save the time as 00:00:00 and will still allow for time zone-based date calculations.
* If your column is currently set to user local, and you don’t need the date to be time zone calculated, you can change it to date only. This is a permanent change and cannot be undone. This change cannot be made to time zone-independent behavior columns. Always be careful changing behaviors as other apps, plugins, or workflows may be relying on the data.

### I have a date only column, but it is showing the wrong date for some users
If this happens, check the behavior that is set up for the date only column. If the column is set to time zone independent or user local, the included timestamp will cause the date to appear differently for different users. The form display settings of UTC or Local will determine if the date displayed is calculated using the user’s time zone settings or if it displays it as the UTC value. Changing the form values to UTC instead of user local will prevent time zone offset calculations and will display the UTC date for the saved row. Alternately, if you need this to be a static date that does not change and the column is currently user local, you can change the column behavior to Date Only. Be cautious though, this can't be undone.

### My (script/plug-in) is supposed to intercept the date submitted using the Universal Client before the user local conversion occurs, but instead it is being treated as User Local data 

The web client and universal client have slightly different behaviors when it comes to when data is translated between UTC and User Local. 
In the web client, dates are entered into the client, passed to the API as provided, and converted later into user local time. This allowed scripts/plug-ins to retrieve the data and take action before data was passed to the platform services and translated into user local time. 
In the universal client, the translation of a date into user local values happens before the data is passed to the API, because of this, the data provided will not be a UTC date but rather a user local date based on the user who retrieved or posted it. 
To resolve this, a user can either:

* Change the form to time zone independent which will retain the UTC value. This only works if the user does not need the form to display in user local time.
* Modify their script to detect the time zone offset used, recalculate back to UTC within the script, then take action.

## Date and time query operators not supported for Date Only behavior  

The following date and time related query operators are invalid for the **Date Only** behavior. An invalid operator exception error is thrown when one of these operators is used in the query.  
  
- Older Than X Minutes  
- Older Than X Hours  
- Last X Hours  
- Next X Hours  

  
### See also

[Create and edit columns](create-edit-fields.md)<br />
[Define calculated columns to automate manual calculations](define-calculated-fields.md)<br />
[Column managed properties](/power-platform/alm/managed-properties-alm#view-and-edit-column-managed-properties)<br />
[Managed properties](/power-platform/alm/managed-properties-alm)  
[Blog: Working with time zones in the Dataverse](https://powerapps.microsoft.com/en-us/blog/working-with-time-zones-in-the-data-platform/)




[!INCLUDE[footer-include](../../includes/footer-banner.md)]