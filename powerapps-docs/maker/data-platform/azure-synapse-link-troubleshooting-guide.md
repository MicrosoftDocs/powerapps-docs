---
title: "Azure Synapse Link trouble shooting guide | MicrosoftDocs"
description: "Troubleshoot issues in Azure Synapse Link service in Power Apps"
ms.custom: ""
ms.date: 01/05/2024
ms.reviewer: "Mattp123"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
applies_to: 
  - "powerapps"
author: "milindav"
ms.assetid: 
ms.subservice: dataverse-maker
ms.author: "matp"
search.audienceType: 
  - maker
contributors:
  - JasonHQX
  - jovanpop
---

# Synapse Link trouble-shooting guide 

When opening a Synapse Link profile, you may see an error with a message and link to this document. In addition, user may also see “Error” status next to tables that are already in a Synapse Link profile. You can use this troubleshooting guide to diagnose and fix error conditions.

| Error message  | Cause  | Resolution |
| -------- | -------- | -------- |
| MSI-801: Synapse Link is unable to access storage account secured via MSI. Data updates are paused | You have enabled managed services identify (MSI) to the storage account selected for this Synapse Link profile. <br> Synase Link service does not have access to the storage account due to MSI configuration issues and the service has paused. <br> You need revisit and verify MSI configuration | Verify that the MSI policy is not deleted <br> Validate that MSI is granted with the required access privileges. <br> See documentation for [MSI configuration](https://learn.microsoft.com/power-apps/maker/data-platform/azure-synapse-link-msi) <br> Once required access is granted, the service will resume |  
| ADLS-802: Synapse Link is unable to access storage account. Data updates are paused | Synapse Link service can’t access storage account and the service has paused. <br> Permissions associated with storage account assigned to Synapse Link profile may have changed or the storage account may not exist.| Verify that the storage account exists and that the Azure Synapse Link service has owner access to storage account. <br> See [configuration documents](https://learn.microsoft.com/power-apps/maker/data-platform/azure-synapse-link-data-lake#prerequisites) <br> Once required access is granted, the service will resume |
|CT-803: Row version change tracking configuration key disabled in linked environment. Data updates in some tables may be paused. | Synapse Link service requires a configuration key “enable row version change tracking” to be enabled in the linked FnO environment. This configuration key has been disabled in the linked environment and the service has paused FnO tables from the linked environment. <br> It is possible that a database restore operation has caused the configuration to be reverted. <br> Enable the configuration key and you need to remove and re-add FnO tables to resume. Impacted tables will be initialized to reflect new data. | Your administrator needs to re-enable the FnO configuration key. <br> See [documentation](https://learn.microsoft.com/power-apps/maker/data-platform/azure-synapse-link-select-fno-data#add-configurations-in-a-finance-and-operations-apps-environment) <br> The service will resume when the configuration key is enabled.|
|DV-804: This environment is in admin mode and service is paused | When a Power platform environment is in administration mode all services including Synapse Link service is temporarily paused. <br> When the environment is back in operations mode, the services will be resumed. | Verify with your environment administrator and ensure that the environment is operational <br> Also verify that “background services are enabled” after the admin mode is disabled. <br> Synapse Link service will resume when the environment is in operational mode |
| SYN-805: Synapse workspace is not accessible | Synapse Link service can’t access the Synapse workspace associated with this profile <br> Synapse tables may not be created immediately when you resolve this issue. System will create tables in the synapse workspace when data gets updated in Dataverse.| In the Synapse workspace networking configuration, you need to enable the checkbox  “Allow Azure services and resources to access this workspace” |
|SYN-806: default storage container in Synapse workspace is not accessible | Synapse workspace associated with this Synapse Link profile does not contain a primary ADLS gen 2 file system. The default storage container may be deleted or the default storage container is not accessible. <br> A default storage container is used by Synapse workspace as temporary storage in creating the file system. Default storage container must be provided when creating a Synapse workspace. <br> It is possible that this storage container was deleted or no longer accessible. | Ask your administrator to launch Synapse workspace and verify the name of the Primary ADLS Gen 2 file system.<br> Also verify that an ADLS gen 2 storage container exists with that name within the same subscription. <br> If the storage container is missing, create a storage container with the same name |
| SPARK-807: Spark compute pool <<pool name>> in <<Synapse workspace> is no longer available. Service is paused | Synapse Link service requires a spark pool in order to process data into delta format. The spark pool provided with this Synapse Link profile is deleted or no longer accessible. <br> It is also possible that access to the Synapse workspace has been restricted. <br> Once you resolve the issue, Synapse Link service will resume data updates as and when data changes | Verify that the spark pool with the chosen name exists. If you or someone deleted this spark pool, create the spark pool with the same name |
| SPARK-808: Spark compute pool <<name>> in <<Synapse workspace> is insufficient. One or more tables could not be updated. | Synapse link service uses the spark pool provided in the configuration to convert files to Delta parquet format as and when data is updated. <br> When a large batch of data is available for update, the size of the spark pool provided in the Synapse Link profile may not provide sufficient compute power. <br> This may happen especially when you add large tables as the initialization process creates a large batch of data. <br> This may also result in case you have “pay as you go” subscriptions with limited capacity. The spark pools within these types subscriptions are limited in capacity. | You can increase the number of cores in the assigned spark pool. <br> System will consume the increased capacity in case of larger workloads and scale down as needed. <br> See [recommended spark pool sizes for Delta conversion](https://learn.microsoft.com/power-apps/maker/data-platform/azure-synapse-link-delta-lake#recommended-spark-pool-configuration) |
| CT-809: Row version change tracking property disabled in Table. This table is paused | Synapse Link service requires enabling the “Row version change tracking” metadata property. This property is disabled for the table and the table is no longer updated. <br> Updating this metadata property in Finance and Operations requires developer intervention. It is possible that the property was disabled after the Synapse Link was profile created. | Re-enable the row version change tracking metadata property to resume this table. <br> You may need an administrator or the developer to re-enable the property using developer tools. See [documentation](https://learn.microsoft.com/dynamics365/fin-ops-core/dev-itpro/data-entities/rowversion-change-track#enable-row-version-change-tracking-for-tables) for details. | 
| FnO-810: Linked Finance and Operations environment is unavailable or paused | FnO environment linked to this Synapse Link profile is either unavailable or in maintenance mode. Synapse Link service is unable to contact FnO environment and the service has paused for tables sourced from FnO. <br> In case of Cloud Hosted Environments (CHE) it is possible that the environment is in a paused state. | Verify with your administrator that the linked FnO environment is not paused and not in maintenance mode. <br> Synapse Link service will resume when the environment is in operational mode |
|FnO-811: Linked Finance and Operations environment needs to be updated | FnO environment linked to this Synapse Link profile needs to be updated to the latest version. <br> If you are currently on FnO versions PU60 or PU61, you need to take the latest cumulative update <br> 10.0.36 (PU 60) - 7.0.7036.133 or Higher <br> 10.0.37 (PU 61) - 7.0.7068.109 or Higher <br> If you are updating to PU62, do not forget to apply the latest cumulative update 10.0.38 (PU 62) - 7.0.7120.59 or Higher | Contact your FnO administrator and apply the latest version updates to your FnO environment. |




 














