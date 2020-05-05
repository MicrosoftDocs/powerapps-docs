---
title: "Send email to unresolved email recipients | MicrosoftDocs"
description: "Learn how to send email to unresolved email recipients."
ms.date: 05/04/2020
ms.service:
  - "dynamics-365-sales"
ms.topic: article
author: sbmjais
ms.author: shjais
manager: shujoshi
---

# Send email to unresolved email recipients

An unresolved email recipient is one whose email address does not get resolved to a contact. By default, you cannot send an email to an unresolved email recipient. If you enter an unresolved email recipient, the email address is deleted as soon as you move the focus out of the **To** field. An administrator must enable the unresolved email recipient feature by selecting **Yes** for **Allow messages with unresolved email recipients to be sent** on the **Email** tab in the **System Settings** dialog box. More information: [System Settings Email tab](https://docs.microsoft.com/power-platform/admin/system-settings-dialog-box-email-tab)

After enabling the feature, when you enter an unresolved email recipient in the **To** field, the email address is shown in red. You can then select the email address, save it to Common Data Service, and then send the email.

**To send email to unresolved email recipients**

1. Open the email editor.

2. Select the unresolved email recipient. 

    ![Unresolved email recipient](media/unresolved-email.png "Unresolved email recipient")

3. In the **Lookup Records** pane, select **New Record**.

    ![Lookup Records pane for unresolved email recipient](media/unresolved-email-lookup.png "Lookup Records pane for unresolved email recipient")

4. Select the record type to create. For example, **Contacts**.

    ![Select a record type](media/unresolved-email-select-record-type.png "Select a record type")

5. In the **Quick Create: Contact** pane, enter the required details, and select **Save and Close**.

    ![Enter contact details](media/unresolved-email-create-record.png "Enter contact details")

6. The contact is created and selected in the **Lookup Records** pane. Select **Add**.

    ![Add the contact](media/unresolved-email-add-record.png "Add the contact")

7. The unresolved email recipient is resolved and shown in the **To** field in the email editor.

    ![Resolved email recipient](media/resolved-email-recipient.png "Resolved email recipient")

### See also

[Allow unresolved email recipients](https://docs.microsoft.com/power-platform/admin/system-settings-dialog-box-email-tab)
