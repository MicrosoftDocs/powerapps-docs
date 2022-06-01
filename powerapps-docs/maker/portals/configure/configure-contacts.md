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

The following instructions will outline how to provide access to a portal for a new or existing contact in Microsoft Dataverse.

> [!IMPORTANT]
> - We recommend that you use the [Azure Active Directory B2C (Azure AD B2C)](configure-azure-ad-b2c-provider.md) identity provider for authentication and deprecate the local identity provider for your portal. More information: [Migrate identity providers to Azure AD B2C](migrate-identity-providers.md)

1. Open the [Portal Management app](configure-portal.md).

1. In the **Security** section, select **Contacts**.

1. Create a new contact or select an existing contact.

1. Choose the **Contact - Portal Contact** form.

1. Select the **Web Authentication** tab.

1. Enter a **Username**.

    :::image type="content" source="media/configure-contacts/contact-form.png" alt-text="Configure contact to provide access to portal.":::

1. Select **Save**.

1. On the command ribbon, choose **Change Password**.

1. Complete the [change password steps](#change-password-for-a-contact-from-the-portal-management-app), and the necessary fields will be automatically configured. The contact will then be configured to access the portal.

A portal user can also [register directly](set-authentication-identity.md#sign-up-by-using-a-local-identity-or-external-identity) on the portal, or be sent an [invitation](invite-contacts.md) to register. 

For more information about federated authentication options, see [set authentication identity for a portal](set-authentication-identity.md). 

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

