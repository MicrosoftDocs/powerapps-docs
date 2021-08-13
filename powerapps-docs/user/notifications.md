---
title: "In-app notifications in model-driven apps | MicrosoftDocs"
description: How notification work in model-driven apps.
ms.custom: ""
ms.date: 08/2/2021
ms.reviewer: ""
ms.service: powerapps
ms.subservice: end-user
ms.topic: "article"
author: "aorth"
ms.author: "mkaur"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---

# Preview: In-app notifications in model-driven apps 

[!INCLUDE [cc-beta-prerelease-disclaimer](../includes/cc-beta-prerelease-disclaimer.md)]

In-app notifications allow you to receive notifications in the notification center of your model-driven app. Notifications are stored in the notification center until you dismiss them or when they expire. By default, notifications expire in 14 days but your system administrator can modify the expiration date.

> [!IMPORTANT]
> - This is a preview feature, and isn't available in all regions. Your administrator needs to enable [early access](/power-platform/admin/opt-in-early-access-updates) to use the new app notifications feature.
> - [!INCLUDE[cc_preview_features_definition](../includes/cc-preview-features-definition.md)]

You only see notifications when you're using an app. That's when the system runs a check and displays any new notification. Notifications are at the organization level so you'll see all notifications in the app that you're using for all apps that are in your environment.

## Notification center

- The notification bell icon shows the count of new notifications. When you open the notification center the count is cleared. To access your notifications, select the bell icon on the nav bar. 


  > [!div class="mx-imgBorder"] 
  > ![Sample notifications in your app.](media/notifications-bell.png)  


- To dismiss and delete a notification, select the close **X** button on a notification. Or, select **Dismiss all** to dismiss and delete all notifications. 

  > [!div class="mx-imgBorder"] 
  > ![Select the close button to dismiss a notifications or select Dismiss all.](media/notifications-dismiss.png)  


## Toast notifications

Toast notifications appear temporarily to the left edge of the application. When multiple notifications appear, they are stacked. When more than three toast notifications are received at a time, you'll see toast that indicates that there's more notification for you to see in the notification center.

> [!div class="mx-imgBorder"] 
> ![Example on how toast notifications appear.](media/notifications-toast.png)  


Your system administrator can enable or disable toast notifications. If toasts are enabled, you can turn them off at a user level. Regardless of the toast being shown, all notifications can be accessed from notification center.

1. To enable or disable toast notifications in the notification center, select **Settings** 

   > [!div class="mx-imgBorder"] 
   > ![Notification settings menu.](media/notifications-settings.png)  

2. To enable or disable toast notifications, do one of the following:

    - **To enable toast notifications**: Move the toggle to **On** and then enter how many seconds the toast will show. 
    - **To disable toast notifications**: Move the toggle to **Off**.
   
       > [!div class="mx-imgBorder"] 
       > ![Enable to disable toast notifications.](media/notifications-2.png)  
   
 3. When you're done, select **Save**.  



## See also

[In-app notifications on Power Apps mobile](../mobile/mobile-notifications.md) </br>
[Send in-app notifications within model-driven apps](../developer/model-driven-apps/clientapi/send-in-app-notifications.md)
