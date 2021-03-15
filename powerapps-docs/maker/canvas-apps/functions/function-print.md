---
title: Patch function | Microsoft Docs
description: Reference information, including syntax and examples, for the Patch function in Power Apps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: nabuthuk
ms.date: 03/29/2021
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---

# Print function in Power Apps 

Opens the current screen in the default browser print dialog. 

## Description 

The print function allows you to take any screen and fit it to a page in order to print to a printer or save as PDF.  

The different configurations of the screen enable different printing outcomes. For fixed screens, they fit to the size of the page, for use of the screen templates/special sized screens, we will fit the content to the size of the print.  

## Syntax

**Print()**

### Examples

1. Go to [Power Apps](https://make.powerapps.com).
1. Select **Apps** from left navigation pane.
1. Select your app or create an app from scratch. 
1. Select **Insert** from the menu and then select **Button**.
1. From property list on top left, select **OnSelect**.
1. Enter the formula `Print()`. 
1. Save and publish the app.
1. Play the app.
1. Select the button that you added.  

The default browser will be opened in a new tab with the contents of the print.  

### Hide controls while printing 

To enable more customizable content, you are able to reference when the screen is printing in order to change properties of your app. For example, hiding buttons, or changing a form to view mode.  

### Use a screen template 

An easy way to get started is to  

Screen sizes for common prints

To build out a print for a specific size,  

## Known limitations

The **Print** function currently doesn't work on mobile devices. The default browser printers are the ones that will be available to print to.  

### See also

[Canvas app formula reference](../formula-reference.md)