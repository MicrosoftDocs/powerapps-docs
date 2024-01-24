---
title: Choose finance and operations data in Azure Synapse Link for Dataverse
description: Learn how to choose finance and operations data in Microsoft Azure Synapse Link for Dataverse and work with Azure Synapse Link and Power BI.
ms.date: 01/12/2024
ms.reviewer: johnmichalak
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
# Choose finance and operations data in Azure Synapse Link for Dataverse

Microsoft Azure Synapse Link for Dataverse lets you choose data from finance and operations apps. Use Azure Synapse Link to continuously export data from finance and operations apps into Azure Synapse Analytics and Azure Data Lake Storage Gen2.

Azure Synapse Link for Dataverse is a service that's designed for enterprise big data analytics. It provides scalable high availability together with disaster recovery capabilities. Data is stored in the Common Data Model format, which provides semantic consistency across apps and deployments.

Azure Synapse Link for Dataverse offers the following features that you can use with finance and operations data:

- You can choose both standard and custom finance and operations entities and tables.
- Continuous replication of entity and table data is supported. Create, update, and delete (CUD) transactions are also supported.
- You can link or unlink the environment to Azure Synapse Analytics and/or Data Lake Storage Gen2 in your Azure subscription. You don't have to go to the Azure portal or Microsoft Dynamics Lifecycle Services for system configuration.
- You can choose data and explore by using Azure Synapse. You don't have to run external tools to configure Synapse Analytics workspaces.
- All features of Azure Synapse Link for Dataverse are supported. These features include availability in all regions, saving as Parquet Delta files, and restricted storage accounts.
- The table limits in the Export to Data Lake service aren't applicable in Azure Synapse Link for Dataverse.
- By default, saving in Parquet Delta Lake format is enabled for finance and operations data, so that query response times are faster.

> [!NOTE]
> 
> This feature is generally available with finance and operations application versions shown in the following list. If you have not yet applied these application versions, install the latest cumulative update to use this feature.
> 
> - 10.0.36 (PU60) cumulative update 7.0.7036.133 or later. 
> - 10.0.37 (PU61) cumulative update 7.0.7068.109 or later.
> - 10.0.38 (PU62) cumulative update 7.0.7120.59 or later
>
> If you're planning to adopt the export to data lake feature in finance and operations apps, consider adopting Azure Synapse Link with finance and operations data support instead. Go to the software lifecycle announcements related to [export to data lake feature](/dynamics365/fin-ops-core/dev-itpro/data-entities/azure-data-lake-ga-version-overview) for more details. For guidance and tools to upgrade from export to data lake to Synapse Link go to [TechTalk Series: Synapse Link for Dataverse: Transitioning from Export to Azure Data Lake to Synapse Link](https://aka.ms/TransitiontoSynapseLinkVideos)
>
> Finance and operations data in Synapse Link is not yet available in the "Azure in China" region.
>

## Prerequisites

- You must have a finance and operations sandbox (Tier-2) or higher environment. You can also use a Tier-1 environment (also known as a cloud-hosted environment) for validation. Your environments must be version 10.0.36 (PU 60) cumulative update 7.0.7036.133 or later.
- The finance and operations apps environment must be linked with Microsoft Power Platform. More information: [Link your finance and operations environment with Microsoft Power Platform](#link-your-finance-and-operations-environment-with-microsoft-power-platform)
- Enable **Sql row version change tracking** configuration key. More information: [Add configurations in a finance and operations apps environment](#add-configurations-in-a-finance-and-operations-apps-environment).
- You can't add finance and operations data to an existing storage account that's configured with Azure Synapse Link. You must have access to an Azure subscription so that you can create a new SynapseL Link profile. Depending on how you plan to consume data, you might need additional Azure resources as shown here.

| How you plan to consume data  |  Azure Synapse Link feature you'll use | Prerequisites and Azure resources needed |
|-------------------------------|------------------------------------|------------------------------------------|
| Access finance and operations tables via Synapse query |  [Azure Synapse Link - Delta lake](azure-synapse-link-delta-lake.md) |  Azure Data lake <br> Azure Synapse workspace <br> Azure Synapse Spark pool <br> Your data is saved in delta parquet format enabling better read performance | 
| Load incremental data changes into your own downstream data warehouse | [Azure Synapse Link - incremental update](azure-synapse-link-incremental.md) | Azure data lake <br> No need to bring Synapse workspace or Spark pool as your data is saved in CSV format |
| Access finance and operations tables via Microsoft Fabric | [Link to Fabric](azure-synapse-link-view-in-fabric.md)  | Microsoft Fabric workspace |

### Link your finance and operations environment with Microsoft Power Platform

Verify with your finance and operations systems administrator whether your finance and operations environment is linked to Power platform.

To confirm that the finance and operations apps environment is linked with Microsoft Power Platform, review the **Environment** page in Lifecycle Services.

You can link with Microsoft Power Platform when you deploy the new environment. You can also link existing environments with Power platform. For more information about Microsoft Power Platform integration, go to [Enable the Microsoft Power Platform integration](/dynamics365/fin-ops-core/dev-itpro/power-platform/enable-power-platform-integration#enable-during-deploy).

> [!NOTE]
> Dual-write setup isn't required to enable finance and operations data in Azure Synapse Link.

### Add configurations in a finance and operations apps environment

You must enable the **Sql row version change tracking** configuration key in your finance and operations environment. In finance and operations versions 10.0.39 (PU63) or later, this configuration key might be enabled by default.

To enable this configuration key, you must turn on maintenance mode. More information: [Turn maintenance mode on and off in DevTest/Demo environments hosted in Customer's subscription](/dynamics365/fin-ops-core/dev-itpro/sysadmin/maintenance-mode#turn-maintenance-mode-on-and-off-in-devtestdemo-environments-hosted-in-customers-subscription).

![Screenshot that shows the Sql row version change tracking configuration key enabled.](media/Synapse-Link-Enable-Fno-Configuration.png)

> [!NOTE]
> If you use a Tier-1 (cloud-hosted) environment, you must do a full database synchronization (DBSync) and use Visual Studio to complete the maintenance mode.

After row version change tracking is enabled, a system event that's triggered in your environment might cause reinitialization of tables in export to data lake. If you have downstream consumption pipelines, you might have to reinitialize the pipelines. More information: [Some tables have been "initialized" without user action](/dynamics365/fin-ops-core/dev-itpro/data-entities/finance-data-azure-data-lake#some-tables-have-been-initialized-without-user-action).

## Add finance and operations tables in Azure Synapse Link

You can enable both finance and operations tables and finance and operations entities in Azure Synapse Link for Dataverse. This section is focused on finance and operations tables.

1. Sign in to Power Apps and select the environment you want.
2. On the left navigation pane, select **Azure Synapse Link**.
3. On the command bar of the **Synapse Link** page, select **+ New link to data lake**.
4. Select **Connect to your Azure Synapse Analytics workspace**, and then select the **Subscription**, **Resource group**, and **Workspace name**.
5. Select **Use Spark pool for processing**, and then select the precreated Spark pool and storage account.
6. Select **Next**.
7. Add the tables you want to export. You can choose finance and operations tables provided the [prerequisites](#prerequisites) are met.
8. Select **Advanced**, select **Show advanced configuration settings** and enter the time interval, in minutes, for how often the incremental updates should be captured.
9. Select **Save**. Tables selected are initialized and ready for reporting.

> [!NOTE]
>
> - Finance and operations apps tables are allowed only in Azure Synapse Link. Makers can't currently use them to build apps.
> - You don't have to define finance and operations apps tables as virtual tables, and you don't have to enable change tracking for each table.
>
> To include finance and operations tables in Synapse Link, you must enable the [Delta lake feature](/power-apps/maker/data-platform/azure-synapse-link-delta-lake) in your Synapse Link profile. Finance and operations table selection isn't visible if your Synapse Link profile isn't configured for Delta lake.
>
> Delta lake conversion time interval determines how often table data is updated in delta format. For near real time updates, choose 15 minutes or one hour as the desired updated time internal. Choose daily time interval if near real-time updates aren't required. Delta conversion consumes compute resources from the Spark pool you have provided in the configuration of the Synapse Link profile. The lower the time interval, the more compute resources are consumed and you can incur more cost. Open the Spark pool in Azure portal to see the compute cost.
>
> In the event that the system ran into an error during initial sync or updates, you'll see an error icon and a pointer to trouble-shooting documents that can be used to diagnose and resolve the error.

### Known limitations with finance and operations tables

Currently, there are the following limitations with finance and operations tables and Azure Synapse Link. To learn more about the upcoming roadmap and stay in touch with the product team, join the [preview Viva Engage group](https://aka.ms/SynapseLinkforDynamics/).

- You must create a new Azure Synapse Link profile. You can't add finance and operations apps tables to existing Azure Synapse Link profiles.
- Don't see all tables? Up to 2,750 Microsoft provided finance and operations apps tables are already enabled in Azure Synapse Link with application version 10.0.38. If you have a previous version of finance and operations apps, not all required tables can be enabled by default. You can enable more tables yourself by extending table properties and enabling the change tracking feature. For more information about how to enable change tracking, see [Enable row version change tracking for tables](/dynamics365/fin-ops-core/dev-itpro/data-entities/rowversion-change-track#enable-row-version-change-tracking-for-tables).
- Don't see your custom tables? You must enable change tracking in them. More information: [Enable row version change tracking for tables](/dynamics365/fin-ops-core/dev-itpro/data-entities/rowversion-change-track#enable-row-version-change-tracking-for-tables).
- You can select a maximum of 1,000 tables in an Azure Synapse Link profile. To enable more tables, create another Azure Synapse Link profile.
- If the table selected contains data columns that are secured via **AOS Authorization**, those columns are ignored and the exported data doesn't contain the column. For example in a custom table named *CustTable*, the column *TaxLicenseNum* has the metadata property **AOS Authorization** set to **Yes**. This column is ignored when *CustTable* data is exported with Azure Synapse Link.  
- If the table selected contains data columns that are of **Array** type, those columns are ignored and the exported data doesn't contain the column. For example, in a custom table named *WHSInventTable*, columns **FilterCode** and **FilterGroup** are of type array. These columns aren't exported with Azure Synapse Link.
- In case of Finance and Operations Tables that exhibit (valid time stamp behavior)[https://learn.microsoft.com/dynamicsax-2012/developer/valid-time-state-tables-and-date-effective-data], only the data rows that are currently valid are exported with Synapse Link. For example, **EXchangeRate** table contains both current and previous exchange rates. Only currently valid exchange rates are exported in Synapse Link. As a workaround, until this issue is fixed, you can use an entity such as ExchangeRateBIEntity.


## Access incremental data changes from finance and operations

To load incremental data changes from finance and operations into your own downstream data warehouse, create an Azure Synapse Link profile that provides only incremental data. Azure Synapse Link provides an initial export of all data rows and then provides you with access to data that changed periodically. The data is provided in CSV files stored in time stamped folders and you can easily consume the data using Azure Data factory or other data tools. More information:  [Azure Synapse Link - incremental update](azure-synapse-link-incremental.md)

To create a Azure Synapse Link profile with incremental data:

1. Sign in to Power Apps and select the environment you want.
1. On the left navigation pane, select **Azure Synapse Link**.
1. On the **Azure Synapse Link for Dataverse** page, select **+ New link** on the command bar.
1. Select **Subscription**, **Resource group** and a **Storage account**. You don't need to provide a Synapse workspace or a Spark pool.
1. Select **Next**. The option to choose tables appears.
1. Select **Advanced**, select **Show advanced configuration settings**, and then enable the option **Enable incremental update folder structure**
1. In the **Time interval** field, choose the desired frequency for reading incremental data. Using this frequency, the system partitions data into time stamped folders such that you can read the data without being impacted by ongoing write operations.  
1. Select the Dataverse tables you want. You can also select finance and operations tables. The options **Append only** and **Partition** available at a table level are ignored. Data files are always appended and data is partitioned yearly.
1. Select **Save**. Tables selected are initialized and you see incremental data in the storage account.

> [!NOTE]
>
> If you are upgrading from the export to data lake feature, enabling the incremental data changes option provides similar change data as the [Change feeds feature](/dynamics365/fin-ops-core/dev-itpro/data-entities/azure-data-lake-change-feeds)
>
> We recommend that you create separate Azure Synapse Link profiles for incremental data and tables for ease of management.
>
> The finance and operations table limitations are also applicable to incremental data from tables. More information: [Known limitations with finance and operations tables](#known-limitations-with-finance-and-operations-tables)

## Working with Data and metadata  
**Enumerated fields** are coded data fields in Finance and Operations. 




## Enable finance and operations data entities in Azure Synapse Link

You can enable both finance and operations entities and finance and operations apps tables in Azure Synapse Link for Dataverse. This section is focused on finance and operations data entities.

The process of enabling finance and operations entities has the following steps. Each step is explained in the following subsections.

1. [Enable finance and operations virtual entities in the Power Apps maker portal](#enable-finance-and-operations-virtual-tables-in-power-apps). This step lets you use finance and operations entities in Power Apps (make.powerapps.com) to build apps. You can also use them with Azure Synapse Link.
2. [Enable change tracking for finance and operations entities](#enable-change-tracking-for-finance-and-operations-entities). You must complete this step to enable Azure Synapse Link to use finance and operations entities.

After you complete both steps, you can select finance and operations entities in Azure Synapse Link. To create Azure Synapse Link for Dataverse in Delta lake format, follow the steps in [Export Dataverse data in Delta Lake format](/power-apps/maker/data-platform/azure-synapse-link-delta-lake).

> [!NOTE]
> Finance and operations entities start with the prefix **mserp\_**.

### Enable finance and operations virtual tables in Power Apps

You must enable finance and operations entities as **virtual tables** in Dataverse. Makers then use the chosen finance and operations entities to build apps, and the entities can also be used with Azure Synapse Link.

To enable finance and operations entities as virtual tables, follow the steps in [Enable Microsoft Dataverse virtual entities](/dynamics365/fin-ops-core/dev-itpro/power-platform/enable-virtual-entities).

> [!TIP]
> To validate Azure Synapse Link features, you can use a few of the sample entities from the following list:
>
> - **MainAccountBiEntity** – This entity contains a list of ledger accounts.
> - **ExchangeRateBiEntity** – This entity contains exchange rates in the system.
> - **InventTableBiEntity** – This entity contains a list of inventory items.

### Enable change tracking for finance and operations entities

When you enable finance and operations entities as virtual entities in Dataverse, they appear in the maker portal. Finance and operations entities start with the prefix **mserp\_**.

To enable change tracking, follow these steps.

1. In Power Apps, select **Tables** on the left navigation pane, and then select the table you want.
1. Select **Properties** >  **Advanced options**.
1. Select the **Track changes** option, and then select **Save**. If the option is unavailable, see known limitations below. 

### Known limitations with finance and operations entities

Currently, there are the following limitations with finance and operations entities and Azure Synapse Link. To learn more about the upcoming roadmap and stay in touch with product team, join the [preview Viva Engage group aka.ms/SynapseLinkforDynamics](https://aka.ms/SynapseLinkforDynamics/).

- Enabling change tracking might fail with the error message "chosen entity doesn't pass the validation rules..." or the **Track changes** checkbox is disabled for some entities. Currently, change tracking can't be enabled for all finance and operations entities. The **Track changes** checkbox is unavailable for entities created in finance and operations in the past for data migration. For more information about entity validation rules and how you can fix them, go to [Enable row version change tracking for data entities](/dynamics365/fin-ops-core/dev-itpro/data-entities/rowversion-change-track#enable-row-version-change-tracking-for-data-entities). You might need developer assistance to complete the steps.
- If the chosen entity is unavailable because of the limitation above, you might be able to choose the tables that comprise the data from that entity.

> [!NOTE]
> For a list of ready-made finance and operations entities that pass validation rules, go to [SupportedEntitiesLink](https://www.yammer.com/dynamicsaxfeedbackprograms/uploaded_files/1647660802048). You must be a member of the preview Yammer group to access this list. To join, visit [Dynamics 365 and Power Platform Preview Programs External Network](https://aka.ms/SynapseLinkforDynamics).
