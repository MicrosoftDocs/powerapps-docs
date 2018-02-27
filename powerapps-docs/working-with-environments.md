---
title: Working with environments | Microsoft Docs
description: Switch environments and understand how the content on your pages change.
services: ''
suite: powerapps
documentationcenter: na
author: linhtranms
manager: anneta
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 10/14/2016
ms.author: litran

---
# Working with environments and Microsoft PowerApps
With PowerApps, you can work in different environments and easily switch among them. For an overview of environments, see [Environments overview](environments-overview.md), which explains in detail why you use environments and how you can create and manage them. The scope of this article will cover the following topics on environment:

* how to switch the environment on powerapps.com
* how to an create app in the right environment
* how to view an app in the right environment

## Switch the environment
When you sign up and first sign in to powerapps.com, you will likely land in a default environment. You can verify this by looking at the upper-right corner of the page.

![Default environment](./media/working-with-environments/env-dropdown.png)

The *Default environment* is accessible to everyone. You can start creating apps in this environment and share your apps with other users. You may also have access to other environments, such as those you [create yourself](administrator/environments-administration.md) or those created by others but you have access to. You can switch environments by clicking the environment dropdown in the upper-right corner and selecting a different environment. In this example, I am switching from *Default environment* to *Environment 1*.

![Switch environment](./media/working-with-environments/switch-env.png)

Once you switch to a different environment (such as Environment 1), you will see all the apps you created or have access to in this new environment.

## Create apps in the right environment
You can create apps in existing environments that you have access to or in a new environment. Creating your own environment, however, requires a specific plan. For more information, see [this topic](pricing-billing-skus.md). Before you create an app, always **make sure you select the environment you want to app to be in**. Otherwise, you will have to deal with moving apps between environments.

1. If you are in [powerapps.com](http://web.powerapps.com), select the environment you would like to create your app in. If you are in *PowerApps Studio* or *PowerApps Studio for web*, skip to step 4.

2. Select **+ New app**.

3. Select **Open PowerApps Studio** or **PowerApps Studio for web**.

4. When *PowerApps Studio* or *PowerApps Studio* for web opens, select the environment again at the top right corner. We will improve this experience in the future but, in the current release, you must select this every time you want to create an app in a new environment.

    ![Studio switch environment](./media/working-with-environments/studio-switch-env.PNG)

5. On the **Account** page, select **Change** next to the name of the current environment.

    ![Studio switch environment](./media/working-with-environments/studio-env-dropdown.PNG)

6. Select the environment you want to create your app in.

    ![Studio switch environment](./media/working-with-environments/studio-env-dropdown2.PNG)

7. Select **New** to start creating an app. Your app now will reside in the environment you selected in step 6.

    ![Studio switch environment](./media/working-with-environments/new-app.PNG)

## View apps in the right environment
Whether you are working in [powerapps.com](http://web.powerapps.com), PowerApps Studio for Windows, or PowerApps Studio for web, the list of apps, connections, etc. that you see is always filtered based on the environment that's selected in the dropdown. If you don't see the apps you are looking for, always confirm whether the right environment is selected.

Again, to switch environments in [powerapps.com](http://web.powerapps.com):

![Switch environment](./media/working-with-environments/switch-env.png)

To switch environments in PowerApps Studio for Windows or PowerApps Studio for web:

![Studio switch environment](./media/working-with-environments/studio-switch-env.PNG)

For more information about environments, see [this overview](environments-overview.md).
