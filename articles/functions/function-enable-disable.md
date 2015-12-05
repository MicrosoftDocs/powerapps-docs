<properties
	pageTitle="PowerApps: Enable and Disable functions"
	description="Reference information for the Enable and Disable functions in PowerApps, including syntax and examples"
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="gregli-msft"
	manager="dwrede"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="11/07/2015"
   ms.author="gregli"/>

# Enable and Disable functions in PowerApps #

Turns a [signal](signals.md) on or off.

## Overview ##

Some signals can change often, requiring the app to recalculate as they do.  Rapid changes over a long period of time can drain a device's battery.  These functions enable an author to manually turn on or off a signal.

When a signal is not being used, it is automatically turned off.

## Description ##

The **Enable** and **Disable** functions turn on and off a signal, respectively.

These functions currently only work for the **[Location](signals.md)** signal.

These functions have no return value.  They can only be used in [behavior formulas](working-with-formulas-in-depth.md#behavior-formulas).

## Syntax ##

**Enable**( *Signal* )<br>**Disable**( *Signal* )

- *Signal* - Required.  The signal to turn on or off.

