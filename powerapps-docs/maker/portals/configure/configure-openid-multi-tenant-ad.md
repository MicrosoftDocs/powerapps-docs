---
title: "Configure OpenID Connect provider settings for a portal  | MicrosoftDocs"
description: "Instructions to add and configure OpenID Connect provider settings for a portal."
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/18/2019
ms.author: sandhan
ms.reviewer: tapanm
---

# Enable authentication using a multi-tenant Azure Active Directory application

You can configure your portal to accept [!include[](../../../includes/pn-azure-active-directory.md)] users from any tenant in [!include[](../../../includes/pn-azure-shortest.md)] and not just a specific tenant by using the multi-tenant application registered in [!include[](../../../includes/pn-azure-active-directory.md)]. To enable multi-tenancy, set the **Multi-tenanted** switch to **Yes** in the [!include[](../../../includes/pn-azure-active-directory.md)] application.

![Enable multi tenancy in Azure Active Directory application](../media/enable-multi-tenancy.png "Enable multi tenancy in Azure Active Directory application")

### Related site settings

Multiple identity providers can be configured by substituting a label for the [provider] tag. Each unique label forms a group of settings related to an identity provider. You can create or configure the following site settings in portals to support authentication against [!include[](../../../includes/pn-azure-active-directory.md)] using a multi-tenanted application:

|Site Setting Name    |Description   |
|---|---|
|Authentication/OpenIdConnect/[provider]/Authority   |The Authority to use when making OpenIdConnect calls. For example: `https://login.microsoftonline.com/common`   |
|Authentication/OpenIdConnect/[provider]/ClientId   |The client ID value from the provider application. It may also be referred to as an App ID or Consumer Key.   |
|Authentication/OpenIdConnect/[provider]/ExternalLogoutEnabled   |Enables or disables external account sign-out and registration. Set this value as True.   |
|Authentication/OpenIdConnect/[provider]/IssuerFilter   |A wildcard-based filter that matches on all issuers across all tenants. In most cases, use the value: `https://sts.windows.net/*/`   |
|Authentication/OpenIdConnect/[provider]/RedirectUri  |The reply URL location where the provider sends the authentication response.For example: `https://portal.contoso.com/signin-oidc` |
|Authentication/OpenIdConnect/[provider]/ValidateIssuer   |A Boolean to control if the issuer will be validated during token validation. Set this value as False.   |
|||

