---
title: Known issues about activities
description: Learn about known issues that may occur with activities in model-driven apps.
author: sriharibs-msft
ms.component: pa-user
ms.topic: overview
ms.date: 06/20/2023
ms.subservice: end-user
ms.author: srihas
ms.reviewer: sericks
ms.custom: 
ms.assetid: 
search.audienceType: 
  - enduser
---
# Known issues about activities

Learn about known issues that may occur with activities in model-driven apps.

- On appointment grids, all-day appointments may show incorrect values for **Start Time** and **End Time**. This issue is limited to the grid control showing appointment records, as forms and calendar control show correct **Start Time** and **End Time** for all-day appointments.
  
  To fix this issue, use the [calendar control](../maker/model-driven-apps/add-calendar-control.md) as the default control to view appointments.

- The process that checks for conflicts for the people and resources on an appointment is triggered only when a valid Dynamics 365 solution is installed on the environment, as this requires a few scheduling-related tables to be a part of the environment. Appointments created in an environment without a relevant Dynamics 365 solution installed have an **Open** status, rather than the **Scheduled** status. For more information on the scheduling tables and the license required, see [Restricted tables for create, update, and delete operations](../maker/data-platform/data-platform-restricted-entities.md#restricted-tables-for-create-update-and-delete-operations).
