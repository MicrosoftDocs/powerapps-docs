---
title: Create a Common Data Service database | Microsoft Docs
description: Create a Common Data Service database.
services: powerapps
documentationcenter: na
author: nimakms
manager: kfend
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 12/06/2016
ms.author: kfend

---
# Create a Common Data Service database
You can create a database and build apps by using Common Data Service as a data store. You can either create your own custom entities or use the predefined entities. To create a database, you first need to either create an environment, or be assigned to an existing environment as an administrator. In addition, you must be assigned the appropriate license. For information on purchasing a plan for using the Common Data Service, see [Pricing info](pricing-billing-skus.md).

There are three ways to create a database:

* In the admin center
* In the **Home** pane of powerapps.com
* In the **Entities** pane of powerapps.com

## Create a database in the admin center
1. In the [admin center](https://admin.powerapps.com), in the left navigation pane, click **Environments**.
2. Select the environment, or create a new environment if needed.
3. On the **Database** tab, click **Create a database**. By default, the database is created in Open access mode.
4. If you want to enforce security, select **Restrict access**.

## Create a database in the Home pane of powerapps.com
1. On [powerapps.com](https://web.powerapps.com), in the left navigation pane, click **Home**.
2. In the **Use the Microsoft Common Data Service** section, look for the button that is named either **Create database** or **Get started**. The button's name depends on your license and permission assignments. You might not be allowed to create a database in the current environment.

### Create database in current environnmet
1. Click **Create database**.
2. In the dialog box, select the **Restrict access to database** check box if you want to enforce security.
3. Click **Create my database**.

### Get started by creating a new environment
1. Click **Get started**.
2. In the dialog box, click **Create new environment** to start to create a new environment and database.
3. In the **Environment name** field, enter a unique name. In the **Region** field, select the appropriate region.
4. Select the **Restrict access to database** check box if you want to enforce security.
5. Click **Create**.

## Create a database in the Entities pane of powerapps.com
1. On [powerapps.com](https://web.powerapps.com), expand the **Common Data Service** section and click or tap **Entities** in the left navigation pane.
2. Click **Get started**. The database is created in Open access mode.

## Open and restricted databases
By default, a database is created in Open access mode. In this mode, security for access to entities isn't enforced. The environment administrator can set the database to Restrict access mode. In this mode, security for access to entities is enforced, based on permission sets and roles.

1. On [admin center](https://admin.powerapps.com), in the left navigation pane, click **Environments**.
2. Select the environment.
3. On the **Database** tab, follow one of these steps:
   * To enforce security, select **Restrict access**.
   * To disable security, select **Open access**.

## License and security permissions
To create a database, you must be an administrator in the selected environment, and the appropriate license must be assigned to you. From the environment, you can further configure security permissions for other users by using the **Security** tab. For more information, see [Configure database security](database-security.md) and [Security model](https://docs.microsoft.com/common-data-service/entity-reference/security-model).

## Privacy notice
With the Microsoft PowerApps common data model we collect and store custom entity and field names in our diagnostic systems.  We use this knowledge to improve the common data model for our customers. The entity and field names that Creators create help us understand scenarios that are common across the Microsoft PowerApps community and ascertain gaps in the service’s standard entity coverage, such as schemas related to organizations. The data in the database tables associated with these entities is not accessed or used by Microsoft or replicated outside of the region in which the database is provisioned. Note, however, the custom entity and field names may be replicated across regions and are deleted in accordance with our data retention policies. Microsoft is committed to your privacy as described further in our [Trust Center](https://www.microsoft.com/trustcenter/Privacy/default.aspx).

