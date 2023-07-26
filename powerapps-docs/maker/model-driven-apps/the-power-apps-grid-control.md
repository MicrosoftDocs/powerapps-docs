---
title: "Power Apps grid control | MicrosoftDocs"
description: "A control for use with Power Apps that lets users view, open, and edit records from a view or subgrid"
ms.custom: ""
ms.date: 07/26/2023
ms.reviewer: "matp"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "overview"
applies_to: 
  - "powerapps"
author: "Jasongre"
ms.subservice: mda-maker
ms.author: "matp"
search.audienceType: 
  - maker
---
# Power Apps grid control 

The Power Apps grid control represents the next evolution of the Power Apps read-only grid control, allowing users to view, open, and edit records from views and subgrids. In addition to inline editing, the control provides other capabilities including a modern data browsing experience via infinite scrolling, allowing users to scroll indefinitely through data until they find the records they're interested in, and an ability to customize the visual appearance of columns for specific needs. Like the read-only grid control, this control supports the latest Microsoft accessibility standards and aligns with the latest Microsoft design guidance. This control will eventually replace all read-only and editable grids in model-driven apps.

:::image type="content" source="media/power-apps-grid-control-editing.gif" alt-text="Editing data with the Power Apps grid control":::

> [!IMPORTANT]
> This feature is generally available with the April 2023 release.

## Add the Power Apps grid control to views for an entity

When you configure the Power Apps grid control for an entity, all views for that entity will display using that grid.

1.	Open the [solution explorer](advanced-navigation.md#solution-explorer).
1.	Expand **Entities**. Browse to the table you want and select it. On the **Controls** tab, select **Add control**.
1.	In the **Add control** dialog box, select **Power Apps grid control**, and then select **Add**.
    :::image type="content" source="media/add-the-power-apps-grid-control.png" alt-text="Add Power Apps grid control to a table":::

## Configure the Power Apps grid control

1.	In the **Power Apps grid control** row, select the app types you want to apply the grid to. This makes the control the default control for the selected clients. 
    :::image type="content" source="media/configure-the-power-apps-grid-control.png" alt-text="Select the client types where you want to use the control":::
1.	There are several properties included with the control to let you tailor the grid experience for that table. To modify any of these properties, select **Edit** in the corresponding row, and then change the value using the dropdown list under **Bind to static options**. 
    - The **Enable editing** property determines whether the grid is read-only or editable. The default value is **No**. Select **Yes** to make the grid editable. Editable grids have subtle visual differences to read-only grids including boolean columns showing toggle switches and dropdown and date fields displaying chevrons and date picker icons on hover or focus.
    - The **Enable filtering** property determines if filtering options are available to users in the grid column header dropdowns. The default value is **Yes**. 
    - The **Allow range selection** property controls whether users can select a subset of the grid and copy that data to another application like Excel. The default value is **Yes**.
    - The **Enable jump bar** property can be used to display an alphabetic list at the bottom of views or subgrids. The default value is **No**. Below is a screenshot of the jump bar enabled for the contact table in a model-driven app. 
       :::image type="content" source="media/jump-bar-in-view.png" alt-text="Jump bar enabled and displayed in the view for an app":::
    - The **Enable pagination** property can be used to decide between modern data browsing (infinite scroll) and paging buttons. The default value is **No**. Select **Yes** to disable infinite scrolling and surface paging buttons. Note that the **Select all** action isn't available currently when using infinite scroll, but users can still perform range selection
    - The **Enable OptionSet colors** property can be used to increase the visual appeal of choice columns by showing each value with its configured background color.  The default value is **No**. Be sure to verify the configured color for each choice column to ensure readability and accessibility before enabling this property for a table.  
    - The **Navigation types allowed** property determines which lookup controls in the grid render as hyperlinks. The default value is **All**. Select **Primary only** to suppress hyperlinks on all lookup fields except the primary column for the selected entity.  
    -  The **Customizer control** property allows the maker to link to a single customizer PCF control with definitions for changing the visuals or interactions for one or more columns in the grid. <!-- More information: [Customizing the Power Apps grid control](tbd) -->

3. After configuring the Power Apps grid control to meet your needs, select **Save** on the command bar to save your changes. When you're ready to make the changes available to app users, select **Publish** on the command bar.
 
## Add the Power Apps grid control to a subgrid

1.	Open the [solution explorer](advanced-navigation.md#solution-explorer).
1.	Open the form that contains the subgrid.
1.	Select the subgrid where you want to configure this grid, and then select **Change properties** on the command bar.
1.	In the **Set properties** dialog box, select the **Controls** tab, select **Add control**, and then select **Power Apps grid control**.
1.	To continue with configuring and publishing the control, see [Configure the Power Apps grid control](#configure-the-power-apps-grid-control).

## Customization

For information about how to customize the Power Apps grid control using extensibility APIs, go to [Customize the editable grid control](/power-apps/developer/component-framework/customize-editable-grid-control).

## Known issues and limitations

### Limitations with card form lists

When a view or subgrid is narrow it changes into a card list format that is better for small screens, such as mobile devices. The Power Apps grid control displays the following behavior in a card list:

-  Sort isn't currently available in a card list view. To work around this limitation, create views with the sort order you want.
-  **Select all** and **Clear all** aren't available in a card list view.
-  The jump bar isn't available in a card list view. To work around this limitation, select **Search** to filter records. Type the desired letter, and then press Enter.
-  Images on a record in the list don't display in a card list view. This includes table icons, web resource images, custom images, and conditional images. The only image displayed for a record in the list are the initials of the record.
-  There are no icons for context menu commands in a card list view.
-  When there are no records, some lists have a prompt to create a new item. This button isn't displayed in a card list view that uses the Power Apps read-only grid control.

#### The list view doesn’t display custom cards for the table

To work around this, you can display a custom card by configuring the table to use the card form of the legacy read-only grid control.
1. Go to Power Apps (make.powerapps.com) > **Settings** > **Advanced Settings** > **Settings** > **Customizations** > **Customize the System** > expand **Entities** > select the table you want to customize > **Controls** tab > **Add Control**.
1. Select **Read Only Grid**, and then select **Add**. Choose to display that grid on one or more client form factors.

   :::image type="content" source="media/change-card-form-readonlygrid.png" alt-text="Change card form for the read only grid control":::

1. Select **Configure property** (pencil icon) for the **Card Form** property, and select the custom card form from the drop-down list.
1. Select **OK**, and then **Publish** the customization.

### UI limitations and differences from the read-only grid control

- The **Select all** option is currently not available when infinite scrolling is enabled. Users should use range selection to quickly select multiple rows. 
- The grid doesn't currently support theme customizations.
- Cells with no data are blank instead of displaying three dashes **---**.
- The owner column doesn't show online status and a people card for the user.

### Known issue

If the dataset displayed in the grid contains duplicate rows, the duplicates might not display in the grid. This can lead to the reported record count showing more records than are actually in the grid, or more records appearing when exporting the data to Excel or viewing the data in legacy Advanced Find. This behavior applies to all grid controls, not just the Power Apps grid control.

### See also

[Explore data in a view on a grid page](../../user/grid-filters.md)
