---
title: "Configure SAML 2.0 provider settings for a portal | MicrosoftDocs"
description: "Instructions to add and configure SAML 2.0 provider settings for a portal."
author: sbmjais
manager: shujoshi
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/18/2019
ms.author: shjais
ms.reviewer:
---

# Configure SAML 2.0 provider settings for portals

To provide external authentication, you can add one or more [SAML 2.0](http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0-cd-02.html)–compliant identity providers (IdP). This document describes how to set up various identity providers to integrate with a portal that acts as a service provider.  

## AD FS (IdP)

Settings for an identity provider such as [!include[](../includes/pn-active-dir-fed-svcs-ad-fs.md)].

### Create an AD FS relying party trust

> [!Note]
> See [Configure AD FS by using PowerShell](#configure-ad-fs-by-using-powershell), below, for information about how to perform these steps in a [!INCLUDE[pn-powershell-short](../includes/pn-powershell-short.md)] script.

Using the [!include[](../includes/pn-adfs-short.md)] Management tool, go to **Service** > **Claim Descriptions**.

1.  Select **Add Claim Description**.
2.  Specify the claim:

    -  Display name: **Persistent Identifier**

    -  Claim identifier: **urn:oasis:names:tc:SAML:2.0:nameid-format:persistent**

    -  **Enable** check box for: Publish this claim description in federation metadata as a claim type that this federation service can accept

    -  **Enable** check box for: Publish this claim description in federation metadata as a claim type that this federation service can send

3.  Select **OK**.

Using the [!include[](../includes/pn-adfs-short.md)] Management tool, select **Trust Relationships** >**Relying Party Trusts**.

1. Select **Add Relying Party Trust**.
2. Welcome: Select **Start**.
3. Select Data Source: Select **Enter data about the relying party manually**, and then select **Next**.
4. Specify Display Name: Enter a name, and then select **Next**.
   Example: https://portal.contoso.com/
5. Choose Profile: Select **AD FS 2.0 profile**, and then select **Next**.
6. Configure Certificate: Select **Next**.
7. Configure URL: Select the **Enable support for the SAML 2.0 WebSSO protocol** check box.
   Relying party SAML 2.0 SSO service URL: Enter https://portal.contoso.com/signin-saml2
   - Note: [!include[](../includes/pn-adfs-short.md)] requires that the portal run on HTTPS.

   > [!Note] 
   > The resulting endpoint has the following settings: 
   > - Endpoint type: **SAML Assertion Consume Endpoints**             
   > - Binding: **POST**                                            
   > - Index: n/a (0)                                              
   > - URL: **https://portal.contoso.com/signin-saml2**

8. Configure Identities: Specify https://portal.contoso.com/, select **Add**, and then select **Next**.
   If applicable, you can add more identities for each additional relying party portal. Users will be able to authenticate across any or all of the available identities.
9. Choose Issuance Authorization Rules: Select **Permit all users to access this relying party**, and then select **Next**.
10. Ready to Add Trust: Select **Next**.
11. Select **Close**.

Add the **Name ID** claim to the relying party trust:

**Transform[!INCLUDE[pn-ms-windows-short](../includes/pn-ms-windows-short.md)] account name** to **Name ID** claim (Transform an Incoming Claim):

- Incoming claim type: **[!INCLUDE[pn-ms-windows-short](../includes/pn-ms-windows-short.md)] account name**

- Outgoing claim type: **Name ID**

- Outgoing name ID format: **Persistent Identifier**

- Pass through all claim values

### Create site settings

Apply portal site settings referencing the above [!include[](../includes/pn-adfs-short.md)] relying party trust.

> [!Note]
> A standard [!include[](../includes/pn-adfs-short.md)] (IdP) configuration only uses the following settings (with example values):
> Authentication/SAML2/ADFS/MetadataAddress - <https://adfs.contoso.com/FederationMetadata/2007-06/FederationMetadata.xml>  
> - Authentication/SAML2/ADFS/AuthenticationType - http://adfs.contoso.com/adfs/services/trust    
>   -   Use the value of the **entityID** attribute in the root element of the federation metadata (open the **MetadataAddress URL** in a browser that is the value of the above site setting) 
> - Authentication/SAML2/ADFS/ServiceProviderRealm - https://portal.contoso.com/  
> - Authentication/SAML2/ADFS/AssertionConsumerServiceUrl - https://portal.contoso.com/signin-saml2  
>   The **federation metadata** can be retrieved in **[!INCLUDE[pn-powershell-short](../includes/pn-powershell-short.md)]** by running the following script on the [!include[](../includes/pn-adfs-short.md)] server:
>   `Import-Module adfs`
>   `Get-ADFSEndpoint -AddressPath /FederationMetadata/2007-06/FederationMetadata.xml`

Multiple IdP services can be configured by substituting a label for the [provider] tag. Each unique label forms a group of settings related to an IdP. Examples: ADFS, [!INCLUDE[pn-azure-shortest](../includes/pn-azure-shortest.md)]AD, MyIdP


| Site Setting Name                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                             |
|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Authentication/Registration/ExternalLoginEnabled              | Enables or disables external account sign-in and registration. Default: true                                                                                                                                                                                                                                                                                                                                                            |
| Authentication/SAML2/[provider]/MetadataAddress             | Required. The [WS-Federation](https://msdn.microsoft.com/library/bb498017.aspx) metadata URL of the [!include[](../includes/pn-adfs-short.md)] (STS) server. It commonly ends with the path:/FederationMetadata/2007-06/FederationMetadata.xml . Example: `https://adfs.contoso.com/FederationMetadata/2007-06/FederationMetadata.xml`. [!include[](../includes/proc-more-information.md)] [WsFederationAuthenticationOptions.MetadataAddress](https://msdn.microsoft.com/library/microsoft.owin.security.wsfederation.wsfederationauthenticationoptions.metadataaddress.aspx) |  
| Authentication/SAML2/[provider]/AuthenticationType          | Required. The OWIN authentication middleware type. Specify the value of the [entityID](https://docs.microsoft.com/azure/active-directory/develop/active-directory-federation-metadata) attribute at the root of the federation metadata XML. Example: `http://adfs.contoso.com/adfs/services/trust`. [!include[](../includes/proc-more-information.md)] [AuthenticationOptions.AuthenticationType](https://msdn.microsoft.com/library/microsoft.owin.security.authenticationoptions.authenticationtype.aspx)                                                            |  
| Authentication/SAML2/[provider]/ServiceProviderRealm<br>or <br>Authentication/SAML2/[provider]/Wtrealm                      | Required. The [!include[](../includes/pn-adfs-short.md)] relying party identifier. Example: `https://portal.contoso.com/`. [!include[](../includes/proc-more-information.md)] [WsFederationAuthenticationOptions.Wtrealm](https://msdn.microsoft.com/library/microsoft.owin.security.wsfederation.wsfederationauthenticationoptions.wtrealm.aspx)                       |  
| Authentication/SAML2/[provider]/AssertionConsumerServiceUrl<br>or<br>Authentication/SAML2/[provider]/Wreply                       | Required. The [!include[](../includes/pn-adfs-short.md)] SAML Consumer Assertion endpoint. Example: https://portal.contoso.com/signin-saml2. [!include[](../includes/proc-more-information.md)] [WsFederationAuthenticationOptions.Wreply](https://msdn.microsoft.com/library/microsoft.owin.security.wsfederation.wsfederationauthenticationoptions.wreply.aspx)                                                                                                                                                                                                  |  
| Authentication/SAML2/[provider]/Caption                     | Recommended. The text that the user can display on a sign-in user interface. Default: [provider]. [!include[](../includes/proc-more-information.md)] [WsFederationAuthenticationOptions.Caption](https://msdn.microsoft.com/library/microsoft.owin.security.wsfederation.wsfederationauthenticationoptions.caption.aspx)                |  
| Authentication/SAML2/[provider]/CallbackPath                | An optional constrained path on which to process the authentication callback. [!include[](../includes/proc-more-information.md)] [WsFederationAuthenticationOptions.CallbackPath](https://msdn.microsoft.com/library/microsoft.owin.security.wsfederation.wsfederationauthenticationoptions.callbackpath.aspx)                                                                                                                                                                                                                      |  
| Authentication/SAML2/[provider]/BackchannelTimeout          | Timeout value for back-channel communications. Example: 00:05:00 (5 mins). [!include[](../includes/proc-more-information.md)] [WsFederationAuthenticationOptions.BackchannelTimeout](https://msdn.microsoft.com/library/microsoft.owin.security.wsfederation.wsfederationauthenticationoptions.backchanneltimeout.aspx)                                                                                                                                                                                                                   |  
| Authentication/SAML2/[provider]/UseTokenLifetime            | Indicates that the authentication session lifetime (for example, cookies) should match that of the authentication token. [WsFederationAuthenticationOptions.UseTokenLifetime](https://msdn.microsoft.com/library/microsoft.owin.security.wsfederation.wsfederationauthenticationoptions.usetokenlifetime.aspx).                                                                                                                                                                               |  
| Authentication/SAML2/[provider]/AuthenticationMode          | The OWIN authentication middleware mode. [!include[](../includes/proc-more-information.md)] [AuthenticationOptions.AuthenticationMode](https://msdn.microsoft.com/library/microsoft.owin.security.authenticationoptions.authenticationmode.aspx)                                                                                                                                                                                                                                                                              |  
| Authentication/SAML2/[provider]/SignInAsAuthenticationType  | The AuthenticationType used when creating the System.Security.Claims.ClaimsIdentity. [!include[](../includes/proc-more-information.md)] [WsFederationAuthenticationOptions.SignInAsAuthenticationType](https://msdn.microsoft.com/library/microsoft.owin.security.wsfederation.wsfederationauthenticationoptions.signinasauthenticationtype.aspx)                                                                                                                                                                                                 |  
| Authentication/SAML2/[provider]/ValidAudiences              | Comma-separated list of audience URLs. [!include[](../includes/proc-more-information.md)] [TokenValidationParameters.AllowedAudiences](https://msdn.microsoft.com/library/system.identitymodel.tokens.tokenvalidationparameters.allowedaudiences.aspx)                                                                                                                                                                                                                                                                          |  
| Authentication/SAML2/[provider]/ClockSkew                   | The clock skew to apply when validating times.                                                                                                                                                                                                                                                                                                                                                                                          |
| Authentication/SAML2/[provider]/RequireExpirationTime       | A value indicating whether tokens must have an expiration value.                                                                                                                                                                                                                                                                                                                                                                      |
| Authentication/SAML2/[provider]/ValidateAudience            | A Boolean to control whether the audience will be validated during token validation.                                                                                                                                                                                                                                                                                                                                                         |

### IdP-initiated sign-in

[!include[](../includes/pn-adfs-short.md)] supports the [IdP-initiated single sign-on (SSO)](https://technet.microsoft.com/library/jj127245.aspx) profile of the SAML 2.0 [specification](http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0-cd-02.html#5.1.4.IdP-Initiated%20SSO:%20POST%20Binding|outline). In order for the portal (service provider) to respond properly to the SAML request initiated by the IdP, the [RelayState](http://blogs.technet.com/b/askds/archive/2012/09/27/ad-fs-2-0-relaystate.aspx) parameter must be encoded properly.  

The basic string value to be encoded into the SAML RelayState parameter must be in the format **ReturnUrl=/content/sub-content/**, where **/content/sub-content/** is the path to the webpage you want to go to on the portal (service provider). The path can be replaced by any valid webpage on the portal. The string value is encoded and placed into a container string of the format **RPID=&lt;URL encoded RPID&gt;&RelayState=&lt;URL encoded RelayState&gt;**. This entire string is once again encoded and added to another container of the format **<https://adfs.contoso.com/adfs/ls/idpinitiatedsignon.aspx?RelayState=&lt;URL> encoded RPID/RelayState&gt;**.

For example, given the service provider path **/content/sub-content/** and the relying party ID **https://portal.contoso.com/**, construct the URL with the steps:

Encode the value ReturnUrl=/content/sub-content/

-   to get ReturnUrl%3D%2Fcontent%2Fsub-content%2F

<!-- -->

-   Encode the value https://portal.contoso.com/

<!-- -->

-   to get https%3A%2F%2Fportal.contoso.com%2F

<!-- -->

-   Encode the value RPID=https%3A%2F%2Fportal.contoso.com%2F&RelayState=ReturnUrl%3D%2Fcontent%2Fsub-content%2F

<!-- -->

-   to get RPID%3Dhttps%253A%252F%252Fportal.contoso.com%252F%26RelayState%3DReturnUrl%253D%252Fcontent%252Fsub-content%252F

<!-- -->

-   Prepend the AD FS IdP-initiated SSO path to get the final URL

<!-- -->

-   https://adfs.contoso.com/adfs/ls/idpinitiatedsignon.aspx?RelayState=RPID%3Dhttps%253A%252F%252Fportal.contoso.com%252F%26RelayState%3DReturnUrl%253D%252Fcontent%252Fsub-content%252F

The following [!INCLUDE[pn-powershell-short](../includes/pn-powershell-short.md)] script can be used to construct the URL (save to a file named Get-IdPInitiatedUrl.ps1).

```
<#

.SYNOPSIS 

Constructs an IdP-initiated SSO URL to access a portal page on the service provider.

.PARAMETER path

The path to the portal page.

.PARAMETER rpid

The relying party identifier.

.PARAMETER adfsPath

The AD FS IdP initiated SSO page.

.EXAMPLE

PS C:\\> .\\Get-IdPInitiatedUrl.ps1 -path "/content/sub-content/" -rpid "https://portal.contoso.com/" -adfsPath "https://adfs.contoso.com/adfs/ls/idpinitiatedsignon.aspx"

#>

param

(

[parameter(mandatory=$true,position=0)]

$path,

[parameter(mandatory=$true,position=1)]

$rpid,

[parameter(position=2)]

$adfsPath = https://adfs.contoso.com/adfs/ls/idpinitiatedsignon.aspx

)

$state = ReturnUrl=$path

$encodedPath = [uri]::EscapeDataString($state)

$encodedRpid = [uri]::EscapeDataString($rpid)

$encodedPathRpid = [uri]::EscapeDataString("RPID=$encodedRpid&RelayState=$encodedPath")

$idpInitiatedUrl = {0}?RelayState={1} -f $adfsPath, $encodedPathRpid

Write-Output $idpInitiatedUrl
```

## SAML 2.0 settings for [!INCLUDE[pn-azure-active-directory](../includes/pn-azure-active-directory.md)]

The previous section describing [!include[](../includes/pn-adfs-short.md)] can also be applied to [[!INCLUDE[pn-azure-shortest](../includes/pn-azure-shortest.md)] AD](https://msdn.microsoft.com/library/azure/mt168838.aspx), because [!INCLUDE[pn-azure-shortest](../includes/pn-azure-shortest.md)] AD behaves like a standard [SAML 2.0](https://msdn.microsoft.com/library/azure/dn195591.aspx)&ndash;compliant IdP. To get started, sign in to the [[!INCLUDE[pn-azure-shortest](../includes/pn-azure-shortest.md)] Management Portal](https://msdn.microsoft.com/library/azure/hh967611.aspx#bkmk_azureportal) and create or select an existing directory. When a directory is available, follow the instructions to [add an application](https://msdn.microsoft.com/library/azure/dn132599.aspx) to the directory.  

1.  Under the**Applications** menu of the directory, select **Add**.
2.  Choose **Add an application my organization is developing**.
3.  Specify a custom name for the application, and then choose the type **web application and/or web API**.
4.  For the **Sign-On URL** and the**App ID URI**, specify the URL of the portal for both fields https://portal.contoso.com/.
    This corresponds to the **ServiceProviderRealm** (Wtrealm) site setting value.
5. At this point, a new application is created. Go to the **Configure** section in the menu.

    Under the **single sign-on** section, update the first **Reply URL** entry to include a path in the URL http://portal.contoso.com/signin-azure-ad.

    This corresponds to the **AssertionConsumerServiceUrl** (Wreply) site setting value.

6. In the footer menu, select **View Endpoints** and note the **Federation Metadata Document** field.

This corresponds to the **MetadataAddress** site setting value.

-   Paste this URL in a browser window to view the federation metadata XML, and note the **entityID** attribute of the root element.
-   This corresponds to the**AuthenticationType** site setting value.

> [!Note]
> A standard [!INCLUDE[pn-azure-shortest](../includes/pn-azure-shortest.md)] AD configuration only uses the following settings (with example values):
> Authentication/SAML2/[!INCLUDE[pn-azure-shortest](../includes/pn-azure-shortest.md)]AD/MetadataAddress - <https://login.microsoftonline.com/01234567-89ab-cdef-0123-456789abcdef/federationmetadata/2007-06/federationmetadata.xml> 
> - Authentication/SAML2/[!INCLUDE[pn-azure-shortest](../includes/pn-azure-shortest.md)]AD/AuthenticationType - <https://sts.windows.net/01234567-89ab-cdef-0123-456789abcdef/>  
> - Use the value of the**entityID** attribute in the root element of the federation metadata (open the**MetadataAddress URL** in a browser that is the value of the above site setting) 
> - Authentication/SAML2/[!INCLUDE[pn-azure-shortest](../includes/pn-azure-shortest.md)]AD/ServiceProviderRealm - <https://portal.contoso.com/>  
> - Authentication/SAML2/[!INCLUDE[pn-azure-shortest](../includes/pn-azure-shortest.md)]AD/AssertionConsumerServiceUrl - <https://portal.contoso.com/signin-azure-ad>                                                                                   |

## Shibboleth Identity Provider 3

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

Shibboleth supports the [IdP initiated SSO](https://wiki.shibboleth.net/confluence/display/SHIB2/IdPUnsolicitedSSO) profile of the SAML 2.0 [specification](http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0-cd-02.html#5.1.4.IdP-Initiated%20SSO:%20POST%20Binding|outline). For the portal (service provider) to respond properly to the SAML request initiated by the IdP, the RelayState parameter must be encoded properly.  

The basic string value to be encoded into the SAML RelayState parameter must be in the format **ReturnUrl=/content/sub-content/**, where **/content/sub-content/** is the path to the webpage you want to go to on the portal (service provider). The path can be replaced by any valid webpage on the portal. The full IdP-initiated SSO URL should be in the format <https://idp.contoso.com/idp/profile/SAML2/Unsolicited/SSO?providerId=&lt;URL> encoded provider ID&gt;&target=&lt;URL encoded return path&gt;.

For example, given the service provider path **/content/sub-content/** and the relying party ID **https://portal.contoso.com/**, the final URL is https://idp.contoso.com/idp/profile/SAML2/Unsolicited/SSO?providerId=https%3A%2F%2Fportal.contoso.com%2F&target=ReturnUrl%3D%2Fcontent%2Fsub-content%2F

The following [!INCLUDE[pn-powershell-short](../includes/pn-powershell-short.md)] script can be used to construct the URL (save to a file named Get-ShibbolethIdPInitiatedUrl.ps1).

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

## Configure AD FS by using PowerShell

The process of adding a relying party trust in [!include[](../includes/pn-adfs-short.md)] can also be performed by running the following [!INCLUDE[pn-powershell-short](../includes/pn-powershell-short.md)] script on the [!include[](../includes/pn-adfs-short.md)] server (save contents to a file named Add-AdxPortalRelyingPartyTrustForSaml.ps1). After running the script, continue with configuring the portal site settings.

```
<# 

.SYNOPSIS

Adds a SAML 2.0 relying party trust entry for a website.

.PARAMETER domain

The domain name of the portal.

.EXAMPLE

PS C:\\> .\\Add-AdxPortalRelyingPartyTrustForSaml.ps1 -domain portal.contoso.com

#>

param

(

[parameter(Mandatory=$true,Position=0)]

$domain,

[parameter(Position=1)]

$callbackPath = /signin-saml2

)

$VerbosePreference = Continue

$ErrorActionPreference = Stop

Import-Module adfs

Function Add-CrmRelyingPartyTrust

{

param (

[parameter(Mandatory=$true,Position=0)]

$name

)

$identifier = https://{0}/ -f $name

$samlEndpoint = New-ADFSSamlEndpoint -Binding POST -Protocol SAMLAssertionConsumer -Uri (https://{0}{1} -f $name, $callbackPath)

$identityProviderValue = Get-ADFSProperties | % { $_.Identifier.AbsoluteUri }

$issuanceTransformRules = @'

@RuleTemplate = MapClaims

@RuleName = Transform [!INCLUDE[pn-ms-windows-short](../includes/pn-ms-windows-short.md)] Account Name to Name ID claim

c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname"]

=> issue(Type = "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier", Issuer = c.Issuer, OriginalIssuer = c.OriginalIssuer, Value = c.Value, ValueType = c.ValueType, Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/format"] = "urn:oasis:names:tc:SAML:2.0:nameid-format:persistent");

@RuleTemplate = LdapClaims

@RuleName = Send LDAP Claims

c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", Issuer == "AD AUTHORITY"]

=> issue(store = "[!INCLUDE[pn-active-directory](../includes/pn-active-directory.md)]", types = ("http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname", "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname", "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress"), query = ";givenName,sn,mail;{{0}}", param = c.Value);

'@ -f $identityProviderValue

$issuanceAuthorizationRules = @'

@RuleTemplate = AllowAllAuthzRule

=> issue(Type = http://schemas.microsoft.com/authorization/claims/permit, Value = true);

'@

Add-ADFSRelyingPartyTrust -Name $name -Identifier $identifier -SamlEndpoint $samlEndpoint -IssuanceTransformRules $issuanceTransformRules -IssuanceAuthorizationRules $issuanceAuthorizationRules

}

# add the 'Identity Provider' claim description if it is missing

if (-not (Get-ADFSClaimDescription | ? { $_.Name -eq Persistent Identifier })) {

Add-ADFSClaimDescription -name "Persistent Identifier" -ClaimType "urn:oasis:names:tc:SAML:2.0:nameid-format:persistent" -IsOffered:$true -IsAccepted:$true

}

# add the portal relying party trust

Add-CrmRelyingPartyTrust $domain
```

### See also

[Configure portal authentication](configure-portal-authentication.md)  
[Set authentication identity for a portal](set-authentication-identity.md)  
[OAuth2 provider settings for portals](configure-oauth2-settings.md)  
[Open ID Connect provider settings for portals](configure-openid-settings.md)  
[WS-Federation provider settings for portals](configure-ws-federation-settings.md)  
