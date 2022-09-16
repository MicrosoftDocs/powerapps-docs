---
title: Customize and build your mobile app
description: Learn about how to use the wrap functionality to package one or more canvas apps into a native mobile app package.
author: larryk78
ms.topic: article
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 05/31/2022
ms.subservice: canvas-maker
ms.author: mkaur
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
---

# Customize and build your mobile app

Earlier, you learned about the capabilities of wrap feature, how it works, and its benefits. In this article, you'll learn how to use the wrap feature to package one or more canvas apps as a single native mobile app package.

## Prerequisites

- You must enable your environment for the wrap capability. Refer to [Install an app in an environment](/power-platform/admin/manage-apps#install-an-app), and install the **Wrap for Power Apps** solution using Power Platform admin center.
- You'll need access to [Azure portal](https://portal.azure.com) to register your app, and configure the API permissions on the Microsoft Identity platform.
- You'll need access to [Visual Studio App Center](https://appcenter.ms/) to add new organization and apps.
- You'll need one or more canvas apps (saved in a solution) that you can package for mobile user distribution.
- To use Android platform, ensure you [generate keys](code-sign-android.md#generate-keys), and then [generate signature hash](code-sign-android.md#generate-signature-hash) before you [register the app](#app-registration). You'll need the generated signature hash to configure the **Redirect URI**.

## Add canvas app to solution

This feature requires the apps to be part of a solution. If your canvas apps aren't part of a solution already, add them to an existing or a new solution. More information: [Add an app to a solution](../../canvas-apps/add-app-solution.md#add-an-existing-canvas-app-to-a-solution)

## App registration

Create a new registration for your app in the organizational directory using the Azure portal. For detailed steps, see [Quickstart: Register an application with the Microsoft identity platform](/azure/active-directory/develop/quickstart-register-app).

When creating a new app registration, ensure to use the supported account type that includes accounts in an organizational directory.

> [!IMPORTANT]
> - Wrap only supports **Multitenant** account types currently. **Single tenant** account type is not yet supported. More information: [Account types in Microsoft identity platform](/azure/active-directory/develop/v2-supported-account-types)
> - To ensure the **Redirect URI** matches the [required format](#redirect-uri-format), don't create the **Redirect URI** while creating the app registration. Once the app registration is complete, go to app, and then choose **Authentication** > **+ Add a platform** to add the platform instead.
> - You must create a separate **Redirect URI** for each platform (iOS, Android) that you want to target.

After the app is registered, copy the **Application (client) ID** and the **Redirect URI** that you'll need later when configuring the wrap project inside Power Apps. More information: [Register an application](/azure/active-directory/develop/quickstart-register-app#register-an-application)

### Redirect URI format

For iOS, the **Redirect URI** only requires the **Bundle ID**.

Examples for iOS:
- **Bundle ID**: `com.contoso.myapp`
- **Redirect URI**: `msauth.com.contoso.myapp://auth`

For Android, the **Redirect URI** requires the **Package name**, and the **Signature hash**. To create the signature hash, [generate keys](code-sign-android.md#generate-keys), and then [generate signature hash](code-sign-android.md#generate-signature-hash).

Examples for Android:

- **Package name**: `com.contoso.myapp`
- **Redirect URI**: `msauth://com.contoso.myapp/<generated signature hash>`

### Allow registered apps in your environment

You'll need to allow the apps registered using the Azure portal in your Power Platform environment. To perform this step, use the latest version of the [Power Apps PowerShell module](/power-platform/admin/powerapps-powershell#cmdlets) for **Administrator**, and run the following cmdlet with the Application (client) ID from the [App registration](#app-registration) step:

```powershell
Add-AdminAllowedThirdPartyApps -ApplicationId <App ID>
```

> [!NOTE]
> - This cmdlet is available in 2.0.144 or later versions of the [Power Apps PowerShell module](/power-platform/admin/powerapps-powershell#cmdlets) for **Administrator**.
> - You'll need global tenant administrator privileges to run this cmdlet. The cmdlet allows an administrator to designate which registered 3rd-party applications in Azure AD can invoke Power Platform connections.

## Configure API permissions

[Add and configure](/azure/active-directory/develop/v2-permissions-and-consent#request-the-permissions-in-the-app-registration-portal) the following API permissions for the app you registered earlier using the Azure portal:

- **Microsoft APIs**
    - *Dynamics CRM*
- **APIs my organization uses**
    - *Azure API Connections*
    - *PowerApps Service*

> [!NOTE]
> If you don't find the permissions under **APIs my organization uses**, run the following PowerShell commands as appropriate, and try again:
> - Missing *Azure API Connections* permission: 
>     ```powershell
>     Connect-AzureAD -TenantId <your tenant ID>
>     New-AzureADServicePrincipal -AppId fe053c5f-3692-4f14-aef2-ee34fc081cae -DisplayName "Azure API Connections"
>     ```
> - Missing *PowerApps Service* permission:
>     ```powershell
>     Connect-AzureAD -TenantId <your tenant ID>
>     New-AzureADServicePrincipal -AppId 475226c6-020e-4fb2-8a90-7a972cbfc1d4 -DisplayName "PowerApps Service"
>     ```

For detailed steps, refer to [Request the permissions in the app registration portal](/azure/active-directory/develop/v2-permissions-and-consent#request-the-permissions-in-the-app-registration-portal).

## Create an App Center container for your mobile app

In this step, you'll use App Center to create an app container for your mobile app. More information: [App Center container](overview.md#app-center-container)

> [!TIP]
> For more information about App Center, go to [Visual Studio App Center documentation](/appcenter/).

1. Go to [App Center](https://appcenter.ms/).
1. Sign in with your work or school account.
1. If you don't have any existing organization, select **Add new** &gt; **Add new organization** to create a new organization.
1. Select the organization from the list on the left-pane.
1. Select **Apps** &gt; **Add app**.
1. Enter app name.
1. Select app release type.
1. Select **Custom** OS for iOS apps, or **Android** OS for Android apps.

    > [!NOTE]
    > You must create separate App Center containers for each platform.

1. For **Android** OS, select **Platform** as **React Native**.

    > [!NOTE]
    > **Platform** must be **React Native** for all apps in App Center.

    :::image type="content" source="media/wrap-canvas-app/app-center-app.png" alt-text="App center app configuration.":::

1. Select **Add new app**.

1. Copy the app's App Center URL that you'll need later when configuring the wrap project inside Power Apps.

    For example, `https://appcenter.ms/orgs/Contoso-sales/apps/Sample-canvas-app-for-Android-OS/`

    :::image type="content" source="media/wrap-canvas-app/app-center-url.png" alt-text="App center URL.":::

    More information: [App Center URL](overview.md#app-center-url)

1. Create a new API token for the app access, and copy it for configuring the canvas app project later. More information: [App Center API token](overview.md#app-center-api-token)

    1. Select **Settings** from the left.
    1. Select **App API tokens**.
    1. Select **New API token**.
    1. Enter a description.
    1. Select **Full Access**.
    1. Select **Add new API token**.
        > [!NOTE]
        > Ensure you copy the token before closing the dialog box.
    1. Copy the token, and save it for canvas app wrap configuration [later](#app-center-api-token).
          :::image type="content" source="media/wrap-canvas-app/app-center-token.png" alt-text="App center token.":::

Repeat the above steps to create apps for any additional OS type.

## Create a **wrap** project

Use your [primary canvas app](overview.md#primary-app) to create a wrap project using the app information from both Microsoft identity platform and App Center that you configured in the previous steps. More information: [Build a wrap project](overview.md#build-the-wrap-project)

To create a wrap project, go to [Power Apps](https://make.powerapps.com) > **Apps** > select the primary canvas app > select **Wrap**, and enter the wrap project details described in this section. After entering all details, select **Save** > **Build** to build the project.

Depending on the platform chosen, the build process queues the requests to create your packages for Android, iOS, or Google platforms.

> [!NOTE]
> Depending on the workload, the build process might take a few hours to complete.

After a successful build, you'll see your mobile app in the App Center.

### Display name

A display name of the mobile app as it will appear on the mobile device home screen.

### Secondary apps

Optional. Additional app(s) to bundle within the same mobile app package. More information: [Secondary app](overview.md#secondary-app), [Primary app](overview.md#primary-app)

### App platform(s)

Determines the output type of the wrap build process based on the platform you select. More information: [App platform(s)](overview.md#app-platforms)

### Sign my app (preview)
  
**Optional** Azure Keyvault URI allows for automated app signing for distribution by configuring a keyvault containing the required certificates. More information: [Set up KeyVault for automated signing](how-to.md#set-up-keyvault-for-automated-signing)
 > [!IMPORTANT]
 > - This is a preview feature.
 > - Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.


### Bundle ID

Bundle ID that uniquely identifies the mobile app. For example, `com.contoso.myapp`. More information: [Bundle ID](overview.md#bundle-id)

### Application (client) ID

Client ID of the app registered [earlier](#app-registration) with the Microsoft identity platform. More information: [Application (client) ID](overview.md#application-client-id)

### Redirect URI

URL created [earlier](#app-registration) to redirect after the successful sign-in of the app registered with Microsoft identity platform. More information: [Redirect URI](overview.md#redirect-uri)

### App Center URL

For iOS, Android, or Google Play Store App Center URL copied [earlier](#create-an-app-center-container-for-your-mobile-app). More information: [App Center URL](overview.md#app-center-url)

### App Center API token

Created [earlier](#create-an-app-center-container-for-your-mobile-app). More information: [App Center API token](overview.md#app-center-api-token)

### Appearance

Configure app icons, screen images, color, and theme:

:::image type="content" source="media/wrap-canvas-app/appearance.png" alt-text="Appearance of the app with the highlighted and numbering - 1 - app icons, 2 - splash screen image, 3 - welcome screen image, 4 - background fill color, 5 - button fill color, 6 - status bar text theme, 7 - settings option.":::

#### iOS app icons/ Android app icons

Icon images for the app specific to iOS, Android, or Google Play Store platform. The icon image file size must match required pixel count. [1]

#### Screen images

- **Splash screen image**

    Image that will be used on the splash screen of your mobile app, while it loads. Default image used when not provided. [2]

- **Welcome screen image**

    Image that will be used on the welcome (sign in) screen of your mobile app, while it loads. Default image used when not provided. [3]

#### Color

- **Background fill color**

    Hexadecimal color code used for the background of the welcome screen. [4]

- **Button fill color**

    Hexadecimal color code used to fill the button color. [5]

#### **Status bar text theme**

Color for the status bar text at the top of the app. [6]

#### Settings

Takes you to the app settings. Also available using the shake gesture. Can't be customized. [7]

- **App name** - name of the app, followed by the app bundle ID.
- **App version** - version number for the app; generated automatically.
- **Platform version** - version of the Power Apps Mobile platform.
- **Session ID** - ID of the currently open session.
- **Clear cache** - resets the wrapped app to default settings.
- **App settings** - shows a list of apps that are part of the current package. Selecting an app from this list shows the app details, including the connector information that the app might be configured to use.

  
## Set up KeyVault for automated signing
  
**Prerequisites**
  
- You'll need to have a [Apple account](https://developer.apple.com) enrolled in Apple developer Program or Apple enterprise developer program.
- Create a [distribution certificate](code-sign-ios.md#create-the-distribution-certificate) or [ad-hoc Provisioning Profile](code-sign-ios.md#create-an-ios-provisioning-profile) or enterprise provisioning profile.
- Azure Active Directory subscription to [create Key Vault](/azure/key-vault/general/quick-create-portal).
- Admin access for your tenant.
   
Follow these steps to configure KeyVault URI:
  
1. Sign in to your tenent as an admin and [create an Azure service principal](/powershell/azure/create-azure-service-principal-azureps?#create-a-service-principal) for 1P AAD application: 4e1f8dc5-5a42-45ce-a096-700fa485ba20 (WrapKeyVaultAccessApp) 
  
2. Add a role to the service principal listed above in the subscription where the KeyVault is going to exist. For more information, see [Steps to assign an Azure role](/azure/key-vault/general/quick-create-portal).

3. Create or access existing key vault: [Create a key vault using the Azure portal](/azure/key-vault/general/quick-create-portal)
4. Add access policies for the key vault.
  
   :::image type="content" source="media/wrap-canvas-app/wrap-keyvault.gif" alt-text="Add access policies for the key vault.":::
  
5. Depending on your device, do one of following:
   - For Android, create the .pfx file upload it to the keyvault certificate section. More information: [Generate keys](code-sign-android.md#generate-keys) 
  
     :::image type="content" source="media/wrap-canvas-app/wrap-1.png" alt-text="Create a cert for Android.":::
     > [!NOTE]
      > The name of the certificate must be present in the tag step. The password also needs match the password you entered during the store pass parameter used to create the .pfx file in step 2.
  
   - For iOS: 
     1. Install the .cer into Keychain Access app by double clicking it. More information: [Create the distribution certificate](code-sign-ios.md#create-the-distribution-certificate) </br> Then export the file as a .p12 file by right clicking your certificate file and the select **Export** and select the file format .p12. 
        > [!NOTE]
        > The .p12 password that you set in step 4 is required when uploading it to the keyvault in the next step.
     2. [Create the provisioning profile](code-sign-ios.md#create-an-ios-provisioning-profile) and run the following command to encode it to base64:
        - Mac: base64 `-i example.mobileprovision`
        - Windows:  `certutil -encode data.txt tmp.b64`
     
     3. Get the outputted `base64` string from previous step and upload to Keyvault secret. Then, get the .p12 file and upload it to Keyvault Certificate.
  
        :::image type="content" source="media/wrap-canvas-app/wrap-2.png" alt-text="Create a cert for iOS.":::

6. Once iOS or Android certificates are created and uploaded, add three tags with the name as the bundle id, and the value corresponding to the name of the uploaded certificate(s).
  
     :::image type="content" source="media/wrap-canvas-app/wrap-3.png" alt-text="Add tags.":::
  
## Code signing

[Code signing](overview.md#code-signing) process is different for Android and iOS devices.

- [Code signing for iOS](code-sign-ios.md)
- [Code signing for Android](code-sign-android.md)
- [Code signing for Google Play Store](https://developer.android.com/studio/publish/app-signing)


## Test and distribute mobile app package

For testing and distribution, see [App Center Test](/appcenter/test-cloud/) and [Distribute](/appcenter/distribution/).

### See also

- [Wrap overview](overview.md)
- [Code sign for iOS](code-sign-ios.md)
- [Code sign for Android](code-sign-android.md)
