---
title: Customize and build your mobile app using the wrap wizard
description: Learn about how to use the wrap wizard to package canvas apps into a native mobile app package.
author: komala2019
ms.topic: how-to
ms.custom: canvas
ms.reviewer: smurkute
ms.date: 06/10/2025
ms.subservice: canvas-maker
ms.author: koagarwa
search.audienceType: 
  - maker
contributors:
  - mkaur
---

# Wrap wizard: your step-by-step guide to build your native mobile apps package

Use this guide to convert one or more canvas apps into a single custom-branded app package that can be deployed on Google Play and the iOS App Store.

The wrap feature in Power Apps lets you create native mobile versions of your [canvas apps](../../canvas-apps/getting-started.md) as custom-branded Android and iOS mobile apps (IPA, APK, AAB packages). You can distribute these *wrapped* native mobile apps to end users through [Google Play](https://support.google.com/googleplay/work/answer/6138458), [Apple Business Manager](https://developer.apple.com/custom-apps/), or other native distribution methods.

When you update and republish your app, the wrapped app is automatically updated for users.

## Steps to create a custom-branded native app using the Wrap wizard

> [!VIDEO 4b04af25-b332-4286-a615-e3f36de574e0]

### 1. Sign in and start a wrap project

1. Go to the [Power Apps maker portal](https://make.powerapps.com).
2. Select **Wrap** from the left navigation pane. [!INCLUDE [left-navigation-pane](../../../includes/left-navigation-pane.md)]
3. Select the app you want to wrap, then select **Wrap** on the command bar.

### 2. Select apps

1. On the **Select the app(s) to wrap** screen, choose your primary app (the main app users see at launch) and any optional secondary apps to bundle.

    - **Primary app**: The main app users see when the mobile app launches.
    - **Secondary app(s)**: Optional additional apps bundled in the same mobile app package.

    :::image type="content" source="media/how-to-v2/select-apps-updated.png" alt-text="Screenshot that shows the first step to select the app." lightbox="media/how-to-v2/select-apps-updated.png":::

    > [!NOTE]
    > - You can use the same Primary app in multiple wrap projects.
    > - If the **Primary app** name appears incorrect, proceed to the next step and return to refresh the name.

2. Select **Next**.

### 3. Choose target platform

1. On the **Choose mobile platform to target** screen, enter a **Bundle ID**.

    > [!NOTE]
    > The **Bundle ID** is a unique identifier for your app. It must contain one period (.) and no spaces. Use this same bundle ID when [creating the Azure key vault](create-key-vault-for-code-signing.md#configure-key-vault-uri) after generating and uploading your iOS or Android certificates. If you have already created the Azure Key Vault, verify the bundle ID in the **Tags** section of the [Azure portal](https://portal.azure.com).

2. Under **Target platforms(s)**, select all the mobile platforms your users need.
3. Select the **Azure Key Vault URI** from the list and select **Next**.  
   If you don't see any entries, [create an Azure key vault](/azure/key-vault/general/quick-create-portal#create-a-vault).

4. Create an Azure blob storage account and container if you haven't already. More information: [Create an Azure storage account](/azure/storage/common/storage-account-create?tabs=azure-portal).  
   [How to create a storage account (video)](https://www.youtube.com/watch?v=AhuNgBafmUo&list=PLLasX02E8BPBKgXP4oflOL29TtqTzwhxR&index=6).

5. In your key vault in the [Azure portal](https://ms.portal.azure.com), go to **Secrets** to create a secret for your Azure blob storage access key. More information: [Add a secret to Key Vault](/azure/key-vault/secrets/quick-create-portal#add-a-secret-to-key-vault).  
   To view and copy your access key: [View account access keys](/azure/storage/common/storage-account-keys-manage?tabs=azure-portal#view-account-access-keys).

    :::image type="content" source="media/how-to-v2/azure-secret-2.png" alt-text="Screenshot that shows how to create Azure secrets" lightbox="media/how-to-v2/azure-secret-2.png":::

    Enter the Azure blob storage access key in the **Secret value** field.

    :::image type="content" source="media/how-to-v2/azure-secret-1.png" alt-text="Screenshot that shows Azure secrets" lightbox="media/how-to-v2/azure-secret-1.png":::

6. In your key vault, go to **Tags** and create a new tag with the same secret value as above.

    :::image type="content" source="media/how-to-v2/azure-tag.png" alt-text="Screenshot that shows Azure tags" lightbox="media/how-to-v2/azure-tag.png":::

7. Set the **Sign my app** toggle to **On** or **Off**.

    :::image type="content" source="media/how-to-v2/select-target-platforms-updated.png" alt-text="Screenshot that shows the second step to choose the target platform." lightbox="media/how-to-v2/select-target-platforms-updated.png":::

You can also code sign your mobile app package manually instead of using automatic code signing. For more information, see:  
- [Code sign for iOS](code-sign-ios.md)  
- [Code sign for Android](code-sign-android.md)  
- [Code sign for Google Play Store](https://developer.android.com/studio/publish/app-signing)

> [!NOTE]
> Wrap wizard provides an automatic sign-in process. Developers can also manually sign for Android or iOS using platform-specific methods.

Select **Next**.

### 4. Register your app

On the **Register your app** screen, register your application in Azure to establish trust with Microsoft identity platform. More information: [Registering your app on Azure portal manually](wrap-how-to.md#register-your-app-on-azure-portal-manually-optional).

- If you have already registered, find your registration in the owned registration field.
- If you don't see your registered app name in the **Owned registrations** dropdown:
  - Select **New app registration** to create a new registration.
  - Provide **Application name** and **Android signature hash** (if targeting Android).

    > [!NOTE]
    > The Android hash key is a 28-character alphanumeric string (for example: –ga0RGNYHvNM5d0SLGQfpQWAPGJ8=).  
    > If the signature hash key already exists, you can reuse it.

    :::image type="content" source="media/how-to-v2/new-app-reg2-updated.png" alt-text="Screenshot that shows new app registration screen" lightbox="media/how-to-v2/new-app-reg2-updated.png":::
- Configure the App to be multi-tenant by following the below steps:
  - In the azure portal as an App admin, go to App registrations and select your app.
  - In the Essentials section, locate Supported account types. Select the account type, set it to Accounts in any organizational directory (Any Microsoft Entra directory - Multitenant).

Save your changes.
#### Configure admin allowed third-party apps

The wrap wizard configures required API permissions automatically. You can also configure API permissions manually if needed. More information: [Configure the API permissions for your app manually](wrap-how-to.md#configure-the-api-permissions-for-your-app-manually-optional).

To grant admin access:
- Open Windows PowerShell as administrator.
- Run:
    ```powershell
    Install-Module -Name Microsoft.PowerApps.Administration.PowerShell -AllowClobber -Force
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
    Import-Module -Name Microsoft.PowerApps.Administration.PowerShell
    Add-AdminAllowedThirdPartyApps
    Get-AdminAllowedThirdPartyApps
    ```
- Provide the App ID when prompted.

After completing these steps, the registration screen will look like this:

 :::image type="content" source="media/how-to-v2/new-app-reg-updated.png" alt-text="Screenshot that shows registration screen with green ticks for steps completed" lightbox="media/how-to-v2/new-app-reg-updated.png":::

#### API permissions

Azure admin grants API permissions during registration. More information: [Grant tenant-wide admin consent in Enterprise apps pane](/entra/identity/enterprise-apps/grant-admin-consent?pivots=portal#grant-tenant-wide-admin-consent-in-enterprise-apps-pane).

 :::image type="content" source="media/how-to-v2/api-permissions-2.png" alt-text="Screenshot that shows the API permissions for the app." lightbox="media/how-to-v2/api-permissions-2.png":::

Run these PowerShell commands as an azure admin:
- Ensure the module [Microsoft Graph](https://www.powershellgallery.com/packages/Microsoft.Graph/) is available or install it:
    ```powershell
     Install-Module -Name Microsoft.Graph
     ```
- Grant *Azure API Connections* permission: 
     ```powershell
     Connect-MgGraph -TenantId <your tenant ID>
     New-MgServicePrincipal -AppId fe053c5f-3692-4f14-aef2-ee34fc081cae -DisplayName "Azure API Connections"
     ```
- Grant *PowerApps Service* permission:
     ```powershell
     Connect-MgGraph -TenantId <your tenant ID>
     New-MgServicePrincipal -AppId <AppId> 475226c6-020e-4fb2-8a90-7a972cbfc1d4 -DisplayName "PowerApps Service"
     ```

> [!NOTE]
> If only the **Application name** field is visible, continue to the next steps and select **Android** as a target platform to display the signature hash field.


#### Add Redirect URIs

1. In Azure Portal, go to your app registration > **Authentication**.
2. Select **Add a platform** and choose **iOS** or **Android**.
3. For iOS, enter the **Bundle ID**. For Android, enter the **Bundle ID** and **Signature hash key**.

### 5. Configure branding

On the **Configure Branding** step, set the following options for your app:

> [!NOTE]
> All images must be in .png format. A default image is used if no custom images are selected.

- **App icons**: Recommended size for iOS: 1024x1024 px or larger. For Android: 432x432 px or larger.
- **Splash screen image**: Image shown while the app loads.
- **Welcome screen image**: Image shown on the sign-in screen.
- **Background fill color**: Hex color code for the welcome screen background.
- **Button fill color**: Hex color code for button color.
- **Status bar text theme**: Color for the status bar text.

Select **Next**.

### 6. Manage output

1. Enter your Azure blob storage account and container name.
2. After the build completes, download your APK or IPA from the Azure blob storage location.

:::image type="content" source="media/how-to-v2/manage-output.png" alt-text="Screenshot that shows the fifth step on how to manage the output using Azure blob storage." lightbox="media/how-to-v2/manage-output.png":::

### 7. Wrap up and build

On the **Wrap up** screen, review your app details and select **Build**. After a successful build, your app package will be available in the Azure blob storage you specified.

### View your build

1. After building, select **View Builds** or go to **Wrap projects** in the side pane to see build status and options.
2. Hover over the required project and select it.
3. The **View builds** option appears at the top header. Select it to view the build status and other options.

:::image type="content" source="media/how-to-v2/view-build.png" alt-text="Screenshot that shows how to view builds." lightbox="media/how-to-v2/view-build.png":::

> [!NOTE]
> To manually code sign an iOS app, unzip the IPA file using a Mac device.

## Test and distribute your app

Test your app and distribute it as needed. If you encounter issues, see the [troubleshooting page](/troubleshoot/power-platform/power-apps/manage-apps/wrap-issues).


---

## Register your app on Azure portal manually (optional)

You can create your app registration automatically in the wizard or manually in Azure. More information: [Quickstart: Register an application with the Microsoft identity platform](/azure/active-directory/develop/quickstart-register-app).

> [!NOTE]
> Both single tenant and multitenant customers can use wrap to create native mobile apps based on their Power Apps canvas apps.

When registering, select an account type containing **Any Microsoft Entra directory - Multitenant**.

:::image type="content" source="media/wrap-intro/AppResgistration_AccountTypes.png" alt-text="App registration - supported account types for wrap.":::

> [!IMPORTANT]
> - Wrap only supports **Multitenant** account types currently. **Single tenant** account type isn't yet supported. More information: [Account types in Microsoft identity platform](/azure/active-directory/develop/v2-supported-account-types).
> - You must create a separate **Redirect URI** for each platform (iOS, Android).

---

## Configure API permissions manually (optional)

If you get errors, you can manually configure API permissions. More information: [Add and configure](/azure/active-directory/develop/v2-permissions-and-consent#request-the-permissions-in-the-app-registration-portal)

Required API permissions:

- **Microsoft APIs**
    - Dynamics CRM
- **APIs my organization uses**
    - Azure API Connections
    - PowerApps Service
    - Power BI (if your app uses Power BI data)
    - Microsoft Mobile Application Management (for [Intune](/mem/intune/fundamentals/what-is-intune) distribution)


For detailed steps, see [Request the permissions in the app registration portal](/azure/active-directory/develop/v2-permissions-and-consent#request-the-permissions-in-the-app-registration-portal).

---

## Sign your mobile app package manually (optional)

You can sign your app automatically in **Step 2** or manually after building. [Code signing](overview.md#code-signing) is different for Android and iOS.

- [Manual code sign for iOS](code-sign-ios.md)
- [Manual code sign for Android](code-sign-android.md)
- [Code signing for Google Play Store](https://developer.android.com/studio/publish/app-signing)

---

## See also

- [Troubleshoot issues with the wrap feature in Power Apps](/troubleshoot/power-platform/power-apps/manage-apps-and-solutions/wrap-issues)
- [Wrap overview](overview.md)
- [Manual code sign for iOS](code-sign-ios.md)
- [Manual code sign for Android](code-sign-android.md)
- [Code sign for Google Play Store](https://developer.android.com/studio/publish/app-signing)
- [Create your Azure Key Vault for automated code signing](create-key-vault-for-code-signing.md)
- [Frequently asked questions for wrap](faq.yml)
- [Troubleshoot issues with the wrap feature in Power Apps](/troubleshoot/power-platform/power-apps/manage-apps/wrap-issues)
