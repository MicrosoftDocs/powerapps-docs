---
title: Export Microsoft Dataverse data in Delta Lake format
description: Learn how eligible existing customers can use Azure Synapse Link to export Microsoft Dataverse data to Azure Synapse Analytics in Delta Lake format.
author: anibakore-msft
ms.author: banirud
ms.reviewer: matp
ms.service: powerapps
ms.topic: how-to
ms.subservice: dataverse-maker
ms.date: 10/08/2026
ms.custom: template-how-to
ai-usage: ai-assisted
---
# Export Dataverse data in Delta Lake format

> [!NOTE]
> Azure Synapse Link branding will retire soon. In Power Apps, open **Link data** to access this experience. The UX uses **Link to Data lake**, while this article continues to use Azure Synapse Link so existing customers can recognize the feature.

Azure Synapse Link can export Dataverse data in Delta Lake format by using your own Azure Synapse workspace, storage account, and Spark pool. This export option is also called **Delta Lake (Parquet)**, **Synapse Parquet**, or **bring your own Synapse (BYOS) Parquet**.

> [!IMPORTANT]
> The Delta Lake (Parquet) export option in Azure Synapse Link is deprecated:
>
> - Beginning October 15, 2026, the option won't be available to new customers.
> - For Delta Lake or Parquet output with significantly lower synchronization latency, use [Link to Microsoft Fabric](fabric-link-to-data-platform.md).
> - Existing customers must transition to either CSV output in Azure Synapse Link or Link to Microsoft Fabric by December 2027, when the Delta Lake (Parquet) export option will no longer be available.
> - Eligible existing customers can create a Delta Lake (Parquet) link by using the opt-in URL described in this article. The URL doesn't override eligibility or extend the deprecation deadlines.

Eligible existing customers can continue using this export option while they transition their downstream solutions. Delta Lake is the native format for Microsoft Fabric and many other tools, such as Azure Databricks. Exporting data in Delta Lake format directly from Dataverse eliminates the need for a separate Delta Lake conversion process. This article explains the existing-customer experience and shows you how to perform the following tasks:

- Understand Delta Lake and Parquet.
- Recreate a BYOS Parquet link for an eligible existing Dataverse organization.
- Monitor your Azure Synapse Link and data conversion.
- View your data from Azure Data Lake Storage Gen2.
- View your data from an Azure Synapse Analytics workspace.

## What is Delta Lake?

Delta Lake is an open-source project that enables building a lakehouse architecture on top of data lakes. Delta Lake provides ACID (atomicity, consistency, isolation, and durability) transactions, scalable metadata handling, and unifies streaming and batch data processing on top of existing data lakes. Azure Synapse Analytics is compatible with Linux Foundation Delta Lake. The current version of Delta Lake included with Azure Synapse has language support for Scala, PySpark, and .NET. More information: [What is Delta Lake?](/azure/synapse-analytics/spark/apache-spark-what-is-delta-lake). You can also learn more from the [Introduction to Delta Tables video](https://www.youtube.com/watch?v=B_wyRXlLKok).

Apache Parquet is the baseline format for Delta Lake, enabling you to leverage the efficient compression and encoding schemes that are native to the format. Parquet file format uses column-wise compression. It's efficient and saves storage space. Queries that fetch specific column values need not read the entire row data thus improving performance. Therefore, serverless SQL pool needs less time and fewer storage requests to read the data.

## Delta Lake characteristics

- **Scalability**: Delta Lake is built on top of Open-source Apache license, which is designed to meet industry standards for handling large-scale data processing workloads.
- **Reliability**: Delta Lake provides ACID transactions, ensuring data consistency and reliability even in the face of failures or concurrent access.
- **Performance**: Delta Lake leverages the columnar storage format of Parquet, providing better compression and encoding techniques, which can lead to improved query performance compared to query CSV files.
- **Cost-effective**: The Delta Lake file format is a highly compressed data storage technology that offers significant potential storage savings for businesses. This format is specifically designed to optimize data processing and potentially reduce the total amount of data processed or running time required for on-demand computing.
- **Data protection compliance**: Delta Lake with Azure Synapse Link provides tools and features including soft-delete and hard-delete to comply with data privacy regulations, including the General Data Protection Regulation (GDPR).

## How Delta Lake works with Azure Synapse Link for Dataverse

For an eligible existing Dataverse organization, use the opt-in creation flow in this article to connect Azure Synapse Link to a Synapse workspace and Spark pool. Azure Synapse Link exports the selected Dataverse tables in CSV format at designated time intervals and processes them through a Delta Lake conversion Spark job. After the conversion process completes, the system removes the CSV data to save storage. The system also schedules daily maintenance jobs that compact and vacuum the data files to optimize storage and query performance.

> [!IMPORTANT]
>
> - If an eligible existing organization replaces a CSV-based solution with a Delta Lake link, update existing custom-view scripts to use **non_partitioned** tables. Replace instances of `_partitioned` with an empty string.
> - For the Dataverse configuration, append-only is enabled by default to export CSV data in `appendonly` mode. The Delta Lake table will have an in-place update structure because the Delta Lake conversion comes with a periodic merge process.
> - You need to provision a Spark pool (compute resources) in your own Azure subscription for Delta conversion. This Spark pool is used to perform periodic Delta conversions based on the time interval chosen by you. 
> - There are no costs incurred with the creation of Spark pools. Charges are only incurred once a Spark job is executed on the target Spark pool and the Spark instance is instantiated on demand. These costs are related to the usage of Azure Synapse workspace Spark and are billed monthly. The cost of conducting Spark computing mainly depends on the time interval for incremental update and the data volumes. More information: [Azure Synapse Analytics pricing](https://azure.microsoft.com/pricing/details/synapse-analytics/)
> - You need to create a Spark pool with the current version (go to the version table in [In-place upgrade from previous versions](#in-place-upgrade-from-previous-versions)). If you're using a previous Spark version, perform an in-place upgrade for your existing profiles. More information: [In-place upgrade from previous versions](#in-place-upgrade-from-previous-versions)

> [!NOTE]
> The Azure Synapse Link status in Power Apps reflects the Delta Lake conversion state:
> - `Count` shows the number of records in the Delta Lake table.
> - `Last synchronized on` Datetime represents the last successful conversion timestamp.
> - `Sync status` is shown as **active** once the data sync and Delta Lake conversion completes, indicating that the data is ready for consumption.

## Prerequisites

- Your Dataverse organization ID must be eligible for the existing-customer BYOS Parquet creation option. Eligibility doesn't apply to other organization IDs in the same tenant.
- Dataverse: You must have the Dataverse **system administrator** security role. Additionally, tables you want to export through Azure Synapse Link must have the **Track changes** property enabled. More information: [Advanced options](create-edit-entities-portal.md#advanced-options)
- Azure Data Lake Storage Gen2: You must have an Azure Data Lake Storage Gen2 account and **Owner** or the [custom-role permissions](azure-synapse-link-synapse.md#custom-role-permissions). Your storage account must enable **Hierarchical namespace** and **public network access** for both initial setup and delta sync. **Allow storage account key access** is required only for the initial setup.  
- Synapse workspace: You must have a Synapse workspace and **Owner** or the [custom-role permissions](azure-synapse-link-synapse.md#custom-role-permissions), plus the **Synapse Administrator** role access within the Synapse Studio. The Synapse workspace must be in the same region as your Azure Data Lake Storage Gen2 account. The storage account must be added as a linked service within the Synapse Studio. To create a Synapse workspace, go to [Creating a Synapse workspace](/azure/synapse-analytics/get-started-create-workspace).
- An Apache Spark pool in the connected Azure Synapse workspace with the current Apache Spark version (go to [version requirements](#current-versions-and-requirements)) using this [recommended Spark Pool configuration](#recommended-spark-pool-configuration). For information about how to create a Spark Pool, go to [Create new Apache Spark pool](/azure/synapse-analytics/quickstart-create-apache-spark-pool-portal#create-new-apache-spark-pool).
- The Microsoft Dynamics 365 minimum version requirement to use this feature is 9.2.22082. More information: [Opt in to early access updates](/power-platform/admin/opt-in-early-access-updates#how-to-enableearly-access-updates)

### Recommended Spark Pool configuration

This configuration can be considered a bootstrap step for average use cases.

- Node size: small (4 vCores / 32 GB)
- Autoscale: Enabled
- Number of nodes: 3 to 10 (or 20 if needed. <sup>1</sup>More information below.)  
- Automatic pausing: Enabled
- Number of minutes idle: 5
- Apache Spark: 3.5 (go to [version requirements](#current-versions-and-requirements) for latest)
- Dynamically allocate executors: Enabled
- Default number of executors: 1 to 9

> [!IMPORTANT]
>
> - Use the Spark pool exclusively for the Delta Lake conversion operation with Azure Synapse Link for Dataverse. For optimal reliability and performance, avoid running other Spark jobs using the same Spark pool.
> - You might need to increase the number of nodes of the Spark pool if you expect a large number of rows to be processed. If the size of the Spark pool is insufficient, Delta conversion jobs might fail
> - The same Spark pool is used by the system to run a nightly job that compacts Delta files in the lake between 11 PM and 6 AM local time. The system determines the night time to run this job based on the location of your Dataverse environment. You can't provide a specific time window. This option reduces the size of Delta files by merging files known as "compaction." In rare cases, this job might interfere with the incremental conversion job. You can increase the number of nodes to 20 in case you notice these failures.
> - You're only charged for the spark pool nodes actually utilized. Increasing the number of nodes might not result in higher charges.

## Create a BYOS Parquet link as an eligible existing customer

> [!IMPORTANT]
> Eligibility is evaluated at the Dataverse organization ID level, not at the tenant level. This option is available only for an existing eligible organization to give customers time to migrate to [Link to Microsoft Fabric](fabric-link-to-data-platform.md). You can't use it with a new environment that has a new organization ID, even if another organization in the same tenant is eligible. If you unlink an eligible existing organization, you can use this option to create the link again for that same organization ID. Using the opt-in URL doesn't override eligibility or extend the December 2027 transition deadline.

1. Sign in to [Power Apps](https://make.powerapps.com/) with the Dataverse system administrator security role and select the environment you want.
1. Open **Link data**, and then add `enableSynapseParquet=true` to the URL. Keep your usual Maker Portal host and environment ID. For example:

   ```text
   https://make.powerapps.com/environments/<environment-id>/linkdata?tab=other&enableSynapseParquet=true
   ```

   Use the exact parameter spelling and lowercase `true`, and include the parameter only once. If the URL already contains `?`, append `&enableSynapseParquet=true`. Otherwise, append `?enableSynapseParquet=true`.

   The optional `tab=other` parameter opens **Data lake links**. The `tab=fabric` parameter opens **Fabric Links** and doesn't control BYOS eligibility.
1. Allow the page to finish loading, and then select **Create link to data lake**. Don't select **Create a new Fabric link** if you intend to create a BYOS Parquet link.

   :::image type="content" source="media/bring-your-parquet-link-data.png" alt-text="Link data page with Create link to data lake selected.":::

1. In **Create Link to Data lake**, find the **Get more from your data with Link to Fabric** card, and then select **Get Parquet format in a Synapse workspace anyway**.

   :::image type="content" source="media/bring-your-parquet-option.png" alt-text="Create Link to Data lake panel with the existing-customer Parquet option highlighted.":::

   > [!NOTE]
   > The URL doesn't select Parquet. The creation panel starts with CSV, and the Parquet action appears only after the URL opt-in and your organization's eligibility are confirmed. If the action isn't available, don't try other feature flags.

1. Select the **Subscription**, **Resource group**, and **Synapse workspace**.
1. Select **Use Spark pool for Delta Lake data conversion job**, and then select the precreated **Spark pool** and **Storage account**.

   :::image type="content" source="media/bring-your-parquet-resources.png" alt-text="Create Link to Data lake panel with Spark enabled for the Delta Lake conversion job.":::

1. Select **Next**.
1. Add the tables you want to export, and then select **Advanced**.
1. Optionally, select **Show advanced configuration settings** and enter the time interval, in minutes, for how often the incremental updates should be captured.
1. Select **Save**.

The format note changes to Parquet when you select the Spark pool. Selecting **Switch back to CSV** returns to CSV-only creation. It doesn't convert an existing link.

## Monitor your Azure Synapse Link and data conversion

1. Select the Azure Synapse Link you want, and then select **Go to Azure Synapse Analytics workspace** on the command bar.
1. Select **Monitor** > **Apache Spark applications**. More information: [Use Synapse Studio to monitor your Apache Spark applications](/azure/synapse-analytics/monitoring/apache-spark-applications)

## View your data from Synapse workspace

1. Select the Azure Synapse Link you want, and then select **Go to Azure Synapse Analytics workspace** on the command bar.
1. Expand **Lake Databases** on the left pane, select **dataverse-***environmentNameorganizationUniqueName*,
and then expand **Tables**. All Parquet tables are listed and available for analysis with the naming convention
*DataverseTableName.* **(Non_partitioned Table)**.

> [!NOTE]
> Don't use tables with the naming convention *_partitioned*. When you choose Delta parquet as the format, tables with the *_partition* naming convention are used as staging tables and removed after they're used by the system.

## View your data from Azure Data Lake Storage Gen2

1. Select the Azure Synapse Link you want, and then select **Go to Azure data lake** on the command
bar.
1. Select the **Containers** under **Data Storage**.
1. Select **dataverse-* **environmentName-organizationUniqueName*. All parquet files are stored in the
**deltalake** folder.

## In-place upgrade from previous versions

### Current versions and requirements

The following table shows the current and previous versions for Azure Synapse Link with Delta Lake. When you upgrade an existing profile or recreate a link for an eligible existing organization, use the current versions listed in the following table.

| Component | Current version | Previous version | Status | Reference link |
|-----------|----------------|------------------|--------|----------------|
| Apache Spark | 3.5 | 3.4 | 3.4 retired | [Apache Spark 3.4 runtime](/azure/synapse-analytics/spark/apache-spark-34-runtime) |
| Delta Lake | 3.0 | 2.4 | - | [Delta Lake compatibility](https://docs.delta.io/releases/) |

### Upgrade from Apache Spark 3.4 to 3.5

In accordance with the Synapse runtime for Apache Spark lifecycle policy, Azure Synapse runtime for Apache Spark 3.4 is retired. After the end of the support date, the retired runtimes are unavailable for new Spark pools and existing workflows with Spark 3.4 pools won't be executed and metadata temporarily remains in the Synapse workspace. More information: [Azure Synapse Runtime for Apache Spark 3.4](/azure/synapse-analytics/spark/apache-spark-34-runtime).

To ensure that your existing Azure Synapse Link profiles continue to process data, upgrade them by using the in-place upgrade process described here.

#### Prerequisites for upgrade

- You must have an existing Azure Synapse Link for Dataverse Delta Lake profile running with a previous Apache Spark version.
- You must create a new Synapse Spark pool with the current Spark version ([go to versions and requirements table](#current-versions-and-requirements)), *using the same or higher nodes hardware configuration within the same Synapse workspace*. For information about how to create a Spark pool, go to [Create new Apache Spark pool](/azure/synapse-analytics/quickstart-create-apache-spark-pool-portal#create-new-apache-spark-pool). This Spark pool should be created independent of your existing pool - *don't delete your current Spark pool or create the new pool with the same name*.

#### Upgrade steps

1. Sign in to Power Apps and select your preferred environment.
1. On the left navigation pane, select **Link data**, and then select **Other Links**. If the item isn't in the left navigation pane, select **…More** and then select the item you want.
1. If you're using a retired Spark version, an error message indicating that support has ended appears. Select the upgrade button in the ribbon to begin the upgrade process.

   :::image type="content" source="media/synapse-link-spark-34-eol-message.png" alt-text="Error message showing Apache Spark end of support with upgrade button in ribbon.":::

1. In the upgrade dialog, select the available Spark pool with the current version from the dropdown list.

   :::image type="content" source="media/synapse-link-spark-35-pool-selection.png" alt-text="Dropdown menu showing available Apache Spark pools for upgrade.":::

1. Select **Update** to complete the upgrade.

> [!NOTE]
>
> - The Spark pool upgrade occurs only when a new Delta Lake conversion Spark job is triggered. Ensure you have at least one data change after selecting **Update**.
> - After selecting **Update**, the upgrade process can take up to 48 hours to complete due to the cache. During this time, the old Spark pool continues to be used for Delta Lake conversion until the upgrade is fully applied in the backend. Don't delete the old Spark pool until you have confirmed that the new Spark pool is being used for Delta Lake conversion jobs. If the new Spark pool isn't used for Delta Lake conversion after two days, contact [Microsoft to get support](/power-platform/admin/get-help-support).

## Related articles

[What is Azure Synapse Link for Dataverse?](export-to-data-lake.md)

[Access audit data with Azure Synapse Link and Power BI](/power-platform/admin/audit-data-azure-synapse-link)

[Configure a Parquet data source for Microsoft Dynamics 365 ingestion](/azure/databricks/ingestion/lakeflow-connect/d365-parquet-source-setup)
