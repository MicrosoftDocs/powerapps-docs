---
title: "Developers: Get started with Microsoft Dataverse | Microsoft Docs"
description: Learn about some available methods that developers can use to access business data, customize business logic, write applications, and access external systems.
suite: powerapps
author: JimDaly
ms.date: 08/20/2026
ms.subservice: dataverse-developer
ms.author: jdaly
ms.reviewer: pehecke
ms.collection: get-started
search.audienceType: 
  - developer
---

# Developers: Get started with Microsoft Dataverse

Where you start depends on the problem you're trying to solve. This guide includes information about a wide range of capabilities, and it's unlikely you'll ever use all of them. The following sections include several of the key areas to begin.

## Work with data using web services

There are two different access points, each using a different protocol, for the business data web service: a RESTful (OData) data access point, and the Organization service endpoint. Your code can access the OData access point by using the Web API, or the Organization service endpoint by using the SDK for .NET.

Which one you should use depends on the type of project you're working on. For more information, see [Work with data using code](work-with-data.md).

## Apply business logic

The most common extensions created by using code involve automating the processes used by businesses. You can find a summary of options available for you in [Apply business logic with code](apply-business-logic-with-code.md). Each of these approaches is typically invoked based on events that occur on the server, so understanding of the [Event Framework](event-framework.md) is valuable.

This developer guide provides documentation for how to write custom business logic by using the documented APIs. However, it's much easier to write and deploy your code if you install and use [Power Platform Tools for Visual Studio](tools/devtools-install.md).

## Integrate with external data

Data management capabilities in Dataverse not only let you work with data within Dataverse, but also effectively interact with external data that's critical to your business. For more information, see: 

- [Import data](/powerapps/developer/data-platform/import-data)
- [Synchronize data](/powerapps/developer/data-platform/data-synchronization)
- [Virtual tables](/powerapps/developer/data-platform/virtual-entities/get-started-ve)
- [Azure Integration](/powerapps/developer/data-platform/azure-integration)
- [Webhooks](/powerapps/developer/data-platform/use-webhooks
)

## Dataverse tables

Tables store the business data you work with. It's essential to understand what they are and how to work with them.

More information:

- [Dataverse tables](entities.md)
- [About table/entity Reference](reference/about-entity-reference.md)

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

## Work with table definitions

If you develop a good working understanding of the *metadata* (data that describes data) in the system, you can better understand how the Dataverse platform works. In general, use designers to add, update, or delete table columns that store business data. You can also define metadata that provides more information about a table or column. For example, most tables have a "Name" column, and there's metadata that describes if that column is required, when it was modified, and by whom. Both the Web API and SDK for .NET provide capabilities to perform common operations on the table definition and other metadata. For more information, see [Work with metadata using code](metadata-services.md). 

## Use solutions to package and distribute extensions

If you distribute the extensions you create or any customizations that they depend on, you need to understand solutions. Solutions that an individual creates are relatively simple to work with and don't require the skills of a developer. But for a team of developers to work productively with solutions and use effective application lifecycle management principles requires a more sophisticated approach. For more information, see:

 - [Introduction to solutions](introduction-solutions.md)
 - [SolutionPackager tool](/power-platform/alm/solution-packager-tool)
 - [Package Deployer tool](/power-platform/alm/package-deployer-tool)
 - [Publish your app on Marketplace](/power-platform/developer/appsource/publish-app)

## Create client applications and authentication

When you create extensions that apply business logic on the server, you don't need to include code to authenticate. The only times you need to authenticate are when you are [creating a client application](./connect-dataverse.md). A simple console client application is a good way to familiarize yourself with the Dataverse APIs. Enabling a way to connect to the data is an important first step. Most of the code samples provided include a way to authenticate. The Xrm.Tooling connector provides capabilities to make authentication simpler. For more information, see:

- [Authentication](authentication.md)
- [Build web applications using Server-to-Server (S2S) authentication](./build-web-applications-server-server-s2s-authentication.md)
- [Build Windows client applications using XRM tools](./xrm-tooling/build-windows-client-applications-xrm-tools.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
