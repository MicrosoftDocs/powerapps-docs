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

In this article, you'll learn about how to manually code sign for Android (APK). You need to sign your app for Android if you selected Android as one of the [platforms](overview.md#app-platforms) while creating and building your [wrap project](wrap-how-to.md#create-custom-branded-native-power-apps-for-ios-and-android-using-the-wrap-wizard).

> [!IMPORTANT]
> If you'd like to sign an AAB app for Google Play distribution instead, refer to [Sign your app](https://developer.android.com/studio/publish/app-signing).

## Prepare your PC

You need the following information to get started:

- Set up [Android Studio](https://developer.android.com/studio)
- Set up [OpenSSL](https://slproweb.com/products/Win32OpenSSL.html)
- Set up [apksigner tool](https://developer.android.com/studio/command-line/apksigner)

## Prerequisites

- Application name for creating the hash key.
- Latest APK file for signing in process.

## Generate keys

> [!NOTE]
> Skip to [sign the APK package](#manual-sign-the-apk-package) if you've already generated keys and signature hash while creating the [app registration](wrap-how-to.md#step-3-register-app).

We'll use **keytool.exe** (available after installing Android Studio, from the folder location "Drive:\Program Files\Android\Android Studio\jre\bin\keytool.exe") to create a certificate to sign the application package. Keytool is used to manage a keystore (database) of cryptographic keys, X.509 certificate chains, and trusted certificates.

If you don't have environment variables, open a command prompt and run the following command to generate a key:

1. Download Android Studio, openssl
2. Add keytool and openssl as environment variable. Add C:\Program Files\Android\Android Studio\jbr\bin as env variable. Add path of openssl.exe in environment variable (C:\Program Files\OpenSSL-Win64\bin)
3. Run this command---keytool -genkey -alias powerappswrap -keyalg RSA -keystore powerappswrap.jks -keysize 2048 -validity 10000
Generate Keys
4. Run this command in cmd - keytool -exportcert -alias powerappswrap -keystore powerappswrap.jks | openssl sha1 -binary | openssl base64
Generate Signature Hash

:::image type="content" source="media/code-sign-android/codeSignIn3.png" alt-text="A screenshot with keytool command using the parameters in the example shown above." lightbox="media/code-sign-android/codeSignIn3.png":::


If you have environment variables, open a command prompt and run the following command to generate a key:

`keytool -genkey -alias SIGNATURE_ALIAS -keyalg RSA -keystore PATH_TO_KEYSTORE -keysize 2048 -validity 10000`


Parameters:

- **genkey** - command to generate a key.
- **alias** - indicates the alias to be used in the future to refer to the keystore entry containing the keys that are generated.
- **keyalg** - key algorithm name.
- **keystore** - the name of the keystore you're using.
- **keysize** - the size of each key to be generated.
- **validity** - validity of the key in number of days.

Example:
- If preparing Key Vault, PATH_TO_KEYSTORE should have .pfx extension.

  `keytool -genkey -alias powerappswrap -keyalg RSA -keystore powerappswrap.pfx -keysize 2048 -validity 10000`

- If preparing for manual signing, PATH_TO_KEYSTORE should have .jks extension.

  `keytool -genkey -alias powerappswrap -keyalg RSA -keystore \Users\name\Desktop\powerappswrap.jks -keysize 2048 -validity 10000`

:::image type="content" source="media/code-sign-android/codeSignIn1.png" alt-text="A screenshot with keytool command using the parameters in the above example." lightbox="media/code-sign-android/codeSignIn1.png":::

## Generate signature hash

> [!NOTE]
> Skip to [sign the APK package](#manual-sign-the-apk-package) if you've already generated keys and signature hash while creating the [app registration](wrap-how-to.md#step-3-register-app).

After generating the key, the **exportcert** command is used in **keytool** to export the keystore certificate.

`keytool -exportcert -alias SIGNATURE_ALIAS -keystore PATH_TO_KEYSTORE | openssl sha1 -binary | openssl base64`

Parameters:

- **exportcert** - reads from the keystore the certificate associated with alias and stores it in the cert_file file. When no file is specified, the certificate is output to stdout.
- **alias** - the alias used while generating keys [earlier](#generate-keys).
- **keystore** - the name of the keystore you're using.
- **openssl** - generates SHA1 key for Android.

Add the generated signature hash in the **Redirect URI** while [registering the app](wrap-how-to.md#step-3-register-app).

### Convert SHA1 hex to Base64-encoded signature hash manually

You might see the following error if your signature hash isn't correctly encoded or unacceptable in the Azure portal:

"The signature hash must be base64-encoded SHA1."

When this error appears, try to generate the signature hash using the following steps instead:

1. Run `keytool -list -v -alias SIGNATURE_ALIAS -keystore PATH_TO_KEYSTORE` to list the certificate information in verbose mode.
1. Copy the **SHA1** value under the **Certificate fingerprints** section from the output. Ensure that you only copy the hexadecimal value.
    <br> For example: `EF:11:45:3D:F1:72:D9:8C:43:32:CD:0A:49:C2:E4:75:2D:B3:2D:9F`
1. Use any available "Hexadecimal to Base64" converter to convert the copied certificate fingerprint hexadecimal value into Base64 encoded value.
    <br> Example of the Base64 encoded value: `8CPPeLaz9etdqQyaQubcqsy2Tw=`
1. Copy the generated Base64 encoded value as the **Signature hash** in the Azure portal while [registering the app](wrap-how-to.md#step-3-register-app).

## Manual sign the APK package

> [!Note]
> These steps are required if you haven't wrapped the app using automatic sign-in or are trying to upload an AAB file for Play Store. To avoid repeating this step, we recommend using automatic sign-in.

To sign the APK package, we'll use the [apksigner tool](https://developer.android.com/studio/command-line/apksigner). This tool allows you to sign APKs and ensure that the APK package signature are verified successfully on all Android platforms supported by the APKs.

### Find your apksigner

1. Check the Android SDK path in the Android Studio.
1. Select **Tool** > **SDK Manager** > **Android SDK Location**.

    If using iOS, check the apksigner file from the **buildTools Version** directory:

    Go to **SDK** directory > **build-tools** > **buildToolsVersion** > **lib**, and check the **apksigner.jar** file 

:::image type="content" source="media/code-sign-android/codeSignIn2.png" alt-text="A screenshot with apksigner location information." lightbox="media/code-sign-android/codeSignIn2.png":::

### Use the apksigner file

Run the following command to use the **apksigner** and sign the package:

`apksigner.bat sign --ks PATH_TO_KEYSTORE --ks-key-alias KEY_ALIAS PATH_TO_APK`

Parameters:

- **ks** - path to the keystore.
- **ks-key-alias** - key alias path to APK file.

When prompted, enter the password.

More information: [Android Studio command line tools: **apksigner**](https://developer.android.com/studio/command-line/apksigner)

## Distribute the app

You can host the package on a distribution service such as Azure blob storage. To distribute using Microsoft Intune, see [Add an Android line-of-business app to Microsoft Intune](/mem/intune/apps/lob-apps-android). To learn about giving an app access to the Intune app protection service, see [Give your app access to the Intune app protection service](/mem/intune/developer/app-sdk-get-started#give-your-app-access-to-the-intune-app-protection-service-optional).


### See also

- [Wrap overview](overview.md)
- [Manually Signing the APK - Xamarin](/xamarin/android/deploy-test/signing/manually-signing-the-apk)
- [Manual code sign on iOS](code-sign-ios.md)  
- [Frequently asked questions for wrap](faq.yml)  
- [Troubleshoot issues with the wrap feature in Power Apps](/troubleshoot/power-platform/power-apps/manage-apps/wrap-issues)  

