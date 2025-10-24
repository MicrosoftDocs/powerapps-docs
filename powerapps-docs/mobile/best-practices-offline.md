---
title: Best practices for developing an app for offline use
description: Learn about the best practices for developing an app for offline use.
author: trdehove
ms.component: pa-user
ms.topic: quickstart
ms.date: 05/31/2024
ms.subservice: mobile
ms.author: trdehove
ms.custom: ""
ms.reviewer: smurkute
ms.assetid: 
search.audienceType: 
  - enduser
searchScope:
  - "Power Apps"
---

# Best practices for developing an app for offline use
This article provides recommendations for how to create the best experience for users of apps configured for offline use. 

- If you configure a canvas app for offline use, you need to optimize how the app fetches data from the data source. Learn more: [How to create the best offline user experience in canvas apps](best-practices-offline#how-to-create-the-best-offline-user-experience-in-canvas-apps)
- To function offline, an app must initially download all necessary assets, including resources and data, to operate independently of a network connection. This process is a one-time setup task that occurs during the app’s first use. The speed of this initial download is influenced by the volume of data downloaded to the device, which is determined by the offline profile settings and the quantity of data available to the user within the app’s environment. For a seamless, initial experience, it’s advisable to plan your [offline app rollout](best-practices-offline#plan-your-offline-app-rollout).    

## How to create the best offline user experience in canvas apps

Use the following recommendations to create a fast user experience for specific scenarios. 

 |Scenario                      |  Approach that's not recommended                     |  Recommended approach               |
 |-------------------------------|----------------------------|--------------------------------|
 | Show related tables information in a gallery. | Use a look-up to fetch the data. | Use a view containing the columns of the related table.|
 | Create a filterable gallery with a lot of records.  | Load the records from Dataverse and store them in a collection. Set the items of the gallery to the filtered collection.  | Directly set the items of the gallery to the Dataverse-filtered data. |
 | Update multiple records. | Loop the records and patch them individually. | Bulk patch a collection containing all the modifications. |

### Diagnose mobile offline canvas apps with Monitor

Monitor is a tool that offers makers a deep view of what an app does and how it does it by logging all key activities that occur in the app as it runs. You can [connect a mobile app session to Monitor](/power-apps/maker/monitor-canvasapps) to better diagnose and troubleshoot issues faster.

## Plan your offline app rollout

> [!IMPORTANT]
> If you're using an **auto-generated offline profile** (available for canvas apps only), and if the first synchronization is taking too much time, you should create a manual, offline profile by using the following best practices. 

Develop and roll out your offline app in three phases.

:::image type="content" source="media/mobile-offline-guidelines/phases.png" alt-text="Illustration that shows Phase 1 for a maker, Phase 2 for testers, and Phase 3 for users.":::

### Phase 1: Develop and iterate

After you've [set up mobile offline for canvas apps](canvas-mobile-offline-setup#create-profiles-from-within-power-platform-admin-center-with-admin-rights) or [set up mobile offline for model-driven apps](setup-mobile-offline#set-up-a-mobile-offline-profile), it's time to start testing and tweaking. Use [Power Apps mobile](run-powerapps-on-mobile.md) or [Field Service Mobile](/dynamics365/field-service/field-service-mobile-app-user-guide) to determine how the app behaves when it's offline. For Windows, you'll find the [Power Apps for Windows](windows-app-install.md) app in the Microsoft Store that allows iterating without the need for a mobile device.

In this phase, you'll add tables and apply filters to existing tables to make sure that the right data is downloaded to the app, following the guidelines to [Optimize the offline profile](mobile-offline-guidelines.md).

#### Outcome
You confirm that all the tables and forms work offline after the data is downloaded and that download sizes are reasonable. 

> [!IMPORTANT]
> The metadata for the model-driven app is retrieved when the app starts. This means that if you change a component in your app, such as a form component or view, then you need to restart the app for the profile to reflect the changes.  

### Phase 2: Test with users

Ask a few users to test the app with real data. Make sure the offline profile scales for different types of users and works on devices with varying storage capacities. Check the **Device status** page (available out of the box in model-driven apps) for each user. For more information, see [Using the Offline template and offline status icon](canvas-mobile-offline-setup.md#using-the-offline-template-and-offline-status-icon). Adjust the filters in the offline profile to increase or decrease the amount of data that's downloaded.

:::image type="content" source="media/mobile-offline-guidelines/offline-status.png" alt-text="Screenshot of a mobile app's Offline Status page after a successful download.":::

#### Outcome
You confirm that the offline profile scales to real-use cases. If not, [optimize the offline profile](mobile-offline-guidelines.md).

### Phase 3: Roll it out

Deploy the app to the rest of your organization.

#### Outcome
You confirm that each class of user in the rollout is able to sync successfully and work offline. 

## Don't miss the data your users need

Test whether your users have all the data they need. Compare the data available when the app is online and when it's offline. With the device in airplane mode, make sure the views and forms show the same data as in a web browser online. If there are differences, either adjust the filters in your views or adjust the filters in your offline profile.

### Add related tables if your app needs them

- **Business process flows**: If a form contains a business process flow, be sure to add the business process flow table. For more information, see [Supported capabilities](/dynamics365/mobile-app/mobile-offline-capabilities#supported-capabilities).

- **Files and images**: If your offline profile contains files and images, add tables for them. For more information, see [Configure files and images in offline model-driven apps](offline-file-images.md) or [Configure files and images in offline canvas apps](files-images-offline-canvas-apps.md). Use custom filters to limit the download of critical files.

- **Timeline**: To make notes on the timeline control (for model-driven apps only) available offline, add the **Notes** table and the **Users** table to the offline profile. Notes can be large if users upload images and videos, so apply custom filters to the **Notes** table to limit download times.

    > [!IMPORTANT]
    > Data downloads may be slower if users upload files larger than 4 MB to the timeline control. If users need to upload files larger than 4 MB, use the quick notes control in Field Service or **Files**/**Images** instead of the timeline to improve performance.

## Tips on mobile offline synchronization
  
- Mobile offline synchronization with mobile devices occurs periodically. A synchronization cycle could last for several minutes, depending on Azure network latency, the volume of data that’s set for synchronization, and mobile network speed. Users can still use mobile apps during synchronization.  
  
- The time for initial metadata download is determined by the number of total tables in offline-configured app modules. Make sure to configure only those tables and app modules for offline that are necessary to optimize the experience for end users. 
  
- Ensure that any view that you want to work offline doesn’t reference tables that aren't configured for offline use. For example, assuming **Account** is in the offline profile, then an **Account** view that references the primary contact when **Contact** isn't in the profile, isn't available.

- Changes to a user’s security privileges are updated during the next synchronization cycle. Until that time, users can continue to access data according to their previous security privileges, but any changes they make are validated during the synchronization to the server. If they no longer have privileges to make changes for a row, they receive an error and the row won’t be created, updated, or deleted.

- Any changes to a user’s privilege to view a row won’t take effect on the mobile device until the next synchronization cycle.

- Mobile offline honors the security model for mobile apps and the hierarchical security model, except the [field-level security and field sharing](/power-platform/admin/field-level-security).

### See also

- [Optimize the offline profile](mobile-offline-guidelines.md)
- [Configure canvas apps for offline](canvas-mobile-offline-overview.md)
- [Configure model-driven apps for offline](mobile-offline-overview.md)
- [Configure offline data for the Field Service (Dynamics 365) mobile app (contains video)](/dynamics365/field-service/mobile-power-app-system-offline)
- [Five tips for implementing the Field Service (Dynamics 365) mobile app (blog)](https://cloudblogs.microsoft.com/dynamics365/it/2021/04/21/5-tips-for-implementing-the-field-service-dynamics-365-mobile-app/)

