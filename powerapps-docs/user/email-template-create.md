---
title: "How to create an email template  in model-driven apps | MicrosoftDocs"
description: Learn how to create an email template.
author: mduelae
manager: kvivek
ms.service: powerapps
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

Email templates are a fast and easy way to send repetitive and recurring email to multiple customers. They can help save you time and give you a way to create consistent, professional, preformatted email messages that you can use when communicating with your customers. You can view, create, and edit any email templates you've created.

When creating a template, you have the option to work with a blank or existing template.

   ![Create an email template.](media\email-how-to-create-an-email-template-1a.png "Create an email template")

When you select **New** from the **Email Templates** command bar, a drop-down list appears with options to either **Start with a blank template** or **Start with existing templates**.

## Start with a blank template

Starting with a blank template means that you build and add all the data to the template.

If you select **Create an email template**, the following is displayed:

   ![Start with a blank template option.](media\email-create-an-email-template-1a.png "Start  with a blank template option")

Legend 
   1. **Template name**. Assign your email template a detailed name you want to save for future use.
   2. **Permission level**. You can share the template you create with your **Organization** or as  **Individual** for personal use.
   3. **Category**. The default for this field is set to **User**. Categories determine which dynamic text fields are available for use in your template.
   4. **Language**. You can display your installed language packs in this field. **Language** also helps to categorize your templates. 
   5. **Create**. Once an email is formatted, you can create it into a template.
   
### New Customer Template overview

If you select **New Customer Template**, the following example page displays, where you can make edits. 

   ![New Customer Template.](media\email-new-customer-template-1c.png "New Customer Template")

Legend 
   1. **New Attachments**. Allows you to include attachments to your template. 
   2. **Subject**. Allows you to change the subject line.
   3. **Insert dynamic text**. Allows you to use dynamic text in both the Subject line and body of the email.

## Start with existing templates

Starting with an existing template means the template is automatically pre-populated with the pre-established data that you can customize. 

#### Create a new email template overview

The following **Create a new email template** screen appears, which allows you to customize your template

  ![Start with existing templates.](media\email-start-with-existing-templates-1a.png "Start with existing templates")

   Legend
   1. **Search**. Allows you to search for templates. Search does not support regular expressions and it works on the template name only.
   2. **Browse**. Allows you to browse through out-of-the-box email templates. A list of available out-of-the-box email templates (global and entity specific) will display in alphabetical order. Global templates are shown as the type User. If you've created a custom email template, it will also be displayed here. 
   3. **Details**. Allows you to preview the email template.  When you select an email template, you can preview the content so you can pick the template that best meets your needs. After inserting an email template, you can modify the template content as needed.
   3. **Select**. Allows you to insert the template content into your email.

      > [!Important] 
      > When you begin working in the new environment, do not edit your templates in the old legacy web client; otherwise you will lose your inline images and strip out some of the advanced formatting and functionality.

### Work with existing templates

When you select an existing template, the following display appears:

   ![Creating email template copies.](media\email-template-copy-1a.png "Creating email template copies")

   - **Name**. The new template you created from the existing template will display **– Copy** at the end of the template name to identify it is a copy of an existing template.
   - **Template Editor**. All of the data is carried over from the existing template which can be edited and modified.
