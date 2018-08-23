---
title: Customize commands with model-driven apps | Microsoft Docs
description: Learn how to customize commands with model-driven apps
services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: faisalmo
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/17/2018
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Customize commands with model-driven apps 

The commands that appear within a form or list command bar are customizable. Commands are based on the XML schemas used in Office ribbons, so the term *ribbon* is still used. When you create a command, you can define three elements:

- *Display rules* are evaluated when the form or list loads to determine whether a command or group of commands are visible.
- *Enable rules* control whether a command is enabled based on various conditions such as the currently selected item in the UI.
- An *Action* for each command to tell it what to do when selected. A command can open a URL or execute a function defined within a JavaScript web resource.

Custom commands are positioned based on any existing commands. You must compose a *custom action* that defines what change to apply to the existing set of commands. 

There is no designer provided for commands. Fortunately, the community has provided tools. The [Ribbon Workbench](http://www.develop1.net/public/rwb/ribbonworkbench.aspx) provides a graphical interface and is the most commonly used tool to customize commands.

More information: [Dynamics 365 Customer Engagement Developer Guide: Customize commands and the ribbon](/dynamics365/customer-engagement/developer/customize-dev/customize-commands-ribbon)


