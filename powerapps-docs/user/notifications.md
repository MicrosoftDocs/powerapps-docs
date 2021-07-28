---
title: "How notifications work in model-driven apps | MicrosoftDocs"
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

# Use in-app notifications within model-driven apps (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../includes/cc-beta-prerelease-disclaimer.md)]

In-app notification system uses the Notification table to store notifications for each user. The model-driven app polls the system for new notifications to be shown to the user. The notification sender or your system administrator can indicate if a toast is shown and how it is dismissed. Notifications are seen in the notification center until they're dismissed by a user or expire. Expiration of a notification defaults to 14 days but can be overriden by your administrator.

This topic outlines steps for [early access](/power-platform/admin/opt-in-early-access-updates) to enable the in-app notifications and send notifications to a specific user.

  > [!IMPORTANT]
  > - This is a preview feature, and isn't available in all regions.
  > - [!INCLUDE[cc_preview_features_definition](../includes/cc-preview-features-definition.md)]

To use the private preview, append the following parameters to the URL of the user to receive the notifications.

> ?flags=FCB.NotificationCenter=true

## Toast notifications
Toast notifications appear temporarily to the left edge of the application.  When multiple notifications appear they are stacked.

TODO: Add screenshot of notification center

## Notification center
Notification center is accessed by the bell icon in the app header.  It opens as a panel containing a list of the notifications.  A user can dismiss notifications by clicking the "X" which deletes the notification.

TODO: Add screenshot of notification center

Notifcations have an expiration date which is used to delete older notifications.

## Related links

[Send in-app notifications](../maker/model-driven-apps/send-in-app-notifications.md)
