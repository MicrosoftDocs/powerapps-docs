---
title: Exit function in Power Apps
description: Reference information including syntax and examples for the Exit function in Power Apps.
author: gregli-msft
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 05/04/2020
ms.subservice: canvas-maker
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - gregli-msft
  - nkrb
---
# Exit function in Power Apps
Exits the currently running app and optionally signs out the current user.

## Description
The **Exit** function exits the currently running app. The user is returned to the list of apps. The user can then select another app to open.  

**Exit** stops any further formula evaluation. Any function calls chained with a [semicolon operator](operators.md) after the **Exit** aren't carried out.   

Use the optional *Signout* argument to sign the current user out of Power Apps. *Signout* is useful when devices are shared to ensure user security.

While authoring the app, calling **Exit** doesn't exit or sign out the user.  However, it stops the evaluation of the rest of the formula.

**Exit** can only be used in [behavior formulas](../working-with-formulas-in-depth.md).

## Syntax
**Exit**( [*Signout*] )

* *Signout* – Optional. A Boolean value that if *true* will sign the current user out of Power Apps.  The default is *false* and the user remains signed in.

## Examples

| Formula | Description | 
| --- | --- | 
| **Exit()** | Exits the current app and leaves the user signed in.  The user is returned to the list of apps.  |
| **Exit(&nbsp;true&nbsp;)** | Exits the current app and the user is signed out.  The user will need to sign back in with their credentials before running an app. | 




[!INCLUDE[footer-include](../../../includes/footer-banner.md)]