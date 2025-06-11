---
title: Code sign for Android
description: Learn how to code sign for Android for Power Apps wrap.
author: komala2019
ms.topic: how-to
ms.custom: canvas
ms.reviewer: smurkute
ms.date: 03/12/2025
ms.subservice: canvas-maker
ms.author: koagarwa
search.audienceType: 
  - maker
contributors:
  - mduelae
---

# Code sign for Android 

This article explains how to manually code sign your Android (APK) app for Power Apps wrap. You need to sign your app for Android if you selected Android as one of the [platforms](overview.md#app-platforms) when creating and building your [wrap project](wrap-how-to.md#create-custom-branded-native-power-apps-for-ios-and-android-using-the-wrap-wizard).

> [!IMPORTANT]
> If you want to sign an AAB app for Google Play distribution, refer to [Sign your app](https://developer.android.com/studio/publish/app-signing).

## Prepare your PC

To get started, make sure you have:

- [Android Studio](https://developer.android.com/studio) installed
- [OpenSSL](https://slproweb.com/products/Win32OpenSSL.html) installed
- [apksigner tool](https://developer.android.com/studio/command-line/apksigner) set up

## Prerequisites

- Application name for creating the hash key
- Latest APK file for signing

## Generate keys

> [!NOTE]
> Skip to [sign the APK package](#manual-sign-the-apk-package) if you've already generated keys and signature hash while creating the [app registration](wrap-how-to.md#step-3-register-app).

Use **keytool.exe** (installed with Android Studio, usually at `Drive:\Program Files\Android\Android Studio\jre\bin\keytool.exe`) to create a certificate for signing the application package.

If you don't have environment variables set, follow these steps:

1. Download Android Studio and OpenSSL.
2. Add keytool and openssl to your environment variables.  
   - Add `C:\Program Files\Android\Android Studio\jbr\bin` to your PATH.  
   - Add the path of openssl.exe (e.g., `C:\Program Files\OpenSSL-Win64\bin`) to your PATH.
3. Run this command to generate a key:  
   `keytool -genkey -alias powerappswrap -keyalg RSA -keystore powerappswrap.jks -keysize 2048 -validity 10000`
4. Run this command to generate the signature hash:  
   `keytool -exportcert -alias powerappswrap -keystore powerappswrap.jks | openssl sha1 -binary | openssl base64`

:::image type="content" source="media/code-sign-android/codeSignIn3.png" alt-text="A screenshot with keytool command using the parameters in the example shown above." lightbox="media/code-sign-android/codeSignIn3.png":::

If you have environment variables set, you can run:

`keytool -genkey -alias SIGNATURE_ALIAS -keyalg RSA -keystore PATH_TO_KEYSTORE -keysize 2048 -validity 10000`

Parameters:

- **genkey**: command to generate a key
- **alias**: alias for the keystore entry
- **keyalg**: key algorithm name
- **keystore**: name of the keystore
- **keysize**: size of each key
- **validity**: validity of the key in days

Example:
- For Key Vault, use a `.pfx` extension:  
  `keytool -genkey -alias powerappswrap -keyalg RSA -keystore powerappswrap.pfx -keysize 2048 -validity 10000`
- For manual signing, use a `.jks` extension:  
  `keytool -genkey -alias powerappswrap -keyalg RSA -keystore \Users\name\Desktop\powerappswrap.jks -keysize 2048 -validity 10000`

:::image type="content" source="media/code-sign-android/codeSignIn1.png" alt-text="A screenshot with keytool command using the parameters in the above example." lightbox="media/code-sign-android/codeSignIn1.png":::

## Generate signature hash

> [!NOTE]
> Skip to [sign the APK package](#manual-sign-the-apk-package) if you've already generated keys and signature hash while creating the [app registration](wrap-how-to.md#step-3-register-app).

After generating the key, use the **exportcert** command in **keytool** to export the keystore certificate:

`keytool -exportcert -alias SIGNATURE_ALIAS -keystore PATH_TO_KEYSTORE | openssl sha1 -binary | openssl base64`

Parameters:

- **exportcert**: reads the certificate from the keystore
- **alias**: alias used when generating keys
- **keystore**: name of the keystore
- **openssl**: generates SHA1 key for Android

Add the generated signature hash in the **Redirect URI** while [registering the app](wrap-how-to.md#step-3-register-app).

### Convert SHA1 hex to Base64-encoded signature hash manually

If you see the error "The signature hash must be base64-encoded SHA1" in the Azure portal, follow these steps:

1. Run:  
   `keytool -list -v -alias SIGNATURE_ALIAS -keystore PATH_TO_KEYSTORE`
2. Copy the **SHA1** value from the **Certificate fingerprints** section.
   - Example: `EF:11:45:3D:F1:72:D9:8C:43:32:CD:0A:49:C2:E4:75:2D:B3:2D:9F`
3. Use a "Hexadecimal to Base64" converter to convert the SHA1 value to Base64.
   - Example: `8CPPeLaz9etdqQyaQubcqsy2Tw=`
4. Use the Base64 value as the **Signature hash** in the Azure portal when [registering the app](wrap-how-to.md#step-3-register-app).

## Manual sign the APK package

> [!NOTE]
> These steps are required if you haven't wrapped the app using automatic sign-in or are trying to upload an AAB file for Play Store. To avoid repeating this step, we recommend using automatic sign-in.

To sign the APK package, use the [apksigner tool](https://developer.android.com/studio/command-line/apksigner).

### Find your apksigner

1. Check the Android SDK path in Android Studio.
2. Go to **Tool** > **SDK Manager** > **Android SDK Location**.

   If using iOS, check the apksigner file from the **buildTools Version** directory:

   Go to **SDK** directory > **build-tools** > **buildToolsVersion** > **lib**, and check the **apksigner.jar** file.

:::image type="content" source="media/code-sign-android/codeSignIn2.png" alt-text="A screenshot with apksigner location information." lightbox="media/code-sign-android/codeSignIn2.png":::

### Use the apksigner file

Run the following command to sign the package:

`apksigner.bat sign --ks PATH_TO_KEYSTORE --ks-key-alias KEY_ALIAS PATH_TO_APK`

Parameters:

- **ks**: path to the keystore
- **ks-key-alias**: key alias
- **PATH_TO_APK**: path to the APK file

When prompted, enter the password.

More information: [Android Studio command line tools: apksigner](https://developer.android.com/studio/command-line/apksigner)

## Distribute the app

To distribute using Microsoft Intune, see [Add an Android line-of-business app to Microsoft Intune](/mem/intune/apps/lob-apps-android).  
To give an app access to the Intune app protection service, see [Give your app access to the Intune app protection service](/mem/intune/developer/app-sdk-get-started#give-your-app-access-to-the-intune-app-protection-service-optional).

### See also

- [Wrap overview](overview.md)
- [Manually Signing the APK - Xamarin](/xamarin/android/deploy-test/signing/manually-signing-the-apk)
- [Manual code sign on iOS](code-sign-ios.md)  
- [Frequently asked questions for wrap](faq.yml)  
- [Troubleshoot issues with the wrap feature in Power Apps](/troubleshoot/power-platform/power-apps/manage-apps/wrap-issues)
