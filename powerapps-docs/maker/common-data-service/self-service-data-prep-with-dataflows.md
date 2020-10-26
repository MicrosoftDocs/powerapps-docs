---
title: "Self-service data prep with dataflows in Power Apps | MicrosoftDocs"
description: "Learn how to use dataflows in Power Apps to prepare your data"
ms.custom: ""
ms.date: 08/05/2019
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 
caps.latest.revision:
ms.author: "matp"
manager: "kvivek"
tags: 
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---


<!--note from editor: I think "dataflows" should be lowercase based on this entry in the Microsoft style guide (scroll down to find dataflows): https://styleguides.azurewebsites.net/Styleguide/Read?id=2696&topicid=42299 -->



# Self-service data prep with dataflows

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

As the volume of data continues to grow, so does the challenge of shaping that
data into well-structured, actionable information. You want data that’s ready for
apps, AI workloads, or analytics so that you can quickly turn volumes of
data into actionable insights. With self-service data prep in the Power Apps
portal, you can transform and load data to Common Data Service or your organization’s
Azure Data Lake Storage Gen2 account with just a few clicks.

Dataflows were introduced to help organizations unify data from disparate
sources and prepare it for consumption. You can easily create dataflows using
familiar, self-service tools to ingest, transform, integrate, and enrich big
data. When creating a dataflow, you will define data source connections, ETL (extract, transform, load)
logic, and destination to load the resulting data to. Once created, you can
configure a dataflow's refresh schedule to indicate how frequently it should
run. In addition, the new model-driven calculation engine makes the process of
data preparation more manageable, more deterministic, and less cumbersome for
dataflow customers. With dataflows, tasks that once required a data IT
organization to create and oversee (and many hours or days to complete) can now
be handled with a few clicks by individuals who aren’t even data scientists,
such as app creators, business analysts and report creators.


Dataflows store data in entities. An entity is a set of records used to store
data, similar to how a table stores data within a database. Customers can define
custom entity schema or leverage the Common Data Model’s standard entities.
The Common Data Model is a shared data language for business and analytical
applications to use. The Common Data Model metadata system enables consistency
of data and its meaning across applications and business processes such as
Power Apps, Power BI, some Dynamics 365 apps (model-driven apps), and Azure, which store data in conformance with the Common Data Model. A dataflow’s resulting entities can then be stored
in either of the following:

-   **Common Data Service.** Lets you securely store and manage data that's used
    by business applications built using Power Apps and Power Automate.

-   **Azure Data Lake Storage Gen2.** Lets you collaborate with people in your
    organization using Power BI, Azure Data, and AI services or custom-built line-of-business applications that read data from the lake. Dataflows that load
    data to an Azure Data Lake Storage Gen2 account store data in [Common Data Model
    folders](https://go.microsoft.com/fwlink/?linkid=2045304). **Common Data Model folders**
    contain schematized data and metadata in a standardized format to
    facilitate data exchange and to enable full interoperability across services
    that produce or consume data stored in an organization’s Azure Data Lake
    Storage account as the shared storage layer.

You can use dataflows to ingest data from a large and growing set of supported
on-premises and cloud-based data sources including Excel, Azure SQL Database,
SharePoint, Azure Data Explorer, Salesforce, Oracle database, and more.

After selecting the data source, you can use the Power Query low-code/no-code
experience to transform the data and map it to standard entities in the Common
Data Model or create custom entities. Advanced users can directly edit a
dataflow’s M-language to fully customize dataflows, similar to the Power Query
experience that millions of Power BI Desktop and Excel users already know.

Once you’ve created and saved a dataflow, you will need to run it in the cloud.
You can choose to trigger a dataflow to run manually or schedule the frequency
for the Power Platform Dataflow service to run it for you. When a dataflow
completes a run, its data is available to use. To get dataflow data loaded into
Common Data Service, the Common Data Service connector can be used in Power Apps,
Power Automate, Excel, and all other applications that support the Common Data Service
connector. To get from dataflows stored in your organization’s Azure Data Lake
Storage Gen2 account, you can used the Power Platform Dataflow connector in
Power BI Desktop or access the files directly in the lake.

## How to use dataflows
The previous section provided background on dataflows technology. In this
section, you get a tour of how dataflows can be used in an organization.

> [!NOTE]
> You must have a paid Power Apps plan to use dataflows, but you are not charged separately for using dataflows. 

### Load data to Common Data Service
Dataflows can be used to populate entities in the [Common Data
Service](https://docs.microsoft.com/powerapps/maker/common-data-service/data-platform-intro)
that are then used in Power Apps applications. With a few clicks, you can
integrate data from online and on-premises sources data sources.

<!--from editor: In the last sentence above, should it change to "...on-premises data sources." ? -->


### Extend the Common Data Model for your business needs
For organizations that want to extend and build upon the Common Data Model,
dataflows enable business intelligence professionals to customize the standard
entities or create new ones. This self-service approach to customizing the data
model can then be used with dataflows to build Power BI dashboards that are
tailored to an organization.

### Extend your capabilities with Azure Data and AI services
Power Platform dataflows can be configured to store dataflow data in your
organization’s Azure Data Lake Storage Gen2 account. When an environment is
connected to your organization's data lake, data scientists and developers can
leverage powerful Azure products such as Azure Machine Learning, Azure
Databricks, Azure Data Factory, and more.

For more information about Azure Data Lake Storage Gen2 and dataflows
integration, including how to create dataflows that reside in your
organization's Azure Data Lake, see [Connect Azure Data Lake Storage Gen2 for dataflow storage](connect-azure-data-lake-storage-for-dataflow.md).

## Summary of self-service data prep for big data in Power Apps
There are multiple scenarios and examples where dataflows can enable you to get
better control—and faster insights—from your business data. Other people in
your organization can leverage dataflows either via Common Data Service, the
Power Platform Dataflow connector in Power BI, or via direct access to Dataflow’s
**Common Data Service** folder in your organization’s Azure Data Lake Storage Gen2
account. Using a standard data model (schema) defined by the Common Data Model,
business applications can depend on an entity’s schema, and be abstracted from
how the data was created or from which data source. When a dataflow completes a
scheduled run, the data is ready for modeling and creation of apps, flows, or BI
insights in a very short period... in what used to take months, or longer, to
create.

The standardized format of the Common Data Model allows people in your
organization to create apps that generate quick, easy, and automatic visuals and
reports. Those include, but aren’t limited to:

-   Mapping your data from various sources to standard entities in the Common
    Data Model to unify data and leverage the known schema to drive
    out-of-the-box applications.

-   Creating your own custom entities to unify data across your organization.

-   Creating Power BI reports and dashboards that leverage dataflow data.

-   Creating integration with Azure Data and AI services via your organization’s
    Azure Data Lake Storage Gen2 account.

## Next steps

This article provided an overview of self-service data prep in the Power Apps portal,
and the ways you can use it. The following topics go into more detail about
common usage scenarios for dataflows:

-   [Creating and using dataflows in Power Apps](https://go.microsoft.com/fwlink/?linkid=2100076)

-   [Add data to an entity in Common Data Service](https://go.microsoft.com/fwlink/?linkid=2100075)

-   [Connect Azure Data Lake Storage Gen2 for dataflow storage](https://go.microsoft.com/fwlink/?linkid=2099973)

-   [Using dataflows with on-premises data sources](https://go.microsoft.com/fwlink/?linkid=2100077)

For more information about Power Query and scheduled refresh, you can read these
articles:

-   [Query overview in Power BI Desktop](/power-bi/desktop-query-overview)

-   [Configuring scheduled refresh](/power-bi/refresh-scheduled-refresh)

For more information about the Common Data Model, you can read its overview
article:

-   [Common Data Model - overview](/powerapps/common-data-model/overview)

