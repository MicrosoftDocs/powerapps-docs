---
title: "Command bar customization limitations | MicrosoftDocs"
description: "Use the command designer to customize the command bar."
Keywords: command bar, command designer
author: caburk
ms.author: caburk
ms.reviewer: matp
manager: kvivek
ms.date: 07/26/2021
ms.service: powerapps
ms.subservice: mda-maker
ms.topic: conceptual
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Modern commanding known limitations

Please note these are preview features and the intent is to collect feedback that helps prioritize what’s next. This new infrastructure does not yet support many things you may want to do – nor does it have full parity with classic commanding capabilities. We invite you to join us in this journey that is only just beginning. 

We look forward to your feedback on what you like or dislike as well as what features are missing for your use cases.

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

1.	Pre-existing classic commands cannot be customized within the command designer. This includes the out of the box commands. However, you may continue to use other mechanisms and 3rd party tools for customizing classic commands.
2.	Not all Power Fx functions are currently supported for commands. We’re just getting started so certain functions will not work during this preview. 
3.	Sharing is currently handled a little differently.
a.	Canvas based resources such as component libraries must be shared with any user running or customizing the commands. 
i.	Note that admins can share with themselves in the admin center or by using PowerShell.
b.	For example, System administrators do not automatically have access to all command component libraries in the environment. 
4.	Dataverse is currently the only supported data source when using Power Fx. Other data sources will be added in future releases.
5.	You cannot currently add additional tables as data sources directly from the command designer. It will only add the table the command belongs to but not related tables. 
a.	However, you may open the command component library in canvas studio and add additional tables as data sources and then use them within the command designer. You must first close your command designer session.
6.	When writing Power Fx formulas in the command designer, intellisense may sometimes provide recommendations for unsupported functions. It may not show an error for unsupported functions in commanding. 
a.	For example, functions that canvas apps support, but commands do not. You may not get an error when using the formula bar in command designer or when editing the command component library. 
7.	Commands and the command component library created from one app cannot be added to different apps. 
a.	For now you must re-create each command to use it in different apps and different locations. 
8.	Not all out of the box visibility rules from classic commands are currently supported. Custom visibility rules are not currently supported either. We’re working to support these within Power Fx + on the backend, but do not plan on exposing these in the command designer. 
9.	Split buttons and Flyout menus are not currently supported.
10.	Dynamically populated buttons are not supported. We do not plan to support these and recommend creating them declaratively. 
11.	Other types of command bars are not supported in the command designer. For example, the global application header or dashboard command bars. 
a.	Please share feedback if you find this valuable to prioritize. This is not currently on the near-term roadmap. 
12.	Command checker may not show all relevant information in some scenarios. 
