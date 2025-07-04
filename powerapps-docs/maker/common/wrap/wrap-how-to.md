---
title: Customize and build your mobile app using the wrap wizard
author: komala2019
ms.topic: how-to
ms.custom: canvas
ms.reviewer: smurkute
ms.date: 06/18/2025
ms.subservice: canvas-maker
ms.author: koagarwa
search.audienceType: 
  - maker
contributors:
  - mkaur
---

# Wrap wizard: Step-by-step guide to building your native mobile app

Use this guide to convert one or more canvas apps into a single custom-branded app package that you can deploy on Google Play and the iOS App Store.

The wrap feature in Power Apps enables you to create native mobile versions of your [canvas apps](../../canvas-apps/getting-started.md) as custom-branded Android and iOS mobile apps (IPA, APK, AAB packages). You can distribute these wrapped native mobile apps to end users through [Google Play](https://support.google.com/googleplay/work/answer/6138458), [Apple Business Manager](https://developer.apple.com/custom-apps/), or other native distribution methods.

When you update and republish your app, the wrapped app is automatically updated for users.



## Steps to create a custom-branded native app using the wrap wizard

> [!VIDEO 4b04af25-b332-4286-a615-e3f36de574e0]

### 1. Sign in and start a wrap project

1. Sign in to [Power Apps maker portal](https://make.powerapps.com).
2. Select **Wrap** from the left navigation pane. [!INCLUDE [left-navigation-pane](../../../includes/left-navigation-pane.md)]
3. Select the app you want to wrap, then select **Wrap** on the command bar.

### 2. Select apps

1. On the **Select the app(s) to wrap** screen, select your primary and secondary app.

   - **Primary app**: The main app end users see when the mobile app launches.
   - **Secondary app(s)**: Optional other apps bundled in the same mobile app package.

   :::image type="content" source="media/how-to-v2/select-apps-updated.png" alt-text="Screenshot that shows the first step to select the app." lightbox="media/how-to-v2/select-apps-updated.png":::

   > [!NOTE]
   > - You can use the same primary app in multiple wrap projects.
   > - If the primary app name appears incorrect, proceed to the next step and return to refresh the name.

2. Select **Next**.

### 3. Choose target platform

1. On the **Choose mobile platform to target** screen, enter a **Bundle ID**.

   > [!NOTE]
   > The **Bundle ID** is a unique identifier that you create for your app. It must contain one period (.) and no spaces. Use this same bundle ID when [creating the Azure key vault](create-key-vault-for-code-signing.md#configure-key-vault-uri) after generating and uploading your iOS or Android certificates. If you have already created the Azure Key Vault, verify the bundle ID in the **Tags** section of the [Azure portal](https://portal.azure.com).

2. Under **Target platform(s)**, select all the mobile platforms that your end users use on their mobile devices.

3. Turn **ON** automatic app signing (Optional).
   :::image type="content" source="media/how-to-v2/select-target-platforms-updated.png" alt-text="Screenshot that shows the second step to choose the target platform." lightbox="media/how-to-v2/select-target-platforms-updated.png":::

   > [!NOTE]
   > Manual signing options:
   > - [Code sign for iOS](code-sign-ios.md)
   > - [Code sign for Android](code-sign-android.md)
   > - [Code sign for Google Play Store](https://developer.android.com/studio/publish/app-signing)
   >
   > You must manually sign AAB files regardless of the signing option selected in the wizard.
  
      a. If you choose automatic signing, [create an Azure key vault](create-key-vault-for-code-signing.md#configure-key-vault-uri), if you haven't created one. Add the required tags, secrets, and certificates described in the link for automatic signing. Add the environment     variable  if not created already. To create the environment variable, go to [Power Apps](https://make.powerapps.com) > **Solutions** > **Default solution**.  
         Then select **New** > **More** > **Environment variable**, add the display name as "PA_Wrap_KV_ResourceID".
        :::image type="content" source="media/how-to-v2/add-new-env-variable.png" alt-text="Screenshot that shows screen for adding new environment variable." lightbox="media/how-to-v2/add-new-env-variable.png":::
      
      b. To add vault information to your environment variables, access the **Azure** portal as an admin. Navigate to **All Resources** > **Your Key Vault** > **Properties**, and then copy the **Resource ID**. 
         :::image type="content" source="media/how-to-v2/copy-resource-id.png" alt-text="Screenshot that shows resource id to be copied." lightbox="media/how-to-v2/copy-resource-id.png":::
    
      c. To add the input to the environment variable, go to **Power Apps** > **ApplicationName** > **All** > **Environment variable**. Click the three dots, select **Edit**, add the copied value to **Default value**, and save. 
    
      d. To check whether the table value has been updated, go to **Power Apps** > **Tables** > **Environment variable definition** > **new_PA_Wrap_KV_ResourceID** . The value in **Default value** must be same as that of the resourceID for which you want to add the vault. 
         > [!NOTE]
         > Guidelines for adding the input behind the environment variables for Key vault information:
         > - Environment variables must not be empty or can contain multiple entries.
         > - Ensure that the resourceID added is correct (verify spelling).
         > - Ensure that the resourceID added has non-empty tags and includes all the tags expected with the bundle ID used in the wrap wizard.
    
      e. Follow the steps in [Steps for automated code signing](create-key-vault-for-code-signing.md) to create the tags, secrets, and certificates required during the automatic signing process.

4. Turn **ON** Azure blob storage to upload your build to Azure blob storage. If you haven't already, create an Azure blob storage account and container.
   - More about creating a storage account: [Create an Azure storage account](/azure/storage/common/storage-account-create?tabs=azure-portal).
   - Watch a tutorial: [How to create a storage account](https://www.youtube.com/watch?v=AhuNgBafmUo&list=PLLasX02E8BPBKgXP4oflOL29TtqTzwhxR&index=6).
   > [!NOTE]
   > You can download the link from the wrap wizard if you don't use the blob storage mechanism.
   
   1. In your key vault in the [Azure portal](https://ms.portal.azure.com), go to **Secrets** to create a secret for your Azure blob storage access key. More information: [Add a secret to key vault](/azure/key-vault/secrets/quick-create-portal#add-a-secret-to-key-vault).
      :::image type="content" source="media/how-to-v2/azure-secret-2.png" alt-text="Screenshot that shows how to create Azure secrets" lightbox="media/how-to-v2/azure-secret-2.png":::
      
   2. To view and copy your access key: [View account access keys](/azure/storage/common/storage-account-keys-manage?tabs=azure-portal#view-account-access-keys)
      :::image type="content" source="media/how-to-v2/view-access-key.png" alt-text="Screenshot that shows access key" lightbox="media/how-to-v2/view-access-key.png":::

   3. Enter the Azure blob storage access key in the **Secret value** field.
      :::image type="content" source="media/how-to-v2/azure-secret-1.png" alt-text="Screenshot that shows Azure secrets" lightbox="media/how-to-v2/azure-secret-1.png":::
      
   4. In your key vault, go to **Tags** and create a new tag with the same secret value as above.
      :::image type="content" source="media/how-to-v2/azure-tag.png" alt-text="Screenshot that shows Azure tags" lightbox="media/how-to-v2/azure-tag.png":::

5. Select **Next**.

### 4. Register your app

On the **Register your app** screen, register your application in Azure to establish trust with the Microsoft identity platform.

- **If you have already registered an app**:
  - Find your registration in the owned registration field.

- **If you do not see your registered app**:
  1. Select **New app registration** to create a new registration.
  2. Provide:
     - **Application name**: The customer-facing name of your app
     - **Android signature hash** (if targeting Android): A 28-character alphanumeric string
       :::image type="content" source="media/how-to-v2/new-app-reg2-updated.png" alt-text="Screenshot that shows new app registration screen" lightbox="media/how-to-v2/new-app-reg2-updated.png":::
  3. In the Microsoft Entra admin center, go to App registrations and select your app. In the Essentials section, locate Supported account types, set it to Accounts in any organizational directory (Any Microsoft Entra directory - Multitenant).
      :::image type="content" source="media/how-to-v2/registration-multitenant.png" alt-text="Screenshot that shows multitenant registration screen" lightbox="media/how-to-v2/registration-multitenant.png":::
  4. Save your changes.

     > [!NOTE]
     > If the signature hash key already exists, you can reuse it.

     
#### Configure admin allowed third-party apps as an azure tenant admin

The wrap wizard configures required API permissions automatically. To grant admin access:

1. Open Windows PowerShell as administrator.
2. Run these commands:
   ```powershell
   Install-Module -Name Microsoft.PowerApps.Administration.PowerShell -AllowClobber -Force
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
   Import-Module -Name Microsoft.PowerApps.Administration.PowerShell
   Add-AdminAllowedThirdPartyApps
   Get-AdminAllowedThirdPartyApps
   ```
3. Provide the App ID when prompted.

After completing these steps, the registration screen will look like this:

:::image type="content" source="media/how-to-v2/new-app-reg-updated.png" alt-text="Screenshot that shows registration screen with green ticks for steps completed" lightbox="media/how-to-v2/new-app-reg-updated.png":::

#### Grant API permissions as an Azure tenant admin

Azure admin grants API permissions during registration. Make sure **DeviceManagementManagedApplication** is set to **Yes** when you grant admin consent for your app. For more information, see [Grant tenant-wide admin consent in Enterprise apps pane](/entra/identity/enterprise-apps/grant-admin-consent?pivots=portal#grant-tenant-wide-admin-consent-in-enterprise-apps-pane).
    :::image type="content" source="media/how-to-v2/api-permissions-2.png" alt-text="Screenshot that shows the API permissions for the app." lightbox="media/how-to-v2/api-permissions-2.png":::

### Required API permissions

| API Type                    | Specific API                                             | Reason                                                                                                                       |
|----------------------------|----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| **Microsoft APIs**         | Dynamics CRM                                             | The application needs `user_impersonation` to call Dataverse for the user.                      |
| **APIs my organization uses** | Azure API Connections                                      | The application needs `Runtime.All` to call any connector from Power Platform.                                   |
| **APIs my organization uses** | PowerApps Service                                         | The application needs the `User` permission to contact Power Apps backend services from Power Platform.                                     |
| **APIs my organization uses** | Power BI                                                 | The application needs Power BI permissions to access or embed Power BI content.                                          |
| **APIs my organization uses** | Microsoft Mobile Application Management        | The application needs this permission because Power Apps uses Intune SDK internally. |


For detailed steps, see [Request the permissions in the app registration portal](/azure/active-directory/develop/v2-permissions-and-consent#request-the-permissions-in-the-app-registration-portal).

Run these PowerShell commands as an Azure admin if you don't see permissions under **APIs my organization uses**:

1. Ensure the module [Microsoft Graph](https://www.powershellgallery.com/packages/Microsoft.Graph/) is available or install it:
   ```powershell
   Install-Module -Name Microsoft.Graph
   ```

2. Grant *Azure API Connections* permission for the static AppId fe053c5f-3692-4f14-aef2-ee34fc081cae:
   ```powershell
   Connect-MgGraph -TenantId <your tenant ID>
   New-MgServicePrincipal -AppId fe053c5f-3692-4f14-aef2-ee34fc081cae -DisplayName "Azure API Connections"
   ```

3. Grant *PowerApps Service* permission for the static AppId 475226c6-020e-4fb2-8a90-7a972cbfc1d4:
   ```powershell
   Connect-MgGraph -TenantId <your tenant ID>
   New-MgServicePrincipal -AppId 475226c6-020e-4fb2-8a90-7a972cbfc1d4 -DisplayName "PowerApps Service"
   ```

> [!NOTE]
> If only the **Application name** field is visible, continue to the next steps and select **Android** as a target platform to display the signature hash field.

## Configure API permissions manually (optional)

If you get errors, manually configure API permissions. For more information, see [Add and configure](/azure/active-directory/develop/v2-permissions-and-consent#request-the-permissions-in-the-app-registration-portal).


#### Add Redirect URIs as an app admin

1. In the Azure Portal, go to your app registration > **Authentication**.
2. Select **Add a platform** and choose **iOS** or **Android**.
3. For iOS, enter the **Bundle ID**.
   For Android, enter both the **Bundle ID** and **Signature hash key**.
   :::image type="content" source="media/how-to-v2/redirect-uri.png" alt-text="Screenshot that shows redirect URIs for the app." lightbox="media/how-to-v2/redirect-uri.png":::

### 5. Configure branding

1. On the **Configure Branding** step, set the following options for your app:

> [!NOTE]
> All images must be in .png format. Default images will be used if no custom images are selected.

| Setting | Description | Requirements |
|---------|-------------|--------------|
| **App icons** | Icons for your app | iOS: 1024x1024 px or larger<br>Android: 432x432 px or larger |
| **Splash screen image** | Image shown while the app loads | .png format |
| **Welcome screen image** | Image shown on the sign-in screen | .png format |
| **Background fill color** | Color for welcome screen background | Hexadecimal color code |
| **Button fill color** | Color for buttons | Hexadecimal color code |
| **Status bar text theme** | Color for the status bar text | Light or Dark |

2. Select **Next**.

### 6. Manage output

1. Enter your Azure blob storage account name and container name.
2. After the build completes, download your APK or IPA from the Azure blob storage location.

:::image type="content" source="media/how-to-v2/manage-output.png" alt-text="Screenshot that shows the fifth step on how to manage the output using Azure blob storage." lightbox="media/how-to-v2/manage-output.png":::

### 7. Wrap up and build

1. On the **Wrap up** screen, review your app details and select **Build**.
2. After a successful build, your app package will be available in the Azure blob storage you specified.

### View your build

You can view your build in several ways:

- After building, select **View Builds**
- Go to **Wrap projects** in the side pane, hover over the required project, and select it
- Select the **View builds** option in the top header

:::image type="content" source="media/how-to-v2/view-build.png" alt-text="Screenshot that shows how to view builds." lightbox="media/how-to-v2/view-build.png":::

> [!NOTE]
> To manually code sign an iOS app, unzip the IPA file using a Mac device.

## Test and distribute your app

Test your app and distribute it as needed. If you encounter issues, see the [troubleshooting page](/troubleshoot/power-platform/power-apps/manage-apps/wrap-issues).


## Register your app on Azure portal manually (optional)

You can create your app registration automatically in the wizard or manually in Azure. More information: [Quickstart: Register an application with the Microsoft identity platform](/azure/active-directory/develop/quickstart-register-app).

> [!NOTE]
> Both single tenant and multitenant customers can use wrap to create native mobile apps based on their Power Apps canvas apps.

When registering, select an account type containing **Any Microsoft Entra directory - Multitenant**:
- Accounts in any organizational directory (Any Microsoft Entra directory - Multitenant)
- Accounts in any organizational directory (Any Microsoft Entra directory - Multitenant) and personal Microsoft accounts such as Skype or Xbox

:::image type="content" source="media/wrap-intro/AppResgistration_AccountTypes.png" alt-text="App registration - supported account types for wrap.":::

> [!IMPORTANT]
> - Wrap only supports **Multitenant** account types currently. The single tenant account type is not yet supported. More information: [Account types in Microsoft identity platform](/azure/active-directory/develop/v2-supported-account-types).
> - You must create a separate **Redirect URI** for each platform (iOS, Android).

## Sign your mobile app package manually (optional)

You can sign your app automatically in **Step 2** or manually after building. [Code signing](overview.md#code-signing) is different for Android and iOS.

**Advantages of automatic signing for iOS and Android (APK):**

- You don't need to repeat the signing process during rewrapping.
- You don't have to wait for app developers to finish the process.
- You don't need to set up Android Studio or remember passwords.
- You don't need a Mac device for iOS signing.

| Platform | Signing Method |
|----------|---------------|
| iOS                  | [Manual code sign for iOS](code-sign-ios.md) |
| Android              | [Manual code sign for Android](code-sign-android.md) |
| Google Play Store    | [Code signing for Google Play Store](https://developer.android.com/studio/publish/app-signing) |

## See also

- [Troubleshoot issues with the wrap feature in Power Apps](/troubleshoot/power-platform/power-apps/manage-apps/wrap-issues)
- [Wrap overview](overview.md)
- [Manual code sign for iOS](code-sign-ios.md)
- [Manual code sign for Android](code-sign-android.md)
- [Create your Azure Key Vault for automated code signing](create-key-vault-for-code-signing.md)
- [Frequently asked questions for wrap](faq.yml)
