---
title: EncodeUrl and PlainText functions | Microsoft Docs
description: Reference information, including syntax and examples, for the EncodeUrl and PlainText functions in PowerApps
services: ''
suite: powerapps
documentationcenter: na
author: gregli-msft
manager: anneta
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 11/07/2015
ms.author: gregli

---
# EncodeUrl and PlainText functions in PowerApps
Encodes and decodes strings.

## Description
The **EncodeUrl** function encodes a URL string, replacing non-alphanumeric characters with % and a hexadecimal number.  

The **PlainText** function removes HTML and XML tags, converting tags such as these to an appropriate symbol:

* **&amp;nbsp;**
* **&amp;quot;**

The return value from these functions is the encoded or decoded string.   

## Syntax
**EncodeUrl**( *String* )

* *String* - Required.  URL to be encoded.

**PlainText**( *String* )

* *String* - Required. String from which HTML and XML tags will be stripped.

## Examples
If you show an RSS feed in a text gallery and then set the **[Text](../maker/controls/properties-core.md)** property of a label in that gallery to **ThisItem.description**, the label might show raw HTML or XML code as in this example:

    <p>We have done an unusually&nbsp;&quot;deep&quot; globalization and localization.<p>

If you set the **[Text](../maker/controls/properties-core.md)** property of the label to **PlainText(ThisItem.description)**, the text appears as in this example:

    We have done an unusually "deep" globalization and localization.
