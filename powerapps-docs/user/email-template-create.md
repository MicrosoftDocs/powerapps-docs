---
title: "How to create an email template  in model-driven apps | MicrosoftDocs"
description: Learn how to create an email template.
author: sericks007

ms.component: pa-user
ms.topic: conceptual
ms.date: 04/01/2023
ms.subservice: end-user
ms.author: sericks
ms.custom: ""
ms.reviewer: sericks
ms.assetid: 
search.audienceType: 
  - enduser
---

# Create email templates

Email templates are a fast and easy way to send consistent, professional, preformatted email messages to your customers. To create email templates, the legacy email template editor is available by default. However, the enhanced email template editor is displayed as a choice if it is enabled by your administrator.

You can create email templates by using one of the following options:  
- **Start with a blank template**: Create a template from scratch. The editor that's displayed depends on wether the enhanced email template editor option is enabled.
- **Start with an existing template** : Create a template by choosing an existing template. The editor that's displayed depends on the editor in which the existing template was created.

:::image type="content" source="media/email-how-to-create-an-email-template-1a.png" alt-text="Screenshot that shows options to create a template from blank or from an existing template.":::

## Start with a blank template

When you start with a blank template, nothing is provided for you. You must add everything you want customers to see. 

1. On the **Email Templates** command bar, select **New**, and then select **Start with a blank template**.

3. Enter the following details:
   - **Template name**: Give your email template a detailed name to help you identify it later.
   - **Permission level**: Select **Organization** to share your template with others or **Individual** for personal use.
   - **Category**: The default value is **User**. Categories determine which dynamic text fields are available for use in your template.
   - **Language**: Display installed language packs. **Language** also helps to categorize your templates.
   - **Create**: Opens one of two editors where you can build your template.
 
       :::image type="content" source="media/email-create-an-email-template-1a.png" alt-text="Screenshot that shows blank template page."::: 
 
3. Select **Create**. The template editor is displayed.

The editor page you see depends on whether your administrator has turned on the enhanced email template editor option:

- If yes, you'll use the enhanced email template editor page.
- If not, you'll use the email template editor page. 

## Start with existing templates

Start with an existing template to create an email template faster and with less effort. The template is pre-populated with data. All you need to do is customize it for your needs.

1. On the **Email Templates** command bar, select **New**, and then select **Start with existing templates**.
2. Enter the following details:
   - **Search**: Search for the name of a template to start from. Search doesn't support regular expressions.
   - **Browse** out-of-the-box templates, global and entity-specific, listed in alphabetical order. Global templates are shown as the type User. If you've created custom email templates, they're also listed.
   - **Details**. Preview the templates so that you can pick the one that best meets your needs. You can modify it as needed later.
  
       :::image type="content" source="media/email-start-with-existing-templates-1a.png" alt-text="Screenshot that shows existing email templates to start from.":::
  
3. The template editor page is displayed.

When you create a template from an existing template, irrespective of the enhanced email template editor option setting, the app displays the newly-created email template in one of the following template editors:
  - Enhanced email template: If the selected email template was created with the enhanced email template.
  - Email template: If the selected template was created with the legacy email template.

> [!Important]
> If you create templates in the enhanced editing environment, don't edit them in the legacy web client. You'll lose any inline images and strip out some of the advanced formatting and functionality.

### Work with existing templates

:::image type="content" source="media/email-template-copy-1a.png" alt-text="Screenshot of the email template editor with an existing template open for editing.":::

- **Template** tab: Specify or change the template details and the email subject. The name includes **– Copy** at the end to identify this template is a copy of another one.
- **Template editor** section: [Design and customize the email template](cs-template-options.md).
- Select **New Attachment** to add attachments to your template if needed.


## Email template editor

You can use either the enhanced email template editor or the legacy email template editor to create email templates.

### Enhanced email template editor
 
The enhanced email template editor is displayed if the enhanced email template editor option is enabled. However, for Customer Service workspace and Customer Service Hub apps, the enhanced email template editor is displayed by default. More information: [Enhanced email template editor option](cs-email-template-builder.md) 

:::image type="content" source="media/email-template-enh.png" alt-text="Screenshot of the enhanced email template editor with a blank template open for editing.":::

- **Editor** tab: Use this tab to design and customize your email template. See: [Design and customize the email template](cs-template-options.md).
- **Template** tab: Specify or change the template details and the email subject.
- **Attachments** tab: Add attachments to your template if needed.

### Email template editor

The email template editor is displayed if the enhanced email template editor option is disabled. 

:::image type="content" source="media/email-new-customer-template-1c.png" alt-text="Screenshot of the default email template editor with a blank template open for editing.":::

   1. **Insert dynamic text**: Use dynamic text in the subject and body of the email.
   2. **Subject**: Enter or change the email subject.
   3. **New Attachment**: Add one or more attachments to your template, if needed.

### See also

[Personalize content with Insert dynamic text](email-dynamic-text.md)<br>
[Set up enhanced email](/power-platform/admin/system-settings-dialog-box-email-tab)<br>
[Understand the email experience](view-create-email.md)   
