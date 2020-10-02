---
title: "Configure SAML 2.0 provider settings for a portal | MicrosoftDocs"
description: "Instructions to add and configure SAML 2.0 provider settings for a portal."
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/18/2019
ms.author: sandhan
ms.reviewer: tapanm
---

# SAML 2.0 settings for [!INCLUDE[pn-azure-active-directory](../../../includes/pn-azure-active-directory.md)]

The previous section describing [!include[](../../../includes/pn-adfs-short.md)] can also be applied to [[!INCLUDE[pn-azure-shortest](../../../includes/pn-azure-shortest.md)] AD](https://docs.microsoft.com/azure/active-directory/), because [!INCLUDE[pn-azure-shortest](../../../includes/pn-azure-shortest.md)] AD behaves like a standard [SAML 2.0](https://docs.microsoft.com/azure/active-directory/develop/single-sign-on-saml-protocol)&ndash;compliant IdP. To get started, sign in to the [[!INCLUDE[pn-azure-shortest](../../../includes/pn-azure-shortest.md)] Management Portal](https://msdn.microsoft.com/library/azure/hh967611.aspx#bkmk_azureportal) and create or select an existing directory. When a directory is available, follow the instructions to [add an application](https://docs.microsoft.com/azure/active-directory/develop/quickstart-register-app) to the directory.  

> [!NOTE]
> Portals can be configured with identity providers that conform to the SAML 2.0 standards. In this article, you'll learn about using Azure Active Directory as an example of identity providers using SAML 2.0.

1.  Under the**Applications** menu of the directory, select **Add**.
2.  Choose **Add an application my organization is developing**.
3.  Specify a custom name for the application, and then choose the type **web application and/or web API**.
4.  For the **Sign-On URL** and the**App ID URI**, specify the URL of the portal for both fields https://portal.contoso.com/.
    This corresponds to the **ServiceProviderRealm** (Wtrealm) site setting value.
5. At this point, a new application is created. Go to the **Configure** section in the menu.

    Under the **single sign-on** section, update the first **Reply URL** entry to include a path in the URL https://portal.contoso.com/signin-azure-ad.

    This corresponds to the **AssertionConsumerServiceUrl** (Wreply) site setting value.

6. In the footer menu, select **View Endpoints** and note the **Federation Metadata Document** field.

This corresponds to the **MetadataAddress** site setting value.

-   Paste this URL in a browser window to view the federation metadata XML, and note the **entityID** attribute of the root element.
-   This corresponds to the**AuthenticationType** site setting value.

> [!Note]
> A standard [!INCLUDE[pn-azure-shortest](../../../includes/pn-azure-shortest.md)] AD configuration only uses the following settings (with example values):
> Authentication/SAML2/[!INCLUDE[pn-azure-shortest](../../../includes/pn-azure-shortest.md)]AD/MetadataAddress - <https://login.microsoftonline.com/01234567-89ab-cdef-0123-456789abcdef/federationmetadata/2007-06/federationmetadata.xml> 
> - Authentication/SAML2/[!INCLUDE[pn-azure-shortest](../../../includes/pn-azure-shortest.md)]AD/AuthenticationType - <https://sts.windows.net/01234567-89ab-cdef-0123-456789abcdef/>  
> - Use the value of the**entityID** attribute in the root element of the federation metadata (open the**MetadataAddress URL** in a browser that is the value of the above site setting) 
> - Authentication/SAML2/[!INCLUDE[pn-azure-shortest](../../../includes/pn-azure-shortest.md)]AD/ServiceProviderRealm - <https://portal.contoso.com/>  
> - Authentication/SAML2/[!INCLUDE[pn-azure-shortest](../../../includes/pn-azure-shortest.md)]AD/AssertionConsumerServiceUrl - <https://portal.contoso.com/signin-azure-ad>                                                                                   |
