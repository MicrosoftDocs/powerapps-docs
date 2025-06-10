---
title: Customize and build your mobile app using the wrap wizard
description: Learn about how to use the wrap wizard to package canvas apps into a native mobile app package.
author: komala2019
ms.topic: how-to
ms.custom: canvas
ms.reviewer: smurkute
ms.date: 02/04/2025
ms.subservice: canvas-maker
ms.author: koagarwa
search.audienceType: 
  - maker
contributors:
  - mkaur
---

# Wrap wizard: your step-by-step guide to build your native mobile apps package

Use this step-by-step Wrap wizard guide to convert one or more canvas apps into a single custom-branded app package that can be deployed on Google Play and the iOS App Store.

The wrap feature in Power Apps lets you create native mobile versions of your [canvas apps](../../canvas-apps/getting-started.md) as custom-branded Android and iOS mobile apps (IPA, APK, AAB packages). You can distribute these *wrapped* native mobile apps to end users through [Google Play](https://support.google.com/googleplay/work/answer/6138458), [Apple Business Manager](https://developer.apple.com/custom-apps/), or other native distribution methods.

The wrap feature wraps your canvas apps in a native mobile app shell that you can digitally sign and distribute. When you update your app and republish it, the app is automatically updated.

## Create custom-branded native Power Apps for iOS and Android using the Wrap wizard

1. Sign in to [Power Apps maker portal](https://make.powerapps.com).

2. Select **Wrap**, from the left navigation pane. [!INCLUDE [left-navigation-pane](../../../includes/left-navigation-pane.md)]

3. Select the app that you want to wrap, and then select **Wrap** on the command bar.

### Step 1: Select apps 

1. On the **Select the app(s) to wrap** screen, select your primary and secondary app.

   - **Primary app**: Select the app your end users see when the mobile app is launched.
   - **Secondary app(s)**: Optional other apps that you can bundle the same build for mobile app package along with the Primary app.

    :::image type="content" source="media/how-to-v2/select-apps-updated.png" alt-text="Screenshot that shows the first step to select the app." lightbox="media/how-to-v2/select-apps-updated.png":::
  
     > [!NOTE]
     > - You can use the same Primary app in multiple wrap projects.
     > - In the wrap wizard, if the **Primary app** name appears incorrect, proceed to the next step and then return to see the correct name.

2.  Select **Next**.

### Step 2: Target platform 

1.  On the **Choose mobile platform to target** screen, enter a **Bundle ID** of our choice. 

    > [!NOTE]
    > The **Bundle ID** is a unique identifier that you create for your app. A bundle ID must contain one period (.) and no spaces. Use this same bundle ID in step 6 when [creating the Azure key vault](create-key-vault-for-code-signing.md#configure-key-vault-uri) after generating and uploading your iOS or Android certificates. If you have already created the Azure Key Vault, verify the bundle ID in the **Tags** section of the [Azure portal](https://portal.azure.com).

2. Under **Target platforms(s)**, select all the mobile platforms that your end users use on their mobile devices.

3. Select the **Azure Key Vault URI** from the list and select **Next**. 
If you don't have any entries in **Azure Key Vault URI** list, you need to create Azure key vault first. More information: [Create a vault](/azure/key-vault/general/quick-create-portal#create-a-vault).

4. Create an Azure blob storage account and container name if you don't have it set up already. More information: [Create an Azure storage account](/azure/storage/common/storage-account-create?tabs=azure-portal). A video for creating an Azure storage account is available at [How to create a storage account](https://www.youtube.com/watch?v=AhuNgBafmUo&list=PLLasX02E8BPBKgXP4oflOL29TtqTzwhxR&index=6).

5. In your key vault in the [Azure portal](https://ms.portal.azure.com), go to **Secrets** to create Azure blob storage secret name if not done already. More information: [Add a secret to Key Vault](/azure/key-vault/secrets/quick-create-portal#add-a-secret-to-key-vault). While creating a secret, you'll need your access key. To view and copy your access key refer [View account access keys](/azure/storage/common/storage-account-keys-manage?tabs=azure-portal#view-account-access-keys).

:::image type="content" source="media/how-to-v2/azure-secret-2.png" alt-text="Screenshot that shows how to create Azure secrets" lightbox="media/how-to-v2/azure-secret-2.png":::

Enter the Azure blob storage access key in **Secret value** field.

:::image type="content" source="media/how-to-v2/azure-secret-1.png" alt-text="Screenshot that shows Azure secrets" lightbox="media/how-to-v2/azure-secret-1.png":::

6. In your key vault in the [Azure portal](https://ms.portal.azure.com), go to **Tags**, create a new tag with the same secret value as created in the preceding step.

:::image type="content" source="media/how-to-v2/azure-tag.png" alt-text="Screenshot that shows Azure tags" lightbox="media/how-to-v2/azure-tag.png":::

7. Set the **Sign my app** toggle to **On** or **Off**.

    :::image type="content" source="media/how-to-v2/select-target-platforms-updated.png" alt-text="Screenshot that shows the second step to choose the target platform." lightbox="media/how-to-v2/select-target-platforms-updated.png":::

You can also code sign your mobile app package manually instead of using automatic code signing available in wrap wizard. For more information on how to code sign your app manually, see:
  
   - [Code sign for iOS](code-sign-ios.md)
   - [Code sign for Android](code-sign-android.md) 
   - [Code sign for Google Play Store](https://developer.android.com/studio/publish/app-signing)

> [!NOTE]
> Wrap wizard provides an automatic sign-in process. However, developers familiar with mobile processes can manually sign in for their Android or iOS applications using different mechanisms for each platform.

6.  Select **Next**.

### Step 3: Register app

On the **Register your app** screen, register your application manually in Azure to establish a trust relationship between your app and the Microsoft identity platform. More information: [Registering your app on Azure portal manually](wrap-how-to.md#register-your-app-on-azure-portal-manually-optional).

Your app must be registered in Microsoft Entra so that your app users can sign in. If you have already registered, find your registration in the owned registration field.

If you don't see your registered app name in the **Owned registrations** dropdown, follow these steps.

- Select **New app registration** to create a new registration for your app automatically.
- You'll need to provide **Application name** and **Android signature hash**, as they're mandatory fields. **Application name** is required because it's the customer-facing name of the application. **Android signature hash** is necessary if you have selected Android as one of your platforms while creating and building your wrap project.

    > [!NOTE]
    > The format of the Android hash key is 28-digit alphanumeric hash number such as  –ga0RGNYHvNM5d0SLGQfpQWAPGJ8=.
    > If the signature hash key already exists, there's no need to create a new one. You can reuse the previously generated signature hash key when creating a new app registration.

    :::image type="content" source="media/how-to-v2/new-app-reg2-updated.png" alt-text="Screenshot that shows new app registration screen" lightbox="media/how-to-v2/new-app-reg2-updated.png":::

#### Configure admin allowed third-party apps

The wrap wizard configures all the required API permissions for your app automatically. You can also configure the API permissions manually if your need to troubleshoot this step. More information: [Configure the API permissions for your app manually](wrap-how-to.md#configure-the-api-permissions-for-your-app-manually-optional).

When you register the app, Azure admin needs to provide access to continue. Follow these steps to grant access:
- Open Windows PowerShell and run it as an administrator.
- Execute the command- `Install-Module -Name Microsoft.PowerApps.Administration.PowerShell -AllowClobber -Force`.
- Set the execution policy with: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned`.
- Import the module using: `Import-Module -Name Microsoft.PowerApps.Administration.PowerShell`.
- Run `Add-AdminAllowedThirdPartyApps` and provide the App ID for which admin access is needed.
- Run `Get-AdminAllowedThirdPartyApps` to verify if your app name appears in the list.

Once you complete the preceding steps the registration screen look like the following screenshot.

 :::image type="content" source="media/how-to-v2/new-app-reg-updated.png" alt-text="Screenshot that shows registration screen with green ticks for steps completed" lightbox="media/how-to-v2/new-app-reg-updated.png":::

#### API permissions

When you register the app, the Azure admin grants API permissions for the app. 
More information about granting access and the reasons why API permissions are required: [Grant tenant-wide admin consent in Enterprise apps pane](/entra/identity/enterprise-apps/grant-admin-consent?pivots=portal#grant-tenant-wide-admin-consent-in-enterprise-apps-pane).

 :::image type="content" source="media/how-to-v2/api-permissions-2.png" alt-text="Screenshot that shows the API permissions for the app." lightbox="media/how-to-v2/api-permissions-2.png":::

> [!NOTE]
> In this step, sometimes for the new customers, only the **Application name** field is visible. The field to add the **Android signature hash** isn't displayed. To resolve this, continue to the next steps and select the **Target platform(s)** as **Android** in the **Target Platforms Step**.


#### Add Redirect URIs:

1. Navigate to **Azure Portal** > **Your App Registration Name** > **Authentication**.
2. Click **"Add a platform"** and select either **iOS** or **Android** based on the App type.
3. * For **iOS**: Enter the **Bundle ID**.
   * For **Android**: Enter the **Bundle ID** and the **Signature Hash Key**.


### Step 4: Configure branding

1. On the **Configure Branding Step**, set the following look and feel options for your app:

     > [!NOTE]
     > All the images must be in .png format. A default image will be used if no custom images are selected.
   
   - **App icons**: Upload icons to use for your app. Recommended size for iOS: 1024 px by 1024 px .png image or larger. Recommended image size for Android: 432 px by 432 px .png image or larger.
   - **Splash screen image**: Image that's used on the splash screen of your mobile app, while it loads. Default image used when not provided.
   - **Welcome screen image**: Image that's used on the welcome (sign in) screen of your mobile app, while it loads. Default image used when not provided.
   - **Background fill color**: Hexadecimal color code used for the background of the welcome screen.
   - **Button fill color**: Hexadecimal color code used to fill the button color.
   - **Status bar text theme**: Color for the status bar text at the top of the app.
   
3.  Select **Next**.

### Step 5: Manage Output

1. Add the Azure blob storage account name and the container name created during target platform step. 
1. Download the built APK or IPA from the Azure blob storage location created above after the build steps are completed. To find your built APK or IPA, go to your Azure blob storage name > **Containers** > select the container name, and check your builds.


:::image type="content" source="media/how-to-v2/manage-output.png" alt-text="Screenshot that shows the fifth step on how to manage the output using Azure blob storage." lightbox="media/how-to-v2/manage-output.png":::

### Step 6: Wrap up

On the **Wrap up** screen, review the app details and then select **Build**.
After a successful build, you'll see your mobile app in the **azure blob storage location** that you have selected in the previous step.

### View your build

1. After completing the wrap-up step in wrap wizard, select the **Build** button to build your project.
1. Select **View Builds** to view your build.
1. Alternatively, go to the **Wrap projects** option in your side pane to view the build.
1. Hover over the required project, and select it.
1. The **View builds** option appears at the top header. Select it to view the build status and other options.

:::image type="content" source="media/how-to-v2/view-build.png" alt-text="Screenshot that shows how to view builds." lightbox="media/how-to-v2/view-build.png":::

> [!NOTE]
> To manually code sign an iOS app, unzip the IPA file created using a Mac device only.

## Test and distribute mobile app package

Test and distribute your application. If you face any issue while testing, [check troubleshoot page.](/troubleshoot/power-platform/power-apps/manage-apps/wrap-issues)

> [!VIDEO 4b04af25-b332-4286-a615-e3f36de574e0]

  
## Register your app on Azure portal manually (optional)
You can automatically create your app registration in the wrap wizard as mentioned in [step 3](wrap-how-to.md#step-3-register-app). Or, you can manually create a new registration for your app on Azure portal. More information: [Quickstart: Register an application with the Microsoft identity platform](/azure/active-directory/develop/quickstart-register-app).

> [!NOTE]
> Both single tenant and multitenant customers can use wrap to create native mobile apps based on their Power Apps canvas apps.

Whether you're a single or multitenant maker, you must select any of the options containing **Any Microsoft Entra directory - Multitenant** when choosing the supported account type for your app to enable it for wrap. Choose one of the following account types:
 - Accounts in any organizational directory (Any Microsoft Entra directory - Multitenant)
 - Accounts in any organizational directory (Any Microsoft Entra directory - Multitenant) and personal Microsoft accounts such as Skype or Xbox.

:::image type="content" source="media/wrap-intro/AppResgistration_AccountTypes.png" alt-text="App registration - supported account types for wrap.":::


> [!IMPORTANT]
> - Wrap only supports **Multitenant** account types currently. **Single tenant** account type isn't yet supported. More information on the account types: [Account types in Microsoft identity platform](/azure/active-directory/develop/v2-supported-account-types).
> - You must create a separate **Redirect URI** for each platform (iOS, Android) that you want to target.

## Configure the API permissions for your app manually (optional)

When you complete [step 3](wrap-how-to.md#step-3-register-app) the wrap wizard will automatically configure all the required API permissions for your app. 

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
> - Ensure the module [Microsoft Graph](https://www.powershellgallery.com/packages/Microsoft.Graph/) is available or install it using the following command:
>     ```powershell
>     Install-Module -Name Microsoft.Graph
>     ```
> - Missing *Azure API Connections* permission: 
>     ```powershell
>     Connect-MgGraph -TenantId <your tenant ID>
>     New-MgServicePrincipal -AppId fe053c5f-3692-4f14-aef2-ee34fc081cae -DisplayName "Azure API Connections"
>     ```
> - Missing *PowerApps Service* permission:
>     ```powershell
>     Connect-MgGraph -TenantId <your tenant ID>
>     New-MgServicePrincipal -AppId 475226c6-020e-4fb2-8a90-7a972cbfc1d4 -DisplayName "PowerApps Service"
>     ```

For detailed steps, refer to [Request the permissions in the app registration portal](/azure/active-directory/develop/v2-permissions-and-consent#request-the-permissions-in-the-app-registration-portal).

## Sign your mobile app package manually (optional)

You can automatically sign your mobile app package during wrap process in **Step 2**, but you can also do so manually after the mobile app package is build. [Code signing](overview.md#code-signing) process is different for Android and iOS devices.

- [Manual code sign for iOS](code-sign-ios.md)
- [Manual code sign for Android](code-sign-android.md)
- [Code signing for Google Play Store](https://developer.android.com/studio/publish/app-signing)


## See also
- [Troubleshoot issues with the wrap feature in Power Apps](/troubleshoot/power-platform/power-apps/manage-apps-and-solutions/wrap-issues)
- [Wrap overview](overview.md)
- [Manual code sign for iOS](code-sign-ios.md)
- [Manual code sign for Android](code-sign-android.md)
- [Code sign for Google Play Store](https://developer.android.com/studio/publish/app-signing)
- [Create your Azure Key Vault for automated code signing](create-key-vault-for-code-signing.md)
- [Frequently asked questions for wrap](faq.yml)  
- [Troubleshoot issues with the wrap feature in Power Apps](/troubleshoot/power-platform/power-apps/manage-apps/wrap-issues)  

