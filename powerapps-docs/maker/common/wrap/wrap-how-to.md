---
title: Customize and build your mobile app using the wrap wizard (preview)
description: Learn about how to use the wrap wizard to package canvas apps into a native mobile app package.
author: makolomi
ms.topic: article
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 2/9/2023
ms.subservice: canvas-maker
ms.author: makolomi
search.audienceType: 
  - maker
contributors:
  - mkaur
  - makolomi
---

# Use the wrap wizard to build your mobile app (preview)

[This article is pre-release documentation and is subject to change.]

Use the wrap feature to package one or more canvas app(s) as a single native mobile app package using the step-by-step wizard.

The wrap feature in Power Apps lets you create native mobile versions of your [canvas apps](../../canvas-apps/getting-started.md) as custom-branded Android and iOS mobile apps. You can distribute such *wrapped* native mobile apps to the end users through Microsoft Intune, App Center or other native distribution methods.

Wrap feature allows you to create mobile apps for iOS, Android or Google Play Store:

- iOS (IPA package)
- Android (APK package)
- Google Play Store (AAB package)

The wrap feature will wrap your canvas apps in a native mobile app shell that you can digitally sign and distribute. More information:

- [Code sign for iOS](code-sign-ios.md)
- [Code sign for Android](code-sign-android.md)

You can use Microsoft Intune, App Center or Apple Business Manager, Google Play Store to distribute your native mobile apps created with wrap.

When you update your app and republish it, the app is automatically updated.

> [!IMPORTANT]
> - This is a preview feature.
> - Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so  that customers can get early access and provide feedback.


## Prerequisites

You'll need access to:
- [Azure portal](https://portal.azure.com/) to register your app and configure the API permissions on the Microsoft Identity platform.
- [App Center](https://appcenter.ms/) to add new organization and apps.
- This feature requires the apps to be part of a  [managed or unmanaged solution](/power-platform/alm/solution-concepts-alm#managed-and-unmanaged-solutions). If your apps aren't part of a solution already, add them to an existing or a new solution. More information: [Create a canvas app from within a solution](../../canvas-apps/add-app-solution.md#add-an-existing-canvas-app-to-a-solution). 

To use Android platform, ensure you [<u>generate keys</u>](code-sign-android.md#generate-keys), and then [generate signature hash](code-sign-android.md#generate-signature-hash) before you [<u>register the app</u>](how-to.md#app-registration). You'll need the generated signature hash to configure the **Redirect URI**.

## Create native mobile apps for iOS and Android using the wizard

1. Sign in to [Power Apps](https://make.powerapp.com/).

2. Select **Apps**, from the left navigation pane. 

3. Select the app that you want to wrap, and then select **Wrap** on the command bar.

   > [!div class="mx-imgBorder"] 
   > ![Select the app to wrap.](media/how-to-v2/select-app-to-wrap.png "Select the app to wrap")

4. On the **Wrap** pane, select **Get started** to use the wizard.

   > [!div class="mx-imgBorder"] 
   > ![Use the wrap wizard.](media/how-to-v2/wrap-get-started.png "Use the wrap wizard")


### Step 1: Select Apps 

1. On the **Select the app(s) to wrap** screen, select your primary and secondary app.

   - **Primary app**: Select the app your end users will see when they launch the mobile app.
   - **Secondary app(s)**: Optional additional apps that you can bundle the same build for mobile app package along with the Primary app.

     > [!div class="mx-imgBorder"] 
     > ![Choose the apps to wrap.](media/how-to-v2/select-apps.png "Choose the apps to wrap")
  
     > [!NOTE]
     > You can use the same Primary app in multiple wrap projects.

2.  Select **Next**.

### Step 2: Target Platform 

1.  On the **Choose mobile platform to target** screen, enter a **Bundle ID** of our choice. 

    > [!NOTE]
    > The **Bundle ID** is a unique identifier that you create for your app. A bundle ID must contain one period (.) and no spaces. 

2. Under **Target platforms(s)**, select all the mobile platforms that your end users use on their mobile devices.

3. Set the **Sign my app (preview)** toggle to **ON** to code sign your app and then select **Next**. For more information on code sign, see:
  
   - [Code sign for iOS](code-sign-ios.md)
   - [Code sign for Android](code-sign-android.md) 

4.  Select **Next**.

### Step 3: Configure Branding

1. On the **Configure Branding Step**, set the following look and feel options for your app:
   
   - **App icons**: Upload icons to use for your app. All five icons need to be selected for your wrapped mobile app
   - **Splash screen image**: Image that will be used on the splash screen of your mobile app, while it loads. Default image used when not provided.
   - **Welcome screen image**: Image that will be used on the welcome (sign in) screen of your mobile app, while it loads. Default image used when not provided.
   - **Background fill color**: Hexadecimal color code used for the background of the welcome screen.
   - **Button fill color**: Hexadecimal color code used to fill the button color.
   - **Status bar text theme**: Color for the status bar text at the top of the app.
   
     > [!NOTE]
     > All the images must be in .png format. 

2.  Select **Next**.

### Step 4: Register app

On the **Register your app** screen, register your application in Azure to establish a trust relationship between your app and the Microsoft identity platform.

Your app must be registered in Azure ADD so that your app users can sign in. You need to go to [Azure portal](https://portal.azure.com/) to register your app and configure the API permissions on the Microsoft Identity platform.

- **For iOS**: The **Redirect URI** only requires the **Bundle ID**.  Examples for iOS:

    - **Bundle ID**: com.contoso.myapp
    - **Redirect URI**: msauth.com.contoso.myapp://auth

- **For Android**: The **Redirect URI** requires the **Package name**, and the **Signature hash**. To create the signature hash, [generate keys](code-sign-android.md#generate-keys), and then [generate signature hash](code-sign-android.md#generate-signature-hash). Examples for Android:

    - **Package name**: com.contoso.myapp
    - **Redirect URI**: msauth://com.contoso.myapp/&lt;generated signature hash&gt;

#### New app registration

For new app registration, select **New app registration** to create a new registration for your app in the organizational directory using the Azure portal. For detailed steps, see [Quickstart: Register an application with the Microsoft identity platform](/azure/active-directory/develop/quickstart-register-app).

   > [!div class="mx-imgBorder"] 
   > ![New app registration.](media/how-to-v2/new-app-reg.png "New app registration")

When creating a new app registration, ensure to use the supported account type that includes accounts in an organizational directory.

Both single tenant and multitenant customers can use wrap to create native mobile apps based on their canvas app.

However, you must select any of the options containing **Any Azure AD directory - Multitenant** when choosing the supported account type for your app to enable it for wrap:

 > [!div class="mx-imgBorder"] 
 > ![Register an app.](media/how-to-v2/wrap-2.png "Register an app")
    
The sign-in experience for users on the mobile wrapped up will still be scoped to a single tenant regardless of what type of account you choose in this step for your app.

> [!IMPORTANT]
> - Wrap only supports **Multitenant** account types currently. **Single tenant** account type is not yet supported. More information: [Account types in Microsoft identity platform](/azure/active-directory/develop/v2-supported-account-types)
> - To ensure the **Redirect URI** matches the [required format](how-to.md#redirect-uri-format), don't create the **Redirect URI** while creating the app registration. Once the app registration is complete, go to app, and then choose **Authentication** &gt; **+ Add a platform** to add the platform instead.
> - You must create a separate **Redirect URI** for each platform (iOS, Android) that you want to target.

After the app is registered, copy the **Application (client) ID** and the **Redirect URI** that you'll need later when configuring the wrap project inside Power Apps. More information: [Register an application](/azure/active-directory/develop/quickstart-register-app#register-an-application)

### Step 5: Manage output

On the **Manage output** screen, create or select an existing App Center location to send your mobile app once the build is complete. 

- **Android**: Choose an existing location or create a new location.

- **iOS**: Choose an existing location or create a new location.

### Step 6: Wrap up

On the **Wrap up** screen, review the app details and then select **Build**.
