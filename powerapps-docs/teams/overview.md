---
title: Teams integration - Overview | Microsoft Docs
description: Provides an overview of creating apps in Microsoft Teams.
author: KumarVivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 09/03/2020
ms.author: kvivek
ms.reviewer: 
---
# Create apps in Teams using Power Apps

[!INCLUDE [cc-beta-prerelease-disclaimer.md](../includes/cc-beta-prerelease-disclaimer.md)]

With the significant number of enterprise employees working remotely and millions of them meeting and collaborating through Microsoft Teams, there’s been significant interest in building low code and no code applications that could make remote work easier and more productive.

Introducing *Project Oakdale*, a built-in, low-code data platform for Microsoft Teams that empowers users to build custom apps and workflows in Teams using Power Apps and Power Automate. Project Oakdale&mdash;built on Common Data Service&mdash;provides relational data storage, rich data types, enterprise-grade governance, and one-click solution deployment to Teams app store.  

The new *Power Apps app* in Teams provides an integrated experience for app makers to create and edit apps and workflows within Teams and quickly publish and share them for anyone on the team to use without having to switch between multiple apps and services. With the Power Apps Studio embedded in the Power Apps app in Teams and the new built-in data platform providing an easy-to-use editable data table, users can quickly build apps based on custom data tables that are Teams and scenario specific.

![App creation experience in Microsoft Teams](media/overview.png "App creation experience in Microsoft Teams including the embedded Power Apps Studio experience")

> [!IMPORTANT]
> - This is a preview feature.
> - [!INCLUDE[cc_preview_features_definition](../includes/cc-preview-features-definition.md)]

To help organizations realize value faster, you can use *templates* that are purpose-built apps for common application patterns that can be easily discovered and installed by members of the team. While these templates can work without modification, members of the team can customize and extend them to meet the specific needs of their business.

Access and authorization align with the Microsoft Teams security model and include security groups that enable access for owners, members, and guests of the Microsoft Team your app is associated with.  

## Get started with creating apps in Teams

There are two ways to use the apps created using Power Apps in Teams. 
- You can use the Power Apps app from the default Teams catalog as a personal app and create apps to share with teams in Microsoft Teams. More information: [Install the Power Apps personal app](install-personal-app.md) 
 
- You can install the apps created using Power Apps directly from the Microsoft Teams catalog that are published using Microsoft AppSource or the organization’s app catalog. More information: [Embed an app in Teams](../maker/canvas-apps/embed-teams-app.md).

When you create an app in Teams using Power Apps app for the first time or install a Power Apps app from the app catalog for the first time, a new Project Oakdale environment is created for the selected team. The Project Oakdale environment is used to store, manage, and share team-specific data, apps, flows, and chatbots. Each team can have one environment and all data, apps, and flows created using the Power Apps app inside a team are available from that team's Project Oakdale environment. More information: [About the Project Oakdale environment](/power-platform/admin/about-teams-environment).

## Get started with creating flows and chatbots in Teams

You can create:
- Power Automate flows using the Power Apps app in Teams. For more information, see [Create flows using the Power Apps app in Teams](/power-automate/teams/create-flows-power-apps-app) in Power Automate docs. 

- Chatbots using the Power Virtual Agents app in Teams. For more information, see [TODO: Add link] in Power Virtual Agents docs.

### Next steps

[Install the Power Apps personal app](install-personal-app.md)<br/>
[Create your first app in Teams](create-first-app.md)
