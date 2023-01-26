---
title: Use drop-down lists with choices from lookup columns in a list created using Microsoft Lists
description: This article explains how to use the drop-down list in your app to show choices from a lookup column in a list created using Microsoft Lists.
author: emcoope-msft

ms.topic: conceptual
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 10/21/2021
ms.subservice: canvas-maker
ms.author: emcoope
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - mduelae
  - navjotm
  - wimcoor
  - emcoope-msft
---
# Use drop-down lists with choices from lookup columns in a list created using Microsoft Lists

In this scenario article, you'll learn how to use a drop-down list with choices from a lookup column in a list.

## Prerequisites

- You must have created an app using SharePoint connector that connects to a list.
- The list should consist of a lookup column with values from another column.

## Scenario details

You can use lookup columns in SharePoint that consume values from other lists or libraries.

When using such columns as a field in a canvas app, you can use a drop-down list with choices.

To use the choices in a drop-down list, you have to use the function [choices](../functions/function-choices.md).

For example, `Choices([@'Vehicle registration'].Vehicle_x0020_type)` uses the list **Vehicle Registration**:

:::image type="content" source="media/scenarios-choice-to-lookup/vehicle-registration-list.png" alt-text="Vehicle registration list.":::

The column **Vehicle type** is a lookup column for the type of the vehicle:

:::image type="content" source="media/scenarios-choice-to-lookup/vehicle-type-lookup.png" alt-text="Vehicle type column.":::

## Example

1. Sign in to [Power Apps](https://make.powerapps.com).

1. [Create](../app-from-sharepoint.md) a new app, or [edit](../edit-app.md) an existing app.

    > [!NOTE]
    > Ensure the app uses a SharePoint connection and connects to a list as described in the prerequisites.

1. Select **+** (insert) from the left pane.

1. Select **Drop down**.

    ![Select Drop down.](./media/scenarios-choice-to-lookup/insert-drop-down.png "Select Drop down")

1. Update the **Items** property with the following formula:

    `Choices([@'Vehicle registration'].Vehicle_x0020_type)`

    Replace **Vehicle registration** with the name of your list and **Vehicle type** with the name of the lookup column in the list.

    ![Choices formula.](./media/scenarios-choice-to-lookup/choices-formula.png "Choices formula")

1. Refresh the data source by selecting the SharePoint data source > ellipsis (**...**) > **Refresh**.

    :::image type="content" source="media/scenarios-choice-to-lookup/refresh-data-source.png" alt-text="Refresh data source.":::

1. Play the app, or press **Alt** on the keyboard and select the drop-down list.

    ![Drop-down choices.](./media/scenarios-choice-to-lookup/drop-down-choices.png "Drop-down choices")

### See also

- [Formula reference](../formula-reference.md) for Power Apps
- [Control reference](../reference-properties.md) for Power Apps

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]