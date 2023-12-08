---
title: Overview on how to create performant Power Apps  
description: Learn about how to create well performing Power Apps.
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
# Create performant apps - overview

## How and why to use performant patterns and avoiding anti-patterns.
### App patterns and the Power App productivity gain. 
Power Apps uses well-known enterprise app patterns to make development of enterprise-grade apps easier for you. An app pattern is the way you use the various Power Apps elements (such as data sources, collections, controls, Power Automate, and pages.) Power Apps builds key performant capabilities right into Power Apps so that low-code developers can quickly turn out enterprise grade working apps. Deployment and Power Apps administration tasks are simple as well. There’s a lot you don’t need to think about anymore as Power Apps makes you and your development team much more productive. 

### Power Apps steers towards performant patterns. 
The default Power Apps behaviors guide you towards well known performant patterns. Examples of these key patterns include efficiently loading data at startup, paging data incrementally to the app automatically, caching data for collections, and only loading what is necessary for given page. These are patterns that work well for data intensive enterprise applications. And, there's successful Power Apps following these patterns that use over a hundred tables and over 50 screens with good performance.  

### Falling into anti-patterns. 
As with all app development platforms it’s possible to build an app that works against you. These “anti-patterns” can result in slow apps that take a long time to load, transition between pages, or update and / or retrieve data. Examples include bringing down too much data, transforming everything into collections, and overloading OnStart. It’s most common to fall into these patterns when you're trying to work around a perceived or real limitation in Power Apps.  While we try to guide you to the best patterns automatically, it’s possible to inadvertently use a bad app pattern and end up with a poorly performing app. 

## Four key performance design principles.
Below are four key performance principles to consider while building your app. These principles aren't completely independent of each other so you'll find some performance suggestions repeated in different sections. To best understand these topics, it also is useful to understand the [Execution phases of a Power App](execution-phases-data-flow.md) article. If you have an existing app that doesn't perform well, use the principles below to examine your app.  

Each of the principles below links to a page with greater detail on the subject.

1.	[Optimize page loads](fast-app-page-load.md). Optimize your apps for app and page load speed. Minimize, delay, or eliminate actions that prevent fast app or page load.
2.	[Small data payloads](small-data-payloads.md). Keep the amount of data that is bulk retrieved small.
3.	[Optimize query data patterns](optimized-query-data-patterns.md). Do data mashups on the server, not in your Power Apps app.  
5.	[Efficient calculations.](efficient-calculations.md). Work with Power Fx - not against it.

These principles should cover most of what is necessary to make your app fast.  

## Additional performance guidance
There are other performance considerations to keep in mind. For additional guidance, see these articles: 

 * [Other performance considerations](app-performance-considerations.md) discusses  additional factors, which might affect performance.
 * [Build large complex apps](working-with-large-apps.md) outlines key factors to consider while building a large app.
 * [Canvas apps coding standards and guidelines](https://pahandsonlab.blob.core.windows.net/documents/PowerApps%20canvas%20app%20coding%20standards%20and%20guidelines.pdf) outlines general coding and development guidelines that can help in building an app.  




