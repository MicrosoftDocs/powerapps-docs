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

| MSI-801: Synapse Link is unable to access storage account secured via MSI. Data updates are paused 
| You have enabled managed services identify (MSI) to the storage account selected for this Synapse Link profile. <br> Synase Link service does not have access to the storage account due to MSI configuration issues and the service has paused. <br> You need revisit and verify MSI configuration 
| Verify that the MSI policy is not deleted <br> Validate that MSI is granted with the required access privileges. <br> See documentation for [MSI configuration](https://learn.microsoft.com/power-apps/maker/data-platform/azure-synapse-link-msi) <br> Once required access is granted, the service will resume
|  

| ADLS-802: Synapse Link is unable to access storage account. Data updates are paused 
| Row 2, Column 2 
| Row 2, Column 3 
|


