---
title: Portal Power Apps portals Studio anatomy | Microsoft Docs
description: Learn about the anatomy of Power Apps portals Studio.
author: tapanm-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 06/02/2020
ms.author: tapanm
ms.reviewer:
---

# Power Apps portals Studio anatomy

You can use Power Apps portals Studio to create and customize your website. It contains various options to add and configure webpages, components, forms, and lists. The anatomy of Power Apps portals Studio is as follows:

![Power Apps portals Studio anatomy](media/maker-anatomy.png "Power Apps portals Studio anatomy")  

| **Annotation** | **Name**        | **Description**                                                                              |
|----------------|-----------------|----------------------------------------------------------------------------------------------|
| 1              | Command bar     | Allows you to create a webpage, delete a component, synchronize portal configuration*, and browse the website you're creating.  |
| 2              | Toolbelt        | Allows you to:<ul><li>View and manage webpages</li><li>Add components</li><li>Edit templates</li></ul>  |
| 3              | Canvas          | Contains components that build a webpage.                                                    |
| 4              | Footer          | Displays autosave status and allows you to open-source code editor.                         |
| 5              | Properties pane | Displays properties of webpage and selected components and lets you edit them as required. |

\* Sync Configuration synchronizes the latest portal configuration changes with your current Studio session. For example, configuration or site setting updated using the Portal Management app.

> [!NOTE]
> Editing a portal through Power Apps portals Studio will temporarily cause poor portal performance due to multiple background processes. For example, the clear cache process runs and reloads data from Common Data Service.
