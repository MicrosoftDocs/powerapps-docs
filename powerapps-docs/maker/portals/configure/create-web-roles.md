---
title: Create web roles for portals
description: Learn how to create web roles for a portal.
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/21/2021
ms.subservice: portals
ms.author: sandhan
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - sandhangitmsft
---

# Create web roles for portals

After a contact has been configured to use the portal, it must be given one or more web roles to perform any special actions or access any protected content on the portal. For example, to access a restricted page, the contact must be assigned to a role to which read for that page is restricted to. To publish new content, the contact must be placed in a role which is given content publishing permissions.

To create a web role:

1. Open the [Portal Management app](configure-portal.md).

2. Go to **Portals** > **Web Roles**.
    Alternately, you can also open the **Web Roles** page from the [Share](../manage-existing-portals.md#share) pane. 

3. Select **New**.

4. Enter appropriate values in the fields.

5. Select **Save**.

## Attributes and relationships

The table below explains the Web Role attributes used by portals.

| Name                     | Description                                                                                                                                                                                                                                     |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name                     | The descriptive name of the Web Role                                                                                                                                                                                                            |
| Website                  | The associated website                                                                                                                                                                                                                          |
| Description              | An explanation of the Web Role's purpose. Optional.                                                                                                                                                                                             |
| Authenticated Users Role | Boolean. If set to true, this will be the default web role for authenticated users (see below). Only one Web Role with the Authenticated Users Role attribute set to true should exist for a given website. All authenticated user automatically get permissions defined in this role. |
| Anonymous Users Role     | Boolean. If set to true, this will be the default web role for unauthenticated users (see below). Only one Web Role with the Anonymous Users Role attribute set to true should exist for a given website. This will be the default web role for unauthenticated users. The Anonymous Users Role will only respect Table Permissions.| 
|| 

Now that the Web Role has been created, you will be able to configure it to meet your needs via various permissions, rules, and associations.

- **Optional default web role for authenticated users**: By enabling the **Authenticated Users Role**, it will become the default web role for all users. This role is commonly used to provide a predetermined access for users that are not associated to any other roles. Keep in mind that users can have multiple web roles, but there can only be one Authenticated Users web role for authenticated users.
- **Optional default web role for unauthenticated users**: The **Anonymous Users Role** is intended to be used with Table Permissions. It will not respect any other rules or permissions. By enabling the "Anonymous Users Role" it will become the default web role for all users. There can only be one Anonymous Users web role for unauthenticated users.

### See also

[Configure a portal](configure-portal.md) <br>
[Control webpage access for portals](webpage-access-control.md)  
[Add record-based security by using table permissions for portals](assign-entity-permissions.md) <br>


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
