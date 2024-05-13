---
title: transition from Export to Data lake and BYOD to Fabric Link and Synapse Link for Dataverse
description: Learn how to transition from Export to Data lake and BYOD in finance and operations to Link to Fabric and Azure Synapse Link for Dataverse 
ms.date: 05/11/2024
ms.reviewer: matp 
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
# Transitioning from Export to Data Lake and BYOD

Data export service (DES), [BYOD](https://learn.microsoft.com/dynamics365/fin-ops-core/dev-itpro/analytics/export-entities-to-your-own-database), [Export to Data lake](https://learn.microsoft.com/dynamics365/fin-ops-core/dev-itpro/data-entities/azure-data-lake-ga-version-overview) were features introduced in Dynamics 365 apps to export data for analytics and data integration scenarios. These services enabled IT admins and specialists to export data into external databases or data lakes and build data integration pipelines. While we have improved these services over the years with updates, as part of unification of Dynamics 365 with the power platform, we have rearchitected the same capabilities of these disparate services into simpler, unified experiences built into Power Apps maker portal. Transitioning to Fabric Link or upgrading to Synapse Link, the rearchitected services, provide you with an easy ramp to benefit from AI and Copilot investments in Dataverse and Microsoft Fabric.

If you are a customer using any of the previous generation services, this document provides guidance on upgrading to new experiences, benefiting from innovations as well as reducing end-to-end expenses and effort.

Based on preview customer surveys, we have also compiled a high level cost and benefits estimate to enable you to help with the transition. You will also see links to more information and videos as well as links to join forums and weekly office hour sessions to engage with product team, Microsoft specialists as well as fellow users as we continue to enhance these services with community participation.

## Before transition 

If you are a customer using legacy services BYOD, DES or Export to Data lake, you may have a data integration architecture similar to the one shown below. The highlighted box indicates the data pipelines your organization may have built to leverage the data exported from Dynamics 365 and Dataverse. You may use a selection of tools from Microsoft as well as others to copy and integrate Dynamics data with your own data. You may also transform and aggregate data by copying into multiple stores – shown under the Data-prep box. You may use Power BI or another tool to visualize data and create actionable insights. You may also have pipelines built to export data to an on-premise system and/or other clouds.
<< before picture >>

## After transition

There are 2 data integration patterns enabled in Power Apps maker portal. 
-	Synapse Link enables continuous export of data similar to BYOD, Export to Data lake or DES services. This option is enabled for IT admins and data integration specialists.
-	Link to Fabric feature provides a no-copy, no-ETL, fully managed software as a service (SaaS) integration.

<< after picture>> 

These options are complementary and we provide a detailed comparison below. 

If you are a Finance and Operations customer, currently using BYOD or Export to Data lake features, by upgrading to Synapse Link or Fabric Link, you can benefit from:

Simplified data integration architecture resulting in reduced operational costs 
•	Easy to configure and maintain via Power Apps maker portal - Built-in integration with Synapse and Microsoft Fabric
•	Synapse Link and Fabric Link are fully managed services - requires minimal ongoing management overhead
•	New services offer the same data shapes as previous services – your existing downstream integration pipelines can remain as is.
•	Minimal impact to operational workloads, you don’t need manage workloads and schedule data exports 

Secure, end-to-end data integration pipelines 
-	With Fabric link, your data doesn’t leave Dataverse governance boundary while authorized Fabric users can securely access data that resides within Dataverse
-	Synapse Link service enables you to restrict access to your storage accounts with firewalls while enabling Dataverse to export data with Managed Service Identities (MSI) a security feature built into Microsoft Entra. 

If you are a Dynamics 365 customer using Data Export service (DES) or classic Synapse Link with data exports in CSV format, you can benefit from efficient reporting enabled with the industry standard Delta/ Parquet data format.
•	Built-in Delta/ parquet conversion option reduces the need to build your own pipelines for analytics and operational reporting
•	Delta parquet format enables faster, more responsive queries & reports and scales to larger datasets of any size.
•	Data in lake is compressed to 1/3 ~ 1/8 the original size - resulting in smaller files that reduce data query and carrying costs

| link to Fabric  |  Azure Synapse Link |
|-------------------------------|------------------------------------|
| No copy, no ETL direct integration with Microsoft Fabric.	 | Export data to your own storage account and integrate with Synapse, Microsoft Fabric, and other tools. |
| Data stays in Dataverse - users get secure access in Microsoft Fabric. | 	Data stays in your own storage. You manage access to users.|
| All tables chosen by default.	| System administrators can choose required tables. |
|Consumes additional Dataverse storage.	| Consumes your own storage as well as other compute and integration tools.| 



