---
title: "Configure SAML 2.0 for portals with Azure Active Directory. | MicrosoftDocs"
description: "Learn how to configure SAML 2.0 for portals with Azure Active Directory."
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/18/2019
ms.author: sandhan
ms.reviewer: tapanm
---

# Configure SAML 2.0 for portals with Azure Active Directory

In this article, you'll learn about configuring SAML 2.0 provider for portals with Azure Active Directory.

> [!NOTE]
> Portals can be configured with identity providers that conform to the SAML 2.0 standards. In this article, you'll learn about using Azure Active Directory as an example of identity providers using SAML 2.0.

To configure SAML 2.0 provider with Azure AD:

1. Select [Add provider](use-simplified-authentication-configuration.md#add-configure-or-delete-an-identity-provider) for your portal.

1. Select **Login provider** as **Other**.

1. Select **Protocol** as **SAML 2.0**.

1. Enter a provider name.

    ![Add SAML 2.0 provider](media/authentication/add-saml2-provider.png "Add SAML 2.0 provider")

1. Select **Next**.

1. In this step, create the application and configure the settings with your identity provider.

    ![Create SAML 2.0 application](media/authentication/create-configure-saml-application.png "Create SAML 2.0 application")

    > [!NOTE]
    > - The Reply URL is used by the app to redirect users to the portal after the authentication succeeds. If your portal uses a custom domain name, you might have a different URL than the one provided here.
    > - More details about creating the app registration on the Azure portal are available in the [Quickstart: Register an application with the Microsoft identity platform](https://docs.microsoft.com/azure/active-directory/develop/quickstart-register-app).

    1. Sign in to the [Azure portal](https://portal.azure.com).

    1. Search for and select **Azure Active Directory**.

    1. Under **Manage**, select **App registrations**.

    1. Select **New registration**.

        ![New app registration](media/authentication/app-registration-new.png "New app registration")

    1. Enter a name.

    1. If required, select a different **Supported account type**. More information: [Supported account types](https://docs.microsoft.com/azure/active-directory/develop/quickstart-register-app)

    1. If not already, select **Web** for **Redirect URI**.

    1. If required, select a different **Supported account type**. More information: [Supported account types](https://docs.microsoft.com/azure/active-directory/develop/quickstart-register-app)

    1. If not already, select **Web** for **Redirect URI**.

    1. Enter the **Reply URL** for your portal in the **Redirect URI** text box. <br> Example: `https://contoso-portal.powerappsportals.com/signin-saml_1`

        > [!NOTE]
        > If you're using the default portal URL, copy and paste the **Reply URL** as shown in **Create and configure SAML 2.0 provider settings**. If you're using a custom domain name, enter the URL manually. However, ensure that the value entered here for your application is exactly the same as the value available for the **Redirect URL** in your portal settings while configuring SAML 2.0 provider. <br> For example, if the **Reply URL** in portals is `https://contoso-portal.powerappsportals.com/signin-saml_1`, use it as is for the Azure portal. Using `https://contoso-portal.powerappsportals.com/signin-saml` in this case is incorrect.

        ![Register application](media/authentication/register-application-saml2.png "Register application")

    1. Select **Register**.

    1. Select **Expose an API**.

    1. Select **Set** for **Application ID URI**.

        ![Application ID URI](media/authentication/saml2-applicationid-uri.png "Application ID URI")

    1. Enter the portal URL as the **App ID URI**.

        ![Portal URL as the Application ID URI](media/authentication/portal-url-for-appidURI.png "Portal URL as the Application ID URI")

        > [!NOTE]
        > The portal URL may be different if you're using a custom domain name.

    1. Select **Save**.

        ![Saved Application ID URI](media/authentication/saved-appiduri-saml.png "Saved Application ID URI")

    1. Keep the Azure portal open, and switch to the SAML 2.0 configuration for Power Apps portals for the next steps.

1. In this step, enter the site settings for the portal configuration.

    ![Configure SAML 2.0 site settings](media/authentication/configure-saml2-site-settings.png "Configure SAML 2.0 site settings")

    > [!TIP]
    > If you closed the browser window after configuring the app registration in the earlier step, sign in to the Azure portal again and go to the app that you registered for the next steps.

    1. **Metadata address** - To configure the metadata address:

        1. Select **Overview** in the Azure portal.
        
        1. Select **Endpoints**.
        
            ![Endpoints](media/authentication/endpoints-saml2.png "Endpoints")

        1. Copy the **Federation metadata document**.

            ![Federation metadata document](media/authentication/federation-metadata-saml.png "Federation metadata document")

        1. Paste the copied document URL as the **Metadata address** for portals.

    1. **Autentication type** - To configure the authentication type:

        1. Copy and paste the **Metadata address** configured earlier in a new browser window.

        1. Copy the value of `entityID` tag from the URL document.

            ![Federation metadata entityID](media/authentication/entity-id-metadata-document.png "Federation metadata entityID")

        1. Paste the copied value of `entityID` as the **Authentication type**. <br> Example: `https://sts.windows.net/22a47203-270e-4476-a9fd-189d82e4b467/`

    1. **Service provider realm** - Enter the portal URL as the service provider realm. <br> Example: `https://contoso-portal.powerappsportals.com`
    
        > [!NOTE]
        > The portal URL may be different if you're using a custom domain name.
        
    1. **Assertion consumer service URL** - Enter the **Reply URL** for your portal in the **Assertion consumer service URL** text box. <br> Example: `https://contoso-portal.powerappsportals.com/signin-saml_1`

        ![Assertion consumer service URL](media/authentication/redirect-uri-azure-power-apps-saml.png "Assertion consumer service URL")

        > [!NOTE]
        > If you're using the default portal URL, copy and paste the **Reply URL** as shown in **Create and configure SAML 2.0 provider settings**. If you're using a custom domain name, enter the URL manually. However, ensure that the value entered here is exactly the same as the value you entered as the **Redirect URI** in the Azure portal earlier.

1. Select **Confirm**.

    ![Confirm configuration](media/authentication/confirm-saml-config.png "Confirm configuration")

1. Select **Close**.
