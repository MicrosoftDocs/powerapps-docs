<properties
	pageTitle="Launch and Param functions | Microsoft PowerApps"
	description="Reference information, including syntax and examples, for the Launch and Param functions in PowerApps"
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

# Launch and Param functions in PowerApps #

Launches or downloads a webpage or an app with parameters.  

## Description ##

The **Launch** function launches a webpage or an app.  Optionally, this function can pass parameters to the app.  

The optional *LaunchAction* parameter controls how the webpage or app is launched, and has these values:

| LaunchAction | Description |
|------------|-------------|
| LaunchAction.Open | Opens the web page or app.  This is the default if LaunchAction is not supplied. |
| LaunchAction.Download | Downloads the web page to the local device.  The user is prompted for a location to save the file.
| LaunchAction.DownloadAndOpen | Downloads the web page to the local device.  The user is promoted for a location to save the file.  After downloading, the file is opened. |

The **Param** function retrieves a parameter passed to the app when it was launched.  If the named parameter wasn't passed, **Param** returns *blank*.

## Syntax ##

**Launch**( *Address* [, *ParameterName1*, *ParameterValue1*, ... ] [, *LaunchAction* ] )

- *Address* - Required.  The address of a webpage or the ID of an app to launch.

- *ParameterName(s)* - Optional.  Parameter name.

- *ParameterValue(s)* - Optional.  Corresponding parameter values to pass to the app or the webpage.

- *LaunchAction* - Optional.  Action to take.  Default is *Open*, which opens the *Address* as a webpage or app.    

**Param**( *ParameterName* )

- *ParameterName* - Required.  The name of the parameter passed to the app.
