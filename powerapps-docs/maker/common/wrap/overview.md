---
title: Overview of wrap
description: Learn about the wrap functionality in Power Apps.
author: komala2019
ms.topic: conceptual
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

The **wrap** feature in Power Apps enables you to package your canvas apps as custom-branded Android and iOS apps for native distribution to mobile users. You can distribute these wrapped native mobile apps to end users through [Google Play Store](https://support.google.com/googleplay/work/answer/6138458) and [Apple Business Manager](https://developer.apple.com/custom-apps/) or Microsoft Intune.

:::image type="content" source="media/wrap-intro/wrap.png" alt-text="Canvas apps published to mobile users as mobile app package using wrap feature." border="false":::

---

## Key capabilities

With wrap, you can:

- Package a single or multiple Power Apps canvas apps in the same native mobile app package
- Customize your mobile app startup experience to match your organization's branding
- Specify app icon, splash screen image, welcome screen image, and color palette
- Update wrapped mobile apps by publishing changes to the included canvas app(s) through the [Power Apps](https://make.powerapps.com) maker portal
- Allows distribution using MDM

> [!NOTE]
> All published changes to the included canvas app(s) are downloaded automatically by existing, released versions of your wrapped mobile apps.

---

## Benefits of wrap

**Wrap** brings native mobile application development platform (MADP) capabilities to Power Apps:

| Benefit | Description |
|---------|-------------|
| **No-code mobile app development** | Create mobile apps with no previous experience |
| **Managed mobile app builds** | We generate the app for you |
| **Seamless end-to-end branding** | Use your own logo and color palette |
| **Multiple canvas apps support** | Bundle multiple apps in a single mobile app |
| **Enterprise governance with Microsoft Intune** | Protect your data with app management |
  
---

## Software and device requirements

### Platforms supported

- **iOS**: Version 14.0 and later
- **Android**: Version 8.0 (API level 26) and later

### Device requirements

- **iOS**: iPhone 6S or later, iPad 5th generation or later
- **Android**: Any device running Android 8.0 or later

### Developer requirements

- Microsoft Power Apps account with appropriate licenses
- Access to Microsoft Entra ID (formerly Azure AD) for app registration
- Azure subscription (for Azure Key Vault and Blob Storage)
- For manual code signing:
  - iOS: macOS device with Xcode installed
  - Android: Windows PC with Android Studio installed

---

## Wrap process overview

The **wrap** feature packages your canvas apps in a native mobile app shell and produces a mobile package. You can digitally sign and distribute this mobile package as your custom-branded Android and iOS apps through native distribution channels like [Google Play Store](https://support.google.com/googleplay/work/answer/6138458) and [Apple Business Manager](https://developer.apple.com/custom-apps/).

### Step-by-step process

1. Select your **primary canvas app** and start the wrap wizard. A primary canvas app provides the initial experience users see when launching your mobile app. Your canvas apps must be part of a solution. More information: [Add canvas app to solution](prerequisites.md#add-canvas-app-to-solution).

2. Optionally, add **secondary canvas apps** to your mobile app in the wrap wizard. More information: [Wrapping multiple canvas apps together](#wrap-multiple-canvas-apps-together).

3. Select the **target platforms** (iOS and Android) for your mobile app. Optionally, select **automatically code sign** your mobile app package.

4. Register your app. Use an existing **app registration** or create a new one in the wrap wizard.

5. Customize **app branding** with icons, images, and color palette to personalize your mobile app.

6. Add **Azure blob storage account name and container name**. Use an existing **Azure blob storage** or create a new one.

7. Start the build process in the **Wrap up** step to generate your custom-branded mobile app.

8. Download your mobile app from the **App blob storage location**.

9. If you didn't choose **automatically code sign** in the wrap wizard, you must **code sign** the mobile app package manually. More information: [Signing your mobile app package manually](wrap-how-to.md#sign-your-mobile-app-package-manually-optional).

10. Test the app package.

11. Distribute the app package to mobile users.

---

## Wrap multiple canvas apps together

You can wrap more than one canvas app into a single mobile app package. The mobile app package needs a home app, called the primary app. This app becomes the entry point for all other canvas apps included in the mobile app package, which are called secondary apps.

Secondary apps are optional. When you wrap only one canvas app, that app is considered the primary app, and the mobile app package has no secondary apps.

As shown in the illustration below, a primary app can have links to multiple secondary apps. You can manage navigation between primary and secondary apps using the [Launch()](../../canvas-apps/functions/function-param.md) function.

:::image type="content" source="media/wrap-intro/primary-secondary-apps.png" alt-text="Primary and secondary apps wrapped together." border="false":::

---

## Brand your mobile app

Wrap supports customization of the mobile app bootstrap experience to match your organization's branding requirements. You can specify:

- App icon
- Splash screen image
- Welcome (sign in) screen image
- Color palette for native experiences

:::image type="content" source="media/wrap-intro/wrap-branding.png" alt-text="Branding in wrap." border="false":::

Branding customization options are available when building your wrap project. More information: [Configure branding](wrap-how-to.md#step-4-configure-branding)

---

## Wrap terminology

Wrap involves multiple components across Power Apps and third-party platforms such as iOS and Android. Understanding these components is important when working with the wrap functionality.

### App platform(s)

Target platforms for your app during the build process. You can create builds for:

- **iOS** — creates IPA package
- **Android** — creates APK package
- **Google Play Store** — creates AAB package for distribution

### Bundle ID

The bundle ID is a unique identifier for your app that follows a reverse domain name pattern. It must contain one period (.) and no spaces. Example: `com.contoso.myapp`.

This bundle ID is used when [creating the Azure key vault for wrap](create-key-vault-for-code-signing.md) after iOS or Android certificates are created and uploaded. If you've already created the Azure key vault, verify the bundle ID in the **Tags** section of the [Azure portal](https://portal.azure.com). Use this same bundle ID in [Step 2: Target platform](wrap-how-to.md#step-2-target-platform).

### Code signing

Code signing completes a mobile app before distribution to end users. A code-signed app assures users it comes from a known source and the app code hasn't changed since it was last signed by the trusted source.

### Primary app

A primary app is the entry point or home app for the mobile app experience when wrapping multiple canvas apps together. If only one canvas app is wrapped, it's considered the primary app.

### Secondary app

Secondary apps are optional canvas apps that you wrap in the same build for mobile app distribution along with the [primary app](#primary-app).

### Redirect URI

A redirect URI (reply URL) is the location where the authorization server sends the user after successful app authorization and access token grant. The authorization server sends the code or token to the redirect URI, so registering the correct location during app registration is important. More information: [Redirect URI](/azure/active-directory/develop/reply-url)

---

## Common issues and limitations

### Known limitations

- The wrap feature only supports canvas apps (not model-driven apps)
- All canvas apps in a wrap project must be from the same environment
- Users must have a Power Apps license to use wrapped apps

### Common issues

- **Bundle ID conflicts**: Ensure your bundle ID is unique across your organization
- **Image format issues**: All images must be in PNG format
- **Signing certificate problems**: Verify certificate validity and expiration dates
- **Azure Key Vault access**: Make sure proper permissions are configured

For troubleshooting details, see [Troubleshoot issues with the wrap feature in Power Apps](/troubleshoot/power-platform/power-apps/manage-apps/wrap-issues).

---

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
