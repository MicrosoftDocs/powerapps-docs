---
title: Use the Entity form control | Microsoft Docs
description: Create apps faster by using the Entity form control to add rich forms for a Common Data Service entity.
author: aneesmsft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: anneta
ms.date: 03/11/2017
ms.author: aneesa
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Use the Entity form control
Create apps faster by using the **Entity form** control to add rich forms for a Common Data Service entity.

For an introduction to the **Entity form** control, see this blog post: [New entity form control (experimental feature) for Common Data Service](https://powerapps.microsoft.com/blog/new-entity-form-control-experimental-feature-for-common-data-service/).

> [!IMPORTANT]
> Please be aware of the experimental nature of the **Entity form** control as outlined in the blog post, and be careful about using the **Entity form** control in production apps, at least for now.

## Key properties
Here are the key properties of an **Entity form** control.

**DataSource** – Specifies the data source that contains the record(s) that you want to display.   
> [!NOTE]
> Currently only entities in the Common Data Service are supported as data sources for the **Entity form** control.  

**Pattern** – Specifies the style of the form that you want to display in the **Entity form** control. Set this property by using the **FormPattern** enumeration.

* **FormPattern.List** – Displays a tabular list of records.
* **FormPattern.CardList** – Displays a card list of records.
* **FormPattern.Details** – Displays a form to view or edit the details of a single record.
* **FormPattern.None** – No style has been explicitly specified. Defaults to **List** for tablet apps and **CardList** for phone apps.

**Item** – Specifies the record in the data source that the **Entity form** control should display. This property is used only when **Pattern** is set to **FormPattern.Details**.

**Selected** – Gets the record that’s currently selected.  
Example: If the **Entity form** control displays a list of sales-order records, the **Selected** property will give you the record that’s currently selected. You can also access a field within a record. (For example, specify the value of the **Account** field of the selected record as **Selected.Account**.)

**SelectableFields** – Specifies which fields should appear as links. Set the value of this property by using this syntax:  
**{Field1Name : true, Field2Name : true}**  
Example: If you want the **SalesOrderId** and **Account** fields to appear as links in a form, set the **SelectableFields** property of that form to this value:  
**{SalesOrderId : true, Account : true}**

**SelectedField** – Determines which field was clicked or tapped. This applies only to the fields specified as **SelectableFields**.  
Example: If you set the **SelectableFields** property to **{SalesOrderId : true, Account : true}** and the user clicks or taps the **Account** field, **SelectedField.Account** is set to true.

**OnFieldSelect** – How an app responds when the user clicks or taps a field. This applies only to the fields specified as **SelectableFields**.

**Mode** – Determines the mode of the form. To change the mode, use the **ViewForm**, **EditForm**, or **NewForm** function. These functions work only when the **Pattern** property is set to **FormPattern.Details**. Set the value of the **Mode** property to a value of the **FormMode** enumeration.

* **FormMode.View** – Allows users to view but not edit or add a record.
* **FormMode.Edit** – Allows users to edit a record.
* **FormMode.New** – Allows users to add a record.

**OnSuccess** – How an app responds when a data operation has been successful.

**OnFailure** - How an app responds when a data operation has been unsuccessful.

**Unsaved** – Determines whether a record that a user is editing has unsaved changes.

## Related functions
You can use these  shared functions with either the **Entity form** control or the [Edit form control](functions/function-form.md). These functions work with the **Entity form** control only when its **Pattern** property is set to **FormPattern.Details**.

**ViewForm** – Sets the **Mode** property of an **Entity form** control to **FormMode.View**.

**EditForm**- Sets the **Mode** property of an **Entity form** control to **FormMode.Edit**.

**NewForm** - Sets the **Mode** property of an **Entity form** control to **FormMode.New**.

**SubmitForm** - Saves changes when a user edits a record in an **Entity form** control.

**ResetForm** - Abandons unsaved changes when a user edits a record in an **Entity form** control.

Now that you have an overview of the various properties and functions, let’s look at them in action.

> [!NOTE]
> If you don’t have access to a Common Data Service database, create one before you start to follow these steps.

## Display a list of records
The next five procedures provide a single, end-to-end example of how to use **Entity form** controls. In this procedure, add a form that shows a list of sales orders.  

1. Create a blank tablet app.
   
    ![](media/entity-form-control/entityform-tutorial-01-01.png)
2. Rename the first screen **SalesOrderListScreen**.
   
    ![](media/entity-form-control/entityform-tutorial-01-02.png)
3. On the **Insert** tab, click or tap **Forms**, and then click or tap **Entity form (experimental)**.  
   
    An **Entity form** control is added to the screen.  
   
    ![](media/entity-form-control/entityform-tutorial-01-03.png)
4. Rename the **Entity form** control **SalesOrderListForm**, and resize it to cover the entire screen.
5. In the right-hand pane, click or tap the database icon next to the text **No data source selected**, and then click or tap **Add a data source**.  
   
    ![](media/entity-form-control/entityform-tutorial-01-04.png)
6. In the list of connections, click or tap the connection for your database.  
   
    ![](media/entity-form-control/entityform-tutorial-01-05.png)
7. In the list of entities, click or tap **Sales order**, and then click or tap **Connect**.  
   
    A data source for the **Sales order** entity is created, and the **DataSource** property of the **SalesOrderListForm** is set to that data source.
   
    ![](media/entity-form-control/entityform-tutorial-01-06.png)  
   
    The **Entity form** control shows a list of sales orders. By using the **Entity form** control, you quickly displayed a list form without having to manually build it.
   
    ![](media/entity-form-control/entityform-tutorial-01-07.png)  
   
    You didn’t set the **Pattern** property for the **Entity form** control, so it defaults to the **List** pattern. In addition, the **DefaultList** field group of the **Sales order** entity is used to display the list form. The form is also dynamic and will automatically reflect any change in the field group.


## Display the details of a record
Let’s add another **Entity form** control to display the details of the sales order that’s selected in the list that you created earlier.  

1. Resize **SalesOrderListForm** to cover half the screen, and add a second **Entity form** control to cover the other half of the screen.  
   <br>![](media/entity-form-control/entityform-tutorial-01-09.png)
2. Rename the second **Entity form** control **SalesOrderDetailsForm**, and connect it to the **Sales order** data source that you created earlier.  
   <br>![](media/entity-form-control/entityform-tutorial-01-10.png)
3. Set the **Pattern** property of **SalesOrderDetailsForm** to **FormPattern.Details**.  
   
    **SalesOrderDetailsForm** uses the **DefaultDetails** field group of the **Sales order** entity to display the form. As with the **SalesOrderListForm**, you can quickly show record details without having to manually build a form.  
   
    ![](media/entity-form-control/entityform-tutorial-01-11.png)
4. Set the **Item** property of **SalesOrderDetailsForm** to **SalesOrderListForm.Selected**.
   
    **SalesOrderDetailsForm** will display the details of the record that the user clicks or taps in **SalesOrderListForm**.
   
    ![](media/entity-form-control/entityform-tutorial-01-12.png)
5. Preview the app by pressing F5, and then click or tap a sales order in the list on the left.  
   
    The details of the order that you selected appear on the right side.  
   
    ![](media/entity-form-control/entityform-tutorial-01-13.png)  

## Configure a field to navigate to another screen
Next let’s add more screens to our app and then configure fields in an **Entity form** control to navigate to another screen in the app when the user clicks or taps a field.  

1. Add a second screen to the app, and rename the screen **SalesOrderDetailsScreen**.
2. Cut the **SalesOrderDetailsForm**, paste it on the **SalesOrderDetailsScreen**, and resize the form to cover most of the screen, leaving enough space for an icon at the top.
3. Add a back-arrow icon near the upper-left corner of **SalesOrderDetailsScreen**.
4. Set the **OnSelect** property of the back-arrow icon to the [**Back**](functions/function-navigate.md) function.  
   
    ![](media/entity-form-control/entityform-tutorial-01-14.png)
5. On the **SalesOrderListScreen**, resize the **SalesOrderListForm** to cover the entire screen.
6. Click or tap the **SalesOrderListForm** to select it.
7. In the right-hand pane, under **Fields**, set **SalesOrderId** to navigate to the **SalesOrderDetailsScreen**.  
   
    ![](media/entity-form-control/entityform-tutorial-01-15.png)
   
    The **Entity form** control displays the values in the **SalesOrderId** field (the first column in the list) as links.
   
    ![](media/entity-form-control/entityform-tutorial-01-16.png)  
8. Preview the app by pressing F5, and then click or tap a link in the list of sales orders.
   
    ![](media/entity-form-control/entityform-tutorial-01-17.png)  
   
    The second screen opens and displays the details of the sales order that you specified.
   
    ![](media/entity-form-control/entityform-tutorial-01-18.png)  
   
    To display the details of a different sales order, click or tap the back arrow to navigate back to the list, and then click or tap the link of the order for which you want to show details.

## Navigate with a context variable
The **Item** property of the **SalesOrderDetailsForm** is set to **SalesOrderListForm.Selected** so that **SalesOrderDetailsForm** shows details about the record that the user selects in **SalesOrderListForm**. You can also get the context of the selected record by using the **NavigationContext** context variable, which gets automatically created when you use the form-customization pane to configure a field to navigate.  

1. Set the **Item** property of **SalesOrderDetailsForm** to **NavigationContext**.
   
    ![](media/entity-form-control/entityform-tutorial-01-19.png)
2. Preview the app by pressing F5, and then click or tap a link in the list of sales orders.
   
    The app opens **SalesOrderDetailsScreen** and displays the details of the sales order that you specified.

Let’s dig into how the form-customization pane sets up the navigation and context for us.  

The **SelectableFields** property of the **SalesOrderListForm** specifies **SalesOrderId** as a selectable field.

![](media/entity-form-control/entityform-tutorial-01-20.png)  

This was set up automatically when we used the form-customization pane to make the **SalesOrderId** field navigate to the **SalesOrderDetailsScreen**. Therefore, the values in the **SalesOrderId** field appear as links.

The **OnFieldSelect** property of the **SalesOrderListForm** is set to an [**If**](functions/function-if.md) function, which determines whether the user clicks or taps the **Sales order ID** field: **SalesOrderListForm.SelectedField.SalesOrderId = true**.  

If the function is evaluated as true, the **SalesOrderDetailsScreen** opens with the context variable named **NavigationContext** that we used earlier.  

All this was also set up automatically when we used the form-customization pane to make the **SalesOrderId** field navigate to the **SalesOrderDetailsScreen**.  

Therefore, when the user clicks or taps a sales order ID field, the [**If**](functions/function-if.md) function evaluates to true, and the [**Navigate**](functions/function-navigate.md) function is called with the corresponding context, opening the details screen.  

![](media/entity-form-control/entityform-tutorial-01-21.png)  

> [!NOTE]
> When you use the form-customization pane, the **NavigationContext** is intelligently determined for you. When the user clicks or taps **SalesOrderId**, **NavigationContext** is set to **SalesOrderListForm.Selected**, as the earlier formula shows. If we had specified the **Account** field for navigation instead, **NavigationContext** would have been set to **SalesOrderListForm.Selected.Account**, ensuring that the correct context is passed. However, to consume that context, you would need an **Entity form** control connected to the **Account** entity in the Common Data Service.

## Edit and save a record
Finally let’s look at how we can edit and save a record in an **Entity form** control.  

1. On the **SalesOrderDetailsScreen**, add an edit icon, and then set its **OnSelect** property to this formula:  
   **EditForm(SalesOrderDetailsForm)**
   
    ![](media/entity-form-control/entityform-tutorial-01-22.png)
2. Add a checkmark icon next to the edit icon, and then set the **OnSelect** property of the checkmark icon to this formula:  
   **SubmitForm(SalesOrderDetailsForm)**  
   
    ![](media/entity-form-control/entityform-tutorial-01-23.png)
3. Preview the app by pressing F5, click or tap a **Sales order ID** link to view the details of a sales order, and then click or tap the edit icon.  
   
    The **Mode** of the **Entity form** control is set to **FormMode.Edit** so that you can edit the record.
4. Update the **Order status** to **Invoice**.  
   
    ![](media/entity-form-control/entityform-tutorial-01-24.png)
5. Update the **Sales person** to **WRK014**.
   
    To help you pick the **Sales person**, the **Entity form** control automatically renders a rich detailed lookup. To generate and display this lookup, the control uses the **DefaultLookup** field group of the **Worker** entity in the Common Data Service. The **Worker** entity is used because the **Sales person** field is of type **Worker**.
   
    ![](media/entity-form-control/entityform-tutorial-01-25.png)
6. Click or tap the checkmark icon to save your changes.

This step concludes this article on how to use the **Entity form** control in your apps. We hope that you find the information covered here useful to get started using the **Entity form** control. We look forward to hearing what you think about the **Entity form** control and our overall push toward helping you quickly add rich forms to your apps.

