---
title: Enable and Disable functions | Microsoft Docs
description: Reference information, including syntax and examples, for the Enable and Disable functions in PowerApps
documentationcenter: na
author: gregli-msft
manager: kfile
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: reference
ms.component: canvas
ms.date: 11/07/2015
ms.author: gregli

---
# Enable and Disable functions in PowerApps
Turns a [signal](signals.md) on or off.

## Overview
Some signals can change often, requiring the app to recalculate as they do.  Rapid changes over a long period of time can drain a device's battery. You can use these functions to manually turn a signal on or off.

When a signal isn't being used, it's automatically turned off.

## Description
The **Enable** and **Disable** functions turn a signal on and off, respectively.

These functions currently only work for the **[Location](signals.md)** signal.

These functions have no return value. You can use them only in [behavior formulas](../working-with-formulas-in-depth.md).

## Syntax
**Enable**( *Signal* )<br>**Disable**( *Signal* )

* *Signal* - Required.  The signal to turn on or off.

