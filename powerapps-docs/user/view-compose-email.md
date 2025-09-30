---
title: "View, compose and respond to email | MicrosoftDocs"
description: How to view, compose and respond to email.
author: shwetamurkute

ms.component: pa-user
ms.topic: article
ms.date: 05/10/2024
ms.subservice: end-user
ms.author: smurkute
ms.custom: ""
ms.reviewer: smurkute
ms.assetid: 
search.audienceType: 
  - enduser
---

# View, compose and respond to email

Users can view, create, and send email faster with streamlined access that helps users compose, reply, and send emails using rich text editing and drag-and-drop attachment features and functionalities to embed images in emails.


## Access and view emails

   ![Access and view email.](media\email-how-to-view-an-email-11a.png "Access and view email.")
   Legend
   1. Select **Activities**
   2. Select **All Activities** 
   3. Under **Activity Type** select **Email**
   4. Email list appears in the screen below

## Compose an email

Email capabilities, like rich-text editing and drag-and-drop or copy-and-paste images enriches customer interactions when composing email. 

When enabled by your system administrator, you can access email from the top navigation bar.

### Compose an email

   ![Compose an email.](media\email-how-to-compose-an-email-11b.png "Compose an email")
   1. Select **Activities**
   2. On the command bar, select **Email**. An email then opens in a new window where you can begin composing. 

### Anatomy of an email form

![Anatomy of email.](media\email-how-to-compose-an-email-1g.png "Anatomy of an email form.")

Legend

1. **From**. The name displayed in the **From** field is automatically populated based on the user who is currently signed in.
2. **Expand**. The **Expand** ![Expand icon.](media\email-expand-icon.png "xpand email") icon allows you to compose your email in a full-screen view and minimize when done.
3. **Rich text editor**. This tool bar helps you  format emails. The editor is displayed as a single line that can be expanded to view the full list of editing features by default. For more information, see [Use the rich text editor toolbar in email](email-rich-text-editor.md) and [Accessibility shortcuts for email](keyboard-shortcuts.md#email). **User Personalization**. The ![Set default.](media\personalization.png "personalization icon") icon allows you to set the default font and font size for your emails. Once set, the **Font** and **Font Size** display these values by default. 
1.  **Body**. The body is where you compose and/or reply to an email.
1. **Insert Signature**. Use this command to personalize your message.  
1. **Insert Template**. This is used to apply an email template. <BR>
For more information, see [Insert an email template](insert-email-template.md).

   > [!Note]
   > The **To** box must contain a recipient to select a template.

7. **New Attachment**. This command is used to add a file to your email.
8. **Attach File**.  This command uses the 'plus' ![attach file icon.](media\email-new-attachment-icon.png "attach file icon") icon functionality to add attachments. 

   > [!Note] 
   > After you save your email, you can use Attach file and New Attachments interchangeably.

9.	**Send**. Select this icon ![Send email icon.](media\email-send-icon.png "Send email icon")  to **Send** your email when you are done.

    >[!Important]
    > - The **From** and **To** fields are automatically populated based on the user and the account and contact of the original record.

## View email sentiment (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]


 When you get an incoming email from a customer, the Customer sentiment card is displayed on the email form.

The customer sentiment card displays the following:

 - **Current sentiment**: The customer’s current sentiment. A sentiment intensity indicator in the corresponding colors is also displayed.
 - **Sentiment timeline**: A visual representation that shows how the customer sentiment in the emails received changes across a period.   
 The timeline displays indicators for up to six customer emails, including the current email. Customer service representatives can select historical sentiment and then select **View email**. The system shows the relevant email for that period and sentiment in a new tab.

- The **Inbox** view also displays the sentiment with the sentiment intensity indicator.

> [!Note]
> For emails received before the feature is enabled, the system doesn’t display the sentiment.

[!INCLUDE [preview-banner](../../../shared-content/shared/preview-includes/production-ready-preview-dynamics365.md)]


## Reply to an email
The way you can reply to an email depends on where you are in your app. 

When enabled by your system administrator, the email option displays in the top navigation bar and in the activities command bar.

>[!Note]
> The best performance is achieved when the HTML content size is 1 MB or less. When your HTML content size exceeds 1 MB, you might notice slower response times for loading and editing content. By default, image content is referenced from the content HTML but isn't stored as part of the HTML content, so in the default configuration, images don't negatively impact performance.

## Enhanced recipient handling 

Users can perform the following actions only if the administrator has added the [**Email Recipient control**](/dynamics365/customer-service/administer/add-enhanced-attachment-control#enable-recipient-control) component to an email form:

 - Drag and drop recipient names across **To**, **CC**, and **BCC** fields.
 - View the recipient's email address along with their names.
 - View the recipients' presence status and out-of-office messages.
 - Resolve an unresolved email address faster. In the email editor, if there's an [unresolved email address](unresolved-email-recipient.md), the application displays a banner message and the **Review** option to map the email. Select the button to view and map an unresolved email address to an existing record. 
   >[!Note]
   > You can't resolve an unresolved email address for a read-only email.


   :::image type="content" source="media/recepient-handling.png" alt-text="Screenshot of runtime experience.":::

### Access email
When accessing email, there are a couple of options you can use. 

-  **Option 1:**<BR>
   ![Respond to an email.](media\email-how-to-respond-to-an-email-1c.png "Respond to an email")

    - Select **Email** on the command bar.

   >[!Note]
   > Email option will only appear in the drop-down list and the command bar when enabled by your system administrator.

-  **Option 2:**<BR>
   ![How to respond to an email.](media\email-how-to-respond-to-an-email-1d.png "How to respond to an email")

   1. From the navigation bar, select the plus ![Plus icon.](media\email-plus-icon.png "email icon") icon.
   2. Select **Email** from the drop-down menu.
  
### Set the default font and font size
  
You can set the default font and font size for your email text. Perform the following steps:
  
  - In the email editor, in the Rich text editor tool bar, select ![Set default.](media\personalization.png "personalization icon").
  - In **User Personalization** specify the **Font** and **Font Size**. 
  - Select **Ok**. The application defaults the values specified in the Font and Font Size fields of the rich text editor toolbar.
  
  If your administrator has set default font and font size, the application displays the set values in the Font and Font Size fields of the rich text editor toolbar.
  
## Reply to email in timeline
When replying to emails in Timeline, the command bar in the top-right corner provides you with reply options. When you select an option, your email automatically is set and opens in that state ready for you to begin your message.  

You can use the following command options when working with emails in the timeline.

   ![Respond to emails in timeline.](media\email-respond-in-timeline-1a.png "Respond to emails in timeline.") 

   1. **Reply**. Use this command to reply directly the sender of the email you received.
   2. **Reply All**. Use this command to reply to everyone on an email you received.
   3. **Forward**. Use this command to forward the email to someone else.

## Download email

Select **Download** to download emails as a .eml file. 

