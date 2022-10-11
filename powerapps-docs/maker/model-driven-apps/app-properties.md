---
title: "Manage model-driven app settings in the Power Apps app designer | MicrosoftDocs"
description: "Learn how to manage the settings for your app"
keywords: ""
ms.date: 08/09/2022
ms.custom: 
ms.topic: how-to
applies_to:
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: e773e60f-0211-4c4b-a1af-663be4997629
ms.author: matp
manager: kvivek
ms.reviewer: 
ms.suite: 
ms.tgt_pltfrm: 
caps.latest.revision: 14
topic-status: Drafting
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Manage model-driven app settings in the app designer

App settings define important details about the app, like its title. You define app settings when you create an app. If you want to change those settings later, you can do that in the app designer.  
  
1. In the app designer, on the left pane, select **App** under the **Pages** section. Or alternatively, select **Settings** on the command bar.

    > [!div class="mx-imgBorder"]
    > ![App designer Properties pane](media/model-driven-app-properties.png "App designer Properties pane")  
  
2. View and change the information, as required:

    |Area|Setting|Description|  
    |-------------|--------------|-----------------|
    | **General**  | **Solution**  | Read-only property that displays the solution name where the app is located.  |
    |**General** |**App name**| The friendly name for the app.|  
    |**General** |**Description**| An optional description of what the app is.|  
    |**General** | **Icon** | Change the app icon by selecting **Select icon**, to browse and select an image web resource. This icon will be displayed on the preview tile of the app. More information: [Create or edit model-driven app web resources to extend an app](create-edit-web-resources.md)|
    | **Advanced settings**   | **Unique name**  | Read-only property that displays the app unique name including the publisher prefix.  |
    | **Advanced settings**   | **Welcome page**   | This option allows a maker to select from the web resources available in your organization. The welcome pages created can contain information that's useful to users, such as links to videos, upgrade instructions, or getting started information. The welcome page is displayed when an app is opened. Users can select **Do not show this Welcome Screen next time** on the welcome page to disable the page so it doesn't appear the next time the app starts. Notice that the **Do not show this Welcome Screen next time** option is a user-level setting and can't be controlled by administrators or app makers. More information: [Create or edit model-driven app web resources to extend an app](create-edit-web-resources.md)  |
    |**Advanced settings**  | **Primary mobile player**(preview)  | [!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]<br />Determines which mobile player you want the model-driven app to be available from. By default, **Power Apps mobile** is selected. For example, if you want the model-driven app only available from the Dynamics 365 Sales mobile app, select **Dynamics 365 Sales**.<br /> - **Power Apps Mobile**. More information: [Use model-driven apps on Power Apps mobile](../../mobile/use-custom-model-driven-app-on-mobile.md) <br /> - **Dynamics 365 Sales**. More information: [Overview of Dynamics 365 Sales mobile app](/dynamics365/sales/sales-mobile/dynamics-365-sales-mobile-app) <br /> - **Field Service (Dynamics 365)**. More information: [Overview of the Field Service (Dynamics 365) mobile app](/dynamics365/field-service/mobile-power-app-overview) |

3. **Save** the app.  

## Features

When you select **Settings** from the command bar, select **Features** to enable or disable model-driven app features for the app. 

:::image type="content" source="media/model-driven-app-features.png" alt-text="Features available to this model-driven app":::

Here are a few of the features available to app makers: 

- **Enable Power BI quick report visualizations on a table**. When enabled, lets app users view table data from a Power BI quick report. More information: [Visualize data in a view with Power BI service](../../user/visualize-in-power-bi.md)
- **In app notifications**. When enabled, the app polls for new in-app notifications and displays them. More information: [Send in-app notifications within model-driven apps](../../developer/model-driven-apps/clientapi/send-in-app-notifications.md)
- **Offline setup from the app designer**. [Enable your app for offline use (preview)](../../mobile/setup-mobile-offline.md#enable-your-app-for-offline-use-preview)
- **Mobile commanding improvements**. When enabled, optimizes the command bar for phone and tablet providing easy access to contextual commands to users helping increase productivity and satisfaction.
- **Table optimization for command bar**. When in enabled, replaces the native command bar at the bottom of the screen with the web command bar located at the top of the screen on tablets.

## Known limitations

The following app properties can't be edited in the app designer:

- App Url Suffix
- Manage App
- Enable Mobile Offline
- Mobile Offline Profiles

## See also

[Create or edit an app](create-edit-app.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
