---
title: Overview of building a model-driven app with Power Apps | Microsoft Docs
description: Step-by-step instructions for creating and configuring a table to use with a Power Apps model-driven app.
ms.custom: intro-internal
author: Mattp123
ms.service: powerapps
ms.topic: overview
ms.component: model
ms.date: 06/16/2020
ms.subservice: mda-maker
ms.author: matp
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
searchScope:
  - "Power Apps"
---
# What are model-driven apps in Power Apps?

## Model-driven apps overview

Model-driven app design is an approach that focuses on adding components such as [forms](../model-driven-apps/model-driven-app-glossary.md#form), [views](../model-driven-apps/model-driven-app-glossary.md#view), and [charts](../model-driven-apps/model-driven-app-glossary.md#chart) and [dashboards](../model-driven-apps/model-driven-app-glossary.md#dashboard) to [tables](model-driven-app-glossary.md#table) apps using an app designer tool. Additionally, [relationships](model-driven-app-glossary.md#relationship) tie tables together in a way that permits navigation between them and ensures that data is not repeated unnecessarily.

Using the app designer with little or no code, you can build apps that are **simple** or very **complex**.

### Process driven apps

Model-driven apps are especially well suited to **process driven** apps that are data dense and make it easy for users to move between related records. For example, if you are building an app to manage a complex process, such as onboarding new employees, managing a sales process, or member relationships in an organization such as a bank, a model-driven app is a great choice.

### Data modelling

Whilst we call them model-driven apps it is often easier to think of them as [data model](../model-driven-apps/model-driven-app-glossary.md#data-model) driven apps as without a data model housed within Microsoft [Dataverse](model-driven-app-glossary.md#dataverse) they cannot be created.

### User experience

From the perspective of users all model-driven apps offer a very similar **user experience**, that is both [accessible](model-driven-app-glossary.md#accessibility) to many users and to the device used.  The experience is similar to the diagram shown below.  

In this case we have one [dashboard](../model-driven-apps/model-driven-app-glossary.md#dashboard), containing multiple [charts](../model-driven-apps/model-driven-app-glossary.md#chart) and [views](../model-driven-apps/model-driven-app-glossary.md#view) in addition to being able to see 3 [tables](../model-driven-apps/model-driven-app-glossary.md#table).  We can navigate between the tables using the menus on the left hand side or via the [dashboard](../model-driven-apps/model-driven-app-glossary.md#dashboard).

:::image type="content" source="media/model-driven-app-overview/model-app-sample.png" alt-text="Sample model-driven app":::

## Benefits of the model-driven approach

Unlike [canvas app](../model-driven-apps/model-driven-app-glossary.md#canvas-app) development where the designer has complete control over app layout, with model-driven apps much of the user interface is determined for you and is largely designated by the [components](../model-driven-apps/model-driven-app-glossary.md#component) you add to the app.

There are some notable advantages to this method of application development.  

- Once the [data model](../model-driven-apps/model-driven-app-glossary.md#data-model) and [relationships](../model-driven-apps/model-driven-app-glossary.md#relationship) have been created the build process is **relatively rapid** due to rich component-focused no-code design environments
- Apps have a **similar user interface** across a variety of devices from desktop to mobile
- The apps are [**accessible**](../model-driven-apps/model-driven-app-glossary.md#accessibility) and [**responsive**](../model-driven-apps/model-driven-app-glossary.md#responsive-apps) automatically
- The user experience is **consistent** across all model-driven apps.  As such once a user is confident with one model-driven app later apps are much easier to adopt within an organization.
- Migrating apps between Development, Test and Production [Environments](../model-driven-apps/model-driven-app-glossary.md#environment) is relatively straightforward through the use of [solutions](../model-driven-apps/model-driven-app-glossary.md#solution)

[Learn more about the benefits of the model-driven approach](app-value-proposition.md)

## Model-driven and canvas apps compared

In canvas apps, the app maker has total control over the app layout. In model-driven apps, on the other hand, much of the layout is determined by the components you add. The emphasis is more on quickly viewing your business data and making decisions instead of on intricate app design.

|Category|Model-driven apps|Canvas Apps|  
|-----------|------------|------------|
|**Data integration**|Microsoft Dataverse only|Microsoft Dataverse + many others using connectors|
|**Design Experience**|No-code component focused design|Manipulation of control properties using Power Fx expressions|
|**UI control**|Limited, predominantly customisation|Full control|
|**App consistency**|High – differs predominantly based on the tables and views chosen|Often low, given the significant control the designers have of the user experience|
|**Migration between environments**|Simple|Potentially complex given that the datasources may need to be updated|
|**Speed of creation**|Rapid|Relative to the complexity of the design|
|**Responsive**|Automatically responsive|Only responsive if designed in this way|
|**Navigation through relationships**|Automatic, provided relationships exist|Only where designed and applied using Power Fx formulas|
|**Accessibility features**|Built in|Only if designed into the app|

## Steps to building and sharing a model driven app

At a fundamental level, model-driven app making consists of the following areas.

- Modeling business data
- Defining business processes
- Composing the app
- Configuring security roles
- Sharing your app

A large part of the time spent building the app is dedicated to modelling the business data and in some case to defining the business processes. Work on security roles will depend upon the needs of the organization.

[Learn more about the steps to building a model-driven app](app-building-steps.md)

## Using a model-driven app

Documentation has been developed that is dedicated to helping **users** of model driven apps to successfully navigate around them and interact with them in a way that lets them be more productive.

[Learn more about using model-driven apps](https://docs.microsoft.com/powerapps/user/use-model-driven-apps)

## Using solutions to assist with Application Lifecycle Management

[Application lifecycle management](../model-driven-apps/model-driven-app-glossary.md#application-lifecycle-management) is the way in which we develop an app from conception to end of life.

[Solutions](../model-driven-apps/model-driven-app-glossary.md#solution) are used to act as wrappers for all the elements required to deliver a product for use within a business.

As a minimum a model driven app requires a single table, a site map plus the app itself however they generally include an considerable amount more, and this includes canvas apps, roles, environment variables and much more.  

:::image type="content" source="../../maker/model-driven-apps/media/solution-assets-explorer.png" alt-text="Solution explorer":::

Solutions offer the means by which these elements can be migrated between environments.  Consequently, they are an important part of any application lifecycle management strategy.

It is regarded as best practice when creating model-driven apps that these are done so within a solution.

[Learn more about solutions](../../developer/data-platform/introduction-solutions.md)

[Create a solution](../../maker/data-platform/create-solution.md)

## Minimum requirements for building a model-driven app

Model-driven apps can be complex, however the minimum requirements for building them are relatively straightforward.  These are as follows :-

- A Microsoft Power Apps [license](https://docs.microsoft.com/power-platform/admin/pricing-billing-skus)
- [Capacity](https://docs.microsoft.com/power-platform/admin/capacity-storage) within the organization to create a Dataverse [Environment](model-driven-app-glossary.md#environment) (This is a function of the Power Apps and Dynamics licenses held)
- A Dataverse Environment
- Rights for the developer to work as an [administrator](https://docs.microsoft.com/power-platform/admin/database-security) within the environment
- A Dataverse [Database](model-driven-app-glossary.md#database) within the environment
- A [table](model-driven-app-glossary.md#table) (There are a number, including account which exist by default)
- One table [column](model-driven-app-glossary.md#column) (Every table has at least one column, and many system columns)
- One table [view](model-driven-app-glossary.md#view), to see records (There are a number by default)
- One table [form](model-driven-app-glossary.md#form), to enter data (There will be one by default)

Beyond this the model-driven app is created, in simple terms, by adding an table to a [site map](model-driven-app-glossary.md#site-map) using the [app designer](model-driven-app-glossary.md#app-designer), and running through the app validation and publishing process.

## Next steps

[Building a simple model-driven app](build-first-model-driven-app.md) is a great way to start.  You may wish to [Create a solution](../../maker/data-platform/create-solution) before you do so.

To go deeper into creating model-driven apps see [Steps to building a model-driven app](app-building-steps.md).

If you are new to Power Apps, and want to learn about how to convert your ideas into a fully working solution using Power Apps, start with [Planning a Power Apps project](../../guidance/planning/introduction.md).

[Understand model-driven app components](model-driven-app-components.md) will help you to understand some of the elements that make up a model-driven app.

[Learn about licensing for the Power Platform](https://docs.microsoft.com/power-platform/admin/pricing-billing-skus)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]