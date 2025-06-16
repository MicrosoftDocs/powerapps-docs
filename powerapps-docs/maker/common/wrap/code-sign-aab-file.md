---
title: Code signing process for AAB files
description: Learn how to manually code sign in Android App Bundle (AAB) files and convert them to APKs for debugging, including required tools and step-by-step commands.
author: komala2019
contributors:
ms.topic: how-to
ms.date: 06/05/2025
ms.author: koagarwa
ms.reviewer: smurkute
ms.subservice: canvas-maker
ms.custom: canvas
search.audienceType: 
  - maker
---
# Code signing process for AAB file

This article explains how to manually code sign an AAB file.

## Prerequisite

1. Set up [Android Studio](https://developer.android.com/studio).

1. Install bundletool for converting AAB file to APK file. You can download the latest version from the [official site](https://github.com/google/bundletool/releases).

1. Install jarsigner for signing in the AAB file. You can install jarsigner by downloading and setting up the [Java Development Kit (JDK)](https://www.oracle.com/java/technologies/javase-downloads.html).

## Signing process for AAB file 

> [!NOTE]
> You need to sign the AAB file even if you select the automatic signing process in the wrap wizard.

To sign an AAB file, follow these steps:

1. Open a terminal or command prompt.
1. Go to the directory where `jarsigner` is installed.
1. Run the commands shown in the image.
    :::image type="content" source="media/code-sign-aab-file/jarsigner-code.png" alt-text="Screenshot of command prompt showing jarsigner usage for AAB file.":::
        Replace the placeholders:
        - `<path-to-your-keystore>.jks` – Path to your .jks keystore file
        - `<output-signed-aab-file>.aab` – Output file name.
        - `<input-unsigned-aab-file>.aab` – Unsigned .aab file.
        - `<bundleid>` – Bundle ID used while wrapping.

## Convert AAB to APK file for manual debugging

To convert an AAB file to an APK file, follow these steps:

1. Open a terminal or command prompt.
2. Run the commands shown in the screenshot.
    :::image type="content" source="media/code-sign-aab-file/java-code.png" alt-text="Screenshot of command prompt showing java code for AAB file.":::
        Replace the placeholders:
        - `<path-to-signed-aab-file>.aab` – Path to the signed AAB file.
        - `<output-directory>` – Output directory for the .apks file.

- Sign the APK if you use the manual signing process. For more information, see [Code sign for Android - Power Apps](/power-apps/maker/common/wrap/code-sign-android#manual-sign-the-apk-package).


## See also

- [Manual code sign for iOS](code-sign-ios.md)
- [Manual code sign for Android](code-sign-android.md)