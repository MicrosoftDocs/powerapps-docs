---
title: Manage model-driven app settings in the Power Apps app designer
description: Learn how to manage the settings for your app using the app designer
keywords: ""
ms.date: 03/31/2025
ms.custom: 
ms.topic: how-to
applies_to:
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: e773e60f-0211-4c4b-a1af-663be4997629
ms.author: matp
ms.reviewer: 
caps.latest.revision: 14
ms.subservice: mda-maker
search.audienceType: 
  - maker
contributors:
- chmoncay
---
# Manage model-driven app settings in the app designer

App settings define important details about the app, like its title. You define app settings when you create an app. If you want to change those settings later, you can do that in the app designer.  

You must select **Publish** to activate an app settings change.

1. In the app designer select **Settings** on the command bar.

2. View and change the information, as required:

    |Area|Setting|Description|  
    |-------------|--------------|-----------------|
    | **General**  | **Solution**  | Read-only property that displays the solution name where the app is located.  |
    |**General** |**App name**| The friendly name for the app.|  
    |**General** |**Description**| The description of the app (optional). If your app is in a [managed environment](/power-platform/admin/managed-environment-overview), you can select **Create description using AI** to have  Copilot generate one for you. More information: [Create an app description with Copilot (preview)](build-first-model-driven-app.md#create-an-app-description-with-copilot-preview) |  
    |**General** | **Icon** | Change the app icon by selecting **Select icon**, to browse and select an image web resource. This icon is displayed on the preview tile of the app. More information: [Create or edit model-driven app web resources to extend an app](create-edit-web-resources.md)|
    | **Advanced settings**   | **Unique name**  | Read-only property that displays the app unique name including the publisher prefix.  |
    | **Advanced settings**   | **Welcome page**   | This option allows a maker to select from the web resources available in your organization. The welcome pages created contain information that's useful to users, such as links to videos, upgrade instructions, or getting started information. The welcome page is displayed when an app is opened. Users can select **Do not show this Welcome Screen next time** on the welcome page to disable the page so it doesn't appear the next time the app starts. Notice that the **Do not show this Welcome Screen next time** option is a user-level setting and can't be controlled by administrators or app makers. More information: [Create or edit model-driven app web resources to extend an app](create-edit-web-resources.md)  |
    |**Advanced settings**  | **Primary mobile player**  | Determines which mobile player you want the model-driven app to be available from. By default, **Power Apps mobile** is selected. For example, if you want the model-driven app only available from the Dynamics 365 Sales mobile app, select **Dynamics 365 Sales**.<br><br> - **Power Apps Mobile**. More information: [Use model-driven apps on Power Apps mobile](../../mobile/use-custom-model-driven-app-on-mobile.md) <br /> - **Dynamics 365 Sales**. More information: [Overview of Dynamics 365 Sales mobile app](/dynamics365/sales/sales-mobile/dynamics-365-sales-mobile-app) <br /> - **Field Service (Dynamics 365)**. More information: [Overview of the Field Service (Dynamics 365) mobile app](/dynamics365/field-service/mobile-power-app-overview) |

3. **Save** and **Publish** the app.  

## Features

When you select **Settings** from the command bar, select **Features** to enable or disable model-driven app features for the app.

:::image type="content" source="media/model-driven-app-features.png" alt-text="Features available to this model-driven app":::

Here are a few of the features available to app makers:

- **Enable Power BI quick report visualizations on a table**. Enabled by default, this feature allows app users to create a Power BI quick report from a table view by selecting the **Visualize this view** command on the app command bar. More information: [Visualize data in a view with Power BI service](../../user/visualize-in-power-bi.md)
- **In app notifications**. When enabled, the app polls for new in-app notifications and displays them. More information: [Send in-app notifications within model-driven apps](../../developer/model-driven-apps/clientapi/send-in-app-notifications.md)
- **Lock tabs at the top of forms on mobile and tablets**. When enabled, tabs remain visible at the top of a form while users scroll through the data on the form. More information: [Lock tabs at the top of forms](../../mobile/use-custom-model-driven-app-on-mobile.md#lock-tabs-at-the-top-of-forms)
- **Mobile commanding improvements**. When enabled, optimizes the command bar for phone and tablet providing easy access to contextual commands to users helping increase productivity and satisfaction. More information: [Mobile commanding improvements](../../mobile/use-custom-model-driven-app-on-mobile.md#mobile-commanding-improvements)
- **Offline setup from the app designer**. [Enable your app for offline use](../../mobile/setup-mobile-offline.md#enable-your-app-for-offline-use)
- **Tablet optimization for command bar**. When enabled, replaces the native command bar at the bottom of the screen with the web command bar located at the top of the screen on tablets. More information: [Tablet optimization for command bar](../../mobile/use-custom-model-driven-app-on-mobile.md#tablet-optimization-for-command-bar)
- **Try the new look**. Enabled by default, this feature shows end users a "Try the new look" switch to enable the new experience. End users can switch back at any time. More information: [Modern, refreshed look for model-driven apps](../../user/modern-fluent-design.md)
- **Form fill assist toolbar**. When enabled, the form fill assist toolbar is visible at the top of a form, providing easy access to Copilot form fill assistance capabilities like smart paste and files. For more information about AI form fill assistance environment settings, go to [AI form fill assistance](/power-platform/admin/settings-features#ai-form-fill-assistance). For more information about using this feature, go to [Use Copilot's form fill assistance feature in model-driven apps](../../user/form-filling-assistance.md).

## Upcoming 

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

The **Upcoming** tab displays preview features currently available:

> [!IMPORTANT]
> [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]

- **Choose the offline mode to apply to your app**. When enabled, users can continue working in the model-driven app when offline. More information: [Mobile offline overview (preview)](../../mobile/mobile-offline-overview.md)

## Known limitations

The following app properties can't be edited in the app designer:

- App Url Suffix
- Manage App

## See also

[Create or edit an app](create-edit-app.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
