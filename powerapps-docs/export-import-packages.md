---
title: Export and import resources | Microsoft Docs
description: Export and import resources
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
ms.date: 07/28/2017
ms.author: kfend

---
# Export and import resources
If you've created multiple environments to support the development of your database and apps, you must move changes from one environment to another environment. You can use **Export resources** and **Import resources** to move resources between environments.

## Why use multiple environments?
Each environment contains resources, such as entities, flows, and apps, that you create or modify during the development process. 

Typically, development is done in the same environment that is used by the organization's end users. This environment is known as the default environment. It's relatively easy to manage resource changes in the same environment. You validate the changes to make sure that all critical business processes and applications are functional, and then you release the app.

Sometimes, development and testing are done in separate environments, and changes are moved to the default environment when they are ready to be used by end users. There are several reasons why you might use separate environments. For example, you might have used a separate environment when you initially evaluated the system. Alternatively, you might want to minimize the risk that is involved when changes are made to the default environment. Separate environments provide isolation, because you make your changes in an environment that isn't the default environment. Depending on the extent of the risks, you might create an additional staging environment. In this case, you have a development environment, a staging environment, and a default environment.

## Moving resource changes
You move resources through separate export and import processes, by using a package (.zip) file. The package file is exported, saved to local storage, sent to the administrator of the target environment, and then imported into the target environment. The import process is often followed by validation testing to help guarantee that no critical business processes have been adversely affected.

The functionality for both resource import and resource export is available in the **Environments** section of the admin center. Both export and import occur in the context of a selected environment.

### Export resources
The export package will contain all changes to **entities, and picklists**. We are working to enable the export of more resource types such as apps, flows, connectors, roles and others. This option lets you move contents of one environment to another environment.

1. In the [admin center](https://admin.powerapps.com), in the left navigation pane, click **Environments**.
2. Select the source environment.
3. In the upper right, click **Export resources**.
4. Choose the resources you want to start with:
   1. Select the tab corresponding to a resource type you want to select, such as **Entities**.
   2. Select all resources under the type by clicking the header checkbox, or select resources individually.
   3. Click **Next**.
5. Include related resources if appropriate:
   1. If we discover any related resources, we will show you a pre-selected list.
   2. Exclude all related resources by clicking the header checkbox, or unselect resources individually.
   3. Click **Next**.
6. Add a **Name** for the exported package.
7. Optionally, you can customize setup actions to be performed upon import of resources:
   1. For each resource, click the **Import setup** to see a dialog.
   2. Select the setup action you want performed by default when this package is imported
   3. Click **Save**.
8. Click **Export**.
9. When export is completed, save the package file in local storage.

Alternatively, you can click **Select all resources** in the resource selection page to include all resources of all supported types in the final package, and go directly to the final export page.

### Import resources
The first step is to select a package file that was exported from the source environment. The import process validates, analyzes, and tries to import the package.

1. In the [admin center](https://admin.powerapps.com), in the navigation pane, click **Environments**.
2. Select the target environment.
3. In the upper right, click **Import resources**.
4. Click **Upload**, and browse to a package file in local storage.
5. Click **Next** to go to the final import page.
6. Resolve import validation errors and warnings:
   1. Look for warnings or errors, as indicated by the icon to the left of a resource **Name**.
   2. Click the **Import setup** field or the icon under **Action** for more information.
   3. Select an appropriate import setup action.
   4. The package being imported is automatically validated again.
7. Proceed to **Import** if there are no errors.

If the package is only partially applied, you receive an error message that describes what was imported and what wasn't imported.

## Resource types
The development process can involve changes to many types of resources. For example, if you update an app, you might add, remove, or update several entities or connections. Changes to some, and not all, resource types can be moved across environments. The following sections describe the types of resources that you can move.

### Entities, picklists
You can export and import entities, and picklists as follows:

* **Standard entities** – Only customizations are moved across environments. (You can't modify the out-of-box fields of standard entities.)
* **Custom entities** – Custom entities are moved across environments.
* **Custom picklists** – Custom picklists are moved across environments.

## Data
You can't move database data as part of the export and import of resources. To move data, you can use Microsoft Excel. For more information, see [Import or export data](maker/data-platform-export-data.md).

