---
title: Optimize canvas-app performance | Microsoft Docs
description: Follow the best practices in this topic to boost the performance of canvas apps that you create in Power Apps. 
author: yingchin
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 01/22/2020
ms.author: yingchin
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Tips and best practices to improve canvas apps performance

In the previous articles, you learned about the [execution phases and data call flow](execution-phases-data-flow.md), [common sources of slow performance](slow-performance-sources.md), and [common performance issues/resolutions](common-performance-issue-resolutions.md) in canvas apps. You can also benefit by following the tips, and best practices in this article to boost the performance of apps that you create.

## Limit data connections 
**Don’t connect to more than 30 data sources from the same app**. Apps prompt new users to sign in to each connector, so every 
extra connector increases the amount of time that the app needs to start. As an app runs, each connector requires CPU resources,
memory, and network bandwidth when the app requests data from that source. 

You can quickly measure your app’s performance by turning on Developer Tools in [Microsoft Edge](https://docs.microsoft.com/microsoft-edge/devtools-guide/network) or [Google Chrome](https://developers.google.com/web/tools/chrome-devtools/network-performance/) while running the app. Your app is more likely to take longer than 15 seconds to return data if it frequently requests
data from more than 30 data sources, such as Microsoft Dataverse, Azure SQL, SharePoint, and Excel on OneDrive.  

## Limit the number of controls 
**Don’t add more than 500 controls to the same app**. Power Apps generates an HTML DOM to render each control. The more controls you add,
the more generation time Power Apps needs. 

You can, in some cases, achieve the same result and have the app start faster if you use a gallery instead of individual controls. In
addition, you might want to reduce the number of control types on the same screen. Some controls (such as PDF viewer, data table, and
combo box) pull in large execution scripts and take longer to render. 

## Optimize the OnStart property
Use the [**ClearCollect**](functions/function-clear-collect-clearcollect.md) function to cache data locally if it doesn’t change during the user session. Also, use the [**Concurrent**](functions/function-concurrent.md) function to load data sources simultaneously.

As [this reference topic](functions/function-concurrent.md) demonstrates, you can
use **Concurrent** to cut the amount of time an app needs to load data in half.

Without the **Concurrent** function, this formula loads each of four tables one at a time:

```
ClearCollect( Product, '[SalesLT].[Product]' );
ClearCollect( Customer, '[SalesLT].[Customer]' );
ClearCollect( SalesOrderDetail, '[SalesLT].[SalesOrderDetail]' );
ClearCollect( SalesOrderHeader, '[SalesLT].[SalesOrderHeader]' )
```

You can confirm this behavior in the Developer Tools for your browser:

![Serial ClearCollect](./media/performance-tips/perfconcurrent1.png)
	
You can enclose the same formula in the **Concurrent** function to reduce the overall time that the operation needs:

```
Concurrent(	
	ClearCollect( Product, '[SalesLT].[Product]' ),
	ClearCollect( Customer, '[SalesLT].[Customer]' ),
	ClearCollect( SalesOrderDetail, '[SalesLT].[SalesOrderDetail]' ),
	ClearCollect( SalesOrderHeader, '[SalesLT].[SalesOrderHeader]' ))
```

With this change, the app fetches the tables in parallel: 

![Parallel ClearCollect](./media/performance-tips/perfconcurrent2.png)	

> [!NOTE]
> For more information about the performance problems and resolutions related to OnStart, read [OnStart event](common-performance-issue-resolutions.md#onstart-event-tuning).

## Cache lookup data
Use the **Set** function to cache data from lookup tables locally to avoid repeatedly retrieving data from the source. This technique
optimizes performance if the data probably won’t change during a session. As in this example, the data is retrieved from the source once,
and then, referenced locally until the user closes the app. 

```
Set(CustomerOrder, Lookup(Order, id = “123-45-6789”));
Set(CustomerName, CustomerOrder.Name);
Set(CustomerAddress, CustomerOrder.Address);
Set(CustomerEmail, CustomerOrder.Email);
Set(CustomerPhone, CustomerOrder.Phone);
```

Contact information doesn’t change frequently, and neither do default values and user information. So you can generally use this 
technique with the **Defaults** and **User** functions also. 

## Avoid controls dependency between screens
To improve performance, the screens of an app are loaded into memory only as they're needed. This optimization can be hampered if, for example, screen 1 is loaded and one of its formulas uses a property of a control from screen 2. Now screen 2 must be loaded to fulfill the dependency before screen 1 can be displayed. Imagine screen 2 has a dependency on screen 3, which has another dependency on screen 4, and so on. This dependency chain can cause many screens to be loaded.

For this reason, avoid formula dependencies between screens. In some cases, you can use a global variable or collection to share information between screens.

There's an exception. In the previous example, imagine that the only way to display screen 1 is by navigating from screen 2. Then screen 2 would have already been loaded in memory when screen 1 was to be loaded. No extra work is needed to fulfill the dependency for screen 2 and therefore there's no performance impact.

## Use delegation

Where possible, use functions that delegate data processing to the data source instead of retrieving data to the local device for processing. If an app must process data locally, the operation requires much more processing power, memory, and network bandwidth, especially if the data set is large.

> [!TIP]
> To learn about delegable functions supported by specific connectors, refer to the [Connector documentation](https://docs.microsoft.com/connectors/).

For an example of delegable functions, consider an ID column defined as Number data type in the SharePoint list. Formulas in the following example will return the results as expected. However, the former is non-delegable while the latter is delegable.

| Formula                                           | Delegable? |
|---------------------------------------------------|------------|
| `Filter (‘SharePoint list data source’, ID = 123 )` | Yes        |
| `Filter(‘SharePoint list data source’, ID ="123")`  | No         |

As we assume that the ID column in SharePoint is defined with the data type of Number, the right-hand side value should be numeric variable instead of string variable. Otherwise, such mismatch may trigger the formula to be non-delegable.

Use of non-delegable functions, and inappropriate data row limit for non-delegable functions can have adverse effect on the performance of the app.

For more information about delegation, and data row limits for non-delegable queries, go to [Delegation](delegation-overview.md#non-delegable-limits).

## Use Delayed Load
Turn on the [experimental feature](working-with-experimental.md) for Delayed Load if your app has more than 10 screens, no rules, and many controls that are on multiple screens and that are directly bound to the data source. If you build this type of app and don’t enable this feature, app performance may suffer because the controls in all screens must be populated even on screens that aren’t open. Also, all screens of the app must be updated whenever the data source changes, such as when the user adds a record.

## Working with large data sets
Use data sources and formulas that can be delegated to keep your apps performing well while users can access all the information they need, and avoid hitting the data row limit of 2000 for non-delegable queries. For data-record columns on which users can search, filter, or sort data, those indexes of columns are designed well as these docs describe for [SQL Server](https://docs.microsoft.com/sql/relational-databases/sql-server-index-design-guide) and [SharePoint](https://support.office.com/article/Add-an-index-to-a-SharePoint-column-f3f00554-b7dc-44d1-a2ed-d477eac463b0).

> [!NOTE]
> For additional information about how large data sets can cause common performance problems on different platforms, read [Large data sets loading slowly on different platforms](common-performance-issue-resolutions.md#large-data-sets-loading-slowly-on-different-platforms).

## Republish apps regularly
[Republish your apps](https://powerapps.microsoft.com/blog/republish-your-apps-to-get-performance-improvements-and-additional-features/) (blog post) to get performance improvements and more features from the Power Apps platform.

## Avoid repeating the same formula in multiple places
If multiple properties run the same formula (especially if it's complex), consider setting it once and then referencing the output of the first property in subsequent ones. For example, don't set the **DisplayMode** property of controls A, B, C, D, and E to the same complex formula. Instead, set A's **DisplayMode** property to the complex formula, set B's **DisplayMode** property to the result of A's **DisplayMode** property, and so on for C, D, and E.

## Enable DelayOutput on all Text input controls
If you have multiple formulas or rules that reference the value of a **Text input** control, set the **DelayedOutput** property of that control to true. The **Text** property of that control will be updated only after keystrokes entered in quick succession have stopped. The formulas or rules won't run as many times, and app performance will improve.

## Avoid using Form.Updates in rules and formulas
If you reference a user-input value in a rule or a formula by using a `Form.Updates` variable, it iterates over all the form’s data cards and creates a record each time. To make your app more efficient, reference the value directly from the data card or the control value.

## Next steps
Review the [coding standards](https://aka.ms/powerappscanvasguidelines) for maximizing app performance and keeping apps easier to maintain.

### See also

[Understand canvas apps execution phases and data call flow](execution-phases-data-flow.md) <br>
[Common canvas app performance issues and resolutions](common-performance-issue-resolutions.md) <br>
[Possible sources of slow performance for canvas apps](slow-performance-sources.md) <br>
[Common issues and resolutions](common-issues-and-resolutions.md) <br>
[Troubleshooting startup issues for Power Apps](../../troubleshooting-startup-issues.md)
