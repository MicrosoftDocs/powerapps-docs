---
title: "Make model-driven app views and grids editable using the editable grid control"
description: "Learn how to use the editable grid control to make views and grids editable in Power Apps."
ms.custom: ""
ms.date: 09/19/2024
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
ms.assetid: cefbc0c2-769b-4230-ab5a-b28a84630a42
caps.latest.revision: 8
author: "Mattp123"
ms.subservice: mda-maker
ms.author: "matp"
search.audienceType: 
  - maker
---
# Make model-driven app views editable using the editable grid control

By default, users can't enter data directly using the read-only view control for views and subgrids on forms. Users select the row in the grid to open a form, edit the data, and then save, which requires multiple steps. With editable grids, users can do rich in-line editing directly from views and subgrids whether they're using a web app or tablet. This editing experience isn't available on phones.
  
 ![Editable grid example on a model-driven app form.](media/editable-grid-example.png "Editable grid example on a model-driven app form")  
  
When editable grids are enabled through the editable grid control, users can edit the data inside most types of columns, including basic lookup columns and choices columns. Editable grids avoid the need to open a form.

## Add an editable grid to a main form

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), select **Solutions** on the left navigation pane, and then open the solution you want. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Select the **Table** within the solution, and then select the **Forms** area. Open the **Main Form** that contains the subgrid for editing.
1. In the form designer, select **Components** on the left navigation pane, expand **Grid**, and then select **Editable Grid**.
1. Select the following for the grid.

   |Area  |Property  |Description  |
   |---------|---------|---------|
   |Grid     | Table   | Select the table you want that will display records in the grid.   |
   |Grid     | View    | Select the table view you want displayed in the grid.     |
   | Grid   |  Lookup view   | Select to add a lookup. Select the lookup column to add (for example, select **Primary Contact**) and in the **Default view** list, select the data source for the lookup column.    |
   |Subgrid     | Table    |  If you have a nested grid select the **Table** and **View** for the nested grid (phones and tablets only).     |
   |Subgrid     | Subgrid parent id   | For the subgrid parent id, select the relationship for the tables. For example, the subgrid parent id table column connects the **Account** and **Contact** tables.         |
   |Group by     |  Enable or Disable   | If you don't want to allow the user to group data by any column in the view (you want to save space, for example), in the **Group by** value select **Disable**.        |
   |Layout  |  Vertical or Horizontal   |  Determines how the grid displays on the form.    |
   |Allow filtering     | Enable or Disable   | Disable if you don't want users the ability to filter the grid by keyword.     |
   |Hide nested grid column header  | Show column header or Hide column header    | Determines whether the grid header displays.   |
   |Alphanumeric filter bar | Show the alphanumeric filter bar or Hide the alphanumeric filter bar       |  Determines whether the filter bar located at the bottom of the grid is displayed.       |
   |Show component on     |  Web, Mobile, Tablet   | Determines the client type that can use the editable grid control.    |
1. Select **Done**.
1. **Save and publish** the form to save and make it available to app users.

For information about editing the properties of an existing subgrid on a form, go to [Configure a subgrid component](form-designer-add-configure-subgrid.md#configure-a-subgrid-component).

## Make main grids editable for views using the classic solution explorer

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), select **Solutions** on the left navigation pane, and then open the solution you want. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. On the toolbar select **...** > **Switch to classic**. This opens solution explorer in a new browser window.
1. In the **Entities** list (these represent Dataverse tables), open the table you want, select the **Controls** tab, and then select **Add Control**.  
  
   ![Add Editable Grids custom control.](media/add-editable-grids-custom-control.png "Add Editable Grids custom control")  
  
1. In the **Add Control** dialog box, select **Editable Grid**, and then select **Add**.  
  
1. In the **Editable Grid** row that's added, select the client type you want to apply the grid to, web, phone, and tablet. This makes the editable grid control the default control for the selected client type. Since the control doesn't work with phones, you should select **Web** for desktop app users. At runtime, users are able to toggle between editable grids and read-only grids.

> [!NOTE]
> Since the editing experience is not available on the **Phone** form factor, if this control is configured for phones, you will see a read-only version of the list control.
  
![Editable Grid row with form factor selection.](media/editable-grid-row-wit-factor-selection.png "Editable Grid row with form factor selection")

1. To add a lookup, in the **Editable Grid** area, select **Add Lookup**, and then in the **Configure Property "Add Lookup"** dialog box:  
  
   1. In the **Available Views** list, select the view to add the lookup to (for example, select **My Active Accounts**).  
  
   1. In the **Available Columns** list, select the lookup column to add (for example, select **Primary Contact**).  
  
   1. In the **Default View** list, select the data source for the lookup column.  
  
   1. If you want to limit the rows displayed, select the **Only show rows where** check box, and then select your criteria from the list, and then select **OK**.  
  
       ![Add lookup in Editable Grid control.](media/add-lookup-in-editable-grid-control.png "Add lookup in Editable Grid control")  

1. If you have a nested grid, select the pencil button for **Nested grid view**, and then select the table and view for the nested grid. For the **Nested grid parent ID** select the relationship for the tables. For example, the **ParentAccountID** column connects the **Account** and **Contact** tables.  
  
   > [!NOTE]
   >  Nested grids are only available for phones and tablets, not the web.  
  
1. If you don't want to allow the user to group data by any column in the view (you want to save space, for example), in the **Group by Column** row, select the pencil button, and then in the **Configure Property "Group by Column"** dialog box, select **Disabled**, and then select **OK**.  
  
   > [!TIP]
   >  This is mostly useful for sub-grids on forms.  
  
1. If you want to add JavaScript events, select the **Events** tab, and then select the appropriate tables, columns, and events. More information: [Developer Documentation: Use editable grids](../../developer/model-driven-apps/use-editable-grids.md)
  
   ![Add events in Editable Grid control.](media/add-events-in-editable-grid-control.png "Add events in Editable Grid control")  
  
1. To save your changes, select **Save** on the action bar.  
  
1. When you're ready to make changes available to your team, select **Publish** on the action bar.  
  
1. To test your changes, go to the view you specified in the previous step, and then make some in-line editing changes.  
  
## Make a subgrid on a form editable using classic solution explorer

> [!NOTE]
> To save an editable grid change within a sub-grid, the user must explicitly save before navigating out of the form.
  
1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
  
2. Select **Solutions**, and then open the solution you want. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
  
3. Select the **Table** within the solution, and then select the **Forms** area.  Open the **Main Form** that contains the subgrid.

4. On the form designer command bar, select **...** > **Switch to classic**. This action opens a new tab in your browser.
  
5. Select the appropriate control, and then select **Change Properties** on the ribbon.  

    :::image type="content" source="media/editable-subgrid-classic.png" alt-text="Editable subgrid - classic view":::

6. In the **Set Properties** dialog box, select **Controls**.

7. Select **Add Control**, select **Editable Grid**, and then select **Add**.  
  
8. In the **Editable Grid** row that's added, select the client types you want to apply the grid to. This makes the editable grid control the default control for the selected form factor. For most instances, select **Web**.
  
     ![Editable Grid row with form factor selection.](media/editable-grid-row-wit-factor-selection.png "Editable Grid row with form factor selection")

9. Select **Save**, and then select **Publish**.

## Editable grids support
  
- In-line editing of rows at the table or subgrid level (includes custom tables).
  
- System views and personal views.

- Web and mobile clients.
  
- Navigation with a keyboard or mouse.
  
- Grouping and sorting (you can group by/sort rows on the client-side by any column in the current view).
  
- Filtering.
  
- Moving and resizing columns. 
  
- Pagination. 
  
- Lookup configuration.
  
- Calculated columns and rollup columns.
  
- Business rules (Show error message, Set column value, Set business required, Set default value, Lock, or unlock column).
  
- JavaScript events.
  
- Enabling or disabling of cells based on security role.
  
- Users can continue to use search and charts, and can access the action bar as with read-only grids.

## Supported standard tables  

|**Web/tablet/phone**|**Tablet/phone only**|**Web only**|
|---------|---------|---------|
|Account<br /><br /> Appointment<br /><br /> Bookable Resource<br /><br /> Bookable Resource Booking<br /><br /> Bookable Resource Booking Header<br /><br /> Bookable Resource Category<br /><br /> Bookable Resource Category Assn<br /><br /> Bookable Resource Characteristic<br /><br /> Bookable Resource Group<br /><br /> Booking Status<br /><br /> Case<br /><br /> Category<br /><br /> Characteristic<br /><br /> Competitor<br /><br /> Contact<br /><br /> Email<br /><br /> Entitlement<br /><br /> Feedback<br /><br /> Invoice<br /><br /> Knowledge Article<br /><br /> Knowledge Article Views<br /><br /> Knowledge Base Record<br /><br /> Lead<br /><br /> Opportunity<br /><br /> Order<br /><br /> Phone Call<br /><br /> Price List<br /><br /> Product<br /><br /> Queue<br /><br /> Quote<br /><br /> Rating Model<br /><br /> Rating Value<br /><br /> SLA KPI Instance<br /><br /> Social Activity<br /><br /> Social Profile<br /><br /> Sync Error<br /><br /> Task<br /><br /> Team<br /><br /> User|Activity<br /><br /> Attachment<br /><br /> Channel Access Profile Rule Item<br /><br /> Competitor Address<br /><br /> Connection<br /><br /> Connection Role<br /><br /> Email Signature<br /><br /> Email Template<br /><br /> Expired Process<br /><br /> Invoice Product<br /><br /> Knowledge Article Incident<br /><br /> Lead To Opportunity Sales<br /><br /> Process<br /><br /> Mailbox<br /><br /> New Process<br /><br /> Note<br /><br /> Opportunity Product<br /><br /> Opportunity Sales Process<br /><br /> Order Product<br /><br /> Organization<br /><br /> Phone to Case Process<br /><br /> Price List Item<br /><br /> Queue Item<br /><br /> Quote Product<br /><br /> Sharepoint Document<br /><br /> Translation Process|Campaign<br /><br /> Campaign Activity<br /><br /> Campaign Response<br /><br /> Channel Access Profile<br /><br /> Channel Access Profile Rule<br /><br /> Contract<br /><br /> Entitlement Template<br /><br /> External Party<br /><br /> Fax<br /><br /> Letter<br /><br /> Marketing List<br /><br /> Position<br /><br /> Quick Campaign<br /><br /> Recurring Appointment<br /><br /> Sales Literature<br /><br /> SLA|  

## Limitations

### Data types that aren't editable in an editable grid

The following data types aren't editable in editable grids: Customer and Partylist Lookup columns; Composite (address) columns; State/Status columns; Lookup table-related columns (for example, the Account table includes a contact lookup, where the Contact column is editable but the EmailAddress(Contact) column isn't editable). 

### Group by views work on client side only

Grouping behavior works only on the client side and doesn't span pages. Group by is a client only function and works only on one page of data. Group by doesn't show you all options based on your complete data set on the server. Group by shows grouping only on the current page. You can disable the grouping by using the property on custom control configuration. More information: [Make a subgrid on a form editable using classic solution explorer](#make-a-subgrid-on-a-form-editable-using-classic-solution-explorer)

### Inline grid modifications aren't persisted

Changes made to the structure of the editable grid from within the grid, such as column resizing, column reordering, grouping, filtering, and sorting, will be reset the next time the user visits the page. These types of changes aren't saved across sessions or within views.  

### Business rules work only if conditional column is a column on the grid

Business rules on an editable grid are supported only if the conditional column is also a column on the grid. If the column isn't a column the business rules won’t work. Verify that each column referenced in the business rule is also included on the form. Note that business rules on an editable grid don't fire if the editable grid is configured on a dashboard.

### Editable grids don't work on phones

Based on customer feedback, we have removed the editable grid experience from phones. When using an editable grid on a phone, you see a read-only version of the list control.

### Duplicate rows in a dataset might not be displayed in the grid

If the dataset displayed in the grid contains duplicate rows, the duplicates might not display in the grid. This can lead to the reported record count showing more records than are actually in the grid, or more records appearing when exporting the data to Excel or viewing the data in legacy Advanced Find.

## Next steps

[Setting managed properties for views](managed-properties-views.md)

[Keyboard shortcuts for editable grids (views)](../../user/keyboard-shortcuts.md#editable-grids-views)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
