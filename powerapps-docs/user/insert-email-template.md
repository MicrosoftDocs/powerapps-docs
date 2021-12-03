---
title: "Insert email template while composing an email in model-driven apps | MicrosoftDocs"
description: "Insert a preformatted email message while composing an email."
ms.custom: ""
author: sbmjais
manager: shujoshi
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 06/30/2021
ms.subservice: end-user
ms.author: shjais
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---


# Insert an email template

If you previously created an email template, you can easily use it as the basis for your email by inserting it into the email.

   ![Insert an email template.](media\email-how-to-insert-an-email-template-1a.png "How to insert an email template")

   - You can access the email template you created from the command bar by selecting **Insert Template**. <BR><BR>

**Insert an email template overview**  

Once you select **Insert Template**, the following window appears displaying a list of existing **Email templates** that are available to use.

> [!Note]
> There is an intermediary window that may display if:
> 1. You don't have either a Recipient or Regarding field for your email.
>
> ![Message window for no recipient or regarding field.](media\email-template-recipient.png "Message when missing recipient or regarding field")
>
> 2. When you have both a Recipient and Regarding field. You must select one.
>
> ![Message when both recipient and regarding field are present.](media\email-template-select-record.png "Message when both recipient and regarding fields are present")
>
> The selection of one of these fields determines which template types are shown to a user in the template selection window:
> - Recipient (TO): user (global) and contact templates are displayed.
> - Regarding: user (global) and templates for the regarding entity are shown.

#### Email template selection window

   ![Email template selection window.](media\email-how-to-insert-an-email-template-1b.png "Email template selection window")

   Legend
   1. **Language**. Templates are loaded as per the selected language.
   2. **search**. You can use search to find a template. Search does not support regular expressions and only works when using the name of that specific template.  
   3. **All templates**. All existing templates that have been created are displayed in this window  which you can browse and choose from.
   4. **Preview**. When you select an email template, a preview of the template is displayed here. The preview shows you the content so you can pick the template that best meets your needs. After inserting an email template, you can modify the content as needed.
   5. **Apply template** to insert the content to your  email.

      > [!Note] 
      > If you try to insert an email template on a device with a smaller screen size, you'll only see an option to search and select a template.
      
### See also

[Set up enhanced email](/power-platform/admin/system-settings-dialog-box-email-tab)<br>
[Understand the email experience](view-create-email.md)


[!INCLUDE[footer-include](../includes/footer-banner.md)]
