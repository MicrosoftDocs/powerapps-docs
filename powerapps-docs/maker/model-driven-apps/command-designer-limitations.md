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

# Modern commanding known limitations (preview)

While this feature is in preview, our intent is to collect feedback that helps prioritize what’s next. This new infrastructure does not yet support many things you may want to do – nor does it have full parity with classic commanding capabilities. We invite you to join us in this journey that is only just beginning.

We look forward to your feedback on what you like or dislike as well as what features are missing for your use cases.

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

- Pre-existing classic commands can't be customized within the command designer. This includes the out-of-the-box commands. However, you may continue to use other mechanisms and third party tools for customizing classic commands.
- Not all Power Fx functions are currently supported for commands. Certain functions won't work during this preview.
-	Sharing is currently handled differently in the command designer than with canvas apps.
   - Canvas based resources such as component libraries must be shared with any user running or customizing the commands. Notice that administrators can share with themselves in the Power Platform admin center or by using PowerShell. For example, system administrators don't automatically have access to all command component libraries in the environment.
- Microsoft Dataverse is currently the only supported data source when using Power Fx.
-	You can't currently add additional tables as data sources directly from the command designer. It will only add the table the command belongs to but not related tables.
   - However, you may open the command component library in canvas studio and add additional tables as data sources and then use them within the command designer. You must first close your command designer session.
-	When you write Power Fx formulas in the command designer, intellisense may sometimes provide recommendations for unsupported functions. It may not show an error for unsupported functions in commanding.
   - For example, functions that canvas apps support, but commands do not. You may not get an error when using the formula bar in command designer or when editing the command component library. 
-	Commands and the command component library created from one app can't be added to different apps.
   - For now, you must re-create each command to use it in different apps and different locations. 
-	Not all out-of-the-box visibility rules from classic commands are currently supported. Custom visibility rules are not currently supported either. During the preview, don't expose these in the command designer.
-	Split buttons and flyout menus are not currently supported.
-	Dynamically populated buttons aren't supported. We do not plan to support these and recommend creating them declaratively.
-	Other types of command bars are not supported in the command designer. For example, the global application header or dashboard command bars. Share feedback if you find this valuable to prioritize.
-	Command checker may not show all relevant information in some scenarios.

### See also

[Introducing Command Checker for model-app ribbons](https://powerapps.microsoft.com/blog/introducing-command-checker-for-model-app-ribbons/)