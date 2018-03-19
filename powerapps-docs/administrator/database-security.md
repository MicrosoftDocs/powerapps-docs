---
title: Configure database security | Microsoft Docs
description: This topic explains how to configure database security.
services: powerapps
documentationcenter: na
author: maertenm
manager: kfend
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/21/2018
ms.author: manasma

---
# Configure database security
The Common Data Service uses a role-based security model to help secure access to the database. This topic explains how to create the security artifacts that you must have to help secure an app. The user roles control run-time access to data and are separate from the Environment roles that govern environment administrators and environment makers. For an overview of environments, see [Environments overview](environments-overview.md).

## Out-of-box security roles
Following security roles are provided out of the box:

* **System Administrator** – The System Administrator role is intended for users who have an administrative function. The creator of the environment and the **Environment Admin** are automatically assigned to this role, when database is provisioned. Users in this role always have full access to all entities in the database. They even have full access to new entities that are added. Users in this role can also create and edit entity schemas in the database. 

* **System Customizer** – The System Customizer role is intended for users who need to create and modify entities in the database. They can create roles, but not assign permissions to the users. 

* **Environment Maker** – The Environment Maker role can create resources within an environment including apps, connections, custom connectors, gateways, and flows using Microsoft Flow. Environment Makers can also distribute the apps they build in an environment to other users in your organization. They can share the app with individual users. For more information, see [Share an app in PowerApps](../maker/canvas-apps/share-app.md). For the users making or editing apps and flows connecting to the database and needs creating or updating the entities and roles, should be assigned System Customizer role as well, along with the Environment Maker. This role, has no priviliges on the database.

* **Common Data Service User** – The Common Data Service User, can read the data, where the user has permissions. This role is suitable for the users, who just need to access and update their own data while playing an app. 

## Custom security roles
To meet the needs of your app and organization policies, you can create [custom roles][1].


> [!NOTE]
> Currently, only users can be assigned to the roles. Assigning a role to a security group is in our backlog.






