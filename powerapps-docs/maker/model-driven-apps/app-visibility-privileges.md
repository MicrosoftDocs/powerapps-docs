---
title: Privileges required to view apps in Power Apps | Microsoft Docs
description: Learn about the privileges required to view and access apps in Power Apps.
documentationcenter: ''
author: Mattp123
editor: ''
tags: ''
ms.topic: article
ms.component: model
ms.date: 03/12/2024
ms.subservice: mda-maker
ms.author: matp
search.audienceType: 
  - maker
---

# Privileges required to view and access apps

Apps can be viewed by valid users with appropriate privileges who sign into Power Apps, the Power Apps mobile app, or Dynamics 365 home page. For a user to view and access apps in an environment, the following privileges, security role, or team membership are required:

- A user who has both write and create privileges on the Model-driven App table makes the user a maker persona. That user can view and access all apps in the environment.
- A user who has only the read privilege on the Model-driven App table, must also have the associated security roles that are assigned to the app (or equivalent).

Read, create, and write privileges can be granted to a user by the security roles assigned to the user or granted through team membership.

By default, users who have only the Basic User security role can only access model-driven apps that have that security role assigned to the app. This behavior is because the Basic User security role only has read privileges on the Model-driven App table.

However, users who have the System Administrator, System Customizer, or Environment Maker<sup>1</sup>, security role can access and edit all model-driven apps within the environment. This behavior is because these security roles have create, read, and write privileges on the Model-driven App table. More information: [Share a model-driven app using Power Apps](share-model-driven-app.md)

<sup>1</sup> Although the environment maker security role has read and write access to the Model Driven App table, the role alone doesn't have access to the core and custom tables required to view, create, and edit data in an app.

### See also

[Manage teams](/power-platform/admin/manage-teams) <br />
[Security roles and privileges](/power-platform/admin/security-roles-privileges)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
