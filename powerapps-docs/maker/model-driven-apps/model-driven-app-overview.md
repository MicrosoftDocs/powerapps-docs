---
title: Overview of building a model-driven app with Power Apps
description: Step-by-step instructions for creating and configuring a table to use with a Power Apps model-driven app.
author: Mattp123
ms.topic: overview
ms.component: model
ms.date: 01/09/2026
ms.subservice: mda-maker
ms.author: matp
search.audienceType: 
  - maker
searchScope:
  - "Power Apps"
---
# What are model-driven apps in Power Apps?

## Model-driven apps overview

Model-driven app design is an approach that focuses on adding components such as [forms](../model-driven-apps/model-driven-app-glossary.md#form), [views](../model-driven-apps/model-driven-app-glossary.md#view), [charts](../model-driven-apps/model-driven-app-glossary.md#chart), and [dashboards](../model-driven-apps/model-driven-app-glossary.md#dashboard) to [tables](model-driven-app-glossary.md#table) using an app designer tool. Additionally, [relationships](model-driven-app-glossary.md#relationship) connect tables together in a way that permits navigation between them and ensures that data isn't repeated unnecessarily.

Using the app designer with little or no code, you can build apps that are simple or complex.

:::image type="content" source="media/create-app.png" alt-text="App designer with account and contact table added" lightbox="media/create-app.png":::

### Process driven apps

Model-driven apps are especially well suited to process driven apps that are data dense and make it easy for users to move between related records. For example, if you're building an app to manage a complex process, such as onboarding new employees, managing a sales process, or member relationships in an organization such as a bank, a model-driven app is a great choice.

### Data modeling

Although we call them *model-driven apps*, it's often easier to think of them as [data model](../model-driven-apps/model-driven-app-glossary.md#data-model) driven apps. This is because, without a data model housed within [Microsoft Dataverse](model-driven-app-glossary.md#dataverse), you can't create a model-driven app.

### User experience

From the user's perspective, all model-driven apps offer a similar experience, which is both [accessible](model-driven-app-glossary.md#accessibility) to many users and to the device used. The experience is similar to the diagram shown here.  

In this example, the app contains three [tables](../model-driven-apps/model-driven-app-glossary.md#table) (challenges, ideas, team projects), one [dashboard](../model-driven-apps/model-driven-app-glossary.md#dashboard), and multiple [charts](../model-driven-apps/model-driven-app-glossary.md#chart) and [views](../model-driven-apps/model-driven-app-glossary.md#view). Users navigate between the tables using the left pane or via the dashboard.

:::image type="content" source="media/model-driven-app-overview/model-app-sample.png" alt-text="Sample model-driven app":::

## Benefits of the model-driven approach

Unlike [canvas app](../model-driven-apps/model-driven-app-glossary.md#canvas-app) development where the designer has complete control over app layout, with model-driven apps much of the user interface is determined for you and is largely designated by the [components](../model-driven-apps/model-driven-app-glossary.md#component) you add to the app.

There are some notable advantages to this method of application development.  

- Once the [data model](../model-driven-apps/model-driven-app-glossary.md#data-model) and [relationships](../model-driven-apps/model-driven-app-glossary.md#relationship) are created, the build process is relatively rapid due to rich component-focused no-code designers.
- Apps have a similar user interface across various devices from desktop to mobile.
- The apps are [**accessible**](../model-driven-apps/model-driven-app-glossary.md#accessibility) and [**responsive**](../model-driven-apps/model-driven-app-glossary.md#responsive-apps) automatically.
- The user experience is consistent across all model-driven apps. Once a user is confident with one model-driven app, later apps are easier to adopt within an organization.
- Migrating apps between development, test, and production [environments](../model-driven-apps/model-driven-app-glossary.md#environment) is relatively straightforward by using [solutions](../model-driven-apps/model-driven-app-glossary.md#solution).

[Learn more about the benefits of the model-driven approach](app-value-proposition.md)

## Model-driven and canvas apps compared

In canvas apps, the app maker has total control over the app layout. With model-driven apps, much of the layout is determined by the components you add. The emphasis is more on quickly viewing your business data and making decisions instead of on intricate app design.

|Category|Model-driven apps|Canvas apps|  
|-----------|------------|------------|
|**Data platform**| Dataverse only| Dataverse + many others using connectors|
|**Design experience**|No-code component focused design|Manipulation of control properties using Power Fx expressions|
|**UI control**|Limited, predominantly customization|Full control|
|**App consistency**|High – differs predominantly based on the tables and views chosen|Often low, given the significant control the designers have of the user experience|
|**Migration between environments**|Simple|Potentially complex given that the datasources might need to be updated|
|**Speed of creation**|Rapid|Relative to the complexity of the design|
|**Responsive**|Automatically responsive|Only responsive if designed in this way|
|**Navigation through relationships**|Automatic, provided relationships exist|Only where designed and applied using Power Fx formulas|
|**Accessibility features**|Built in|Designed into the app: [Create accessible canvas apps](../canvas-apps/accessible-apps.md)|

## Steps to building and sharing a model-driven app

At a fundamental level, model-driven app making consists of the following areas.

- Modeling business data
- Defining business processes
- Composing the app
- Configuring security roles
- Sharing your app

A large part of the time spent building the app is dedicated to modeling the business data and in some case to defining the business processes. Customizing security roles depend on the needs of the organization.

[Learn more about the steps to building a model-driven app](app-building-steps.md)

## Using a model-driven app

Documentation has been developed that helps users successfully navigate around and interact with model-driven apps in a way that helps make them more productive.

[Learn more about using model-driven apps](../../user/use-model-driven-apps.md)

You can use model-driven apps on a mobile device and run them in offline mode.

- [Get started with Power Apps mobile](../../mobile/run-powerapps-on-mobile.md)

- [Mobile offline overview (preview)](../../mobile/mobile-offline-overview.md)

## Using solutions to assist with application lifecycle management

[Application lifecycle management](../model-driven-apps/model-driven-app-glossary.md#application-lifecycle-management) (ALM) is the way in which we develop an app from conception to end of life.

[Solutions](../model-driven-apps/model-driven-app-glossary.md#solution) are used to act as wrappers for all the elements required to deliver a product for use within a business.

As a minimum, a model-driven app requires a single table, a site map, plus the app itself. However, model-driven apps generally include a considerable amount more, and this includes canvas apps, security roles, environment variables, and much more.  

:::image type="content" source="../../maker/model-driven-apps/media/solution-assets-explorer.png" alt-text="Solution explorer" lightbox="../../maker/model-driven-apps/media/solution-assets-explorer.png":::

Solutions offer the means by which these objects can be migrated between environments. Consequently, solutions are an important part of any application lifecycle management strategy.

When you create a model-driven app, you should create it within a solution.

- [Learn more about solutions](../../developer/data-platform/introduction-solutions.md)
- [Create a solution](../../maker/data-platform/create-solution.md)

## Minimum requirements for building a model-driven app

Model-driven apps can be complex. However, the minimum requirements for building them are relatively straightforward.

- A Microsoft Power Apps [license](/power-platform/admin/pricing-billing-skus).
- [Capacity](/power-platform/admin/capacity-storage) to create a Power Platform [environment](model-driven-app-glossary.md#environment). This is a feature of the Power Apps and Dynamics 365 licenses held.
- A Power Platform environment.
- A Dataverse [database](model-driven-app-glossary.md#database) within the environment. This is selected when you create an environment. More information: [Create an environment with a database](/power-platform/admin/create-environment#create-an-environment-with-a-database)
- Privileges for the maker to work as a system customizer or environment maker in the environment where the model-driven app is created. More information: [About predefined security roles](share-model-driven-app.md#about-predefined-security-roles)
- A [table](model-driven-app-glossary.md#table). (There are many standard tables, including account, which exist by default.)
- One table [column](model-driven-app-glossary.md#column). (Every table has at least one column, and many system columns.)
- One table [view](model-driven-app-glossary.md#view), to view records. (There are a number by default.)
- One table [form](model-driven-app-glossary.md#form), to enter data. (There will be one by default.)

Using the [app designer](model-driven-app-glossary.md#app-designer), a model-driven app is created by adding a page, which adds navigation to the app, and is typically based on a table or [custom page](model-app-page-overview.md).

## Next steps

[Learn about the value of model-driven apps](app-value-proposition.md)

[Building a simple model-driven app](build-first-model-driven-app.md) is a great way to start.  You might wish to [Create a solution](../../maker/data-platform/create-solution.md) before you do so.

To go deeper into creating model-driven apps, go to [Steps to building a model-driven app](app-building-steps.md).

If you're new to Power Apps, and want to learn about how to convert your ideas into a fully working solution using Power Apps, start with [Planning a Power Apps project](../../guidance/planning/introduction.md).

[Understand model-driven app components](model-driven-app-components.md) helps you understand some of the elements that make up a model-driven app.

[Learn about licensing for the Power Platform](/power-platform/admin/pricing-billing-skus)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
