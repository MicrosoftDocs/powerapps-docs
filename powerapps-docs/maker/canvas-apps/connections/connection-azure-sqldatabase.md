---
title: Connect to Azure SQL Server from Power Apps
description: Learn how to connect to Azure SQL or an on-premises SQL Server database.
author: lancedMicrosoft

ms.topic: reference
ms.custom: canvas
ms.date: 10/25/2024
ms.subservice: canvas-maker
ms.author: lanced
ms.reviewer: mkaur
search.audienceType: 
  - maker
contributors:
  - mduelae
  - lancedmicrosoft
---

# Connect to SQL Server from Power Apps

You can connect to SQL Server in either Azure or an on-premises database.

> [!NOTE]
> Newly created SQL data sources are no longer prefixed with `[dbo]` like in previous versions of Power Apps.
>
> For more information, see [Common issues and resolutions for Power Apps](/troubleshoot/power-platform/power-apps/common-issues-and-resolutions).

## Generate an app automatically

Depending on which Power Apps interface you're using, reference the [new look](../intro-maker-portal.md?tabs=home-new-look) or the [classic look](../intro-maker-portal.md?tabs=home-classic) to build an app.



## Access data and view results

You can add a data source to your app, using views or stored procedures. Learn more in [Methods to access data](sql-methods-to-access-data.md).

Once connected, you can filter your data by accessing the results from a stored prodecure. Learn more in [Methods to view results](sql-method-to-access-results.md).

## Work with a gallery

You can access a stored procedure for the **Items** property of a gallery after you declare it safe for the UI. Reference the data source name and the name of the stored procedure followed by 'ResultSets'. You can access multiple results by referencing the set of tables returned such as Table 1, Table 2, etc.

For example, your access of a stored procedure off of a data source named 'Paruntimedb' with a stored procedure named 'dbo.spo_show_all_library_books()' will look like the following.

```power-fx
Paruntimedb.dbospshowalllibrarybooks().ResultSets.Table1
```

This populates the gallery with records. However, stored procedures are an addition of **action** behaviors to the tabular model. Refresh() only works with tabular data sources and can't be used with stored procedures. Then you need to refresh the gallery when a record is created, updated, or deleted. When you use a Submit() on a form for a tabular data source, it effectively calls Refresh() under the covers and updates the gallery.

To get around this limitation, use a variable in the OnVisible property for the screen and set the stored procedure to the variable.

```power-fx
Set(SP_Books, Paruntimedb.dbospshowalllibrarybooks().ResultSets.Table1);
```

And then set the 'Items' property of the gallery to the variable name.

```power-fx
SP_Books
```

Then after you create, update, or delete a record with a call to the stored procedure, set the variable again. This updates the gallery.

```power-fx
Paruntimedb.dbonewlibrarybook({   
  book_name: DataCardValue3_2.Text, 
  author: DataCardValue1_2.Text,
    ...
});
Set(SP_Books, Paruntimedb.dbospshowalllibrarybooks().ResultSets.Table1);
```

## Known issues

### SQL data sources no longer add a `[dbo]` prefix to the data source name

The `[dbo]` prefix doesn't serve any practical purpose in Power Apps as data source names are automatically disambiguated. Existing data sources aren't affected by this change, but any newly added SQL data sources don't include the prefix.

If you need to update a large number of formulas in one of your apps, the [Power Apps Source File Pack and Unpack Utility](https://powerapps.microsoft.com/blog/source-code-files-for-canvas-apps/) can be used to do a global search-and-replace.

> [!NOTE]
> Starting in version 3.21054, we'll automatically update broken legacy name references to the new data source name after reading the data source.

## Next steps

- Learn how to [show data from a data source](../add-gallery.md).
- Learn how to [view details and create or update records](../add-form.md).
- See other types of [data sources](../connections-list.md) to which you can connect.  
- [Understand tables and records](../working-with-tables.md) with tabular data sources.

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
