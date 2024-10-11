---
title: Set an app as a startup app
description: Learn how to set an app as a startup app for mobile experience in Power Apps mobile app.
ms.date: 03/22/2024
ms.topic: overview
ms.component: pa-user
ms.subservice: mobile
author: trdehove
ms.author: devangpandya
ms.reviewer: smurkute
search.audienceType: 
  - enduser
searchScope:
  - "Power Apps"
---

# Set an app as a startup app 

Users can set an app as a startup app in Power Apps mobile app. This feature is available for the iOS and Android versions of Power Apps mobile app.

Users can mark any canvas or model-driven app as a startup app in two ways:

- [From an in-app suggestion](#set-a-startup-app-from-a-suggestion)
- [On the app **Details** page](#set-a-startup-app-from-the-details-page)


## Benefits of setting a startup app

- Improves productivity:
  - Once an app is set as the startup app, it opens by default when users open Power Apps mobile app.
  - No need to wait for the home page to load, saving the user time.
  - Creating and testing an app is faster, since you can bypass the home page.

- Efficient to create:
  - You can set a startup app with one tap.
  - This feature is better than shortcut apps, which require three to four taps and need external apps/device feature support.

- Simple to enable:
  - No changes are required for makers to use this feature.
  - There's in-app information about the feature's use and benefits.
  - The feature is compatible with offline, wrap, custom branding, push notifications, and shortcut features.

## Set a startup app from a suggestion

If a user opens the same app for seven days, a suggestion appears, at the top of the home page, when they close the app.  

1. View the startup app suggestion.

   You might see an in-app suggestion, asking users if they want to open the app as a Power Apps mobile startup app.

   :::image type="content" source="media/set-startup-app-mobile/startup-app-suggestion.png" alt-text="Screenshot showing the notification ":::

2. Set the start up app.

   Tap on **Set** to set the app as the startup. The user sees a success message that confirms the app is set to open as the startup app.

   :::image type="content" source="media/set-startup-app-mobile/success-message-after-tap.png" alt-text="Screenshot that shows the success message that appears after you tap Set.":::

3. Confirm success with the startup app icon.

   If an app is successfully marked as the startup app, an icon appears next to the app title on the home page.

   :::image type="content" source="media/set-startup-app-mobile/startup-app-icon-near-app-title.png" alt-text="Screenshot that shows the app icon near the app title, which means the app is now a startup app.":::

### If the suggestion is dismissed

- If a user closes the suggestion, they're asked if they want to receive the suggestion in the future. Canceling the suggestion or tapping outside of it closes the suggestion dialogue.

  :::image type="content" source="media/set-startup-app-mobile/dismiss-suggestions-dialogue.png" alt-text="Screenshot that shows the Dismiss Suggestions? dialog box.":::

- If users close the suggestion permanently, they can still set a startup app later from the app **Details** page.

  :::image type="content" source="media/set-startup-app-mobile/can-mark-app-from-app-details.png" alt-text="Screenshot that shows the notification banner that tells you to press i if you want to mark an app as a startup app.":::

## Set a startup app from the **Details** page

To set a startup app from the **Details** page, follow these steps.

1. Tap the **Open at startup** icon on the app **Details** page.

   :::image type="content" source="media/set-startup-app-mobile/set-app-from-deatils-page.png" alt-text="Screenshot that shows where the Open at startup icon is located on the Details page of the app.":::

   After you tap the icon, the app is marked as a startup app.

1. View or dismiss the usage message for offline scenarios.

   This usage message disappears in 10 seconds if not canceled by users.

   :::image type="content" source="media/set-startup-app-mobile/usage-message-from-details-page.png" alt-text="Screenshot that shows usage details for offline scenarios in a message.":::

## Reset a startup app

If an app is already marked as the startup app, the app **Details** page shows a **Remove from startup** icon.

1. Tap this icon to unmark the app as the startup app.

   :::image type="content" source="media/set-startup-app-mobile/remove-from-startup-icon.png" alt-text="Screenshot that shows where the Remove from startup icon is located on the Details page.":::

   You see a message that the app no longer opens by default when a user taps on the Power Apps mobile page.

   :::image type="content" source="media/set-startup-app-mobile/app-no-longer-opens-as-startup.png" alt-text="Screenshot that shows a message confirming that the app will no longer open when starting up.":::

1. Tap **Ok** to replace the existing startup app with another app. The existing app is now unmarked and the new app is marked as the startup app.

   :::image type="content" source="media/set-startup-app-mobile/user-asked-about-replacement-app.png" alt-text="Screenshot that shows the confirmation message where you tap OK to change the startup app.":::

## Known limitations

- Only canvas and model driven apps are eligible for this feature.
- This feature works only on iOS and Android devices.
- Users can set only one app as the startup app.
- Only end users can set a startup app.
