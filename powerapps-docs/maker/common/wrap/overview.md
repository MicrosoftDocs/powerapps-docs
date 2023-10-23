---
title: Overview of wrap
description: Learn about the wrap functionality in Power Apps.
author: larryk78
ms.topic: article
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 06/08/2022
ms.subservice: canvas-maker
ms.author: mkaur
search.audienceType: 
  - maker
contributors:
  - mduelae
---

# Overview of wrap


The **wrap** feature in Power Apps enables you to *wrap* your canvas apps as custom-branded Android and iOS apps for native distribution to mobile users. You can distribute such wrapped native mobile apps to the end users through [Microsoft Intune](/mem/intune/fundamentals/what-is-intune), [Microsoft App Center](https://visualstudio.microsoft.com/app-center/), [Google Play Store](https://support.google.com/googleplay/work/answer/6138458) and [Apple Business Manager](https://developer.apple.com/custom-apps/).

:::image type="content" source="media/wrap-intro/wrap.png" alt-text="Canvas apps published to mobile users as mobile app package using wrap feature." border="false":::

You can wrap a single or multiple Power Apps canvas apps in the same native mobile app package. You can use wrap feature to customize your mobile app start up experience to match the branding requirements of your organization. You can specify the app icon, splash screen image, welcome (sign in) screen image, and color palette to use in the mobile app.

You can update the wrapped mobile apps by publishing changes to the canvas app(s) that are included in the mobile package using the [Power Apps](https://make.powerapps.com) maker portal. All published changes to the included canvas app(s) are downloaded automatically by the existing, released versions of your wrapped mobile apps. 


**Wrap** brings native mobile application development platform (MADP) capabilities to Power Apps.

- **No-code mobile app development**&mdash;make mobile apps with no previous experience
- **Managed mobile app builds**&mdash;we generate the app for you
- **Seamless end-to-end branding**&mdash;use your own logo and color palette
- **Multiple canvas apps support**&mdash;bundle multiple apps in a single mobile app
- **Enterprise governance with Microsoft Intune**&mdash;protect your data with app management

## Understand wrap process

The **wrap** feature will *wrap* your canvas apps in a native mobile app shell and produce a mobile package. You can digitally sign and distribute this mobile package as your custom-branded Android and iOS apps to mobile users through the native distribution channels like [Microsoft Intune](/mem/intune/fundamentals/what-is-intune), [Microsoft App Center](https://visualstudio.microsoft.com/app-center/), [Google Play Store](https://support.google.com/googleplay/work/answer/6138458) and [Apple Business Manager](https://developer.apple.com/custom-apps/).

The following section explains steps involved in using the wrap feature to create native mobile apps:

:::image type="content" source="media/wrap-intro/wrap-steps.png" alt-text="Steps involved in using wrap feature to create mobile apps." border="false":::

1. Select your **primary canvas app** and start wrap wizard. A primary canvas app is the app that provides the initial experience you want your mobile users to see when they launch your mobile app. Your canvas apps must be part of a solution. More information: [Add canvas app to solution](wrap-how-to.md#add-canvas-app-to-solution).
1. Optionally, add **secondary canvas apps** to your mobile app in wrap wizard. More information: [Wrapping multiple canvas apps together](#wrap-multiple-canvas-apps-together).
1. Select the **target platforms** (iOS and Android) for your mobile app. Optionally, select to **automatically code sign** your mobile app package in wrap wizard.
1. Customize **app branding** with icons, images, and color palette to personalize your mobile app.
1. Register you app. Use an existing **app registration**, or create a new one in wrap wizard. 
1. Select **App Center location** to store your mobile app. Use an existing **App Center location** or create a new one in wrap wizard. 
1. Start the build process in **Wrap up** step to generate your custom-branded mobile app.
1. Download your mobile app from the **App Center location**.
1. If **automatically code sign** is not chosen in wrap wizard, you must **code sign** the mobile app package manually. More information: [Signing your mobile app package manually](wrap-how-to.md#sign-your-mobile-app-package-manually-optional).
1. Test the app package.
1. Distribute the app package to mobile users.

## Wrap multiple canvas apps together

You can wrap more than one canvas apps as a single mobile app package. The mobile app package still needs a home app, called as the primary app. This app becomes the entry point for all other canvas apps included in the mobile app package, which are called as secondary apps.

Secondary apps are optional. When you wrap only one canvas app, the included app is still designated as a primary app, but the mobile app package would have no secondary apps.

As the following illustration explains, a primary app can have links to multiple secondary apps. The movement between primary and secondary apps inside such mobile app wrapped together can be managed with the [Launch()](../../canvas-apps/functions/function-param.md) function.

:::image type="content" source="media/wrap-intro/primary-secondary-apps.png" alt-text="Primary and secondary apps wrapped together." border="false":::

## Brand your mobile app

Wrap supports customization of the mobile app bootstrap experience to match the branding requirements of your organization. You can specify the app icon, splash screen image, welcome (sign in) screen image, and color palette to use throughout the native experiences of the mobile app.

:::image type="content" source="media/wrap-intro/wrap-branding.png" alt-text="Branding in wrap." border="false":::

Branding customization options are available when you're building your wrap project. More information: [Configure branding](wrap-how-to.md#step-3-configure-branding)

## System requirements

The following list explains what you'll need before you can start using wrap feature to publish one or more canvas apps as a mobile app package.

### Permissions and access requirements

- Access to one or more [canvas apps](../../canvas-apps/share-app.md) to build the wrap project
- Access to Azure portal to create [app registration](/azure/active-directory/develop/quickstart-register-app#prerequisites)
- Access to [Microsoft App Center](https://appcenter.ms/)

### Software and device requirements

- Mac device for [code signing with iOS](code-sign-ios.md)
- Windows PC for [code signing with Android](code-sign-android.md)
- To run the wrapped mobile app:
    - Android device with version 10 or higher
    - iOS device with version 14 or higher

> [!NOTE]
> Developing apps for the iOS platform requires an [Apple Developer Program](https://developer.apple.com/) account.

## Understanding wrap terminology

Wrap involves multiple components across Power Apps, App Center, and third-party platforms such as iOS and Android. Hence, it becomes important to understand the components involved while working with wrap functionality in Power Apps.

### App center location

Container in App Center to store the built packages for mobile app distribution. Build output types differ depending on the target platform you select.

| Platform                                         |  OS | Build Output file type |
|-------------------------------------------------------------|---------------------------|-------------------------------|
| **iOS** (for distribution using Apple Store)                                                         | Custom                    |  \*.zip                       |
| **Android** (for distribution using all channels except Google Play Store) |  Android                   | \*.apk                       |

### App platform(s)

Intended platforms for the app that you want to go through the build process for publication. You can create builds for mobile app for iOS, Android, or Google Play Store.

- **iOS** creates IPA package
- **Android** creates APK package
- **Google Play Store** creates AAB package
   
### Build the wrap project

Building a wrap project is a process that creates the build packages for the mobile app distribution across different platforms. This process uses the app that you registered on Microsoft identity platform and creates the builds on the given App Center location depending on the platforms you choose. The built packages include the primary and optional secondary apps packaged into one mobile app package for each platform type.

### Bundle ID

A globally unique identity of the output mobile app. Follows a reverse domain name pattern. For example, `com.contoso.myapp`.

### Code signing

Code signing is the process of finalizing a mobile app prior to distribution to end users. An app that is code signed assures that it comes from a known source, and the app code hasn't changed since last time it was signed by the trusted source.

### Primary app

A primary app is the entry point or the home app for the mobile app experience when wrapping more than one canvas apps together. All additional apps are considered [secondary apps](#secondary-app). If only one canvas app is wrapped and built, it's also considered the primary app.

### Redirect URI

A redirect URI, or reply URL, is the location where the authorization server sends the user once the app has been successfully authorized and granted an authorization code or access token. The authorization server sends the code or token to the redirect URI, so it's important you register the correct location as part of the app registration process.

More information: [Redirect URI](/azure/active-directory/develop/reply-url)

### Secondary app

Optional additional canvas apps that you're wrapping in the same build for mobile app distribution along with the [primary app](#primary-app).

## Next steps

[Use the wrap wizard to build your mobile app](wrap-how-to.md) <br>

### See also

- [Troubleshoot issues with the wrap feature in Power Apps](/troubleshoot/power-platform/power-apps/manage-apps-and-solutions/wrap-issues)
- [Code sign on iOS](code-sign-ios.md)
- [Code sign on Android](code-sign-Android.md)
- [Code sign for Google Play Store](https://developer.android.com/studio/publish/app-signing)
- [Create your Azure key vault for automated code signing](create-key-vault-for-code-signing.md)
- [Frequently Asked Questions](faq.yml)
