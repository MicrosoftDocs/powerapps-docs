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
You can enable the preview with an existing F&O environment if your F&O environment is updated to ver. 10.0.34 (PU58) or later. You can also validate the feature by provisioning a new Tier-1 environment, also known as a **Cloud Hosted Environment (CHE), with version 10.0.34 (PU 60) or later**.

Enabling Power platform integration is mandatory. You can link with Power Platform deploying the new environment. See [Enable the Microsoft Power Platform integration - Finance & Operations \| Dynamics 365 \| Microsoft Learn](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/power-platform/enable-power-platform-integration#enable-during-deploy)

You can confirm that the F&O environment is linked with Power platform by visiting Dynamics Life cycle services and reviewing the environment page.

**NOTE:** Dual-Write setup is not required to enable F&O data in Synapse Link

## Add configurations in F&O environment

During preview, you need to enable configuration key **Enable SQL row version change tracking** by turning on maintenance mode. See here for details of [Maintenance mode - Finance & Operations \| Dynamics 365 \| Microsoft Learn](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/maintenance-mode#turn-maintenance-mode-on-and-off-in-devtestdemo-environments-hosted-in-customers-subscription)




