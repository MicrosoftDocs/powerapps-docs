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
> Enabling F&O tables in Synapse Link is in private preview. If you would like to join private preview, join the preview group by visiting [https://aka.ms/SynapseLinkforDynamics](https://aka.ms/SynapseLinkforDynamics)

# Prerequisites
- Finance and Operations Cloud Hosted Environment (CHE) or Tier 2+ environment with version update 10.0.34 (PU 58) (We Recommend using CHE environment or a Sandbox for validation) 
- Finance and Operations environment is linked with Power Platform. 
- Azure Subscription with owner access (you can also add F&O data to an existing storage account configured with Synapse Link)
o	Storage account 
o	Synapse Analytics workspace 
o	Synapse Spark pool with version 3.1 or higher (For Delta Lake conversion)

