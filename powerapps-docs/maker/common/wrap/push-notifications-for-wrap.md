---
title: Set up push notifications for wrap 
description: Learn how to set up push notifications for your Power Apps wrap app on iOS and Android. Follow the step-by-step instructions to keep users engaged with timely alerts. 
author: Murugesh1985
ms.author: murugeshs
ms.reviewer: smurkute
ms.date: 03/16/2026
ms.topic: how-to
---

# Set up push notifications for wrap  

By using push notifications, your custom branded, white-labeled Power Apps wrapped app can alert users with messages, even when they're not actively using the app. This article walks you through everything you need to set up push notifications for iOS, Android, or both. 

## Prerequisites

Make sure you have the following items ready before you start: 

| **Requirement**  | **Details**  |
|----|----|
| A wrap build  | You must already configure your Power Apps canvas app for wrapping.  |
| Apple Developer account  | Required for iOS only. Sign up at [developer.apple.com](https://developer.apple.com).  |
| Firebase account  | Required for both iOS and Android. Sign up at [console.firebase.google.com](https://console.firebase.google.com).  |

## How it works 

Your wrap app uses Firebase Cloud Messaging (FCM) to deliver push notifications. Here's what happens when a user opens the app: 

1.  The app checks whether push notifications are turned on in the wrap Wizard. 
1.  If enabled, the app asks the user for permission and registers the device to receive notifications. 
1.  The device is subscribed to two notification channels: 
    - **All users**: for notifications sent to everyone. 
    - **Individual user**: for notifications sent to a specific user, identified by their sign-in email. 
1.  FCM handles delivery on both platforms. On iOS, it routes through Apple's Push Notification service (APNs). On Android, it delivers through Google's messaging service. 

> [!NOTE]
> On Android 13 and later, users must explicitly allow notifications. The app automatically prompts for this permission after sign-in. If the user denies the permission prompt, notifications don't appear and the user must manually re-enable notifications from **system settings**. 

## Step 1: Configure your Apple developer account (iOS only) 

Set up two things in your Apple Developer account: 
1. Verify your app is configured to receive push notifications 
1. Create a key that lets Firebase communicate with Apple on your behalf

Next, create an APNs auth key that Firebase uses to send notifications to Apple devices on your behalf. One key works across all your apps and environments (development and production). 

1. Go to your Apple developer account.  
1. In the left sidebar, select **Keys**, and then select **+**. 
1. Give the key a descriptive name, such as *PowerAppsWrapPushNotifications*.
1. Select the toggle **Apple Push Notifications service** (APNs) and select **Configure**. 
1. In **Configure Key**, select **environment** and **Save**. 
1. Select **Continue** and select **Register**. 
1. After you register the key, select **Download** to save the .p8 key file. 

> [!NOTE]
> Firebase uses token‑based APNs authentication (.p8 key). This authentication works for both development and production builds. Use the production environment when you configure the APNs Authentication Key. 

> [!IMPORTANT]
> Save the .p8 file somewhere secure right away. Apple only lets you download it once. If you lose it, you need to revoke the key and start over. You can have up to two active APNs keys per account. 

Keep note of these two values, you'll need them in the next step: 

- **Key ID**: the 10-character code shown on the key details page 

- **Team ID**: shown in the top-right corner of the portal, or under Membership 

:::image type="content" source="media/push-notifications-for-wrap/key-id-in-iOS.png" alt-text="Screenshot of the Apple Developer portal showing the Key ID and Team ID values for APNs key configuration."::: 

> [!IMPORTANT]
> Ensure the Apple App ID you use for your wrap build has the following capabilities enabled in the Apple Developer portal: 
> 1. Push Notifications 
> 2. Background Modes > Remote notifications. 
> If **Background Modes** isn't enabled, the app might successfully register with Firebase, but push notifications don't get delivered when the app is backgrounded or terminated. 

## Step 2: Set up Firebase 

Firebase manages notification delivery for both iOS and Android. Register your apps and connect Apple's APNs key to your Firebase project. 

### Create or open a Firebase project 

1. Go to [Firebase console](https://console.firebase.google.com) and sign in. 
1. Select an existing project, or select **Create a project** to make a new one. 

### Add Firebase to your iOS app 

1. In **Project Overview**, select **Add app** (+ icon) and select **iOS** (icon). 
1. Enter your app's **Bundle ID**. The **Bundle ID must match exactly** across Apple App ID, Firebase iOS app configuration, and wrap build configuration.
1. Complete the setup and download the `GoogleService-Info.plist` file. Include this file in your wrap build within Power Apps studio. 

### Connect your APNs key to Firebase (iOS only) 

This step authorizes Firebase to deliver notifications through Apple's servers: 

1. In Firebase console, go to your iOS project.  

1. Go to **Settings** > **Cloud Messaging**. 

1. Under **Apple app configuration**, find your iOS app. 

1. Select **Upload** in the **APNs Authentication Key** section. 

1. Select the .p8 file you downloaded from Apple. 

1. Enter your Key ID and Team ID, and then select **Upload**. 

### Add your Android app to Firebase 

1. In **Project Overview**, select **Add app** and choose **Android**. 

1. Enter your Android package name (for example, com.microsoft.msapps). 

1. Complete the setup and download the google-services.json file for your wrap build. 

## Step 3: Enable push notifications in the wrap wizard 

After you configure Firebase, turn on push notifications in your wrap app: 

1. Open your canvas app in Power Apps Studio. 
1. Select **Wrap** and go to **Target Platforms Step**. 
1. Turn on the Push notifications toggle for iOS, Android, or both, depending on your needs.  
    :::image type="content" source="media/push-notifications-for-wrap/wrap-wizard-push-notification.png" alt-text="Screenshot of the Wrap Wizard target platforms step showing the push notifications toggle for iOS and Android."::: 
1. Upload the GoogleService-Info.plist file (iOS) and the google-services.json file (Android). 
1. Complete and publish your wrap build. 

> [!NOTE]
> The wrap wizard push notifications toggle only controls device registration.   
> Push notifications aren't delivered unless: 
> 
> - You complete the Apple App ID and Firebase setup. 
> 
> - You enable the required capabilities and permissions. 

## Step 4: Test by sending test notification

The quickest way to verify your setup is to send a test notification from Firebase: 

1. In Firebase console, go to your project, and then select **Cloud Messaging** > **New Campaign** > **Compose Notification**. 
1. Enter **Notification title** and **Text**. 
1. Under **Target**, select **User segment** and select your app in **Target user if** dropdown. Alternatively, under **Target**, select **Topic** and enter an email address in the **Message topic** field. To test notifications for a specific user, use an email address without special characters as the topic name. Firebase topic names don't support special characters, so the app automatically converts the email by lowercasing it and stripping out anything that isn't a letter, number, or `-_.~%`. For example: 

    | **Email address**             | **Topic name used**      |
    |--------------------------------|--------------------------|
    | <john.doe@contoso.com>        | johndoecontosocom       |
    | <jane.smith+test@company.com> | janesmithtestcompanycom |
1. Under **Scheduling**, select appropriate options and select **Review**. 
1. Select **Send** and check that the notification appears on a test device. 
1. When you send test notifications from Firebase Cloud Messaging, make sure you select the **correct iOS or Android app** under the project. Sending a campaign at the project level or to the wrong app might result in notifications not being delivered. 
1. Expected behavior is:

    | **App state**      | **Result**                                |
    |--------------------|-------------------------------------------|
    | App terminated     | App launches when notification is tapped  |
    | App in background  | App resumes                               |
    | App in foreground  | Notification banner only                  |

 

## Related information 
Apple and Firebase portals frequently evolve. If UI labels or navigation differ from the above screenshots or steps, see the official documentation for the latest guidance. 
   
- [Get started with Firebase Cloud Messaging in Apple platform apps](https://firebase.google.com/docs/cloud-messaging/ios/get-started) is used for Firebase cloud messaging iOS setup and uploading APNs authentication key.
- [Establishing a token-based connection to APNs](https://developer.apple.com/documentation/usernotifications/establishing-a-token-based-connection-to-apns) explains token‑based APNs auth, why it's preferred, and environment behavior. 
- [Pushing background updates to your App](https://developer.apple.com/documentation/usernotifications/pushing-background-updates-to-your-app) confirms why **Background Modes > Remote notifications** must be enabled.   
- [Notifications in iOS](https://developer.apple.com/notifications/) gives high‑level Apple guidance if behaviour differs across iOS versions.


