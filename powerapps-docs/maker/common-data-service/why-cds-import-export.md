---
title: "Importing and exporting data | MicrosoftDocs"
ms.custom: ""
ms.date: 06/16/2020
ms.reviewer: "Mattp123"
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "powerapps"
author: "mmercuri"
ms.author: "mmercuri"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Importing and exporting data
----------------------------

There are multiple ways to import and export data into Common Data Service. You can use Dataflows, Power Query, Azure Data Factory, Logic Apps, and Power Automate.

Dynamics customers also have access to the Data Export Service.

## Dataflows 

Dataflows enable you to connect with business data from various sources, clean the data, transform it, and then load it into Common Data Service. 
Dataflows supports tens of popular on-premises, cloud, and SaaS data sources.

Power Query is a data connection technology that enables you to discover, connect, combine, and refine data sources to meet your analysis needs. Features in Power Query are available in Excel and Power BI Desktop. 

![Datflows and Power Query with Common Data Service](media/dataflows-power-query-with-cds.png)

More information: [Create and use dataflows in Power Apps](/powerapps/maker/common-data-service/create-and-use-dataflows). 

More information: [Add data to an entity in Common Data Service by using Power Query](/powerapps/maker/common-data-service/data-platform-cds-newentity-pq)

## Azure Data Factory

Azure Data Factory (ADF) is a data integration service that provides a low code / no code approach to construct ETL (extract, transform and load) processes within a visual environment or by writing your own code. 

![Azure Data Factory](media/azure-data-factory.png)

With ADF, you can visually integrate Common Data Service and other data sources using more than 90 natively built and maintenance free connectors.

![Azure Data Factory ETL](media/azure-data-factory-etl.png)

In addition to bringing data into the Common Data Service, Azure Data Factory can also be used to prepare, transform, and enrich data with Databricks and move data into Azure Synapse Analytics.

## Exporting Data from Common Data Service

Exporting data, either to another data technology or to another Common Data Service environment, can utilize any of the same technologies mentioned for importing data, such as Dataflows, Azure Data Factory, Power Query, and Power Automate.

![Export Common Data Service data methods](media/export-cds-data.png)

Dynamics customers that are targeting SQL Server or Microsoft Azure SQL Database can utilize the Data Export Service. It is an add-on service made available as a Common Data Service solution that adds the ability to replicate Common Data Service data to a Microsoft Azure SQL Database store in a customer-owned Microsoft Azure subscription. The supported target destinations are Microsoft Azure SQL Database and Microsoft Azure SQL Server on Microsoft Azure virtual machines. Data Export intelligently synchronizes the entire Common
Data Service schema and data initially and thereafter synchronizes on a continuous basis as changes occur (delta changes) in Common Data Service.

### See also
[Work with any type of app](why-cds-any-type-app.md)