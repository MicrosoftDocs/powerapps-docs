---
title: HashTags function in Power Apps
description: Reference information including syntax and examples for the HashTags function in Power Apps.
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: nabuthuk
ms.date: 11/07/2015
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# HashTags function in Power Apps
Extracts the hashtags (#strings) from a string of text.

## Description
The **HashTags** function scans a string for hashtags. Hashtags start with a pound character (#), which is followed by any combination of:

* uppercase and lowercase letters
* numerals
* underscores
* currency symbols (such as $)

**HashTags** returns a one-column [table](../working-with-tables.md) that contains the hashtags in the string.  If the string contains no hashtags, the function returns a one-column table that's [empty](function-isblank-isempty.md).

## Syntax
**HashTags**( *String* )

* *String* - Required.  String to scan for hashtags.

## Examples
### Step by step
1. Add a **[Text input](../controls/control-text-input.md)** control, name it **Tweet**, and type this sentence into it:
   
    **This #app is #AMAZING and can #coUnt123 or #123abc but not #1-23 or #$\*(#\@")**
2. Add a vertical custom gallery, and set its **[Items](../controls/properties-core.md)** property to this function:
   
    **HashTags(Tweet.Text)**
3. Add a **[Label](../controls/control-text-box.md)** control to the gallery template.
   
    The gallery shows these hashtags:
   
   * **\#app**
   * **\#AMAZING**
   * **\#coUnt123**
   * **\#123abc**
   * **\#1**



[!INCLUDE[footer-include](../../../includes/footer-banner.md)]