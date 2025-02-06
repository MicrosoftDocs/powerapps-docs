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

# Advantages and limitations of Wrap

Wrap offers several benefits over Power Apps Mobile, addressing key challenges such as low adoption rates, branding limitations, and the preference for custom distribution channels.

## Advantages of Wrap

The following are the challenges with Power Apps Mobile Distribution

1. **Low Adoption Rate of PAM**: App makers face difficulties in effectively distributing their applications within the PowerApps framework.
    * *Expectation*: Users expect to find and use the app directly by searching for the app name in the app store and then opening it.
    * *Reality*: In reality, users need to first install PowerApps from the app store. After installing PowerApps, they must then click on the app name within PowerApps to start using the app.
2. **Branding Limitations**: Makers look for greater flexibility to customize their app's branding, which would streamline both the distribution process and user engagement.
    * *Expectation*: Users expect to find and use the app directly by searching for the app name in the App Store or Play Store.
    * *Reality*: In reality, users need to first install Power Apps from the App Store or Play Store. After installing Power Apps, they must then click on the app name within PowerApps to start using the app.
3. **Preference for Custom Channels**: Many makers prefer to distribute their apps through their own channels instead of relying on standard platforms like the Play Store or App Store.

## Limitations

1. **Missing Logout Button**: The logout button option for the user is missing.
   > [!NOTE]
   > Users can long press the indented application for which they want to logout. To make this feature discoverable, we recommend that makers provide a notification to their users.

2. **No Push Notifications**: The app doesn't support push notifications.

3. **Navigation Limitations**: Wrap does not support navigating from a specific screen of one app to a specific screen of another app. When users attempt to navigate, only the home screen of the other app is opened. For example, consider a primary app with screens A1, A2, and A3, and a secondary app with screens B1, B2, and B3. Currently, users can only navigate from any screen in App A to the home screen of App B. Direct navigation between individual screens of App A and App B is not supported.

4. **APK Size Limitation**: If your distribution method is via the Google Play Store, note that the APK file size is limited to 100MB. We recommend creating an AAB file instead of an APK file during the wrap process, as AAB files support sizes up to 150MB for the Play Store.

5. **Android Hardware Back Button**: The Android hardware back button doesn't sync coherently with the application back button.

6. **Feedback**: Users can't provide feedback inside the wrap.

7. **Surveys**: Users don't receive surveys for the wrap.