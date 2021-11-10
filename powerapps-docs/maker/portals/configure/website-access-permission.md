---
title: Create website access permissions
description: Learn how to create and associate website access permissions to elements in a portal.
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/21/2020
ms.subservice: portals
ms.author: sandhan
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - sandhangitmsft
---

# Create website access permissions

Website Access Permissions is a permission set, associated with a [web role](create-web-roles.md), that permits front-side editing of the various content managed elements within the portal other than just web pages. The permission settings determine which components can be managed in the portal.

| Name                         | Description                                                                                      |
|------------------------------|--------------------------------------------------------------------------------------------------|
| Manage Content Snippets      | Allows the editing of Snippet controls.                                                          |
| Manage Site Markers          | Allows the editing of hyperlinks that use Site Markers                                           |
| Manage Web Link Sets         | Allows the editing of [web link sets](manage-web-links.md), including adding an removing web links from a web link set. |
| Preview Unpublished Entities | Allows the viewing of portal-exposed tables that have a publishing state of Draft.             |
|||

To create a website access permission and add it to a web role:

1. Open the [Portal Management app](configure-portal.md).

2. Go to **Portals** > **Website Access Permissions**.

3. Select **New**.

4. Under **General**, enter name, website, and select the required permissions.

    ![Create website access permission.](../media/website-access-permission.png "Create website access permission")

5. Under **Web Roles**, select **Add Existing Web Role**, and add the web role to associate the permission with.

6. Save the changes.

    


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]