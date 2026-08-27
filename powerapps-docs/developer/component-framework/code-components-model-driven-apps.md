---
title: Code Components for Model-Driven Apps
description: Learn how to create, add, and update code components for model-driven apps with Power Apps component framework. Get started with the development process.
author: anuitz
ms.author: anuitz
ms.date: 08/26/2026
ms.reviewer: jdaly
ms.topic: article
ms.subservice: pcf
contributors:
 - JimDaly
---

# Code components for model-driven apps

This article explains how professional developers can create, debug, import, and add code components for model-driven apps by using Power Apps component framework and [Microsoft Power Platform CLI](get-powerapps-cli.md). These components help extend visualizations in model-driven apps. You can add code components to columns, grids, and sub grids in model-driven apps. 

> [!IMPORTANT]
> Power Apps component framework is enabled for model-driven apps by default. See [Code components for canvas apps](component-framework-for-canvas-apps.md) to learn how to enable Power Apps component framework for canvas apps.

## Implement code components

Before you start creating code components, make sure that you have installed all the [prerequisites](create-custom-controls-using-pcf.md#prerequisites) that are required to develop components using Power Apps component framework.

The [create your first code component](implementing-controls-using-typescript.md) article demonstrates the step-by-step process to create code components.

## Add code components to model-driven apps

To add code components to a column or a table in model-driven apps, see [Add code components to model-driven apps](add-custom-controls-to-a-field-or-entity.md).

:::image type="content" source="../../maker/model-driven-apps/media/add-slider.PNG" alt-text="Screenshot of the Add Control dialog for a linear slider code component.":::

:::image type="content" source="media/add-dataset-component.png" alt-text="Screenshot of the Data Set Grid code component configuration.":::

## Update existing code components

Whenever you update the code components and want to see the changes in runtime, you need to bump the version property in the manifest file. It is recommended to always bump the version of the component whenever you make changes.

## See also

[Power Apps component framework overview](overview.md)<br/>
[Create your first code component](implementing-controls-using-typescript.md)<br/>
[Learn Power Apps component framework](/training/paths/use-power-apps-component-framework)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
