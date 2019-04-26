---
title: Build Northwind Orders (Canvas): Part 1, Orders list | Microsoft Docs
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
# Build Northwind Orders (Canvas): Part 1, Orders list

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

## Edit and display Order information

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

1. Add and remove fields to get to the list we want.  The order of fields in the pane and in the form doesn't matter, we'll rearrange them on the form shortly.  To follow along with these instructions, you'll want these fields:

	- **Order Number**
	- **Order Status**
	- **Order Date**
	- **Paid Date**
	- **Customer**
	- **Employee**
	- **Notes**

	![](media/northwind-orders-canvas-part2/form-fields-our-set.png)

1. 







## On to Part 3

To recap, we just built a single screen Canvas app that shows the list of Orders.  This list includes:
- A formula to format the Order Number: `"Orders " & ThisItem.OrderNumber`
- A field in a Many-to-One relationship: `ThisItem.Customer.Company`
- An Option set label: `ThisItem.'Order Status'`
- Conditional formatting for the status: `Switch( ThisItem.'Order Status', 'Orders Status'.Closed, Green, ...`
- An aggregate function over a One-to-Many relationship: `Sum( ThisItem.'Order Details', Quantity * 'Unit Price' )`

In the next part, we'll add an [**Edit form** control](controls/control-form-detail.md) to display and edit more information about the order in a form.




	


