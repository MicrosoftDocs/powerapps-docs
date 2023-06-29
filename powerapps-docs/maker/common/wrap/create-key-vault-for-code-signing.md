---
title: Create key vault for code signing
description:  Learn how to create Azure key valut for automated code signing of native mobile apps in wrap wizard.
author: makolomi
ms.topic: article
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 29/06/2023
ms.subservice: canvas-maker
ms.author: mkaur
search.audienceType: 
  - maker
contributors:
  - mkaur-msft
---
# Create Azure key valut for wrap for Power Apps
You need to have [Azure Key Vault](/azure/key-vault/general/basic-concepts) set up to automatically sign your Android or iOS mobile app package in **Step 2** of wrap wizard. Azure key vault is a cloud service that provides a secure store for secrets. You can securely store keys, passwords, certificates, and other secrets. More information: [Intoduction to Azure key vault](https://learn.microsoft.com/en-us/azure/key-vault/general/overview).

You can use an exsiting Azure key vault or create a new one one using the isnructions below.

//on Azure portal at [https://portal.azure.com](https://portal.azure.com).
  
**Prerequisites**
  
- Azure Active Directory subscription to [create Key Vault](/azure/key-vault/general/quick-create-portal).
- Admin access for your tenant.
- You need to have a [Apple account](https://developer.apple.com) enrolled in Apple developer Program or Apple enterprise developer program.
- Create a [distribution certificate](code-sign-ios.md#create-the-distribution-certificate) or [ad-hoc Provisioning Profile](code-sign-ios.md#create-an-ios-provisioning-profile) or enterprise provisioning profile.
   
Follow these steps to create **Azure key vault** for wrap for Power Apps and configure **KeyVault URI**:
  
1. Sign in to your tenent as an admin and create a new Azure service principal for 1P AAD application: **4e1f8dc5-5a42-45ce-a096-700fa485ba20 (WrapKeyVaultAccessApp)** by running the following script: <br>
`Connect-AzureAD -TenantId <your tenant ID>` in Power Shell <br>
`New-AzureADServicePrincipal -AppId 4e1f8dc5-5a42-45ce-a096-700fa485ba20 -DisplayName "Wrap KeyVault Access App"`
  
2. In your default subscription's **Access Control (IAM)**, add a **Reader** role assignment to the **Service Principal** representing your app, e.g. **Wrap KeyVault Access App**. Make sure it is present in the **Subscription's IAM**, and the **Keyvault's IAM**.

   Go to **Access control (IAM)** tab and select **Add role assignment** option under **Add** menu button.

   > [!div class="mx-imgBorder"] 
   > ![Add role assignment on Access control tab.](media/how-to-v2/Access_control_tab.png "Add role assignment on Access control tab.")

  Select **Job fucntion roles** tab and make sure **Reader** role is selcetdd. Then click on **Members** tab in the top menu.
   
    > [!div class="mx-imgBorder"] 
   > ![Click on Members tab.](media/how-to-v2/Add_members.png "Click on Members tab.")

   Search for **Wrap KeyVault Access App** on **Members** tab.
   
   > [!div class="mx-imgBorder"] 
   > ![Search for Wrap KeyVault Access App.](media/how-to-v2/Add_role_assignment.png "Search for Wrap KeyVault Access App.")

   Select **Wrap KeyVault Access App** and click on **Review + assign** button on the bottom of the tab to assign **Reader** role to it.
  
   > [!div class="mx-imgBorder"] 
   > ![Assign Reader role to Wrap KeyVault Access App.](media/how-to-v2/Add_role_for_wrap_signing.png "Assign Reader role to Wrap KeyVault Access App.")
  
4. Create or access existing key vault. Please ensure this key vault is located in the default subscription for your tenant. More information: [Create a key vault using the Azure portal](/azure/key-vault/general/quick-create-portal).
   
5. Add access policies for the key vault.
  
   :::image type="content" source="media/wrap-canvas-app/wrap-keyvault.gif" alt-text="Add access policies for the key vault.":::
  
6. Follow one of the these options, depending on your device:
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

7. Once iOS or Android certificates are created and uploaded, add three tags with the name as the bundle id, and the value corresponding to the name of the uploaded certificate(s).
  
     :::image type="content" source="media/wrap-canvas-app/wrap-3.png" alt-text="Add tags.":::
  
# Troubleshoot Azure key valut for wrap for Power Apps
The following Azure key vault errors might appear in wrap for Power Apps and can be rectified.


| Error code      | Description          | Cool  |
| ------------- |:-------------:| -----:|
| ##1000118    | Default subscription not found, or missing access permissions| $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |
