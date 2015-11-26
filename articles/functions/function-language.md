<properties
	pageTitle="PowerApps: Language function"
	description="Reference information for the Language function in PowerApps, including syntax and examples"
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
   ms.date="11/01/2015"
   ms.author="gregli"/>

# Language function in PowerApps #

Access to the language used by the app.

## Description ##

The **Language** function returns the language of the app.  

For an app that has been saved to the PowerApps portal, this function returns the language with which the app was branded when it was saved.

For an app that is new or has only been saved locally, this function returns the currently active language from the language preferences. If you change the language preference while the PowerApps client is open, you must restart for the function to reflect the change.

## Syntax ##

**Language**()

## Examples ##

**Language()** could return "en-US" based on your configuration.


