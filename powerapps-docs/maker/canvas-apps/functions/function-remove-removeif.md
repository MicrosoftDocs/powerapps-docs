---
title: Remove and RemoveIf functions | Microsoft Docs
description: Reference information, including syntax and examples, for the Remove and RemoveIf functions in Power Apps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 03/28/2020
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Remove and RemoveIf functions in Power Apps
Removes [records](../working-with-tables.md#records) from a [data source](../working-with-data-sources.md).

## Description
### Remove function
Use the **Remove** function to remove a specific record or records from a data source.  

For [collections](../working-with-data-sources.md#collections), the entire record must match. You can use the **All** argument to remove all copies of a record; otherwise, only one copy of the record is removed.

### RemoveIf function
Use the **RemoveIf** function to remove a record or records based on a condition or a set of conditions. Each condition can be any formula that results in a **true** or **false** and can reference [columns](../working-with-tables.md#columns) of the data source by name. Each condition is evaluated individually for each record, and the record is removed if all conditions evaluate to **true**.

**Remove** and **RemoveIf** return the modified data source as a [table](../working-with-tables.md). You can use both functions only in [behavior formulas](../working-with-formulas-in-depth.md).

You can also use the **[Clear](function-clear-collect-clearcollect.md)** function to remove all of the records in a data source.

### Delegation
[!INCLUDE [delegation-no](../../../includes/delegation-no.md)]

## Syntax
**Remove**( *DataSource*, *Record1* [, *Record2*, ... ] [, **All** ] )

* *DataSource* – Required. The data source that contains the record or records that you want to remove.
* *Record(s)* – Required. The record or records to remove.
* **All** – Optional. In a collection, the same record may appear more than once.  You can add the **All** argument to remove all copies of the record.

**Remove**( *DataSource*, *Table* [, **All** ] )

* *DataSource* – Required. The data source that contains the records that you want to remove.
* *Table* – Required. A table of records to remove.
* **All** – Optional. In a collection, the same record may appear more than once.  You can add the **All** argument to remove all copies of the record.

**RemoveIf**( *DataSource*, *Condition* [, ... ] )

* *DataSource* – Required. The data source that contains the record or records that you want to remove.
* *Condition(s)* – Required. A formula that evaluates to **true** for the record or records to remove.  You can use column names from the *DataSource* in the formula.  If you specify multiple *Conditions*, all must evaluate to **true** for the record or records to be removed.

## Examples

### Simple examples
In these examples, you'll remove a record or records in a data source that's named **IceCream** and that starts with the data in this table:

![](media/function-remove-removeif/icecream.png)

To create a collection with this data, insert a [**Button** control](../controls/control-button.md), set its **OnSelect** property to the below formula, and select the button [while holding down the Alt key](../keyboard-shortcuts.md#alternate-behavior):

```powerapps-dot
ClearCollect( IceCream,
              { ID: 1, Flavor: "Chocolate",  Quantity: 100 },
              { ID: 2, Flavor: "Vanilla",    Quantity: 200 },
              { ID: 3, Flavor: "Strawberry", Quantity: 300 }
)
```


| Formula | Description | Result |
| --- | --- | --- |
| **Remove(&nbsp;IceCream,<br>First(&nbsp;Filter(&nbsp;IceCream,&nbsp;Flavor="Chocolate"&nbsp;)&nbsp;) )** |Removes the **Chocolate** record from the data source. |<style> img { max-width: none } </style> ![](media/function-remove-removeif/icecream-no-chocolate.png)<br><br>The **IceCream** data source has been modified. |
| **Remove(&nbsp;IceCream,<br>First(&nbsp;Filter(&nbsp;IceCream,&nbsp;Flavor="Chocolate"&nbsp;)&nbsp;) First(&nbsp;Filter(&nbsp;IceCream,&nbsp;Flavor="Strawberry"&nbsp;)&nbsp;) )** |Removes two records from the data source. |![](media/function-remove-removeif/icecream-only-vanilla.png)<br><br>The **IceCream** data source has been modified. |
| **RemoveIf(&nbsp;IceCream, Quantity&nbsp;>&nbsp;150 )** |Removes records that have a **Quantity** that's greater than **150**. |![](media/function-remove-removeif/icecream-only-chocolate.png)<br><br>The **IceCream** data source has been modified. |
| **RemoveIf(&nbsp;IceCream, Quantity&nbsp;>&nbsp;150, Left(&nbsp;Flavor,&nbsp;1&nbsp;) = "S" )** |Removes records that have a **Quantity** that's greater than 150 and **Flavor** starts with an **S**. |![](media/function-remove-removeif/icecream-no-strawberry.png)<br><br><br>The **IceCream** data source has been modified. |
| **RemoveIf(&nbsp;IceCream, true )** |Removes all records from the data source. |![](media/function-remove-removeif/icecream-empty.png)<br><br>The **IceCream** data source has been modified. |

### Removing an item from a gallery

In this example we will use a [**Gallery** control](../controls/control-gallery.md) to list the records in a table and then use the **Remove** function to selectively remove an item.  

This example uses the **Contacts** entity in Common Data Service which has been loaded with sample data when the database was created.  You can create your own database with sample data by creating a trial environment.  

Any data source or collection can be used in this same manner.  To use a collection to work through this example, add a [**Button** control](../controls/control-button.md) to your screen, set the **OnSelect** property to the formula below, and select the button [while holding down the Alt key](../keyboard-shortcuts.md#alternate-behavior):

```powerapps-dot
ClearCollect( Contacts, 
              { Name: "Yvonne",  Email: "yvonne@contoso.com" },
              { Name: "Susanna", Email: "susanna@contoso.com" },
              { Name: "Nancy",   Email: "nancy@contoso.com" },
              { Name: "Maria",   Email: "maria@contoso.com" },
              { Name: "Robert",  Email: "robert@contoso.com" },
              { Name: "Paul",    Email: "paul@contoso.com" },
              { Name: "Rene",    Email: "rene@consoto.com" } 
)
```

#### From outside the gallery

In this first part, we will remove an item by using a button that is outside the gallery.

1. Create a [new blank canvas app](../data-platform-create-app-scratch.md) using a Phone layout.

    > [!div class="mx-imgBorder"]
    > ![A blank canvas app using the phone layout](media/function-remove-removeif/gallery-new.png)

1. Select the **Insert** tool pane on the left hand side of the studio.  

1. Select **Vertical gallery**.  A **Gallery** control will be added to your screen.

    > [!div class="mx-imgBorder"]
    > ![Using the Insert tool pane to add a vertical gallery control](media/function-remove-removeif/gallery-add.png)

1. You will be prompted to select a data source.  If your desired data source is not shown, enter the name in the Search box at the top.  For this exercise, select the **Contacts** entity.  

    > [!div class="mx-imgBorder"]
    > ![Selecting the Contacts entity to display in the gallery](media/function-remove-removeif/gallery-datasource.png)

1. The gallery will show items from this entity. 

    > [!div class="mx-imgBorder"]
    > ![Gallery added showing the Contacts entity](media/function-remove-removeif/gallery-data.png)

1. Insert a [**Button** control](../controls/control-button.md) from the Insert tool pane.
    
    > [!div class="mx-imgBorder"]
    > ![Using the Insert tool pane to add a button control](media/function-remove-removeif/gallery-addbutton.png)

1. Set the **OnSelect** property for this button control to the formula:

    ```powerapps-dot
    Remove( Contacts, Gallery1.Selected )
    ```

    > [!div class="mx-imgBorder"]
    > ![Setting the OnSelect property of the button control](media/function-remove-removeif/gallery-button-onselect.png)

    The gallery controls makes the currently selected record available through its **Selected** property.  We use this to tell the **Remove** function which record to be remove from the **Contacts** entity.

1. [Hold down the Alt key](../keyboard-shortcuts.md#alternate-behavior) and select the third item in the gallery, in our case Nancy's record.  You can also preview the app to select items (press F5 or use the triangular icon in the upper right corner of the studio).

1. Again with the Alt key held down, select the button control.  The record for Nancy will be removed.

    > [!div class="mx-imgBorder"]
    > ![Gallery of contacts, now without the Nancy record that has been removed](media/function-remove-removeif/gallery-activatebutton.png)

#### From inside the gallery

In this next part, we will remove an item from inside the gallery.

1. Select the top item of the gallery.  This is important to ensure that the next step will insert the item into the gallery's template and not outside the gallery.

    > [!div class="mx-imgBorder"]
    > ![Gallery with the top record selected, which is the template for how records are replicated throughout the rest of the gallery](media/function-remove-removeif/gallery-select-template.png)

1. Return to the Insert tool pane and select **Add icon**.  This will insert a **+** icon on the left side of the gallery, replicated for each item in the gallery.  

    > [!div class="mx-imgBorder"]
    > ![Using the Insert tool pane to add an icon control](media/function-remove-removeif/gallery-addicon.png)

1. In the top item, move the icon to the right side of the screen.
  
1. To change to a trash can icon, set the **Icon** property to the formula:

    ```powerapps-dot 
    Icon.Trash
    ```
    
    The **Icon.** prefix will not be shown unless you are actively editing the formula.

    > [!div class="mx-imgBorder"]
    > ![Changing the icon to the trash can icon](media/function-remove-removeif/gallery-icontrash.png)

1. Set the **OnSelect** property to the formula:

    ```powerapps-dot
    Remove( [@Contacts], ThisItem )
    ```

    > [!NOTE]
    > At present, we must use the [global disambiguation operator](operators.md#disambiguation-operator) [@...] to avoid a name conflict with a One-to-Many relationship on the Contacts entity.  We are working to reduce name conflicts and make this unnecessary in the future.  This is not needed if the data source has no conflicts, often the case for SharePoint lists or SQL Server tables, but the syntax does no harm either.  

    > [!div class="mx-imgBorder"]
    > ![Setting the OnSelect property of the icon control within the gallery](media/function-remove-removeif/gallery-onselect.png)

1. Hold down the Alt key and select any of the trash can icons in the gallery.  The associate contact will be removed.

    > [!div class="mx-imgBorder"]
    > ![Gallery with one of the contacts removed](media/function-remove-removeif/gallery-activateicon.png)