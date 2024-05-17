---
title: Transition from legacy data generation services to Fabric link and Azure Synapse Link for Dataverse
description: Learn how to transition from Export to Data Lake, BYOD, and data export service to link to Microsoft Fabric and Azure Synapse Link for Microsoft Dataverse.
ms.date: 05/16/2024
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
# Transition from legacy data generation services

Data export service, [bring your own database (BYOD)](/dynamics365/fin-ops-core/dev-itpro/analytics/export-entities-to-your-own-database), and [Export to Data Lake](/dynamics365/fin-ops-core/dev-itpro/data-entities/azure-data-lake-ga-version-overview) were features introduced in Dynamics 365 apps to export data for analytics and data integration scenarios. These services enabled IT admins and specialists to export data into external databases or data lakes and build data integration pipelines. While we improved these services over the years with updates as part of unification of Dynamics 365 with the power platform, we re-architected the same capabilities of these disparate services into simpler, unified experiences built into Power Apps (make.powerapps.com). Transitioning to Microsoft Fabric link or upgrading to Azure Synapse Link, the re-architected services provide you with an easy ramp to benefit from AI and Copilot investments in Microsoft Dataverse and Fabric.

If you are a customer using any of the previous generation services, this article provides guidance on upgrading to the new experiences, benefiting from innovations, as well as reducing end-to-end expenses and effort.

Based on preview customer surveys, we also compiled a high level cost and benefits estimate to help you with the transition. Links to more information and videos, links to join forums and weekly office hour sessions to engage with the product team, Microsoft specialists, and fellow users are also provided here. We strive to enhance these services with community participation.

## Before transition 

If you are a customer using legacy services BYOD, data export service, or Export to Data lake, you might have a data integration architecture similar to the one shown here. The highlighted box <!-- Where's the highlighted box in the below diagram? --> indicates the data pipelines your organization might have built to leverage the data exported from Dynamics 365 and Dataverse. You can use a selection of tools from Microsoft, as well as others, to copy and integrate Dynamics data with your own data. You can also transform and aggregate data by copying into multiple stores – shown in the data prep box of the diagram. You can use Power BI or another tool to visualize data and create actionable insights. You might have pipelines built to export data to an on-premises system and other clouds.

:::image type="content" source="media/Fabric/before-transition.png" alt-text="Data integration solution with Export to Data Lake" lightbox="media/Fabric/before-transition.png":::

## After transition

There are two data integration patterns enabled in Power Apps:

-	Azure Synapse Link enables continuous export of data similar to BYOD, Export to Data Lake, or data export service. This option is enabled for IT admins and data integration specialists.
- Link to Fabric feature provides a no-copy, no-ETL, fully managed software as a service (SaaS) integration.

These options are complementary. Here's a detailed comparison of the data integration services.

If you're a finance and operations apps customer currently using BYOD or Export to Data Lake features, by upgrading to Azure Synapse Link or Fabric link, you can benefit from a simplified data integration architecture resulting in reduced operational costs:

- Easy to configure and maintain via Power Apps (make.powerapps.com). Built-in integration with Azure Synapse and Fabric.
- Synapse Link and Fabric link are fully managed services. Each requires minimal ongoing management overhead.
- New services offer the same data shapes as previous services. Your existing downstream integration pipelines can remain as-is.
- Minimal impact to operational workloads, you don’t need manage workloads and schedule data exports.

Secure, end-to-end data integration pipelines:

-	With Fabric link, your data doesn’t leave the Dataverse governance boundary while authorized Fabric users can securely access data that resides within Dataverse.
-	Synapse Link service enables you to restrict access to your storage accounts with firewalls while enabling Dataverse to export data with managed identities for Azure, a security feature built into Microsoft Entra.

If you are a Dynamics 365 customer engagement customer using data export service or classic Synapse Link with data exports in CSV format, you can benefit from efficient reporting enabled with the industry standard Delta or Parquet data format:

- Built-in Delta Lake or Parquet conversion option reduces the need to build your own pipelines for analytics and operational reporting.
- Delta Lake or Parquet format enables faster, more responsive queries & reports and scales to larger datasets of any size.
- Data in lake is compressed to 1/3 to 1/8 the original size, resulting in smaller files that reduce data query and carrying costs.

| Link to Fabric  |  Azure Synapse Link |
|-------------------------------|------------------------------------|
| No copy, no ETL direct integration with Fabric. | Export data to your own storage account and integrate with Azure Synapse, Fabric, and other tools. |
| Data stays in Dataverse. Users get secure access in Microsoft Fabric. | Data stays in your own storage. You manage access to users.|
| All tables chosen by default.| System administrators can choose required tables. |
| Consumes additional Dataverse storage.| Consumes your own storage and other compute and integration tools.|

## Which option should I use?

If your organization is already using Fabric or planning to transition in the coming months, we recommend using the Fabric link feature. You can continue to use the Synapse Link service if your immediate focus is to upgrade from your current services.

### Simplification with Fabric link

If you are already consuming data using Power BI, using a data warehouse, or using dataflows and notebooks to transform data, the link to Fabric feature provides immediate value. You can simplify your data integration architecture by removing the need to have your own storage account or Synapse services for Dataverse data. Instead of paying for Azure resources like storage and compute, you pay for the increase in Dataverse storage. Compute charges such as near real-time data updates and management overhead is also factored into Dataverse storage. Fabric link option is like having a near real time read-only replica of your data optimized for insights.

:::image type="content" source="media/Fabric/After-transition-fabric.png" alt-text="Data integration solution smplified with Fabric link" lightbox="media/Fabric/After-transition-fabric.png":::

Query this replica using T-SQL, Apache Spark, Python as well as other workloads in Fabric. You can also access this data using any tool that can consume T-SQL or can consume data from Azure Data Lake Storage.

As a Dynamics or Power Apps customer, you get a Dataverse storage quota based on the number of licenses you purchased. The Fabric link feature uses this database quota. You can buy more storage add-ons if the data volume exceeds your quota.

You can continue to retain Azure platform as a service (PaaS) services, like Databricks and SQL Database, in your own subscription. Recently announced Fabric features like data mirroring and shortcuts can help you further simplify your data integration.

Examples of cost reductions achieved with the simplicity derived from Fabric integration feature are described here.

### Upgrading to Synapse Link

By upgrading to Synapse Link and enabling Delta or Parquet conversion, you can eliminate Dataverse data prep pipelines in your solution. Synapse Link service exports the same data shapes into your storage account in a more performant Delta or Parquet format. You can continue to use existing tools and Azure services like storage and Azure Synapse Analytics query with minimal disruptions to your production environments.

:::image type="content" source="media/Fabric/After-transition-synapse-link.png" alt-text="Data integration solution after upgrade to Synapse Link" lightbox="media/Fabric/After-transition-synapse-link.png":::

## Understanding benefits and cost reductions

Simplicity achieved with Fabric link and Synapse Link yields reductions in end-to-end costs. Consider the following examples that are based on preview customer experiences.

### Example 1: Transition from BYOD or Export to Data Lake to Fabric link

Consider the case where you transition to Fabric link from Export to Data Lake.

:::image type="content" source="media/Fabric/before-after-fabric-link.png" alt-text="Before and after solutions with link to Fabric" lightbox="media/Fabric/before-after-fabric-link.png":::

As indicated in the before and after diagrams above, customer retired Export to Data Lake service (1) as well as staging data stores (2) with Fabric link. For operational insights, (4), they consumed data in OneLake directly in Power BI. Some of the insights require data merge, transformation and aggregation (3). Instead of using disparate Azure services, they standardized on the same tools built into Fabric.

Innovations in Dataverse and Fabric enable simplifications and cost reductions:

- Dataverse comes with a built-in OneLake store. Operational data from Dynamics 365 and Power Apps are replicated to built-in lake store near real-time (to avoid impact to operational workloads) and linked securely to Fabric via shortcuts. There's no need to bring Azure storage and secure data that’s exported out. Your data doesn’t leave the Dataverse governance boundary and authorized users in Fabric can work with data using all Fabric workloads.
- Export to Data Lake and data export service exports data in CSV format. CSV files aren't suitable for direct consumption due to poor query performance as well as occasional read/write contention issues. The [before transition](#before-transition) guidance <!-- Do you mean "before transition" instead of "before solution" here? --> uses Azure Data Factory to periodically ingest and convert raw data into an Azure SQL Database or an Azure data warehouse. This layer isn't needed in the [after transition](#after-transition) guidance <!-- Do you mean "after transition" instead of "after solution" here? -->  since Dataverse built-in OneLake data is maintained in Delta or Parquet format – the same open format that is native to Microsoft Fabric. Delta or Parquet format, along with optimizations in Fabric removes the need to maintain additional data stores for caching and improving query performance while eliminating read/ write contention. You can create Power BI reports using Direct Lake over data in OneLake without any additional data stages.
-	While operational insights can be performed using the data already available in OneLake, you might have additional data from other systems. This data might need to be combined, reshaped, and aggregated with Dataverse data. Fabric provides an integrated environment, which provides best of breed tools like dataflows, Azure Data Factory, and Spark. Use these tools as opposed to configuring and provisioning tools standalone, where you adopt the tools of your choice. Integrated billing, source control, and security enables simpler management and governance.
- While you can continue to use Power BI service for reporting purposes, Fabric introduces Direct Lake mode reporting, which leverages the in-memory indexes built into Delta or Parquet format thereby removing the need to use Power BI import mode reports.

These innovations yield end-to-end cost savings in addition to the benefits discussed earlier. The tables here outline the line items of costs along with a comparison of before and after solutions. You can use this table as a guideline to estimate expected cost savings.

| Cost savings line item  |  Before cost - export to data lake | After cost - Fabric link |
|-------------------------------|------------------------------------|------------------------------------------|
| Set-up and configuration | 	Need to use multiple tools. <br> - Pay for multiple software licenses and subscriptions. <br> - System configuration efforts. <br>- Effort to build and validate data pipelines. <br> - Continued governance, management, and monitoring. <br> - Training of users. |	Simpler configuration experience in Power Platform. <br><br> Purchase Fabric capacity and pay for use for all services. You only pay for what you use. In some cases, you are billed by the second. <br><br> No ETL pipelines needed for Dataverse data. |
| Data staging (1, 2) | Cost incurred for Azure services. <br> -	Azure storage cost including cost of IO. <br> -	Synapse Analytics (SQL serverless query). <br> -	Azure Data Factory jobs to copy data. <br> -	Staging data stores, such as Azure SQL Database.	| Cost increase in Dataverse storage <br><br> For example, if you sync 500 GB of data from Dynamics 365, Dataverse storage could increase by around 100 GB (assuming five to eight times data compression). |
| Operating Costs - data prep (3) | - Azure storage staging area. <br> - Data pipelines. <br>- Data ingestion into Azure SQL or data warehouse. <br> - Development of maintenance data. | Spending shifts to Fabric where you pay for consumption with a shared capacity. |
| Operating costs – reporting (4) <br> - Power BI datasets. <br> - Reporting. |	Synapse analytics (SQL query). <br> Power BI capacity and storage for import mode reports.	| As your data is compressed, (for example 1/3 to 1/6 original size) your reporting and query costs reduce accordingly. <br><br> New features like Direct Lake reporting reduces consumption of Power BI storage consumption.|

 > [!NOTE]
 > These estimates are provided to enable estimating the spend after transition. While these estimates are based on experience from preview customers, actual costs incurred in your environment as well as data compression can vary depending on volume and composition of data.

### Example 2: Upgrade to Synapse Link

Upgrading to Synapse Link is an option to consider if you're not currently using Fabric – or not planning to transition in the coming months.

As indicated in the before and after diagrams here, customer retired Export to Data Lake service (1) as well as staging data stores (2) with Synapse Link. Data stores used for data staging, such as intermediate Azure SQL Databases, are retired as Dataverse data is saved in Delta or Parquet format – a more performant and compressed data format. Downstream pipelines used for data merge, transformation and aggregation, (3), as well as presentation tools (4), such as Power BI, remain unchanged.  

:::image type="content" source="media/Fabric/before-after-synapse-link.png" alt-text="Before and after upgrade to Synapse Link" lightbox="media/Fabric/before-after-synapse-link.png":::

Synapse Link provides an easy upgrade path for customers looking to extend their existing investments with minimal changes. As we discuss here, innovations in Dataverse enable easy transition from finance and operations apps services like Export to Data Lake and BYOD.

1. Synapse Link enables easy configuration of Azure storage and Synapse services within the Power Apps (make.powerapps.com). Several limitations of Export to Data Lake are removed:

   1. A uniform experience enables choosing data from all Dynamics 365 apps including both finance and operations and customer engagement apps. You can maintain a single service to export data from all Dynamics 365 and Power Apps.
   1. Table limitations present with Export to Data Lake go away. You can choose up to 1000 tables for each Synapse Link profile within a single storage account. You can create multiple profiles (export pipelines) each with up to 1000 tables.
   1. Synapse Link provides built-in support for using firewall restricted storage accounts to export data.
   1. No need to configure Azure resources. Synapse Link provisions and configures Azure resources on your behalf.
   1. Synapse Link exports data in the same format as Export to Data Lake or BYOD enabling you to retain existing pipelines.

1. Both Export to Data Lake and data export service export data in CSV format. CSV files aren't suited for direct consumption due to poor query performance as well as occasional read/write contention issues. [Before transition](#before-transition) uses Azure Data Factory to periodically ingest and convert raw data into a SQL Azure Database or an Azure data warehouse. This layer isn't needed in the '[after transition](#after-transition) since Synapse Link exports data in Delta or Parquet, which removes the need to maintain additional data stores for caching and improving query performance while eliminating read/write contention.
1. Continue to use your existing data pipelines for combining, reshaping, and aggregating additional data from other systems.
1. Continue to use Power BI service for reporting purposes. Fabric introduces Direct Lake mode reporting, which leverages the in-memory indexes built into Delta or Parquet format thereby removing the need to use Power BI import mode reports.

These innovations yield end-to-end cost savings in addition to the benefits discussed earlier. The tables here outline the line items of costs along with a comparison of before and after solutions. Use the table as a guideline to estimate expected cost savings.

| Cost savings line item | Before cost - Export to Data Lake | After cost - Synapse Link |
|--------------------------|---------------------------------------|--------------------------------|
| Set-up and configuration   | Must use multiple tools. <br> -  Pay for multiple software licenses and subscriptions. <br>- System configuration efforts. <br> - Effort to build and validate data pipelines. <br> - Continued governance, management, and monitoring. <br> - Training of users. | Simpler configuration experience in Power Platform. <br> No ETL pipelines needed for Dataverse data. | 
| Data staging (1, 2) | Cost incurred for Azure services. <br> - Azure storage cost including cost of IO. <br> - Synapse Analytics (SQL serverless query). <br> - Azure Data Factory jobs to copy data. <br> - Staging data stores, such as Azure SQL Database. | Synapse Link requires you to provide a Spark pool to convert data to Parquet format. <br><br> Depending on the frequency of data sync, as well as the volume of data changes, Spark pool costs can vary. <br><br> Small to medium data changes (per month): <br> - $600 to $2,000 for hourly refresh. <br> - $1,200 to $4,100 for 15 minute refresh. <br><br>  Medium to large data changes (per month): <br> - $1,200 to $2,500 for hourly refresh. <br> - $2,500 to $8,300 for 15 minute refresh. |
| Operating costs - data prep (3) | - Azure storage staging area. <br> - Data pipelines. <br> - Data ingestion into Azure SQL Database or data warehouse. <br> - Development and maintenance data. | Same costs as indicated above, however, you might not need to aggregate Dataverse data due to Parquet conversion. |
| Operating costs - reporting (4): <br> - Power BI datasets. <br> - Reporting. | Synapse Analytics (SQL query). <br> Power BI capacity. | As your data is compressed, for example 1/3 to 1/6 original size, your reporting and query costs reduce accordingly. |

 > [!IMPORTANT]
 > These estimates are provided to enable estimating the spend after transition. While these estimates are based on experience from preview customers, actual costs incurred in your environment as well as data compression can vary depending on volume and composition of data.

### Example 3: Incrementally ingesting data to a data warehouse

If you are currently consuming incremental data from Export to Data Lake feature to populate a downstream data pipeline, you can continue to use the same pipeline. As shown here, Synapse Link service can export incremental data changes in the same format as changes feed into Export to Data Lake.

:::image type="content" source="media/Fabric/before-after-incremental.png" alt-text="Before and after incremental data export to Synapse Link" lightbox="media/Fabric/before-after-incremental.png":::

Synapse Link service provides several enhancements over Export to Data Lake for incremental data changes:

- Initial data load is included within change folders. This makes it easy for the same pipeline to consume both the initial load as well as incremental updates.
- Change data is not deleted in case of a re-initialization of a table.
- System creates a time-stamped folder structure and metadata that helps you read the changes in chronological order. Change data once written, is never updated. This approach is better suited to process changes using big data ingestion tools like Azure Data Factory.
- You can configure how often you want the change feeds updated in folders with Synapse Link, as low as  five minutes.

When you transition to Fabric or Azure Synapse Link, the change in cost is minimal for incremental data changes.

## Understanding benefits – more real-time reporting

Fabric not only simplifies your data integration architecture, but also reduces the need to copy or replicate data. The underlying data format in Fabric, the industry standard Delta or Parquet format, can be directly consumed by Power BI, dataflows, notebooks, and other workloads eliminating the need for caching and staging areas.

If you upgrade to Synapse Link and continue to export data, your data is saved in Delta or Parquet format, which can reduce the steps in your own data pipelines for operational reporting.

Consider the time taken to refresh an operational report, such as inventory analysis or month-end financial analysis. These reports might require data aggregation of millions of rows of data from multiple tables in Dynamics 365 Finance. Using Export to Data Lake service, CSV data is exported within 10 minutes. This data might need to be imported into a Power BI report to provide better response times. Power BI refresh can be performed up to 24 times a day (every 30 minutes). Depending on how the report is designed, refresh can take several minutes to complete refresh. Using this approach, users can see data within 60 minutes of an update.

![Data staleness with Export to Data Lake](media/Fabric/before-data-staleness.png)

Operational reports that source data using Fabric link can leverage Direct Lake mode or DirectQuery mode in Fabric, which leverages the in-memory index built into Delta or Parquet files. In these modes, you don’t need to schedule refresh of Power BI reports as the report always shows latest Dataverse data updated in Fabric.

![Data staleness after Fabric link](media/Fabric/after-data-staleness.png)

Fabric link service updates data in Dataverse OneLake within the hour as of this point in time. Dataverse triggers data update jobs every 15 minutes and depending on the volume of data changes, you might see updated Parquet files within 30 to 60 minutes.

If you are consuming incremental data feeds from Dynamics 365 with Export to Data Lake service for near-real time data integration scenarios (example 3). Upgrade to Synapse Link enables you to run the same data pipelines.

## Known issues and workarounds

Currently, there are several limitations that are being addressed by the product team. Until we fix these limitations, use the suggested workaround. To learn more about the upcoming roadmap and stay in touch with the product team, join the preview [Viva Engage group](https://akamms.SynapseLinkforDynamics) <!-- Is there a link for this? -->

<!-- Ire-created the table into a 2 column format. we do need to mention the fix and the workaround, included fixed issues since customers may not be aware. Also, I have kept some upcoming fixes - ie. transition guide should tell customers that these are being addressed in the sam eplace - otherwise they won;t even try -->

|Known issue |Fixes and Workarounds |
| :- | :- |
|When adding a large number of tables at once, the system makes an initial copy of data. <br> We have seen rare cases (especially in smaller environments and Tier 2 sandboxes) where operational workloads may slow down and Initialize time may become much longer | This may impact smaller environments with fewer AOS servers (compute resources). </p><p>In Synapse Link, Add 5 tables at a time in case your environment is a Tier-2 Sandbox – once the initialization completes, you can add more. <br><br> Fabric Link feature scales initialization workloads up and down as available compute resources at roughly 2 concurrent tables per AOS. <br>Ex. if you have 5 AOS servers in your environment, system concurrently initializes up to 10 tables.</p><p> <br><br> Update your finance and operations environment to <br> - PU 63 cumulative update 7.0.7198.95 <br> -PU 62 cumulative update 7.0.7120.155 <br> This update redacts varBinary fields and varBinary attachments from tables added to Synapse Link and Fabric Link which reduces impact to operational workloads |
| When adding tables, the system makes an initial copy of data. In some cases, especially with very large tables, initialization may take longer or appear to be stuck for several days | Update finance and operation environment to <br>- PU 63 cumulative update 7.0.7198.91 <br>-PU 62 cumulative update 7.0.7120.152 <br> This update enables faster initialization of large tables (>200m rows) <br><br> We have enabled indexes to enable faster data sync. In case there’s an ongoing transaction in the operational database, index creation needs to wait for completion of the transaction. The prolonged wait, sometimes due to dormant transactions, may delay initialization process. In such cases system administrator can detect and to force index creation |
| In case your Dataverse environment is located in an Azure region different than the one where your Fabric capacity is located, you can’t use the Link to Fabric feature | As of 30-Apr, you can Link to a Fabric capacity located within the same Geo boundary (ex. USA) <br><br> NOTE: you may incur networking charges in Fabric due to data transfer between Azure regions |
| In case your Dataverse environment is located in an Azure region different than the one where your Data lake or Synapse workspace is located, you can’t use the Synapse Link feature | As of 30-Apr, you can link to a Storage account located within the same geo boundary (ex. USA). <br><br> NOTE: you may incur networking charges in Azure resources like Data lakes if they are not located within the same Azure region. |
| AOS authorization is a way to secure sensitive data fields in finance and operations against data exfiltration scenarios. <br> If the table selected contains data columns that are secured via AOS Authorization, those columns are ignored and the exported data doesn't contain the column. <br><br> Ex CustTable, column TaxLicenseNum has the metadata property AOS Authorization set to Yes. This column is ignored | Update your finance and operations environment to following versions or above <br>- PU 63:7.0.7198.105 <br>- PU 62:7.0.7120.159 <br>With this update, AOS authorization fields will be added to tables. <br>-	Incremental updates will include this column <br> -	Modified records will show these columns and value <br> -	Full refresh will include these fields and all values |
| If the table selected contains data columns that are of Array type, those columns are ignored and the exported data doesn't contain the column. <br><br>For example, in a custom table named WHSInventTable, columns FilterCode and FilterGroup are of type array. These columns aren't exported with Azure Synapse Link | There is no workaround to this issue. This feature will be enables in a future update. <br><br> Join [Viva engage group](https://aka.msSynapsELinkforDynamics) to stay in touch and onboard preview features when available |
| In case of finance and operations app tables that exhibit [valid time stamp behavior](https://learn.microsoft.com/dynamicsax-2012/developer/valid-time-state-tables-and-date-effective-data), only the data rows that are currently valid are exported with Azure Synapse Link. <br><br> For example, the ExchangeRate table contains both current and previous exchange rates. Only currently valid exchange rates are exported in Azure Synapse Link. | As a workaround, until this issue is fixed in a future update, you can use an Entity such as **ExchangeRateBIEntity**. <br>Join [Viva engage group](https://aka.msSynapsELinkforDynamics) to stay in touch and onboard preview features |
|[Table inheritance and derived tables](https://learn.microsoft.com/dynamicsax-2012/developer/table-inheritance-overview) are concepts in finance and operations apps. When choosing a derived table from finance and operations apps, fields from the corresponding base table currently aren't included. | You need to select the base table in addition to the derived table if you need access to these fields. <br> You can use [this FastTrack solution provided via GitHub](https://github.com/microsoft/Dynamics-365-FastTrack-Implementation-Assets/tree/master/Analytics/DataverseLink/DataIntegration#derived-tables). this solution creates view(s) which include fields from base tables |
| Export more than 1000 tables via Synapse Link or add more than 1000 tables to Fabric Link |  If you are using Synapse Link, you can workaround by creating 2 or more profiles that contain less than 1000 tables <br><br> We are enabling you to select more than 1000 tables in Fabric Link and in a Synapse Link profile in a future update.| 
| Finance and operations apps tables included in an Azure Synapse Link profile can't be migrated to a different environment using the import and export profile feature in Azure Synapse Link | Until this issue is addressed, you can add the same tables into the new environment. You can copy and paste a comma separated list of tables into the search box within the manage tables option to select a list of tables at once  |
| Synapse Link or Fabric Link enables Entities where “change tracking” property is enabled. <br> Currently, change tracking can't be enabled for all finance and operations entities. The Track changes checkbox is unavailable for entities created in finance and operations in the past for data migration. <br> In some entities, enabling change tracking might fail with the error message "chosen entity doesn't pass the validation rules..." or the Track changes checkbox is disabled for some entities. <br> For more information about entity validation rules and how you can fix them, go to [Enable row version change tracking for data entities](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/rowversion-change-track#enable-row-version-change-tracking-for-data-entities). You might need developer assistance to complete the steps. | If the chosen entity is unavailable because of the change tracking limitation, you can choose the tables that comprise the data from that entity. <br> You can use [EntityUitl](https://github.com/microsoft/Dynamics-365-FastTrack-Implementation-Assets/tree/master/Analytics/DataverseLink/DataIntegration/EntityUtil) solution provided by the FastTrack team to create Entity shapes using tables |
| In case of a database restore operation in Dataverse, finance and operations entities enabled in Azure Synapse Link are removed. | To re-enable entities, you need to re-enable corresponding virtual tables for all selected entities, re-enable change tracking, and reselect the tables in Azure Synapse Link. You can copy and paste a comma separated list of tables into the search box within the manage tables option to select a list of tables at once|
| Finance and operations apps tables added to an Azure Synapse Link profile might be removed when a back-up is restored in Dataverse. | You must add finance and operations tables into the profile after a database restore operation. Go to [Known limitations with finance and operations tables](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/azure-synapse-link-select-fno-data#known-limitations-with-finance-and-operations-tables) for details on re-enabling entities after a database restore operation.|








-----------------------------
<!-- ==== Following table can be removed ====.-->
<!-- The table has issues and HTML isn't supported in Learn markdown. Using occasional line break br tags is ok in tables to force a line break. Suggest removing all HTML paragraph tags and the extra columns so you only have two columns. So the two columns are the known issue and workaround columns. We do not publish future plans such as bug fixes in the Learn content so the fix and roadmap column should be removed. If table doesn't work for you consider using markdown columns https://review.learn.microsoft.com/en-us/help/platform/markdown-reference?branch=main#columns.-->
|Known issue |Workaround |
| :- | :- |
|When adding a large number of tables at once, the system makes an initial copy of data. <br> We have seen rare cases (especially in smaller environments and Tier 2 sandboxes) where operational workloads may slow down and Initialize time may become much longer |We are addressing this issue which typically impacts smaller environments.</p><p></p><p>Add 5 tables at a time in case your environment is a Tier-2 Sandbox – once the initialization completes, you can add more.</p><p></p>|<p>Apr release resolves some of these issues</p><p></p><p>We are redacting varBinary fields and varBinary attachments from tables added to Synapse Link and Fabric Link. These fields will be ignored.</p><p></p><p>- PU 63 cumulative update 7.0.7198.95</p><p>- PU 62 cumulative update 7.0.7120.155</p><p></p><p>Fabric Link feature scales initialization workloads up and down as resources permit at roughly 2 concurrent tables per AOS. </p><p></p><p>Ex. if you have 5 AOS servers in your environment, system concurrently initializes up to 10 tables.</p><p></p><p></p>|
|<p>**When adding a large number of tables at once, the system makes an initial copy of data. In some cases, especially with very large tables, initialization may take longer.** </p><p></p><p>**In some cases initialization appears to be stuck for several days.**</p><p></p><p></p>||<p>Apr release introduces 2 features to reduce this issue.</p><p></p><p>Faster initialization of large tables (>200m rows) </p><p>- PU 63 cumulative update 7.0.7198.91</p><p>- PU 62 cumulative update 7.0.7120.152</p><p></p><p>We have enabled indexes to enable faster data sync. In case there’s an ongoing transaction in the operational database, index creation needs to wait for completion of the transaction. This wait will delay initialization process. </p><p></p><p>System detects such index delays and informs the user to take action if the delays are excessive (ex. > 24hrs).</p><p></p>|
|<p>**In case your Dataverse environment is located in an Azure region different than the one where your Fabric capacity is located, you can’t use the Link to Fabric feature** </p><p></p>|This issue is addressed in Apr release|<p>In Apr release, you can Link to a Fabric capacity located within the same Geo boundary (ex. USA) </p><p></p><p>NOTE: you may incur networking charges in Fabric. See: </p><p></p>|
|<p>**In case your Dataverse environment is located in an Azure region different than the one where your Data lake or Synapse workspace is located, you can’t use the Synapse Link feature** </p><p></p>|<p>You need to create a data lake and synapse resources in the same region as Dataverse</p><p></p><p></p>|<p>In Apr release, you can link to Storage account located within the same geo boundary.</p><p></p><p>NOTE: you may incur networking charges in Azure resources like Data lakes. See: </p><p></p>|
|<p>**AOS authorization is a way to secure sensitive data fields in FnO against data exfiltration scenarios.**</p><p></p><p>**If the table selected contains data columns that are secured via AOS Authorization, those columns are ignored and the exported data doesn't contain the column.** </p><p></p><p>**Ex *CustTable*, column *TaxLicenseNum* has the metadata property AOS Authorization set to Yes. This column is ignored**</p><p></p>||<p>Apr release addresses this issue</p><p></p><p>With FnO latest quality update (10.0.38, 10.0.39), AOS authorization fields will be added </p><p>- Incremental updates will include this column </p><p>- Modified records will show these columns and value </p><p>- Full refresh will include these fields and all values</p><p></p>|
||||
|<p>**If the table selected contains data columns that are of Array type, those columns are ignored and the exported data doesn't contain the column.** </p><p></p><p>**For example, in a custom table named *WHSInventTable*, columns FilterCode and FilterGroup are of type array. These columns aren't exported with Azure Synapse Link**</p>|There is no workaround to this issue. We are working on enabling these fields.|ETA – May update|
|**In case of finance and operations app tables that exhibit [valid time stamp behavior](https://learn.microsoft.com/en-us/dynamicsax-2012/developer/valid-time-state-tables-and-date-effective-data), only the data rows that are currently valid are exported with Azure Synapse Link. For example, the ExchangeRate table contains both current and previous exchange rates. Only currently valid exchange rates are exported in Azure Synapse Link.** |<p>We are working on enabling this pattern so that you can extract all records.</p><p></p><p>As a workaround, until this issue is fixed, you can use an Entity such as **ExchangeRateBIEntity**.</p><p></p>|ETA – May update |
|**Export more than 1000 tables** |<p>We are enabling you to select more than 1000 tables in Fabric Link and in a Synapse Link profile</p><p></p><p>If you are using Synapse Link, you can workaround by creating 2 or more profiles that contain less than 1000 tables</p><p> </p>|ETA – May update|
||||
|<p>[**Table inheritance and derived tables](https://learn.microsoft.com/en-us/dynamicsax-2012/developer/table-inheritance-overview) **are concepts in finance and operations apps. When choosing a derived table from finance and operations apps, fields from the corresponding base table currently aren't included.** </p><p></p>|<p>You need to select the base table in addition to the derived table if you need access to these fields.</p><p></p><p><https://github.com/microsoft/Dynamics-365-FastTrack-Implementation-Assets/tree/master/Analytics/DataverseLink/DataIntegration#derived-tables> </p><p>You can use the FastTrack solution provided via GitHub[^1] - this solution creates view(s) which include fields from base tables</p><p></p><p></p>|ETA – Jun update|
||||
|**Finance and operations apps tables included in an Azure Synapse Link profile can't be migrated to a different environment using the import and export profile feature in Azure Synapse Link**|We are working on this feature |ETA – Jun/ July|
|<p>**Synapse Link or Fabric Link enables Entities where “change tracking” property is enabled.** </p><p></p><p>**Currently, change tracking can't be enabled for all finance and operations entities. The Track changes checkbox is unavailable for entities created in finance and operations in the past for data migration.** </p><p></p><p>**In some entities, enabling change tracking might fail with the error message "chosen entity doesn't pass the validation rules..." or the Track changes checkbox is disabled for some entities.** </p><p></p><p>**For more information about entity validation rules and how you can fix them, go to [Enable row version change tracking for data entities](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/rowversion-change-track#enable-row-version-change-tracking-for-data-entities). You might need developer assistance to complete the steps.**</p><p></p><p></p>|<p>If the chosen entity is unavailable because of the change tracking limitation, you can choose the tables that comprise the data from that entity.</p><p></p><p><https://github.com/microsoft/Dynamics-365-FastTrack-Implementation-Assets/tree/master/Analytics/DataverseLink/DataIntegration/EntityUtil> </p><p>You can use EntityUitl[^2] solution provided by the FastTrack team to create Entity shapes using tables</p><p></p>|ETA – Jun/ July|
||||
|**In case of a database restore operation in Dataverse, finance and operations entities enabled in Azure Synapse Link are removed.** |To re-enable entities, you need to re-enable corresponding virtual tables for all selected entities, re-enable change tracking, and reselect the tables in Azure Synapse Link|ETA: Aug/ Sept|
|<p>**Finance and operations apps tables added to an Azure Synapse Link profile might be removed when a back-up is restored in Dataverse.** </p><p></p>|You must add finance and operations tables into the profile after a database restore operation. Go to [Known limitations with finance and operations tables](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/azure-synapse-link-select-fno-data#known-limitations-with-finance-and-operations-tables) for details on re-enabling entities after a database restore operation.|ETA: Aug / Sept |
||||


