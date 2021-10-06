---
title: "Power Apps grid control | MicrosoftDocs"
description: "A control for use with Power Apps that lets users view and open records from a view or subgrid"
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

The Power Apps grid control lets users view and open records from views and subgrids. The control supports the latest Microsoft accessibility standards and is built to be performant and easily extensible for the future. The Power Apps grid control also aligns with the latest Microsoft design guidance for fonts, sizing, and styling. The Power Apps grid control will eventually replace both the legacy read-only grid and editable grid controls in both model-driven and canvas apps.

> [!NOTE]
> Currently, the Power Apps grid control provides read-only views and subgrids.

## Add the Power Apps grid control to views for a table

When you configure the Power Apps grid control for a table, *all* views for that table will display using the Power Apps grid control.

1. Open [solution explorer](advanced-navigation.md#solution-explorer).
1. Expand **Entities**, in the list of tables, open the table you want, select the **Controls** tab, and then select **Add Control**.
1. In the **Add Control** dialog box, select **Power Apps Grid**, and then select **Add**.
   :::image type="content" source="media/add-power-apps-grid-control.png" alt-text="Add Power Apps grid control to a table":::

### Configure the Power Apps grid control

1. In the **Power Apps Grid** row that's added, select the app types you want to apply the grid to. This makes the control the default control for the selected clients.
   :::image type="content" source="media/configure-power-apps-grid-control.png" alt-text="Select the client types where you want to use the control":::
1. By default the jump bar is disabled. To display an alphabetic list at the bottom of views or subgrids (the jump bar), select the pencil icon in the **Jump bar** row. Under **Bind to static options**, select **Enable** in the dropdown list. Below is a screenshot of the jump bar enabled for the contact table in a model-driven app.
   :::image type="content" source="media/jump-bar-in-view.png" alt-text="Jump bar enabled and displayed in the view for an app":::
1. To save your changes, select **Save** on the command bar. When you're ready to make the changes available to app users, select **Publish** on the command bar.

## Add the Power Apps grid control to a subgrid

1. Open [solution explorer](advanced-navigation.md#solution-explorer).
1. Open the form that contains the subgrid.
1. Select the subgrid where you want to configure the Power Apps grid control, and then select **Change Properties** on the command bar.
1. In the **Set Properties** dialog box, select the **Controls** tab, select **Add Control**, and then select **Power Apps Grid**. 
1. To continue with configuring and publishing the control, see [Configure the Power Apps grid control](#configure-the-power-apps-grid-control).

## Known issues and limitations

### Limitations with card form lists

When a view or subgrid is narrow it changes into a card list format that is better for small screens, such as mobile devices. The Power Apps grid control displays the following behavior in a card list:

- Sort is not currently available in a card list view. To work around, create views with the sort order you want.
- Select all and clear all isn't available in a card list view.
- The jump bar isn't available in a card list view. To work around, select **Search** to filter records. Type the desired letter, and then press Enter.
- Images on a record in the list don't display in a card list view. This includes table icons, web resource images, custom images, and conditional images. The only image displayed for a record in the list are the initials of the record.
- There are no icons for context menu commands in a card list view.
- When there are no records, some lists have a prompt to create a new item. This button is not displayed in a card list view that uses the Power Apps grid control.

#### The list view doesn’t display custom cards for the table

To work around, you can display a custom card by configuring the table to use the card form of the legacy read-only grid control.
1. Go to Power Apps (make.powerapps.com) > **Settings** > **Advanced Settings** > **Settings** > **Customizations** > **Customize the System** > expand **Entities** > select the entity you want to customize > **Controls** tab > **Add Control**.
1. Select **Read Only Grid**, and then select **Add**. Choose to display that grid on one or more client form factors.

   :::image type="content" source="media/change-card-form-readonlygrid.png" alt-text="Change card form for the read only grid control":::

1. Select **Configure property** (pencil icon) for the **Card Form** property, and select the custom card form from the drop-down list.
1. Select **OK**, and then **Publish** the customization.

### UI limitations and differences from the read-only grid control

- Users can’t right-click links in the Power Apps grid to get browser link options like **Open link in new tab**. To work around this limitation:
   - Option 1: Ctrl+click the link to open in a new tab, and then Shift+click to open in a new window.
   - Option 2: Duplicate the browser tab, then navigate to the record.
- Users can’t drag the mouse across multiple records to select a range of records. To work around this limitation, use Shift+click to select a range of records.
- Cells with no data are blank instead of displaying three dashes **---**.
- The owner column does not show online status and a people card for the user.
- Filtering a column using the column **Filter By** drop-down list doesn't change the underlying view. 
  :::image type="content" source="media/view-filter-by.png" alt-text="Filter By drop down list in a view":::
   To work around this limitation, use the **Open advanced filtering panel** to change the actual view.
   :::image type="content" source="media/advanced-filter-panel.png" alt-text="Select the Open advanced filtering panel feature":::
   More information: [See the current view definition)](../../user/grid-filters-advanced?branch=matp-2451824#see-the-current-view-definition)

## Disable the Power Apps grid control

The Power Apps grid control can be disabled in different ways:

- For the entire environment by setting the `FCB.PcfDatasetGrid` value to false.
- For a particular table by customizing the control for the table and selecting the read-only grid control. To do this, go to **Settings** > **Advanced Settings** > **Settings** > **Customizations** > **Customize the System** > expand **Entities** > select the entity you want to customize > **Controls** tab > **Add Control**. Select **Read Only Grid**. Choose to display that grid on one or more client form factors. Select **Save** on the command bar, and then **Publish** the customization.

## Enable the jump bar by default

You can turn on the jump bar by default for all grids that are using the Power Apps grid control in the environment by setting the `FCB.PcfDatasetGridShowJumpBar` value to true. View and grid-level customizations to disable the jump bar will continue to work with this feature control enabled.

### See also

[Use the column options in a view or grid (preview)](../../user/grid-filters.md#use-the-column-options-in-a-view-or-grid-preview)