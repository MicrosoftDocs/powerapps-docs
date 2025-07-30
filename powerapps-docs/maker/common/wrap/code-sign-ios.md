---
title: Manual code sign for iOS
description: Learn how to manually code sign for iOS for Power Apps wrap.
author: komala2019
ms.topic: how-to
ms.custom: canvas
ms.reviewer: smurkute
ms.date: 03/22/2024
ms.subservice: canvas-maker
ms.author: koagarwa
search.audienceType: 
  - maker
contributors:
  - mduelae
---

# Manual code sign for iOS

This article explains how to code sign for iOS. You need to sign your app for iOS if you selected iOS as one of the [platforms](overview.md#app-platforms) while creating and building your [wrap project](wrap-how-to.md#steps-to-create-a-custom-branded-native-app-using-the-wrap-wizard).

> [!IMPORTANT]
> Using Xcode to digitally sign your wrapped mobile apps for iOS is not supported. Follow the instructions below to sign your wrapped mobile app packages for iOS correctly.


## Before you begin

### Prerequisites

Before you start, make sure you have:

- App ID
- Device UDIDs (only for testing and development purposes)
- A macOS device to code sign for iOS

### Set up your Mac

1. Install **Xcode**. More information: [Xcode](https://developer.apple.com/support/xcode/)
2. Install PowerShell for macOS. More information: [Installing PowerShell on macOS](/powershell/scripting/install/installing-powershell-on-macos)
3. Enroll in the [Apple Developer Program](https://developer.apple.com/programs/)
4. For organization distribution, sign up for the [Apple Enterprise Developer Program](https://developer.apple.com/programs/enterprise/)


## Create App ID

1. Sign in to your developer account at <https://developer.apple.com> and select the **Account** tab.

    :::image type="content" source="media/code-sign-ios/account-tab.png" alt-text="Account tab.":::

2. Go to [**Certificates, IDs & Profiles > Identifiers**](https://developer.apple.com/account/resources/identifiers/list).

3. Select **+** to create a new identifier.

    :::image type="content" source="media/code-sign-ios/identifier.png" alt-text="Create new identifier.":::

4. Select **App IDs**, then select **Continue**.

    :::image type="content" source="media/code-sign-ios/register-identifier.png" alt-text="Register a new identifier.":::

5. Select the type as **App**, then select **Continue**.

6. Register an **App ID**:

    :::image type="content" source="media/code-sign-ios/register-appid.png" alt-text="Register an App ID.":::

    - **Description** - Name of your app.
    - **Bundle ID** - Select **Explicit Bundle ID**.
    - Enter the bundle ID that you used while [creating the wrap project](wrap-how-to.md#3-choose-target-platform). More information: [Bundle ID](overview.md#bundle-id)
    - Enable these capabilities:
        - Associated Domains
        - iCloud
        - NFC Tag Reading
        - Push Notifications
    - Select **Continue**.

7. Review and register the App ID.

## Create distribution certificate

### Create Certificate Signing Request (CSR)

1. On your Mac, go to the **Applications** folder > **Utilities** > open **Keychain Access**.

2. Select **Keychain Access** > **Certificate Assistant** > **Request a Certificate from a Certificate Authority**.

    :::image type="content" source="media/code-sign-ios/cert-req.png" alt-text="Request a certificate from a CA.":::

3. Fill out the **Certificate Information**:
    - In the **User Email Address** field, enter your Apple ID email address.
    - In the **Common Name** field, enter your name.
    - In the **Request** group, select **Saved to disk**.
    - Save the file to your Mac.
    - Select **Continue**.

### Upload and install certificate

1. Sign in to your developer account at <https://developer.apple.com> by selecting the **Account** tab.

2. Go to [**Certificates, IDs & Profiles > Certificates**](https://developer.apple.com/account/resources/certificates/list).

3. Select **+** to create a new certificate.

4. Select **App Store and Ad Hoc** > **Continue**.

    ![Certificates, Identifiers & Profiles](media/code-sign-ios/new-cert.png)

    > [!NOTE]
    > If you have an Enterprise Developer Account, you'll have the option to create an Enterprise Distribution certificate.

5. Upload the Certificate Signing Request (CSR) file that you generated in the previous steps.

    :::image type="content" source="media/code-sign-ios/upload-cert.png" alt-text="Upload the certificate.":::

6. Select **Continue**, and download the certificate to your Mac.

7. Double-click the downloaded .cer file to install it in Keychain Access.

8. Make note of the **Name** of the certificate (usually formatted as **iPhone Distribution: Name (Team ID)**). This value is the code signing identity needed for signing.


## Register devices for testing

> [!NOTE]
> This step is only necessary if you're distributing the app to external users. It's not required if the app is only for internal users.

1. Sign in to your developer account at <https://developer.apple.com> by selecting the **Account** tab.

2. Go to [**Certificates, IDs & Profiles > Devices**](https://developer.apple.com/account/resources/devices/list).

3. Select **+** to register one or more devices.

4. Enter the **Device Name** and **Device ID (UDID)**.

    :::image type="content" source="media/code-sign-ios/register-device.png" alt-text="Register a device.":::

5. Select **Save**.

    > [!TIP]
    > You can register multiple devices at once by uploading a list of UDIDs.


## Create iOS Provisioning Profile

1. Sign in to your developer account at <https://developer.apple.com> and select the **Account** tab.

2. Go to [**Certificates, IDs & Profiles > Profiles**](https://developer.apple.com/account/resources/profiles/list).

3. Select **+** to create a new profile.

4. Select **Ad Hoc** > **Continue**.

    :::image type="content" source="media/code-sign-ios/ad-hoc.png" alt-text="Ad Hoc.":::

    > [!NOTE]
    > For production use, select the **App Store** distribution method.

5. Select the App ID you created earlier, then select **Continue**.

    :::image type="content" source="media/code-sign-ios/app-id.png" alt-text="App ID.":::

6. Select the certificate you created earlier, then select **Continue**.

    :::image type="content" source="media/code-sign-ios/select-cert.png" alt-text="Select certificate.":::

7. Select all the test devices where you want to install your app, then select **Continue**.

    :::image type="content" source="media/code-sign-ios/add-devices.png" alt-text="Add devices.":::

8. Name your provisioning profile and note down the name.

9. Select **Generate** and download the profile to your Mac.

10. Double-click the downloaded file (*.mobileprovision) to register it with Xcode.

## Sign the iOS Archive

1. Download and unzip the **iOS-Archive.zip** file from your Azure blob storage. This creates a folder named after the [Bundle ID](wrap-how-to.md#3-choose-target-platform). In the example below, the Bundle ID is **com.single.wrap**.

2. For enterprise signing only: Open the file **Distribution-exportOptions.plist** with Xcode and change the value for the **method** field to **enterprise**.

    > [!NOTE]
    > Enterprise signing is not supported with Key Vault signing.

3. Open Terminal and change directory to the unzipped folder.

4. Enter `pwsh` to start PowerShell in the terminal.

5. Run the PowerShell script with your certificate and provisioning profile information:
   ```
   ./SignAndGenerateIPA.ps1 -CodeSigningIdentity "YOUR_CODE_SIGNING_IDENTITY" -ProvisioningProfilePath "PATH_TO_PROVISIONING_PROFILE"
   ```

    > [!NOTE]
    > To find your **CodeSigningIdentity** value, right-click on the **.mobileprovision** file, select **More Info** > **Preview**. Look for the **Name** field under **Certificates**.

    > [!TIP]
    > The **ProvisioningProfilePath** is the path to the .mobileprovision file you downloaded. For example: `/Users/username/Downloads/MyProvisioningProfile.mobileprovision`

    :::image type="content" source="media/code-sign-ios/powershell.png" alt-text="Run PowerShell script.":::

6. When the script completes, a **.ipa** file is created (for example, **com.single.wrap.ipa**).

    > [!IMPORTANT]
    > If the script fails, delete the unzipped folder and files as they might be corrupted. Unzip **iOS-Archive.zip** again before retrying.

    :::image type="content" source="media/code-sign-ios/folder-structure.png" alt-text="IPA package.":::



## Distribute the app

Install the **.ipa** file on registered devices using the **Finder** app. 

For enterprise distribution with Microsoft Intune:
- [Add an iOS/iPadOS line-of-business app to Microsoft Intune](/mem/intune/apps/lob-apps-ios) 
- [Give your app access to the Intune app protection service](/mem/intune/developer/app-sdk-get-started#give-your-app-access-to-the-intune-app-protection-service-optional)



## See also

- [Wrap overview](overview.md)
- [Manual code sign on Android](code-sign-android.md)  
- [Frequently asked questions for wrap](faq.yml)  
- [Troubleshoot issues with the wrap feature in Power Apps](/troubleshoot/power-platform/power-apps/manage-apps/wrap-issues)
