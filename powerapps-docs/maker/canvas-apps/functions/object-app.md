---
title: App object | Microsoft Docs
description: Reference information, including syntax and examples, for the App object in PowerApps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: anneta
ms.date: 03/01/2019
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# App object in PowerApps
Provides information about the currently running app and control over the app's behavior.

## Description
Like a control, the **App** object provides properties that your app can use to know which screen is currently being displayed and to control when a confirmation dialog should be displayed before losing unsaved changes.  Every app has an **App** object.  

For setting properties, the **App** object appears at the top of the hierarchical list of controls in the left navigation pane, and you can select this object like a control on a screen. After you select the object, you can view and edit one of its properties if you select that property in the drop-down list to the left of the formula bar.  

![](media/object-app/appobject.png)

## ActiveScreen property
The **ActiveScreen** provides the screen that's currently displayed. 

It returns a screen object, which you can use to reference properties of the screen or compare to another screen to determine which screen is displayed.  

Use the **[Back](function-navigate.md)** or **[Navigate](function-navigate.md)** functions to change the displayed screen.

## OnStart property
The **OnStart** property is executed when the user starts the app. 

This property is commonly used to retrieve and cache data into collections with the **[Collect](function-clear-collect-clearcollect.md)** function, set up variables with the **[Set](function-set.md)** function, and navigate to an initial screen with the **[Navigate](function-navigate.md)** function. 

This formula is evaluated before the first screen appears. No screen is loaded, so you can't set context variables with the **[UpdateContext](function-updatecontext.md)** function. However, you can pass context variables with the **Navigate** function.

After you change the **OnStart** property, you can test it by hovering over the **App** object in the left navigation pane, selecting the ellipsis (...) that appears, and then selecting **Run OnStart**. Unlike when the app is loaded for the first time, existing collections and variables will already be set. Use the **[ClearCollect](function-clear-collect-clearcollect.md)** function instead of the **Collect** function to start with empty collections.

 ![App item context menu with Run OnStart](media/object-app/appobject-runonstart.png)

## ConfirmExit properties

Nobody wants to lose unsaved changes.  Use the **ConfirmExit** and **ConfirmExitMessage** properties to warn the user before they close the app.

### ConfirmExit

**ConfirmExit** is a Boolean property that if true causes a confirmation dialog to be shown before closing the app.  The default for this property is *false* and no confirmation dialog is shown.

Use this property to control when a confirmation dialog should be shown based on the state of unsaved data in the app.  Use a formula that can check variables and other properties, for example, the **Unsaved** property of form controls.

The confirmation dialog will be shown in any situation where data could be lost, including:
- Executing the [**Exit**](function-exit.md) function.
- If running the app on the web:
    - Closing the browser or browser tab.
- If running the app in a native player (iOS or Android):
    - Executing the [**Launch**](function-param.md) function.  When used on the web, **Launch** will open a new browser tab and no data would be lost.
    - Closing the native player.
    - Swiping left to switch to a different app.

The confirmation dialog will not be shown for Studio sessions.

### ConfirmExitMessage

**ConfirmExitMessage** is a text string property for a custom message to show in the confirmation dialog.  

The default is the generic message **You may have unsaved changes.** (in the language of the user).  This message is included in the confirmation dialog along with an action question (such as "Close this app?") and response buttons.  The look of the dialog may vary across players and versions of PowerApps.

The message will be truncated to fit within the confirmation dialog.  Keep the message to a few lines at most. 

### Example

Imagine your app contains two form controls named **AccountForm** and **ContactForm**.  To warn the user before closing when there are unsaved changes in either of these form controls set the **App** object's **ConfirmExit** property to `AccountForm.Unsaved Or ContactForm.Unsaved`.

![](media/object-app/confirm-native.png)

To give the user more information on which form is dirty, set the **App** object's **ConfirmExitMessage** property to `If( AccountsForm.Unsaved, "Accounts form has unsaved changes.", "Contacts form has unsaved changes." )`.  Assuming the **AccountForm** is not dirty but the **ContactForm** is:

![](media/object-app/confirm-native-custom.png) 



