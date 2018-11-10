---
title: "Developers: Get started with Common Data Service for Apps | Microsoft Docs"
description: Learn how developers can add value using Common Data Service for Apps in PowerApps.
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
ms.date: 10/31/2018
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Developers: Get started with Common Data Service for Apps

There are many aspects to how developers can contribute to creating apps that use Common Data Service (CDS) for Apps. While it is possible to build an application with code using CDS for Apps as your data source, most projects will use either model-driven driven apps or canvas apps to generate the experience that people will use. 

## Working with model-driven apps

Model-driven apps are built on CDS for Apps. A model-driven app can only connect to a CDS for Apps environment and all the data that defines a model-driven app is stored within CDS for Apps.

Model-driven apps share the method of distributing customizations and extensions used by CDS for Apps: Solutions. You can learn more about solutions in [Introduction to solutions](introduction-solutions.md)

Model driven apps also have a number of points for developers to write code to extend. For information on what developers can do with model-driven apps, see [Model-driven apps Developer Overview](../model-driven-apps/overview.md)

## Understand when to write code

Because CDS for Apps includes many capabilities for people to configure custom business logic without writing code, the most common scenarios for developers to contribute involve filling spaces in-between where existing features may not provide functionality you need to meet a requirement. Fortunately, CDS for Apps provides many points for developers to extend the common functionality using code.

For a developer who will contribute to projects it is important that they understand what can be done without writing code. You should familiarize yourself with these capabilities. More information: [What is Common Data Service for Apps?](../../maker/common-data-service/data-platform-intro.md)

## Where to begin?

Where to begin depends on what problem you are trying to solve. This guide includes content about a wide range of capabilities and it is unlikely you will ever use all of them. The following includes several of the key areas to begin.

> [Work with data using web services](#work-with-data-using-web-services)<br/>
> [Applying business logic](#applying-business-logic)<br/>
> [CDS for Apps entities](#cds-for-apps-entities)<br/>
> [Work with metadata](#work-with-metadata)<br/>
> [Use solutions to package and distribute extensions](#use-solutions-to-package-and-distribute-extensions)<br/>
> [Create client applications and authentication](#create-client-applications-and-authentication)<br/>
> [Content for on-premises deployments](#content-for-on-premises-deployments)<br/>

### Work with data using Web services

There are two different web services that you can use to work with data. Which one you should use depends on the type of project you are working on. More information: [Work with data using code](work-with-data-cds.md)

### Applying business logic

The most common extensions created using code involve automating the processes used by businesses. You can find a summary of options available for you in [Apply business logic with code](apply-business-logic-with-code.md). Each of these approaches are typically invoked based on events that occur on the server, so understanding of the [Event Framework](event-framework.md) will be valuable.

### CDS for Apps entities

Entities store the business data you will work with. An understanding what they are and how to work with them is essential.
More information:

- [Common Data Service for Apps entities](entities.md)
- [About the Entity Reference](reference/about-entity-reference.md)

### Work with metadata

Developing a good working understanding of the metadata in the system can help you understand how CDS for Apps platform works. Generally you will use designers to add, update, or delete entity schema that defines metadata, but both the Web API and the Organization service web services provide capabilities to perform CRUD operations on the entity schema. More information: [Work with metadata using code](metadata-services.md) 

### Use solutions to package and distribute extensions

If you are going to distribute the extensions you create or any customizations that they depend on, you will need to understand solutions. Solutions created by an individual are relatively simple to work with and don't require the skills of a developer. But for a team of developers to work productively with solutions and use effective application lifecycle management principles requires a more sophisticated approach. More information:

 - [Introduction to solutions](introduction-solutions.md)
 - [SolutionPackager toolSolutionPackager tool](compress-extract-solution-file-solutionpackager.md)
 - [Package Deployer tool](./package-deployer/create-packages-package-deployer.md)
 - [Publish your app on AppSource](publish-app-appsource.md)

### Create client applications and authentication

When you create extensions that apply business logic on the server you will not need to include code to authenticate. The only times you will need to authenticate are when you are creating a client application. A simple console client application is a good way to familiarize yourself with the CDS for Apps APIs. Enabling a means to connect to the data is an important first step. Most of the code samples provided include a means to authenticate. The Xrm.Tooling connector provides capabilities to make authentication simpler. More information:

- [Authentication](authentication.md)
- [Create Client applications](connect-cds.md)
- [Quick Start: Create a console app using the organization service](org-service/quick-start-org-service-console-app.md)
- [Quick Start: Web API sample (C#)](webapi/quick-start-console-app-csharp.md)
- [Sample: Quick start for XRM Tooling API](xrm-tooling/sample-quick-start-xrm-tooling-api.md)

## Content for on-premises deployments

CDS for Apps is not available for on-premise deployments at this time. Content in this guide does not include information about options that are only available for on-premises or internet facing deployments(IFD). For information related to these options, see the [Software Development Kit for Microsoft Dynamics 365 (online) and Dynamics 365 (on-premises)](https://msdn.microsoft.com/library/hh547453.aspx).