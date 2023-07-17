---
title: "Choose Dynamics 365 Finance and Operations data | MicrosoftDocs"
description: "Learn how to choose Dynamics 365 Finance and Operations data in Synapse Link for Dataverse and work with Synapse Link and PowerBI"
ms.custom: ""
ms.date: 05/25/2023
ms.reviewer: "matp"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
applies_to: 
  - "powerapps"
author: "Milindav"
ms.assetid: 
ms.subservice: dataverse-maker
ms.author: "Milindav"
search.audienceType: 
  - maker
---
# Overview

Azure Synapse Link for Dataverse enables choosing data from Dynamics 365 for Finance and Operations (F&O). Using Azure Synapse Link, you can continuously export data from F&O into
- Azure Synapse Analytics
- Azure Data Lake Storage Gen2

The Azure Synapse Link for Dataverse is a service designed for enterprise big data analytics by delivering scalable high availability with disaster recovery capabilities. Data is stored in the Common Data Model format, which provides semantic consistency across apps and deployments. 

The Azure Synapse Link for Dataverse offers these additional features for D365 F&O data.
- Supports choosing both standard and custom F&O entities and Tables
- Continuous replication of Entity and table data as well as create, update, and delete (CUD) transactions. 
- Linking or unlinking the environment to Azure Synapse Analytics and/or Azure Data Lake Storage Gen2 in your Azure Subscription. No need to visit Azure portal or Dynamics Life Cycle Services (LCS) for system configuration.
- Simply choose data and explore with Synapse. No need to run external tools to configure Synapse Analytics workspaces
- Support all the features of Synapse Link for Dataverse including, availability in all regions, save as Parquet Delta files as well as support for restricted storage accounts
- Table limits in Export to Data lake service are not applicable in Synapse Link for Dataverses
- Save as Parquet Delta lake format is enabled by default for F&O data enabling faster query response times. 


> [!NOTE]
>This is a preview feature
>
> Export to data lake feature in Dynamics 365 Finance and Operations (F&O) will be combined with Synapse Link for Dataverse in the future. We also plan to retire Export to Data Lake service and transition existing customers to Synapse Link for Dataverse.
If you are planning to adopt Export to Data Lake feature in F&O the future, you should consider adopting Synapse Link with F&O data support instead. 
We will provide a path for existing customers to transition to Synapse Link for Dataverse. If you are currently using Export to Data Lake feature in F&O, you can continue to operate both services in parallel until transition. 


# Prerequisites
- F&O Sandbox (Tier-2) with version update 10.0.34 (PU 58) or later. You can also use F&O Cloud Hosted environment (CHE) for validation. Your CHE needs to be version update 10.0.36 (PU 60) or later  
- Finance and Operations environment is linked with Power Platform. 
- Azure Subscription with owner access (you can also add F&O data to an existing storage account configured with Synapse Link)
o	Storage account 
o	Synapse Analytics workspace 
o	Synapse Spark pool with version 3.1 or higher (For Delta Lake conversion)

# Power platform integration
You can enable the preview with an existing F&O environment if your F&O environment is updated to ver. 10.0.34 (PU58) or later. You can also validate the feature by provisioning a new Tier-1 environment, also known as a **Cloud Hosted Environment (CHE), with version 10.0.36 (PU 60) or later**.

Enabling Power platform integration is mandatory. You can link with Power Platform deploying the new environment. See [Enable the Microsoft Power Platform integration - Finance & Operations \| Dynamics 365 \| Microsoft Learn](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/power-platform/enable-power-platform-integration#enable-during-deploy)

You can confirm that the F&O environment is linked with Power platform by visiting Dynamics Life cycle services and reviewing the environment page.

**NOTE:** Dual-Write setup is not required to enable F&O data in Synapse Link

## Add configurations in F&O environment

During preview, you need to enable configuration key **Enable SQL row version change tracking** by turning on maintenance mode. See here for details of [Maintenance mode - Finance & Operations \| Dynamics 365 \| Microsoft Learn](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/maintenance-mode#turn-maintenance-mode-on-and-off-in-devtestdemo-environments-hosted-in-customers-subscription)

![Enable Configuration](/media/Synapse-Link-Enable-Fno-Configuration.png)

**NOTE:** When using Tier 1 or CHE environment, you need to perform full DBSync using Visual Studio to complete the maintenance mode.

Enabling **Row Version Change Tracking** triggers a system event in your environment that may cause tables in Export to Data lake to re-initialize. If you have downstream consumption pipelines, you may also need to re-initialize the pipelines. See documentation for more details.

# Enable F&O data entities in Synapse Link

You can enable F&O entities as well as F&O Tables in Synapse Link for Dataverse. This section focuses on enabling F&O data entities. To enable F&O Entities;

1.  **Enable F&O virtual entities in PowerApps maker portal**: this step enables you to use F&O Entities in PowerApps maker portal to build apps as well as use with Synapse Link
2.  **Enable change tracking**: this step is required to enable Synapse Link for F&O Entities

You will be able to choose F&O entities in Synapse Link (Hint: see tables with mserp\_ prefix)

## Enable F&O virtual entities in PowerApps maker portal

You need to enable F&O Entities as **virtual entities** in Dataverse. By Enabling F&O Entities in PowerApps maker portal as a **Virtual entity**, you enable the chosen F&O Entities to makers to build Apps as well as for Synapse Link. You need to perform the following steps to enable F&O entities as virtual entities in PowerApps maker portal.

To Enable F&O entities as virtual entities see the steps here: [Enable Microsoft Dataverse virtual entities - Finance & Operations \| Dynamics 365 \| Microsoft Learn](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/power-platform/enable-virtual-entities)

**Hint**: for validating Synapse Link features, you can choose a few of the sample entities from the following list

-   MainAccountBiEntity: contains a list of Ledger accounts
-   ExchangeRateBiEntity: contains exchange rates in the system
-   InventTableBiEntity: contains a list of inventory items

## Enable Change tracking for F&O entities

When you enable F&O entities as virtual entities in Dataverse, they will appear in the maker portal (hint: F&O entities start with prefix **mserp\_**)

To enable Track changes in Dataverse, Select the Table, **Select \> Properties\> Advance Options**

Select **Track changes**. The checkbox should be enabled. See troubleshooting steps below in case the checkbox is disabled.

### Chosen Entity does not pass validation rules required to enable change tracking.

Not all F&O entities can be enabled for change tracking at this point in time. Track changes checkbox is disabled for Entities that fail validation rules. See here for more information on entity validation rules and how you can fix the validation rules. You may need developer assistance in completing the steps.

[Allow Row version change tracking for tables and data entities - Finance & Operations \| Dynamics 365 \| Microsoft Learn](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/rowversion-change-track#enable-row-version-change-tracking-for-data-entities)

For a list of ready-made entities that pass validation rules, see here: \<need to add this list somewhere\> [SupportedEntitiesLink](https://www.yammer.com/dynamicsaxfeedbackprograms/uploaded_files/1647660802048)

### Virtual entity definition is obsolete

Underlying Entity definition may have changed since it was defined. You will need to refresh

# Enable F&O Tables in Synapse Link

You can enable F&O entities as well as F&O Tables in Synapse Link for Dataverse. This section focuses on enabling F&O Tables.

F&O Tables are allowed only in Synapse Link and they are not enabled for makers to build apps at this point in time. **You do not need to define F&O tables as virtual entities or enable change tracking for each table**.

To Enable this feature during preview, you need to launch the maker portal with the following

**https://make.powerapps.com/environments/{environment-id}/exporttodatalake?athena.enableFnOTables=true**

**NOTE:** selection of Delta Lake feature is mandatory for F&O Tables preview.

## Known limitations

There are several limitations in the preview. These limitations will be addressed in the future. To know more about the upcoming roadmap and stay in touch with product team, you can join the preview yammer group at <https://aka,ms/SynapseLinkforDynamics>

1.  You need to create a new synapse Link profile. You can’t add F&O tables into existing Synapse Link profiles.
2.  F&O Tables can’t be added to Managed Store, aka. Data lake provisioned with Dataverse at this point in time.
3.  F&O Tables shipped by Microsoft are already enabled in Synapse Link except for a set of tables identified below. To enable custom tables, you need to enable change tracking in custom tables as explained here: [Allow Row version change tracking for tables and data entities - Finance & Operations \| Dynamics 365 \| Microsoft Learn](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/rowversion-change-track#enable-row-version-change-tracking-for-tables)
4.  Following Tables shipped by Microsoft are not enabled at this point in time. We will enable these tables in a future release.
    1.  Tables without a unique index on Rec id column (ex. REQPLAN)
    2.  Tables that contain sensitive fields including: CUSTTABLE, VENDTABLE, CONTACTPERSON, VENDBANKACCOUNT, HCMPERSONPRIVATECITIZENSHIPDETAILS, HCMPERSONPRIVATEDETAILS, WHSWORKUSER, CUSTBANKACCOUNT, BANKACCOUNTTABLE, BANKSTMTISOREPORTENTRY, JMGEMPLOYEE
    3.  Tables that contain EDT Array types PROJTABLE, TSTIMESHEETLINEWEEK, WHSCONTAINERTABLE, WHSWAVETABLE, WHSINVENTTABLE, RESOURCESETUP
5.  F&O table updates in Delta parquet format may take upto 1hr. We are working to reduce the time.
6.  You must choose the Delta lake format as the default when working with F&O data. You can enable Delta lake format by following steps here: [Export Microsoft Dataverse data in Delta Lake format - Power Apps \| Microsoft Learn](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/azure-synapse-link-delta-lake)
7.  At this point, you can only choose up to 1000 tables in a single Synapse Link profile.



