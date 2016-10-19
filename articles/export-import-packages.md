<properties
	pageTitle="Export and import resources | Microsoft PowerApps"
	description="Export and import resources"
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
   ms.date="10/19/2016"
   ms.author="robinr"/>

# Export and import resources
If you've created multiple environments to support the development of your database and apps, you must move changes from one environment to another environment. You can use **Export resources** and **Import resources** to move resources between environments.

## Why use multiple environments?
Each environment contains resources, such as entities, flows, and apps, that you create or modify during the development process. 

Typically, development is done in the same environment that is used by the organization's end users. This environment is known as the default environment. It's relatively easy to manage resource changes in the same environment. The app maker validates the changes to make sure that all critical business processes and applications are functional, and then releases the app.

Sometimes, development and testing are done in separate environments, and changes are moved to the default environment when they are ready to be used by end users. There are several reasons why you might use separate environments. For example, you might have used a separate environment when you initially evaluated the system. Alternatively, you might want to minimize the risk that is involved when changes are made to the default environment. Separate environments provide isolation, because you make your changes in an environment that isn't the default environment. Depending on the extent of the risks, you might create an additional staging environment. In this case, you have a development environment, a staging environment, and a default environment.

## Moving resource changes
You move resources through separate export and import processes, by using a package (.pkg) file. The package file is exported, saved to local storage, sent to the administrator of the target environment, and then imported into the target environment. The import process is often followed by validation testing to help guarantee that no critical business processes have been adversely affected.

The functionality for both resource import and resource export is available in the **Environments** section of the administrator portal. Both export and import occur in the context of a selected environment.

### Export all resources
If you select **All resources** as an option, the export package contains all changes to entities, picklists, translation sets, permission sets, and roles. This option lets you move all the contents of one environment to another environment.

1. On [admin.powerapps.com](https://admin.powerapps.com), in the left navigation pane, click **Environments**.
1. Select the source environment.
1. In the upper right, click **Export resources**.
1. When you receive an "Export completed" message, save the package file in local storage.

### Import resources

The first step is to select a package file that was exported from the source environment. The import process validates, analyzes, and tries to import the package.

1. On [admin.powerapps.com](https://admin.powerapps.com), in the navigation pane, click **Environments**.
1. Select the target environment.
1. In the upper right, click **Import resources**.
1. Click **Select**, and browse to a package file in local storage.
1. Click **Import**.

If the package is only partially applied, you receive an error message that describes what was imported and what wasn't imported.

## Resource types
The development process can involve changes to many types of resources. For example, if you update an app, you might add, remove, or update several entities or connections. Changes to most, if not all, resource types can be moved across environments. The following sections describe the types of resources that you can move.

### Entities, picklists, and translation sets
You can export and import entities, picklists, and translation sets as follows:

+ **Standard entities** – Customizations are moved across environments. (You can't modify the out-of-box fields of standard entities.)
+ **Custom entities** – Custom entities are moved across environments.
+ **Standard picklists** – Standard picklists are moved across environments. (You can't modify the out-of-box fields of standard pick lists.)
+ **Custom picklists** – Custom picklists are moved across environments.
+ **Translation sets** – Translation sets are moved across environments. For more information, see [Translation sets](translation-sets.md).

### Permission sets and roles
Permission sets and roles are security resources that help control access to the database. Both can be moved across environments. After you move permission sets and roles, you should make sure that the permission sets are referenced by the appropriate roles, and that the appropriate users are assigned to any new roles. For more information, see [Configure database security](database-security.md).

## Data
You can't move database data as part of the export and import of resources. To move data, you can use Microsoft Excel. For more information, see [Import or export data](data-platform-export-data.md).
