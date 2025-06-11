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

Wrap provides several advantages for app makers, including improved adoption, enhanced branding, and flexible distribution options. However, there are also some limitations to consider.

## Benefits of Wrap

1. **Improved app adoption**: Users can easily find and use your app by searching for its name in the App Store or Play Store. This direct access streamlines the user experience and increases adoption rates.

2. **Enhanced branding flexibility**: Makers can customize their app's branding, improving both distribution and user engagement.

3. **Custom distribution channels**: Distribute your apps through preferred channels, giving you more control and potentially reaching your target audience more effectively, rather than relying solely on standard platforms.

4. **Power Apps Mobile for Frontline Workers (FLWs)**: Power Apps Mobile is designed for frontline workers. The wrap APK supports guest account logins, enabling FLWs outside your organization to log in. For details, see [Frequently asked questions for wrap: Why am I not able to sign into my wrapped application?](faq.yml).

5. **Access without MFA or Intune**: The Power Apps mobile app can be accessed without multifactor authentication (MFA) or Microsoft Intune if your organization's conditional access policies allow it.

6. **Offline features**: Wrap apps support offline capabilities.

## Limitations of Wrap

1. **Logout button**: There is no visible sign out button.  
   > [!NOTE]
   > Users can long press the indented application to sign out. Makers should notify users about this method.

2. **Push notifications**: Push notifications are not supported.

3. **Navigation between apps**: You cannot navigate directly from a specific screen in one app to a specific screen in another. Only the home screen of the other app will open.

4. **APK size limit**: APK files distributed via the Google Play Store are limited to 100 MB. To support larger apps (up to 150 MB), create an AAB file during the wrap process.

5. **Android hardware back button**: The Android hardware back button does not always sync with the application back button.

6. **Feedback**: Users cannot provide feedback within the wrap app.

7. **Surveys**: Surveys are not available for wrap users.

8. **Sovereign cloud**: Wrap is not supported in sovereign cloud environments.

9. **Full image view (offline)**: Offline-enabled wrap apps only support image thumbnails, not full image viewing.

10. **VPN**: The wrap wizard does not support creating a wrapped app while connected to a VPN. Updates are in progress.

### See also

- [Troubleshoot issues with the wrap feature in Power Apps](/troubleshoot/power-platform/power-apps/manage-apps-and-solutions/wrap-issues)
- [Frequently Asked Questions](faq.yml)
