<properties
	pageTitle="PowerApps: Launch and Param functions"
	description="Reference information for the Param functions in PowerApps, including syntax and examples"
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

Launches a web address or app with parameters.  

## Description ##

The **Launch** function launches a web address or app.  Optionally, it can pass parameters to the app.  

The **Param** function retrieves a parameter passed to the app when it was launched.  If the named parameter was not passed, **Param** returns *blank*.

## Syntax ##

**Launch**( *Address* [, *ParameterName1*, *ParameterValue1*, ... ] )

- *Address* - Required.  A web address or App ID to launch.

- *ParameterName(s)* - Optional.  Parameter name.

- *ParameterValue(s)* - Optional.  Corresponding parameter values to pass to the app or web site.

**Param**( *ParameterName* )

- *ParameterName* - Required.  The name of the parameter passed to the app.
