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

This article explains how to manually code sign your Android (APK) app for Power Apps wrap. You must sign your app for Android if you selected Android as one of the [platforms](overview.md#app-platforms) when creating and building your [wrap project](wrap-how-to.md#create-custom-branded-native-power-apps-for-ios-and-android-using-the-wrap-wizard).

> [!IMPORTANT]
> If you want to sign an AAB app for Google Play distribution, see [Sign your app](https://developer.android.com/studio/publish/app-signing).

---

## Before you begin

### Required software

Before you begin, install and set up the following:

- [Android Studio](https://developer.android.com/studio)
- [OpenSSL](https://slproweb.com/products/Win32OpenSSL.html)
- [apksigner tool](https://developer.android.com/studio/command-line/apksigner) (included with Android Studio)

### Prerequisites

You need:
- Application name for creating the hash key
- Latest APK file for signing

> [!NOTE]
> Use `.jks` extension for manual signing and `.pfx` extension for automatic signing.

---

## Generate key and signature hash

> [!NOTE]
> Skip to [Manual signing](#manual-signing-of-apk-package) if you have already generated keys and the signature hash while creating the [app registration](wrap-how-to.md#step-3-register-app).

### Set up environment variables

If you don't have environment variables set:

1. Download and install Android Studio and OpenSSL.
2. Add keytool and openssl to your PATH environment variable:  
   - Add `C:\Program Files\Android\Android Studio\jbr\bin` to your PATH.  
   - Add the path of openssl.exe (for example, `C:\Program Files\OpenSSL-Win64\bin`) to your PATH.

### Generate keystore and key

Run this command to generate a key:

```
keytool -genkey -alias powerappswrap -keyalg RSA -keystore powerappswrap.jks -keysize 2048 -validity 10000
```

When prompted:
1. Enter a password for your keystore.
2. Provide your name, organization, location, and other required details.
3. Confirm the information when asked.

:::image type="content" source="media/code-sign-android/codeSignIn1.png" alt-text="A screenshot with keytool command using the parameters in the above example." lightbox="media/code-sign-android/codeSignIn1.png":::

### Generate signature hash

Run this command to generate the signature hash:

```
keytool -exportcert -alias powerappswrap -keystore powerappswrap.jks | openssl sha1 -binary | openssl base64
```

When prompted, enter the keystore password you created earlier.

:::image type="content" source="media/code-sign-android/codeSignIn3.png" alt-text="A screenshot with keytool command using the parameters in the example shown above." lightbox="media/code-sign-android/codeSignIn3.png":::

### Alternative command format

If you have environment variables set, you can use the generic format:

```
keytool -genkey -alias SIGNATURE_ALIAS -keyalg RSA -keystore PATH_TO_KEYSTORE -keysize 2048 -validity 10000
```

**Parameters explained:**

- **genkey**: Command to generate a key
- **alias**: Alias for the keystore entry
- **keyalg**: Key algorithm name
- **keystore**: Name of the keystore
- **keysize**: Size of each key
- **validity**: Validity of the key in days

**Examples:**
- For Key Vault (automatic signing), use a `.pfx` extension:  
  ```
  keytool -genkey -alias powerappswrap -keyalg RSA -keystore powerappswrap.pfx -keysize 2048 -validity 10000
  ```
- For manual signing, use a `.jks` extension:  
  ```
  keytool -genkey -alias powerappswrap -keyalg RSA -keystore \Users\name\Desktop\powerappswrap.jks -keysize 2048 -validity 10000
  ```

---

## Export certificate and generate signature hash

After generating the key, export the keystore certificate using the **exportcert** command:

```
keytool -exportcert -alias SIGNATURE_ALIAS -keystore PATH_TO_KEYSTORE | openssl sha1 -binary | openssl base64
```

When prompted, enter the keystore password.

**Parameters explained:**

- **exportcert**: Reads the certificate from the keystore
- **alias**: Alias used when generating keys
- **keystore**: Name of the keystore
- **openssl**: Generates SHA1 key for Android

Add the generated signature hash in the **Redirect URI** when [registering the app](wrap-how-to.md#step-3-register-app).

### Convert SHA1 hex to Base64-encoded signature hash

If you see the error "The signature hash must be base64-encoded SHA1" in the Azure portal:

1. Run:  
   ```
   keytool -list -v -alias SIGNATURE_ALIAS -keystore PATH_TO_KEYSTORE
   ```
2. When prompted, enter the keystore password.
3. Copy the **SHA1** value from the **Certificate fingerprints** section.  
   - Example: `EF:11:45:3D:F1:72:D9:8C:43:32:CD:0A:49:C2:E4:75:2D:B3:2D:9F`
4. Use a "Hexadecimal to Base64" converter to convert the SHA1 value to Base64.  
   - Example: `8CPPeLaz9etdqQyaQubcqsy2Tw=`
5. Use the Base64 value as the **Signature hash** in the Azure portal when [registering the app](wrap-how-to.md#step-3-register-app).

---

## Manual signing of APK package

> [!NOTE]
> These steps are required if you haven't used automatic sign-in during wrap or are trying to upload an AAB file for Play Store. To avoid repeating this process, we recommend using automatic sign-in when possible.

### Locate the apksigner tool

1. Open Android Studio.
2. Go to **Tools** > **SDK Manager** > **Android SDK Location** to find your SDK path.
3. In the SDK directory, navigate to:
   - **build-tools** > **[version number]** > find **apksigner.bat** (Windows) or **apksigner** (Mac/Linux)
   - Or: **build-tools** > **[version number]** > **lib** > find **apksigner.jar**

:::image type="content" source="media/code-sign-android/codeSignIn2.png" alt-text="A screenshot with apksigner location information." lightbox="media/code-sign-android/codeSignIn2.png":::

### Sign the APK file

Run this command to sign your APK:

```
apksigner.bat sign --ks PATH_TO_KEYSTORE --ks-key-alias KEY_ALIAS PATH_TO_APK
```

**Parameters explained:**

- **ks**: Path to your keystore file (for example, `C:\Users\name\Desktop\powerappswrap.jks`)
- **ks-key-alias**: The alias you used when generating the key (for example, `powerappswrap`)
- **PATH_TO_APK**: Full path to your APK file (for example, `C:\Users\name\Downloads\MyApp.apk`)

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

For more information, see [Android Studio command line tools: apksigner](https://developer.android.com/studio/command-line/apksigner).

---

## Distribute the app

### Distribution options

To distribute using Microsoft Intune, see [Add an Android line-of-business app to Microsoft Intune](/mem/intune/apps/lob-apps-android).

To give an app access to the Intune app protection service, see [Give your app access to the Intune app protection service](/mem/intune/developer/app-sdk-get-started#give-your-app-access-to-the-intune-app-protection-service-optional).

---

## See also

- [Wrap overview](overview.md)
- [Manually Signing the APK - Xamarin](/xamarin/android/deploy-test/signing/manually-signing-the-apk)
- [Manual code sign on iOS](code-sign-ios.md)
- [Frequently asked questions for wrap](faq.yml)
- [Troubleshoot issues with the wrap feature in Power Apps](/troubleshoot/power-platform/power-apps/manage-apps/wrap-issues)
