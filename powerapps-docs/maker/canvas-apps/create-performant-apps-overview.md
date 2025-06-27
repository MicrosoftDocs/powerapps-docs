---
title: How to create performant Power Apps
description: Learn how to create performant Power Apps for faster, more efficient apps. Discover key principles and tips to optimize your app's performance.
author: lancedMicrosoft
ms.subservice: canvas-developer
ms.topic: how-to
ms.date: 06/27/2025
ms.author: lanced
ms.reviewer: mkaur
search.audienceType:
  - maker
contributors:
  - lancedMicrosoft
  - mduelae
  
---

# Overview of creating performant apps

Creating performant Power Apps ensures your apps run efficiently and provide a better user experience. This article explains key patterns, anti-patterns to avoid, and design principles to help you build high-performing Power Apps for your organization.

- **App patterns and Power Apps productivity gain**: Power Apps makes it easier to build enterprise-grade apps by using established app patterns. Patterns are groups of Power Apps elements that work together, like data sources, collections, controls, Power Automate, and pages. Power Apps includes key performant patterns by default, so low-code developers quickly build functional enterprise apps. Deployment and administration tasks are also straightforward. With Power Apps, your team is more productive because many elements don't need your attention.

- **Power Apps steers towards performant patterns**: Power Apps guides you toward well known performant patterns by default. These patterns include streamlined data loading at launch, automatic incremental paging, caching data for collections, and loading only essential data for each page. These proven patterns work well for data-heavy enterprise apps. Many successful Power Apps implementations use more than 100 tables and over 50 screens while keeping excellent performance.

- **Falling into anti-patterns**: When you build an app on any development platform, you risk making it perform poorly because of anti-patterns. These patterns can cause slow loading, slow page transitions, and make it hard to update or get data. Common anti-patterns include loading too much data, turning everything into collections, and overloading OnStart. People often use these patterns to work around real or perceived Power Apps limitations. Even with guidance, you might still use a bad pattern and end up with a slow app.

## Key performance design principles

When building your app, consider these key performance principles to ensure it runs efficiently. These principles cover most aspects needed to enhance your app's speed. Note that some performance suggestions may appear in multiple sections due to their interrelated nature. 

- [Optimize page loads](fast-app-page-load.md): Optimize your apps for app and page load speed. Minimize, delay, or eliminate actions that prevent fast app or page load.
- [Small data payloads](small-data-payloads.md): Keep the amount of data that is bulk retrieved small.
- [Optimize query data patterns](optimized-query-data-patterns.md): Do data mashups on the server, not in your app.  
- [Fast calculations](efficient-calculations.md): Work with Power Fx, not against it.

For a deeper understanding, also see [Execution phases of a Power App](execution-phases-data-flow.md) article.

## Additional performance guidance

Other performance considerations can affect your app. For more guidance, see these articles:

 * [Other performance considerations](app-performance-considerations.md): Discusses additional factors that might affect performance.
 * [Build large complex apps](working-with-large-apps.md): Lists key factors to consider when building a large app.
 * [Canvas apps coding standards and guidelines](https://www.microsoft.com/en-us/power-platform/blog/wp-content/uploads/2024/06/PowerApps-canvas-app-coding-standards-and-guidelines.pdf): Lists general coding and development guidelines that help you build an app.
