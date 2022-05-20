---
title: Overview of wrap (preview)
description: Learn about the wrap functionality in Power Apps.
author: larryk78
ms.topic: article
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 04/07/2022
ms.subservice: canvas-maker
ms.author: lknibb
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - larryk78
---

# Overview of wrap (preview)

[This article is pre-release documentation and is subject to change.]

The **wrap** feature in Power Apps enables you to *wrap* your canvas apps as custom-branded Android and iOS apps, for native distribution to mobile users.

:::image type="content" source="media/wrap-intro/wrap.png" alt-text="Canvas apps published to mobile users as mobile app package using wrap feature." border="false":::

**Wrap** brings mobile application development platform (MADP) capabilities to Power Apps.

- **No-code mobile app development**&mdash;make mobile apps with no previous experience
- **Managed mobile app builds**&mdash;we generate the app for you
- **Seamless end-to-end branding**&mdash;use your own logo and color palette
- **Multiple canvas apps support**&mdash;bundle multiple apps in a single mobile app
- **Enterprise governance with Microsoft Intune**&mdash;protect your data with app management

> [!IMPORTANT]
> - This is a preview feature.
> - [!INCLUDE[cc_preview_features_definition](../../../includes/cc-preview-features-definition.md)] To submit feedback, or report a problem with this feature, send an email to <pamobsup@microsoft.com>.
> - This preview feature is currently available only in North America (NAM) and United Kingdom (UK) environments.

## Overview

The **wrap** feature in Power Apps lets you *wrap* your canvas apps as custom-branded Android and iOS apps for distribution to mobile users through Intune or other native distribution channels.

The following section explains steps involved in using the wrap feature to create mobile apps:

:::image type="content" source="media/wrap-intro/wrap-steps.png" alt-text="Steps involved in using wrap feature to create mobile apps." border="false":::

1. Start with your primary canvas app. A primary canvas app is the app that provides the initial experience you want your mobile users to see when they launch your mobile app. Ensure this canvas app is part of a solution (if not, create a new solution and add the canvas app).
1. Register your soon-to-be mobile app in Azure portal to allow it to connect to your company resources, including the Power Apps online service.
1. Set up a Visual Studio App Center storage location to store the builds of your mobile app.
1. Create a wrap project from the primary app.
1. Optionally, add additional canvas apps to the solution and to the wrap project. More information: [Wrapping multiple canvas apps together](#wrap-multiple-canvas-apps-together)
1. Customize app branding with icons, images, and color palette to personalize your mobile app.
1. Start the build process to generate your custom-branded mobile app.
1. Download your mobile app from the App Center.
1. Sign and test the app package.
1. Distribute the app package to mobile users.

## Wrap multiple canvas apps together

You can wrap more than one canvas apps as a single mobile app package. The mobile app package still needs a home app, called as the primary app. This app becomes the entry point for all other canvas apps included in the mobile app package, which are called as secondary apps.

Secondary apps are optional. When you wrap only one canvas app, the included app is still designated as a primary app, but the mobile app package would have no secondary apps.

As the following illustration explains, a primary app can have links to multiple secondary apps. The movement between primary and secondary apps inside such mobile app wrapped together can be managed with the [Launch()](../../canvas-apps/functions/function-param.md) function.

:::image type="content" source="media/wrap-intro/primary-secondary-apps.png" alt-text="Primary and secondary apps wrapped together." border="false":::

## Brand your mobile app

Wrap supports customization of the mobile app bootstrap experience to match the branding requirements of your organization. You can specify the app icon, splash screen image, welcome (sign in) screen image, and color palette to use throughout the native experiences of the mobile app.

:::image type="content" source="media/wrap-intro/wrap-branding.png" alt-text="Branding in wrap." border="false":::

Branding customization options are available when you're building your wrap project. More information: [Configure appearance in the wrap project](how-to.md#appearance)

## Understand wrap terminology

Wrap involves multiple components across Power Apps, App Center, and third-party platforms such as iOS and Android. Hence, it becomes important to understand the components involved while working with wrap functionality in Power Apps.

### App Center API token

App Center allows you to create user tokens, and app tokens. Wrap requires the use of app token that allows full access to the app. Power Apps uses this token to connect and work with the app and the app location in App Center.

Consider the following best practices when using API token:

- Use a different token for each app center location.
- Don't reuse token created for wrap capability anywhere else.
- Don't use a user token for wrap. Use an app token.

### App Center container

Container in App Center to store the built packages for mobile app distribution. Build output types differ depending on the target platform you select.

| Platform                                         |  OS | Build Output file type |
|-------------------------------------------------------------|---------------------------|-------------------------------|
| **iOS** (for distribution using Apple Store)                                                         | Custom                    |  \*.zip                       |
| **Android** (for distribution using the Google Play Store)         | Custom                    |      \*.aab                   |
| **Android** (for distribution using all channels except Google Play Store) |  Android                   | \*.apk                       |

### App Center URL

App Center URL refers to the URL and the location of the app you created in App Center that you want to use for storing the distributable builds for mobile users.

### App platform(s)

Intended platforms for the app that you want to go through the build process for publication. You can create builds for mobile app for iOS, Android, or Google Play Store.

- **iOS** creates IPA package
- **Android** creates APK package
- **Google Play Store** creates AAB package

### Application (client) ID

Also called the client ID, this value uniquely identifies your application in the Microsoft identity platform.

More information: [Quickstart: Register an application with the Microsoft identity platform](/azure/active-directory/develop/quickstart-register-app).

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

[Wrap canvas apps as a native mobile app (preview)](how-to.md)

### See also

- [Code sign on iOS (preview)](code-sign-ios.md)
- [Code sign on Android (preview)](code-sign-Android.md)
- [Frequently Asked Questions](faq.yml)
