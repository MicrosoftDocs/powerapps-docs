---
title: Common Data Service for Apps Developer Overview | Microsoft Docs
description: Learn how developers can add value using Common Data Service for Apps.
services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: kvivek
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/20/2018
ms.author: jdaly
---
<!-- This topic was not migrated it was written for PowerApps -->
# Common Data Service for Apps Developer Overview

PowerApps offers users, businesses, independent software vendors (ISVs), and systems integrators (SIs) a powerful platform for building line-of-business apps. The new addition to PowerApps in this release is the expansion of the Common Data Service, now called Common Data Service for Apps which now contains the core functionality of the Dynamics 365 Customer Engagement platform that powers Dynamics 365 Customer Engagement for Sales, Marketing, Customer Service.

> [!NOTE]
> If you are already experienced with the the Dynamics 365 Customer Engagement for Sales, Marketing, or Customer Service apps, you will find that you will be able to apply your experience to customize and extend Common Data Service for Apps.


## Get Started

There are many aspects to how developers can contribute to creating apps that use CDS for Apps. While it is possible to build an application with code using CDS for Apps as your data source, most projects will use either model-driven driven apps or canvas apps to generate the experience that people will use. 

## Working with model-driven apps

Model-driven apps are built on CDS for apps. A model-driven app can only connect to a CDS for Apps environment and all the data that defines a model-driven app is stored within CDS for Apps.

Model-driven apps share the method of distributing customizations and extensions used by CDS for Apps: Solutions. You can learn more about solutions in [Introduction to solutions](introduction-solutions.md)

Model driven apps also have a number of points for developers to write code to extend. For information on what developers can do with model-driven apps, see [Model-driven apps Developer Overview](../model-driven-apps/overview.md)

## Understand when to write code

Because CDS for Apps includes many capabilities for people to configure custom business logic without writing code, the most common scenarios for developers to contribute involve filling spaces in-between where existing features may not provide functionality you need to meet a requirement. Fortunately, CDS for Apps provides many points for developers to extend the common functionality using code.

For a developer who will contribute to projects it is important that they understand what can be done without writing code. You should familiarize yourself with these capabilities. More information: [What is Common Data Service for Apps?](../../maker/common-data-service/data-platform-intro.md)

## Where to begin?

Where to begin depends on what problem you are trying to solve. This guide includes content about a wide range of capabilities and it is unlikely you will ever use all of them. The following includes several of the key areas to begin.

### Applying business logic

The most common extensions created using code involve automating the processes used by businesses. You can find a summary of options available for you in [Apply business logic with code](apply-business-logic-with-code.md). Each of these approaches are typically invoked based on events that occur on the server, so understanding of the [Event Framework](event-framework.md) will be valuable.

### Solutions

If you are going to distribute the extensions you create or any customizations that they depend on, you will need to understand solutions. Solutions created by an individual are relatively simple to work with and don't require the skills of a developer. But for a team of developers to work productively with solutions and use effective application lifecycle management principles requires a more sophisticated approach. More information:
 - [Introduction to solutions](introduction-solutions.md)
 - [How to manage solutions](how-manage-solutions.md)


### Authentication

When you create extensions that apply business logic on the server you will not need to include code to authenticate. The only times you will need to authenticate are when you are creating a client application. A simple console client application is a good way to familiarize yourself with the CDS for Apps APIs. Enabling a means to connect to the data is an important first step. Most of the code samples provided include a means to authenticate. The Xrm.Tooling connector provides capabilities to make authentication simpler. More information:
- [Authentication](authentication.md)
- [Create a client application](create-client-application.md)
- [Quick Start: Create a console app using the organization service](org-service/quick-start-org-service-console-app.md)
- [Simple Web API quick-start sample (C#)](webapi/simple-web-api-quick-start-sample-csharp.md)
- [Sample: Quick start for XRM Tooling API](xrm-tooling/sample-quick-start-xrm-tooling-api.md)

### Web services

There are two different web services you can use to work with data. Which one you should use depends on the type of project you are working on. For more information see [Use Common Data Service for Apps web services](use-web-services.md)

### Entities

Entities store the business data you will work with. An understanding what they are and how to work with them is essential.
More information:
- [Common Data Service for Apps entities](entities.md)
- [About the Entity Reference](reference/about-entity-reference.md)

## Content for on-premises deployments

CDS for Apps is not available for on-premise deployments at this time. Content in this guide does not include information about options that are only available for on-premises or internet facing (IFD) deployments. For information related to these options see the [Software Development Kit for Microsoft Dynamics 365 (online) and Dynamics 365 (on-premises)](https://msdn.microsoft.com/library/hh547453.aspx)


