---
title: "Overview of Power Apps Portals admin center | MicrosoftDocs"
description: "Information about Power Apps Portals admin center."
author: tapanm-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/07/2019
ms.author: tapanm
ms.reviewer:
---

# Power Apps Portals admin center

The Power Apps Portals admin center allows you perform advanced administrative actions on portals. The admin center is available when a portal is provisioned successfully.

## Open Power Apps Portals admin center

1. Go to the **Recent apps** section on the Power Apps home page and locate your portal.

    > [!div class=mx-imgBorder]
    > ![Recent apps](../media/recent-apps.png "Recent apps")  

2. Select **More Commands (...)** > **Settings**.

    > [!div class=mx-imgBorder]
    > ![Portal settings option](../media/portal-settings-option.png "Portal settings option")

3. In the **Portal settings** pane, select **Administration**.

    > [!div class=mx-imgBorder]
    > ![Portal settings pane](../media/portal-settings-admin.png "Portal settings pane")

## Add yourself as an owner of the Azure AD application

If you are not a global administrator and you try to manage a portal that has already been provisioned, or you resubmit the provisioning if it failed, you must be the owner of the Azure Active Directory (Azure AD) application connected to your portal.

1. Go to the Power Apps Portals admin center and open the **Portal Details** tab.

2. Copy the value from the **Application ID** field.

    > [!div class=mx-imgBorder]
    > ![Portal Details tab](../media/portal-details-admin.png "Portal Details tab")

3. Go to Azure AD associated with your tenant. [!include[](../../../includes/proc-more-information.md)] [Take over an unmanaged directory as administrator in Azure Active Directory](https://docs.microsoft.com/azure/active-directory/active-directory-manage-o365-subscription)

4. In Azure AD, search for the app registration by using the application ID you copied. You might need to switch from **My apps** to **All apps**.

5. Add users or groups as owners of this app registration. [!include[](../../../includes/proc-more-information.md)] [Managing access to apps](https://docs.microsoft.com/azure/active-directory/active-directory-managing-access-to-apps)

    > [!Note]
    > This task can be performed either by a global administrator of your organization or the existing owner of this application.

6. After you've added yourself as an owner, reopen the Power Apps Portals admin center page.