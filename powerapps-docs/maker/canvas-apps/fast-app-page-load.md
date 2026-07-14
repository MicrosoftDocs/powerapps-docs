---
title: Speed up app or page load in Power Apps  
description: Optimizing app and page loading for peak performance in Power Apps.
author: lancedMicrosoft
ms.subservice: canvas-developer
ms.topic: how-to
ms.date: 01/05/2024
ms.author: lanced
ms.reviewer: mkaur
search.audienceType:
  - maker
contributors:
  - lancedMicrosoft
  - mduelae
  
---
# Optimize app or page load for peak performance

One of the key factors that shape a user's perception of an app is how quickly it opens and becomes functional. Therefore, prioritizing this goal is crucial in building a performant app. To achieve optimal app performance, there's three main areas that require attention:

1. Load data fast
2. Efficient calculations
3. Minimizing required resources

Each of these areas has several common anti-patterns.

## Load data fast

Follow these guidelines to achieve fast data loading apps.

### Avoid directly populating a collection with large amounts of data
Sometimes authors use ClearCollect() to copy data from a server to a collection in their app. This practice is a work-around for delegation limitations in the source or because they plan to use collections in the app for other purposes. Using ClearCollect() can potentially increase the speed of the app when the collection is later utilized. However, it's important to exercise caution while implementing it. Using ClearCollect in this manner can lead to slower app load times or when navigating between pages. ClearCollect() must finish before you can see the data in a gallery or a table. This step can take a long time if there's lots of data or if you use this approach for too many data sources. Collections are best used for situations where the data is small and you need to do many calculations on the collection. For example, a good use of collections is an Online order basket. The customer may update and remove items several times before choosing to commit the order.  Additionally, you may augment the collection with more data items like potential discounts, highlights, etc. Data that is 'read-only' should be accessed natively - without bringing it into a collection.

### Consider avoiding calling Power Automate to populate a collection
This issue is a slight variation of the previous section. Sometimes authors also use Power Automate to populate their collection in Power Apps. There's approximately a 0.6-second performance cost to instantiate Power Automate. Power Automate must be independently launched each time it's called. It must allocate memory, get situated with the right components, and be ready to run.  As with the above advice, one or two calls to Power Automate might not be an issue depending on your app. But, almost universally, the worst performing apps overuse this approach. The performance cost can add up quickly and ruin the performance of your app.

### Avoid using SaveData() and LoadData() as a full offline scenario
Some authors use ClearCollect() and then SaveData() to store data for general purpose offline use. You can use SaveData() to save the collection to your device, and LoadData() to load it when you're offline. However, this approach isn't recommended for instances where there's a large amount of data or if the data is complex. It makes your app slower because it has to wait for ClearCollect() to finish before it can show the data. You should only use SaveData() and LoadData() for small and simple data scenarios such as preferences and short lists. A better way to work with large amounts of offline data is to use the Power Apps offline feature that works with Dataverse. This feature can handle larger and more complex data more efficiently.

### Use Explicit column selection
Explicit column selection is on by default. However, some authors turn this feature off. The issue is that with Explicit column selection (ECS) turned on, columns are sometimes not retrieved from the data source if the data is first retrieved into a collection. As some tables may have many columns, ECS automatically computes which columns are necessary to retrieve based on their usage in controls (for example, galleries and forms.) As some tables can many columns, reducing the size of the download can speed up performance. Some tables can have a hundred columns or more. If your app only needs to use 10 columns, and you bring down all the columns from a 100 column table, you are bringing down ten times as much data as you actually need.

Most issues arise when bringing data into collections. If a column is explicitly referenced in a control then ECS works well.  And, ECS generally does work for collections. However, the column lineage is occasionally lost when the data moves through collections and variables.  And, and so Power Apps may lose track of the column it should retrieve. To resolve this issue, you can force Power Apps to "remember" the column by using the `ShowColumns` function. For example:

```power-fx
    ClearCollect(
        MyColTable, 
        ShowColumns(Filter(BankAccounts, AcountNo = 32),
        "Col1", 
        "Col2", 
        "Col3")
    );
```

   Where `Col1`, `Col2`, and `Col3` are columns you expect to be retrieved from the data source (for example, the `Account` data source).

   Alternatively, you can add a hidden control to your form that references the column. This forces Power Apps to "remember" the column.

## Fast calculations
Fast (or efficient) calculations are a performance goal in its own right. For more information, see [Fast (efficient) calculations](efficient-calculations.md). However there are some common anti-patterns that can affect app load as well and so we discuss them here. Below is a list of  optimizations you should consider that might affect app launch or page navigation.

### Use App.Formulas
Historically many authors have put a large number of calculations in OnStart. When you place an expression in OnStart, it forces Power Apps to run that expression precisely when the app starts and before everything else. However, with the introduction of App.Formulas you can let Power Apps decide when to run an expression. Power Apps can run the formula 'Just-in-time' before it's needed. For more information, see [App formulas](/power-platform/power-fx/reference/object-app). Use App.Formulas to split up your formula into pieces that Power Apps can arrange more efficiently for execution. 

### Use Concurrent
Use the Concurrent function to allow formulas to be executed at the same time. It's common to use this function to populate collections as it allows for parallel execution. While this can provide some modest speed ups, adding many data sources can cause timing and throttling issues.  

### Use Enhanced performance for hidden controls
When enabled by default in all new apps created since December 2022, Power Apps doesn't render any control that isn't initially visible.

## Minimize required resources
Minimize the resources required to launch your app or screen. This effort includes carefully scoping or partitioning the resources your app or screen needs. Below are several approaches to help you. 

### Use a low dependency start screen and eliminate unused screens.
Use a low-dependency first screen such as a welcome on your application. Create a screen that doesn't load a gallery or table or reference data. This manages the user's perception of speed and allow Power Fx to properly delay some calculations to later. If you have any unused screens, remove them. 

### Keep cross screen dependencies between screens low
Cross page references force the load of additional pages via references, for example, referencing controls on pages and putting into collections. Some references might be unavoidable.  Centralize common references to a single page if possible so that only page is loaded.

### Consider embedded media
Authors sometimes embed media in their apps to ensure fast loading. If you have embedded media consider whether or not, you're using it.  If not, delete it. If you have embedded a .png file, consider substituting a .svg file which is smaller. Note that if you use a .svg, the font for the .svg must be on the client machine. Consider the embedded media resolution. Is it too high for the device it will used on?

### Don't forget App.StartScreen
If you use App.StartScreen, ensure the first screen is a blank screen.  Due to current packaging of the app, the first logical screen is always bundled with the app init logic and will get initialized, regardless of whether we ever navigate to it.

### Consider splitting up the app
If your app is large, consider partitioning it into smaller apps. If the functionality is separate enough in different parts of your app, this approach might work. In this scenario, you create an actual separate app that you launch with parameters that include context from the first or parent app.  



## Suggestions
To achieve the goal of a fast app and page start, consider the following questions and suggestions:

1. Are you loading lots of data in a first screen?  Can you use a different first screen? 
1. Are you running many commands or Power Fx expressions at the beginning of the app load? Can you defer these commands and expressions to a later point in the application? Only get the data you actually need to start the app? 
1 Can you convert expressions in App.OnStart to named formulas with App.Formulas?  This allows Power Fx to decide when to actually execute the formula rather than forcing it to happen on load or navigate events. 
1. Can you use a separate Power Automate flow to create a temporary table in a local data store such as Dataverse that combines data from different sources? And then access that data in your Power App? 
1. For business process kick offs, can you use Server triggered actions rather than calling a Power Automate Flow?
1. Can you create a view on the server that joins the data for you?
1. If you want to use offline data in your app, can you use the Power Apps offline feature that works with Dataverse? If your data isn't in Dataverse, can you move it there?

 
