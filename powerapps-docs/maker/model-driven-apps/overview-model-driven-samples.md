---
title: Model-driven sample apps
description: Understand how to get, customize, and remove model-driven sample apps.
documentationcenter: na
author: caburk
manager: kvivek
ms.service: powerapps
ms.devlang: na
ms.topic: conceptual
ms.component: model
ms.date: 03/08/2018
ms.author: caburk

---

# Model-driven sample apps

In [powerapps.com](https://powerapps.com), use a sample app to explore design possibilities and discover concepts that you can apply as you develop your own apps. Each sample app uses fictitious data to showcase a real-world scenario. 

Be sure to check out documentation specific to each sample app for more details. 

![Fundraiser Sample App](media/overview-model-driven-samples/fundraiser-app1.png)


## Get sample apps

In order to play or edit model-driven sample apps, the apps must first be provisioned in a Common Data Service database. First create a trial environment and database and be sure to check **Include sample apps and data**.

![Create database](media/overview-model-driven-samples/create-database1.png)


> [!IMPORTANT]
> This option installs all available sample apps in your database. Sample apps are for educational and demonstration purposes and we do not recommend installing them in production databases. 

## Customize a sample app

1. Sign in to [powerapps.com](https://powerapps.com) and chose **Model-driven** for the design mode. 

    ![Choose design mode](media/overview-model-driven-samples/choose-design-mode.png)

2. From the Home page, hover over the sample app and click **Customize**.
3. The App designer will open providing multiple options for customizing the app. 
4. For additonal customization options, click **Advanced** from the left navigation in the portal.

## Remove sample apps and data 
- Deleting a sample app requires deleting the corresponsing  [managed solution](https://docs.microsoft.com/dynamics365/customer-engagement/developer/uninstall-delete-solution). 
- Deleting the solution also deletes any sample data specific to the custom entities for the app.
- If customizations were made to the sample app, there may be [dependencies](https://docs.microsoft.com/dynamics365/customer-engagement/developer/dependency-tracking-solution-components), which must be removed before deleting the solution.

### Steps
1. Login to the [PowerApps admin portal](https://admin.powerapps.com).

2. Select an environment.

3. Click **Dynamics 365 Administration Center** 

    ![Dynamics 365 Administration Center](media/overview-model-driven-samples/admin-center.png)

4. Select your Database from the list and click **OPEN**.

    ![Select database](media/overview-model-driven-samples/select-database.png)

5. Navigate to **Settings/Solutions**.

6. Select the solution for the app that is to be deleted and click **delete**.

    ![Delete solution](media/overview-model-driven-samples/delete-solution.png)

*Alternatively navigate to the list of solutions by clicking **Advanced** in the maker portal and delete everything in the URL after .dynamics.com/*

> [!IMPORTANT]
> Do not delete other system solutions unless you're aware of the impact.

## Install or uninstall Sample Data
1. Follow steps 1-4 above.
2. Navigate to **Settings/Data Management/Sample Data**.
3. If sample data is installed, the option to remove is available. Otherwise the option to install is available. 

    ![remove sample data](media/overview-model-driven-samples/remove-sample-data.png)




