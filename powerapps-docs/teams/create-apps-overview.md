---
title: Create apps in Microsoft Teams by using Power Apps | Microsoft Docs
description: Provides an overview of creating apps in Microsoft Teams.
author: KumarVivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: intro-internal
ms.date: 12/18/2020
ms.subservice: teams
ms.author: kvivek
ms.reviewer: kvivek
contributors:
  - kvivek
  - tapanm-msft
---
# Create apps in Microsoft Teams by using Power Apps

With the significant number of enterprise employees working remotely, and millions of them meeting and collaborating through Microsoft Teams, there's significant interest in building low-code and no-code applications that can make remote work easier and more productive.

Introducing [Microsoft Dataverse for Teams](overview-data-platform.md) (formerly called Project Oakdale), a built-in, low-code data platform for Teams that empowers you to build custom apps and workflows in Teams by using Power Apps and Power Automate. Dataverse for Teams, built on [Microsoft Dataverse](../maker/data-platform/data-platform-intro.md) (formerly called Common Data Service), provides relational data storage, rich data types, enterprise-grade governance, and one-click solution deployment to the Teams app store.  

The new Power Apps app in Teams provides an integrated experience for app makers to create and edit apps and workflows within Teams, and quickly publish and share them for anyone on the team to use, without having to switch between multiple apps and services. With Power Apps Studio embedded in the Power Apps app in Teams and the new built-in data platform providing an easy-to-use, editable data table, you can quickly build apps based on custom data tables that are Teams-specific and scenario-specific.

![The app creation experience in Teams.](media/overview.png "The app creation experience in Teams, including the embedded Power Apps Studio experience")

To help organizations realize value faster, you can use *templates*, which are purpose-built apps for common application patterns that can be easily discovered and installed by members of the team. Although these templates can work without modification, members of the team can customize and extend them to meet the specific needs of their business.

Access and authorization align with the Microsoft Teams security model and include security groups that enable access for owners, members, and guests of the team that your app is associated with.

## Licensing requirements

The ability to create apps within Microsoft Teams will be available as part of select Microsoft 365 subscriptions. For detailed information, see [Licensing and restrictions](/power-platform/admin/about-teams-environment#licensing-and-restrictions) in the Power Platform admin guide.

## Get started with creating apps in Teams

There are two ways to use the apps created by using Power Apps in Teams:

- You can use the Power Apps app from the default Teams catalog as a personal app and create apps to share with teams in Teams. More information: [Install the Power Apps personal app](install-personal-app.md)

- You can install the apps created using Power Apps directly from the Microsoft Teams store. More information: [Use sample apps from Teams store](use-sample-apps-from-teams-store.md).

When you create an app in Teams with the Power Apps app for the first time, or install an app created with Power Apps from the app catalog for the first time, a new Dataverse for Teams environment is created for the selected team. The Dataverse for Teams environment is used to store, manage, and share team-specific data, apps, flows, and chatbots. Each team can have one Dataverse for Teams environment, and all data, apps, and flows created with the Power Apps app inside a team are available from that environment. More information: [About the Dataverse for Teams environment](/power-platform/admin/about-teams-environment)

When you create an app in Teams with the Power Apps app for the first time, or install an app created with Power Apps from the app catalog for the first time, you get to choose which team is responsible for customizing, maintaining, and sharing the app.

After selecting a team, we will create a new Dataverse for Teams environment if one doesn’t already exist. This will provide the necessary workspace for your team to collaborate on all your data, apps, flows, and bots. More information: [About the Dataverse for Teams environment](/power-platform/admin/about-teams-environment)

## Get started with creating flows and chatbots in Teams

You can create:

- Power Automate flows by using the new Power Apps app in Teams. More information: [Create flows using the Power Apps app in Teams](/power-automate/teams/create-flows-power-apps-app)

- Chatbots by using the new Power Virtual Agents app in Teams. More information: [Power Virtual Agents in Teams](/power-virtual-agents/teams/fundamentals-what-is-power-virtual-agents-teams)

### Next steps

[Install the Power Apps personal app](install-personal-app.md)<br/>
[Create your first app in Teams](create-first-app.md)

### Related topics
[Administer Dataverse for Teams environment](/power-platform/admin/about-teams-environment)


[!INCLUDE[footer-include](../includes/footer-banner.md)]