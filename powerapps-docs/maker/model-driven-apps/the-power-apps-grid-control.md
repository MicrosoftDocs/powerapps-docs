---
title: "Power Apps grid control in Power Apps"
description: "A control for use with Power Apps that lets users view, open, and edit records from a view or subgrid in model-driven apps."
ms.custom: ""
ms.date: 05/12/2025
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

The Power Apps grid control represents the next evolution of the classic Power Apps read-only grid control, allowing users to view, open, and edit records from views and subgrids. In addition to inline editing, the control provides a number of other powerful capabilities including infinite scrolling, nested grids, grouping, aggregation, and is customizable. Like the read-only grid control, this control supports the latest Microsoft accessibility standards and aligns with the latest Microsoft design guidance. This control will eventually replace all read-only and editable grids in model-driven apps.

- **Infinite scroll**: A modern data browsing experience in which users can scroll indefinitely through data until they find the records they're interested in. Since there are no page boundaries, users can select more rows at once (up to 1,000 rows) to facilitate taking action against a set of records or perform bulk editing.
- **Inline editing**: This singular grid control can be utilized for read-only or edit scenarios.
- **Nested grids**: Makers can configure the grid to show surface related records. When configured, users can expand a row to see a subgrid of related records. Multiple rows in the grid can be expanded simultaneously. This is an improvement over older grid experiences.  
- **Grouping**: Users can organize tabular data in interesting ways by grouping the data based on a single column. Each group is collapsed initially, but users can expand and collapse the groups as desired. Grouping is exposed on most data types with the notable exception of lookup columns. Grouping isn't supported when paging on the grid is enabled.
- **Aggregation**: Users can surface meaningful insights from their data by enabling aggregation on one or more numeric columns in a grid. For each column, users can choose to see the total, minimum value, maximum value, or average of values from that column. If grouping is applied, this aggregate value is also displayed for each group.
- **Customizable**: Makers have the ability to modify various experiences inside the grid component. 

:::image type="content" source="media/power-apps-grid-control-editing.gif" alt-text="Editing data with the Power Apps grid control":::

## Add the Power Apps grid control using form designer
1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), select **Solutions** on the left navigation pane, and then open the solution you want. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Select the **Table** within the solution, and then select the **Forms** area. Open the **Main Form** that contains the subgrid for editing.
1. In the form designer, select **Components** on the left navigation pane, expand **Grid**, and then select **Power Apps grid control**. **. If the component isn't listed, select the subgrid on the form canvas, expand **Components** on the right property pane, select **+ Component**, and then select **Power Apps grid control** from the **Add component** page.
1. [Configure the Power Apps grid control](#configure-the-power-apps-grid-control)
1. Select **Done**.
1. **Save and publish** the form to save and make it available to app users.

## Add the Power Apps grid control to views using classic solution explorer

When you configure the Power Apps grid control for a table, all views for that table display using that grid.

1. Open the [solution explorer](advanced-navigation.md#solution-explorer).
1. Expand **Entities**. Browse to the table you want and select it. On the **Controls** tab, select **Add control**.
1. In the **Add control** dialog box, select **Power Apps grid control**, and then select **Add**.
    :::image type="content" source="media/add-the-power-apps-grid-control.png" alt-text="Add Power Apps grid control to a table":::
1. [Configure the Power Apps grid control](#configure-the-power-apps-grid-control)
1. After configuring the Power Apps grid control to meet your needs, select Save on the command bar to save your changes. When you're ready to make the changes available to app users, select Publish on the command bar.

## Add the Power Apps grid control to a subgrid using classic solution explorer

1. Open the [solution explorer](advanced-navigation.md#solution-explorer).
1. Expand **Entities**, expand the table you want, and then select **Forms**.
1. Open the form where you want to add the Power Apps grid control.
1. On the form canvas, select the subgrid where you want to configure this grid (usually located on a form section), and then select **Change properties** on the command bar.
1. In the **Set properties** dialog box, select the **Controls** tab, select **Add control**, and then select **Power Apps grid control**.
1. To configure the control, go to [Configure the Power Apps grid control](#configure-the-power-apps-grid-control).
1. Select **OK** to close the **Set properties** dialog box.
1. To save and make available to apps, select **Save**, and then select **Publish**.
1. After configuring the Power Apps grid control to meet your needs, select **Save** on the command bar to save your changes. When you're ready to make the changes available to app users, select **Publish** on the command bar.

## Configure the Power Apps grid control

1.	Select the **Power Apps grid control** components. More infomation: [Configure components on a form](add-move-configure-or-delete-components-on-form#configure-components-on-a-form)
1.	There are several properties included with the control to let you tailor the grid experience for that table. To modify any of these properties, select **Edit** in the corresponding row, and then change the value using the dropdown list under **Bind to static options**. 
    - The **Enable editing** property determines whether the grid is read-only or editable. The default value is **No**. Select **Yes** to make the grid editable. Editable grids have subtle visual differences to read-only grids including boolean columns showing toggle switches and dropdown and date fields displaying chevrons and date picker icons on hover or focus.
    - The **Enable filtering** property determines if filtering options are available to users in the grid column header dropdowns. The default value is **Yes**.
    - The **Enable sorting** property determines if sorting options are available to users in the grid column header dropdowns. The default value is **Yes**.
    - The **Enable grouping** property determines if grouping options are available to users in the grid column header dropdowns. The default value is **No**.
    - The **Enable aggregation** property determines if aggregation options (sum, minimum, maximum, average) are available to users in numeric columns of the grid. The default value is **No**.
    - The **Allow column reordering** property controls whether users can reorder columns from directly within the grid. This includes drag-and-drop of the column headers or using **Move left** and **Move right** actions from the column header dropdowns. The default value is **No**.
    - The **Enable multiselect** property determines whether users can select multiple rows in the grid simultaneously or just a single row. The default value is **Yes**.
    - The **Allow range selection** property controls whether users can select a subset of the grid and copy that data to another application like Excel. The default value is **Yes**.
    - The **Enable jump bar** property can be used to display an alphabetic list at the bottom of views or subgrids. The default value is **No**. Below is a screenshot of the jump bar enabled for the contact table in a model-driven app. 
       :::image type="content" source="media/jump-bar-in-view.png" alt-text="Jump bar enabled and displayed in the view for an app":::
    - The **Enable pagination** property can be used to decide between modern data browsing (infinite scroll) and paging buttons. The default value is **No**. Select **Yes** to disable infinite scrolling and surface paging buttons. Note that the **Select all** action isn't available currently when using infinite scroll, but users can still perform range selection
    - The **Enable OptionSet colors** property can be used to increase the visual appeal of choice columns by showing each value with its configured background color. The default value is **No**. Be sure to verify the configured color for each choice column to ensure readability and accessibility before enabling this property for a table.
    - The **Show row status icons** property controls whether users see status icons (invalid, save in progress, saving, etc.) at the beginning of a grid row during the editing experience. The default value is **Yes**.
    - The **Show data type icons** property determines whether column headers display an icon corresponding to the data type next to the column name. The default value is **No**.
    - The **Navigation types allowed** property determines which lookup controls in the grid render as hyperlinks. The default value is **All**. Select **Primary only** to suppress hyperlinks on all lookup fields except the primary column for the selected entity, or **None** to suppress all hyperlinks in the grid.
    - The **Reflow behavior** property determines whether the grid components render always in a tabular fashion (**Grid only**), always as a list (**List only**), or switches between tabular and list depending on the available width (**Reflow**). The default value is **Reflow**.
    - The **Child  items** property is used to configure the nested grid capability, which allows users to expand rows to see related records in a subgrid. To set this up, you specify the **Entity** where the related records come from and the **View** that defines the filters, sorts, and columns to show in the subgrid. The default value is no nested grid configured.
        - The **Child items parent ID** property is also needed to configure a nested grid and specifies the field (and relationship) to use to link the parent and child entities together.
        - The **Disable editing in child items grid** property provides some control over the editability of the nested grid. By default, the nested grid inherits the editability of the parent grid, but this property can be used to suppress editing in the nested grid when the parent grid is editable. The default value is **No**.  
    -  The **Customizer control** property allows the maker to link to a single customizer Power Apps component framework control with definitions for changing the visuals or interactions for one or more columns in the grid or the empty grid visual.


## Customization

For information about how to customize the Power Apps grid control using extensibility APIs, go to [Customize the editable grid control](/power-apps/developer/component-framework/customize-editable-grid-control).

## Known issues and limitations

### Limitations with card form lists

When a view or subgrid is narrow it changes into a card list format that is better for small screens, such as mobile devices. The Power Apps grid control displays the following behavior in a card list:

- Sort isn't currently available in a card list view. To work around this limitation, create views with the sort order you want.
- **Select all** and **Clear all** aren't available in a card list view.
- The jump bar isn't available in a card list view. To work around this limitation, select **Search** to filter records. Type the desired letter, and then press Enter.
- Images on a record in the list don't display in a card list view. This includes table icons, web resource images, custom images, and conditional images. The only image displayed for a record in the list are the initials of the record.
- There are no icons for context menu commands in a card list view.
- When there are no records, some lists have a prompt to create a new item. This button isn't displayed in a card list view that uses the Power Apps read-only grid control.

#### The list view doesn’t display custom cards for the table

To work around this, you can display a custom card by configuring the table to use the card form of the legacy read-only grid control.

1. Go to Power Apps (make.powerapps.com) > **Settings** > **Advanced Settings** > **Settings** > **Customizations** > **Customize the System** > expand **Entities** > select the table you want to customize > **Controls** tab > **Add Control**.
1. Select **Read Only Grid**, and then select **Add**. Choose to display that grid on one or more client form factors.

   :::image type="content" source="media/change-card-form-readonlygrid.png" alt-text="Change card form for the read only grid control":::

1. Select **Configure property** (pencil icon) for the **Card Form** property, and select the custom card form from the drop-down list.
1. Select **OK**, and then **Publish** the customization.

### UI limitations and differences from the read-only grid control

- The grid doesn't currently support legacy theme customizations.
- Cells with no data are blank instead of displaying three dashes **---**.
- The owner column doesn't show online status and a people card for the user.
- Columns lookup filters, when using the 'Equals' or 'Does not equal' operator, only show lookup options available within the current set of applied filters.
  - For example, if the contact table has users 'Person A', 'Person B', and 'Person C' but account table data only has rows referencing 'Person B' and 'Person C', then the column filter lookup for the contact column in the account grid only shows the options for 'Person B' and 'Person C'. This is a change in behavior from previous grids.

### Known issues

- Column grouping isn't supported when paging on the grid is enabled.
- If the dataset displayed in the grid contains duplicate rows, the duplicates might not display in the grid. This can lead to the reported record count showing more records than are actually in the grid, or more records appearing when exporting the data to Excel or viewing the data in legacy Advanced Find. This behavior applies to all grid controls, not just the Power Apps grid control.
- If a user has read-only privileges to the main list and then navigates through a form to a subgrid representing an entity to which they have write privileges, the subgrid still won't allow the user to make changes as access is determined first by the main entity, then by the related entity.

### Related articles

[Explore data in a view on a grid page](../../user/grid-filters.md)
