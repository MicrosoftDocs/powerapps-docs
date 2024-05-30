---
title: Get insights from your Dataverse data
description: An overview of reporting and analytics options available in Dataverse and Dynamics 365 apps.
ms.date: 05/29/2024
ms.reviewer: matp 
ms.topic: "overview"
applies_to: 
  - "powerapps"
author: Milindav
ms.subservice: dataverse-maker
ms.author: Milindav
search.audienceType: 
  - maker
ms.custom: bap-template
---
# Get insights from your data

Microsoft Dataverse is the intelligent data platform that powers Dynamics 365 apps and the Power Platform. All Dynamics 365 data is hosted in Dataverse. The data included data from finance and operations apps and customer engagement apps like Dynamics 365 Sales and Dynamics 365 Customer Service. Dynamics 365 applications can be extended with Power Platform tools like Power Apps, Power Automate, and Power Pages for low-code and pro-code extensions. Data from Power Platform apps is also hosted in Dataverse.

When you understand the data and its intent, Dataverse provides turnkey capabilities in a consistent manner for all your data. Dataverse isn't just a database or storage, it encompasses everything needed to build integrated applications, processes, and in turn provides insights from the data it hosts. Dataverse also provides a comprehensive governance framework for your data including granular role based security and audit and compliance. Because it's a low-code data platform, developers can spend more time focusing on business needs through the configuration of the system and less time building infrastructure.

There are several approaches to getting insights from your data hosted by Dataverse:

- [Quick view](../../user/visualize-in-power-bi.md) is a data exploration feature built into Power Apps. When you build a low-code app, either by extending Dynamics 365 or with your own data, quick view is enabled by default. There's no need to create reports to inquire and explore data. You can save these reports as required and later extend them in Power BI Desktop - the authoring tool for Power BI.

- [Power BI with Dataverse data](use-powerbi-dataverse.md). As a low-code maker or a business analyst, you can use Power BI with Dataverse data to create rich reports and embed these reports within pages and forms in Power Apps.

- [Link to Fabric](azure-synapse-link-view-in-fabric.md) feature provides a no-copy, no-ETL, fully managed software as a service (SaaS) integration. The link to Microsoft Fabric feature enables data engineers and business analysts to use all the tools of Microsoft Fabric to combine Dataverse data with their own data.

- [Azure Synapse Link](export-to-data-lake.md) enables continuous export of data to your own Azure data lake and enables IT admins and data integration specialists to create data pipelines.

Data export service, bring your own device (BYOD), and Export to Data Lake were features introduced in Dynamics 365 apps to export data for analytics and data integration scenarios. These services enabled IT admins and specialists to export data into external databases or data lakes and build data integration pipelines. While we have improved these services over the years with updates, as part of unification of Dynamics 365 with the Power Platform, we rearchitected the same capabilities of these disparate services into simpler, unified experiences built into Power Apps (make.powerapps.com). When you transition to Fabric link or upgrading to Azure Synapse Link, these features provide you with an easy ramp to benefit from AI and Copilot investments in Dataverse and Fabric. Go to the [transition from legacy integration services](azure-synapse-link-transition-from-FnO.md) article for more information about how you can transition to Dataverse insights.
