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
|DV-804: This environment is in admin mode and service is paused | When a Power platform environment is in administration mode all services including Synapse Link service is temporarily paused. <br> When the environment is back in operations mode, the services will be resumed. | Verify with your environment administrator and ensure that the environment is operational <br> Also verify that “background services are enabled” after the admin mode is disabled. <br> 
Synapse Link service will resume when the environment is in operational mode |
| SYN-805: Synapse workspace is not accessible | Synapse Link service can’t access the Synapse workspace associated with this profile <br> Synapse tables may not be created immediately when you resolve this issue. System will create tables in the synapse workspace when data gets updated in Dataverse.| In the Synapse workspace networking configuration, you need to enable the checkbox  “Allow Azure services and resources to access this workspace” |
|








