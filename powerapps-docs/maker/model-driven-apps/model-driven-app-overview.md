---
title: Overview of building a model-driven app with Power Apps | Microsoft Docs
description: Step-by-step instructions for creating and configuring an entity to use with a Power Apps model-driven app.
author: Mattp123
ms.service: powerapps
ms.topic: conceptual
ms.component: model
ms.date: 06/16/2020
ms.author: matp
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# What are model-driven apps in Power Apps?

Model-driven app design is a component-focused approach to app development. Model-driven app design doesn’t require code and the apps you make can be simple or very complex.  Unlike canvas app development where the designer has complete control over app layout, with model-driven apps much of the layout is determined for you and largely designated by the components you add to the app.

:::row:::
   :::column span="":::
      <img src="../media/index/i_get-started.svg" alt="Overview icon" width="80"/><br><br>**Get started** <br /> Get started with model-driven apps<Br><ul><li>[Overview](overview.md)</li><li>[Motivation](motivation.md)</li><li>[Download](<https://aka.ms/coestarterkitdownload>)</li></ul>
   :::column-end:::
   :::column span="":::
      <img src="../media/index/i_model-driven-apps.svg" alt="Overview icon" width="80"/><br><br>**Design and build**  <br /> Build a model-driven app<br><ul><li>[Understand model-driven app components](model-driven-app-components.md)</li><li>[Define data](define-data-model-driven-app.md)</li><li>[Deep dive](power-bi.md)</li></ul>
   :::column-end:::
   :::column span="":::
      <img src="media/i_setup.svg" alt="Overview icon" width="80"/><br><br>**Govern** <br />   Establish audit and compliance processes <br><ul><li>[Set up](setup-governance-components.md)</li><li>[Use](governance-components.md)</li><li>[Deep dive](example-processes.md)</li></ul>
   :::column-end:::
   :::column span="":::
      <img src="media/i_get-started.svg" alt="Overview icon" width="80"/><br><br>**Nurture** <Br>Accelerate your adoption by thriving with a community of makers <br><ul><li>[Set up](setup-nurture-components.md)</li><li>[Use](nurture-components.md)</li></ul>
   :::column-end:::
:::row-end:::

Model-driven app design provides the following benefits:
- Rich component-focused no-code design environments 
- Create complex responsive apps with a similar UI across a variety of devices from desktop to mobile
- Rich design capability 
- Your app can be distributed as a solution

![Sample model-driven app](media/model-driven-app-overview/model-app-sample.png)
 
## The approach to model-driven app making
At a fundamental level, model-driven app making consists of three key focus areas.

- Modeling business data 
- Defining business processes 
- Composing the app

### Modeling business data
To model business data you determine what data your app will need and how that data will relate to other data. Model-driven design uses a metadata-driven architecture so that designers can customize the application without writing code. Metadata means “data about data” and it defines the structure of the data stored in the system. [Tutorial: Create a custom entity that has components in Power Apps](../common-data-service/create-custom-entity.md)

### Defining business processes
Defining and enforcing consistent business processes is a key aspect of model-driven app design. Consistent processes help make sure your app users focus on their work and not on remembering to perform a set of manual steps. Processes can be simple or complex and often change over time. To create a process, from the PowerApps.com Model-driven area select ![Settings](media/powerapps-gear.png) > **Advanced customizations** > **Open solution explorer**. Next, on the left navigation pane in solution explorer select **Processes**, and then select **New**. More information: [Business process flows overview](/flow/business-process-flows-overview) and [Apply business logic with Common Data Service](../common-data-service/cds-processes.md). 

### Composing the model-driven app
After modeling data and defining processes, you build your app by selecting and configuring the components you need using the app designer.

![App designer](media/model-driven-app-overview/app-designer.png)

If you are new to Power Apps, and want to learn about how to convert your ideas into a fully working solution using Power Apps, start with [Planning a Power Apps project](/powerapps/guidance/planning/introduction).

## Next steps

[Build your first model-driven app](build-first-model-driven-app.md)

[Understand model-driven app components](model-driven-app-components.md)

