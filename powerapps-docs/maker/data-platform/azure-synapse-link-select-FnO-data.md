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

| How you plan to consume data  |  Synapse Link feature you'll use | Prerequisites and Azure resources needed |
|-------------------------------|------------------------------------|------------------------------------------|
| Access finance and operations tables via Synapse query |  [Synapse Link - Delta lake](/powerapps-docs-pr/powerapps-docs/maker/data-platform/azure-synapse-link-delta-lake.md) |  Azure Data lake <br> Azure Synapse workspace <br> Azure Synapse Spark pool <br> Your data is saved in delta parquet format enabling better read performance | 
| Load incremental data changes into your own downstream data warehouse | [Synapse Link - incremental update](azure-synapse-link-incremental.md) | Azure data lake <br> No need to bring Synapse workspace or spark pool as your data will be saved in CSV format |
| Access finance and operations tables via Microsoft Fabric | [Link to Fabric](/powerapps-docs/maker/data-platform/azure-synapse-link-view-in-fabric.md)  | Microsoft Fabric workspace |

### Link your finance and operations environment with Microsoft Power Platform

Verify with your finance and operations systems administrator whether your Finance and Operations environment is linked to Power platform.

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

After row version change tracking is enabled, a system event that's triggered in your environment might cause re-initialization of tables in export to data lake. If you have downstream consumption pipelines, you might have to reinitialize the pipelines. More information: [Some tables have been "initialized" without user action](/dynamics365/fin-ops-core/dev-itpro/data-entities/finance-data-azure-data-lake#some-tables-have-been-initialized-without-user-action).

## Add finance and operations tables in Azure Synapse Link

You can enable both finance and operations entities and finance and operations tables in Azure Synapse Link for Dataverse. This section is focused on finance and operations tables.

1. Sign in to Power Apps and select the environment you want.
2. On the left navigation pane, select **Azure Synapse Link**.
3. On the command bar of the **Synapse Link** page, select **+ New link to data lake**.
4. Select **Connect to your Azure Synapse Analytics workspace**, and then select the **Subscription**, **Resource group**, and **Workspace name**.
5. Select **Use Spark pool for processing**, and then select the pre-created Spark pool and storage account.
6. Select **Next**.
7. Add the tables you want to export. You can choose finance and operations tables provided the [prerequisites](#prerequisites) are met.
8. Select **Advanced**, select **Show advanced configuration settings** and enter the time interval, in minutes, for how often the incremental updates should be captured.
9. Select **Save**. Tables selected are initialized and ready for reporting.

> [!NOTE]
>
> - Finance and operations apps tables are allowed only in Azure Synapse Link. Makers can't currently use them to build apps.
> - You don't have to define finance and operations apps tables as virtual entities, and you don't have to enable change tracking for each table.
>
> To include finance and operations tables in Synapse Link, you must enable [Delta lake feature](/power-apps/maker/data-platform/azure-synapse-link-delta-lake) in your Synapse Link profile. Finance and operations table selection will not be visible if your Synapse Link profile isn't configured for Delta lake.
>
> Delta lake conversion time interval determines how often table data is updated in delta format. For near real time updates, you can choose 15 minutes or one hour as the desired updated time internal. You might choose daily time interval if near real-time updates aren't required. Delta conversion consumes compute resources from the Spark pool you have provided in the configuration of the Synapse Link profile. The lower the time interval, the more compute resources are consumed and you can incur more cost. Open the Spark pool in Azure portal to see the compute cost.
>
> In the event that the system ran into an error during initial sync or updates, you'll see an error icon and a pointer to trouble-shooting documents that can be used to diagnose and resolve the error.

### Known limitations <!-- You have three sections in this article with this same name. Either incorporate the all the known limitations content into one section or rename affected sections to clearly describe what each section represents. -->

Currently, there are the following limitations. To learn more about the upcoming roadmap and stay in touch with the product team, join the [preview Viva Engage group](https://aka.ms/SynapseLinkforDynamics/).

- You must create a new Azure Synapse Link profile. You can't add finance and operations apps tables to existing Azure Synapse Link profiles.
- Don't see all tables? Up to 2,750 Microsoft provided finance and operations apps tables are already enabled in Azure Synapse Link with application version 10.0.38. If you have a previous version of finance and operations apps, not all required tables may be enabled by default. You can enable more tables yourself by extending table properties and enabling the change tracking feature. For more information about how to enable change tracking, see [Enable row version change tracking for tables](/dynamics365/fin-ops-core/dev-itpro/data-entities/rowversion-change-track#enable-row-version-change-tracking-for-tables).
3. Don't see your custom tables? you must enable change tracking in them. For more information about how to enable change tracking, see [Enable row version change tracking for tables](/dynamics365/fin-ops-core/dev-itpro/data-entities/rowversion-change-track#enable-row-version-change-tracking-for-tables).
4. You can choose a maximum of 1,000 tables in an Azure Synapse Link profile. To enable more tables, create another Synapse Link profile.
5. If the table selected contains data fields that secured via **AOS Authorization**, those fields will be ignored and the exported data does not contain the field. For an Example in CustTable, the field TaxLicenseNum has the metadata property AOS Authorization set to Yes. This field is ignored when CustTable data is exported with Synapse Link.  
6. If the table selected contains data fields that are of Array type, those fields will be ignored anf the exported data does not contain the field. For an Example i WHSInventTable table, fields FilterCode and FilterGroup are of type Array. These fields are not exported with Synapse Link.

## Access incremental data changes from Finance and Operations
If want to load incremental data changes from Finance and Operations into your own downstream Data warehouse, you can create a Synape Link profile that provides only incremental data. Synapse Link will  provide an initial export of all data rows and then provide you with access to data that changed periodically. The data is provided via CSV files stored in time stamped folders and you can easily consume the data using Azure Data factory or other data tools. See  [Synapse Link - incremental update](azure-synapse-link-incremental.md) for more details.

To create a Synapse Link profile with incremental data:

1. Sign in to Power Apps and select your preferred environment
2. On the left navigation pane, select Azure Synapse Link.
3. In Synapse Link page, On the command bar, select + New link to data lake.
4. Select Subscription, Resource group and a Storage account. You do not need to provide a Synapse workspace or a spark pool.
6. Select Next. You will see the option to choose tables. 
7. Select **Advanced**, select **Show advanced configuration settings** and enable the option **Enable incremental update folder structure**
8. In the **Time interval** field, choose the desired frequency for reading incremental data. Using this frequency, system will partition data into time stamped folders such that you can read the data without being impacted by ongoing write operations.  
9. You will be able to choose tables from Dataverse as well as Finance and Operations. Finance and Operations tables will appear in the selection.
10. Options **Append only** and **Partition** available at a table level are ignored. Data files are always appended and data is partitioned Yearly.
11. Choose tables and select **Save**. Tables selected will be initialized and you will see incremental data in the storage account

> [!NOTE]
> 
> If you are upgrading from Export to Data lake feature, enabling incremental data changes option provides similar change data as the [Change feeds feature](https://learn.microsoft.com/dynamics365/fin-ops-core/dev-itpro/data-entities/azure-data-lake-change-feeds)
>
> It is recommended that you create seperate Synapse Link profiles for incremental data and table for ease of management.

### Known limitations
All the known limitations applicable to Finance and Operations Tables are applicable to incremental data. 


## Enable finance and operations data entities in Azure Synapse Link

You can enable both finance and operations entities and finance and operations apps tables in Azure Synapse Link for Dataverse. This section is focused on finance and operations data entities.

The process of enabling finance and operations entities has the following steps. Each step is explained in the following subsections.

1. **Enable finance and operations virtual entities in the Power Apps maker portal.** This step lets you use finance and operations entities in the Power Apps maker portal to build apps. You can also use them with Azure Synapse Link.
2. **Enable change tracking for finance and operations entities.** You must complete this step to enable Azure Synapse Link to use finance and operations entities.

After you've completed both steps, you can select finance and operations entities in Azure Synapse Link. To create Synapse Link for Dataverse in Delta Lake format, follow the steps in [Export Dataverse data in Delta Lake format](/power-apps/maker/data-platform/azure-synapse-link-delta-lake).

> [!NOTE]
> Finance and operations entities start with the prefix **mserp\_**.

### Enable finance and operations virtual entities in the Power Apps maker portal

You must enable finance and operations entities as **virtual entities** in Dataverse. Makers can then use the chosen finance and operations entities to build apps, and the entities can also be used with Azure Synapse Link.

To enable finance and operations entities as virtual entities, follow the steps in [Enable Microsoft Dataverse virtual entities](/dynamics365/fin-ops-core/dev-itpro/power-platform/enable-virtual-entities).

> [!TIP]
> To validate Azure Synapse Link features, you can use a few of the sample entities from the following list:
>
> - **MainAccountBiEntity** – This entity contains a list of ledger accounts.
> - **ExchangeRateBiEntity** – This entity contains exchange rates in the system.
> - **InventTableBiEntity** – This entity contains a list of inventory items.

### Enable change tracking for finance and operations entities

When you enable finance and operations entities as virtual entities in Dataverse, they appear in the maker portal. Finance and operations entities start with the prefix **mserp\_**.

To enable change tracking, follow these steps.

1. In Dataverse, select the table.
2. Select **Properties \> Advance Options**.
3. Select the **Track changes** checkbox. If the checkbox is unavailable, see [The chosen entity doesn't pass the validation rules that are required to enable change tracking](#entity-fails-val-rules) later in this article. <!-- There's no section in this article that corresponds to this bookmark -->

### Knwon limitations
There are several limitations that will be addressed in future releases. To learn more about the upcoming roadmap and stay in touch with product team, join the [preview Viva Engage group aka.ms/SynapseLinkforDynamics](https://aka.ms/SynapseLinkforDynamics/).

1. Enabling change tracking may fail with the error message "chosen entity doesn't pass the validation rules..." or the Track changes checkbox may be disabled for some entities. Currently, change tracking can't be enabled for all finance and operations entities. The **Track changes** checkbox is unavailable for entities created in Finance and Operations in the past for data migration.  
2. For more information about entity validation rules and how you can fix them, see [Enable row version change tracking for data entities](/dynamics365/fin-ops-core/dev-itpro/data-entities/rowversion-change-track#enable-row-version-change-tracking-for-data-entities). You might require developer assistance to complete the steps.
3. If the chosen Entity is unavailable (ie. due to limitation above), you may be able to choose the tables that comprise the data from that entity.  

> [!NOTE]
> For a list of ready-made entities that pass validation rules, see [SupportedEntitiesLink](https://www.yammer.com/dynamicsaxfeedbackprograms/uploaded_files/1647660802048). You must be a member of the preview Yammer group to access this list. To join, visit [https://aka.ms/SynapseLinkforDynamics](https://aka.ms/SynapseLinkforDynamics).
