---
title: ShowError function | Microsoft Docs
description: Reference information, including syntax and examples, for the ShowError function in PowerApps
services: ''
suite: powerapps
documentationcenter: na
author: gregli-msft
manager: anneta
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/21/2018
ms.author: gregli

---
# ShowError function in PowerApps
Displays an error to the user.

## Description
The **ShowError** function displays an error to the user.  Messages are shown both when authoring your app and when end users are using your app.

**ShowError** can only be used in [behavior formulas](../working-with-formulas-in-depth.md).

**ShowError** always returns *true*.

**ShowError** can be paired with the [**IfError**](function-iferror.md) function to detect and report errors with a custom error message.

## Syntax
**ShowError**( *Message* )

* *Message* - Required.  Message to display to the user. 

## Examples

### Step by step

1. Add a **Button** control to your screen.

2. Set the **OnSelect** property of the **Button** to:

	**ShowError( "Hello, World" )**

3. Click or press the button.  

	Each time the button is clicked, the message **Hello, World** is displayed to the user.

	![In the authoring environment, showing Button.OnSelect calling ShowError and displaying the resuling Hello, World message as a red banner message for the user](media/function-showerror/hello-world.png)
