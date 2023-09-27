---
title: Code sign for Android
description: Learn about how to code sign for Android for Power Apps wrap.
author: larryk78
ms.topic: article
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 06/06/2022
ms.subservice: canvas-maker
ms.author: mkaur
search.audienceType: 
  - maker
contributors:
  - mduelae
  - larryk78
---

# Code sign for Android 

In this article, you'll learn about how to code sign for Android (APK). You need to sign your app for Android if you selected Android as one of the [platforms](overview.md#app-platforms) while creating and building your [wrap project](wrap-how-to.md#create-native-mobile-apps-for-ios-and-android-using-the-wizard).

> [!IMPORTANT]
> If you'd like to sign an AAB app for Google Play distribution instead, refer to [Sign your app](https://developer.android.com/studio/publish/app-signing).

## Prepare your PC

You need the following information to get started:

- Install [Android Studio](https://developer.android.com/studio)
- Install [OpenSSL](https://www.openssl.org/)

## Generate keys

> [!NOTE]
> Skip to [sign the APK package](#sign-the-apk-package) if you've already generated keys and signature hash while creating the [app registration](wrap-how-to.md#step-4-register-app).

We'll use **keytool.exe** (available after installing Android Studio, from the folder location "Drive:\Program Files\Android\Android Studio\jre\bin\keytool.exe") to create a certificate to sign the application package. Keytool is used to manage a keystore (database) of cryptographic keys, X.509 certificate chains, and trusted certificates.

To generate a key, open a command prompt and run the following command:

`keytool -genkey -alias SIGNATURE_ALIAS -keyalg RSA -keystore PATH_TO_KEYSTORE -keysize 2048 -validity 10000`


Parameters:

- **genkey** - command to generate a key.
- **alias** - indicates the alias to be used in the future to refer to the keystore entry containing the keys that are generated.
- **keyalg** - key algorithm name.
- **keystore** - the name of the keystore you're using.
- **keysize** - the size of each key to be generated.
- **validity** - validity of the key in number of days.

Example:



- If preparing Keyvault, PATH_TO_KEYSTORE should have .pfx extension.

  `keytool -genkey -alias powerappswrap -keyalg RSA -keystore powerappswrap.pfx -keysize 2048 -validity 10000`

- If preparing for manual signing, PATH_TO_KEYSTORE should have .jks extension.

  `keytool -genkey -alias powerappswrap -keyalg RSA -keystore powerappswrap.jks -keysize 2048 -validity 10000`


:::image type="content" source="media/code-sign-android/keytool.png" alt-text="A screenshot with keytool command using the parameters in the above example.":::

## Generate signature hash

> [!NOTE]
> Skip to [sign the APK package](#sign-the-apk-package) if you've already generated keys and signature hash while creating the [app registration](wrap-how-to.md#step-4-register-app).

After generating the key, the **exportcert** command is used in **keytool** to export the keystore certificate.

`keytool -exportcert -alias SIGNATURE_ALIAS -keystore PATH_TO_KEYSTORE | openssl sha1 -binary | openssl base64`

Parameters:

- **exportcert** - reads from the keystore the certificate associated with alias and stores it in the cert_file file. When no file is specified, the certificate is output to stdout.
- **alias** - the alias used while generating keys [earlier](#generate-keys).
- **keystore** - the name of the keystore you're using.
- **openssl** - generates SHA1 key for Android.

Add the generated signature hash in the **Redirect URI** while [registering the app](wrap-how-to.md#step-4-register-app).

### Convert SHA1 hex to Base64-encoded signature hash manually

You might see the following error if your signature hash isn't correctly encoded or unacceptable in the Azure portal:

"The signature hash must be base64-encoded SHA1."

When this error appears, try to generate the signature hash using the following steps instead:

1. Run `keytool -list -v -alias SIGNATURE_ALIAS -keystore PATH_TO_KEYSTORE` to list the certificate information in verbose mode.
1. Copy the **SHA1** value under the **Certificate fingerprints** section from the output. Ensure that you only copy the hexadecimal value.
    <br> For example: `EF:11:45:3D:F1:72:D9:8C:43:32:CD:0A:49:C2:E4:75:2D:B3:2D:9F`
1. Use any available "Hexadecimal to Base64" converter to convert the copied certificate fingerprint hexadecimal value into Base64 encoded value.
    <br> Example of the Base64 encoded value: `8CPPeLaz9etdqQyaQubcqsy2Tw=`
1. Copy the generated Base64 encoded value as the **Signature hash** in the Azure portal while [registering the app](wrap-how-to.md#step-4-register-app).

## Sign the APK package

To sign the APK package, we'll use the [apksigner tool](https://developer.android.com/studio/command-line/apksigner). This tool allows you to sign APKs and ensure that the APK package signature are verified successfully on all Android platforms supported by the APKs.

### Find your apksigner

1. Check the Android SDK path in the Android Studio.
1. Select **Tool** > **SDK Manager** > **Android SDK Location**.

    If using iOS, check the apksigner file from the **buildTools Version** directory:

    Go to **SDK** directory > **build-tools** > **buildToolsVersion** > **lib**, and check the **apksigner.jar** file 

### Use the apksigner file

Run the following command to use the **apksigner** and sign the package:

`apksigner.bat sign --ks PATH_TO_KEYSTORE --ks-key-alias KEY_ALIAS PATH_TO_APK`

Parameters:

- **ks** - path to the keystore.
- **ks-key-alias** - key alias path to APK file.

When prompted, enter the password.

More information: [Android Studio command line tools: **apksigner**](https://developer.android.com/studio/command-line/apksigner)

## Distribute the app

You can host the package on a distribution service such as [App Center](wrap-how-to.md#create-an-app-center-location-for-your-mobile-app-manually-optional). To distribute using Microsoft Intune, see [Add an Android line-of-business app to Microsoft Intune](/mem/intune/apps/lob-apps-android). To learn about giving an app access to the Intune app protection service, see [Give your app access to the Intune app protection service](/mem/intune/developer/app-sdk-get-started#give-your-app-access-to-the-intune-app-protection-service-optional).


### See also

- [Wrap overview](overview.md)
- [Manually Signing the APK - Xamarin](/xamarin/android/deploy-test/signing/manually-signing-the-apk)
- [Code sign on iOS](code-sign-ios.md)
