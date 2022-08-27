---
title: "Command bar customization limitations | MicrosoftDocs"
description: "Discover the modern commanding limitations."
Keywords: command bar, command designer
author: caburk
ms.author: caburk
ms.reviewer: matp
manager: kvivek
ms.date: 05/26/2022
ms.subservice: mda-maker
ms.topic: conceptual
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Modern commanding known limitations

## Power Fx and Command component libraries limitations

Power Fx shares certain infrastructure with custom pages and canvas apps. Relevant [limitations of custom pages](model-app-page-issues.md) are also applicable to commands.

- Not all Power Fx functions are currently supported for commands.
- Microsoft Dataverse is currently the only supported data source when using Power Fx with commands. However, custom pages can be used for connecting to external data.
-	To add additional tables, open the command component library from command designer. Or you may reopen command designer by selecting a different table in app designer.
-	When you write Power Fx formulas in the command designer, intellisense may sometimes provide recommendations for unsupported functions. It may not show an error for unsupported functions within command designer or the associated command component library.
-	Commands and the command component library created from one app can't be added to different apps. However, you can copy the command and paste it within another app or command bar location.
-	Not all out-of-the-box or custom visibility rules from classic commands are currently supported in Power Fx. Classic visibility is supported without using Power Fx. This is needed to migrate classic commands to modern and classic rule formats but won't be exposed in command designer. However, classic visibility is exposed within solution files and Dataverse.
-	To delete command component libraries, you must delete the app. Alternatively, you can delete the associated record within the model-driven app element table, then delete the component library. The model-driven app element record exists in Dataverse but isn't exposed in solutions. It can be deleted via oData API or alternative low-code approach. 
- PowerFx based commands are not supported and will not run within the Dynamics 365 app for Outlook or a model-driven app that's hosted within a Portal.

## Command designer limitations

- Pre-existing classic commands can't be customized within the command designer until they're migrated to the modern infrastructure. This includes the out-of-the-box commands, which will be migrated incrementally over time. You may continue to use other mechanisms and third-party tools for customizing classic commands.
- Dynamically populated buttons aren't supported. We recommend creating them declaratively.
- Global application header and dashboard command bars aren't currently supported in command designer. These are customized infrequently. Share feedback if you find this valuable to prioritize.

### See also

[Modern commanding overview](command-designer-overview.md)

[Introducing Command Checker for model-app ribbons](https://powerapps.microsoft.com/blog/introducing-command-checker-for-model-app-ribbons/)
