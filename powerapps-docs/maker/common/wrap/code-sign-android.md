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

This article explains how to manually code sign your Android (APK) app for Power Apps wrap. Sign your app for Android if you select Android as one of the [platforms](overview.md#app-platforms) when you create and build your [wrap project](wrap-how-to.md#steps-to-create-a-custom-branded-native-app-using-the-wrap-wizard).

> [!IMPORTANT]
> To sign an AAB app for Google Play distribution, see [Sign your app](https://developer.android.com/studio/publish/app-signing).

## Before you begin

### Required software

Before you begin, install and set up:

- [Android Studio](https://developer.android.com/studio)
- [OpenSSL](https://slproweb.com/products/Win32OpenSSL.html)
- [apksigner tool](https://developer.android.com/studio/command-line/apksigner) (included with Android Studio)

### Prerequisites

You need:
- The application name to create the hash key.
- The latest APK file to sign in.

> [!NOTE]
> Use the `.jks` extension for manual signing and the `.pfx` extension for automatic signing.

## Generate key and signature hash

> [!NOTE]
> Skip to [Manual signing](#manual-signing-of-apk-package-not-for-kv-signing) if you already generated keys and the signature hash when you created the [app registration](wrap-how-to.md#4-register-your-app).

### Set up environment variables

If you don't set environment variables:

1. Download and install Android Studio and OpenSSL.
1. Add `keytool` and `openssl` to your PATH environment variable:
   - Add `C:\Program Files\Android\Android Studio\jbr\bin` to your PATH.
   - Add the path of `openssl.exe` (for example, `C:\Program Files\OpenSSL-Win64\bin`) to your PATH.


## **For manual signing process**
### Generate signature hash key and certificate

Run this command in the command prompt:

```
keytool -genkey -alias powerappswrap -keyalg RSA -keystore powerappswrap.jks -keysize 2048 -validity 10000
```

When prompted:
1. Enter a password for your keystore.
1. Enter your name, organization, location, and other required details.
1. Confirm the information.

:::image type="content" source="media/code-sign-android/codeSignIn1.png" alt-text="Screenshot of keytool command using the parameters in the preceding example." lightbox="media/code-sign-android/codeSignIn1.png":::

Run this command to generate key and certificate:

```
keytool -exportcert -alias powerappswrap -keystore powerappswrap.jks | openssl sha1 -binary | openssl base64
```

When prompted, enter the keystore password you created earlier.

:::image type="content" source="media/code-sign-android/codeSignIn3.png" alt-text="A screenshot with keytool command using the parameters in the example shown earlier." lightbox="media/code-sign-android/codeSignIn3.png":::

**Parameters explained:**

| Parameter | Description |
|-----------|-------------|
| **genkey** | Command to generate a key |
| **alias** | Alias for the keystore entry |
| **keyalg** | Key algorithm name |
| **keystore** | Name of the keystore |
| **keysize** | Size of each key |
| **validity** | Validity of the key in days |
| **exportcert** | Reads the certificate from the keystore |
| **openssl** | Generates SHA1 key for Android |

## **For automatic key vault signing process**

### Generate signature hash key and certificate

Run this command in the command prompt:

```
keytool -genkey -alias powerappswrap -keyalg RSA -keystore powerappswrap.pfx -keysize 2048 -validity 10000
```

When prompted:
1. Enter a password for your keystore.
1. Enter your name, organization, location, and other required details.
1. Confirm the information.

:::image type="content" source="media/code-sign-android/codeSignIn1.png" alt-text="A screenshot with keytool command using the parameters in the preceding example." lightbox="media/code-sign-android/codeSignIn1.png":::

Run this command to generate key and certificate:

```
keytool -exportcert -alias powerappswrap -keystore powerappswrap.pfx | openssl sha1 -binary | openssl base64
```

When prompted, enter the keystore password you created earlier.

:::image type="content" source="media/code-sign-android/codeSignIn3.png" alt-text="A screenshot with keytool command using the parameters in the example shown earlier." lightbox="media/code-sign-android/codeSignIn3.png":::

**Parameters explained:**

| Parameter | Description |
|-----------|-------------|
| **genkey** | Generates a key. |
| **alias** | Alias for the keystore entry. |
| **keyalg** | Key algorithm name. |
| **keystore** | Name of the keystore. |
| **keysize** | Size of each key. |
| **validity** | Validity of the key in days. |
| **exportcert** | Reads the certificate from the keystore |
| **openssl** | Generates SHA1 key for Android |


## Manual signing of APK package (Not for KV signing)

Follow these steps if you don't use automatic sign-in during wrap or if you try to upload an AAB file for Play Store. To avoid repeating this process, use automatic sign-in when possible.

### Locate the apksigner tool

1. Open Android Studio.
1. Go to **Tools** > **SDK Manager** > **Android SDK Location** to find your SDK path.
1. In the SDK directory, navigate to:
   - **build-tools** > **[version number]** > find **apksigner.bat** (Windows) or **apksigner** (Mac/Linux)
   - Or: **build-tools** > **[version number]** > **lib** > find **apksigner.jar**

:::image type="content" source="media/code-sign-android/codeSignIn2.png" alt-text="A screenshot with apksigner location information." lightbox="media/code-sign-android/codeSignIn2.png":::

### Sign the APK file

Run this command to sign your APK:

```
apksigner.bat sign --ks PATH_TO_KEYSTORE --ks-key-alias KEY_ALIAS PATH_TO_APK
```

**Parameters explained:**

| Parameter | Description |
|-----------|-------------|
| **ks** | Path to your keystore file (for example, `C:\Users\name\Desktop\powerappswrap.jks`) |
| **ks-key-alias** | The alias you used when generating the key (for example, `powerappswrap`) |
| **PATH_TO_APK** | Full path to your APK file (for example, `C:\Users\name\Downloads\MyApp.apk`) |

When prompted, enter the keystore password.

**Example:**
```
apksigner.bat sign --ks C:\Users\name\Desktop\powerappswrap.jks --ks-key-alias powerappswrap C:\Users\name\Desktop\MyApp.apk
```

### Verify the signature

After signing, verify the APK signature with:
```
apksigner.bat verify --verbose PATH_TO_APK
```

A successful verification confirms your APK is properly signed and ready for distribution.

For more information, see [Android Studio command line tools: apksigner](https://developer.android.com/studio/command-line/apksigner).


## Distribute the app

After signing your app, you can distribute it using several methods:

### Distribution options

- **Microsoft Intune**: To distribute using Microsoft Intune, see [Add an Android line-of-business app to Microsoft Intune](/mem/intune/apps/lob-apps-android).

- **Intune app protection**: To give your app access to the Intune app protection service, see [Give your app access to the Intune app protection service](/mem/intune/developer/app-sdk-get-started#give-your-app-access-to-the-intune-app-protection-service-optional).

- **Direct distribution**: You can also distribute the signed APK directly to users for manual installation.


## See also

- [Wrap overview](overview.md)
- [Manually Signing the APK - Xamarin](/xamarin/android/deploy-test/signing/manually-signing-the-apk)
- [Manual code sign on iOS](code-sign-ios.md)
- [Frequently asked questions for wrap](faq.yml)
- [Troubleshoot issues with the wrap feature in Power Apps](/troubleshoot/power-platform/power-apps/manage-apps/wrap-issues)
