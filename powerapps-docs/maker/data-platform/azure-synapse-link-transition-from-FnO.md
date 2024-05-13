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

##Before transition 
If you are a customer using legacy services BYOD, DES or Export to Data lake, you may have a data integration architecture similar to the one shown below. The highlighted box indicates the data pipelines your organization may have built to leverage the data exported from Dynamics 365 and Dataverse. You may use a selection of tools from Microsoft as well as others to copy and integrate Dynamics data with your own data. You may also transform and aggregate data by copying into multiple stores – shown under the Data-prep box. You may use Power BI or another tool to visualize data and create actionable insights. You may also have pipelines built to export data to an on-premise system and/or other clouds.
<< before picture >>




