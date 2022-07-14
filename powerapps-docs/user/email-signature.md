---
title: "Use an email signature| MicrosoftDocs"
description: Learn how to use an email signature.
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


# Create a signature for emails

Email signatures are an important and valuable tool for users. Email signatures are like electronic business cards you include when you send an email, and can promote professional branding for your company.

## Add text to an email signature
Adding an email signature is easy and can be done at any point while you are composing an email. You can either add an email signature with static or dynamic text. Dynamic placeholders are used to define dynamic text. The placeholders are replaced  with the corresponding values of the email's sender, specified in the **From** field. 

> [!Note] 
> Inserting dynamic text in email signature templates is an early access feature and is available. You can opt in early to enable these features in your environment with Microsoft Dynamics 365 for Service package installed, which will allow you to test these features and then adopt them across your environments. For information about how to enable these features, see [Opt in to early access updates](/power-platform/admin/opt-in-early-access-updates). Starting October 2022, this feature will be enabled by default.

### Add an email signature
- On the command bar, select **Insert Signature**.  
- From the drop-down list, select an existing signature or select **New Email Signature**.<BR>
![How to add an email signature.](media\email-how-to-add-an-email-signature-1a.png "How to add an email signature")

Based on the email's sender specified in the **From** field, one of the following actions occur:

- If the sender is a user, the dynamic placeholders defined in the email signature template are replaced with the values corresponding to the user.
- If the sender is a queue and the owner of the queue is a user, the dynamic placeholders defined in the email signature template are replaced with the values corresponding to the queue's owner. If the owner of the queue is a team, the the dynamic placeholders are replaced with the values corresponding to the team's Administrator.


## Create an email signature
You can quickly create an email signature at any point while you are composing an email.

### Create a new email signature

You can add a new email signature by:

   ![Add a new email signature.](media\email-how-to-create-an-email-signature-1b.png "Add a new email signature")

   1. **Details** in this section, enter the name of the email signature.
   2. **Signature editor**. This allows you to create your email signature and **Save** when finished. 

      > [!Note] 
      > - You can  include inline images, such as a business logo, in an email signatures, as long as they are under 1 MB in size.
      > -  You can insert dynamic placeholders in your signature templates. You can only add fields that are linked to the **Record type**, User as dynamic placeholders.
      > - Signatures can also be created and used for queues.
      
## Manage email signature lists

You can view and manage email signatures you have created to make edits, change default, and who can view your signatures.

   ![Manage email signature lists.](media\email-manage-email-signature-lists-11a.png "Manage email signature lists")

   Legend
   1. Under **Templates** select **Email signatures**.
   2. **My Email Signatures** list displays, showing all your email signatures you can edit and update.
   3. You can select a default signature for email. Only one signature per user can be set as **Is Default**. 
   4. Email signatures can only be **Viewable By** the individual user.

## Change the default email signature setting
While you can create multiple email signatures depending on your needs, only one can be set as your default email.   

   ![Change email signature default setting.](media\email-change-email-signature-default-setting-1a.png "Change email signature default setting")

   To change your default email signature setting:
   1. Select the email signature you want to set as default. This will change the command bar to display **Edit**.
   2. Select **Edit**. A new page opens, where you can update the email default setting. While you are on this page, you can also delete one or multiple email signatures just by selecting them.
