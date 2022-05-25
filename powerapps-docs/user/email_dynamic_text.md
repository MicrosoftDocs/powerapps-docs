---
title: "Configure the enhanced insert email template selection window | MicrosoftDocs"
description: "Configure the email template selection window at the org level or app."
ms.custom: ""
author: gandhamm
manager: shujoshi
ms.topic: task
ms.date: 05/06/2022
ms.subservice: end-user
ms.author: mgandham
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---


# Introduction

Dynamic text enables you to personalize content. Insert dynamic text placeholders in an email template to automatically replace the recepients' personal details when a message is sent. For example, rather than using a generic greeting like “Dear customer,” you can use dynamic text (“Dear ``{{FirstName}}``”) that is replaced with the customer name (“Dear John”) upon sending the message.

## Insert dynamic text

You can insert dynamic fields for existing email templates or newly created email templates. Select **Insert dynamic text** in the email template editor to add dynamic text to your template.

On the **Edit dynamic text** select the **Record type** and **Field name**. The options displayed in **Field name** are default fields and are based on the **Category** you specify when creating the email template.

## Insert custom fields

If you must insert custom fields in the templates, use the following syntax:

|Field Type  |Syntax  |
|----------|-----------|
|Single Line of Text |{!EntityLogicalName:FieldLogicalName;} |
|Lookup|{!EntityLogicalName:FieldLogicalName/@name;} |
|Date|{!EntityLogicalName:FieldLogicalName/@date;} |
|Time|{!EntityLogicalName:FieldLogicalName/@time;} |
|Currency |{!EntityLogicalName:FieldLogicalName;} |
|Decimal Number |{!EntityLogicalName:FieldLogicalName;} |
|Floating Number|{!EntityLogicalName:FieldLogicalName;} |
|Multiline Line of Text |{!EntityLogicalName:FieldLogicalName;} |
|Multi select option set|{!EntityLogicalName:FieldLogicalName/@name;} |
|Option Set |{!EntityLogicalName:FieldLogicalName/@name;} |
|Two options |{!EntityLogicalName:FieldLogicalName/@name;} |

For example, if you want to add a custom  field, Value in dollars, to the template, you can insert this syntax: ``{{!EntityLogicalName:Value in dollars;}}`` in the editor.
