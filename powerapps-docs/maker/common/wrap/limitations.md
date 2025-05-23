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

Wrap offers several benefits, effectively addressing challenges like increasing adoption rates, enhancing branding flexibility, and supporting custom distribution channels.

## Benefits of Wrap

1. **Improved app adoption**: App makers can distribute their applications more effectively, making it easier for users to find and use the app directly by searching for its name in the App Store or Play Store and opening it. This streamlined process eliminates the need for additional steps, enhancing user experience and adoption rates.

1. **Enhanced branding flexibility**: App makers have greater freedom to customize their app's branding, which streamlines both the distribution process and user engagement.

1. **Custom distribution channels**: App makers now have the flexibility to distribute their apps through their own preferred channels, providing more control and potentially reaching their target audience more effectively, rather than relying solely on standard platforms like the Play Store or App Store.

1. **Power Apps Mobile for Frontline Workers (FLWs)**: Power Apps Mobile is designed primarily for frontline workers (FLWs). To enable FLWs outside of the organization to log in, the wrap APK supports guest account logins. Follow the steps mentioned in [Frequently asked questions for wrap: Why am I not able to sign into my wrapped application?](faq.yml) to log in.

1. **Access without MFA or Intune**: The Power Apps mobile app can be accessed without multifactor authentication (MFA) or installing Microsoft Intune if the organization's conditional policies allow it.

1. **Offline Features**: The wrap app supports offline features.

## Limitations of Wrap

1. **Logout button**: The sign out button option for the user is missing.
   > [!NOTE]
   > Users can long press the indented application for which they want to sign out. To make this feature discoverable, we recommend that makers provide a notification to their users.

1. **Push notifications**:  Currently, the app does not support push notifications.

1. **Navigation**: Wrap doesn't support navigating from a specific screen of one app to a specific screen of another app. When users attempt to navigate, only the home screen of the other app is opened. For example, consider a primary app with screens A1, A2, and A3, and a secondary app with screens B1, B2, and B3. Currently, users can only navigate from any screen in App A to the home screen of App B. Direct navigation between individual screens of App A and App B isn't supported.

1. **APK size**: If your distribution method is via the Google Play Store, the APK file size is limited to 100 MB. We recommend creating an AAB file instead of an APK file during the wrap process, as AAB files support sizes up to 150 MB for the Play Store.

1. **Android hardware back button**: The Android hardware back button doesn't sync coherently with the application back button.

1. **Feedback**:  Currently, users can't provide feedback inside wrap.

1. **Surveys**: Users don't receive surveys for the wrap.

1. **Sovereign cloud**: Wrap is currently not supported in the sovereign cloud.

1. **Full Image View**: Offline-enabled Wrap apps support viewing images as thumbnails but don't currently support viewing images in full view. 

1. **VPN**: If you're connected to VPN, the wrap wizard currently doesn't support creating a wrapped app. We're working on alternatives and will update you shortly. 

1. **Intune**: If you use Intune to download the IPA, the wrapped application currently doesn't work. We're fixing the bug and will release the update soon.

### See also

- [Troubleshoot issues with the wrap feature in Power Apps](/troubleshoot/power-platform/power-apps/manage-apps-and-solutions/wrap-issues)
- [Frequently Asked Questions](faq.yml)