---
title: "Transport Azure Synapse Link for Dataverse configuration | MicrosoftDocs"
description: "Learn to transport Azure Synapse Link for Dataverse configurations across environments."
ms.custom: ""
ms.date: 11/01/2021
ms.reviewer: "Mattp123"
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "conceptual"
applies_to: 
  - "powerapps"
author: "sama-zaki"
ms.assetid: 
ms.subservice: dataverse-maker
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
contributors: ""
---

# Transport the Azure Synapse Link for Dataverse configuration across environments

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

In Power Apps, solutions are used to transport apps and components from one environment to another, or to apply a set of customizations to existing apps. Making the Azure Synapse Link for Dataverse configurations solution-aware enables basic application lifecycle management (ALM) abilities such as distribution, copy, and backup and restore of the Azure Synapse Link for Dataverse configuration.

> [!NOTE]
> Azure Synapse Link for Microsoft Dataverse was formerly known as Export to data lake. The service was renamed effective May 2021 and will continue to export data to Azure Data Lake as well as Azure Synapse Analytics.

## Prerequisites

This section describes the prerequisites necessary to transport the Azure Synapse Link for Dataverse configuration across environments.

- **Azure Synapse Link for Dataverse.** This guide assumes that you have already exported data from Dataverse by using the [Azure Synapse Link for Dataverse](export-to-data-lake.md).

## Install the Azure Synapse Link for Dataverse solution

> [!NOTE]
> The Azure Synapse Link for Dataverse solution must be installed in both the source and the destination environments.

1. Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), and then select the source environment for the Azure Synapse Link for Dataverse configuration.

2. On the left navigation pane, select **Solutions** > **Open AppSource**.

    ![Open App Source](media/open-app-source.png "Open App Source")

3. Select for the solution named **Azure Synapse Link for Dataverse**, and then select **Get it now**.

    ![Azure Synapse Link for Dataverse Solution](media/asl-solution.png "Azure Synapse Link for Dataverse Solution")

4. Repeat above steps in the destination environment. You need the **Azure Synapse Link for Dataverse** solution in both the source and destination environments.

## Add an Azure Synapse Link configuration to a solution

1. Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), select the source environment, and then on the left navigation pane, select **Solutions**.

2. Select **New solution**. Provide a **Name**, **Publisher**, and **Version Number**.  

3. Open the solution you created in the previous step, select **Add existing** > **More** > **Azure Synapse Link config**.

    ![Add Configuration](media/asl-add-config.png "Add Configuration")

4. Select the link configurations that you want, and then select **Add**.

5. In the **Solutions** area, select the solution, and then on the command bar, select **Export**.

    ![Export solution](media/export-solution.png "Export solution")

6. In the **Before you export** pane, select **Publish** to publish all changes before you export, and then select **Next**.

> [!NOTE]
> Once the solution has been configured and exported, it is not updated automatically. Any updates you make to the configuration will require you to re-export and re-import the solution.

## Import the solution that contains the Azure Synapse Link configuration

1. In the destination environment, import the solution under the **Solutions** tab.

2. In the destination environment, import the solution under the **Dataverse** > **Azure Synapse Link** tab.

    ![Import solution](media/import-solution.png "Import solution")

## Verify the Azure Synapse Link configuration

In the destination environment, verify that you can see the new Azure Synapse Link from the solution addition to the list of links.

![Imported Azure Synapse Link for Dataverse tables.](media/imported-export-entities.png "Imported Azure Synapse Link for Dataverse tables")

### See also

[Azure Synapse Link for Dataverse](./export-to-data-lake.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
