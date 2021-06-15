---
title: "Configure a table for feedback with Power Apps | MicrosoftDocs"
description: "Learn how to enable feedback for a table"
ms.custom: ""
ms.date: 05/18/2018
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
ms.assetid: 5b25cf09-d43b-4165-9eaa-7549f4855e7c
caps.latest.revision: 13
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Configure a table for feedback/ratings

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

Let customers or employees write feedback for any table row, or rate table rows within a defined rating range by enabling tables for feedback.  

This capability is commonly used with a system that captures data from customers via a portal, or survey. Data about service or product satisfaction can be applied with tables that represent that kind of data.

Feedback can also be used by employees to provide feedback on a collaborative effort.

> [!NOTE]
> You will need to have the System Administrator or System Customizer security role or equivalent permissions to perform these steps.
  
## Enable feedback  
  
Edit the table to enable **Feedback**. More information: [Edit a table](edit-entities.md)
  
## Add a subgrid for feedback on the table form  

By default, users must go to the list of associated rows of the row you want to add feedback to. To make it easier for users to add feedback, you may want to add a feedback subgrid to the form of the table you are enabling feedback for.  

<!-- This is the closest I could find to a topic about adding an subgrid to a form. -->
More information:  [Sub-Grid properties overview](../model-driven-apps/sub-grid-properties-legacy.md)

## Add a rollup column  to the table form to show the ratings  

Depending on how you want to calculate the rating for the table, you can create a rollup column that calculates the rating, and then add it to the form of the table you're enabling for feedback. More information: [Define rollup columns that aggregate values](define-rollup-fields.md)
  
### See also  
 [Submit feedback or ratings for Dynamics 365 rows](/dynamics365/customer-engagement/basics/submit-feedback-ratings)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]