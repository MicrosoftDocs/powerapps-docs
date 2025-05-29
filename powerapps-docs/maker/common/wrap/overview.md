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


The **wrap** feature in Power Apps enables you to *wrap* your canvas apps as custom-branded Android and iOS apps for native distribution to mobile users. You can distribute such wrapped native mobile apps to the end users through [Google Play Store](https://support.google.com/googleplay/work/answer/6138458) and [Apple Business Manager](https://developer.apple.com/custom-apps/).

:::image type="content" source="media/wrap-intro/wrap.png" alt-text="Canvas apps published to mobile users as mobile app package using wrap feature." border="false":::

You can wrap a single or multiple Power Apps canvas apps in the same native mobile app package. You can use wrap feature to customize your mobile app startup experience to match the branding requirements of your organization. You can specify the app icon, splash screen image, welcome (sign in) screen image, and color palette to use in the mobile app.

You can update the wrapped mobile apps by publishing changes to the canvas app(s) that are included in the mobile package using the [Power Apps](https://make.powerapps.com) maker portal. 


> [!NOTE]
> All published changes to the included canvas app(s) are downloaded automatically by the existing, released versions of your wrapped mobile apps. 


**Wrap** brings native mobile application development platform (MADP) capabilities to Power Apps.

- **No-code mobile app development**&mdash;make mobile apps with no previous experience
- **Managed mobile app builds**&mdash;we generate the app for you
- **Seamless end-to-end branding**&mdash;use your own logo and color palette
- **Multiple canvas apps support**&mdash;bundle multiple apps in a single mobile app
- **Enterprise governance with Microsoft Intune**&mdash;protect your data with app management
  
> [!NOTE]
> **Wrap** is intended for distributing mobile apps to existing Power Apps users, not for public.


## Understand wrap process

The **wrap** feature will *wrap* your canvas apps in a native mobile app shell and produce a mobile package. You can digitally sign and distribute this mobile package as your custom-branded Android and iOS apps to mobile users through the native distribution channels like [Google Play Store](https://support.google.com/googleplay/work/answer/6138458) and [Apple Business Manager](https://developer.apple.com/custom-apps/).

The following section explains steps involved in using the wrap feature to create native mobile apps:


1. Select your **primary canvas app** and start the wrap wizard. A primary canvas app is the app that provides the initial experience you want your mobile users to see when they launch your mobile app. Your canvas apps must be part of a solution. More information: [Add canvas app to solution](prerequisites.md#add-canvas-app-to-solution).
1. Optionally, add **secondary canvas apps** to your mobile app in the wrap wizard. More information: [Wrapping multiple canvas apps together](#wrap-multiple-canvas-apps-together).
1. Select the **target platforms** (iOS and Android) for your mobile app. Optionally, select to **automatically code sign** your mobile app package in the wrap wizard.
1. Register you app. Use an existing **app registration**, or create a new one in the wrap wizard. 
1. Customize **app branding** with icons, images, and color palette to personalize your mobile app.
1. Add **Azure blob storage account name and container name**. Use an already created **Azure blob storage** or create a new one.
1. Start the build process in **Wrap up** step to generate your custom-branded mobile app.
1. Download your mobile app from the **App blob storage location**.
1. If **automatically code sign** isn't chosen in the wrap wizard, you must **code sign** the mobile app package manually. More information: [Signing your mobile app package manually](wrap-how-to.md#sign-your-mobile-app-package-manually-optional).
1. Test the app package.
1. Distribute the app package to mobile users.

## Wrap multiple canvas apps together

You can wrap more than one canvas apps as a single mobile app package. The mobile app package still needs a home app, called as the primary app. This app becomes the entry point for all other canvas apps included in the mobile app package, which are called as secondary apps.

Secondary apps are optional. When you wrap only one canvas app, the included app is still chosen as a primary app, but the mobile app package would have no secondary apps.

As the following illustration explains, a primary app can have links to multiple secondary apps. The movement between primary and secondary apps inside such mobile app wrapped together can be managed with the [Launch()](../../canvas-apps/functions/function-param.md) function.

:::image type="content" source="media/wrap-intro/primary-secondary-apps.png" alt-text="Primary and secondary apps wrapped together." border="false":::

## Brand your mobile app

Wrap supports customization of the mobile app bootstrap experience to match the branding requirements of your organization. You can specify the app icon, splash screen image, welcome (sign in) screen image, and color palette to use throughout the native experiences of the mobile app.

:::image type="content" source="media/wrap-intro/wrap-branding.png" alt-text="Branding in wrap." border="false":::

Branding customization options are available when you're building your wrap project. More information: [Configure branding](wrap-how-to.md#step-4-configure-branding)

## Understanding wrap terminology

Wrap involves multiple components across Power Apps, and third-party platforms such as iOS and Android. Hence, it becomes important to understand the components involved while working with wrap functionality in Power Apps.

### Azure blob storage 

Container in Azure Blob Storage helps store built packages for mobile app distribution. Build output types differ depending on the target platform you select. Details about the feature will be shared before March 31, 2025.

Input:

- [Account Name](#account-name) and [Container Name](#container-name)


#### Account Name

The account name is a unique identifier for your Azure Storage account. It's used to construct the base URI for accessing the storage account. 

#### Container Name

The container name is a unique identifier within a storage account that groups a set of blobs. Containers provide a way to organize blobs within a storage account. 


### App platform(s)

Intended platforms for the app that you want to go through the build process for publication. You can create builds for mobile app for iOS, Android, or Google Play Store.

- **iOS** creates IPA package
- **Android** creates APK package
- **Google Play Store** create AAB package for distribution
   
### Build the wrap project

Building a wrap project is a process that creates the build packages for the mobile app distribution across different platforms. This process uses the app that you registered on Microsoft identity platform and creates the builds on the given Azure blob storage location depending on the platforms you choose. The built packages include the primary and optional secondary apps packaged into one mobile app package for each platform type.

### Bundle ID

The bundle ID is a unique identifier you create for your app. Use any bundle ID name that follows a reverse domain name pattern. A bundle ID must contain one period (.) and no spaces. For example, `com.contoso.myapp`. This bundle ID is used during the process of [creating the Azure key vault for wrap](create-key-vault-for-code-signing.md) once iOS or Android certificates are created and uploaded. If you already created the Azure key vault, verify the bundle ID in the **Tags** section of the [Azure portal](https://portal.azure.com). Use this same bundle ID in [Step 2: Target platform](wrap-how-to.md#step-2-target-platform)

### Code signing

Code signing is the process of completing a mobile app before distribution to end users. An app that is code signed assures that it comes from a known source, and the app code hasn't changed since last time it was signed by the trusted source.

### Primary app

A primary app is the entry point or the home app for the mobile app experience when wrapping more than one canvas apps together. All other apps are considered [secondary apps](#secondary-app). If only one canvas app is wrapped and built, it's also considered the primary app.

### Redirect URI

A redirect URI, or reply URL, is the location where the authorization server sends the user once the app has been successfully authorized and granted an authorization code or access token. The authorization server sends the code or token to the redirect URI, so it's important you register the correct location as part of the app registration process.

More information: [Redirect URI](/azure/active-directory/develop/reply-url)

### Secondary app

Optional more canvas apps that you're wrapping in the same build for mobile app distribution along with the [primary app](#primary-app).

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
