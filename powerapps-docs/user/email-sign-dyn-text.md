---
title: "Use an email signature with dynamic text| MicrosoftDocs"
description: Learn how to use an email signature with dynamic text.
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



# Insert dynamic text in email signatures

You can insert dynamic text in the in existing or newly created email signature templates. Dynamic text replaces a placeholder entity with the value of the entity in the **From** field when you send an email. 

To insert dynamic text, perform the following steps: 

 1. Create an email signature or select an existing email signature template.
 2. Place your cursor in the **Signature editor** and select **Insert dynamic text**.
 1. On  **Edit dynamic text**, specify the **Field name**. 
     > [!Note]
     > - The **Record type** for email signature templates is always **User**.
     > - You can only select fields that are linked to the **Record type**, User.

 ### Insert signature templates with dynamic text

When you insert signature templates with dynamic text placeholders, the information displayed in the body of the email is based on the **From** field as follows:

- Users: 
     -  The default signature template linked to the user is added to the email. User specific information corresponding to the dynamic placeholders configured in the default signature template is displayed.
- Queues:
     -  The default signature template linked to Queue's owner(user) is added to the email. User specific information corresponding to the dynamic placeholders configured in the default signature template is displayed. 
     
> [!Note]
> - If the Queues's owner is a team, the default signature template associated with the team's administrator is added to the email.
> - If a user doesn't have a default email signature template configured, you can add an alternate template by selecting **Insert Signature** and then specifying the required signature template in the **Search Signature** dropdown.

For example, let's say you are user John Doe. You create a email signature template with the following placeholder: {{!User:Full Name}}. This is the default email signature template for your user id.

When you're composing an email, if you specify your user name in the **From** field and you select **Insert signature**, the application displays John Doe in the body of the email.

You are also the owner of the Queue, Contoso Printer. If you specify your Contoso Printer in the **From** field of the email and select **Insert signature**, the application displays John Doe in the body of the email.
