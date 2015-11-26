<properties
	pageTitle="PowerApps: EncodeUrl and PlainText functions"
	description="Reference information for the EncodeUrl and PlainText functions in PowerApps, including syntax and examples"
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

# EncodeUrl and PlainText functions in PowerApps #

Encodes and decodes strings.

## Description ##

The **EncodeUrl** function URL encodes a string.  Non-alphanumeric characters are replaced with % and a hexadecimal number.  

The **PlainText** function removes HTML and XML tags, converting some tags to an appropriate symbol.  Converted tags include &amp;nbsp; and &amp;quot;.

The return value from these functions is the encoded or decoded string.   

## Syntax ##

**EncodeUrl**( *String* )

- *String* - Required.  String to be URL encoded.

**PlainText**( *String* )

- *String* - Required.  String to strip of HTML and XML tags.

## Examples ##

If you bind a text gallery to an RSS feed and then set the **Text** property of a label in that gallery to **ThisItem!description**, the label might show raw HTML or XML code as in this example:

	<p>We have done an unusually&nbsp;&quot;deep&quot; globalization and localization.<p>

If you set the Text property of the label to **PlainText(ThisItem!description)**, the text appears as in this example:

	We have done an unusually "deep" globalization and localization.

