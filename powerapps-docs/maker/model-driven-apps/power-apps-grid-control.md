---
title: "Power Apps grid control | MicrosoftDocs"
description: "A control for use with Power Apps that lets users edit records directly from a view or sub-grid"
ms.custom: ""
ms.date: 10/04/2021
ms.reviewer: "matp"
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "overview"
applies_to: 
  - "powerapps"
author: "Mattp123"
ms.subservice: mda-maker
ms.author: "matp"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Power Apps grid control (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)] More information: [Previews for portals, model-driven apps, and app management](/power-platform/admin/preview-environments#portals-model-driven-apps-and-app-management)

The Power Apps grid control lets app users make rich in-line editing directly from views and sub-grids. The control supports the latest Microsoft Accessibility Standards and is built to be performant and easily extensible for the future. The Power Apps grid control also aligns with the latest Microsoft design guidance for fonts, sizing, and styling. The Power Apps grid control will eventually replace the editable grid control in both model-driven and canvas apps.

## Configure the Power Apps grid control for table views

When you configure the grid control for a table, *all* views for that table will display using the Power Apps grid control.

1. Open [solution explorer](powerapps/maker/model-driven-apps/advanced-navigation.md#solution-explorer).
1. Expand **Entities**, in the list of tables, open the table you want, select the **Controls** tab, and then select **Add Control**.
1. In the **Add Control** dialog box, select **Power Apps Grid**, and then select **Add**.
   :::image type="content" source="media/add-power-apps-grid-control.png" alt-text="Add Power Apps grid control to a table":::
1. In the **Power Apps Grid** row that's added, select the app types you want to apply the grid to. This makes the control the default control for the selected clients.
   :::image type="content" source="media/configure-power-apps-grid-control.png" alt-text="Select the client types where you want to use the control":::
1. To display an alphabetic list in views or subgrids, select the pencil icon in the **Jump bar** row, and then under **Bind to static options**, select **Enable** in the dropdown list. By default the jump bar is disabled. Below is a screenshot of the jump bar enabled for the contact table in a model-driven app.
   :::image type="content" source="media/jump-bar-in-view.png" alt-text="Jump bar enabled and displayed in the view for an app":::
1. To save your changes, select **Save** on the command bar. When you're ready to make the changes available to app users, select **Publish** on the command bar.

## Configure a sub-grid to use the Power Apps grid control

1. Open [solution explorer](powerapps/maker/model-driven-apps/advanced-navigation.md#solution-explorer).
1. Open the form that contains the sub-grid.
1. Select the sub-grid where you want configure the Power Apps grid control, and then select **Change Properties** on the command bar.
1. In the **Set Properties** dialog box, select the **Controls** tab, select **Add Control**, and then select **Power Apps Grid**. 
1. To continue with configuring and publishing the control, see [Configure the Power Apps grid control for table views](#configure-the-power-apps-grid-control-for-table-views).

### See also

[Use grid filters](../../user/grid-filters.md)