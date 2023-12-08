---
title: Efficient calculations in Power Apps  
description: Efficient calculations in Power Apps  
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
# Efficient calculations

Power Fx expressions are powerful and do many background calculations for you automatically. While Power Fx automates many things for you, it's possible to fine-tune your calculations so there as fast as possible. 

## Data retrieval 

### Explicit column selection
The Explicit Column Selection (ECS) feature is enabled by default for all new apps. If it isn't enabled, you should enable it. ECS automatically reduces the number of columns retrieved to only the ones that are used in the application. If ECS isn't enabled, you might be retrieving more data than you need, which can affect performance. Occasionally, when an app pulls data in through collections, the original lineage (or source) of a column can be lost. We don't know if it’s being used and will drop it via ECS. You can usually force ECS to work for a missing column by using the PowerFx expression “ShowColumns” after a collection reference or by using it in a control.

### Gallery and Form usage of images
Use Dataverse thumbnail versions of images for galleries and tables. Dataverse thumbnails are small about 1 kilobyte and are stored inline as part of the record, and are useful and fast for display on controls that show collections. **All** other image references (including all SharePoint images) require a separate call and shouldn't be placed on a gallery or table. Place images that require a separate call on detail forms. Consider never showing a full image by default. Full detailed images can be useful and important to users. However, you can make these images available to users through an explicit user action (for example, a button or navigation to a separate page). SharePoint has a range of intermediate sized images you can use for use on a form short of the full image. Dataverse only has two sizes: Thumbnail and Full.

## Calculations

### Split up formulas with App.formula
The use of App.formulas and named formulas can help with the speed of app load and page navigation because it allows Power Fx to decide when to evaluate a formula. That means it doesn't have to necessarily evaluate it in OnStart.  In addition, named formulas can generally help speed as well. In particular if you have a long script, breaking it up into named formulas allow for more efficient calculations as Power Fx can schedule the work and it enables reuse. For more information, see [App formulas](/power-platform/power-fx/reference/object-app).

### Concurrent
Use the Concurrent function to allow formulas to be executed at the same time. Carefully choose where concurrent is used. It can provide some modest speed  ups but if you're running items that depend on each other it can cause timing and throttling issues.  

### Placement of ForAll
If you have an expression with ForAll and collect that looks like this:
```powerapps-dot
ForAll(x, Collect(y, { … }))
```
Then, invert this to 
```powerapps-dot
Collect(y, ForAll(x, { … }))
```
In the first pattern, any dependent rule on collection y is notified of changes and evaluated for each iteration of x.  In the second pattern, these rules are only evaluated once.
 
### Gallery.AllItems 
When working with Power Apps, it’s best to avoid referencing Gallery.AllItems unless you need out user values. This is because every time AllItems is read, a new output table is generated. Instead, use Gallery.AllItemsCount if you just want to know how many items are loaded.

### Gallery.TemplateSize
To ensure that flexible-height galleries are rendered correctly, it’s important to set a reasonable default size. Initially, we try to render as many rows as possible based on this value. If you set the default size to 0, we try to render everything, except for a few edge cases. If you’re using a formula, make sure to set a minimum value for when the formula might evaluate to 0. For example, you could use Max(20, varFoo + rectBar.Height). This way, if varFoo and rectBar.Height aren’t yet available, we’ll at least use a reasonable value of 20.

### DelayOutput (especially for Search)
 There's one second delay before the changes are detected, which allows you to complete the typing instead of detecting the changes for every typing 



