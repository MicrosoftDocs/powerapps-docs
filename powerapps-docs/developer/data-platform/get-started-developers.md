---
title: "Developers: Get started with Microsoft Dataverse | Microsoft Docs"
description: Learn how developers can add value using Microsoft Dataverse in Power Apps.
suite: powerapps
author: JimDaly
manager: ryjones
ms.service: powerapps
ms.date: 08/05/2019
ms.author: jdaly
ms.reviewer: "pehecke"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Developers: Get started with Microsoft Dataverse

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

Where to start depends on what problem you are trying to solve. This guide includes information about a wide range of capabilities and it is unlikely you will ever use all of them. The following sections include several of the key areas to begin.

## Work with data using Web services

There are two different web services that you can use to work with data: **Web API** and **Organization service**. 

Which one you should use depends on the type of project you are working on. More information: [Work with data using code](work-with-data.md)

## Applying business logic

The most common extensions created using code involve automating the processes used by businesses. You can find a summary of options available for you in [Apply business logic with code](apply-business-logic-with-code.md). Each of these approaches are typically invoked based on events that occur on the server, so understanding of the [Event Framework](event-framework.md) will be valuable.

## Integrate with external data

Data management capabilities in Dataverse not only lets you work with data within Dataverse, but also effectively interact with external data critical to your business. More information: 

- [Import data](/powerapps/developer/data-platform/import-data)
- [Synchronize data](/powerapps/developer/data-platform/data-synchronization)
- [Virtual entities](/powerapps/developer/data-platform/virtual-entities/get-started-ve)
- [Azure Integration](/powerapps/developer/data-platform/azure-integration)
- [Webhooks](/powerapps/developer/data-platform/use-webhooks
)

## Dataverse entities

Entities store the business data you will work with. An understanding what they are and how to work with them is essential.
More information:

- [Dataverse entities](entities.md)
- [About the Entity Reference](reference/about-entity-reference.md)

## Work with metadata

Developing a good working understanding of the metadata in the system can help you understand how Dataverse platform works. Generally you will use designers to add, update, or delete entity schema that defines metadata, but both the Web API and the Organization service web services provide capabilities to perform CRUD operations on the entity schema. More information: [Work with metadata using code](metadata-services.md) 

## Use solutions to package and distribute extensions

If you are going to distribute the extensions you create or any customizations that they depend on, you will need to understand solutions. Solutions created by an individual are relatively simple to work with and don't require the skills of a developer. But for a team of developers to work productively with solutions and use effective application lifecycle management principles requires a more sophisticated approach. More information:

 - [Introduction to solutions](introduction-solutions.md)
 - [SolutionPackager tool](compress-extract-solution-file-solutionpackager.md)
 - [Package Deployer tool](/power-platform/alm/package-deployer-tool)
 - [Publish your app on AppSource](publish-app-appsource.md)

## Create client applications and authentication

When you create extensions that apply business logic on the server you will not need to include code to authenticate. The only times you will need to authenticate are when you are [creating a client application](/powerapps/developer/data-platform/connect-dataverse). A simple console client application is a good way to familiarize yourself with the Dataverse APIs. Enabling a means to connect to the data is an important first step. Most of the code samples provided include a means to authenticate. The Xrm.Tooling connector provides capabilities to make authentication simpler. More information:

- [Authentication](authentication.md)
- [Build web applications using Server-to-Server (S2S) authentication](/powerapps/developer/data-platform/build-web-applications-server-server-s2s-authentication)
- [Build Windows client applications using XRM tools](/powerapps/developer/data-platform/xrm-tooling/build-windows-client-applications-xrm-tools)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]