---
title: Personalize emails with dynamic text
description: Personalize your customer engagement emails with dynamic text in Power Apps.
ms.custom: ""
author: gandhamm
manager: shujoshi
ms.topic: task
ms.date: 06/09/2022
ms.subservice: end-user
ms.author: mgandham
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---

# Personalize emails with dynamic text

Generic greetings like "Dear customer" make customers less likely to engage with your emails. Personalize your outreach instead with dynamic text in your email templates.

Dynamic text replaces a placeholder entity with the value of the entity when you send the email. For example, your email template might contain "Dear {!User:First Name;}" but your customer sees “Dear Sal.”

## Insert dynamic text

You can insert dynamic text in existing email templates or templates that you create.

1. In the template editor, place your cursor where you want the personalized content to appear.

1. Select **Insert dynamic text**.

    :::image type="content" source="media/email_dyn_text.png" alt-text="Screenshot of the email template editor, with Insert dynamic text highlighted.":::

1. Select the **Record type** and **Field name**.

    The category that you specified when you created the email template determines the record types you can choose. The record type you choose determines the fields you can select.

    :::image type="content" source="media/email_dyn_text_fields.png" alt-text="Screenshot of the Edit dynamic text pane, with Record type and Field name highlighted.":::

## Insert custom fields

Dynamic text isn't limited to what you can insert by selecting a record type and field. You can also insert fields from custom entities by typing them directly in your email template.

Use the following syntax:

| Field Type | Syntax |
| --- | --- |
| Single line of text  
 Currency | {!EntityLogicalName:FieldLogicalName;} |
| Lookup | {!EntityLogicalName:FieldLogicalName/@name;} |
| Date  | {!EntityLogicalName:FieldLogicalName/@date;} |
| Time | {!EntityLogicalName:FieldLogicalName/@time;} |
| Currency | {!EntityLogicalName:FieldLogicalName;} |
| Decimal number | {!EntityLogicalName:FieldLogicalName;} |
| Floating number  | {!EntityLogicalName:FieldLogicalName;} |
| Multiple lines of text | {!EntityLogicalName:FieldLogicalName;} |
| Multi-select option set | {!EntityLogicalName:FieldLogicalName/@name;} |
| Option set | {!EntityLogicalName:FieldLogicalName/@name;} |
| Two options | {!EntityLogicalName:FieldLogicalName/@name;} |


For example, let's say you want to insert a custom field, *CustomerId*, that's linked to the record type *User*. Type the following placeholder in your template: ``{{!User:CustomerId;}}``

### See also

[How to create an email template in model-driven apps](email-template-create.md)  
[Enable the enhanced email template editor page](cs-email-template-builder.md)

[!INCLUDE[footer-include](../includes/footer-banner.md)]
