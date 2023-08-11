---
title: Offline profile guidelines
description: Guidance for optimizing offline profiles for model-driven apps.
author: trdehove
ms.component: pa-user
ms.topic: quickstart
ms.date: 04/12/2023
ms.subservice: mobile
ms.author: trdehove
ms.custom: ""
ms.reviewer: sericks
ms.assetid: 
search.audienceType: 
  - enduser
---

# Offline profile guidelines

There's a lot to keep in mind when you create or update an offline profile for model-driven apps. An offline profile should include all the data that app users need to complete tasks in the field. If it includes too much data, however, app users might get stuck waiting for their data to download. They may even run out of space on their device. You'll need to consider the devices and data plans your app users have to make sure they have a great experience.

The following guidelines will help you create an offline profile that meets the exact needs of your organization.

## Plan your offline profile rollout

Develop and roll out your offline profile in three phases:

:::image type="content" source="media/mobile-offline-guidelines/phases.png" alt-text="Illustration that shows Phase 1 for a maker, Phase 2 for testers, and Phase 3 for users.":::

### Phase 1: Develop and iterate

After you've [set up an offline profile](setup-mobile-offline.md#set-up-a-mobile-offline-profile), it's time to start testing and tweaking. Use [Power Apps mobile](run-powerapps-on-mobile.md) or [Field Service Mobile](/dynamics365/field-service/field-service-mobile-app-user-guide) on to determine how the app behaves when it's offline. For Windows, you'll find the [app](windows-app-install.md) in the Microsoft Store that allow iterating without the need for a mobile device.

In this phase, you'll add tables and apply filters to existing tables to make sure that the right data is downloaded to the app.

***Outcome:*** You confirm that all the tables and forms work offline after the data is downloaded and that download sizes are reasonable.

### Phase 2: Test with users

Ask a few users to test the app with real data. Make sure the offline profile scales for different types of users and works on devices with varying storage capacities. Check the Offline Status page for each user. How many tables and files do different types of user accounts download? Adjust the filters in the offline profile to increase or decrease the amount of data that's downloaded.

:::image type="content" source="media/mobile-offline-guidelines/offline-status.png" alt-text="Screenshot of a mobile app's Offline Status page after a successful download.":::

***Outcome:*** You confirm that the offline profile scales to real use cases.

### Phase 3: Roll it out

Deploy the app to the rest of your organization.

***Outcome:*** You confirm that each class of user in the rollout is able to sync successfully and work offline.

## Don't make your users download too much data

Each user may have access to a different set of data. It's important to think about and test how much data different groups of users will see. For example, a group sales manager might have access to many more sales opportunities than a local sales manager.

As you develop your offline profile and test with real or representative data, keep these best practices in mind:

- Limit the total records synced to no more than 200,000.
- Limit the number of tables to fewer than 100.
- Limit the total data size to less than 1 GB. 
- Limit the total files and images size to less than 4 GB. Apply filters to reduce the total download size.

If your app's offline data exceeds these recommendations, users will see slower syncs, higher data utilization, higher battery usage, and slower app performance.

## Optimize your offline profile

Apply the following best practices to make sure that users download only the data they need. Optimizing the data that's downloaded will make it easier to stay within the recommended limits.

### Don't reinvent the wheel

If you're customizing Field Service or Sales, start from their default offline profiles. You know core features will work, and you won't miss tables that are used in standard forms.

The default offline profiles include everything you need for an out-of-the-box solution. You can add more tables that are important for your business.

But **don't remove tables** from the default profile. Without those tables, forms or views may fail at runtime. If the default profile includes too many or too few rows of data, adjust the filters on the largest tables to optimize data sizes for your users.

### Add all tables that are referred to in each form and view in your app

When you add a form or view to your model-driven app, look for references to other tables, including lookups. Make sure each of these tables is included in your offline profile with a corresponding related table or filters. Be sure to add all tables used in web resource scripts as well.

When you add a table to the offline profile, you can choose one of four options to determine which rows will be downloaded:

- Organization rows
- All rows
- Related rows only
- Custom

To choose the best option for each table, consider which of the following categories your table belongs to:

1. **Standalone tables:** Tables that are visible as grids in the app, like Contact

2. **Related tables:** Tables that are referred to in the form or grid view of a different table, like Unit

3. **Resource tables:** Tables that contain resource data, like Currency or Territory

Choose a row option based on the category of table you add:

| Table type  | Organization rows | All rows | Related rows only | Custom |
| --- | --- | --- | --- | --- |
| Standalone | &check; | | | &check; |
| Related    | | | &check; | &check; |
| Resources  | | &check; | | &check; |

### Use filters to reduce the data download size

If users have access to a large set of data when they're online, apply filters to restrict the data that they'll download when they're offline.

> [!IMPORTANT]
> If you add a custom filter to a table that's set to download related rows, the filter is treated as an **OR**. That means that all related rows are downloaded, in addition to the rows specified by the filter. Users may download more data than you intend. If you want to download related rows and apply an additional filter, clear **Related rows only** and specify the relationship and the additional restrictions in a custom filter using **AND**.

- **Standalone tables:** Use a custom filter that includes the records that are required for the grid views in your app. By default, all views are included when you add a table in the app designer. To make sure that users have the same data online and offline, explicitly select the views that filter data that you include in the offline profile.

    :::image type="content" source="media/mobile-offline-guidelines/filters1.png" alt-text="Screenshot that shows a custom filter with an explicit EQUALS condition.":::

- **Related tables:** Use a custom filter if you want users to download rows that are related **AND** that match your other filter criteria.

    :::image type="content" source="media/mobile-offline-guidelines/filters2.png" alt-text="Screenshot that shows a custom filter with an AND condition.":::

- **Resources tables:** Use a custom filter if you want users to download only rows that match your criteria, like rows with an Active status.

    :::image type="content" source="media/mobile-offline-guidelines/filters3.png" alt-text="Screenshot that shows a custom filter with Status equal to Active.":::

#### Common custom filters

**Filter by time and date fields** for time-centric data like bookings and timeline items. Consider both future and past dates. For example, a common filter might include appointments from the past month and the next three months.

:::image type="content" source="media/mobile-offline-guidelines/filters4.png" alt-text="Screenshot that shows multiple filters, based on start and end times, in an OR condition.":::

**Filter by status** to limit downloads to rows with a certain Status.

:::image type="content" source="media/mobile-offline-guidelines/filters7.png" alt-text="Screenshot that shows multiple filters with Status equal to Active.":::

**Filter by custom category or role fields** to scope large tables down to the data needed for your app. For example, you could filter Contacts by Role to limit data to stakeholders.

:::image type="content" source="media/mobile-offline-guidelines/filters5.png" alt-text="Screenshot that shows a filter based on Role.":::

### Avoid these filter pitfalls that can slow down your downloads

If a custom filter results in a slow Dataverse query, downloads will take longer. Follow these best practices to avoid common performance bottlenecks:

- Don't use partial string matches or "Contains," "Begins with," or "Ends with."

- Avoid multiple levels of relationships in custom filters. Filters like this can lead to slow downloads:

    :::image type="content" source="media/mobile-offline-guidelines/filters6.png" alt-text="Screenshot that shows multiple filters with nested relationships.":::

- Avoid using many OR conditions.

## Don't miss the data your users need

Test whether your users have all the data they need. Compare the data available when the app is online and when it's offline. With the device in airplane mode, make sure the views and forms show the same data as in a web browser online. If there are differences, either adjust the filters in your views or adjust the filters in your offline profile.

### Add related tables if your app needs them

- **Business process flows:** If a form contains a business process flow, make sure to add the business process flow table. For more information, go to [Supported capabilities](/dynamics365/mobile-app/mobile-offline-capabilities#supported-capabilities).

- **Files and images:** If your offline profile contains files and images, you'll need to add tables for them. For more information, go to [Configure mobile offline profiles for files and images](offline-file-images.md). Use custom filters to limit download of critical files.

- **Timeline:** To make notes on the timeline control available offline, add the Notes table and the Users table to the offline profile. Notes can be large if users upload images and videos, so apply custom filters to the Notes table to limit download times.

    > [!IMPORTANT]
    > Data downloads may be slower if users upload files larger than 4 MB to the timeline control. If users need to upload files larger than 4 MB, use the quick notes control in Field Service or **Files**/**Images** instead of the timeline to improve performance.

### See also

- [Configure model-driven apps for offline (preview)](mobile-offline-overview.md)
- [Configure offline data for the Field Service (Dynamics 365) mobile app (contains video)](/dynamics365/field-service/mobile-power-app-system-offline)
- [Five tips for implementing the Field Service (Dynamics 365) mobile app (blog)](https://cloudblogs.microsoft.com/dynamics365/it/2021/04/21/5-tips-for-implementing-the-field-service-dynamics-365-mobile-app/)

[!INCLUDE[footer-include](../includes/footer-banner.md)]
