---
title: Speed up app or page load in Power Apps  
description: Optimizing app and page loading for peak performance in Power Apps.
author: lancedMicrosoft
ms.subservice: canvas-developer
ms.topic: article
ms.date: 12/01/2023
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

### Populating a collection instead of direct access as a data source
Sometimes authors use ClearCollect() to copy data from a server to a collection in their app. This is done to work around delegation limitations in the source or because they plan to use collections in the app for other purposes. Although, using ClearCollect() can potentially increase the speed of the app when the collection is later utilized, it's important to exercise caution while implementing it. Using ClearCollect in this manner can lead to slower app loading times at the start or when navigating between pages. ClearCollect() must finish before you can see the data in a gallery or a table. It can take a long time if there's lots of data or if you use this approach for too many data sources. If the amount of data is small and if there's only one or two data sources, it might meet your performance needs.  

### Populating a collection with Power Automate
This is a slight variation of the previous article. Sometimes authors also use Power Automate to populate their collection in Power Apps. There's approximately a 0.6-seconds performance cost to instantiate Power Automate. Power Automate must be independently launched each time it's called. It must allocate memory, get situated with the right components, and be ready to run.  As with the above advice, one or two calls to Power Automate might not be an issue (depending on your app) but poor performing apps use this approach for all their data sources. The performance cost adds up and can quickly ruin the performance of your app. 

### SaveData and Load data as a full offline scenario
Some authors use ClearCollect() and SaveData() to store data for general purpose offline use. You can use SaveData() to save the collection to your device, and LoadData() to load it when you're offline. However, this approach isn't recommended for instances where there's a large amount of data or if the data is complex. It makes your app slower because it has to wait for ClearCollect() to finish before it can show the data. You should only use SaveData() and LoadData() for small and simple data scenarios such as preferences and short lists. A better way to work with large amounts of offline data is to use the Power Apps offline feature that works with Dataverse. This feature can handle larger and more complex data more efficiently. 

## Efficient calculations
Efficient calculations are a performance goal in its own right. For more information, see [Efficient calculations](efficient-calculations.md). However there are some common anti-patterns that can affect app load as well and so we discuss them here. Below is a list of  optimizations you should consider that might affect app launch or page navigation.

### App Formulas
Historically many authors have put a large number of calculations in OnStart. When you place an expression in OnStart, it forces Power Apps to run that expression precisely when the app starts and before everything else. However, with the introduction of App.Formulas you can let Power Apps decide when to run an expression.  PowerApps can run the formula 'Just-in-time' before it's needed. For more information, see [App formulas](/power-platform/power-fx/reference/object-app). Use App.Formulas to split up your formula into pieces that Power Apps can arrange more efficiently for execution. 

### Concurrent
Use the Concurrent function to allow formulas to be executed at the same time. It's common to use this function to populate collections as it allows for parallel execution. While this can provide some modest speed ups, adding many data sources can cause timing and throttling issues.  

### Enhanced performance for hidden controls
When enabled (by default in all new apps created since Dec '22), Power Apps doesn't render any control that isn't initially visible.

## Minimize required resources
Minimize the resources required to launch your app or screen. This includes carefully scoping or partitioning the resources your app or screen needs. Below are several approaches to help you. 

### Use a low dependency start screen
Use a low-dependency first screen (for example, welcome … ) in your application. Create a screen that doesn't load a gallery or table or reference data. This manages the user's perception of speed and allow Power Fx to properly delay some calculations to later. 

### Keep cross screen dependencies between screens low
Cross page references force the load of additional pages via references (for example, referencing controls on pages and putting into collections). Some references might be unavoidable.  Centralize common references to a single page if possible so that only page is loaded - and can be referenced by other screens as well.  

### App.StartScreen
If you use App.StartScreen, ensure the first screen is a blank screen.  Due to current packaging of the app, the first logical screen is always bundled with the app init logic and will get initialized, regardless of whether we ever navigate to it.

### Split up the app
If your app is large, consider partitioning it into smaller apps. If the functionality is separate enough in different parts of your app, this approach might work. In this scenario, you create an actual separate app that you launch with parameters that include context from the first / parent app.  



## Suggestions
To achieve the goal of a fast app and page start, consider the following questions and suggestions:

1. Are you loading lots of data in a first screen?  Can you use a different first screen? 
1. Are you running many commands or Power Fx expressions at the beginning of the app load? Can you defer these commands and expressions to a later point in the application? Only get the data you actually need to start the app? 
1 Can you convert expressions in App.OnStart to named formulas with App.Formulas?  This allows Power Fx to decide when to actually execute the formula rather than forcing it to happen on load or navigate events. 
1. Can you use a separate Power Automate flow to create a temporary table in a local data store such as Dataverse that combines data from different sources? And then access that data in your Power App? 
1. For business process kick offs, can you use Server triggered actions rather than calling a Power Automate Flow?
1. Can you create a view on the server that joins the data for you?
1. If you want to use offline data in your app, can you use the Power Apps offline feature that works with Dataverse? If your data isn't in Dataverse, can you move it there?

 