---
title: Type Table | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
manager: jdaly
ms.date: 06/4/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
ms.assetid: 41ea27ac-65b6-45a4-ae03-5f8d02dfc67b
---

|Value|Description|
|--|--|
|`Currency`|Monetary values between -922,337,203,685,477 and 922,337,203,685,477 can be in this field. You can set a level of precision or choose to base the precision on a specific currency or a single standard precision used by the organization.|
|`DateAndTime.DateAndTime`|Placeholder description for type.DateAndTime.DateAndTime|
|`DateAndTime.DateOnly`|Placeholder description for type.DateAndTime.DateOnly|
|`Decimal`|Up to 10 decimal points of precision can be used for values between -100,000,000,000 and -100,000,000,000 can be in this field. You can specify the level of precision and the maximum and minimum values.|
|`Enum`|Placeholder description for type.Enum|
|`FP`|Up to 5 decimal points of precision can be used for values between -100,000,000,000 and -100,000,000,000 can be in this field. You can specify the level of precision and the maximum and minimum values. |
|`Multiple`|This field can contain up to 1,048,576 text characters. You can set the maximum length to be less than this. When you add this field to a form, you can specify the size of the field.|
|`OptionSet`|This field provides a set of options. Each option has a number value and label. When added to a form, this field displays a control for users to select only one option. |
|`SingleLine.Email`|The text provides a mailto link to open the user’s email application.|
|`SingleLine.Phone`|In the web application, fields will be click-enabled to initiate calls using either Skype or Lync if a client for either is installed on your computer. The telephony provider choice is at the bottom of the General tab of System Settings.For Dynamics 365 for tablets, Skype is the only available telephony provider.|
|`SingleLine.Text`|This option simply displays text.|
|`SingleLine.TextArea`|This format option can be used to display multiple lines of text. But with a limit of 4000 characters, the Multiple Lines of Text field is a better choice if large amounts of text are expected.|
|`SingleLine.Ticker`|For most languages, the text will be enabled as a link to open the MSN Money website to show details about the stock price represented by the ticker symbol.For certain East Asian languages the window will open Bing search results for the ticker symbol.|
|`SingleLine.URL`|The text provides a hyperlink to open the page specified. Any text that does not begin with a valid protocol will have “http://” prepended to it.Only HTTP, HTTPS, FTP , FTPS, ONENOTE and TEL protocols are allowed in this field.|
|`TwoOptions`|This field provides two options. Each option has a number value of 0 or 1 corresponding to a false or true value. Each option also has a label so that true or false values can be represented as “Yes” and “No”, “Hot” and “Cold”, “On” and “Off” or any pair of labels you want to display.|
|`Whole.None`|This option simply displays a number.|
