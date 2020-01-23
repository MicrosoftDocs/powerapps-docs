---
title: Manage existing portals in Power Apps | Microsoft Docs
description: Instructions to manage a portal in Power Apps.
author: tapanm-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/07/2019
ms.author: tapanm
ms.reviewer:
---

# Manage existing portals in Power Apps

Once you've created a portal, it is visible under the **Recent apps** section on the Power Apps home page.

> [!div class=mx-imgBorder]
> ![recent apps](media/recent-apps.png "Recent apps")  

To manage an app, select **More Commands** (**…**) for the portal and choose an action from the context menu.

> [!div class=mx-imgBorder]
> ![portal app options](media/portal-app-options.png "Portal app options")  

## Edit

Opens the [Power Apps portals Studio](portal-designer-anatomy.md) to edit the content and components of the portal.  

> [!div class=mx-imgBorder]
> ![portal maker](media/portal-maker.png "Portal maker")  

## Browse

Opens the portal to browse the website. This helps you to see the portal as it will look to your customers.

> [!div class=mx-imgBorder]
> ![portal website](media/portal-website.png "Portal website")  

Alternately, you can also open the portal to browse the website by selecting **Browse website** in the [Power Apps portals Studio](portal-designer-anatomy.md) to view the changes you have made to the website. The website opens in a new tab with URL of the website.

## Share

Share your portal with internal or external users. Follow the steps mentioned in the **Share this portal** pane.

> [!div class=mx-imgBorder]
> ![share portal](media/share-portal.png "Share portal")  

### Share with internal users

To share the portal with internal users you must first create a security role and then assign users to the security role so they can use the portal.

> [!NOTE]
> As a user in Common Data Service, if you do not have appropriate privileges on portal entities, you might see errors such as “You do not have access to view solutions in this environment.” or “You do not have access to view Website in this environment”. It is recommended that you are in a System Administrator security role in the corresponding Common Data Service database.

#### Step 1: Create a security role

1.  In the **Share this portal** pane, under **Create a security role**, select **Security Roles**. A list of all the configured security roles is displayed.

2.  On the Actions toolbar, select **New**.

3.  In the **New Security Role** window, enter the role name.

4.  Set the privileges for all the entities used in your portal.

5.  When you have finished configuring the security role, on the toolbar, select **Save and Close**.

For information on security roles and privileges, see [Security roles and privileges](https://docs.microsoft.com/power-platform/admin/security-roles-privileges).

#### Step 2: Assign users to the security role

1.  In the **Share this portal** pane, under **Assign users to the security role**, select **Users**. A list of all users is displayed.

2.  Select the user that you want to assign a security role to.

3.  Select **Manage Roles**.

    > [!NOTE]
    > If you are unable to see the **Manage Roles** button on the command bar, you must change the client by setting forceUCI to 0 in the URL. For example, https://&lt;org\_url&gt;/main.aspx?pagetype=entitylist&etn=systemuser&forceUCI=0

4.  In the **Manage User Roles** dialog box, select the security role that you created earlier, and then select **OK**.

### Share with external users

Your portal should work anonymously and should be accessible by the external users. If you want to try advanced capabilities for managing roles and permissions for external users, see [Configure a contact for use on a portal](configure/configure-contacts.md), [Invite contacts to your portals](configure/invite-contacts.md), [Create web roles for portals](configure/create-web-roles.md), [Assign entity permissions](configure/assign-entity-permissions.md).  

## Settings

Displays the portal settings and allows you to change the name of the portal. You can also perform advanced actions such as administering the portal though the Power Apps Portals admin center and working with site settings. Settings provides links to the Power Apps Portals admin center and Site settings. More information: [Advanced portal administration](admin/admin-overview.md) and [Configure site settings](configure/configure-site-settings.md).  

> [!div class=mx-imgBorder]
> ![portal settings](media/portal-settings.png "Portal settings")  

## Delete

Deletes the portal and hosted resources. When you delete a portal, its URL becomes inaccessible. Deleting a portal does not affect any portal configurations or solutions present in your environment, and they will remain as-is.
You must delete the portal configurations manually to completely remove portal configurations from your environment. To do this, use the Portal Management app, and delete the corresponding website record for the portal.

> [!NOTE]
> If you don't have sufficient privileges to delete a portal, an error is displayed. You must have the System Administrator role to delete a portal. Also, you must be the owner of the portal application in Azure Active Directory. The user who creates the portal is by default the owner and can delete a portal. For information on adding yourself as an owner, see [Add yourself as an owner of the Azure AD application](admin/admin-overview.md#add-yourself-as-an-owner-of-the-azure-ad-application).

## Details

Displays details such as owner of the portal, date and time when it was created and last modified, and the URL of the portal.

> [!div class=mx-imgBorder]
> ![portal details](media/portal-details.png "Portal details")  

