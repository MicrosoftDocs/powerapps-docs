---
title: "Configure the Azure Active Directory B2C identity provider for Power Apps portals. | MicrosoftDocs"
description: "Learn how to configure the Azure Active Directory B2C identity provider for Power Apps portals."
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/12/2020
ms.author: sandhan
ms.reviewer: tapanm
---

# Configure the Azure Active Directory B2C provider

[!include[Azure](../../../includes/pn-azure-shortest.md)] Active Directory (Azure AD) powers Office 365 and Dynamics 365 services for employee or internal authentication. [!include[Azure](../../../includes/pn-azure-shortest.md)] Active Directory B2C is an extension to that authentication model that enables external customer signs in through local credentials and federation with various common social identity providers.

A portal owner can configure the portal to accept [!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C as an identity provider. [!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C supports Open ID Connect for federation.

To configure OpenID Connect provider with Azure AD B2C:

1. Select **Configure** for **Azure Active Directory B2C**. More information: [Configure a provider](use-simplified-authentication-configuration.md#add-or-configure-a-provider)

    ![Azure AD B2C provider name](media/authentication/azure-ad-b2c-name.png "Azure AD B2C provider name")

1. If necessary, update the name.

1. Select **Next**.

1. In this step, create the application and configure the settings with your identity provider.

    ![Configure the Azure AD B2C app](media/use-simplified-authentication-configuration/configure-ad-b2c-step1.png "Configure the Azure AD B2C app")

    1. [Create and configure an Azure AD B2C tenant](#create-and-configure-an-azure-ad-b2c-tenant).

    1. [Register an application](https://docs.microsoft.com/azure/active-directory-b2c/tutorial-register-applications?tabs=applications#register-a-web-application) in your tenant. Use the **Reply URL** provided in the wizard while configuring the application.

        > [!NOTE]
        > You must choose **Yes** for the **Allow implicit flow** field and enter your portal URL in the **Reply URL** field.

    1. [Create a sign-up and sign-in user flow](https://docs.microsoft.com/azure/active-directory-b2c/tutorial-create-user-flows#create-a-sign-up-and-sign-in-user-flow). Optionally, [create a password reset user flow](https://docs.microsoft.com/azure/active-directory-b2c/tutorial-create-user-flows#create-a-password-reset-user-flow).

    1. [Configure token compatibility](https://docs.microsoft.com/azure/active-directory-b2c/configure-tokens#configure-token-compatibility) with an **Issuer (iss) claim** URL that includes **tfp**. More information: [Token compatibility](https://docs.microsoft.com/azure/active-directory-b2c/tokens-overview#compatibility)

        ![Configure token compatibility with tfp](media/authentication/token-compatibility.png "Configure token compatibility with tfp") 

1. In this step, enter the site settings and password reset settings for the portal configuration.

    ![Configure site settings](media/use-simplified-authentication-configuration/configure-ad-b2c-step2.png "Configure site settings")

    1. **Configure site settings**

        - **Authority** - The issuer URL defined in the metadata of the sign-up and sign-in policy user flow.​
        <br> To get the issuer URL:

           1. Open the sign-up and sign-in user flow you created earlier. For this step, you need to go to the Azure AD B2C tenant on [Azure portal](https://portal.azure.com).

            ![Select the user flow](media/use-simplified-authentication-configuration/user-flow.png "Select the user flow")

           2. Select **Run user flow**.

            ![Run user flow](media/use-simplified-authentication-configuration/run-user-flow.png "Run user flow")

           3. Select the OpenID configuration URL to open in a new browser window or a tab.

                ![Select the OpenID configuration URL](media/use-simplified-authentication-configuration/select-openid-configuration-url.png "Select the OpenID configuration URL")
        
                The URL refers to the *OpenID Connect identity provider configuration document*, also known as the *OpenID well-known configuration endpoint*.

           4. Copy the URL of the **Issuer** from the new browser window or tab.

                ![Copy the Issuer URL](media/use-simplified-authentication-configuration/issuer-url.png "Copy the Issuer URL")

                Ensure you copy only the URL, without the double quotation marks (*""*). <br> For example, `https://tailspintoysorg.b2clogin.com/799f7b50-f7b9-49ec-ba78-67eb67210998/v2.0/`

        - **Client ID​** - Enter the **Application ID** of the Azure AD B2C application created earlier.

        - **Redirect URI** - Enter the portal URL. <br> You only need to change the redirect URI if you use a custom domain name.

    2. **Password reset settings**

        - **Default policy ID** - Enter the name of the sign-up and sign-in user flow you created in earlier. The name is prefixed with *B2C_1*.

        - **Password reset policy ID** - Enter the name of the password reset user flow you created earlier. The name is prefixed with *B2C_1*.

        - **Valid issuers** - A comma-delimited list of issuer URLs for the sign-up and sign-in user flow and password reset user flow you created earlier. 
        <br> To get the issuer URLs for the sign-up and sign-in user flow, and password reset user flow, open each flow and then follow the steps under **Authority**, earlier in this section.

1. In this step, you'll configure the additional site settings.

    You have the option of configuring additional setting for the Azure AD B2C identity provider.

    ![Configure additional settings](media/use-simplified-authentication-configuration/configure-ad-b2c-step3.png "Configure additional settings")

     - **Registration claims mapping​** - List of logical name/claim pairs to be used to map claim values returned from Azure AD B2C created during sign up to attributes in the contact record. <br> 
     For example, if you've enabled **Job Title (jobTitle)** and **Postal Code (postalCode)** as **User Attributes** in your user flow and you want to update the corresponding Contact entity fields **Job Title (jobtitle)** and **Address 1: ZIP / Postal Code (address1_postalcode)**, enter the claims mapping as: ```jobtitle=jobTitle,address1_postalcode=postalCode```.
     - **Login claims mapping** - List of logical name/claim pairs to be used to map claim values returned from Azure AD B2C after sign-in to the attributes in the contact record. <br> 
     For example, if you've enabled **Job Title (jobTitle)** and **Postal Code (postalCode)** as **Application Claims** in your user flow and you want to update the corresponding Contact entity fields **Job Title (jobtitle)** and **Address 1: ZIP / Postal Code (address1_postalcode)**, enter the claims mapping as: ```jobtitle=jobTitle,address1_postalcode=postalCode```.
     - **External logout** - Enables or disables federated sign-out. When set to **On**, users are redirected to the federated sign-out user experience when they sign out from the portal. When set to **Off**, users are only signed out from the portal.
     - **Contact mapping with email** - Specifies whether contacts are mapped to a corresponding email. When set to **On**, this setting associates a unique contact record with a matching email address, and then automatically assigns the external identity provider to the contact after the user successfully signs in.
     - **Registration Enabled**​ - Turn [open registration](configure-portal-authentication.md#open-registration) for your portal on or off. Setting this toggle to **Off** disables and hides external account registration.

1. Select **Confirm** to view a summary of your configuration and complete the identity configuration.

### Create and configure an Azure AD B2C tenant

> [!NOTE]
> For more details about creating and configuring Azure AD B2C tenant on Azure portal, go to [Create an Azure AD B2C tenant](https://docs.microsoft.com/azure/active-directory-b2c/tutorial-create-tenant).

To create Azure AD B2C tenant:

1. Sign in to your [Azure portal](https://portal.azure.com/).
1. [Create an Azure AD B2C tenant](https://docs.microsoft.com/azure/active-directory-b2c/active-directory-b2c-get-started).
1. Select **[!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C** on the leftmost navigation bar.
1. [Create Azure application](https://docs.microsoft.com/azure/active-directory-b2c/active-directory-b2c-app-registration#register-a-web-application).

   > [!Note]
   > You must choose **Yes** for the **Allow implicit flow** field and specify your portal URL in the **Reply URL** field. The value in the **Reply URL** field should be in the format [portal domain]/signin-[Federation-Name]. For example, `https://contosocommunity.microsoftcrmportals.com/signin-B2C`.

1. Copy the application name, and enter it as the value of Application-Name in the preceding table.
1. Copy the application (client) ID, and enter it as the value of Application-ID in the preceding table.
1. [Create a sign-up or sign-in policy](https://docs.microsoft.com/azure/active-directory-b2c/active-directory-b2c-reference-policies#create-a-sign-up-or-sign-in-policy).
1. Navigate to **Azure AD B2C** resource.
1. Select **User flows** under Policies.
1. Choose the newly created Sign up and sign in policy.
1. From **Settings** list, select **Properties**
1. Under **Token compatibility settings**, from the **Issuer (iss) claim** list, select the URL that has **/tfp** in its path.
1. Save the policy.
1. Select the URL in the **Metadata endpoint for this policy** field.
1. Copy the value of the issuer field and enter it as the value of Issuer-URL in the preceding table.

### See also

[Migrate identity providers to Azure AD B2C](migrate-identity-providers.md)
