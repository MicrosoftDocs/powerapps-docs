---
title: Model-driven sample apps
description: Understand how to get, customize, and remove model-driven sample apps.
documentationcenter: na
author: mr-dang-msft
manager: kvivek
ms.service: powerapps
ms.devlang: na
ms.topic: conceptual
ms.component: model
ms.date: 03/09/2020
ms.author: brdang
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Model-driven sample apps

In [powerapps.com](https://powerapps.com), use a sample app to explore design possibilities and discover concepts that you can apply as you develop your own apps. Each sample app uses fictitious data to showcase a real-world scenario. 

Be sure to check out documentation specific to each sample app for more details. 

> [!div class="mx-imgBorder"] 
> ![Fundraiser Sample App](media/overview-model-driven-samples/fundraiser-app1.png "Fundraiser sample app")


## Get sample apps

In order to play or edit model-driven sample apps, the apps must first be provisioned in a Common Data Service database. First create a trial environment and database and be sure to select **Deploy sample apps and data**.

> [!div class="mx-imgBorder"] 
> ![Create database](media/overview-model-driven-samples/create-database1.png "Create a database")

> [!IMPORTANT]
> This option installs all available sample apps in your database. Sample apps are for educational and demonstration purposes and we do not recommend installing them in production databases. 

## Customize a sample app

1. Sign in to [powerapps.com](https://powerapps.com)  

2. From the **Create** page, select the sample app and click **Create**.

> [!div class="mx-imgBorder"]
> <img src="media/overview-model-driven-samples/model-driven-create-page-sample.png" alt="Create a model-driven sample app" height="427" width="674">

3. The App designer will open providing multiple options for customizing the app.

4. For additional customization options, click **Advanced** from the left navigation in the portal.

## Remove sample apps and data 
- Deleting a sample app requires deleting the corresponding  [managed solution](https://docs.microsoft.com/dynamics365/customer-engagement/developer/uninstall-delete-solution). 
- Deleting the solution also deletes any sample data specific to the custom entities for the app.
- If customizations were made to the sample app, there may be [dependencies](https://docs.microsoft.com/dynamics365/customer-engagement/developer/dependency-tracking-solution-components), which must be removed before deleting the solution.

### Steps
1. Login to the [Power Apps admin portal](https://admin.powerapps.com).

2. Select an environment.

    > [!div class="mx-imgBorder"] 
    > ![Dynamics 365 Administration Center](media/overview-model-driven-samples/admin-center.png "Select an environment")

3. Click **Dynamics 365 Administration Center**.

4. Select your Database from the list and click **OPEN**.

    > [!div class="mx-imgBorder"] 
    > ![Select database](media/overview-model-driven-samples/select-database.png "Select a database")

5. Navigate to **Settings/Solutions**.

6. Select the solution for the app that is to be deleted and click **delete**.

    > [!div class="mx-imgBorder"] 
    > ![Delete solution](media/overview-model-driven-samples/delete-solution.png "Delete the solution")

*Alternatively navigate to the list of solutions by clicking **Advanced** in the maker portal and delete everything in the URL after .dynamics.com/*

> [!IMPORTANT]
> Do not delete other system solutions unless you're aware of the impact.

## Install or uninstall Sample Data
1. Follow steps 1-4 above.
2. Navigate to **Settings/Data Management/Sample Data**.
3. If sample data is installed, the option to remove is available. Otherwise the option to install is available. 

    > [!div class="mx-imgBorder"] 
    > ![remove sample data](media/overview-model-driven-samples/remove-sample-data.png "Remove sample data")




