---
title: API connector overview | Microsoft Docs
description: ISVs and SaaS service owners can build connectors and have them certified by Microsoft.
services: ''
suite: powerapps
documentationcenter: na
author: mgblythe
manager: anneta
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 05/06/2017
ms.author: mblythe

---
# API connector overview (PowerApps)
An **API connector** is an OpenAPI (Swagger) based wrapper around a REST API that allows the underlying service to talk to [Microsoft Flow](https://flow.microsoft.com), [PowerApps](https://powerapps.microsoft.com), and [Logic Apps](https://docs.microsoft.com/azure/logic-apps/). It provides a way for users to connect their accounts and leverage a set of pre-built **triggers** and **actions** to build their apps and workflows.

As an **Independent software vendor (ISV)** or **SaaS service owner**, you can build connectors to enable a wide range of business and productivity scenarios for your users. A connector helps you to go beyond a definite set of integrations, and increase the reach, discoverability, and usage of your service.

## Requirements
To build and submit a connector, your service must meet the following requirements:

* Business user scenario that fits well with Microsoft Flow, PowerApps, and Logic Apps
* Publicly available service with stable REST APIs

## Build your connector
The first step to building an API Connector is to build a fully functional custom connector. A custom connector operates exactly like an API connector but it is limited in availability to its author and specific users within the author's tenant.

The process to build a connector involves multiple steps:

![API connector authoring steps](./media/api-connectors-overview/authoring-steps.png)

[Learn more](api-connector-dev.md) about how to develop an API connector.

## Submit for certification
After you've built a connector, you submit it for certification. As part of our third party certification process, Microsoft reviews the connector before publishing.

This process validates the functionality of your connector in Microsoft Flow and PowerApps, and checks for technical and content compliance.

[Learn more](api-connector-submission.md) about the process to submit your connector for certification and publishing.

## Get support
For onboarding and development support, please email [condevhelp@microsoft.com](mailto:condevhelp@microsoft.com). This account is actively monitored and managed. Developer queries and incidents will quickly find their way to the appropriate team.

