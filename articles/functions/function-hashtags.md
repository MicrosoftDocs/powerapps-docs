<properties
	pageTitle="PowerApps: HashTags function"
	description="Reference information for the HashTags function in PowerApps, including syntax and examples"
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

# HashTags function in PowerApps #

Extracts the hashtags (#strings) from a string. 

## Description ##

The **HashTags** function scans a string for hashtags.  Hashtags start with a pound character (#) and are followed by any combination of: 

- upper and lowercase letters
- numerals
- underscores (_)
- currency symbols (such as $)

**HashTags** returns a one-column [table](working-with-tables.md) containing the hashtags found.  If no hashtags are found, the result will be a one-column table that is [empty](function-isblank-isempty.md).

## Syntax ##

**HashTags**( *String* )

- *String* - Required.  String to scan for hashtags.

## Examples ##

### Step by step ###

1. Add an input-text control, name it Tweet, and type this sentence into it:

	**This #app is #AMAZING and can #coUnt123 or #123abc but not #1-23 or #$*(#@")**

2. Add a vertical custom gallery, and set its **Items** property to this function:

	**HashTags(Tweet!Text)**

3. Add a label to the gallery template. 

4. The label shows these hashtags:

	- \#app
	- \#AMAZING
	- \#coUnt123
	- \#123abc
	- \#1

 

