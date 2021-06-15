---
title: Type Table in Microsoft Dataverse| Microsoft Docs
description: Learn how to use type table in Power Apps component framework
keywords:
ms.author: nabuthuk
manager: kvivek
ms.date: 04/01/2021
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
ms.assetid: 41ea27ac-65b6-45a4-ae03-5f8d02dfc67b
---

|Value |Description |
|--|--|
|Currency|Monetary values between -922,337,203,685,477 and 922,337,203,685,477 can be in this column. You can set a level of precision or choose to base the precision on a specific currency or a single standard precision used by the organization.|
|DateAndTime.DateAndTime|Displays date and time.|
|DateAndTime.DateOnly|Displays date only.|
|Decimal|Up to 10 decimal points of precision can be used for values between -100,000,000,000 and -100,000,000,000 can be in this column. You can specify the level of precision and the maximum and minimum values.|
|Enum|Enumerated data type.|
|FP|Up to 5 decimal points of precision can be used for values between -100,000,000,000 and -100,000,000,000 can be in this column. You can specify the level of precision and the maximum and minimum values. |
|Lookup.Simple|Allows for a single reference to a specific table. All custom lookups are this type.|
|Multiple|This column can contain up to 1,048,576 text characters. You can set the maximum length to be less than this. When you add this column to a form, you can specify the size of the column.|
|MultiSelectOptionSet|You can customize forms (main, quick create, and quick view) and email templates by adding choices columns. When you add choices column, you can specify multiple values that will be available for users to select. When users fill out the form they can select one, multiple, or all the values displayed in a drop-down list.|
|OptionSet|This column provides a set of options. Each option has a number value and label. When added to a form, this column displays a control for users to select only one option. |
|SingleLine.Email|This stores the string time in the format valid for Emails. Out-of-the-box Unified Interface controls automatically make them clickable links.|
|SingleLine.Phone|This stores the string time in the format valid for Phone. Out-of-the-box Unified Interface controls automatically make them clickable links.|
|SingleLine.Text|This option simply displays text.|
|SingleLine.TextArea|This format option can be used to display multiple lines of text. But with a limit of 4000 characters, the Multiple Lines of Text column is a better choice if large amounts of text are expected.|
|SingleLine.Ticker|This stores the string time in the format valid for Ticker. Out-of-the-box Unified Interface controls automatically make them clickable links.|
|SingleLine.URL|The text expected to provides a hyperlink to open the page specified. Out-of-the-box Unified Interface controls automatically prepend “https://” to input values that does not begin with a valid protocol . Only HTTP, HTTPS, FTP , FTPS, OneNote and TEL protocols are expected in this column. |
|TwoOptions|This column provides two options. Each option has a number value of 0 or 1 corresponding to a false or true value. Each option also has a label so that true or false values can be represented as "Yes" and "No", "Hot" and "Cold", "On" and "Off" or any pair of labels you want to display.|
|Whole.None|This option simply displays a number.|

## Value elements that are not supported

Following `of-type` property values are not supported currently:

|Value|Description|
|-----|-----|
|Whole.Duration|This format option can be used to display a list of duration options. But the data stored in the database is always a number of minutes. The column looks like a drop-down list and provides suggested options like 1 minute, 15 minutes, 30 minutes all the way up to 3 days. People can choose these options. However, people can also just type in a number of minutes and it resolves to that period of time.|
|Whole.TimeZone|This option displays a select list of time zones such as (GMT-12:00) International Date Line West and (GMT-08:00) Pacific Time (US & Canada). Each of these zones is stored as a number. For example, for the time zone (GMT-08:00) Pacific Time (US & Canada), the TimeZoneCode is 4. More information: [TimeZoneCode Class (Sdk Assembly)](/previous-versions/dynamics-crm4/developers-guide/bb959779(v=msdn.10))|
|Whole.Language|This option displays a list of the languages provisioned for your organization. The values are displayed as a drop-down list of language names, but the data is stored as a number using LCID codes. Language codes are four-digit or five-digit locale IDs. Valid locale ID values can be found at [Locale ID (LCID) Chart)](/previous-versions/windows/embedded/ms912047(v=winembedded.10)).|
|Lookup.Customer|Allows for a single reference to either an account or a contact record. These lookups are available for the Opportunity, Case, Quote, Order, and Invoice tables. These tables also have separate Account and Contact lookups that you can use if your customers are always one type. Or you can include both instead of using the Customer lookup.|
|Lookup.Owner|Allows for a single reference to either a team or a user record. All team or user-owned tables have one of these.|
|Lookup.PartyList|Allows for multiple references to multiple tables. These lookups are found on the Email table **To** and **Cc** columns. They're also used in the Phone and Appointment tables.|
|Lookup.Regarding|Allows for a single reference to multiple tables. These lookups are found in the regarding column used in activities.|
|Status|A system column that has options that generally correspond to active and inactive status. Some system columns have additional options, but all custom columns have only Active and Inactive status options.|
|Status Reason|A system column that has options that provide additional detail about the Status column. Each option is associated with one of the available Status options. You can add and edit the options.|