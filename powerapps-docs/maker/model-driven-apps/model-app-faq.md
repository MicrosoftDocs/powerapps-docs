---
title: Model-driven app FAQ | MicrosoftDocs
description: Understand the frequently asked questions about Power Apps model-driven apps
Keywords: 
author: alcerri
ms.author: alcerri
ms.reviewer: matp
manager: kvivek
ms.date: 12/02/2020
ms.service: powerapps
ms.topic: troubleshooting
applies_to: 
  - "powerapps"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Model-driven app frequently asked questions

These frequently asked questions (FAQ) can help you resolve issues that might occur when you work with model-driven apps.

## What is an app module?

The term *app module* has been used to describe model-driven apps, and *appmodule* is the name referenced in the Microsoft Dataverse and customer engagement apps schema. **Model-Driven App** is included in the display names for some of the tables referenced in Power Apps. For information about the `appmodule` table, go to [AppModule entity reference](../../developer/data-platform/reference/entities/appmodule.md). For information about using the `appmodule` table API, go to [Create, manage, and publish model-driven apps using code](../../developer/model-driven-apps/create-manage-model-driven-apps-using-code.md).

App modules, which are referred to as model-driven apps in Power Apps, are created and customized within a solution. Solutions are used for application lifecycle management, and you can use them to migrate customizations from one environment to another. It's beneficial to be familiar with the [solution layering](/power-platform/alm/solution-layers-alm) concepts.

## What's the best way to define and manage my model-driven app?

We recommend that you create your app in a dedicated solution. By creating a solution for your app, you can maintain your other solutions without creating any dependencies with your app. Only make changes to that solution when you want to update your app&mdash;for example, when you add, change, or remove components from the app. More information: [Create a solution](../data-platform/create-solution.md)

## Why can't I create a model-driven app?

The most common reasons you can't create model-driven apps are:

* Licensing
* Security
* Environment configuration

A Power Apps or Dynamics 365 license is required to create a model-driven app. More information: [Licensing requirements for tables in the Power Apps Licensing Guide](https://go.microsoft.com/fwlink/p/?linkid=2085130) and [Understanding Power Platform Licensing](/microsoft-365/community/powerplatformlicensingforcitizendeveloper)

Make sure you have sufficient privilege to create model-driven apps in your environment. More information:

* [About predefined security roles](share-model-driven-app.md#about-predefined-security-roles)
* [Environment permissions](/power-platform/admin/environments-overview#environment-permissions)

Additionally, you might be working with a restricted table. The following Dynamics 365 customer engagement applications include restricted tables:

* Dynamics 365 Sales
* Dynamics 365 Customer Service
* Dynamics 365 Field Service
* Dynamics 365 Marketing
* Dynamics 365 Project Service Automation

Make sure you have the appropriate Dynamics 365 application license when working with these tables. More information: [Restricted tables](../data-platform/data-platform-entity-licenses.md#restricted-tables)

## Why can't you see my model-driven app?

Make sure you have the appropriate privileges on the app. Work with your app maker or admin to ensure you have the proper security roles for the app.
More information:

* [Privileges required to view and access apps](app-visibility-privileges.md)
* [Share a model-driven app using Power Apps](share-model-driven-app.md)

## Why don't I see my model-driven app changes?

Make sure you publish your app customizations. More information:

* [Publish changes from Power Apps](../data-platform/create-solution.md#publish-changes)
* [Publish your model-driven app using code](../../developer/model-driven-apps/create-manage-model-driven-apps-using-code.md#publish-your-model-driven-app)

Also, verify your component changes in the active layer. You can use the solution layer feature in Power Apps to review solution layering for a component. More information: [View the solution layers for a component](../data-platform/solution-layers.md#view-the-solution-layers-for-a-component)

## How do I add more tables to my app?

The site map defines the navigation for your model-driven app. You add tables to a model-driven app's site map by using the site map designer. Tables that aren't included in the site map won't be available in your app. More information: [Create a model-driven app site map using the site map designer](create-site-map-app.md)

## How do I share my app?

You use security roles that contain the appropriate privileges and assign them to the users, teams, and apps you want. More information: [Share a model-driven app using Power Apps](share-model-driven-app.md)

## I'm a developer. Where do I get started?

Go to [Supported Customizations for Dataverse](../../developer/data-platform/supported-customizations.md).

## Why don't I see all the views after importing a solution?

A model-driven app change that was made by selecting **All** when selecting a component, such as a view, isn't reflected after importing an update to the app in the target environment. More information: [Newly added components don't appear in the app after importing an update to the app](../data-platform/import-update-export-solutions.md#newly-added-components-dont-appear-in-the-app-after-importing-an-update-to-the-app)

## What is `solutionaction`?

More advanced users can review the solution's customization.xml file. When you import a managed solution, customizations.xml might include the `solutionaction` property when you add and remove components. The possible values for `solutionaction` are:

* Added
* Removed
* Modified

This value specifies the changes in the current layer with respect to the previous managed layer. For example, on solution import, `solutionAction="Removed"` will remove the component from the app. More information: [*Microsoft.Crm.CrmInvalidOperationException: full formXml is expected to create a form message during solution import](../data-platform/import-update-export-solutions.md#microsoftcrmcrminvalidoperationexception-full-formxml-is-expected-to-create-a-form--message-during-solution-import)

## How do I get help?

* Search or post your questions in the [Power Apps Community](https://powerusers.microsoft.com/t5/Power-Apps-Community/ct-p/PowerApps1).
* Admins can [create support tickets](https://admin.powerplatform.microsoft.com/support).

### See also

[What are model-driven apps in Power Apps?](model-driven-app-overview.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]