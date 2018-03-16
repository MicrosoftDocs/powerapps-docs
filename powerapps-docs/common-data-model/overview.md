---
title: Common Data Model Overview | Microsoft Docs
description: Learn how the common data model connects the Common Data Service for Apps with the Common Data Service for Analytics.
services: ''
suite: powerapps
documentationcenter: na
author: RobertBruckner
manager: lmollico
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/14/2018
ms.author: jdaly
---

# Common Data Model Overview

The **Common Data Model** (CDM) provides a library of entities that represent commonly used concepts and activities across a variety of business and application domains. CDM offers well-defined, modular, and extensible business entities such as Account, Business Unit, Case, Contact, Lead, Opportunity, and Product, as well as interactions and relationships between vendors, workers, and customers, such as activities, and service level agreements. 

With CDM at the center of the [Common Data Service for Apps](../maker/common-data-service/data-platform-intro.md) and the Common Data Service for Analytics<!-- TODO add link -->, packaged applications and analytical solutions can work with well-defined entity shapes and share data, irrespective of where data is originally coming from or mastered. At the same time, customized line of business apps and analytical solutions can leverage the same entities and share data, and thereby support the specific needs of your business requirements. 

The Common Data Model simplifies the challenges of data management by unifying data in a known form with *structural and semantic consistency across applications and deployments*. It helps integrate and *disambiguate data* collected from business processes, digital interactions, product telemetry, people interactions, and more. 

Data present in the Common Data Service for Apps, integrates easily into the Common Data Service for Analytics. You can start from enterprise and transactional data you already own (e.g. leads and campaign information, previous customer purchases, etc.), and combine with data from other sources (e.g. search engines, product telemetry, etc.) to get a unified picture. The following diagrame shows applications leveraging Common Data Model entities, with data integration across CDS for Apps and CDS for Analytics.

![Applications leveraging Common Data Model entities, with Data Integration across CDS for Apps and CDS for Analytics.](media/cdm-overview.png)

The Common Data Model is fully extensible - you can add fields to any of the entities that come with the CDM or create your own custom entities. The CDM standard defines a common language for business entities covering customer relationship management (CRM), marketing, product services, and will expand to enterprise resource planning (ERP), finance & operations, and additional areas over time. The goal of CDM is to enable data interoperability spanning multiple channels, service implementations, and vendors.


The Common Data Model and Common Data Service provide a rich and productive development platform through the following features:

- **Common Data Model** – The Common Data Model simplifies the challenges of data management by unifying data in a known form with structural and semantic consistency across applications and deployments. The public CDM GitHub repository ([https://github.com/Microsoft/CDM](https://github.com/Microsoft/CDM)) will be continuously enhanced with entities from customer relationship management, marketing, product services, finance & operations, additional vertical industry data models, and cross-spanning sources such as surveys, search engines, product telemetry, and more.
- **Data integration** – You can quickly and easily import data from your existing systems using a built-in browser-based Power Query experience for seamlessly and visually transforming and combining data from cloud and on-premises sources. <!-- TODO add link -->
 
     The data import includes mapping to standard entities of the Common Data Model, as well as defining, mapping, and loading as new entities. Data integration & mapping templates accelerate connecting to common data sources such as Salesforce.com; these data mapping templates are fully customizable and extensible. 
 
     The following screenshot shows ingesting external data and mapping to standard entities 

    ![Ingest of external data and mapping to standard entities](media/cdm-mapping-entities.png)
 
- **Extensibility** You can extend the entities without breaking data sharing with other apps.
- **Robustness**  Because you can depend on common entities, you can build reusable components that are bound to the entities. The Common Data Model supports extensibility and versioning that protects your development investment.
- **Entity consistency across deployments** Your solutions can connect information from productivity platforms with data from business applications. For example, you can connect a calendar appointment or a Microsoft Outlook task with a sales opportunity. 

The Common Data Service for Apps provides several key capabilities over the Common Data Model including:

- **Packaged applications**: Dynamics 365 apps like the Marketing, Sales, Service, Talent, Finance and Operations apps to transform your business.
- **Customize applications and build native extensions for you needs**: Customizers and developers distribute application solutions so that organizations can use the Common Data Service for Apps to install and uninstall the business functionality defined by the solution. See [Introduction to solutions](../developer/common-data-service/introduction-solutions.md).
- **Build model-driven apps and canvas apps with PowerApp**s: For information about creating apps with the Common Data Service and PowerApps<!-- TODO:  see [Overview of building a model-driven app](../model-driven-app-overview.md). -->.
- **Automate business processes with Flow**: For information about creating a flow that uses the Common Data Service, see [Create a flow that uses the Common Data Service](/flow/common-data-model-intro).

The preview of the Common Data Service for Analytics provides several key capabilities over the Common Data Model including:

- **Packaged analytical solutions, and customize analytical solutions leveraging standard data entities** Applications such as Sales Insights to track historical sales performance, provide you consistent insights regardless of where the data was originally mastered; because the data integration experience maps data from other sources (e.g. Salesforce.com) to Common Data Model entity shapes, and simplifies your analytical solution to focus on the data semantics of well-defined entities such as Leads, Opportunities, etc.
- **No-code/low-code Power Query data integration** Create, populate, transform and enrich entities, using an evolution of the Power Query experience. Your Excel and Power BI data transformation skills transfer seamlessly. 
- **Bring your own storage** You can leverage the Azure data stack to make data available to the Common Data Service for Analytics. The entities are stored in the same common data model format, and data recognized by analytical solutions.
