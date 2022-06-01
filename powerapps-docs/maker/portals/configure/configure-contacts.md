---
title: Configure a contact for use on a portal
description: Learn how to add and configure a contact to be used in a portal.
author: sandhangitmsft

ms.topic: conceptual
ms.custom: 
ms.date: 06/01/2022
ms.subservice: portals
ms.author: sandhan
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - sandhangitmsft
    - dileepsinghmicrosoft
---

# Configure a contact for use on a portal

After filling out the basic information for a contact, or having a user fill out the sign-up form in a portal, go to the web authentication tab on the portal contact form to configure a contact by using local authentication. 

For more information about federated authentication options, see [Set authentication identity for a portal](set-authentication-identity.md). To configure a contact for portals by using local authentication, follow these instructions:  

1. Enter a **username**.
1. On the command ribbon, go to **More Commands** &gt; **Change Password**.

Complete the change password workflow, and the necessary fields will be automatically configured. When you've done this, your contact will be configured for your portals.

## Change password for a contact from the Portal Management app

> [!NOTE]
> You will need to be assigned the **System Administrator** [security role](/power-platform/admin/database-security) to perform these steps.

1. Open the [Portal Management app](configure-portal.md).

1. Go to **Portals** > **Contacts**, and open the contact for which you want to change the password.
    Alternately, you can also open the **Contacts** page from the [Share](../manage-existing-portals.md#share) pane. 

1. Select **Change Password** from the command bar the contact form.

    :::image type="content" source="media/configure-contacts/change-password.png" alt-text="Change password from the command bar.":::

1. In the **New password** field, enter a new password, and then select **Next**.

    :::image type="content" source="media/configure-contacts/change-password-new-password.png" alt-text="Enter new password for the contact.":::

    If you don't enter a password and select **Next**, you'll be asked whether you want to remove password for the selected contact.

    :::image type="content" source="media/configure-contacts/change-password-remove-password.png" alt-text="Remove password for the contact.":::

1. After making the changes, select **Done**.

    :::image type="content" source="media/configure-contacts/change-password-done.png" alt-text="Password changed for the contact.":::

### See also
[Invite contacts to your portals](invite-contacts.md)  
[Set authentication identity for a portal](set-authentication-identity.md)  

