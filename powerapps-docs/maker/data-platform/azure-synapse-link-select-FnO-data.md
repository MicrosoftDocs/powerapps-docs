---
title: Choose finance and operations data in Azure Synapse Link for Dataverse
description: Learn how to choose finance and operations data in Azure Synapse Link for Dataverse and work with Synapse Link and Power BI.
ms.date: 07/18/2023
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

Azure Synapse Link for Dataverse enables you to choose data from finance and operations apps. Use Azure Synapse Link to continuously export data from finance and operations apps into Azure Synapse Analytics and Azure Data Lake Storage Gen2.

Azure Synapse Link for Dataverse is a service that is designed for enterprise big data analytics by delivering scalable high availability with disaster recovery capabilities. Data is stored in the Common Data Model format, which provides semantic consistency across apps and deployments. 

Azure Synapse Link for Dataverse offers the following features to use with finance and operations data:
- Support for choosing both standard and custom finance and operations entities and tables.
- Continuous replication of Entity and table data as well as create, update, and delete (CUD) transactions. 
- Linking or unlinking the environment to Azure Synapse Analytics and/or Azure Data Lake Storage Gen2 in your Azure Subscription. No need to visit Azure portal or Microsoft Dynamics 365 Lifecycle Services for system configuration.
- Choose data and explore with Synapse. No need to run external tools to configure Synapse Analytics workspaces.
- Support for all of the features of Synapse Link for Dataverse including, availability in all regions, save as Parquet Delta files, and support for restricted storage accounts.
- Table limits in Export to Data lake service aren't applicable in Synapse Link for Dataverse.
- Save as Parquet Delta lake format is enabled by default for finance and operations data enabling faster query response times. 


> [!NOTE]
> This is a preview feature. Export to data lake feature in finance and operations apps will be combined with Synapse Link for Dataverse in the future. We also plan to retire Export to Data Lake service and transition existing customers to Synapse Link for Dataverse. If you are planning to adopt Export to Data Lake feature in finance and operations apps the future, you should consider adopting Synapse Link with finance and operations data support instead. We will provide a path for existing customers to transition to Synapse Link for Dataverse. If you are currently using Export to Data Lake feature in finance and operations apps, you can continue to operate both services in parallel until transition. 


## Prerequisites
- Finance and operations sandbox (Tier-2) with version update 10.0.34 (PU 58) or later. You can use finance and operations Cloud Hosted environment (CHE) for validation. Your CHE needs to be version update 10.0.36 (PU 60) or later.  
- Finance and operations apps environment is linked with Microsoft Power Platform. 
- Azure Subscription with owner access (you can also add finance and operations data to an existing storage account configured with Synapse Link):
  - Storage account. 
  - Synapse Analytics workspace.
  - Synapse Spark pool with version 3.1 or higher (For Delta Lake conversion).

## Power Platform integration
You can enable the preview with an existing finance and operations apps environment if your finance and operations apps environment is updated to ver. 10.0.34 (PU58) or later. You can also validate the feature by provisioning a new Tier-1 environment, also known as a **Cloud Hosted Environment (CHE), with version 10.0.36 (PU 60) or later**.

Enabling Power Platform integration is mandatory. You can link with Power Platform when deploying the new environment. For more information on Powe Platform integration, see [Enable the Microsoft Power Platform integration](/dynamics365/fin-ops-core/dev-itpro/power-platform/enable-power-platform-integration#enable-during-deploy).

To confirm that the finance and operations apps environment is linked with Power Platformse, use Lifecycle Services and review the **Environment** page.

> [!NOTE]
> Dual-write setup is not required to enable finance and operations data in Synapse Link.

## Add configurations in finance and operations apps environment

During the preview, you need to enable the configuration key **Enable SQL row version change tracking** by turning on maintenance mode. For more information about using maintenance mode, see [Turn maintenance mode on and off in DevTest/Demo environments hosted in Customer's subscription](/dynamics365/fin-ops-core/dev-itpro/sysadmin/maintenance-mode#turn-maintenance-mode-on-and-off-in-devtestdemo-environments-hosted-in-customers-subscription).

![Enable Configuration](media/Synapse-Link-Enable-Fno-Configuration.png)

> [!NOTE]
> When using a Tier 1 or CHE environment, you need to perform a full DBSync using Microsoft Visual Studio to complete the maintenance mode.

After **Row Version Change Tracking** is enabled, a system event triggers in your environment that may cause tables in Export to Data lake to reinitialize. If you have downstream consumption pipelines, you may also need to re-initialize the pipelines. For more information, see [Some tables have been "initialized" without user action](/dynamics365/fin-ops-core/dev-itpro/data-entities/finance-data-azure-data-lake#some-tables-have-been-initialized-without-user-action).

## Enable finance and operations apps tables in Synapse Link

You can enable finance and operations entities and finance and operations apps tables in Synapse Link for Dataverse. This section focuses on enabling finance and operations apps tables.

Finance and operations apps tables are allowed only in Synapse Link and they aren't currently enabled for makers to build apps. **You do not need to define finance and operations apps tables as virtual entities or enable change tracking for each table**.

To enable this feature during preview, you need to launch the maker portal using the following URL: [https://make.powerapps.com/environments/{environment-id}/exporttodatalake?athena.enableFnOTables=true](https://make.powerapps.com/environments/{environment-id}/exporttodatalake?athena.enableFnOTables=true).

> [!NOTE]
> Selection of Delta Lake feature is mandatory for finance and operations apps Tables preview.

## Known limitations

There are several limitations in the preview. These limitations will be addressed in the future. To learn more about the upcoming roadmap and stay in touch with product team, join the [preview Yammer group](https://aka.ms/SynapseLinkforDynamics).

- You need to create a new synapse Link profile. You can’t add finance and operations apps tables into existing Synapse Link profiles.
- Finance and operations apps tables shipped by Microsoft are already enabled in Synapse Link except for the set of tables identified below. To enable custom tables, you need to enable change tracking in custom tables. For more information on enabling change tracking, see [Enable row version change tracking for tables](/dynamics365/fin-ops-core/dev-itpro/data-entities/rowversion-change-track#enable-row-version-change-tracking-for-tables).
- The following tables that Microsoft provides aren't currently enabled. These tables will be enabled in a future release.
  - Tables without a unique index on the Rec ID column. For example, REQPLAN.
  - Tables that contain sensitive fields including: CUSTTABLE, VENDTABLE, CONTACTPERSON, VENDBANKACCOUNT, HCMPERSONPRIVATECITIZENSHIPDETAILS, HCMPERSONPRIVATEDETAILS, WHSWORKUSER, CUSTBANKACCOUNT, BANKACCOUNTTABLE, BANKSTMTISOREPORTENTRY, JMGEMPLOYEE.
  - Tables that contain EDT Array types PROJTABLE, TSTIMESHEETLINEWEEK, WHSCONTAINERTABLE, WHSWAVETABLE, WHSINVENTTABLE, RESOURCESETUP.
- When working with finance and operations data, you must choose the Delta lake format as the default. You can enable Delta lake format by following steps here: [Export Microsoft Dataverse data in Delta Lake format](azure-synapse-link-delta-lake.md).
- Finance and operations apps table export using the Delta lake format may take up to an hour to complete during the initial data export. Performance of the initial export will improve in the future updates.
- You can only choose up to 1000 tables in a single Synapse Link profile.

## Enable finance and operations data entities in Synapse Link

You can enable finance and operations entities and finance and operations apps tables in Synapse Link for Dataverse. This section focuses on enabling finance and operations data entities. 

Finance and operations apps entities are enabled in the following two steps. Each step is explained in the following sections.

1. **Enable finance and operations virtual entities in Power Apps maker portal** - this step enables you to use finance and operations entities in Power Apps maker portal to build apps and use with Synapse Link.
2. **Enable change tracking** - this step is required to enable Synapse Link for finance and operations apps entities.

You can now, select finance and operations entities in Synapse Link. Follow the steps to create Synapse link for Dataverse with Delta lake format in the [Export Dataverse data in Delta Lake format](/power-apps/maker/data-platform/azure-synapse-link-delta-lake) article.

> [!NOTE]
> Finance and Operations apps entities starts with prefix mserp\_.

### Enable finance and operations virtual entities in Power Apps maker portal

Finance and operations entities need to be enabled as **virtual entities** in Dataverse. By Enabling finance and operations entities in Dataverse as a **Virtual entity**, you enable the chosen finance and operations entities to makers to build Apps and for Synapse Link. You need to perform the following steps to enable finance and operations entities as virtual entities in Power Apps maker portal.

To Enable finance and operations entities as virtual entities, follow the steps in [Enable Microsoft Dataverse virtual entities](/dynamics365/fin-ops-core/dev-itpro/power-platform/enable-virtual-entities).

> [!TIP]
> To validate Synapse Link features, you can choose a few of the sample entities from the following list:
> -   MainAccountBiEntity: contains a list of Ledger accounts.
> -   ExchangeRateBiEntity: contains exchange rates in the system.
> -   InventTableBiEntity: contains a list of inventory items.

### Enable Change tracking for finance and operations entities

When you enable finance and operations entities as virtual entities in Dataverse, they appear in the maker portal. Finance and operations entities start with prefix **mserp\_**.

To enable Track changes, follow these steps.

1. In Dataverse, select the table.
2. Select **Properties \> Advance Options**.
3. Select **Track changes**. The checkbox should be enabled. If the checkbox is disabled, see **The chosen entity doesn't pass validation rules required to enable change tracking**.

### Troubleshooting 

This section explains how to troubleshoot issues that may occur when you enable change tracking. 

#### The chosen entity doesn't pass validation rules required to enable change tracking.

Currently not all finance and operations entities can be enabled for change tracking. If the **Track changes** checkbox is disabled for entities that fail validation rules. For more information on entity validation rules and how you can fix the validation rules, see [Enable row version change tracking for data entities](/dynamics365/fin-ops-core/dev-itpro/data-entities/rowversion-change-track#enable-row-version-change-tracking-for-data-entities). You may need developer assistance to complete the steps.

> [!NOTE]
> For a list of ready-made entities that pass validation rules, see [SupportedEntitiesLink](https://www.yammer.com/dynamicsaxfeedbackprograms/uploaded_files/1647660802048)
> You need to be a member of the preview yammer group to access this list. To join, visit [https://aka.ms/SynapseLinkforDynamics](https://aka.ms/SynapseLinkforDynamics)

