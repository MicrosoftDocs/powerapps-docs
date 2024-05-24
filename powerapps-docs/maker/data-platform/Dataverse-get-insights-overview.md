---
title: Get insights from your Dataverse data
description: An overview of reporting and analytics options available in Dataverse and Dynamics 365 apps
ms.date: 05/29/2024
ms.reviewer: matp 
ms.topic: "concepts"
applies_to: 
  - "powerapps"
author: Milindav
ms.subservice: dataverse-maker
ms.author: Milindav
search.audienceType: 
  - maker
ms.custom: bap-template
---
# Transition from legacy data generation services
Dataverse is the intelligent data platform that powers Dynamics 365 apps as well as the Power platform. All Dynamics 365 data, including those from finance and operations apps as well as customer engagement apps like Sales, customer service are hosted by Dataverse. Dynamics 365 applications can be extended with Power platform tools like Power Apps, Power automate, and Power pages for low-code and pro-code extensions. Data from Power platform apps in turn are also hosted by Dataverse.

By understanding the data and its intent, Dataverse provides turnkey capabilities in a consistent manner for all its data. It’s not just a database or storage, it encompasses everything that is needed to build integrated applications, processes, and in turn provides insights from the data it hosts. Dataverse also provides a comprehensive governance framework for your data including granular role based security as well as audit and compliance. And because it is a low-code data platform, developers can spend more time focusing on business needs through the configuration of the system and less time building infrastructure.

There are several approaches to getting insights from your data hosted by Dataverse. 

Quick view is a data exploration feature built into Power Apps. When you build a Low code app either by extending Dynamics 365 or with your own data, quick view is enabled by default – no need to create reports to inquire and explore data. 

Power BI connector to Dataverse enables creating real-time Power BI reports.

Link to Fabric feature provides a no-copy, no-ETL, fully managed software as a service (SaaS) integration. Link to Fabric feature enables Data engineers and business analysts to use all the tools of Fabric to combine Dataverse data with their own data.

Synapse Link enables continuous export of data similar to BYOD, Export to Data lake or DES services. This option is enabled for IT admins and data integration specialists.

Data export service (DES), BYOD, Export to Data lake were features introduced in Dynamics 365 apps to export data for analytics and data integration scenarios. These services enabled IT admins and specialists to export data into external databases or data lakes and build data integration pipelines. While we have improved these services over the years with updates, as part of unification of Dynamics 365 with the power platform, we have rearchitected the same capabilities of these disparate services into simpler, unified experiences built into Power Apps maker portal. By Transitioning to Fabric Link or upgrading to Synapse Link, provides you with an easy ramp to benefit from AI and Copilot investments in Dataverse and Microsoft Fabric. 
