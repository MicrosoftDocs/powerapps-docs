---
title: Customize and build your mobile app (preview)
description: Learn about how to use the wrap functionality to package one or more canvas apps into a native mobile app package.
author: larryk78
ms.topic: article
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 04/25/2022
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

# Customize and build your mobile app (preview)

[This article is pre-release documentation and is subject to change.]

Earlier, you learned about the capabilities of wrap feature, how it works, and its benefits. In this article, you'll learn how to use the wrap feature to package one or more canvas apps as a single native mobile app package.

## Prerequisites

- You must enable your environment for the wrap capability. Refer to [Install an app in an environment](/power-platform/admin/manage-apps#install-an-app), and install the **Wrap (preview) for Power Apps** solution using Power Platform admin center.
- You'll need access to [Azure portal](https://portal.azure.com) to register your app, and configure the API permissions on the Microsoft Identity platform.
- You'll need access to [Visual Studio App Center](https://appcenter.ms/) to add new organization and apps.
- You'll need one or more canvas apps (saved in a solution) that you can package for mobile user distribution.
- To use Android platform, ensure you [generate keys](code-sign-android.md#generate-keys), and then [generate signature hash](code-sign-android.md#generate-signature-hash) before you [register the app](#app-registration). You'll need the generated signature hash to configure the **Redirect URI**.

## Add canvas app to solution

This feature requires the apps to be part of a solution. If your canvas apps aren't part of a solution already, add them to an existing or a new solution. More information: [Add an app to a solution](../../canvas-apps/add-app-solution.md#link-an-existing-canvas-app-to-a-solution)

## App registration

Create a new registration for your app in the organizational directory using the Azure portal. For detailed steps, see [Quickstart: Register an application with the Microsoft identity platform](/azure/active-directory/develop/quickstart-register-app).

When creating a new app registration, ensure to use the supported account type that includes accounts in an organizational directory.

> [!IMPORTANT]
> - Wrap (preview) only supports **Multitenant** account types currently. **Single tenant** account type is not yet supported. More information: [Account types in Microsoft identity platform](/azure/active-directory/develop/v2-supported-account-types)
> - To ensure the **Redirect URI** matches the [required format](#app-registration), don't create the **Redirect URI** while creating the app registration. Once the app registration is complete, go to app, and then choose **Authentication** > **+ Add a platform** to add the platform instead.

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

- **Microsoft APIs**&mdash;*Dynamics CRM*
- **APIs my organization uses**&mdash;*Azure API Connections* and *PowerApps Service*

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
    1. Select **New API token**.
        > [!NOTE]
        > Ensure you copy the token before closing the dialog box.
    1. Copy the token, and save it for canvas app wrap configuration [later](#app-center-api-token).
          :::image type="content" source="media/wrap-canvas-app/app-center-token.png" alt-text="App center token.":::

Repeat the above steps to create apps for any additional OS type.

## Create a **wrap** project

Use your [primary canvas app](overview.md#primary-app) to create a wrap project using the app information from both Microsoft identity platform and App Center that you configured in the previous steps. More information: [Build a wrap project](overview.md#build-the-wrap-project)

To create a wrap project, go to the preview version of [Power Apps](https://make.preview.powerapps.com) > **Apps** > select the primary canvas app > select **Wrap**, and enter the wrap project details described in this section. After entering all details, select **Save** > **Build** to build the project.

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

## Code signing

[Code signing](overview.md#code-signing) process is different for Android and iOS devices.

- [Code signing for iOS](code-sign-ios.md)
- [Code signing for Android](code-sign-android.md)

For more information, see [Code signing for Android](https://developer.android.com/studio/publish/app-signing) and [Code signing for iOS](https://developer.apple.com/support/code-signing/).

## Test and distribute mobile app package

> [!NOTE]
> Since wrap is a preview feature, the mobile app packages generated by wrap aren't meant for production use.

For testing and distribution, see [App Center Test](/appcenter/test-cloud/) and [Distribute](/appcenter/distribution/).

### See also

- [Wrap overview (preview)](overview.md)
- [Code sign for iOS (preview)](code-sign-ios.md)
- [Code sign for Android (preview)](code-sign-android.md)

