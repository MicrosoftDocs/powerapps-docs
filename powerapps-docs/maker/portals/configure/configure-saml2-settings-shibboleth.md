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

# Shibboleth Identity Provider 3

Use the following guidelines for correctly configuring [Shibboleth Identity Provider](https://wiki.shibboleth.net/confluence/display/IDP30/Home) as an IdP service. The following assumes the IdP is hosted on the domain https://idp.contoso.com.  

The federation metadata URL is https://idp.contoso.com/idp/shibboleth

-   The IdP must be configured to generate or serve a persistent identifier. Follow the instructions to enable [Persistent Identifier Generation](https://wiki.shibboleth.net/confluence/display/IDP30/NameIDGenerationConfiguration).  

-   The IdP federation metadata (&lt;IDPSSODescriptor&gt;) must be configured to include an [SSO redirect binding](https://shibboleth.net/about/advanced.html). [Example](https://wiki.shibboleth.net/confluence/display/SHIB2/MetadataExample).  

```
<SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect"

Location=https://idp.contoso.com/idp/profile/SAML2/Redirect/SSO/>
```

Configure the service providers (relying parties) by setting up the [metadata-providers.xml](https://wiki.shibboleth.net/confluence/display/IDP30/MetadataConfiguration).  

-   Each service provider federation metadata (&lt;SPSSODescriptor&gt;) must include an assertion consumer service post binding. One option is to use a [FilesystemMetadataProvider](https://wiki.shibboleth.net/confluence/display/IDP30/FilesystemMetadataProvider) and reference a configuration file that contains:  

```
<AssertionConsumerService index=1 isDefault=true

Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST"

Location=https://portal.contoso.com/signin-saml2/>
```

The Location attribute corresponds to the**AssertionConsumerServiceUrl** (Wreply) setting.

-   The service provider federation metadata should specify an **entityID** attribute for the EntityDescriptor that corresponds to the **AuthenticationType** setting.

**&lt;EntityDescriptor entityID=<https://portal.local.contoso.com/&gt>;...**

> [!Note] 
> A standard Shibboleth configuration only uses the following settings (with example values):   
> Authentication/SAML2/Shibboleth/MetadataAddress - https://idp.contoso.com/idp/shibboleth   
> -   Authentication/SAML2/Shibboleth/AuthenticationType - https://idp.contoso.com/idp/shibboleth 
> -   Use the value of the **entityID** attribute in the root element of the federation metadata (open the **MetadataAddress URL** in a browser that is the value of the above site setting)  
> -   Authentication/SAML2/Shibboleth/ServiceProviderRealm - https://portal.contoso.com/ 
> -   Authentication/SAML2/Shibboleth/AssertionConsumerServiceUrl - https://portal.contoso.com/signin-saml2 

### IdP-initiated sign-in

Shibboleth supports the [IdP initiated SSO](https://wiki.shibboleth.net/confluence/display/SHIB2/IdPUnsolicitedSSO) profile of the SAML 2.0 [specification](https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0-cd-02.html#5.1.4.IdP-Initiated%20SSO:%20POST%20Binding|outline). For the portal (service provider) to respond properly to the SAML request initiated by the IdP, the RelayState parameter must be encoded properly.  

The basic string value to be encoded into the SAML RelayState parameter must be in the format **ReturnUrl=/content/sub-content/**, where **/content/sub-content/** is the path to the webpage you want to go to on the portal (service provider). The path can be replaced by any valid webpage on the portal. The full IdP-initiated SSO URL should be in the format <https://idp.contoso.com/idp/profile/SAML2/Unsolicited/SSO?providerId=&lt;URL> encoded provider ID&gt;&target=&lt;URL encoded return path&gt;.

For example, given the service provider path **/content/sub-content/** and the relying party ID **https://portal.contoso.com/**, the final URL is https://idp.contoso.com/idp/profile/SAML2/Unsolicited/SSO?providerId=https%3A%2F%2Fportal.contoso.com%2F&target=ReturnUrl%3D%2Fcontent%2Fsub-content%2F

The following [!INCLUDE[pn-powershell-short](../../../includes/pn-powershell-short.md)] script can be used to construct the URL (save to a file named Get-ShibbolethIdPInitiatedUrl.ps1).

```
<# 

.SYNOPSIS

Constructs an IdP initiated SSO URL to access a portal page on the service provider.

.PARAMETER path

The path to the portal page.

.PARAMETER providerId

The relying party identifier.

.PARAMETER shibbolethPath

The Shibboleth IdP-initiated SSO page.

.EXAMPLE

PS C:\\> .\\Get-ShibbolethIdPInitiatedUrl.ps1 -path "/content/sub-content/" -providerId "https://portal.contoso.com/" -shibbolethPath "https://idp.contoso.com/idp/profile/SAML2/Unsolicited/SSO"

#>

param

(

[parameter(mandatory=$true,position=0)]

$path,

[parameter(mandatory=$true,position=1)]

$providerId,

[parameter(position=2)]

$shibbolethPath = https://idp.contoso.com/idp/profile/SAML2/Unsolicited/SSO

)

$state = ReturnUrl=$path

$encodedPath = [uri]::EscapeDataString($state)

$encodedRpid = [uri]::EscapeDataString($providerId)

$idpInitiatedUrl = {0}?providerId={1}&target={2} -f $shibbolethPath, $encodedRpid, $encodedPath

Write-Output $idpInitiatedUrl
```
