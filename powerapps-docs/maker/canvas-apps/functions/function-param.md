---
title: Download, Launch, and Param functions | Microsoft Docs
description: Reference information, including syntax and examples, for the Download, Launch, and Param functions in PowerApps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: anneta
ms.date: 11/07/2015
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Download, Launch, and Param functions in PowerApps
Downloads or launches a webpage or an app with parameters.  

## Description
The **Download** function downloads a file from the web to the local device.  The user is prompted for a location to save the file.  **Download** returns the location where the file was stored locally as a string.  

The **Launch** function launches a webpage or an app.  Optionally, this function can pass parameters to the app.  

The **Param** function retrieves a parameter passed to the app when it was launched.  If the named parameter wasn't passed, **Param** returns *blank*.

## Syntax
**Download**( *Address* )

* *Address* - Required.  The address of a web resource to download.

**Launch**( *Address* [, *ParameterName1*, *ParameterValue1*, ... ] )

* *Address* - Required.  The address of a webpage or the ID of an app to launch.
* *ParameterName(s)* - Optional.  Parameter name.
* *ParameterValue(s)* - Optional.  Corresponding parameter values to pass to the app or the webpage.

**Param**( *ParameterName* )

* *ParameterName* - Required.  The name of the parameter passed to the app.

