<properties
	pageTitle="Language function | Microsoft PowerApps"
	description="Reference information, including syntax and examples, for the Language function in PowerApps"
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

Returns the language of the app.

## Description ##
For an app that has been saved to powerapps.com, this function returns the language with which the app was branded when it was saved.

For an app that's new or has only been saved locally, this function returns the currently active language from the language preferences. If you change the language preference while PowerApps is open, you must restart it for the function to reflect the change.

## Syntax ##

**Language**()

## Example ##

**Language()** could return "en-US" based on your configuration.
