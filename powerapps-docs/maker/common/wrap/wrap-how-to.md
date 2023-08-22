---
title: Customize and build your mobile app using the wrap wizard
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

# Use the wrap wizard to build your mobile app

Use the wrap feature to package one or more canvas app(s) as a single native mobile app package using the step-by-step wizard.

The wrap feature in Power Apps lets you create native mobile versions of your [canvas apps](../../canvas-apps/getting-started.md) as custom-branded Android and iOS mobile apps. 
You can distribute such *wrapped* native mobile apps to the end users through [Microsoft Intune](/mem/intune/fundamentals/what-is-intune), [Microsoft app center](https://visualstudio.microsoft.com/app-center/), [Google Play](https://support.google.com/googleplay/work/answer/6138458) or [Apple Business Manager](https://developer.apple.com/custom-apps/) or other native distribution methods.

Wrap feature allows you to create mobile apps for iOS, Android or Google Play Store:

- iOS (IPA package)
- Android (APK package)
- Google Play Store (AAB package)

The wrap feature wraps your canvas apps in a native mobile app shell that you can digitally sign and distribute. When you update your app and republish it, the app is automatically updated.


## Prerequisites

You need access to:
- [Azure portal](https://portal.azure.com/) to register your app.
- [App center](https://appcenter.ms/) to add new organization and apps.
- This feature requires the apps to be part of a  [managed or unmanaged solution](/power-platform/alm/solution-concepts-alm#managed-and-unmanaged-solutions). If your apps aren't part of a solution already, add them to an existing or a new solution. More information: [Create a canvas app from within a solution](../../canvas-apps/add-app-solution.md#add-an-existing-canvas-app-to-a-solution). 

If you're creating a mobile app package for Android platform and you plan to code sign it manually, ensure you [<u>generate keys</u>](code-sign-android.md#generate-keys), and then [generate signature hash](code-sign-android.md#generate-signature-hash) before you start. You need the generated signature hash to configure the **Redirect URI**.

## Add canvas app to solution

Wrap for Power Apps requires the apps to be part of a solution. If your canvas apps aren't part of a solution already, add them to an existing or a new solution. Go to **Solutions** section, select a solution and press **Edit** button.

:::image type="content" source="media/wrap-canvas-app/select-solution.png" alt-text="Select a solution.":::

Choose **+ Add existing** option from the top menu and select **App > Canvas app** in the dropdown list.

:::image type="content" source="media/wrap-canvas-app/select-add-existing.png" alt-text="Select Add existing from the menu.":::

Select **Outside Dataverse** tab and choose your app from the list. Press **Add** button to add this app to a solution.

:::image type="content" source="media/wrap-canvas-app/add-app.png" alt-text="Select Add app to a solution.":::

More information: [Add an app to a solution](../../canvas-apps/add-app-solution.md#add-an-existing-canvas-app-to-a-solution)


## Create native mobile apps for iOS and Android using the wizard

1. Sign in to [Power Apps](https://make.powerapps.com).

2. Select **Apps**, from the left navigation pane. 

3. Select the app that you want to wrap, and then select **Wrap** on the command bar.

   > [!div class="mx-imgBorder"] 
   > ![Select the app to wrap.](media/how-to-v2/select-app-to-wrap.png "Select the app to wrap")


### Step 1: Select apps 

1. On the **Select the app(s) to wrap** screen, select your primary and secondary app.

   - **Primary app**: Select the app your end users see when the mobile app is launched.
   - **Secondary app(s)**: Optional other apps that you can bundle the same build for mobile app package along with the Primary app.

     > [!div class="mx-imgBorder"] 
     > ![Choose theapps that you want to wrap.](media/how-to-v2/select-apps.png "Choose the apps to wrap")
  
     > [!NOTE]
     > You can use the same Primary app in multiple wrap projects.

2.  Select **Next**.

### Step 2: Target platform 

1.  On the **Choose mobile platform to target** screen, enter a **Bundle ID** of our choice. 

    > [!NOTE]
    > The **Bundle ID** is a unique identifier that you create for your app. A bundle ID must contain one period (.) and no spaces. 

2. Under **Target platforms(s)**, select all the mobile platforms that your end users use on their mobile devices.

3. Set the **Sign my app** toggle to **ON** to automatically code sign your mobile app, then select the **Azure Key Vault URI** from the list and click **Next**. 
If you don't have any entries in **Azure Key Vault URI** list, you need to create **Azure Key Vault** first. More information: [Create Azure key valut for wrap for Power Apps](create-key-vault-for-code-signing.md).

     > [!div class="mx-imgBorder"] 
     > ![Choose the apps which you want to wrap.](media/how-to-v2/select-target-platforms.png "Select target platforms")

You can also code sign your mobile app package manually instead of using automatic code signing available in wrap wizard. For more information on how to code sign your app manually, see:
  
   - [Code sign for iOS](code-sign-ios.md)
   - [Code sign for Android](code-sign-android.md) 
   - [Code sign for Google Play Store](https://developer.android.com/studio/publish/app-signing)

4.  Select **Next**.

### Step 3: Configure branding

1. On the **Configure Branding Step**, set the following look and feel options for your app:

     > [!NOTE]
     > All the images must be in .png format. A default image will be used if no custom images are selected.
   
   - **App icons**: Upload icons to use for your app. Recommended size for iOS: 1024px by 1024px .png image or larger. Recommended image size for Android: 432px by 432px .png image or larger. 
   - **Splash screen image**: Image that's used on the splash screen of your mobile app, while it loads. Default image used when not provided.
   - **Welcome screen image**: Image that's used on the welcome (sign in) screen of your mobile app, while it loads. Default image used when not provided.
   - **Background fill color**: Hexadecimal color code used for the background of the welcome screen.
   - **Button fill color**: Hexadecimal color code used to fill the button color.
   - **Status bar text theme**: Color for the status bar text at the top of the app.
   


3.  Select **Next**.

### Step 4: Register app

On the **Register your app** screen, register your application in Azure to establish a trust relationship between your app and the Microsoft identity platform. Your app must be registered in Azure Active Directory so that your app users can sign in. 

#### New app registration

Select **New app registration** to create a new registration for your app automatically.

   > [!div class="mx-imgBorder"] 
   > ![Create a new app registration.](media/how-to-v2/new-app-reg.png "New app registration")

You can also create a **new app registration** manually. More information: [Registering your app on Azure portal manually](wrap-how-to.md#register-your-app-on-azure-portal-manually-optional).

The wrap wizard configures all the required API permissions for your app automatically. You can also configure the API permissions manually if your need to stoubeshoot this step. More information: [Configure the API permissions for your app manually](wrap-how-to.md#configure-the-api-permissions-for-your-app-manually-optional).

### Step 5: Manage output

On the **Manage output** screen, create or select an existing **app center location** to send your mobile app once the build is complete. To automatically create a new location in wrap wizard, select **New location** on top of the screen, and then select **Android** or **iOS**.

> [!div class="mx-imgBorder"] 
> ![New app center location.](media/how-to-v2/new-app-center-location.png "Create new app center location")

- **Android**: Choose an existing location or create a new location.

- **iOS**: Choose an existing location or create a new location.

You can also choose to create your **app center location** manually at [App Center](https://appcenter.ms/). More information: [Create an app center location for your mobile app manually](wrap-how-to.md#create-an-app-center-location-for-your-mobile-app-manually-optional).

### Step 6: Wrap up

On the **Wrap up** screen, review the app details and then select **Build**.
After a successful build, you'll see your mobile app in the **app center location** that you have selected in the previous step.

## Test and distribute mobile app package

For testing and distribution, see [App center test](/appcenter/test-cloud/) and [Distribute](/appcenter/distribution/).


  
## Register your app on Azure portal manually (optional)
You can automatically create your app registration in the wrap wizard as mentioned in [step 4](wrap-how-to.md#step-4-register-app). Or, you can manually create a new registration for your app on Azure portal. More information: [Quickstart: Register an application with the Microsoft identity platform](/azure/active-directory/develop/quickstart-register-app).

> [!NOTE]
> Both single tenant and multitenant customers can use wrap to create native mobile apps based on their Power Apps canvas apps.

Whether you're a single or multitenant maker, you must select any of the options containing **Any Azure AD directory - Multitenant** when choosing the supported account type for your app to enable it for wrap. Choose one of the following account types:
 - Accounts in any organizational directory (Any Azure AD directory - Multitenant)
 - Accounts in any organizational directory (Any Azure AD directory - Multitenant) and personal Microsoft accounts such as Skype or Xbox.

:::image type="content" source="media/wrap-intro/AppResgistration_AccountTypes.png" alt-text="App registration - supported account types for wrap.":::


> [!IMPORTANT]
> - Wrap only supports **Multitenant** account types currently. **Single tenant** account type is not yet supported. More information on the account types: [Account types in Microsoft identity platform](/azure/active-directory/develop/v2-supported-account-types).
> - You must create a separate **Redirect URI** for each platform (iOS, Android) that you want to target.

## Configure the API permissions for your app manually (optional)

When you complete [step 4](wrap-how-to.md#step-4-register-app) the wrap wizard will automatically configure all the required API permissions for your app. 

If you get errors in wrap wizard, you can manually configure API permissions. More information: [Add and configure](/azure/active-directory/develop/v2-permissions-and-consent#request-the-permissions-in-the-app-registration-portal)

The following API permissions are required when manually configure API permissions:

- **Microsoft APIs**
    - *Dynamics CRM*
- **APIs my organization uses**
    - *Azure API Connections*
    - *PowerApps Service*
    - *Power BI* (only required if your canvas app(s) use Power BI data)
    - *Microsoft Mobile Application Management* (only required if you want to use [Microsoft Intune](/mem/intune/fundamentals/what-is-intune) for mobile app distribution)

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
  
## Create an app center location for your mobile app manually (optional)

You have an option to automatically create a new **app center location** to store your mobile app as mentioned in [step 5](wrap-how-to.md#step-5-manage-output) in wrap wizard, but you can also manually create it directly in app center. More information: [App center location](overview.md#app-center-location)

> [!TIP]
> For more information about app center, go to [Visual Studio app center documentation](/appcenter/).

1. Go to [app center](https://appcenter.ms/).
1. Sign in with your work or school account.
1. If you don't have any existing organization, select **Add new** &gt; **Add new organization** to create a new organization.
1. Select the organization from the list on the left-pane.
1. Select **Apps** &gt; **Add app**.
1. Enter app name.
1. Select app release type.
1. Select **Custom** OS for iOS apps, or **Android** OS for Android apps.

    > [!NOTE]
    > You must create separate app center containers for each platform.

1. For **Android** OS, select **Platform** as **React Native**.

    > [!NOTE]
    > **Platform** must be **React Native** for all apps in app center.

    :::image type="content" source="media/wrap-canvas-app/app-center-app.png" alt-text="App center app configuration.":::

1. Select **Add new app**.

1. Copy the app's app center URL that you need later when your configure the wrap project inside Power Apps.

    For example, `https://appcenter.ms/orgs/Contoso-sales/apps/Sample-canvas-app-for-Android-OS/`

    :::image type="content" source="media/wrap-canvas-app/app-center-url.png" alt-text="App center URL.":::

 

## Sign your mobile app package manually (optional)
You can automatically sign your mobile app package during wrap process in **Step 2**, but you can also do so manually after the mobile app package is build. [Code signing](overview.md#code-signing) process is different for Android and iOS devices.

- [Code signing for iOS](code-sign-ios.md)
- [Code signing for Android](code-sign-android.md)
- [Code signing for Google Play Store](https://developer.android.com/studio/publish/app-signing)


## See also
- [Troubleshoot issues with the wrap feature in Power Apps](/troubleshoot/power-platform/power-apps/manage-apps-and-solutions/wrap-issues)
- [Wrap overview](overview.md)
- [Code sign for iOS](code-sign-ios.md)
- [Code sign for Android](code-sign-android.md)
- [Code sign for Google Play Store](https://developer.android.com/studio/publish/app-signing)
- [Create your Azure key vault for automated code signing](create-key-vault-for-code-signing.md)
- [Frequently asked questions for wrap](faq.yml)
