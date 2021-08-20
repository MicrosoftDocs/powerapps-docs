---
title: Sign in to Power Apps for the first time
description: Learn about signing in to Power Apps for the first time, choosing an environment, creating an app, playing or editing an app, and other common tasks.
author: tapanm-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: intro-internal
ms.reviewer: 
ms.date: 06/15/2021
ms.subservice: canvas-maker
ms.author: tapanm
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
---
# Sign in to Power Apps for the first time

When you sign in to [Power Apps](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), the site offers you a variety of options for creating your own apps, opening apps that you or others have created, and performing related tasks. These tasks range from the most simple, such as identifying the license or licenses that give you access, to more advanced capabilities like creating custom connections to specific data sources.

You can select options in three general areas:

- The header along the top of the page

    ![Header for environment selection.](media/intro-maker-portal/header.png)

- The navigation bar along the left side of the page

    ![Navigation bar.](media/intro-maker-portal/nav-bar.png)

- The large icons that feature prominently in the middle of the page

    ![Center area of the home page.](media/intro-maker-portal/center-area.png)

For best results, start by ensuring that the home page is set to the right environment.

## Choose an environment

Whether you're creating an app, a flow, a data connection, or a table in Microsoft Dataverse, much of what you do in Power Apps is contained in a specific environment. Environments create boundaries between different types of work. For example, an organization might have separate environments for different departments. Many organizations use environments to separate apps that are still being developed from those that are ready for widespread use. You might have access to multiple environments or only one. If you have the appropriate permissions, you might even be able to create your own environments.

To verify which environment you're in, find the environment switcher near the right side of the header.

![Environment switcher.](media/intro-maker-portal/environment-switcher.png)

If you create an app in one environment, you won't be able to see it from another environment. In addition, people who want to run your app must have access to the environment in which you created it.

> [!IMPORTANT]
> - To view the environment list in the environment switcher in Power Apps, you must have the Environment Maker, System Customizer, or System Administrator security role in the environment. For information about predefined security roles, see [Predfined security roles](/power-platform/admin/database-security#predefined-security-roles) in the Microsoft Power Platform admin guide.
> - Make sure that you're in the right environment *before* you create an app, a flow, or a similar component. You can't easily move components from one environment to another.

> [!NOTE]
> Every member in an organization can access [the default environment](https://docs.microsoft.com/power-platform/admin/environments-overview#the-default-environment). Like any environment, users can see apps where they have sufficient privileges to access an app. 
>
> All users with the Environment Maker security role in an environment can see all model driven apps in that environment, including the default environment. You can learn more about model driven app privileges to view and access apps [here](https://docs.microsoft.com/en-us/powerapps/maker/model-driven-apps/app-visibility-privileges).

For more information, see [Environments overview](/power-platform/admin/environments-overview).

## Choose an app type

In Power Apps, you can create and run these types of apps:

- **Canvas apps** support designing custom UI and connecting to data from a variety of sources.
- **Model-driven apps** have a standard UI and connect to data only in Dataverse. However, you can more easily create other elements such as views, dashboards, and different types of business logic.
- **Portals** help you create external-facing websites that allow users outside your organization to sign in with a wide variety of identities, create and view data in Dataverse, or even browse content anonymously.

If you choose an [environment that has a Dataverse database](/power-platform/admin/create-environment#create-an-environment-with-a-database), you can build canvas or model-driven apps from the same **Home** page.

## Play or edit an app

If you've created an app (or someone else has created one and shared it with you), you can play or edit it from the **Home** page or the **Apps** page.

On the **Apps** page, you can filter the list of apps based on criteria such as whether you opened it recently.

![list of apps.](./media/intro-maker-portal/find-apps.png)

You can also search for an app by typing one or more characters in the search bar, which appears near the upper-right corner. When you find the app you want, select the banner icon to play or edit the app.

## Create an app, portal, chatbot, or AI model

From the **Home** page, you can create apps, portals, chatbots, and AI models:

- [Get started with canvas apps](/powerapps/maker/canvas-apps/)
- [Get started with model-driven apps](/powerapps/maker/model-driven-apps/)
- [Get started with portals](/powerapps/maker/portals/)
- [Get started with chatbots](/powerapps/chatbots)
- [Get started with AI models](/powerapps/use-ai-builder)

## Learn more

You can find more information about either canvas apps or model-driven apps in two ways:

- In the left navigation bar, select **Learn**.
- In the header, select the question mark icon.

    ![List of model-driven apps with an ellipsis menu open.](media/intro-maker-portal/help-icon.png)

Both options show links to this documentation set, Power Apps training on Microsoft Learn, the Power Apps Community (where you can share information with users in other organizations), and the Power Apps blog (where the newest features are announced).

## Other common tasks

By selecting options in the header and left navigation bar, you can do more than create and open apps, portals, chatbots, and AI models.

### From the header

- Select the down arrow to download mobile and other clients in which you can run apps.

    For more information, see [Find and run apps](../../user/index.md).

- Select the gear icon to perform tasks such as connecting to data sources, identifying your Power Apps license or licenses, and opening the page where you can perform administrative tasks.

    For more information, see these topics:

  - [Overview of canvas-app connectors](connections-list.md)
  - [Build and certify custom connectors for canvas apps](register-custom-api.md)
  - [Manage an on-premises data gateway](gateway-management.md)
  - [Administer Power Apps](/power-platform/admin/admin-guide)
  - [Licensing overview](/power-platform/admin/pricing-billing-skus)
  - [Overview of building a model-driven app](../model-driven-apps/model-driven-app-overview.md)

### From the left navigation bar

Extend the functionality of your apps by performing these tasks:

- Manage tables, choices, and data integration in [Dataverse](../data-platform/data-platform-intro.md)
- Configure business logic in [Power Automate](/flow/getting-started)
- Author, package, and maintain [solutions](../../developer/data-platform/introduction-solutions.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]

