---
title: Overview on how to create performant Power Apps  
description: Learn about how to create well performing Power Apps.
author: lancedMicrosoft
ms.subservice: canvas-developer
ms.topic: how-to
ms.date: 02/26/2025
ms.author: lanced
ms.reviewer: mkaur
search.audienceType:
  - maker
contributors:
  - lancedMicrosoft
  - mduelae
  
---

# Overview of creating performant apps

## How and why to use performant patterns and avoid anti-patterns

Performant patterns should be used to enhance the efficiency of an app, while anti-patterns should be avoided as they can decrease the effectiveness of an app. It's important to understand how and why to use performant patterns and avoid anti-patterns in order to optimize the performance of your app.

### App patterns and Power Apps productivity gain

Power Apps simplifies the development of enterprise-grade apps by utilizing established app patterns. Patterns are collections of Power Apps elements that work cohesively together.  These Power Apps elements include data sources, collections, controls, Power Automate, and pages. Key performant patterns are built into Power Apps as defaults, enabling low-code developers to quickly create functional enterprise-grade apps. Additionally, deployment and Power Apps administration tasks are straightforward. With Power Apps, you and your development team can be more productive, as there are many elements that no longer require your attention.

### Power Apps steers towards performant patterns

The default Power Apps behavior guides you towards well known performant patterns. These patterns include streamlined data loading at launch, automatic incremental paging of data, caching of data for collections, and loading only essential data for each page. These proven patterns are effective for data-heavy enterprise applications. Many successful Power Apps implementations follow these guidelines, utilizing more than 100 tables and over 50 screens while maintaining excellent performance.

### Falling into anti-patterns

When you create an app on any development platform, there's a risk of creating an app that performs poorly due to anti-patterns. These patterns can cause slow loading times, slow transitions between pages, and difficulty updating and retrieving data. Some common examples of anti-patterns include loading excessive amounts of data, transforming everything into collections, and overloading OnStart. These patterns are often adopted when attempting to work around perceived or real limitations in Power Apps. While we try to guide you towards the best patterns, it's still possible to unintentionally use a bad pattern, resulting in an app that performs poorly.

## Four key performance design principles

Below are four key performance principles to consider while building your app. These principles aren't fully independent of each other and therefore you'll find some performance suggestions repeated in different sections. To best understand these articles, it also is useful to understand the [Execution phases of a Power App](execution-phases-data-flow.md) article. If you have an existing app that doesn't perform well, use the principles below to examine your app.  

Each of the principles below links to a page with greater detail on the subject.

1. [Optimize page loads](fast-app-page-load.md): Optimize your apps for app and page load speed. Minimize, delay, or eliminate actions that prevent fast app or page load.
2. [Small data payloads](small-data-payloads.md): Keep the amount of data that is bulk retrieved small.
3. [Optimize query data patterns](optimized-query-data-patterns.md): Do data mashups on the server, not in your app.  
4. [Fast calculations](efficient-calculations.md): Work with Power Fx, not against it.

These principles should cover most of what is necessary to make your app fast.  

## Additional performance guidance

There are other performance considerations to keep in mind. For additional guidance, see these articles: 

 * [Other performance considerations](app-performance-considerations.md): Discusses  additional factors, which might affect performance.
 * [Build large complex apps](working-with-large-apps.md): Outlines key factors to consider while building a large app.
 * [Canvas apps coding standards and guidelines](https://www.microsoft.com/en-us/power-platform/blog/wp-content/uploads/2024/06/PowerApps-canvas-app-coding-standards-and-guidelines.pdf): Outlines general coding and development guidelines that can help in building an app.  
