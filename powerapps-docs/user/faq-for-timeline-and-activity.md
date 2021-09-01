---
title: "Frequently Asked Questions about activities and the timeline wall| MicrosoftDocs"
description: Frequently Asked Questions about Activities and the Timeline Wall  
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 06/22/2021
ms.subservice: end-user
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

## Why can't I assign or delete an activity from the timeline?	

If you use the **HideCustomActions** rule to hide buttons, such as **Assign** and **Delete** in the ribbon command bar definition, then those buttons that are present in the Timeline control will not work. The buttons in the command bar are the same as the buttons in the Timeline control; therefore, when a user selects the **Assign** or **Delete** button in the Timeline control, the following error message is displayed:

  **You do not have permission to perform this action. Please contact your system administrator.**	

  To mitigate the issue, show the buttons in the command bar definitions.	

## Why do my users see different activities and records in My activities stream or other dashboard timelines?	

The **My activities** stream in the dashboard shows the records and activities that are owned by a particular user. For example, user "A" sees records and activities that are owned by "A", and user "B" sees records and activities that are owned by "B".	


## Can I add activities to read only rows?

Yes. You can add activities to tables that are read only such as, notes, phone calls, tasks, and more. 


## Why I can't see other users activities and rows in the My activities stream in the dashboard?

**My activities** stream in the dashboard shows the rows and activities that are owned by you (user). For example, user **A** see rows and activities that are owned by **A**, and user **B** see rows and activities that are owned by **B**.



## See also

[Set up timeline control](../maker/model-driven-apps/set-up-timeline-control.md)

[FAQs for timeline control](../maker/model-driven-apps/faqs-timeline-control.md)

[Add an appointment, email, phone call, note, or task activity to the timeline](add-activities.md)

[Dynamics 365 Sales: Frequently asked questions](/dynamics365/sales-enterprise/faqs-sales#entity-activity)

    


[!INCLUDE[footer-include](../includes/footer-banner.md)]
