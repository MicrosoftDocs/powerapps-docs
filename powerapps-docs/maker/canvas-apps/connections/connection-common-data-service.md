---
title: Connect to Microsoft Dataverse
description: Learn how to connect to Microsoft Dataverse and use it for building apps in Power Apps.
author: mduelae
ms.topic: reference
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 06/19/2025
ms.subservice: canvas-maker
ms.author: lanced
search.audienceType: 
  - maker
contributors:
  - mduelae
  - lancedmicrosoft
---

# Connect to Microsoft Dataverse

Securely store your business data in Dataverse and build rich apps in Power Apps so users can manage that data. You can also integrate that data into solutions that include Power Automate, Power BI, and data from Dynamics 365.

By default, the app connects to the current environment for Dataverse tables. If your app moves to another environment, the connector connects to data in the new environment. This behavior works well for an app that uses a single environment or follows an application lifecycle management (ALM) process for moving from development, to test, and then to production.

When you add data from Dataverse, change the environment, and then select one or more tables. By default, the app connects to data in the current environment.

![Default environment.](media/connection-common-data-service/common-data-service-connection-change-environment.png)

If you select **Change environment**, specify a different environment to pull data from instead of, or in addition to, the current environment.

![Other environments.](media/connection-common-data-service/common-data-service-connection-select-environment.png)

The name of the selected environment appears under the tables list.

![New environments.](media/connection-common-data-service/common-data-service-connection-after-change-environment.png)

## Visibility and access

When you select **Change environment**, you see a list of environments. Even if you see an environment in the list, the security roles in the environment control what you can do there. For example, if you don't have read privileges, you can't see the tables and records in the environment.

> [!NOTE]
> Connections listed in the app details pane outside of the app designer show connections that need user consent. Because native Dataverse connections used in the app don't need additional consent, a native connection isn't in that list.


## Power Apps data type mappings

The Microsoft Dataverse connector is more robust than the Dynamics 365 connector and is approaching feature parity. The following table lists the data types in Power Apps and how they map to data types in Dataverse.

| Power Apps | Microsoft Dataverse |
| --- | --- |
| Choice | Choice, Yes/No |
| DateTime | Date Time, Date and Time, Date Only |
| Image | Image |
| Number | Floating Point Number, Currency, Decimal Number, Duration, Language, TimeZone, Whole Number |
| Text | Email, Multiline Text, Phone, Text, Text Area, Ticker Symbol, URL |
| Guid | Unique Identifier |

## Power Apps delegable functions and operations for Dataverse

These Power Apps operations, for a given data type, can be delegated to
Dataverse for processing instead of processing locally within Power Apps.

| **Item**                                                        | **Number [1]** | **Text [2]** | **Choice** | **DateTime [3]** | **Guid** |
|-----------------------------------------------------------------|----------------|--------------|------------|------------------|----------|
| \<, \<=, \>, \>=                                                | Yes            | Yes          | No         | Yes              | \-       |
| =, \<\>                                                         | Yes            | Yes          | Yes        | Yes              | Yes      |
| And/Or/Not                                                      | Yes            | Yes          | Yes        | Yes              | Yes      |
| CountRows [4] [5], CountIf [6]                                  | Yes            | Yes          | Yes        | Yes              | Yes      |
| Filter                                                          | Yes            | Yes          | Yes        | Yes              | Yes      |
| First [7]                                                       | Yes            | Yes          | Yes        | Yes              | Yes      |
| In (membership) [8]                                             | Yes            | Yes          | Yes        | Yes              | Yes      |
| In (substring)                                                  | \-             | Yes          | \-         | \-               | \-       |
| IsBlank [9]                                                     | Yes            | Yes          | No         | Yes              | Yes      |
| Lookup                                                          | Yes            | Yes          | Yes        | Yes              | Yes      |
| Search                                                          | No             | Yes          | No         | No               | \-       |
| Sort                                                            | Yes            | Yes          | Yes        | Yes              | \-       |
| SortByColumns                                                   | Yes            | Yes          | Yes        | Yes              | \-       |
| StartsWith                                                      | \-             | Yes          | \-         | \-               | \-       |
| Sum, Min, Max, Avg [6]                                          | Yes            | \-           | \-         | No               | \-       |
| UpdateIf/RemoveIf [10]                                          | Yes            | \-           | \-         | No               | \-       |

### Notes
1.  Numeric with arithmetic expressions (for example, `Filter(table, field + 10 > 100)`) aren't delegable. Language and TimeZone aren't delegable. Casting a column to a number isn't supported. If a value appears as a number in Power Apps but the backend data source isn't a simple number, such as currency, then it isn't delegated.
2.  Doesn't support Trim[Ends] or Len. Supports other functions like Left, Mid, Right, Upper, Lower, Replace, and Substitute. Also, casting such as Text(column) isn't supported for delegation.
3.  DateTime is delegable except for DateTime functions Now() and
    Today().
4.  CountRows on Dataverse uses a cached value. For non-cached values where the record count is under 50,000 records, use `CountIf(table, True)`.
5.  For CountRows, ensure that users have appropriate permissions to get totals for the table. 
6.  All aggregate functions are limited to a collection of 50,000 rows. If needed, use the Filter function to select 50,000 rows. Aggregate functions aren't supported on views.
7.  The FirstN function isn't supported.
8.  The `In` operator is subject to the 15-table query limit of Dataverse.
9.  Supports comparisons. For example, `Filter(TableName, MyCol = Blank())`.
10. UpdateIf and RemoveIf work locally but simulate delegation to a limit of 500 or 2,000 records. They successively bring down records beyond the nondelegation 500 or 2,000 record limit. Records that meet the If condition are collected. Generally, a maximum of 500 or 2,000 records are collected separately and then changed per execution. However, more records can be updated if the existing local data cache is large because the function can access more records for evaluation.

## Call Dataverse actions directly in Power Fx

As part of the Power Fx language, you can now directly invoke a Dataverse action within a formula. Both unbound and bound actions are supported. Add a Power Fx `Environment` language object to your app to use Dataverse actions.

You can work with dynamic fields for both inputs and outputs. For inputs, many Dataverse actions require a dynamic value as an argument. Pass these arguments by using ParseJSON to convert a Power Fx record into a dynamic value. For outputs, if an action returns dynamic values, just use dot notation to access object properties. Cast specific values for use in Power Apps, such as in a label.

Before this feature, you often used Power Automate to call Dataverse directly. Calling Dataverse from Power Fx gives you significant performance benefits and is easier to use, so use this approach for direct transactional reads and updates. If your app uses Power Automate to call Dataverse actions, you see a banner suggesting you use this direct action approach instead.

Working with dynamic fields isn't limited to Dataverse. This feature works with all types of connectors and provides basic ad hoc dynamic schema support.

> [!NOTE]
> 1. DV actions aren't fully supported in Power Fx commanding (for any action call with parameters).
> 2. Direct references to an entity or entity collections aren't supported.
> 3. For parameters of object type that are nested two or more levels deep, Power Apps treats the second-level attributes as required.

### Enable access to Microsoft Dataverse actions

For new apps, this feature is automatically enabled. For apps you created earlier, enable access to Dataverse actions.

For older apps, open your canvas app for editing. Go to **Settings** > **Upcoming features** > **Retired**, and enable Dataverse actions.

### Add the Power Fx Environment language object to your app

To use Dataverse actions in your Power Fx formulas, select **Add data**, search for **Environment**, and add it to your app.

![Screenshot of searching for the Power Fx Environment object in the Add data pane.](media/connection-common-data-service/common-data-service-connection-search-for-environment.png)

This step adds the Power Fx `Environment` language object to your app.

![Screenshot of the Power Fx Environment object as a data source in the app.](media/connection-common-data-service/common-data-service-connection-environment-object-added.png)


### Access Dataverse actions

After you add the Power Fx `Environment` object to your app, access Dataverse actions by adding `Environment` to your formula and then using dot notation for the actions.

![Screenshot of using the Power Fx Environment object in a formula.](media/connection-common-data-service/common-data-service-connection-using-the-Envrionment-PowerFx-object.png)

Unbound Dataverse actions are at the same level as tables and need the parent scope of the **Environment** language object. All actions in your environment are available—both system and custom. Both bound and unbound actions are available. The two-level call limit is removed.

![Screenshot of using a Dataverse action connected to a button.](media/connection-common-data-service/common-data-service-connection-hooking-up-an-action-to-a-button.png)

For more details on how to use Dataverse actions in your formulas, see [Working with dynamic values](../untyped-and-dynamic-objects.md).

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]

### Pass entity type arguments for bound and unbound actions

To pass entity type arguments for Dataverse actions, set the entity type argument value to a variable. Make sure to fill in any missing values, such as ***activityId**. This step is important for entities that don't have defined types in the swagger.

```power-fx
Set(MyArgVar, {
  name: First(systemUser).name,
  Id: First(systemUser).Id
  ... })
```

### Rename, refresh, and use actions in other environments

To rename an Environment, select the ellipses and then select "Rename". If you add a new Dataverse action in Dataverse and want Power Apps to see it, select "Refresh". To use an action in a different environment, change the environment, then search for 'Environment', select it, and add it to your app.  
