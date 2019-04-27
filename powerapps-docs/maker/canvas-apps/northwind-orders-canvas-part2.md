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

This series of articles will build a simple order management Canvas app step-by-step.  It will showcase how to use:
- Many-to-One relationships.  Many Orders can be related to the same Customer.  But each Order can be related to only one Customer.
- One-to-Many relationships.  Each Order can be related to many Order Details (or line items).  But each Order Detail is related to only one Order.
- Many-to-Many relationships.  Each Product can be related to many Product Categories.  And each Product Category can be related to many Products. 
- Option sets.  

The completed app will look like this:

![](media/northwind-orders-canvas-part1/orders-finished.png)

There are four parts:
- [Part 1, Orders list](northwind-orders-canvas-part1.md)
- Part 2, Order details form (this part)
- [Part 3, Order line items](northwind-orders-canvas-part3.md)
- [Part 4, Order categories](northwind-orders-canvas-part4.md) 

If you have not already done so, work through part 1.  Or take a shortcut by opening the **Northwind Orders (Canvas), Building Part 1** app after [installing the Northwind Traders sample database and apps](northwind-install.md)

## A title bar for later

1. Let's create a title bar across the top of the app where we can place additional buttons that will be helpful as we continue building our app.

	Select **Screen1** in the Navigation pane.  This ensures that we don't accidentally add controls to the gallery:

	![](media/northwind-orders-canvas-part2/titlebar-select-screen.png)

1. From the **Insert** ribbon, insert a [**Label** control](controls/control-text-box.md) control:

	![](media/northwind-orders-canvas-part2/titlebar-insert-label.png)

	This control should appear only once, over the top of the gallery.  If it is replicated for each item in the gallery, remove it and ensure the screen is selected in the last step before inserting it again.

1. Resize and reposition the control to span the top of the app:

	![](media/northwind-orders-canvas-part2/titlebar-reposition.png)

1. Double click into the control to edit the text for the control and enter Northwind Orders:

	![](media/northwind-orders-canvas-part2/titlebar-text.png)

	Notice that the **Text** property is being updated in the formula bar as you type. 

1. From the **Home** ribbon, format the control to center the text, fill the background with dark blue, use white for the text color, use a bold font, and increase the font size:

	![](media/northwind-orders-canvas-part2/titlebar-text-format.png)

## Display more Order information

1. From the **Insert** ribbon, insert an [**Edit form** control](controls/control-form-detail.md):

	![](media/northwind-orders-canvas-part2/form-insert.png)

1. Resize and reposition this control under the title bar in the upper right side of the screen:

	![](media/northwind-orders-canvas-part2/form-position.png)

1. In the Properties panel, pull down the Data source and select **Orders**:

	![](media/northwind-orders-canvas-part2/form-datasource.png)

1. This will insert a default set of fields in the form.  

	![](media/northwind-orders-canvas-part2/form-fields-starter.png)

1. We'll replace these with ones that we want to show.  Select **Edit fields** in the Properties pane:

	![](media/northwind-orders-canvas-part2/form-fields-edit.png)

1. With the Fields pane we can add and remove fields.  Let's remove the **Attachments** field:
  
	![](media/northwind-orders-canvas-part2/form-fields-remove-attach.png)

1. And let's add the **Customer** and **Employee** fields:

	![](media/northwind-orders-canvas-part2/form-fields-add.png)

1. Add and remove fields to get to the list we want.  The order of fields in the pane and in the form doesn't matter, we'll rearrange them on the form shortly:  

	![](media/northwind-orders-canvas-part2/form-fields-our-set.png)

	To follow along with these directions, you'll want these fields:

	- **Order Number**
	- **Order Status**
	- **Order Date**
	- **Paid Date**
	- **Customer**
	- **Employee**
	- **Notes**

1. In the **Properties** panel, change the number of columns from 3 to 12.  This will give us more flexibility in laying out the fields: 

	![](media/northwind-orders-canvas-part2/form-columns-3.png)

	Although we said 12, that would make for some very small fields if the form control took us literally.  When switching the number of columns, the form control will keep the fields at least 3 columns wide, but we do have 12 snap points across to work with:

	![](media/northwind-orders-canvas-part2/form-columns-12.png)

1. Reposition the fields within the form by drag-and-drop of their drag handles and resize them as you would any control:

	![](media/northwind-orders-canvas-part2/form-rearrange.gif)

	For more information on working with form layout, see the article [understand data-form layout for canvas apps](working-with-form-layout).

1. For the date fields we don't want to show the time portions.  It is tempting to just select the time controls and delete them, but that can cause problems if they are a part of the formulas for updating data values or the positioning of other controsl.  

	The best way to accomplish our goal is to set the **Visible** property of the hour, minutes, and colon controls to *false* and resize the **Date picker** control to fill the width of the data card.  
 
	To do this, we will need to first unlock the data card:

	![](media/northwind-orders-canvas-part2/form-unlock-date.png)

	Then multi-select the three controls by holding down the Shift key while selecting each.  Zooming in with the slider control at the very bottom of the Studio makes this easier.  You can also multi-select with the Tree View in the left hand pane:

	![](media/northwind-orders-canvas-part2/form-visible-date.png)

	Then set **Visible** to *false* which will be done for all three at once since they are multi-selected:

	![](media/northwind-orders-canvas-part2/form-invisible-date.png)

	And now we can resize the date picker to show all of the date:

	![](media/northwind-orders-canvas-part2/form-wide-date.png)

1. Repeat the last step for the **Paid Date** field:

	![](media/northwind-orders-canvas-part2/form-both-dates.png)

1. Let's connect this form to the selected Order in our Orders list.  Set the **Item** property of the form control to:

	```powerapps-dot
	Gallery1.Selected
	```

	![](media/northwind-orders-canvas-part2/form-item.png)

	As you change selection in the gallery, the form will update to reflect the information for that order.

## Choices and Many-to-One relationships

1. In form contains there [**Combo box** controls](controls/control-combo-box.md).  The first combo box is for **Order Status**.  This is an option set as we saw when building the Orders list.

	If we select the combo box control within the data card, which requires selecting the data card first, we'll see that it's **Items** property is set to `Choices( 'Orders Status' )`:

	![](media/northwind-orders-canvas-part2/choices-status.png)

	The [**Choices** function](functions/function-choices.md) returns all the possilbe values for the option set which are displayed if we pull down on the combo box:

	![](media/northwind-orders-canvas-part2/choices-status-open.png)

	There is nothing to change in our app for this step, we were just exploring how it worked.

1. Something similar happens for Many-to-One relationships.  If we select the control in the **Employee** field:

	![](media/northwind-orders-canvas-part2/choices-employee.png)

	It is set to `Choices(Orders.nwind_EmployeeID)`.  This is the logical name for the lookup field from **Orders** to the **Employees** entity.

	As we saw with the Orders list, we could reference the **Company** field of the **Customer** lookup as if the entire **Customer** record wsa available to us for each **Order**.  The same is true here - the complete record for the employee is available through the combo box control's **Selected** property.

	Likewise the **Choices** function returns the entire record for each employee in a table to feed the combo box.  The copmlete record is used to select a different employee if the app's user decides to change the employee for an order.

	![](media/northwind-orders-canvas-part2/choices-employee-resultview.png)

	Again nothing to change in our app for this step, we are continuing our exploration.

1. Now it is time to act.  Unlock the **Employees** card:

	![](media/northwind-orders-canvas-part2/choices-employee-unlock.png)

1. Resize the combo box control to make room for the employee picture:

	![](media/northwind-orders-canvas-part2/choices-employee-resize.png)


![](media/northwind-orders-canvas-part2/choices-employee-insert-picture.png)

![](media/northwind-orders-canvas-part2/choices-employee-insert-card.png)


![](media/northwind-orders-canvas-part2/choices-employee-empty-picture.png)


![](media/northwind-orders-canvas-part2/choices-employee-picture.png)

![](media/northwind-orders-canvas-part2/ordernumber-open.png)

![](media/northwind-orders-canvas-part2/ordernumber-change.png)

![](media/northwind-orders-canvas-part2/ordernumber-done.png)

![](media/northwind-orders-canvas-part2/ordernumber-bigger.png)



## On to Part 3

To recap, we just built a single screen Canvas app that shows the list of Orders.  This list includes:
- A formula to format the Order Number: `"Orders " & ThisItem.OrderNumber`
- A field in a Many-to-One relationship: `ThisItem.Customer.Company`
- An Option set label: `ThisItem.'Order Status'`
- Conditional formatting for the status: `Switch( ThisItem.'Order Status', 'Orders Status'.Closed, Green, ...`
- An aggregate function over a One-to-Many relationship: `Sum( ThisItem.'Order Details', Quantity * 'Unit Price' )`

In the next part, we'll add an [**Edit form** control](controls/control-form-detail.md) to display and edit more information about the order in a form.




	


