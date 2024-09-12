---
title: Power BI content management in Power Apps solutions (preview)
description: Learn how the Power BI/Power Apps solutions integration makes it possible to include Power BI reports and datasets in your apps and manage them in your ALM lifecycle process.
author: paulinbar
contributors: teddyberco
ms.component: cds
ms.topic: how-to
ms.date: 09/11/2024
ms.subservice: dataverse-maker
ms.author: painbar
search.audienceType: 
  - maker
---
# Power BI content management in Power Apps solutions (preview)

> [!IMPORTANT]
>
> - This feature reached retirement on July 31, 2024 and is no longer available. We recommend removing all Power BI report and dataset components from existing solutions and use [Power BI embedded system dashboard](./create-edit-powerbi-embedded-page.md) instead.
> - Using the Power BI embedded system dashboard doesn't deploy Power BI reports and datasets in a Power BI workspace. Power Apps will no longer create a dedicated environment aware workspace in Power BI. Additionally, embedding the Power BI embedded system dashboard in forms, similar to the feature described in this article, isn't possible.

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

The Power BI in Power Platform solution integration enables you, as an app maker, to add Power BI reports and datasets as Microsoft Dataverse components in Power Platform solutions. When you add a Power BI report or dataset to a solution, it stays connected as the solution is deployed across environments and tenants, and can be seamlessly managed as part of your application lifecycle management (ALM) process across environments and tenants.

This article presents high-level descriptions of some of the main features of the Power BI/Power App solutions integration. If you just want to get started, go to [Create Power BI report and dataset components](./create-edit-powerbi-report-dataset-components.md).

> [!IMPORTANT]
> - This is a preview feature.
> - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)]

## Add Power BI components to solutions

Working in Power Apps, you add Power BI report and dataset components from Power BI workspaces just like any other Dataverse component. When you add a Power BI report, any dependency between the report and the relevant dataset will be detected, and the dependent dataset will be added as a component automatically. Once the report or dataset is added to the solution, the artifacts will be exported and uploaded to Dataverse, and a new dedicated workspace in Power BI will automatically be created to store the artifacts. This dedicated Power BI workspace inherits privileges from several predefined roles (see [Permission sync between Power Apps environment and Power BI workspace](../model-driven-apps/customize-manage-powerbi-components.md#permission-sync-between-power-apps-environment-and-power-bi-workspace), giving the users in these roles permission in the workspace, thus enabling coauthoring between Power Apps and Power BI. This process ensures that your Power BI reports and datasets can be embedded as a system dashboard or inside forms and will survive deployment across environments and tenants.

## Control Power BI dataset parameters from Power Apps

Once you've added Power BI components to a solution, you can configure connectivity across environments using dataset parameters (see [Configure Power BI parameters](./create-edit-powerbi-report-dataset-components.md#configure-power-bi-parameters)). Every Power BI dataset that includes a dynamic query parameter can be controlled from Power Apps solutions by defining its value with an environment variable, an environment domain, or custom text. This gives you flexibility in controlling data sources on deployment between your dev, test, and production environments. Datasets that connect to Dataverse and don't have existing parameters can automatically be configured to connect to the target environment domain when you deploy.

## Power BI components in the Power Apps solutions package
 
When you export your solution with Power BI components, the Power BI artifacts are stored in the solution format rather than in *.pbix* files. In the export zip file, there will be a specific package for each Power BI dataset and report in the solution. This means that when you store, version, or deploy a Power Apps solution, the same action will apply to the embedded Power BI reports and datasets.

## Solution Customization
 
You can fully [customize Power BI components](./customize-manage-powerbi-components.md#customization-with-power-bi-components) to fit your exact needs. When you deploy a managed solution, any customizations you make are saved as an additional, unmanaged layer. This enables you to take a managed solution from your own organization, a vendor, or even from AppSource, and adapt it to suit your own analytics needs.

### See also

* [Create Power BI report and dataset components](./create-edit-powerbi-report-dataset-components.md)
* [Customize and manage Power BI components](../model-driven-apps/customize-manage-powerbi-components.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
