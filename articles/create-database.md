<properties
	pageTitle="Create a Common Data Service database | Microsoft PowerApps"
	description="Create a Common Data Service database."
	services="powerapps"
	documentationCenter="na"
	authors="nimakms"
	manager="robinarh"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="10/16/2016"
   ms.author="robinr"/>

# Create a Common Data Service database
You can create a database and build apps by using Common Data Service as a data store. You can either create your own custom entities or use the predefined entities. To create a database in an environment, you must be an administrator, and the appropriate license must be assigned to you.

There are three ways to create database:

+ In the Admin Portal
+ In the Maker Portal
+ In the **Entities** pane

## Create a database in the Admin Portal
1. On [admin.powerapps.com](https://admin.powerapps.com), in the left navigation pane, click **Environments**.
1. Select the environment.
1. On the **Database** tab, click **Create a database**. By default, the database is created in Open access mode.
1. If you want to enforce security, select **Restrict access**.

## Create a database in the Maker Portal
1. On [powerapps.com](https://web.powerapps.com), in the left navigation pane, click **Home**.
1. In the **Use the Microsoft Common Data Service** section, look for the button that is named either **Create database** or **Get started**. The button's name depends on your license and permission assignments. You might not be allowed to create a database in the current environment.

### Create database
1. Click **Create database**.
1. In the dialog box, select the **Restrict access to database** check box if you want to enforce security.
1. Click **Create my database**.

### Get started
1. Click **Get started**.
1. In the dialog box, click **Create new environment** to start to create a new environment and database.
1. In the **Environment name** field, enter a unique name. In the **Region** field, select the appropriate region.
1. Select the **Restrict access to database** check box if you want to enforce security.
1. Click **Create**.

## Create a database in the Entities pane
1. On [powerapps.com](https://web.powerapps.com), in the left navigation pane, click **Entities**.
1. Click **Create a database**. The database is created in Open access mode.

## Open and restricted databases
By default, a database is created in Open access mode. In this mode, security for access to entities isn't enforced. The environment administrator can set the database to Restrict access mode. In this mode, security for access to entities is enforced, based on permission sets and roles.

1. On [admin.powerapps.com](https://admin.powerapps.com), in the left navigation pane, click **Environments**.
1. Select the environment.
1. On the **Database** tab, follow one of these steps:
    + To enforce security, select **Restrict access**.
    + To disable security, select **Open access**.

## License and security permissions
To create a database, you must be an administrator in the selected environment, and the appropriate license must be assigned to you. From the environment, you can further configure security permissions for other users by using the **Security** tab. For more information, see [Secure the database](database-security.md).
