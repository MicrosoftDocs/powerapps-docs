---
title: "Frequently Asked Questions about activities and the timeline wall| MicrosoftDocs"
description: Frequently Asked Questions about Activities and the Timeline Wall  
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 09/23/2020
ms.author: mkaur
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

No. When adding a note to an activity, the title column is marked as a mandatory column but is not required. This is a known issue in the legacy Web Client.

## For an appointment, when I choose the option to *Save as Draft* it doesn't show that the appointment has been saved as a draft.

When you save an appointment in the legacy Web Client as a draft the title does not display **[DRAFT]** to indicate that the appointment has been saved as a draft.

## Can I add activities to read only rows?

Yes. You can add activities to tables that are read only such as, notes, phone calls, tasks, and more. 

## Are HTML tags supported in **Notes**?

No. When creating a note activity for any row or table, HTML tags are not supported. For example, if you add `<TAG> </TAG>` to a note column it will be displayed as `<TAG_XXX="XX"> </TAG>`.

## How can I improve performance on timeline wall?

Timeline Wall performance can be improved by optimizing how much data is returned by a specific table row. 

1.	Configure table forms to only show activities that are in use.  This can be done at the form level to only show useful activities.  For example, if you don’t use tasks for cases you can configure the timeline wall on the case form to not show tasks.
2.	Reduce the number of default rows that are shown by the timeline wall.  By default, it is set to return 10, beyond 10 it can cause performance issues.  It is recommended to not exceed the default. 

## Activity Wall is not supported in Print Preview.

When you select the **Print Preview** option in Dynamics 365 the **Timeline Wall** will not show in the available list. You will see **Notes** but it will not show tasks or emails.

## Why I can't see other users activities and rows in the My activities stream in the dashboard?

**My activities** stream in the dashboard shows the rows and activities that are owned by you (user). For example, user **A** see rows and activities that are owned by **A**, and user **B** see rows and activities that are owned by **B**.



## See also

[Set up timeline control](../maker/model-driven-apps/set-up-timeline-control.md)

[FAQs for timeline control](../maker/model-driven-apps/faqs-timeline-control.md)

[Add an appointment, email, phone call, note, or task activity to the timeline](add-activities.md)

[Dynamics 365 Sales: Frequently asked questions](https://docs.microsoft.com/dynamics365/sales-enterprise/faqs-sales#entity-activity)

    


[!INCLUDE[footer-include](../includes/footer-banner.md)]