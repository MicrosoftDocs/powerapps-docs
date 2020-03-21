---
title: Exit function | Microsoft Docs
description: Reference information, including syntax and examples, for the Exit function in Power Apps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 03/21/2020
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Exit function in Power Apps
Exits the currently running app and optionally signs out the current user.

## Description
The **Exit** function exits the currently running app.  The user is returned to the list of apps, where they can select another app to open.  

**Exit** stops any further formula evaluation.  Any function calls chained after the **Exit** are not carried out (using the [**;** operator](operators.md).   

In addition to exiting, use the *Signout* argument to also sign the current user out of Power Apps.  This is helpful when devices are shared between users and per user security and logging is desired.  

While authoring the app, calling **Exit** does not exit or sign out the user.  However it will stop evaluation of the remainder of the formula just as it would normally. 

**Exit** can only be used in [behavior formulas](../working-with-formulas-in-depth.md).

> [!NOTE]
> At this time, signing out is not supported when running the app in a web browser.

## Syntax
**Exit**( [*Signout*] )

* *Signout* – Optional. A Boolean value that if *true* will sign the current user out of Power Apps.  Default is *false*.

## Examples

| Formula | Description | 
| --- | --- | 
| **Exit()** | Exits the current app and returns the user to the list of apps.  The user remains signed in. |
| **Exit(&nbps;true&nbsp;)** | Exits the current app and the user is signed out.  The user will need to sign back in with their credentials before running another app. | 


