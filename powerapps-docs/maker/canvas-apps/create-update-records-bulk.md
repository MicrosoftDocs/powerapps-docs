---
title: Create or update bulk records in a canvas app | Microsoft Docs
description: Learn about how to create or update bulk records in canvas apps.
author: denisem-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 02/17/2021
ms.author: denisem
search.audienceType:
  - maker
search.app:
  - PowerApps
contributors:
  - denisem-msft
  - tapanm-msft
  - gregli-msft
---

# How to bulk update records in Power Apps

The following formulas can be used to bulk update records in Power Apps Canvas applications based on the situation in an application:
- [Patch() function](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/functions/function-patch#modify-or-create-a-set-of-records-in-a-data-source-1) - Use this when the collection matches the data source
    ```
    Patch( DataSource, Collection )
    ```
- [ForAll() function](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/functions/function-forall) + [nested Patch()](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/functions/function-patch) + [Disambiguation Operator](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/functions/operators#disambiguation-operator) - Use when the data sources have different columns that you need to join.
    ```
    ForAll( Collection,
        Patch( DataSource, 
            LookUp( DataSource, Id = Collection[@Id] ),
            { Column: Value }
        )
    )
    ```

- [AddColumns()](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/functions/function-table-shaping) Can be used to provide a lookup reference in the Collection that contains the updates to the DataSource if it does not have fields that easily reference the table. 

## Example
Assume you have a checklist of tasks. When you are done with a few tasks you can mark them as complete. You could extend this scenario to a Product Launch checklist, Home Inspection checklist, et cetera.
- I've created a simple checklist where I can check off tasks related to my blogging or posting on social media. 
- I'll not get into the details of building the app here. 
- Below is the excel screenshot containing the Checklist items. My table on the excel is called as `ChecklistItems`. You can find the excel [here](https://blogcode.blob.core.windows.net/pablogassets/BulkUpdate_blog/Bulkupdate_blog.zip).
- I'm using Collections to demo this. The approach works for any tabular backend of your choice.

    ![alt text](./media/bulk-update-records-1.png)

I've imported excel data as static data into my PowerApps application. On the `App.OnStart` property, `Collect()` the excel ChecklistItems data into `ChecklistItemsSource` collection. Throughout the application we will use the `ChecklistItemsSource` as the source data.

This example uses a 2 screen application:
- Screen 1: Used to review the checklist items and mark them as complete.
- Screen 2: Used to create a new checklist item. The new item will be added to `ChecklistItemsSource` collection.

    ![Screen1](./media/bulk-update-records-2.jpg) ![Screen2](./media/bulk-update-records-2.jpg)

Every time a checklist item is checked, we add it into a collection `CheckedItems` using the below formula on the `OnCheck` event property of the Checkbox control. If the item is already checked and is part of the collection, it is removed. Else the checked item is added. You can toggle the status between Done and Pending, or on the `Oncheck` and `OnUncheck` events as well.
```
If( !IsBlank( 
        LookUp( CheckedItems, Id = ThisItem.Id )
    ),
    Remove( CheckedItems, ThisItem ),
    Collect( CheckedItems, ThisItem )
)
```

## Solutions

There are different ways of bulk updating records depending on the scenario. Below are details on creating multiple records at once in canvas apps.

When the user clicks Done in the above scenario, we need to update `ChecklistItemsSource` with changes from CheckedItems collection.

### Using Patch:

If your Source and Destination have the same column names, you can use a simple Patch statement. `ChecklistItemsSource` and the `CheckedItems` collections, have the same column names. Hence you can use the below formula to update the source at once with all the changes.
```
Patch( ChecklistItemsSource, CheckedItems )
```
### Using ForAll and Patch:

If the columns in source and destination tables vary, use ForAll with Patch instead.

With `ForAll()`, you must loop through each record using a condition. The condition is a comparison between similar columns (e.g. `Id` column) of the different tables. This comparison becomes complicated when the source table and the destination table have the same column names (e.g. if `ProjectId` was a column found in both `Project` and `PurchaseOrder` tables). Let's look at a few examples on how to achieve this easily.
<br>

#### 1. With disambiguation operator:

To update the `Status` of `CheckedItems` to "Done", when the source and destination table column names are the same, use this formula:
```
ForAll( CheckedItems,
    Patch( ChecklistItemsSource, 
        LookUp( ChecklistItemsSource, Id = CheckedItems[@Id] ),
        { Status: "Done" }
    )
)
```
For each item in the `CheckedItems` collection, we compare its Id (represented by the disambiguation operator `CheckedItems[@Id])` against the Id column of `ChecklistItemsSource` collection and update each matched record with the Status as "Done". The disambiguation operator is used when two columns belonging to different tables have the same name. If you don't use this disambiguation operator you will observe that only the first record gets updated.

#### 2. Using an additional label within the gallery

If you don't want to use an additional collection to store the checked items, you can try the following:
1. Create an additional label within the gallery template, bind it to the Id column and rename the label to IdText.

1. Remove the code on the Oncheck of the checkbox control mentioned above.

1. Write the following formula on the OnSelect event of the Done Button:
      ```
      ForAll(
          Filter( ChecklistGallery.AllItems,
            StatusCheckbox.Value = true
          ),
          Patch( ChecklistItemsSource,
            LookUp( ChecklistItemsSource, Id = IdText.Text ),
            { Status: "Done" }
          )
      )
      ```
1. Here, you are directly applying the filter on the Gallery's items to find the checked items, and for each record in the filtered items, we find a match on the ChecklistItemsSource table by comparing the Id with value stored in IdText label. 
1. Finally, we update the status to "Done".

The Disambiguation operator cannot be used on the Gallery's items. Hence, we can store a label within the gallery and reference it for comparison.

<!--@Vasavi can we remove this sction or add more detail on what you mean?-->
#### 3. With AddColumns:
This is an alternative to using the Disambiguation operator or a label inside gallery.

While creating a local copy of your data source, you can use `AddColumns()` formula to create a new column with a different label (`NewId`) for the Id column in your source collection. When using ForAll with patch, you compare the NewId column, against the Id column in your source data.

## Bulk create records
We have already tackled the hard problem of bulk updating records. We do generally see a need to create new records in bulk. For example, when you are app has to click some images and you may want to upload them all at once.

Let's see how this can be achieved with the example of Checklist items above.

On the Checklist Create screen, each time you click Add, store the information in `NewChecklistItems` collection. And on Submit, use `ForAll()` with `Patch()` to update the Source collection.
```
ForAll( NewChecklistItems,
    Patch( ChecklistItemsSource,
        Defaults( ChecklistItemsSource ),{
            Id: Id,
            Category: Category,
            Description: Description,
            Status:Status
        }
    )
)
```
For each item in the `NewChecklistItems`, we are creating a new record (indicated by `Defaults(ChecklistItemsSource)`) in the `ChecklistItemsSource` collection. The `Id` is set to the `Id` from the `NewChecklistItems` collection. Similarly, `Category`, `Description`, and `Status` values are set.

## Summary

In this blog, I'm not writing a lot of details on building the application but just concentrating on the key formulas to bulk update records. You can download all the related files [here](https://blogcode.blob.core.windows.net/pablogassets/BulkUpdate_blog/Bulkupdate_blog.zip).

### Key points:

- Use `Patch()`, when source and destination columns names are same.
- Disambiguation operator [@] on the comparison column to differentiate the source and local data column name. Make sure to use this when using `ForAll()` if you run into an issue where only the first record gets updated.
- Store the comparison key in a label control in the gallery to reference the local data.
- Use `AddColumns()` to rename the Comparison Key column name on your local data.
