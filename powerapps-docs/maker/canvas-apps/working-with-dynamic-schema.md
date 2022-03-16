---
title: Working with dynamic schema data sources in Power Apps (experimental)
description: Learn about how to work with data sources that use dynamic schema in service calls when working with canvas apps.
author: lancedMicrosoft
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 03/15/2022
ms.subservice: canvas-maker
ms.author: tapanm
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - lancedMicrosoft
---

# Working with dynamic schema data sources in Power Apps (experimental)

[This article is pre-release documentation and is subject to change.]

> [!IMPORTANT]
> - This is an experimental feature.
> - Experimental features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.

Power Apps generally uses a fixed set of fields returned by the data source. However, some data sources may return a different set of fields depending on the service call parameter values. Such service calls are considered to have dynamic schema since fields in the service call response change dynamically depending on how the service is called.

For example, Azure DevOps work items may use custom fields. Since custom fields aren't available for all work items, some calls to Azure DevOps are considered dynamic. In such instances, you'll potentially get a different set of fields depending on the Azure DevOps organization that contains such [custom fields](/azure/devops/organizations/settings/work/add-custom-field).

> [!NOTE]
> This article uses the Azure DevOps connector to explain the use of dynamic schema in Power Apps. To create a canvas app that connects to Azure DevOps, see [Connect to Azure DevOps from Power Apps](connections/azure-devops.md). To configure your Azure DevOps project with a custom field, see [create custom fields](/azure/devops/organizations/settings/work/add-custom-field).

With the **Dynamic schema** experimental feature, you can now **capture schema** for such data sources locking a particular call with the set of fields returned. And then, use the fields from such dynamic schema while working with data, instead of the default schema available with the default service calls.

## Enable dynamic schema

To enable **Dynamic schema** feature, go to **Settings** > **Upcoming features** > **Experimental** > **Dynamic schema** while keeping your canvas app open for editing.

:::image type="content" source="media/working-with-dynamic-schema/setting.png" alt-text="Turn Dynamic schema setting On.":::

Close the current Power Apps Studio session, and reopen the app for editing. You'll see a warning icon when the formula uses service calls that support dynamic schema. When you expand the formula bar, you'll see a new button named **Capture schema**.

:::image type="content" source="media/working-with-dynamic-schema/capture-schema.png" alt-text="Option to capture schema and a warning message for dynamic schema service calls.":::

## Use dynamic schema

Selecting **Capture schema** retrieves the fields that support the service call with schema as defined at the data source specific to the service call.

For example, the following image shows a list of all fields retrieved when connecting to Azure DevOps project. Unless dynamic schema is "captured", the list of fields remains as available by default for Azure DevOps work items.

:::image type="content" source="media/working-with-dynamic-schema/field-description.png" alt-text="List of all fields returned by the service call by default that doesn't include Fabrikam ID.":::

Consider a project in Azure DevOps that uses custom field&mdash;for example, **Fabrikam ID**:

:::image type="content" source="media/working-with-dynamic-schema/field-fabrikamID.png" alt-text="Example of Fabrikam ID as a custom field in Azure DevOps.":::

You'll need to capture the schema for the service call to use this custom field. To capture schema, select and expand the formula that shows the warning message, and then, select **Capture schema**.

Once the dynamic schema is captured, you'll be able to use the custom field **Fabrikam ID** for the selected field in your canvas app.

:::image type="content" source="media/working-with-dynamic-schema/captured-schema.png" alt-text="Example of Fabrikam ID captured through dynamic schema feature.":::

You can also see the updated schema available for use for the service call of the gallery that was used to capture the schema. To see this schema detail, move the cursor at the end of the formula, and select the drop-down button below the formula bar to expand the result set.

:::image type="content" source="media/working-with-dynamic-schema/captured-schema-formula-bar.png" alt-text="Example of captured schema with Fabrikam ID listed in the formula bar.":::

### See also

[Connect to Azure DevOps from Power Apps](connections/azure-devops.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]