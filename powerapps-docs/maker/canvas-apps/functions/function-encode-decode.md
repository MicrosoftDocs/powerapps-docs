---
title: EncodeUrl and PlainText functions in Power Apps
description: Reference information including syntax and examples for the EncodeUrl and PlainText functions in Power Apps.
author: gregli-msft
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 11/07/2015
ms.subservice: canvas-maker
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - gregli-msft
  - nkrb
---
# EncodeUrl and PlainText functions in Power Apps
Encodes and decodes strings.

## Description
The **EncodeUrl** function encodes a URL string, replacing certain non-alphanumeric characters with % and a hexadecimal number.  

The **PlainText** function removes HTML and XML tags, converting certain tags such as these to an appropriate symbol:

* **&amp;nbsp;**
* **&amp;quot;**

The return value from these functions is the encoded or decoded string. This function doesn't remove all HTML and XML tags. 

## Syntax
**EncodeUrl**( *String* )

* *String* - Required.  URL to be encoded.

**PlainText**( *String* )

* *String* - Required. String from which HTML and XML tags will be stripped.

## Examples
If you show an RSS feed in a text gallery and then set the **[Text](../controls/properties-core.md)** property of a label in that gallery to **ThisItem.description**, the label might show raw HTML or XML code as in this example:

```html
    <p>We have done an unusually&nbsp;&quot;deep&quot; globalization and localization.</p>
```

If you set the **[Text](../controls/properties-core.md)** property of the label to **PlainText(ThisItem.description)**, the text appears as in this example:

```
    We have done an unusually "deep" globalization and localization.
```

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]