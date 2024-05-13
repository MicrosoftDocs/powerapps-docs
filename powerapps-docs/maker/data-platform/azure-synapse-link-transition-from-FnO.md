---
title: transition from Export to Data lake and BYOD to Fabric Link and Synapse Link for Dataverse
description: Learn how to transition from Export to Data lake and BYOD in finance and operations to Link to Fabric and Azure Synapse Link for Dataverse 
ms.date: 05/11/2024
ms.reviewer: matp 
ms.topic: "how-to"
applies_to: 
  - "powerapps"
author: Milindav
ms.subservice: dataverse-maker
ms.author: Milindav
search.audienceType: 
  - maker
ms.custom: bap-template
---
# Transitioning from Export to Data Lake and BYOD

Data export service (DES), [BYOD](https://learn.microsoft.com/dynamics365/fin-ops-core/dev-itpro/analytics/export-entities-to-your-own-database), [Export to Data lake](https://learn.microsoft.com/dynamics365/fin-ops-core/dev-itpro/data-entities/azure-data-lake-ga-version-overview) were features introduced in Dynamics 365 apps to export data for analytics and data integration scenarios. These services enabled IT admins and specialists to export data into external databases or data lakes and build data integration pipelines. While we have improved these services over the years with updates, as part of unification of Dynamics 365 with the power platform, we have rearchitected the same capabilities of these disparate services into simpler, unified experiences built into Power Apps maker portal. Transitioning to Fabric Link or upgrading to Synapse Link, the rearchitected services, provide you with an easy ramp to benefit from AI and Copilot investments in Dataverse and Microsoft Fabric.

If you are a customer using any of the previous generation services, this document provides guidance on upgrading to new experiences, benefiting from innovations as well as reducing end-to-end expenses and effort.

Based on preview customer surveys, we have also compiled a high level cost and benefits estimate to enable you to help with the transition. You will also see links to more information and videos as well as links to join forums and weekly office hour sessions to engage with product team, Microsoft specialists as well as fellow users as we continue to enhance these services with community participation.

## Before transition 

If you are a customer using legacy services BYOD, DES or Export to Data lake, you may have a data integration architecture similar to the one shown below. The highlighted box indicates the data pipelines your organization may have built to leverage the data exported from Dynamics 365 and Dataverse. You may use a selection of tools from Microsoft as well as others to copy and integrate Dynamics data with your own data. You may also transform and aggregate data by copying into multiple stores – shown under the Data-prep box. You may use Power BI or another tool to visualize data and create actionable insights. You may also have pipelines built to export data to an on-premise system and/or other clouds.
<< before picture >>

## After transition

There are 2 data integration patterns enabled in Power Apps maker portal. 
-	Synapse Link enables continuous export of data similar to BYOD, Export to Data lake or DES services. This option is enabled for IT admins and data integration specialists.
-	Link to Fabric feature provides a no-copy, no-ETL, fully managed software as a service (SaaS) integration.

<< after picture>> 

These options are complementary and we provide a detailed comparison below. 

If you are a Finance and Operations customer, currently using BYOD or Export to Data lake features, by upgrading to Synapse Link or Fabric Link, you can benefit from:

Simplified data integration architecture resulting in reduced operational costs 
•	Easy to configure and maintain via Power Apps maker portal - Built-in integration with Synapse and Microsoft Fabric
•	Synapse Link and Fabric Link are fully managed services - requires minimal ongoing management overhead
•	New services offer the same data shapes as previous services – your existing downstream integration pipelines can remain as is.
•	Minimal impact to operational workloads, you don’t need manage workloads and schedule data exports 

Secure, end-to-end data integration pipelines 
-	With Fabric link, your data doesn’t leave Dataverse governance boundary while authorized Fabric users can securely access data that resides within Dataverse
-	Synapse Link service enables you to restrict access to your storage accounts with firewalls while enabling Dataverse to export data with Managed Service Identities (MSI) a security feature built into Microsoft Entra. 

If you are a Dynamics 365 customer using Data Export service (DES) or classic Synapse Link with data exports in CSV format, you can benefit from efficient reporting enabled with the industry standard Delta/ Parquet data format.
•	Built-in Delta/ parquet conversion option reduces the need to build your own pipelines for analytics and operational reporting
•	Delta parquet format enables faster, more responsive queries & reports and scales to larger datasets of any size.
•	Data in lake is compressed to 1/3 ~ 1/8 the original size - resulting in smaller files that reduce data query and carrying costs

| link to Fabric  |  Azure Synapse Link |
|-------------------------------|------------------------------------|
| No copy, no ETL direct integration with Microsoft Fabric.	 | Export data to your own storage account and integrate with Synapse, Microsoft Fabric, and other tools. |
| Data stays in Dataverse - users get secure access in Microsoft Fabric. | 	Data stays in your own storage. You manage access to users.|
| All tables chosen by default.	| System administrators can choose required tables. |
|Consumes additional Dataverse storage.	| Consumes your own storage as well as other compute and integration tools.| 

## Which option should I use?
If your organization is already using Fabric or planning to transition, we recommend using Fabric Link feature. You can continue to use Synapse Link service if your immediate focus is to upgrade from your current services.

### Simplification with Fabric Link
If you are already consuming data using Power BI, using Data warehouse, or using Data flows and Notebooks to transform data, Link to Fabric feature provides immediate value. You can simplify your data integration architecture by removing the need to have your own storage account or Synapse services for Dataverse data. Instead of paying for Azure resources like storage and compute, you will pay for the increase in Dataverse storage. Compute charges such as near real-time data updates and management overhead is also factored into Dataverse storage. Fabric Link option is like having a near real time read-only replica of your data optimized for insights.

You can query this replica using T-SQL, Spark/ python as well as all the workloads in Fabric. You can also access this data using any tool that can consume T-SQL as well as ADLS storage.

As a Dynamics or PowerApps customer, you get a Dataverse storage quota based on the number of licenses you purchased. Fabric Link feature uses this database quota. You can buy more storage add-ons if the data volume exceeds your quota.

You can continue to retain Azure PaaS services like Databricks and SQL DBs in your own subscription. Recently announced Fabric features like data mirroring and shortcuts may help you further simplify your data integration.

Refer to examples on cost reductions achieved with the simplicity derived from Fabric integration feature below. 
<< After - Fabric Link picture>> 


### Upgrading to Synapse Link
By upgrading to Synapse Link and enabling delta parquet conversion, you can eliminate Dataverse data prep pipelines in your solution. Synapse Link service will export the same data shapes into your storage account in a more performant Delta/ parquet format. You can continue to use existing tools and Azure services like storage and Synapse query with minimal disruptions to your production environments.

<<< After - Synapse Link picture>>

## Understanding benefits – cost reductions 
Simplicity achieved with Fabric Link and Synapse Link yields reductions in end-to-end costs. Consider the following examples that are based on actual customer experiences. 

### Example 1: Transition from “BYOD” and “Export to Data lake” to Fabric Link 
Consider the case where you transition to Fabric Link from Export to Data lake. 

<< Before - after Fabric Link >>
 
As indicated in the before and after diagrams above, customer retired Export to Data lake service (1) as well as staging data stores (2) with Fabric Link. For operational insights, (4), they were able to consume data in OneLake directly in Power BI. Some of the insights require data merge, transformation and aggregation -(3). Instead of using disparate Azure services, they standardized on same tools built into Microsoft Fabric. 
As we discuss below, innovations in Dataverse and Microsoft Fabric enable simplifications and cost reductions. 
1.	Dataverse comes with a built-in OneLake store. Operational data from Dynamics 365 and PowerApps are replicated to built-in lake store near real-time (to avoid impact to operational workloads) and linked securely to Fabric via shortcuts. There is no need to bring Azure storage and secure data that’s exported out. Your data doesn’t leave Dataverse governance boundary and authorized users in Fabric can work with data using all Fabric workloads. 
2.	Export to Data lake (as well as DES) exports data in CSV format. CSV files are not suited for direct consumption due to poor query performance as well as occasional read/write contention issues. “Before solution” uses Azure Data Factory to periodically ingest and convert raw data into a SQL Azure DB or an Azure data warehouse. This layer is not needed in the “after solution” since Dataverse built-in OneLake data is maintained in Dela/ parquet format – the same open format that is native to Microsoft Fabric. Delta/ parquet format, along with optimizations in Fabric removes the need to maintain additional data stores for caching and improving query performance while eliminating read/ write contention. You can create Power BI DirectLake reports directly over data in OneLake without any additional data stages. 
3.	While operational insights can be performed using the data already available in OneLake, you may have additional data from other systems. This data may need to be combined, reshaped and aggregated with Dataverse data. Microsoft Fabric provides an integrated environment which provides best of breed tools like Data flows, Data factory, Spark. As opposed to configuring and provisioning tools standalone, you can simply consume the tools of choice. Integrated billing, source control and security enables simpler management and governance.
4.	While you can continue to use Power BI service for reporting purposes, Fabric introduces DirectLake mode reporting which leverages the in-memory indexes built into delta/ parquet format thereby removing the need to use Power BI import mode reports. 

These innovations yield end-to-end cost savings in addition to the benefits discussed above. Following tables outlines the Line items of costs along with a comparison of before and after solutions. You can use the table below as a guideline to estimate expected cost savings.

| Cost savings/ Line item  |  Before cost - Export to data lake | After cost - Fabric Link |
|-------------------------------|------------------------------------|------------------------------------------|
| Set-up & configuration | 	Need to use multiple tools <br> - Pay for multiple software licenses/ subscriptions <br> - System configuration efforts <br>- effort to build/ validate data pipelines <br> - continued governance, management, and monitoring <br> - training of users |	Simpler configuration experience in Power platform. <br> Purchase Fabric capacity and pay for use for all services. You only pay for what you use – in some cases, you are billed by the second. <br> No ETL pipelines needed for Dataverse data |
| Data Staging (1, 2) | Cost incurred for Azure services <br> -	Azure storage cost including cost of IO <br> -	Synapse Analytics (SQL serverless query) <br> -	Data Factory jobs to copy data <br> -	Staging data stores (ex. SQL DB)	| Cost increase in Dataverse DB storage <br><br> Ex. if you sync 500GB of data from D365, Dataverse storage may increase by ~100GB (5~8x data compression) |
| Operating Costs - Data Prep (3) | - Azure storage staging area <br> - Data pipelines <br>- Data ingestion into SQL or Dwh <br> - Development/ maintenance Data | Spend shifts to Fabric where you pay for consumption with a shared capacity. |
| Operating Costs – Reporting (4) <br> - Power BI datasets <br> - Reporting |	Synapse analytics (SQL Query) <br> Power BI capacity and storage for import mode reports	| As your data is compressed, (ex. 1/3 ~ 1/6 original size) your reporting and query costs reduce accordingly. <br> New features like DirectLake reporting reduces consumption of Power BI storage consumption.| 


