---
title: App object | Microsoft Docs
description: Reference information, including syntax and examples, for the App object in PowerApps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: anneta
ms.date: 05/29/2019
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

It returns a screen object, which you can use to reference properties of the screen or compare to another screen to determine which screen is displayed.  You can also retrieve the name of the currently displayed screen with **App.ActiveScreen.Name**.

Use the **[Back](function-navigate.md)** or **[Navigate](function-navigate.md)** functions to change the displayed screen.

## OnStart property
The **OnStart** property is executed when the user starts the app. 

This property is commonly used to retrieve and cache data into collections with the **[Collect](function-clear-collect-clearcollect.md)** function, set up global variables with the **[Set](function-set.md)** function, and navigate to an initial screen with the **[Navigate](function-navigate.md)** function. 

This formula is evaluated before the first screen appears. No screen is loaded, so you can't set context variables with the **[UpdateContext](function-updatecontext.md)** function. However, you can pass context variables with the **Navigate** function.  

After you change the **OnStart** property, you can test it by hovering over the **App** object in the left navigation pane, selecting the ellipsis (...) that appears, and then selecting **Run OnStart**. Unlike when the app is loaded for the first time, existing collections and variables will already be set. Use the **[ClearCollect](function-clear-collect-clearcollect.md)** function instead of the **Collect** function to start with empty collections.

 ![App item context menu with Run OnStart](media/object-app/appobject-runonstart.png)

## ConfirmExit properties

Nobody wants to lose unsaved changes.  Use the **ConfirmExit** and **ConfirmExitMessage** properties to warn the user before they close your app.

> [!NOTE]
> **ConfirmExit** does not work in embedded scenarios such as Power BI or SharePoint.

### ConfirmExit

**ConfirmExit** is a Boolean property that when *true* causes a confirmation dialog to be shown before closing the app.  The default for this property is *false* and no confirmation dialog is shown.

Use this property to show a confirmation dialog if there is any unsaved data in the app.  Use a formula that can check variables and control properties, for example, the **Unsaved** property of form controls.

The confirmation dialog will be shown in any situation where data could be lost, including:
- Executing the [**Exit**](function-exit.md) function.
- If running the app on the web:
    - Closing the browser or browser tab.
    - Selecting the back button in the browser.
- If running the app in a native player (iOS or Android):
    - Executing the [**Launch**](function-param.md) function.  This not true when running in the web player described above since **Launch** will open a new browser tab and no data would be lost.
    - Closing the native player.
    - Swiping to switch to a different app.
    - Selecting the back button on the device (Android only).

The exact look of the confirmation dialog may vary across players and versions of PowerApps.  

The confirmation dialog will not be shown when authoring in Studio.

### ConfirmExitMessage

By default, the confirmation dialog will display a generic message such as **"You may have unsaved changes."** in the language of the user.  

Use **ConfirmExitMessage** to provide a custom message in the confirmation dialog.  If this property is *blank*, the default will be used.  The message will be truncated to fit within the confirmation dialog; keep the message to a few lines at most. 

In some cases when used in a browser, the confirmation dialog will appear but **ConfirmExitMessage** cannot be honored because the browser will override with its own generic message.

### Example

Imagine your app contains two form controls named **AccountForm** and **ContactForm**.  To warn the user before closing when there are unsaved changes in either of these form controls set the **App** object's **ConfirmExit** property to the formula:

```powerapps-dot
AccountForm.Unsaved Or ContactForm.Unsaved
```

When the user closes their app on a phone, this confirmation dialog will appear:

![](media/object-app/confirm-native.png)

To give the user more actionable information about which form is dirty, set the **App** object's **ConfirmExitMessage** property to the formula:

```powerapps-dot
If( AccountsForm.Unsaved, 
    "Accounts form has unsaved changes.", 
    "Contacts form has unsaved changes." 
)
```

Assuming the **AccountForm** is dirty, the user will see this confirmation dialog:

![](media/object-app/confirm-native-custom.png) 



