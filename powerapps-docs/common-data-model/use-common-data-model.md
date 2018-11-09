---
title: Development using the Common Data Model | Microsoft Docs
description: "Provides information about how you can use the Common Data Model to develop apps and solutions."
author: RobertBruckner
ms.service: powerapps
ms.reviewer: anneta
ms.topic: article
ms.date: 07/24/2018
ms.author: robruc
---

# How to use the Common Data Model

With the Common Data Model (CDM), you can put your data into formats that represent concepts and activities that are commonly used and well understood. That way, you can query that data, reuse it, and interoperate with other businesses and apps that use the same format. This strategy matches that of, for example, manufacturers who produce AA batteries that fit in most remote controls. The CDM defines the size and shape of, for example, a **Contact** so that your app developers and business partners can parse that data and build your apps (or interoperate) with agility and confidence. The CDM is an open-source definition of standard entities and a metadata system that enable consistency of data and its meaning across apps and business processes.

Today, the CDM is used within Common Data Service (CDS) for Apps, which supports Dynamics and PowerApps, and the data-preparation capabilities in Power BI to create schematized files in Azure Data Lake.

![Common Data Model with CDS for Apps](media/cdm-with-cds.png)

You can use the CDM and CDS for Apps in these ways:

- **Securely store and manage your data in the CDM format**: You can use CDS for Apps to securely store and manage your data in the standardized format of the CDM. By doing so, you can then access and use that data in Microsoft apps and services such as Dynamics, PowerApps, Microsoft Flow, Power BI, or your own custom apps.

- **Create custom entities in the CDM**: The CDM is extensible, so you can create entities that are specific to your organization and populate them with your existing data using **Power Query**. With this approach, you can take advantage of the CDM and tailor it to your business.

- **Create your own repositories of data**: You can build repositories of data that adhere to the schema of the CDM and connect to those data sources using Microsoft data connectors. This lets you build custom line-of-business apps that use or share your data in the CDM, regardless of where the data originated or is stored.

- **Quickly derive and distribute insights using Power BI**: You can use advanced data-preparation services in Power BI that access your data stores in the CDM (such as data that you’ve put into CDS for Apps) to create reports and dashboards. Then you can create report-generating apps that automatically pull your data from the CDM into customized insights for individuals and groups in your organization.

- **Produce customized, organization-wide reports in Power BI**: You can use apps that automatically generate customized reports that you can place into Power BI workspaces for users in your organization and beyond.

Microsoft continues to extend the CDM in concert with many partners and subject-matter experts so that more industries, such as health
care, can benefit from the CDM and the platforms that support it.

## Data integration and Power Query Online

Both platforms that currently support CDM also offer data-integration experiences through Power Query Online that allow users to bring in data from a variety of sources, transform it if necessary, and then map it to standard entities in the CDM or create custom entities. Power Query Online leverages the same visual, self-service data-prep experience as Power Query within Excel and Power BI Desktop, so existing users can ramp up quickly.

![Map data with entities in CDM](media/cdm-map-entities.png)

## Common Data Service for Apps

By using CDS for Apps, you can jumpstart apps using the CDM with business logic, security, and integration already built in. The platform provides these benefits:

- **Leverage packaged business applications**: Many Microsoft Dynamics solutions and third-party apps are built on top of (or at least leverage) CDS for Apps. When your data is in the CDM, you can take advantage of those packaged applications.

- **Gain access to customized solutions**: Developers who understand and work with data in the CDM format have created an ecosystem of extensions and complete apps. For more information, see [introduction to solutions](https://docs.microsoft.com/powerapps/developer/common-data-service/introduction-solutions).

Whatever your intent, the CDM puts your data into a common format so that you can use, share, and analyze it more easily.

### Resources for CDS for Apps

- [What is CDS for Apps?](../maker/common-data-service/data-platform-intro.md)
- [Add data to an entity in CDS for Apps by using Power Query](../maker/common-data-service/data-platform-cds-newentity-pq.md)
- [Introduction to solutions](../developer/common-data-service/introduction-solutions.md)
- [Build a model-driven app](../maker/model-driven-apps/model-driven-app-overview.md)
- [Build a canvas app](../maker/canvas-apps/getting-started.md)
- [Create a flow that uses CDS for Apps](https://docs.microsoft.com/flow/common-data-model-intro)

## Power BI

You can use the dataflows feature of Power BI to ingest data into the CDM from Dynamics 365, Salesforce, Azure SQL Database, Excel, SharePoint, or another source. You create and manage dataflows in app workspaces by using the Power BI service, and the data itself is stored as entities in the CDM in Azure Data Lake Storage Gen2.

> [!NOTE]
> The dataflows functionality is in preview, and is subject to change and updates prior to general availability.

Similar to how spreadsheets handle recalculations for all affected formulas, dataflows manage changes for an entity or data element on your behalf, automating updates, and alleviating what used to be tedious and time consuming logic checks for even a basic data refresh. With dataflows and a few clicks, analysts and report creators can handle tasks that once required data scientists to oversee (and many hours or days to complete).

Organizations can incorporate dataflows in these ways, among others, to suit their needs:

- Customize standard entities and create their own.
- Create dataflows programmatically with custom definition files (model.json).
- Leverage powerful Azure products such as Azure Machine Learning, Azure Databricks, and Azure Data Factory.
- Add CSV data from Azure Blob Storage.
- Enjoy more storage, more frequent refreshes, incremental refresh, and computed and linked entities with Power BI Premium.

### Resources for Power BI

- [Self-service data prep in Power BI](https://docs.microsoft.com/power-bi/service-dataflows-overview)
- [Creating and using dataflows in Power BI](https://docs.microsoft.com/power-bi/service-dataflows-create-use)
- [Connect to data created by Power BI dataflows in Power BI Desktop](https://docs.microsoft.com/power-bi/desktop-connect-dataflows)
- [Developer resources for Power BI dataflows](https://docs.microsoft.com/power-bi/service-dataflows-developer-resources)