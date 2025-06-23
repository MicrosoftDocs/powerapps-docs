---
title: Advantages and limitations of Wrap
description: Learn about advantages and limitations of Wrap
author: komala2019
ms.topic: article
ms.custom: canvas
ms.reviewer: smurkute
ms.date: 02/04/2025
ms.subservice: canvas-maker
ms.author: koagarwa
search.audienceType: 
  - maker
---

# Benefits and limitations of Wrap

Wrap gives app makers benefits like improved adoption, better branding, and flexible distribution options. But it also has some limitations you need to consider.

## Benefits of wrap

1. **Improved app adoption**: Users easily find and use your app by searching for its name in the App Store or Play Store. This direct access streamlines the experience and increases adoption rates.
1. **Enhanced branding flexibility**: Makers customize their app's branding, improving both distribution and user engagement.
1. **Custom distribution channels**: Distribute your apps through preferred channels, so you have more control and can reach your target audience more effectively, instead of relying only on standard platforms.
1. **Power Apps mobile for frontline workers (FLWs)**: Power Apps Mobile is for frontline workers. The wrap APK lets guest accounts sign in, so frontline workers outside your organization can use it. For details, see [Frequently asked questions for wrap: Why am I not able to sign into my wrapped application?](faq.yml).
1. **Access without MFA or Intune**: You can use the Power Apps mobile app without multifactor authentication (MFA) or Microsoft Intune if your organization's conditional access policies allow it.
1. **Offline features**: Wrap apps support offline capabilities.

## Limitations of Wrap

1. **Logout button**: There's no visible sign out button. 
   > [!NOTE]
   > Users can select and hold the indented application to sign out. Makers should let users know about this method.
1. **Push notifications**: Push notifications aren't supported.
1. **Navigation between apps**: You can't go directly from a specific screen in one app to a specific screen in another app. Only the home screen of the other app opens.
1. **APK size limit**: APK files distributed through the Google Play Store are limited to 100 MB. To support larger apps (up to 150 MB), create an AAB file during the wrap process.
1. **Android hardware back button**: The Android hardware back button doesn't always sync with the application back button.
1. **Feedback**: You can't provide feedback in the wrap app.
1. **Surveys**: Surveys aren't available for wrap users.
1. **Sovereign cloud**: Wrap doesn't support sovereign cloud environments.
1. **Full image view (offline)**: Offline-enabled wrap apps only show image thumbnails, not full image views.
1. **VPN**: The wrap wizard doesn't support creating a wrapped app while you're connected to a VPN. Updates are in progress.

### See also

- [Troubleshoot issues with the wrap feature in Power Apps](/troubleshoot/power-platform/power-apps/manage-apps-and-solutions/wrap-issues)
- [Frequently Asked Questions](faq.yml)
