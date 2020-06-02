---
title: "Send email to multiple recipients | MicrosoftDocs"
description: "Learn how to send email to multiple recipients."
ms.date: 05/11/2020
ms.service:
  - "dynamics-365-sales"
ms.topic: article
author: sbmjais
ms.author: shjais
manager: shujoshi
---

# Send email to multiple recipients

You can send an email to multiple recipients by using email templates. This is known as *direct* or *bulk* emailing. By default, the direct email feature is disabled. An administrator must enable the direct email feature by selecting **Yes** for **Enable Send Direct Email Action in Unified Interface for Send Email enabled entities** on the **Email** tab in the **System Settings** dialog box. More information: [System Settings Email tab](https://docs.microsoft.com/power-platform/admin/system-settings-dialog-box-email-tab)

**To send email to multiple recipients**
  
1. In the site map for the model-driven app, select an entity to which you want to send email. For example, **Contacts**.  
  
2. In the list of records, select the contacts you want to send an email to.  
  
3. On the command bar, select **Send Direct Email**.  

    ![Select multiple contacts and then select Send Direct Email](media/select-contacts.png "Select multiple contacts and then select Send Direct Email")

4. In the **Send Email** pane, select an email template from the **Template** list.

    > [!NOTE]
    > If you have multiple records that span across multiple pages, you can select one of following options from the **To** list:
    > - **All records on current page**: Sends the email to all records displayed on the current page.
    > - **All records on all pages**: Send the email to all the stored records.

5. Select **Send**.

    ![Send email to multiple recipients](media/direct-email.png "Send email to multiple recipients")

### See also

[Enable direct email](https://docs.microsoft.com/power-platform/admin/system-settings-dialog-box-email-tab)