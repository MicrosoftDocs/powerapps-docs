---
title: "Insert email template while composing an email in model-driven apps | MicrosoftDocs"
description: "Insert a preformatted email message while composing an email."
ms.custom: ""
author: sbmjais
manager: shujoshi
ms.component: pa-user
ms.topic: conceptual
ms.date: 03/25/2022
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

<!-- note from editor: I changed "the following window" to "a window" in line 35 because the image of the window isn't shown until after a lengthy note and another header, which is confusing if the reader expects the see the image right after that sentence. -->
<!-- Also, there's a link in line 69 that you should test on the review page. (I can't access the review pages.)  -->


# Insert an email template

If you previously created an email template, you can easily use it as the basis for your email by inserting it into the email.

![Insert an email template.](media\email-how-to-insert-an-email-template-1a.png "How to insert an email template")

You can access the email template you created from the command bar by selecting **Insert Template**. 

## Insert an email template overview  

Once you select **Insert Template**, a window appears displaying a list of existing **Email templates** that are available to use.

> [!Note]
> There is an intermediary window that may display if:
> - You don't have either a Recipient or Regarding field for your email.
>
>   ![Message window for no Recipient or Regarding field.](media\email-template-recipient.png "Message when missing Recipient or Regarding field")
>
> - You have both a Recipient and Regarding field. You must select one.
>
>   ![Message when both Recipient and Regarding field are present.](media\email-template-select-record.png "Message when both Recipient and Regarding fields are present")
>
> The selection of one of these fields determines which template types are shown to a user in the template selection window:
> - Recipient (TO): user (global) and contact templates are displayed.
> - Regarding: user (global) and templates for the regarding entity are shown.

### Enhanced email template selection window

The application displays the enhanced email template selection window only if your admin has configured the [enhanced insert template dialog](customize-insert-email-template.md) option. You can perform the following actions in the ehanced email template selection window:

 - Switch between list, tile, and grid views.
 - Search for templates based on their title, subject, description, or content of the template.  
 - Filter templates based on standard and custom attributes.
 - Zoom in to view templates on a full screen. The application provides an option to navigate between templates.
 - Admins can add custom attributes to the Template Gallery Filter Form to extend Filters, Email Template Sorted View to extend the grids, and Template Gallery Properties Form to extend the template details section.

![Enhanced email template selection window.](media\email-templates.png "New Email template selection window")

**Legend**
  
1. **Search**. Use search to find a template. You can search for templates based on name, subject, description, or content. Search doesn't support regular expressions.
2. **All templates**. Choose and browse from the templates based on TO or Regarding that are displayed in this window. You can change the view to display the templates in a grid, list, or tile view. Hover over the template tile to see the zoom option. Select the tile to open the template on a full screen.
3. **Preview**. When you select an email template, a preview of the template is displayed here. The preview shows you the content so you can pick the template that best meets your needs. After inserting an email template, you can modify the content as needed in the email editor.
4. **Filter**. You can filter templates based on standard or custom attributes.
5. **View**. Use the dropdown list to switch between grid, tile, or list views. Based on your admin's settings, the application displays a specific view. More information: [Customize the email](customer-service-hub-user-guide-email-font-admin.md#configure-the-default-email-template-selection-view).
 
> [!Note] 
> If you try to insert an email template on a device with a smaller screen size, you'll only see an option to search and select a template.
  
### Email template selection window

You can perform the following actions on the email template selection window:

- Select a language.
- Search for templates by title.
- Modify the content for a selected template.

![Email template selection window.](media\email-how-to-insert-an-email-template-1b.png "Email template selection window")

**Legend**

1. **Language**. Templates are loaded according to the selected language.
2. **Search**. Use search to find a template. Search doesn't support regular expressions and only works when using the name of that specific template.  
3. **All templates**. All existing templates that have been created are displayed in this window, which you can browse and choose from.
4. **Preview**. When you select an email template, a preview of the template is displayed here. The preview shows you the content so you can pick the template that best meets your needs. After inserting an email template, you can modify the content as needed.
5. **Apply template** to insert the content to your email.

> [!Note] 
> If you try to insert an email template on a device with a smaller screen size, you'll only see an option to search and select a template.
      
### See also

[Set up enhanced email](/power-platform/admin/system-settings-dialog-box-email-tab)<br>
[Understand the email experience](view-create-email.md)


[!INCLUDE[footer-include](../includes/footer-banner.md)]
