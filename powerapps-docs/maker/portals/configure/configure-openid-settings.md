---
title: "Configure the OpenID Connect provider for portals with Azure Active Directory.  | MicrosoftDocs"
description: "Instructions to configure the OpenID Connect provider for portals with Azure Active Directory."
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/12/2020
ms.author: sandhan
ms.reviewer: tapanm
---

# Configure OpenID Connect for portals with Azure Active Directory

In this article, you'll learn about configuring OpenID Connect provider for portals with Azure Active Directory, and multi-tenant Azure AD.

> [!NOTE]
> Portals isn't limited to only Azure AD, multi-tenant Azure AD, or Azure AD B2C as the OpenID Connect providers. You can use any other provider that confirms to the OpenID Connect specifications with portals.

To configure OpenID Connect provider with Azure AD:

1. Select [Add provider](use-simplified-authentication-configuration.md#add-configure-or-delete-an-identity-provider) for your portal.

1. Select **Login provider** as **Other**.

1. Select **Protocol** as **OpenID Connect**.

1. Enter a provider name.

    ![Provider name](media/authentication/select-other-openid.png "Provider name")

1. Select **Next**.

1. In this step, create the application and configure the settings with your identity provider.

    ![Create application](media/authentication/step-1-openid.png "Create application")

    > [!NOTE]
    > - The Reply URL is used by the app to redirect users to the portal after the authentication succeeds. If your portal uses a custom domain name, you might have a different URL than the one provided here.
    > - More details about creating the app registration on the Azure portal are available in the [Quickstart: Register an application with the Microsoft identity platform](https://docs.microsoft.com/azure/active-directory/develop/quickstart-register-app).

    1. Sign in to the [Azure portal](https://portal.azure.com).

    1. Search for and select **Azure Active Directory**.

    1. Under **Manage**, select **App registrations**.

    1. Select **New registration**.

        ![New app registration](media/authentication/app-registration-new.png "New app registration")

    1. Enter a name.

    1. If necessary, select a different **Supported account type**. More information: [Supported account types](https://docs.microsoft.com/azure/active-directory/develop/quickstart-register-app)

    1. If not already, select **Web** for **Redirect URI**.

    1. Enter the **Reply URL** for your portal in the **Redirect URI** text box. <br> Example: `https://contoso-portal.powerappsportals.com/signin-openid_1`

        > [!NOTE]
        > If you're using the default portal URL, copy and paste the **Reply URL** as shown in **Create and configure OpenID Connect provider settings**. If you're using custom domain name for the portal, enter the custom URL. However, ensure you use this value when you configure the **Redirect URL** in your portal settings while configuring OpenID Connect provider. <br> For example, if you enter the **Reply URL** in Azure portal as `https://contoso-portal.powerappsportals.com/signin-openid_1`, use it as is for the OpenID Connect configuration in portals. In this example, using `https://contoso-portal.powerappsportals.com/signin-openid` or `https://portal.contoso.com/signin-openid_1` in portals site settings will be incorrect.

        ![Register application](media/authentication/register-application.png "Register application")

    1. Select **Register**.

    1. Keep the Azure portal open, and switch to the OpenID Connect configuration for Power Apps portals for the next steps.

1. In this step, enter the site settings for the portal configuration.

    ![Configure OpenID Connect site settings](media/authentication/openid-site-settings-1.png "Configure OpenID Connect site settings")

    > [!TIP]
    > If you closed the browser window after configuring the app registration in the earlier step, sign in to the Azure portal again and go to the app that you registered for the next steps.

    1. **Authority** - To configure the authority URL, use the following format:

        `https://login.microsoftonline.com/<Directory (tenant) ID>/`

        For example, if the *Directory (tenant) ID* in the Azure portal is `22a47203-270e-4476-a9fd-189d82e4b467`, the authority URL is `https://login.microsoftonline.com/22a47203-270e-4476-a9fd-189d82e4b467/`

    1. **Client ID** - Copy the **Application (client) ID** from the Azure portal as the client ID.

        ![Authority and Client ID](media/authentication/authority-client-id.png "Authority and Client ID")

    1. **Redirect URL** - Confirm that the **Redirect URL** site setting value is the same as the **Redirect URI** that you set in the Azure portal earlier.

        ![Confirm Redirect URL](media/authentication/redirect-uri-azure-power-apps.png "Confirm Redirect URL")

        > [!NOTE]
        > If you're using the default portal URL, you can copy and paste the **Reply URL** as shown in **Create and configure OpenID Connect provider settings**. If you're using a custom domain name, enter the URL manually. However, ensure that the value entered here is exactly the same as the value you entered as the **Redirect URI** in the Azure portal earlier.

    1. **Metadata address** - To configure the metadata address:

        1. Select **Overview** in the Azure portal.
        
        1. Select **Endpoints**.
        
            ![Endpoints in Azure portal](media/authentication/endpoints.png "Endpoints in Azure portal")

        1. Copy the **OpenID Connect metadata document**.

            ![OpenID Connect metadata document](media/authentication/openid-connect-metadata-document.png "OpenID Connect metadata document")

        1. Paste the copied document URL as the **Metadata address** for portals.

    1. **Scope** - Set the **Scope** site setting value as:

        `openid email`

        > [!NOTE]
        > `openid` value in **Scope** is mandatory. `email` value is optional, and specifying it in the scope ensures that the email address of the portal user (contact record) is pre-filled, and shown on the *Profile* page after the user logs in.

        > [!TIP]
        > For additional claims, see [Configure additional claims](#configure-additional-claims).

    1. **Response type** - Select **code id_token**.

    1. **Response mode** - Select **form_post**.

1. Select **Confirm**.

    ![Confirm the configuration](media/authentication/confirm-config.png "Confirm the configuration")

1. Select **Close**.

### Configure additional claims

To configure additional claims, such as using first name, or last name:

1. Enable [optional claims in Azure AD](https://docs.microsoft.com/azure/active-directory/develop/active-directory-optional-claims#configuring-directory-extension-optional-claims).

1. Set **Scope** to include the additional claims.
    <br> Example: `openid email profile`

1. Set the **Registration claims mapping** additional site setting.
    <br> Example: `firstname=given_name,lastname=family_name`

1. Set the **Login claims mapping** additional site setting.
    <br> Example: `firstname=given_name,lastname=family_name`

## Enable authentication using a multi-tenant Azure Active Directory application

You can configure your portal to accept [!include[](../../../includes/pn-azure-active-directory.md)] users from any tenant in [!include[](../../../includes/pn-azure-shortest.md)] and not just a specific tenant by using the multi-tenant application registered in [!include[](../../../includes/pn-azure-active-directory.md)]. To enable multi-tenancy, [update the application registration](https://docs.microsoft.com/azure/active-directory/develop/howto-convert-app-to-be-multi-tenant#update-registration-to-be-multi-tenant) in the [!include[](../../../includes/pn-azure-active-directory.md)] application.

To support authentication against [!include[](../../../includes/pn-azure-active-directory.md)] using a multi-tenanted application, you have to create or configure the additional **Issue Filter** site setting in portals.

`Authentication/OpenIdConnect/[provider]/IssuerFilter`

This site setting is a wildcard-based filter that matches on all issuers across all tenants. Example: `https://sts.windows.net/*/`

### See also

- [Frequently Asked Questions (FAQs) when using OpenID Connect in portals](configure-openid-faqs.md)
