---
title: "Overview of performance insights in Power Apps | MicrosoftDocs"
description: Understand performance insights. 
ms.custom: ""
ms.date: 06/15/2021
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "overview"
applies_to: 
  - "powerapps"
author: "Mattp123"
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# What are performance insights?

Performance insights is a self-service tool for enterprise app makers that analyzes runtime telemetry data and provides a prioritized list of recommendations to help improve the performance of model-driven apps. This feature provides a daily set of analytic insights related to the performance of a Power Apps standalone model-driven or Dynamics 365 customer engagement app, such as Dynamics 365 Sales or Dynamics 365 Service, with recommendations and actionable items. Enterprise app makers can view detailed performance insights at an app-level in the [Power Apps portal](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).

## How to access 

1. Go to [make.powerapps.com](https://make.powerapps.com). 
1. On the left navigation pane, select **Apps**, and then select a model-driven app in the app list.
1. Use the ... context menu or command bar to select **Performance**.

If you want to switch the environment in which your app is deployed, you can switch environments in the top right corner of the page using the **Environment** selector. Additionally, you can navigate to performance insights from a model-driven app’s context menu from the **Solutions** area. 

> [!IMPORTANT]
> Since recommendations are generated using telemetry data, we recommend that you view performance insights from an environment where the app will be used, such as a production environment.

## How insights are generated

Performance insights are generated based on collected telemetry data of your model-driven app every 24 hours. When end-users use an app, key telemetry data recorded by the Power Apps platform is stored. The performance insights engine leverages this data and analyzes it to generate insights and recommendations related to performance enhancements.  

Performance insights are available for all model-driven apps in your selected environment, provided there is recorded telemetry data. You can view insights history for the previous seven days, as long as there was usage on the selected date, by selecting a date in the drop down.

