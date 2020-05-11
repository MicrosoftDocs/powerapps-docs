---
title: "Send email to unresolved email recipients | MicrosoftDocs"
description: "Learn how to send email to unresolved email recipients."
ms.date: 05/11/2020
ms.service:
  - "dynamics-365-sales"
ms.topic: article
author: sbmjais
ms.author: shjais
manager: shujoshi
---

# Resolve an unresolved email recipient

An *unresolved email recipient* is one whose email address isn't associated with any entity records in Common Data Service. By default, you can't send an email to an unresolved email recipient. If you enter an unresolved email recipient address, the email address is deleted as soon as you move the focus out of the **To**, **Cc**, or **Bcc** field. An administrator must enable the unresolved email recipient feature by selecting **Yes** for **Allow messages with unresolved email recipients to be sent** on the **Email** tab in the **System Settings** dialog box. More information: [System Settings Email tab](https://docs.microsoft.com/power-platform/admin/system-settings-dialog-box-email-tab)

After the feature is enabled, you can add an unresolved email recipient in the **To**, **Cc**, or **Bcc** field. The entered email address is shown in red. You can then select the email address and associate it with an entity record in Common Data Service without navigating away from the email form.

If you receive an email that has email addresses that aren't associated with an entity record, the email addresses are shown in red. You can then individually select the email addresses and associate them with an entity record. You can then send emails to the newly added email addresses.

> [!NOTE]
> You can also resolve emails to existing records.

**To resolve an unresolved email recipient**

1. Open the email editor and select the unresolved email recipient.

    ![Unresolved email recipient](media/unresolved-email.png "Unresolved email recipient")

2. In the **Lookup Records** pane, select **New Record**.

    ![Lookup Records pane for unresolved email recipient](media/unresolved-email-lookup.png "Lookup Records pane for unresolved email recipient")

3. Select the record type to create. For example, **Contacts**.

    ![Select a record type](media/unresolved-email-select-record-type.png "Select a record type")

4. In the **Quick Create: Contact** pane, enter the required details, and select **Save and Close**.

    ![Enter contact details](media/unresolved-email-create-record.png "Enter contact details")

5. The contact is created and selected in the **Lookup Records** pane. Select **Add**.

    ![Add the contact](media/unresolved-email-add-record.png "Add the contact")

6. The unresolved email recipient is resolved and shown in the **To** field in the email editor.

    ![Resolved email recipient](media/resolved-email-recipient.png "Resolved email recipient")

### See also

[Allow unresolved email recipients](https://docs.microsoft.com/power-platform/admin/system-settings-dialog-box-email-tab)
