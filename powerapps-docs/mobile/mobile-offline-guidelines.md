---
title: Offline profile guidelines | Microsoft Docs
description: Guidelines to configure offline profiles when using offline capabilities in Power Apps mobile.
author: trdehove
ms.component: pa-user
ms.topic: quickstart
ms.date: 07/08/2022
ms.subservice: mobile
ms.author: trdehove
ms.custom: ""
ms.reviewer: mkaur
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---

# Offline profile guidelines

There's a lot to keep in mind when creating or updating an offline profile for model-driven apps. An offline profile should include all the data the app users need to complete tasks in the field, but if it includes too much data, app users might get stuck waiting to download the data they need or even run out of disk space. You'll need to consider the devices and data plans your app users have to make sure they have a great experience.

To optimize an offline profile for the exact needs of your organization, keep the following guidelines in mind.

## Validate your offline profile updates

You should develop and roll out your offline profile in three main phases:

:::image type="content" source="media/mobile-offline-guidelines/phases.png" alt-text="An image that shows phase 1 for a maker, phase 2 for testers, and phase 3 for users.":::

### Phase 1: Offline profile development and iteration

You as the maker or admin create or update an offline profile based on data configured in an app module. In a test environment, you can validate how the app behaves when offline using Power Apps or Field Service on iOS, Android, or Windows. Windows users will find apps in the Microsoft Store that allow quick iterations without the need for a mobile device. In this phase, you'll add new tables and filters to existing tables to make sure that the right data is downloaded to the app.

***Outcome:*** You validate that all the grids and forms work offline after data download is complete and download sizes are reasonably based on test data.

### Phase 2: User validation

Enroll a few users in the field or in test environments with real copies of data to make sure the offline profile scales with different types of users and works on devices with different storage capacities. Review the offline status page for each user to understand how many rows and files are downloaded by different types of user accounts. You can update filters in the offline profile to increase or reduce how much data will be downloaded to user devices:

:::image type="content" source="media/mobile-offline-guidelines/offline-status.png" alt-text="An image that shows offline status for tables selected for the app.":::

***Outcome:*** Validate that the offline profile scales to the real user use case.

### Phase 3: Rollout

Deploy the app to the wider organization. Confirm that each class of user in the rollout is able to sync successfully and work offline.

## Don't make your users download too much data

Each user has access to a different set of data, so it's important to think about and test how much data different groups of users will see. For example, a group sales manager might have access to many more sales opportunities than a local sales manager.

As you develop your offline profile and test with real or representative data, keep these best practices in mind:

- Limit the total records synced to less than 200,000
- Limit the number of tables in an offline profile to less than 100 
- Limit the total data size to less than 4 GB. If your users use Files, Images, or Timeline Annotations, you should apply filters to reduce the total download size

If offline data exceeds these recommendations, users will see slower syncs, higher data utilization, higher battery usage, and slower app performance.

## Optimize your offline profile

Apply the following best practices to ensure that users only download the data they need.

### Don't reinvent the wheel

If you're customizing Field Service or Sales, start from the default offline profiles packaged with those apps. They include everything you need for an out-of-box solution, and you can add other standard and custom tables that are important for your business. By starting with the default profile, you know that core features will work, and you won't miss tables referenced by standard forms.

If you're using a default profile, **don't remove tables**. Removing tables from the default profile may result in runtime failures in forms or views. If the default profile includes too many or too few rows of data, adjust filters on the largest tables to optimize data sizes for your users.

### Add all tables referenced by each form and view in your app module

When you add a new form or view to your model-driven app, look for references to other tables including lookups and other related tables. Make sure each of these tables is included in your offline profile with a corresponding related table or filters. All tables referenced by web resource scripts should also be added to the offline profile.

When you add a table to the offline profile, you can choose between these four options to determine which rows will be downloaded:

:::image type="content" source="media/mobile-offline-guidelines/options.png" alt-text="An image that shows four options to download rows with options of organization rows, all rows, related rows only, and custom.":::

Consider which of these categories your table belongs to in your model-driven app to help choose the best option for each table:

1. **Standalone tables:** Tables visible as Grids in the app, like Contact

2. **Related Tables:** Tables referenced in the Form or Grid view of a different table, like Unit

3. **Resource Tables:** Tables containing resource data, like Currency or Territory

Choose a row option based on the category of table you add:

|   Table type         | Organization rows | All rows | Related rows only | Custom |
|------------|-------------------|----------|-------------------|--------|
| Standalone | &check;                 |          |                   | &check;      |
| Related    |                   |          | &check;                 | &check;      |
| Resources  |                   | &check;        |                   | &check;      |

### Use filters to reduce data download size

If some users have access to a large set of data online, you should add custom filters to restrict the data that these users will download offline.

> [!IMPORTANT]
> If you add a custom filter to a table configured to download related rows, the custom filter will be treated as an **OR** with all related rows also being downloaded in addition to rows specified by the filter, so users may download more data than you intend. If you want to download related rows and apply an additional filter, uncheck Related rows only and specify the relationship and the additional restrictions in a custom filter using **AND**.

For **Standalone** Tables, you can use a custom filter that includes the records referenced by the Grid views configured in your model-driven app. By default, all views are included when you add a table to the app designer.

To ensure that users, see the same data online and offline, you should explicitly select the views that filter data that you include in the offline profile.

:::image type="content" source="media/mobile-offline-guidelines/filters1.png" alt-text="An image that shows filter with explicit equal condition.":::

For **Related** Tables, use a custom filter if you want users to download rows that are related **AND** match your other filter criteria.

:::image type="content" source="media/mobile-offline-guidelines/filters2.png" alt-text="An image that shows filter with custom filter with AND condition.":::

For **Resources** Tables, use a custom filter if you want users to download only rows that match your criteria like rows with an Active Status.

:::image type="content" source="media/mobile-offline-guidelines/filters3.png" alt-text="An image that shows filter with active status.":::

#### Common custom filters

**Filter by time and date fields** for time-centric data like bookings and Timeline items. Consider both future and past dates. For example, a common filter might include appointments from the past month and the next three months.

:::image type="content" source="media/mobile-offline-guidelines/filters4.png" alt-text="An image that shows multiple filters with or condition based on start and end times.":::

**Filter by** **status** to limit downloads to Active rows or rows that meet your status criteria.

:::image type="content" source="media/mobile-offline-guidelines/filters7.png" alt-text="An image that shows multiple filters with status of active.":::

**Filter by custom category or role fields** to scope large tables down to the data needed for your app. For example, you could filter Contacts by Role to limit data to only stakeholders.

:::image type="content" source="media/mobile-offline-guidelines/filters5.png" alt-text="An image that shows a filter with role type.":::

### Avoid these filter pitfalls that can slow down your downloads

If a custom filter results in a slow Dataverse query, it will take longer for your users to download offline data. Follow these best practices to avoid common performance bottlenecks.

- Don't use partial string matches or "Contains", "Begins with", or "Ends with".

- Avoid multiple levels of relationships in custom filters. Filters like this can lead to slow downloads:

    :::image type="content" source="media/mobile-offline-guidelines/filters6.png" alt-text="An image that shows multiple filters with relationships and nesting.":::

- Avoid too many OR conditions

## Don't miss the data your users need

To validate if your users have all the data they need, you should compare the data available online and offline. Use the mobile app in airplane mode or with your internet connection disabled, and make sure the views and forms you see show the same data as you see in a web browser online. If there are differences, it means you should either refine filters in your Views or refine the filters in your offline profile.

### Add these related tables if your app needs them

- **Business process flows:** If a form contains a business process flow, make sure to add the business process flow table. More information: [Mobile Offline Supported Capabilities](/dynamics365/mobile-app/mobile-offline-capabilities#supported--capabilities) for more details.

- **Files and Images:** To add Files and Images to your offline profile in the Power Platform Admin Center, see [Configure mobile offline profiles for files and images](offline-file-images.md). Use custom filters to limit download of critical files.

- **Timeline:** To make Notes on the timeline control available offline, add the Notes table and the Users table to the offline profile. Notes can be large if users upload images and videos, so use custom filters to the Notes table to limit download times.

- **Warning**: you may see slower data downloads if users upload files larger than 4 MB to the Timeline control. If users need to upload files larger than 4 MB, use the Quick Notes control in **Field Service**, or **Files**/**Images** instead of the **Timeline** to improve performance.

### See also

- [Configure model-driven apps for offline (preview)](mobile-offline-overview.md)
- [Configure offline data for the Field Service (Dynamics 365) mobile app (contains video)](/dynamics365/field-service/mobile-power-app-system-offline)
- [Five tips for implementing the Field Service (Dynamics 365) mobile app (blog)](https://cloudblogs.microsoft.com/dynamics365/it/2021/04/21/5-tips-for-implementing-the-field-service-dynamics-365-mobile-app/)

[!INCLUDE[footer-include](../includes/footer-banner.md)]
