---
title: Key vault for code signing
description:  Learn how to configure Azure Key Vault for automated code signing of native mobile apps in wrap wizard.
author: komala2019
ms.topic: how-to
ms.custom: canvas
ms.reviewer: smurkute
ms.date: 5/9/2024
ms.subservice: canvas-maker
ms.author: koagarwa
search.audienceType: 
  - maker
contributors:
  - mduelae
---

# Azure key vault for wrap using default subscription

Azure Key Vault is a cloud-based service for securely storing secrets, such as certificates, passwords, keys, and other sensitive information. To learn more, see [Introduction to Azure Key Vault](/azure/key-vault/general/overview). Setting up Azure Key Vault is required for creating Azure blob storage and for the automatic signing process in wrap.

This article explains how to use an existing Azure Key Vault or create a new one in the [Azure portal](https://portal.azure.com).

## Prerequisites

- Microsoft Entra subscription to [create key vault](/azure/key-vault/general/quick-create-portal).
- Your subscription ID must be the default one. More information: [Get subscription information](/cli/azure/manage-azure-subscriptions-azure-cli?tabs=bash#get-subscription-information)
- Admin access for your tenant.
- An [Apple account](https://developer.apple.com) enrolled in the Apple Developer Program or Apple Enterprise Developer Program.
- Create a [distribution certificate](code-sign-ios.md#create-the-distribution-certificate) or [ad-hoc Provisioning Profile](code-sign-ios.md#create-an-ios-provisioning-profile) or enterprise provisioning profile.

## Configure key vault URI

> [!IMPORTANT]
> Before configuring the Key Vault URI, you need to create an Azure Key Vault. Follow the steps in [Create a vault](/azure/key-vault/general/quick-create-portal#create-a-vault).

1. **Create a service principal for Wrap KeyVault Access App**

   Sign in to your tenant as an admin and run the following PowerShell commands:

   ```
   Connect-AzureAD -TenantId <your tenant ID>
   New-AzureADServicePrincipal -AppId 4e1f8dc5-5a42-45ce-a096-700fa485ba20 -DisplayName "Wrap KeyVault Access App"
   ```

2. **Assign Reader role to the service principal**

   Add a **Reader** role assignment to the Wrap Key Vault Access App in the **Access Control (IAM)** of your default subscription and the Key Vault.

   1. In the Azure portal, select **Access control (IAM)** and then **Add** > **Add role assignment**.
   2. Go to the **Members** tab, select **Job function roles**, and ensure **Reader** is selected.

      > [!div class="mx-imgBorder"] 
      > ![Select the Members tab.](media/how-to-v2/Add_members.png "Select the Members tab.")

   3. On the **Members** tab, select **Select member** and search for **Wrap Key Vault Access App**.

      > [!div class="mx-imgBorder"] 
      > ![Search for Wrap Key Vault Access App.](media/how-to-v2/Add_role_assignment.png "Search for Wrap Key Vault Access App.")

   4. Select **Wrap Key Vault Access App** and then **Review + assign** to assign the Reader role.

      > [!div class="mx-imgBorder"] 
      > ![Assign Reader role to Wrap KeyVault Access App.](media/how-to-v2/Add_role_for_wrap_signing.png "Assign Reader role to Wrap KeyVault Access App.")

3. **Create or access an existing Key Vault**

   Ensure the Key Vault is in your tenant's default subscription. More information: [Create a key vault using the Azure portal](/azure/key-vault/general/quick-create-portal).

4. **Add access policies for the Key Vault**

   For **Secret permissions** and **Certificate permissions**, select **Get** and **List**.

   > [!div class="mx-imgBorder"] 
   > ![Access Policies required: Get, List for secret and certificates permissions.](media/how-to-v2/AzureKV-Access-Policy.png "Access Policies required: Get, List for secret and certificates permissions")

5. **Upload certificates and secrets**

   Choose your platform and follow the steps below:

   - **Android**

     Generate the .pfx file and upload it to the certificate section of the Key Vault. More information: [Generate keys](code-sign-android.md#generate-keys)

     :::image type="content" source="media/wrap-canvas-app/wrap-1.png" alt-text="Create a cert for Android.":::

     > [!NOTE]
     > Ensure the certificate name is included in the tag step and the password matches the store pass parameter used when creating the .pfx file.

   - **iOS**

     1. Install the .cer file using Keychain Access. See [Create the distribution certificate](code-sign-ios.md#create-the-distribution-certificate).
     2. Export the certificate as a .p12 file, then rename the extension to **.pfx** (required by Key Vault).
     3. When uploading to Key Vault, provide the password set for the .p12 file.
     4. [Create the provisioning profile](code-sign-ios.md#create-an-ios-provisioning-profile) and encode it to base64:
        - Mac: `base64 -i example.mobileprovision`
        - Windows: `certutil -encode data.txt tmp.b64`
     5. Upload the base64 string as a Key Vault secret, then upload the .pfx file as a Key Vault certificate.

     :::image type="content" source="media/wrap-canvas-app/wrap-2.png" alt-text="Create a cert for iOS.":::

6. **Add tags for certificates**

   After uploading iOS or Android certificates, add three tags with the name as the bundle ID and the value as the uploaded certificate name(s). Use the same bundle ID as in the [wrap wizard](wrap-how-to.md#step-2-target-platform).

   :::image type="content" source="media/wrap-canvas-app/wrap-3.png" alt-text="Add tags.":::

A video for configuring key vault is available at [How to configure access to key vault](https://www.youtube.com/watch?v=QV5xAUoJDcA&t=7s)

## Troubleshoot

For troubleshooting, see [Troubleshoot issues with the wrap feature in Power Apps](/troubleshoot/power-platform/power-apps/manage-apps-and-solutions/wrap-issues).

### See also

- [Wrap overview](overview.md)
- [Code sign for iOS](code-sign-ios.md)
- [Code sign for Android](code-sign-android.md)
- [Code sign for Google Play Store](https://developer.android.com/studio/publish/app-signing)
- [Frequently asked questions for wrap](faq.yml)  
- [Troubleshoot issues with the wrap feature in Power Apps](/troubleshoot/power-platform/power-apps/manage-apps/wrap-issues)
