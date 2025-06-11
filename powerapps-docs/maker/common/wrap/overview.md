---
title: Overview of wrap
description: Learn about the wrap functionality in Power Apps.
author: komala2019
ms.topic: article
ms.custom: canvas
ms.reviewer: smurkute
ms.date: 02/04/2025
ms.subservice: canvas-maker
ms.author: koagarwa
search.audienceType: 
  - maker
contributors:
  - mduelae
---

# Overview of wrap

The **wrap** feature in Power Apps allows you to package your canvas apps as custom-branded Android and iOS apps for native mobile distribution. You can distribute these wrapped apps to users through the [Google Play Store](https://support.google.com/googleplay/work/answer/6138458) and [Apple Business Manager](https://developer.apple.com/custom-apps/).

:::image type="content" source="media/wrap-intro/wrap.png" alt-text="Canvas apps published to mobile users as mobile app package using wrap feature." border="false":::

With wrap, you can include one or more Power Apps canvas apps in a single native mobile app package. The wrap feature lets you customize the startup experience to match your organization's branding, including app icon, splash screen, welcome (sign-in) screen, and color palette.

You can update your wrapped mobile apps by publishing changes to the canvas app(s) included in the package using the [Power Apps](https://make.powerapps.com) maker portal.

> [!NOTE]
> All published changes to the included canvas app(s) are automatically downloaded by existing, released versions of your wrapped mobile apps.

**Wrap** brings native mobile application development platform (MADP) capabilities to Power Apps, including:

- **No-code mobile app development**: Build mobile apps without prior experience.
- **Managed mobile app builds**: The platform generates the app package for you.
- **Seamless end-to-end branding**: Use your own logo and color palette.
- **Multiple canvas apps support**: Bundle several apps in a single mobile app.
- **Enterprise governance with Microsoft Intune**: Protect your data with app management.

> [!NOTE]
> **Wrap** is intended for distributing mobile apps to existing Power Apps users, not for public distribution.

## Understand the wrap process

The wrap feature packages your canvas apps in a native mobile app shell and produces a mobile package. You can digitally sign and distribute this package as your custom-branded Android and iOS app through native channels like [Google Play Store](https://support.google.com/googleplay/work/answer/6138458) and [Apple Business Manager](https://developer.apple.com/custom-apps/).

The main steps in the wrap process are:

1. Select your **primary canvas app** and start the wrap wizard. The primary app is the initial experience for users. Your canvas apps must be part of a solution. More information: [Add canvas app to solution](prerequisites.md#add-canvas-app-to-solution).
2. Optionally, add **secondary canvas apps** to your mobile app in the wrap wizard. More information: [Wrapping multiple canvas apps together](#wrap-multiple-canvas-apps-together).
3. Select the **target platforms** (iOS and Android) for your mobile app. Optionally, choose to **automatically code sign** your app package.
4. Register your app. Use an existing **app registration** or create a new one in the wrap wizard.
5. Customize **app branding** with icons, images, and color palette.
6. Add your **Azure blob storage account name and container name**. Use an existing Azure blob storage or create a new one.
7. Start the build process in the **Wrap up** step to generate your custom-branded mobile app.
8. Download your mobile app from the **App blob storage location**.
9. If you did not choose automatic code signing, **code sign** the mobile app package manually. More information: [Signing your mobile app package manually](wrap-how-to.md#sign-your-mobile-app-package-manually-optional).
10. Test the app package.
11. Distribute the app package to your mobile users.

## Wrap multiple canvas apps together

You can include more than one canvas app in a single mobile app package. The package requires a home app, called the primary app, which serves as the entry point. Other included apps are secondary apps.

Secondary apps are optional. If you wrap only one canvas app, it is the primary app and there are no secondary apps.

As shown below, a primary app can link to multiple secondary apps. Navigation between primary and secondary apps can be managed with the [Launch()](../../canvas-apps/functions/function-param.md) function.

:::image type="content" source="media/wrap-intro/primary-secondary-apps.png" alt-text="Primary and secondary apps wrapped together." border="false":::

## Brand your mobile app

Wrap supports customizing the mobile app's startup experience to match your organization's branding. You can specify the app icon, splash screen image, welcome (sign-in) screen image, and color palette for the native app experience.

:::image type="content" source="media/wrap-intro/wrap-branding.png" alt-text="Branding in wrap." border="false":::

Branding customization options are available when building your wrap project. More information: [Configure branding](wrap-how-to.md#step-4-configure-branding)

## Understanding wrap terminology

Wrap involves several components across Power Apps and third-party platforms such as iOS and Android. Understanding these components is important when working with wrap functionality.

### Azure blob storage

Azure Blob Storage containers store built packages for mobile app distribution. Build output types differ depending on the target platform.

- **Account Name**: Unique identifier for your Azure Storage account, used to construct the base URI.
- **Container Name**: Unique identifier within a storage account that groups a set of blobs.

### App platform(s)

The platforms you want to build for: iOS, Android, or Google Play Store.

- **iOS**: Creates an IPA package.
- **Android**: Creates an APK package.
- **Google Play Store**: Creates an AAB package for distribution.

### Build the wrap project

Building a wrap project creates the build packages for mobile app distribution across different platforms. This uses the app registered on Microsoft identity platform and creates builds in your Azure blob storage location.

### Bundle ID

A unique identifier for your app, following a reverse domain name pattern (e.g., `com.contoso.myapp`). The bundle ID is used during [Azure key vault creation](create-key-vault-for-code-signing.md) and in [Step 2: Target platform](wrap-how-to.md#step-2-target-platform).

### Code signing

Code signing completes a mobile app before distribution, assuring users that the app comes from a trusted source and hasn't been altered.

### Primary app

The entry point or home app for the mobile experience when wrapping multiple canvas apps. If only one app is wrapped, it is the primary app.

### Redirect URI

A redirect URI (reply URL) is where the authorization server sends the user after successful authorization. Register the correct URI during app registration.

More information: [Redirect URI](/azure/active-directory/develop/reply-url)

### Secondary app

Optional additional canvas apps included in the same build for distribution with the [primary app](#primary-app).

## Next steps

[System requirements and prerequisites for Wrap](prerequisites.md)  

### See also

- [Use the wrap wizard to build your mobile app](wrap-how-to.md)
- [Manual code sign on iOS](code-sign-ios.md)
- [Manual code sign on Android](code-sign-Android.md)
- [Code sign for Google Play Store](https://developer.android.com/studio/publish/app-signing)
- [Create your Azure Key Vault for automated code signing](create-key-vault-for-code-signing.md)
- [Frequently Asked Questions](faq.yml)
- [Troubleshoot issues with the wrap feature in Power Apps](/troubleshoot/power-platform/power-apps/manage-apps/wrap-issues)
- [Benefits and limitations of Wrap](limitations.md)
