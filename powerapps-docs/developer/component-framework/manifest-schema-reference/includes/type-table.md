---
title: Type Table | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
manager: kvivek
ms.date: 04/23/2019
ms.service: "powerapps"
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
|`DateAndTime.DateAndTime`|Displays date and time.|
|`DateAndTime.DateOnly`|Displays date only.|
|`Decimal`|Up to 10 decimal points of precision can be used for values between -100,000,000,000 and -100,000,000,000 can be in this field. You can specify the level of precision and the maximum and minimum values.|
|`Enum`|Enumerated data type.|
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

## Value elements that are not supported

Following `of-type` attribute values are not supported currently:

|Value|Description|
|-----|------|
|`Whole.Duration`|This format option can be used to display a list of duration options. But the data stored in the database is always a number of minutes. The field looks like a drop-down list and provides suggested options like 1 minute, 15 minutes, 30 minutes all the way up to 3 days. People can choose these options. However, people can also just type in a number of minutes and it resolves to that period of time.|
|`Whole.Timezone`|This option displays a select list of time zones such as (GMT-12:00) International Date Line West and (GMT-08:00) Pacific Time (US & Canada). Each of these zones is stored as a number. For example, for the time zone (GMT-08:00) Pacific Time (US & Canada), the TimeZoneCode is 4. More information: [TimeZoneCode Class (Sdk Assembly)](https://docs.microsoft.com/en-us/previous-versions/dynamics-crm4/developers-guide/bb959779(v=msdn.10))|
|`Whole.Language`|This option displays a list of the languages provisioned for your organization. The values are displayed as a drop-down list of language names, but the data is stored as a number using LCID codes. Language codes are four-digit or five-digit locale IDs. Valid locale ID values can be found at [Locale ID (LCID) Chart)](https://docs.microsoft.com/en-us/previous-versions/windows/embedded/ms912047(v=winembedded.10)).|
|`Lookup.Simple`|Allows for a single reference to a specific entity. All custom lookups are this type.|
|`Lookup.Customer`|Allows for a single reference to either an account or a contact record. These lookups are available for the Opportunity, Case, Quote, Order, and Invoice entities. These entities also have separate Account and Contact lookups that you can use if your customers are always one type. Or you can include both instead of using the Customer lookup.|
|`Lookup.Owner`|Allows for a single reference to either a team or a user record. All team or user-owned entities have one of these.|
|`Lookup.PartyList`|Allows for multiple references to multiple entities. These lookups are found on the Email entity **To** and **Cc** fields. They’re also used in the Phone and Appointment entities.|
|`Lookup.Regarding`|Allows for a single reference to multiple entities. These lookups are found in the regarding field used in activities.|
|`MultiSelectOptionSet`|You can customize forms (main, quick create, and quick view) and email templates by adding multi-select fields. When you add a Multi-Select Option Set field, you can specify multiple values that will be available for users to select. When users fill out the form they can select one, multiple, or all the values displayed in a drop-down list.|
