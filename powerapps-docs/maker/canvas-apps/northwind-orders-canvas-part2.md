---
title: 'Build Northwind Orders (Canvas): Part 2, Order form | Microsoft Docs'
description: Build the Canvas version of Northwind Orders
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: anneta
ms.date: 04/25/2019
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Build Northwind Orders (Canvas): Part 2, Order form

Let's continue building a simple order management canvas app over data in the Common Data Service, step-by-step.  When we are done we will have a single screen master-detail app:

![](media/northwind-orders-canvas-part1/orders-finished.png)

This app will showcase:

- **Many-to-One relationships.** Many Orders can be related to the same Customer. Each Order can be related to only one Customer.  All of the columns of the foreign entity are available to use.
- **One-to-Many relationships.** Each Order can be related to many Order Details (or line items). Each Order Detail is related to only one Order.
- **Option sets.**  A set of named choices defined in the database and shared across apps.  
- **Gallery and form interactions.**  The gallery provides the list of Orders to choose from, and the rest of the app responds to changes in the gallery's selection.      

The instructions for building the app are broken into three parts:

![](media/northwind-orders-canvas-part1/orders-parts.png)

- [**Part 1, Orders list**](northwind-orders-canvas-part1.md):  Displays the list of orders.  Selection in this list determines which order is being edited on the rest of the screen.
- **Part 2, Order form**:  View and edit information about the order.  Here new orders can be created and existing orders deleted.  You are here.
- [**Part 3, Order details**](northwind-orders-canvas-part3.md):  View and edit the product line items that are associated with the order.  

If you have not already done so, work through [part 1](northwind-orders-canvas-part1.md).  Or take a shortcut by opening the **Northwind Orders (Canvas), Start Part 2** app after [installing the Northwind Traders sample database and apps](northwind-install.md)

## An app title bar

1. Let's create a title bar across the top of the app.  We'll use this space to hold action buttons later.

	Select **Screen1** in the Navigation pane.  This ensures that we don't accidentally add controls to the orders list gallery:

	![](media/northwind-orders-canvas-part2/titlebar-01.png)

1. From the **Insert** ribbon, insert a [**Label** control](controls/control-text-box.md):

	![](media/northwind-orders-canvas-part2/titlebar-02.png)

	This control should appear only once, over the top of the gallery.  If it is replicated for each item in the gallery, delete it and ensure the screen is selected (see previous step) before inserting it again.

1. Re-size and re-position the control to span the top of the screen:

	![](media/northwind-orders-canvas-part2/titlebar-03.png)

1. Double click into the control to edit the text for the control and enter **Northwind Orders**.  Alternatively, you can modify the **Text** property in the formula bar, both methods do the same thing:

	![](media/northwind-orders-canvas-part2/titlebar-04.png)

1. Using the **Home** ribbon, use the formatting buttons to format the label control:
    - increase the font size to 24 points
    - use a bold font
    - use white for the text color
    - center the text
    - fill the background with dark blue

    ![](media/northwind-orders-canvas-part2/titlebar-05.png)

## Display more Order information in a form

1. Let's display more of the columns from the currently selected order.  

    From the **Insert** ribbon, insert an [**Edit form** control](controls/control-form-detail.md):

	![](media/northwind-orders-canvas-part2/form-01.png)

	The control will overlay the other controls on the screen in the top left corner and may difficult to see:

	![](media/northwind-orders-canvas-part2/form-02.png)

1. Re-size and re-position this control under the title bar in the upper right corner of the screen:

	![](media/northwind-orders-canvas-part2/form-03.png)

1. In the formula bar, set the **DataSource** property of the control to this formula:

    ```powerapps-dot
    Orders
    ```

	![](media/northwind-orders-canvas-part2/form-04.png)

    We could have also used the Properties panel to set the data source but this would have added fields to the form that we don't need.  By setting the data source in the formula bar the form remains empty. 

1. In the Properties panel, select **Edit fields** which will open the **Fields** panel:  

	![](media/northwind-orders-canvas-part2/form-05.png)

1. Select **+ Add field** and place a check mark next to these fields:

	- **Customer**
	- **Employee**

	![](media/northwind-orders-canvas-part2/form-06.png)

	Scroll down and place a check mark next to these fields:

	- **Notes**
	- **Order Date** 
	- **Order Number**
	- **Order Status**
	- **Paid Date**

	![](media/northwind-orders-canvas-part2/form-07.png)

	Finally, select the **Add** button at the bottom of the Fields panel.

	We now see seven fields in our form:

	![](media/northwind-orders-canvas-part2/form-08.png)

    If any of these fields show a red error there may be a problem with metadata fetch.  Using the **View** ribbon, select **Data sources**, select the three elipses to the right of **Orders** and **Refresh** the data source.

1. In the **Properties** panel, change the number of columns from 3 to 12.  This will give us more flexibility in laying out the fields:

	![](media/northwind-orders-canvas-part2/form-08b.png)

    Using a 12 column layout is common in UI design as spans of 12 columns can evenly accomodate rows of 1, 2, 3, 4, 6, and 12 controls.  We'll use this for a mix of 1, 2, and 4 controls in each row.

1. Re-position the fields within the form by drag-and-drop of their drag handles and re-size them as you would any control:

	![](media/northwind-orders-canvas-part2/form-rearrange.gif)

	For more information on working with form layout, see [understand data-form layout for canvas apps](working-with-form-layout.md).

1. Let's not show the time portions of the date fields, that level of granularity is not needed.  

    It is tempting to just select the time controls and delete them, but that can cause problems if they are a part of the formulas for updating data values or the positioning of other controls within the data card.  

	The best way to accomplish our goal is to set the **Visible** property of the hour, minutes, and colon separator controls to *false* and resize the [**Date picker** control](controls/control-date-picker.md) to fill the width of the data card.  
 
	Find the **Order Date** data card in the left navigation pane (it may have a different name, but should contain **Order Date**).  In the navigation pane, multi-select the three controls by holding down the Shift key while selecting each.  

	![](media/northwind-orders-canvas-part2/form-09.png)

	Then set **Visible** to *false*.  All controls selected will be effected:

	![](media/northwind-orders-canvas-part2/form-10.png)

	And now we can re-size the date picker to show the complete date:

	![](media/northwind-orders-canvas-part2/form-11.png)

1. Repeat the last step for the **Paid Date** field.  First multi-select the controls in the left hand navigation panel:

	![](media/northwind-orders-canvas-part2/form-12.png)

    Then set **Visible** to *false*:

	![](media/northwind-orders-canvas-part2/form-13.png)	

    And finally re-size the date picker control:

	![](media/northwind-orders-canvas-part2/form-14.png)	

1. Finally, let's connect the selected item in our Orders list to the Order form.  
 
    Select the form control in the navigation pane.  Set the **Item** property of the form control to:

	```powerapps-dot
	Gallery1.Selected
	```

	![](media/northwind-orders-canvas-part2/form-15.png)

    Your gallery may be named something different than **Gallery1**.  Check the navigation pane to find the name of your form if you experience problems.  

	Now as you change selection in the gallery, the form will update to reflect additional information for that order.

	![](media/northwind-orders-canvas-part2/form-select.gif)

## Alternate data cards

1. The Order number field is an auto-number field, assigned by the Common Data Service when the record is created.  Let's change the data card so this field is not editable.

    Some data types offer a selection of pre-built experiences.  Select the form control and in the properties panel select **Edit fields**.  Then select the **Order number** field:

	![](media/northwind-orders-canvas-part2/alt-01.png)

1. Pull down on the **Control type** control:

	![](media/northwind-orders-canvas-part2/alt-02.png)

1. Select the **View text** data card:  

	![](media/northwind-orders-canvas-part2/alt-02b.png)

1. Close the Data panel.  Now we will only see the order number but will be unable to change it:
	
	![](media/northwind-orders-canvas-part2/alt-03.png)

1. To make the order number more prominent, use the **Home** ribbon to re-size the text of the order number to 20 points:

	![](media/northwind-orders-canvas-part2/alt-04.png)

## Using Many-to-One relationships in data cards

1. 	Let's display the employee's picture next to the selected employee.  Select the employee data card:  

	![](media/northwind-orders-canvas-part2/employee-01.png)

1. Using the Advanced panel, unlock the **Employees** card:

	![](media/northwind-orders-canvas-part2/employee-02.png)

	After it has been unlocked, formulas that were previously read only can now be edited:

	![](media/northwind-orders-canvas-part2/employee-03.png)

1. Re-size the combo box control within the data card to make room for the employee picture:

	![](media/northwind-orders-canvas-part2/employee-03b.png)

1. From the **Insert** menu, insert an [**Image** control](controls/control-image.md).  Make sure that the data card is selected before doing so:

	![](media/northwind-orders-canvas-part2/employee-04.png)

	The data card will expand to accept the image control: 

	![](media/northwind-orders-canvas-part2/employee-05.png)

1. Re-size and re-position the image control to the right of the combo box control:

	![](media/northwind-orders-canvas-part2/employee-06.png)

1. Set the **Image** property of the image control to this formula:

	```powerapps-dot
	DataCardValue1.Selected.Picture
	```

	![](media/northwind-orders-canvas-part2/employee-07.png)

	And now we see the picture of the selected employee.

    It is possible the name of your combo box control is different than shown here.  Check the navigation pane on the left side of the PowerApps Studio to see the control name used in your app.
 	
    The **Orders** entity has a Many-to-One relationship with the **Employees** entity.  As we saw with the Orders list we can reference all the columns of the related record, in this case the **Picture** field.  We are doing this from the record that is selected in the combo box control.

1. Change the value in the combo box to see how the picture shown tracks with the selection.

	![](media/northwind-orders-canvas-part2/employee-select.gif)

## Saving changes

1. Let's add a button to save the changes that app users make in the form.  

    Select **Screen1** in the navigation pane, to ensure we don't add a control to a data card.  From the **Insert** ribbon, insert a check mark **Icon** control: 

	![](media/northwind-orders-canvas-part2/save-01.png)

    The inserted icon will overlap other controls in the left upper corner of the screen and may be difficult to see: 

	![](media/northwind-orders-canvas-part2/save-02.png)

1. Using the **Home** ribbon, change the color of this icon to white.  Re-size and re-position this control to the upper right hand side of the title bar:

	![](media/northwind-orders-canvas-part2/save-03.png)

1. Set the **OnSelect** property to the formula:

	```powerapps-dot
	SubmitForm( Form1 )
	```

	![](media/northwind-orders-canvas-part2/save-04.png)

    The [**SubmitForm** function](functions/function-form.md) will gather any changed values in the form and submit them to the database.  Marching ants can be seen across the top of the screen while this is happening, and when complete, the gallery control will reflect the changes.

1. Set the **DisplayMode** property to the formula:

	```powerapps-dot
	If( Form1.Unsaved, DisplayMode.Edit, DisplayMode.Disabled )
	```

	![](media/northwind-orders-canvas-part2/save-05.png)

    It only makes sense to submit changes if there are unsaved changes on the form.  If there are no unsaved changes, the icon will appare with the **DisabledColor** which we will set next. 

1. Set the **DisabledColor** property to the formula:

	```powerappd-dot
	Gray
	```

	![](media/northwind-orders-canvas-part2/save-06.png)

	We can now save changes to an order.  The check mark icon will be disabled and gray if we have not changed anything on the form:

	![](media/northwind-orders-canvas-part2/save-submit.gif)

1. Let's add a button to cancel changes made to the data in a form, in case an app user changes their mind. 

    From the **Insert** ribbon, insert a cancel **Icon** control: 

	![](media/northwind-orders-canvas-part2/save-07.png)

    The inserted icon will overlap other controls in the left upper corner of the screen and may be difficult to see:

	![](media/northwind-orders-canvas-part2/save-08.png)

1. Using the **Home** ribbon, change the color of this icon to white.  Re-size and re-position this control to the upper right hand side of the title bar:

	![](media/northwind-orders-canvas-part2/save-09.png)

1. Set the **OnSelect** property to the formula:

	```powerapps-dot
	ResetForm( Form1 )
	```

	![](media/northwind-orders-canvas-part2/save-10.png)

    The [**ResetForm** function](functions/function-form.md) will discard all changes in the form and return the record to its original state.

1. Set the **DisplayMode** property to the formula:

	```powerapps-dot
	If( Form1.Unsaved Or Form1.Mode = FormMode.New, DisplayMode.Edit, DisplayMode.Disabled )
	```

	![](media/northwind-orders-canvas-part2/save-11.png)

    The formula here is slightly different from the one we used for the submit button.  I doesn't make sense to discard changes if none have been made.  But there is an added case: if the form is in **New** mode (which we'll enable next) we will want **ResetForm** to discard the new record.

1. Set the **DisabledColor** property to the formula:

	```powerappd-dot
	Gray
	```

	![](media/northwind-orders-canvas-part2/save-12.png)

	We can now cancel changes to an order.  The check mark and cancel icons will be disabled and gray if we have not changed anything on the form:

	![](media/northwind-orders-canvas-part2/save-cancel.gif)

1. From the **Insert** ribbon, insert an add **Icon** control.  

	![](media/northwind-orders-canvas-part2/save-13.png)

    The inserted icon will overlap other controls in the left upper corner of the screen and may be difficult to see:

	![](media/northwind-orders-canvas-part2/save-14.png)

1. Using the **Home** ribbon, change the color of this icon to white.  Re-size and re-position this control to the upper right hand side of the title bar:

	![](media/northwind-orders-canvas-part2/save-15.png)

1. Set the **OnSelect** property to the formula:

	```powerapps-dot
	NewForm( Form1 )
	```

	![](media/northwind-orders-canvas-part2/save-15b.png)

    The [**NewForm** function](functions/function-form.md) will create a new blank record to show in the form.  

1. Set the **DisplayMode** property to the formula:

	```powerapps-dot
	If( Form1.Unsaved Or Form1.Mode = FormMode.New, DisplayMode.Disabled, DisplayMode.Edit )
	```

	![](media/northwind-orders-canvas-part2/save-16.png)

    The formula is the reverse of the last **DisplayMode** we set.  Here, if there are unsaved changed we should be disabled until those are saved.  Even if there are no unsaved changed (no deviation from the default blank) we still should not enter **New** mode again.  

1. Set the **DisabledColor** property to the formula:

	```powerappd-dot
	Gray
	```

	![](media/northwind-orders-canvas-part2/save-17.png)

	We can now create new orders.  But only if the form has no unsaved changes and we are already not creating an order:  

	![](media/northwind-orders-canvas-part2/save-new.gif)

1. From the **Insert** ribbon, insert a **Trash** **Icon** control.  

	![](media/northwind-orders-canvas-part2/save-18.png)

    The inserted icon will overlap other controls in the left upper corner of the screen and may be difficult to see:

	![](media/northwind-orders-canvas-part2/save-19.png)

1. Using the **Home** ribbon, change the color of this icon to white.  Re-size and re-position this control to the upper right hand side of the title bar:

	![](media/northwind-orders-canvas-part2/save-20.png)

1. Set the **OnSelect** property to the formula:

	```powerapps-dot
	Remove( Orders, Gallery1.Selected )
	```

	![](media/northwind-orders-canvas-part2/save-21.png)

    The [**Remove** function](functions/function-remove-removeif.md) is not a form control function.  But we are grouping it here since the app's user would see that the currently selected record, which is showing in the form, is the one to be deleted.  Rather than working through the form control, we use the **Remove** function which directly removes a record form a data source.

1. Set the **DisplayMode** property to the formula:

	```powerapps-dot
	If( Form1.Mode = FormMode.New, DisplayMode.Disabled, DisplayMode.Edit )
	```

	![](media/northwind-orders-canvas-part2/save-22.png)

    It doesn't make sense to delete a record that is being created, that does not yet exist in the data source.

1. Set the **DisabledColor** property to the formula:

	```powerappd-dot
	Gray
	```

	![](media/northwind-orders-canvas-part2/save-23.png)

	We can now delete existing orders.

	![](media/northwind-orders-canvas-part2/save-delete.gif)

## On to Part 3

To recap, we just added a form to our app which allows us to see and edit more information about each order.  We used:
- A form for Orders: **DataSource =** `Orders`
- A connection between the Orders list and the form: **Item =** `Gallery1.Selected`
- An alternate data card for Order number: **View text**
- A Many-to-One relationship to show the employee's picture in the employee data card: `DataCardValue1.Selected.Picture`
- Icon to save changes to an Order: `SubmitForm( Form1 )`
- Icon to cancel changes to an Order: `ResetForm( Form1 )`
- Icon to create a new Order: `NewForm( Form1 )`
- Icon to delete an existing record: `Remove( Orders, Gallery1.Selected )` 

In the next part, we'll add another gallery control and use the [**Patch** function](functions/function-patch.md) to display and edit the list of items sold with each order.




	


