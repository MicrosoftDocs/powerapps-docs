---
title: "Command bar customization limitations | MicrosoftDocs"
description: "Discover the modern commanding limitations."
Keywords: command bar, command designer
author: caburk
ms.author: caburk
ms.reviewer: matp
manager: kvivek
ms.date: 07/26/2021

ms.subservice: mda-maker
ms.topic: conceptual
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Modern commanding known limitations (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

<!-- While this feature is in preview, our intent is to collect feedback that helps prioritize what’s next. This new infrastructure does not yet support many things you may want to do – nor does it have full parity with classic commanding capabilities. We invite you to join us in this journey that is only just beginning.

We look forward to your feedback on what you like or dislike as well as what features are missing for your use cases. -->

## Power Fx and Command component libraries limitations
Power Fx shares infrustructure with custom pages and certain limitations of custom pages may also apply.

- Not all Power Fx functions are currently supported for commands. More functions will become available incrementally.
- Microsoft Dataverse is currently the only supported data source when using Power Fx with commands. However, custom pages can be used for connecting to external data.
-	To add additional tables open the command component library from command designer. Or you may re-open command designer by slecting a different table in app designer. 
-	When you write Power Fx formulas in the command designer, intellisense may sometimes provide recommendations for unsupported functions. It may not show an error for unsupported functions within command designer or the associated command component library. 
-	Commands and the command component library created from one app can't be added to different apps. However, you can copy the command and paste it within another app or command bar location.
-	Not all out-of-the-box or custom visibility rules from classic commands are currently supported in Power Fx. Classic visibility are supported without using Power Fx. This is needed to migrate classic commands to modern and classic rule formats but will not be exposed in command designer. Only within solution files and Dataverse.
-	Command component libraries can be difficult to delete. You must first delete the associated record within the Model-driven app elemet table. This record exists in Dataverse but is not exposed in solutions. However, these records can be deleted under Data --> Tables (slect a table) --> Data within the Power Apps maker experience. 
        
## Command designer limitations
- Pre-existing classic commands can't be customized within the command designer until they're migrated to the modern infrastructure. This includes the out-of-the-box commands which will migrated incrementally over time. Capabilities to migrate your own classic commands will be available soon. You may also continue to use other mechanisms and third-party tools for customizing classic commands.    
- Dynamically populated buttons aren't supported. We don't plan to support these and recommend creating them declaratively. 
- Global application header and dashboard command bars are not currently supported in command designer. These are customized infrequently. Share feedback if you find this valuable to prioritize.                                                    

### See also

[Modern commanding overview (preview)](command-designer-overview.md)

[Introducing Command Checker for model-app ribbons](https://powerapps.microsoft.com/blog/introducing-command-checker-for-model-app-ribbons/)
