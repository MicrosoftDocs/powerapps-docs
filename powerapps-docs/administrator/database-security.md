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
ms.date: 05/08/2017
ms.author: kfend

---
# Configure database security
The Common Data Service uses a role-based security model to help secure access to the database. This topic explains how to create the security artifacts that you must have to help secure an app. The user roles control run-time access to data and are separate from the Environment roles that govern environment administrators and environment makers. For an overview of environments, see [Environments overview](environments-overview.md).

It's important that you understand what level of access to these entities users of the app require. The Common Data Service supports create, read, update, and delete (CRUD) permissions on entities.

* **Create** – A user can create new entries in the entity.
* **Read** – A user can view and search existing entries in the entity.
* **Update** – A user can update or edit an existing entry in the entity.
* **Delete** – A user can delete or remove an existing entry in the entity.

The two permission levels that are most often used are read-only access and full access. The Common Data Service includes permission sets at these two permission levels for all its entities. View permission sets provide read access to an entity. Maintain permission sets provide full access to an entity.

The security model enables any combination of these permissions to be assigned to a user role. Roles combine the various permissions that are granted across the permission sets that are added to them. Therefore, the members of a role can access all the data that the permission sets that are included in the role give them access to. For more information about the Common Data Service security model, see [Security model](https://docs.microsoft.com/common-data-service/entity-reference/security-model).

## Identify the entities
To configure the correct access controls for an app, you must know what entities the app uses. To see a list of the entities that an app uses, follow these steps.

1. Open the app in Microsoft PowerApps Studio.
2. On the **Content** tab, click or tap **Data sources**. The list of data sources appears in the right pane.

## Configure security
When you create a new entity, you must also create a new permission set or edit an existing permission set to provide access to the entity's data. When you create an app, we recommend that you also create a permission set that provides access to all the entities that are required in order to run the app. Security is managed in the admin center.

1. Open the [admin center](https://admin.powerapps.com).
2. Click or tap the environment that contains your database.
3. Click or tap **Security**. You can then use the **Permission sets** and **User roles** tabs to configure security on your database.

## Create a permission set
To enable access to a new app, you must first create a new permission set.

1. Click or tap **Permission sets**.
2. Click or tap **New permission set** to create a permission set.
3. Enter a name and description for the permission set, and then tap or click **Create**. The new permission set appears in the list of permission sets.
4. Click or tap the permission set that you just created.
5. Click or tap the **Entities** tab. The **Entities** tab contains a list of all the entities in your database. For each entity that is used in your app, select the check box for the permission to allow.
6. Click or tap **Save**.

## Create a policy (Technical Preview)
To enable or restrict access to the records in an entity, you must first create a policy.

1. Click or tap **Policies**.
2. Click or tap **New policy**.
3. Enter a name and description for the policy.
4. Select the type of policy to create. If you're creating a picklist policy, enter the picklist to use.
5. Select the operator to use.
6. Select the value for the policy to check against.
7. Click or tap **Create**.

## Assign a policy (Technical Preview)
To apply a policy, you must assign it to a data entity in a permission set.

1. Click or tap **Permission Sets**.
2. Click or tap the permission set to assign a policy under.
3. Click or tap the **Edit** button for the entity to assign a policy to.
4. Expand the **Policy assignment** section.
5. Select the data operations to apply a policy to (**Create**, **Read**, **Update**, or **Delete**).
6. Select the entity field that the policy will be based on.
7. Select the policy to assign.
8. Click or tap **Assign**.
9. Click or tap **Save**.

## Create and assign a role
After the correct permissions are included in a permission set, you can create a role that can be assigned to users.

1. Click or tap **User roles**.
2. Click or tap **New role**.
3. Enter a name and description for the role, and then click or tap **Create**. The new role appears in the **User** roles list.
4. Click or tap the role that you just created.
5. Click or tap the **Permission sets** tab.
6. Enter the name of the permission set that you created earlier. In the drop-down list that appears as you type, click or tap the permission set to add it to the role. Repeat this step for every other permission set that you want for the role.
7. Click or tap the **Users** tab for the role.
8. Enter the names or email addresses of the users or groups to add to the role. In the drop-down list that appears as you type, click or tap the user. Users and groups that the role will be assigned to are added to the list.
9. Click or tap **Save**.

The users or groups in this role can now access the data that any permission set that is associated with the role gives them access to. To use the data in your database, a user must have a security role and access to a PowerApps app that uses the data.

## Edit permission sets and roles
To edit roles and permission sets after they have been created, click the **Edit** button.

To delete a role or permission set, use the **Delete** button.

## Out-of-box security roles
Two security roles are provided out of the box:

* **Database Owner** – The Database Owner role is intended for users who have an administrative function. The creator of the environment is automatically assigned to this role. Users in this role always have full access to all entities in the database. They even have full access to new entities that are added. Users in this role can also create and edit entity schemas in the database. You don't have to add permission sets to this role. You just have to assign users to it.
* **Organization User** – The Organization User role is the default role that is assigned to all users. The purpose of this role is to give all users access to the entities that contain public data. If an app is shared in restricted mode, the entities that the app uses should be contained in this role. You don't have to assign this role, because it's already assigned to everyone in your organization. You just have to add the permission sets that you want to give to your whole organization.

