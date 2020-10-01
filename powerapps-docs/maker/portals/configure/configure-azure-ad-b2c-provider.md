---
title: "Use simplified authentication and identity provider configuration (Preview) | MicrosoftDocs"
description: "Learn how to use quick, easy, and simplified portal configuration for authentication."
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 07/29/2020
ms.author: sandhan
ms.reviewer: tapanm
---

# Configure the Azure Active Directory B2C provider

[!include[Azure](../../../includes/pn-azure-shortest.md)] Active Directory (Azure AD) powers Office 365 and Dynamics 365 services for employee or internal authentication. [!include[Azure](../../../includes/pn-azure-shortest.md)] Active Directory B2C is an extension to that authentication model that enables external customer sign-ins through local credentials and federation with various common social identity providers.

A portal owner can configure the portal to accept [!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C as an identity provider. [!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C supports Open ID Connect for federation.

### Step 1 - Configure the Azure Active Directory B2C application

![Configure the Azure AD B2C app](media/use-simplified-authentication-configuration/configure-ad-b2c-step1.png "Configure the Azure AD B2C app")

To use Azure AD B2C as an identity provider:

1. [Create and configure an Azure AD B2C tenant](https://docs.microsoft.com/azure/active-directory-b2c/tutorial-create-tenant).

1. [Register an application](https://docs.microsoft.com/azure/active-directory-b2c/tutorial-register-applications?tabs=applications#register-a-web-application) in your tenant. Use the **Reply URL** provided in the wizard while configuring the application.

    > [!NOTE]
    > You must choose **Yes** for the **Allow implicit flow** field and enter your portal URL in the **Reply URL** field.

1. [Create a user flow](https://docs.microsoft.com/azure/active-directory-b2c/tutorial-create-user-flows#create-a-sign-up-and-sign-in-user-flow). Optionally, [create a password reset user flow](https://docs.microsoft.com/azure/active-directory-b2c/tutorial-create-user-flows#create-a-password-reset-user-flow).

1. [Configure token compatibility](https://docs.microsoft.com/azure/active-directory-b2c/configure-tokens#configure-token-compatibility) with an **Issuer (iss) claim** URL that includes **tfp**. More information: [Token compatibility](https://docs.microsoft.com/azure/active-directory-b2c/tokens-overview#compatibility)

### Step 2 - Configure site settings

Configure the following site settings and password reset policy for your Azure AD B2C provider.

![Configure site settings](media/use-simplified-authentication-configuration/configure-ad-b2c-step2.png "Configure site settings")

- **Authority** - The issuer URL defined in the metadata of the sign-up and sign-in policy user flow.​
<br> To get the issuer URL:

   1. Open the sign-up and sign-in user flow you created in [step 1](#step-1---configure-the-azure-active-directory-b2c-application). For this step, you need to go to the Azure AD B2C tenant on [Azure portal](https://portal.azure.com).

        ![Select the user flow](media/use-simplified-authentication-configuration/user-flow.png "Select the user flow")

   1. Select **Run user flow**.

        ![Run user flow](media/use-simplified-authentication-configuration/run-user-flow.png "Run user flow")

   1. Select the OpenID configuration URL to open in a new browser window or a tab.

        ![Select the OpenID configuration URL](media/use-simplified-authentication-configuration/select-openid-configuration-url.png "Select the OpenID configuration URL")
        
        The URL refers to the *OpenID Connect identity provider configuration document*, also known as the *OpenID well-known configuration endpoint*.

   1. Copy the URL of the **Issuer** from the new browser window or tab.

        ![Copy the Issuer URL](media/use-simplified-authentication-configuration/issuer-url.png "Copy the Issuer URL")

        Ensure you copy only the URL, without the double quotation marks (*""*). <br> For example, `https://tailspintoysorg.b2clogin.com/acf18993-4325-4d94-b519-96824b0d06db/v2.0/`

- **Client ID​** - Enter the **Application ID** of the Azure AD B2C application created in [step 1](#step-1---configure-the-azure-active-directory-b2c-application).

- **Redirect URI** - Enter the portal URL. <br> You only need to change the redirect URI if you use a custom domain name.

#### Password reset settings

- **Default policy ID** - Enter the name of the sign-up and sign-in user flow you created in [step 1](#step-1---configure-the-azure-active-directory-b2c-application). The name is prefixed with *B2C_1*.

- **Password reset policy ID** - Enter the name of the password reset user flow you created in [step 1](#step-1---configure-the-azure-active-directory-b2c-application). The name is prefixed with *B2C_1*.

- **Valid issuers** - A comma-delimited list of issuer URLs for the sign-up and sign-in user flow and password reset user flow you created in [step 1](#step-1---configure-the-azure-active-directory-b2c-application). 
<br> To get the issuer URLs for the sign-up and sign-in user flow, and password reset user flow, open each flow and then follow the steps under **Authority**, earlier in this section.

For more information about site settings, see [related site settings](azure-ad-b2c.md#related-site-settings).

### Step 3 - Configure additional settings

You have the option of configuring additional setting for the Azure AD B2C identity provider.

![Configure additional settings](media/use-simplified-authentication-configuration/configure-ad-b2c-step3.png "Configure additional settings")

- **Registration claims mapping​** - List of logical name/claim pairs to be used to map claim values returned from Azure AD B2C created during sign up to attributes in the contact record. <br> 
For example, if you've enabled **Job Title (jobTitle)** and **Postal Code (postalCode)** as **User Attributes** in your user flow and you want to update the corresponding Contact entity fields **Job Title (jobtitle)** and **Address 1: ZIP / Postal Code (address1_postalcode)**, enter the claims mapping as: ```jobtitle=jobTitle,address1_postalcode=postalCode```.
- **Login claims mapping** - List of logical name/claim pairs to be used to map claim values returned from Azure AD B2C after sign in to the attributes in the contact record. <br> 
For example, if you've enabled **Job Title (jobTitle)** and **Postal Code (postalCode)** as **Application Claims** in your user flow and you want to update the corresponding Contact entity fields **Job Title (jobtitle)** and **Address 1: ZIP / Postal Code (address1_postalcode)**, enter the claims mapping as: ```jobtitle=jobTitle,address1_postalcode=postalCode```.
- **External logout** - Enables or disables federated sign-out. When set to **On**, users are redirected to the federated sign-out user experience when they sign out from the portal. When set to **Off**, users are only signed out from the portal.
- **Contact mapping with email** - Specifies whether contacts are mapped to a corresponding email. When set to **On**, this setting associates a unique contact record with a matching email address, and then automatically assigns the external identity provider to the contact after the user successfully signs in.
- **Registration Enabled**​ - Turn [open registration](configure-portal-authentication.md#open-registration) for your portal on or off. Setting this toggle to **Off** disables and hides external account registration.

Select **Confirm** to view a summary of your configuration and complete the identity configuration.

For more information about claims mapping, see [Azure AD B2C claims mapping scenarios](azure-ad-b2c.md#claims-mapping).

For more information about configuring Azure AD B2C identity provider, see [Azure AD B2C provider settings for portals](azure-ad-b2c.md#customize-the--ad-b2c-user-interface).

### See also

- [Set authentication identity for a portal](set-authentication-identity.md)
- [Configure Azure AD B2C provider settings](azure-ad-b2c.md)
- [Configure OAuth2 provider settings](configure-oauth2-settings.md)
- [Microsoft Learn: Authentication and user management in Power Apps portals](https://docs.microsoft.com/learn/modules/authentication-user-management/)
