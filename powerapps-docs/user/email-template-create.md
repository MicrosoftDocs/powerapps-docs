---
title: "How to create an email template  in model-driven apps | MicrosoftDocs"
description: Learn how to create an email template.
author: mduelae
manager: kvivek

ms.component: pa-user
ms.topic: conceptual
ms.date: 6/30/2021
ms.subservice: end-user
ms.author: mkaur
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---

# Create email templates

Email templates are a fast and easy way to send consistent, professional, preformatted email messages to your customers.

To create a template, select **New** on the **Email Templates** command bar. You can [start with a blank template](#start-with-a-blank-template) or [customize an existing template](#start-with-existing-templates).

:::image type="content" source="media/email-how-to-create-an-email-template-1a.png" alt-text="Screenshot that shows options to create a template from blank or from an existing template.":::

## Start with a blank template

When you start with a blank template, nothing is provided for you. You must add everything you want customers to see.

Specify the following information:

:::image type="content" source="media/email-create-an-email-template-1a.png" alt-text="Screenshot of template information to provide.":::

   1. **Template name**: Give your email template a detailed name to help you identify it later.
   2. **Permission level**: Select **Organization** to share your template with others or **Individual** for personal use.
   3. **Category**: The default value is **User**. Categories determine which dynamic text fields are available for use in your template.
   4. **Language**: Display installed language packs. **Language** also helps to categorize your templates.
   5. **Create**: Opens one of two editors where you can build your template.

When you select **Create**, the editor page you see depends on whether your administrator has turned on the [enhanced email template editor option](cs_email_template_builder.md):

- If yes, you'll use the enhanced email template editor page.
- If not, you'll use the default email template editor page.

### Enhanced email template editor overview

:::image type="content" source="media/email-template-enh.png" alt-text="Screenshot of the enhanced email template editor with a blank template open for editing.":::

- **Editor** tab: [Design and customize the email template](cs-template-options.md).
- **Template** tab: Specify or change the template details and the email subject.
- **Attachments** tab: Add attachments to your template if needed.

### Default email template editor overview

:::image type="content" source="media/email-new-customer-template-1c.png" alt-text="Screenshot of the default email template editor with a blank template open for editing.":::

   1. **Insert dynamic text**: Use dynamic text in the subject and body of the email.
   2. **Subject**: Enter or change the email subject.
   3. **New Attachment**: Add one or more attachments to your template, if needed.

## Start with existing templates

Start with an existing template to create an email template faster and with less effort. The template is pre-populated with data. All you need to do is customize it for your needs.

:::image type="content" source="media/email-start-with-existing-templates-1a.png" alt-text="Screenshot that shows existing email templates to start from.":::

   1. **Search**: Search for the name of a template to start from. Search doesn't support regular expressions.
   2. **Browse** out-of-the-box templates, global and entity-specific, listed in alphabetical order. Global templates are shown as the type User. If you've created custom email templates, they're also listed.
   3. **Details**. Preview the templates so that you can pick the one that best meets your needs. You can modify it as needed later.
   4. **Select**: Insert the selected template content into your email.

> [!Important]
> If you create templates in the enhanced editing environment, don't edit them in the legacy web client. You'll lose any inline images and strip out some of the advanced formatting and functionality.

### Work with existing templates

:::image type="content" source="media/email-template-copy-1a.png" alt-text="Screenshot of the email template editor with an existing template open for editing.":::

- **Template** tab: Specify or change the template details and the email subject. The name includes **– Copy** at the end to identify this template is a copy of another one.
- **Template editor** section: [Design and customize the email template](cs-template-options.md).
- Select **New Attachment** to add attachments to your template if needed.

### See also

[Set up enhanced email](/power-platform/admin/system-settings-dialog-box-email-tab)<br>
[Understand the email experience](view-create-email.md)   
