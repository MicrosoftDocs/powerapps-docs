---
title: "Importing and exporting data | MicrosoftDocs"
description: Learn about importing and exporting data into Microsoft Dataverse.
ms.custom: ""
ms.date: 08/30/2022
ms.reviewer: "Mattp123"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "powerapps"
author: "mmercuri"
ms.subservice: dataverse-maker
ms.author: "kvivek"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Importing and exporting data

There are multiple ways to import and export data into Microsoft Dataverse. You can use dataflows, Power Query, Azure Synapse Link, Azure Data Factory, Azure Logic Apps, and Power Automate.

## Dataflows and Power Query

Dataflows enable you to connect with business data from various sources, clean the data, transform it, and then load it into Dataverse. Dataflows support dozens of popular on-premises, cloud, and software as a service (SaaS) data sources.

Power Query is a data connection technology you can use to discover, connect, combine, and refine data sources to meet your analysis needs. Features in Power Query are available in Excel and Power BI Desktop. 

![Dataflows and Power Query with Dataverse.](media/dataflows-power-query-with-cds.png "Dataflows and Power Query with Dataverse")

More information: [Create and use dataflows in Power Apps](./create-and-use-dataflows.md) and [Add data to a table in Dataverse by using Power Query](/power-query/dataflows/add-data-power-query)

## Azure Data Factory

Data Factory is a data integration service that provides a low-code or no-code approach to construct extract, transform, and load (ETL) processes within a visual environment or by writing your own code. 

![Data Factory.](media/azure-data-factory.png "Data Factory")

With Data Factory, you can visually integrate Dataverse and other data sources by using more than 90 natively built and maintenance-free connectors.

![Data Factory ETL.](media/azure-data-factory-etl.png "Data Factory ETL")

In addition to bringing data into Dataverse, Data Factory can also be used to prepare, transform, and enrich data with Databricks and move data into Azure Synapse Analytics.

## Exporting data from Dataverse

Exporting data, either to another data technology or to another environment, can use any of the same technologies mentioned for importing data, such as dataflows, Data Factory, Power Query, and Power Automate.

![Export Dataverse data methods.](media/export-cds-data.png "Export Dataverse data methods")

Dynamics customers who are targeting SQL Server or Azure SQL Database can use Azure Synapse Link. Azure Synapse Link for Dataverse connects with Azure Synapse Analytics to enable you to get near real-time insights over your data from Microsoft Dataverse. With a tight seamless integration between Dataverse and Azure Synapse Analytics, Azure Synapse Link enables you to run analytics, business intelligence and machine learning scenarios on your data. More information: [What is Azure Synapse Link for Dataverse](export-to-data-lake.md)

### See also

[Work with any type of app](work-with-any-type-app.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
