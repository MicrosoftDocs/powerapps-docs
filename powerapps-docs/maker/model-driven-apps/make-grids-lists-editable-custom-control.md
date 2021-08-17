---
title: "Make model-driven app views and grids (lists) editable by using the Editable Grid custom control with Power Apps | MicrosoftDocs"
description: "Learn how to use the editable grid custom control"
ms.custom: ""
ms.date: 04/09/2020
ms.reviewer: ""
ms.service: powerapps
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
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Make model-driven app views editable using the editable grid control

[!INCLUDE [cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

By default, users can't enter data directly using the read-only view control for views and sub-grids on forms. Users select the row in the grid to open a form, edit the data, and then save, which requires multiple steps. With editable grids, users can do rich in-line editing directly from views and sub-grids whether they're using a web app, tablet, or phone.  
  
 ![Editable grid examples.](media/editable-grid-example.png "Editable grid examples")  
  
 When editable grids are enabled through the Editable Grids control, users can edit most types of columns, including basic Lookup columns and choices.  

**Editable grids support:**
  
-   In-line editing of rows at the table or sub-grid level (includes custom tables)  
  
-   System views and personal views  
  
-   Web and mobile clients  
  
-   Navigation with a keyboard or mouse  
  
-   Grouping and sorting (you can group by/sort rows on the client-side by any column in the current view)  
  
-   Filtering  
  
-   Moving and resizing columns  
  
-   Pagination  
  
-   Saving changes from one session to another for grouping, sorting, filtering, pagination, and moving and resizing columns  
  
-   Lookup configuration  
  
-   Calculated columns and rollup columns  
  
-   Business rules (Show error message, Set column value, Set business required, Set default value, Lock or unlock column)  
  
-   JavaScript events  
  
-   Enabling or disabling of cells based on security role  
  
-   Users can continue to use search and charts, and can access the action bar as with read-only grids  
  
## Make main grids editable  
  
1.  Open [solution explorer](advanced-navigation.md#solution-explorer).  
  
2.  In the **Tables** list, open the appropriate table, select the **Controls** tab, and then select **Add Control**.  
  
     ![Add Editable Grids custom control.](media/add-editable-grids-custom-control.png "Add Editable Grids custom control")  
  
3.  In the **Add Control** dialog box, select **Editable Grid**, and then select **Add**.  
  
4.  In the **Editable Grid** row that's added, select the form factor(s) you want to apply the grid to. This makes the editable grid control the default control for the selected form factor(s).  
  
     ![Editable Grid row with form factor selection.](media/editable-grid-row-wit-factor-selection.png "Editable Grid row with form factor selection")    

   > [!NOTE]
   >  At runtime, users can toggle between editable grids and read-only grids.  
      
5.  To add a lookup, in the **Editable Grid** option group, select **Add Lookup**, and then in the **Configure Property "Add Lookup"** dialog box:  
  
    1.  In the **Available Views** list, select the view to add the lookup to (for example, select **My Active Accounts**).  
  
    2.  In the **Available Columns** list, select the lookup column to add (for example, select **Primary Contact**).  
  
    3.  In the **Default View** list, select the data source for the lookup column.  
  
    4.  If you want to limit the rows displayed, select the **Only show rows where** check box, and then select your criteria from the list, and then select **OK**.  
  
         ![Add lookup in Editable Grid control.](media/add-lookup-in-editable-grid-control.png "Add lookup in Editable Grid control")  
     
6.  If you have a nested grid, select the pencil button for **Nested grid view**, and then select the table and view for the nested grid. For the **Nested grid parent ID** select the relationship for the tables. For example, the ParentAccountID column connects the **Account** and **Contact** tables.  
  
    > [!NOTE]
    >  Nested grids are only available for phones and tablets, not the web.  
  
7.  If you don't want to allow the user to group data by any column in the view (you want to save space, for example), in the **Group by Column** row, select the pencil button, and then in the **Configure Property "Group by Column"** dialog box, select **Disabled**, and then select **OK**.  
  
    > [!TIP]
    >  This is mostly useful for sub-grids on forms.  
  
8.  If you want to add JavaScript events, select the **Events** tab, and then select the appropriate tables, columns, and events. More information: [Developer Documentation: Use editable grids](../../developer/model-driven-apps/use-editable-grids.md)
  
     ![Add events in Editable Grid control.](media/add-events-in-editable-grid-control.png "Add events in Editable Grid control")  
  
9. To save your work, select **Save** on the action bar.  
  
10. When you're ready to make changes available to your team, select **Publish** on the action bar.  
  
11. To test your changes, go to the view you specified in step 5, and then make some in-line editing changes.  
  
## Make a sub-grid on a form editable

> [!NOTE] 
> - To save an editable grid change within a sub-grid, the user must explicitly save before navigating out of the form.
> - If you are using legacy forms (versions prior to Dynamics CRM 2016) and enable an editable grid on a sub-grid, the editable sub-grid will not be rendered. System administrators can turn off legacy forms in system settings, if needed.
  
1.  Open [solution explorer](advanced-navigation.md#solution-explorer).  
  
2.  Open the form that contains the sub-grid.  
  
3.  Select the appropriate control, and then select **Change Properties** on the ribbon.  
  
4.  In the **Set Properties** dialog box, select **Controls**, select **Add Control**, and then follow the same steps listed above.  
  
## Supported standard tables  

|**Web/tablet/phone**|**Tablet/phone only**|**Web only**|
|---------|---------|---------|
|Account<br /><br /> Appointment<br /><br /> Bookable Resource<br /><br /> Bookable Resource Booking<br /><br /> Bookable Resource Booking Header<br /><br /> Bookable Resource Category<br /><br /> Bookable Resource Category Assn<br /><br /> Bookable Resource Characteristic<br /><br /> Bookable Resource Group<br /><br /> Booking Status<br /><br /> Case<br /><br /> Category<br /><br /> Characteristic<br /><br /> Competitor<br /><br /> Contact<br /><br /> Email<br /><br /> Entitlement<br /><br /> Feedback<br /><br /> Invoice<br /><br /> Knowledge Article<br /><br /> Knowledge Article Views<br /><br /> Knowledge Base Record<br /><br /> Lead<br /><br /> Opportunity<br /><br /> Order<br /><br /> Phone Call<br /><br /> Price List<br /><br /> Product<br /><br /> Queue<br /><br /> Quote<br /><br /> Rating Model<br /><br /> Rating Value<br /><br /> SLA KPI Instance<br /><br /> Social Activity<br /><br /> Social Profile<br /><br /> Sync Error<br /><br /> Task<br /><br /> Team<br /><br /> User|Activity<br /><br /> Attachment<br /><br /> Channel Access Profile Rule Item<br /><br /> Competitor Address<br /><br /> Connection<br /><br /> Connection Role<br /><br /> Email Signature<br /><br /> Email Template<br /><br /> Expired Process<br /><br /> Invoice Product<br /><br /> Knowledge Article Incident<br /><br /> Lead To Opportunity Sales<br /><br /> Process<br /><br /> Mailbox<br /><br /> New Process<br /><br /> Note<br /><br /> Opportunity Product<br /><br /> Opportunity Sales Process<br /><br /> Order Product<br /><br /> Organization<br /><br /> Phone to Case Process<br /><br /> Price List Item<br /><br /> Queue Item<br /><br /> Quote Product<br /><br /> Sharepoint Document<br /><br /> Translation Process|Campaign<br /><br /> Campaign Activity<br /><br /> Campaign Response<br /><br /> Channel Access Profile<br /><br /> Channel Access Profile Rule<br /><br /> Contract<br /><br /> Entitlement Template<br /><br /> External Party<br /><br /> Fax<br /><br /> Letter<br /><br /> Marketing List<br /><br /> Position<br /><br /> Quick Campaign<br /><br /> Recurring Appointment<br /><br /> Sales Literature<br /><br /> SLA|  
 
##  Data types that aren't editable in an editable grid
The following data types aren't editable in editable grids: Customer and Partylist Lookup columns; Composite (address) columns; State/Status columns; Lookup table-related columns (for example, the Account table includes a contact lookup, where the Contact column is editable but the EmailAddress(Contact) column is not editable). 

## Group by views work on client side only
Grouping behavior works only on the client side and does not span pages. Group by is a client only function and works only on one page of data. Group by does not show you all options based on your complete data set on the server. Group by shows grouping only on the current page. You can disable the grouping by using the property on custom control configuration. More information: [Make main grids editable](#make-main-grids-editable)

## Business rules work only if conditional column is a column on the grid
Business Rules on an editable grid are supported only if the conditional column is also a column on the grid. If the column is not a column the business rules won’t work. Verify that each column referenced in the business rule is also included on the form. Note that business rules on an editable grid do not fire if the editable grid is configured on a dashboard.

## Next steps  
 [Use keyboard shortcuts in editable grids](/dynamics365/customer-engagement/basics/keyboard-shortcuts#editable-grids-views)



[!INCLUDE[footer-include](../../includes/footer-banner.md)]