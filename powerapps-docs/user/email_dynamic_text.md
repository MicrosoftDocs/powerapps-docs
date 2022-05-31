---
title: "Use the Insert dynamic text option | MicrosoftDocs"
description: "Personalize emails using the Insert dynamic text option"
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


# Personalize emails with dynamic text

Dynamic text enables you to personalize email content. **Insert dynamic text** option allows you to update an email with the dynamic value of an entity. For example, rather than using a generic greeting like “Dear customer,” you can use the dynamic text, (“Dear ``{!Case:Customer;}``”). On sending the message, the dynamic text is replaced with the customer's name (“Dear John”).

## Insert dynamic text

You can insert dynamic fields in the existing email templates or newly created email templates. Select **Insert dynamic text** in the email template editor to add dynamic text to your template.

On the **Edit dynamic text** select the **Record type** and **Field name**. The options displayed in **Field name** are default fields and are based on the **Record type**. 

The **Record type** options are determined by the **Category** you specify when you are creating the email template.

## Insert dynamic values from custom entities

If you must insert fields from custom entities in the templates, use the following syntax:

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

For example, if you want to add a custom  field, Customer id, that is linked to the Record type user to the template, you can insert this syntax: ``{{!User:Customerid;}}`` in the editor.

So when the email is sent out, the dynamic text is replaced with the user's customer  id.
