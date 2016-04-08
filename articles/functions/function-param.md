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

Launches a webpage or an app with parameters.  

## Description ##

The **Launch** function launches a webpage or an app.  Optionally, this function can pass parameters to the app.  

The **Param** function retrieves a parameter passed to the app when it was launched.  If the named parameter wasn't passed, **Param** returns *blank*.

## Syntax ##

**Launch**( *Address* [, *ParameterName1*, *ParameterValue1*, ... ] )

- *Address* - Required.  The address of a webpage or the ID of an app to launch.

- *ParameterName(s)* - Optional.  Parameter name.

- *ParameterValue(s)* - Optional.  Corresponding parameter values to pass to the app or the webpage.

**Param**( *ParameterName* )

- *ParameterName* - Required.  The name of the parameter passed to the app.
