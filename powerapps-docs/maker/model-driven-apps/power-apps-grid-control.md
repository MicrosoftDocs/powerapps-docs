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

## Add the Power Apps grid control to views for a table

When you configure the grid control for a table, *all* views for that table will display using the Power Apps grid control.

1. Open [solution explorer](advanced-navigation.md#solution-explorer).
1. Expand **Entities**, in the list of tables, open the table you want, select the **Controls** tab, and then select **Add Control**.
1. In the **Add Control** dialog box, select **Power Apps Grid**, and then select **Add**.
   :::image type="content" source="media/add-power-apps-grid-control.png" alt-text="Add Power Apps grid control to a table":::

### Configure the Power Apps grid control

1. In the **Power Apps Grid** row that's added, select the app types you want to apply the grid to. This makes the control the default control for the selected clients.
   :::image type="content" source="media/configure-power-apps-grid-control.png" alt-text="Select the client types where you want to use the control":::
1. To display an alphabetic list in views or subgrids, select the pencil icon in the **Jump bar** row, and then under **Bind to static options**, select **Enable** in the dropdown list. By default the jump bar is disabled. Below is a screenshot of the jump bar enabled for the contact table in a model-driven app.
   :::image type="content" source="media/jump-bar-in-view.png" alt-text="Jump bar enabled and displayed in the view for an app":::
1. To save your changes, select **Save** on the command bar. When you're ready to make the changes available to app users, select **Publish** on the command bar.

## Add the Power Apps grid control to a sub-grid

1. Open [solution explorer](advanced-navigation.md#solution-explorer).
1. Open the form that contains the sub-grid.
1. Select the sub-grid where you want configure the Power Apps grid control, and then select **Change Properties** on the command bar.
1. In the **Set Properties** dialog box, select the **Controls** tab, select **Add Control**, and then select **Power Apps Grid**. 
1. To continue with configuring and publishing the control, see [Configure the Power Apps grid control](#configure-the-power-apps-grid-control).

## Known issues and limitations with card form lists

When a view or sub-grid is narrow it changes into a card list format that is better for small screens, such as mobile devices. The Power Apps grid control displays the following behavior in a card list:

- Sort is not currently available in a card list view. To workaround, create views with the sort order you want.
- Select all and clear all isn't available in a card list view.
- The jump bar isn't available in a card list view. To work around, select **Search** to filter records. Type the desired letter, and then press Enter.
- Images on a record in the list don't display in a card list view. This includes table icons, web resource images, custom images, and conditional images. The only image displayed for a record in the list are the initials of the record.
- There are no icons for context menu commands in a card list view.
- When there are no records, some lists have a prompt to create a new item. This button is not displayed in a card list view that uses the Power Apps grid control.

### The list view doesn’t display custom cards for the table

To workaround, you can display a custom card by configuring the table to use the card form of the old grid control. 
1. Power Apps (make.powerapps.com) go to **Settings** > **Advanced Settings** > **Settings** > **Customizations** > **Customize the System** > Expand **Entities** > select the entity you want to customize > **Controls** tab > **Add Control**. 
1. Select **Read Only Grid**, and then select **Add**. Choose to display that grid on one or more client form factors. 
   :::image type="content" source="media/change-card-form-readonlygrid.png" alt-text="Change card form for the read only grid control":::
1. Select **Configure property** (pencil icon) for the **Card Form** property, and select the custom card form from the drop down list.
1. Select **OK**, and then **Publish** the customization.

## Disable the Power Apps grid control

The Power Apps grid control can be disabled in different ways:

- For the entire environment by setting the `FCB.PcfDatasetGrid` value to false.
- For a particular table by customizing the control for the table and selecting the read only grid control. To do this, go to Settings > Advanced Settings > Settings > Customizations > Customize the system > Expand Entities > select the entity you want to customize > Controls tab > Add Control. Select **Read Only Grid**. Choose to display that grid on one or more client form factors. Select **Save** on the command bar, and then **Publish** the customization.


### See also

[Use grid filters](../../user/grid-filters.md)