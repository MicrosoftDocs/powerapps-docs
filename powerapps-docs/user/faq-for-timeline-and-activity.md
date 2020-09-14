---
title: "Frequently Asked Questions about activities and the timeline wall| MicrosoftDocs"
ms.custom: ""
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 09/11/2020
ms.author: mduelae
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---
# Frequently Asked Questions about Activities and the Timeline Wall  

## Is a title required when adding a new note?

No. When adding a note to an activity, the title field is marked as a mandatory field but is not required. This is a known issue in the legacy Web Client.

## For an appointment, when I choose the option to *Save as Draft* it doesn't show that the appointment has been saved as a draft.

When you save an appointment in the legacy Web Client as a draft the title does not display **[DRAFT]** to indicate that the appointment has been saved as a draft.

## Can I add activities to read only records?

Yes. You can add activities to entities that are read only such as, notes, phone calls, tasks, and more. 

## Are HTML tags supported in **Notes**?

No. When creating a note activity for any record or entity, HTML tags are not supported. For example, if you add `<TAG> </TAG>` to a note field it will be displayed as `<TAG_XXX="XX"> </TAG>`.

## How can I improve performance on timeline wall?

Timeline Wall performance can be improved by optimizing how much data is returned by a specific entity record. 

1.	Configure entity forms to only show activities that are in use.  This can be done at the form level to only show useful activities.  For example, if you don’t use tasks for cases you can configure the timeline wall on the case form to not show tasks.
2.	Reduce the number of default records that are shown by the timeline wall.  By default, it is set to return 10, beyond 10 it can cause performance issues.  It is recommended to not exceed the default. 

## Activity Wall is not supported in Print Preview.

When you select the **Print Preview** option in Dynamics 365 the **Timeline Wall** will not show in the available list. You will see **Notes** but it will not show tasks or emails.

## Why I can't see other users activities and records in the My activities stream in the dashboard?

**My activities** stream in the dashboard shows the records and activities that are owned by you (user). For example, user **A** see records and activities that are owned by **A**, and user **B** see records and activities that are owned by **B**.


## Known issues

### Email content is lost after entering text in the description field on a email form 

**Issue**: When composing an email and filling the description field if **Save**, **Save and Close**, or **Send** is selected immediately after entering text in the description field, the most recent content added to the email may get lost. 

**Resolution**: To avoid this issue, wait a few seconds before you select **Save**, **Save and Close**, or **Send** after text is entered in the description field. 

### The From field is read only or lookup isn't working

**Issue**: The **From** field in an email form is read-only or you can't look up records and filter results by **User** or **Queue**.

**Resolution**: This happens when customization specifically have been applied on this field by your system administrator. To fix the issue, open a browser window and run the following two commands replacing the **environment URL** with the URL of your environment.


 - (replace with your envioment URL)/api/data/v9.1/RemoveActiveCustomizations(SolutionComponentName='AttributeLookupValue',ComponentId=(25E9AF0C-2341-DB11-898A-0007E9E17EBD))
 - (replace with your envioment URL)/api/data/v9.1/RemoveActiveCustomizations(SolutionComponentName='AttributeLookupValue',ComponentId=(26E9AF0C-2341-DB11-898A-0007E9E17EBD))
 
To find the URL, in the address bar the first part of the URL that starts with **https://** and ends with **.com** is your environment URL. For more information on how to find the enviroment URL, see [Get the environment UR](https://docs.microsoft.com/power-platform/guidance/coe/setup-powerbi#get-the-environment-url).

## See also

[Set up timeline control](../maker/model-driven-apps/set-up-timeline-control.md)

[FAQs for timeline control](../maker/model-driven-apps/faqs-timeline-control.md)

[Add an appointment, email, phone call, note, or task activity to the timeline](add-activities.md)

[Timeline section in the Customer Service Hub app](https://docs.microsoft.com/dynamics365/customer-service/customer-service-hub-user-guide-basics#timeline)

    
