---
title: Code sign for Android (preview)
description: Learn about how to code sign for Android for Power Apps wrap.
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

# Code sign for Android (preview)

[This article is pre-release documentation and is subject to change.]

In this article, you'll learn about how to code sign for Android. You'll need to sign your app for Android if you selected Android as one of the [platforms](overview.md#app-platforms) while creating and building your [wrap project](how-to.md#create-a-wrap-project).

> [!TIP]
> For general guidance about signing an app for Android platforms, see [Sign your app](https://developer.android.com/studio/publish/app-signing).

## Prepare your PC

You'll need the following information to get started:

- Install [Java™ Platform, Standard Edition Development Kit (JDK™)](https://www.oracle.com/java/technologies/downloads/)
- Install [Android Studio](https://developer.android.com/studio)
- Install [OpenSSL](https://www.openssl.org/)

## Generate keys

We'll use [keytool](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/keytool.html) from Java SDK to create a certificate to sign the application package. Keytool is used to manage a keystore (database) of cryptographic keys, X.509 certificate chains, and trusted certificates.

To generate a key, open a command prompt and run the following command:

`keytool -genkey -alias SIGNATURE_ALIAS -keyalg RSA -keystore PATH_TO_KEYSTORE -keysize 2048 -validity 100`

Parameters:

- **genkey** - command to generate a key.
- **alias** - indicates the alias to be used in the future to refer to the keystore entry containing the keys that will be generated.
- **keyalg** - key algorithm name.
- **keystore** - the name of the keystore you're using.
- **keysize** - the size of each key to be generated.
- **validity** - validity of the key in number of days.

More information: [Generate Keys](https://docs.oracle.com/javase/tutorial/security/toolsign/step3.html)

Example:

`keytool -genkey -alias powerappswrap -keyalg RSA -keystore powerappswrap.jks -keysize 2048 -validity 10000`

:::image type="content" source="media/code-sign-android/keytool.png" alt-text="A screenshot with keytool command using the parameters in the above example.":::

## Generate signature hash

After generating the key, we'll use the **exportcert** command in **keytool** to export the keystore certificate.

`keytool -exportcert -alias SIGNATURE_ALIAS -keystore PATH_TO_KEYSTORE | openssl sha1 -binary | openssl base64`

Parameters:

- **exportcert** - reads from the keystore the certificate associated with alias and stores it in the cert_file file. When no file is specified, the certificate is output to stdout.
- **alias** - the alias used while generating keys [earlier](#generate-keys).
- **keystore** - the name of the keystore you're using.
- **openssl** - generates SHA1 key for Android.

## Sign the APK package

The next step is to sign the APK package using **apksigner** tool. The [apksigner tool](https://developer.android.com/studio/command-line/apksigner) allows you to sign APKs and ensure that the APK package signature will be verified successfully on all Android platforms supported by the APKs.

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

You can now host the package on a distribution service such as [App Center](how-to.md#test-and-distribute-mobile-app-package). To distribute using Microsoft Intune, see [Add an Android line-of-business app to Microsoft Intune](/mem/intune/apps/lob-apps-android).

### See also

- [Wrap overview (preview)](overview.md)
- [Manually Signing the APK - Xamarin](/xamarin/android/deploy-test/signing/manually-signing-the-apk)
- [Code sign on iOS (preview)](code-sign-ios.md)
