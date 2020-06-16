---
title: Portal Power Apps portals Studio anatomy | Microsoft Docs
description: Learn about the anatomy of Power Apps portals Studio.
author: tapanm-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 06/16/2020
ms.author: tapanm
ms.reviewer:
---

# Power Apps portals Studio anatomy

You can use Power Apps portals Studio to create and customize your website. It contains various options to add and configure webpages, components, forms, and lists. The anatomy of Power Apps portals Studio is as follows:

![Power Apps portals Studio anatomy](media/maker-anatomy.png "Power Apps portals Studio anatomy")  

| **Annotation** | **Name**        | **Description**                                                                              |
|----------------|-----------------|----------------------------------------------------------------------------------------------|
| 1              | Command bar     | Allows you to: <ul> <li> Create a webpage. </li> <li> Delete a component. </li> <li> Sync Configuration - synchronizes the latest portal configuration changes in Common Data Service database with your current Studio session. For example, configuration changes to pages, forms or any other object using the Portal Management app. Use Sync Configuration to reflect these changes in Studio. </li> <li> Browse website - clears the portal cache and opens the current portal page. </li></ul>  |
| 2              | Toolbelt        | Allows you to:<ul><li>View and manage webpages</li><li>Add components</li><li>Edit templates</li></ul>  |
| 3              | Canvas          | Contains components that build a webpage.                                                    |
| 4              | Footer          | Displays autosave status and allows you to open-source code editor.                         |
| 5              | Properties pane | Displays properties of webpage and selected components and lets you edit them as required. |

> [!NOTE]
> Editing a portal through Power Apps portals Studio will temporarily cause poor portal performance due to multiple background processes. For example, the clear cache process runs and reloads data from Common Data Service.
