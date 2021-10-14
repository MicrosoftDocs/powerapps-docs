---
title: Privileges required to view apps in Power Apps | Microsoft Docs
description: Learn about the privileges required to view and access apps in Power Apps.
documentationcenter: ''
author: Mattp123
manager: kvivek
editor: ''
tags: ''
ms.service: powerapps
ms.topic: conceptual
ms.component: model
ms.date: 10/22/2020
ms.subservice: mda-maker
ms.author: matp
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Privileges required to view and access apps

Apps can be viewed by valid users with appropriate privileges who sign into Power Apps, the Power Apps mobile app, or Dynamics 365 home page. For a user to view and access apps in an environment, the following privileges, security role, or team membership are required:

- A user who has the write or create privilege on the Model-driven App table makes the user a maker persona. That user can view and access all apps in the environment.
- A user who has only the read privilege on the Model-driven App table, must also have the associated security role(s) that are assigned to the app (or equivalent).

Note that read, create, and write privileges can be granted to a user by the security roles assigned to the user or granted through team membership.

By default, users who have only the Basic User security role can only access model-driven apps that have that security role assigned to the app. This is because the Basic User security role only has read privileges on the Model-driven App table.

However, users who have the Environment Maker, System Administrator, or System Customizer security role can access and edit all model-driven apps within the environment. This is because these security roles have create, read, and write privileges on the Model-driven App table. More information: [Share a model-driven app using Power Apps](share-model-driven-app.md)

### See also

[Manage teams](/power-platform/admin/manage-teams) <br />
[Security roles and privileges](/power-platform/admin/security-roles-privileges)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]