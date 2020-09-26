---
title: "Azure AD B2C provider settings for portals | MicrosoftDocs"
description: "Instructions to enable Azure AD B2C provider settings for portals."
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 09/02/2020
ms.author: sandhan
ms.reviewer: tapanm
---

# Azure AD B2C provider settings for portals

[!include[Azure](../../../includes/pn-azure-shortest.md)] Active Directory (Azure AD) powers Office 365 and Dynamics 365 services for employee or internal authentication. [!include[Azure](../../../includes/pn-azure-shortest.md)] Active Directory B2C is an extension to that authentication model that enables external customer sign-ins through local credentials and federation with various common social identity providers.

A portal owner can configure the portal to accept [!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C as an identity provider. [!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C supports Open ID Connect for federation.

In the process of configuring [!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C as an identity provider for your portal, multiple values are generated that you will use later while you configure the portal. You can note these values in the following table. While configuring the portal, replace the variable name with the values you note here.

| Variable Name     | Value | Description                                                           |
|-------------------|-------|-----------------------------------------------------------------------|
| Application-Name  |       | Name of the application that represents the portal as a relying party |
| Application-ID    |       | The Application ID associated with the application created in Azure Active Directory B2C.  |
| Issuer-URL |       | The Issuer (iss) URL defined in the metadata endpoint.                |
| Federation-Name   |       | A unique name to identify the type of federation provider such as 'B2C'. This will be used in Site Setting names to group configuration settings for this specific provider.                                                                      |
| | | |

### Use Azure AD B2C as an identity provider for your portal

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
1. Under **Token compatability settings**, from the **Issuer (iss) claim** list, select the URL that has **/tfp** in its path.
1. Save the policy.
1. Select the URL in the **Metadata endpoint for this policy** field.
1. Copy the value of the issuer field and enter it as the value of Issuer-URL in the preceding table. 

## Portal configuration

After creating and configuring the B2C tenant in [!include[Azure](../../../includes/pn-azure-shortest.md)], you must configure your portal to federate with [!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C by using the Open ID Connect protocol. You must create a unique name for your federation to [!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C&mdash;for example, B2C&mdash;and store it as the value of the *Federation-Name* variable in the above table.

### Configure your portal
1. Open the Portal Management app.
2. Go to **Portals** > **Websites**.
3. Select the website record for which [!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C needs to be enabled.
4. Go to **Site Settings**.
5. Create the following site settings:
   -   **Name**: Authentication/OpenIdConnect/[Federation-Name]/Authority

       **Value**: [Issuer-URL]
   -   **Name**: Authentication/OpenIdConnect/[Federation-Name]/ClientId

       **Value**: [Application-ID]
   -   **Name**: Authentication/OpenIdConnect/[Federation-Name]/RedirectUri

       **Value**: [portal domain]/signin-[Federation-Name]

       For example, `https://mysite.com/signin-b2c` 
6. To support a federated sign-out, create the following site setting:
   - **Name**: Authentication/OpenIdConnect/[Federation-Name]/ExternalLogoutEnabled

     **Value**: true
7. To hardcode your portal to a single identity provider, create the following site setting:
   - **Name**: Authentication/Registration/LoginButtonAuthenticationType

     **Value**: [Issuer-URL]

8. To support password reset, create the required site settings described [here](#password-reset).
9. To support claims mapping, create the required site settings described [here](#claims-mapping).

For a complete list of related site settings, see [here](#related-site-settings).

### Related content snippet

If registration is disabled for a user after the user has redeemed an invitation, display a message by using the following content snippet:

**Name**: Account/Register/RegistrationDisabledMessage

**Value**: Registration has been disabled.