---
title: "Configure WS-Federation provider settings for a portal  | MicrosoftDocs"
description: "Instructions to add and configure WS-Federation provider settings for a portal."
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/18/2019
ms.author: sandhan
ms.reviewer: tapanm
---

# Create an AD FS relying party trust

Using the AD FS Management tool, go to **Trust Relationships** &gt; **Relying Party Trusts**.

1.  Select **Add Relying Party Trust**.
2.  Welcome: Select **Start**.
3.  Select Data Source: Select **Enter data about the relying party manually**, and then select **Next**.
4.  Specify Display Name: Enter a **name**, and then select **Next**.
    Example: https://portal.contoso.com/
5.  Choose Profile: Select **AD FS 2.0 profile**, and then select **Next**.
6.  Configure Certificate: Select **Next**.
7.  Configure URL: Select the **Enable support for the WS-Federation Passive protocol** check box.

Relying party WS-Federation Passive protocol URL: Enter https://portal.contoso.com/signin-federation

-   Note: AD FS requires that the portal run on **HTTPS**.

    > [!Note]
    > The resulting endpoint has the following settings:
    > Endpoint type: **WS-Federation**
    > -   Binding: **POST**
    > -   Index: n/a (0)
    > -   URL: **https://portal.contoso.com/signin-federation**

8.  Configure Identities: Specify https://portal.contoso.com/, select **Add**, and then select **Next**.
    If applicable, more identities can be added for each additional relying party portal. Users will be able to authenticate across any or all of the available identities.
9.  Choose Issuance Authorization Rules: Select **Permit all users to access this relying party**, and then select **Next**.
10.  Ready to Add Trust: Select **Next**.
11.  Select **Close**.

Add the **Name ID** claim to the relying party trust:

**Transform [!INCLUDE[pn-ms-windows-short](../../../includes/pn-ms-windows-short.md)] account name** to **Name ID** claim (Transform an Incoming Claim):
- Incoming claim type: Windows account name
- Outgoing claim type: Name ID
- Outgoing name ID format: Unspecified
- Pass through all claim values

### Create AD FS site settings

Apply portal site settings referencing the above AD FS Relying Party Trust.

> [!Note]
> A standard AD FS (STS) configuration only uses the following settings (with example values):
> - Authentication/WsFederation/ADFS/MetadataAddress - https://adfs.contoso.com/FederationMetadata/2007-06/FederationMetadata.xml
> - Authentication/WsFederation/ADFS/AuthenticationType - https://adfs.contoso.com/adfs/services/trust
>   - Use the value of the **entityID** attribute in the root element of the Federation Metadata (open the **MetadataAddress URL** in a browser that is the value of the above site setting)
> - Authentication/WsFederation/ADFS/Wtrealm - https://portal.contoso.com/
> - Authentication/WsFederation/ADFS/Wreply - https://portal.contoso.com/signin-federation

The **WS-Federation metadata** can be retrieved in **[!INCLUDE[pn-powershell-short](../../../includes/pn-powershell-short.md)]** by running the following script on the AD FS server:

```
Import-Module adfs
Get-ADFSEndpoint -AddressPath /FederationMetadata/2007-06/FederationMetadata.xml
```


|                      Site Setting Name                      |                                                                                                                                                                                                                                                 Description                                                                                                                                                                                                                                                 |
|-------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|      Authentication/Registration/ExternalLoginEnabled       |                                                                                                                                                                                                                Enables or disables external account sign-in and registration. Default: true                                                                                                                                                                                                                 |
|      Authentication/WsFederation/ADFS/MetadataAddress       | Required. The [WS-Federation](https://msdn.microsoft.com/library/bb498017.aspx) metadata URL of the AD FS (STS) server. Commonly ending with the path:/FederationMetadata/2007-06/FederationMetadata.xml . Example:<https://adfs.contoso.com/FederationMetadata/2007-06/FederationMetadata.xml>. For more information: [WsFederationAuthenticationOptions.MetadataAddress](https://msdn.microsoft.com/library/microsoft.owin.security.wsfederation.wsfederationauthenticationoptions.metadataaddress.aspx). |
|     Authentication/WsFederation/ADFS/AuthenticationType     |            Required. The OWIN authentication middleware type. Specify the value of the [entityID](https://docs.microsoft.com/azure/active-directory/develop/active-directory-federation-metadata) attribute at the root of the federation metadata XML. Example: https://adfs.contoso.com/adfs/services/trust. For more information: [AuthenticationOptions.AuthenticationType](https://msdn.microsoft.com/library/microsoft.owin.security.authenticationoptions.authenticationtype.aspx).             |
|          Authentication/WsFederation/ADFS/Wtrealm           |                                                                                                              Required. The AD FS relying party identifier. Example: `https://portal.contoso.com/`. For more information: [WsFederationAuthenticationOptions.Wtrealm](https://msdn.microsoft.com/library/microsoft.owin.security.wsfederation.wsfederationauthenticationoptions.wtrealm.aspx).                                                                                                               |
|           Authentication/WsFederation/ADFS/Wreply           |                                                                                                     Required. The AD FS WS-Federation passive endpoint. Example: https://portal.contoso.com/signin-federation. For more information: [WsFederationAuthenticationOptions.Wreply](https://msdn.microsoft.com/library/microsoft.owin.security.wsfederation.wsfederationauthenticationoptions.wreply.aspx).                                                                                                     |
|          Authentication/WsFederation/ADFS/Caption           |                                                                                                           Recommended. The text that the user can display on a sign in user interface. Default: ADFS. For more information: [WsFederationAuthenticationOptions.Caption](https://msdn.microsoft.com/library/microsoft.owin.security.wsfederation.wsfederationauthenticationoptions.caption.aspx).                                                                                                            |
|        Authentication/WsFederation/ADFS/CallbackPath        |                                                                                                             An optional constrained path on which to process the authentication callback. For more information: [WsFederationAuthenticationOptions.CallbackPath](https://msdn.microsoft.com/library/microsoft.owin.security.wsfederation.wsfederationauthenticationoptions.callbackpath.aspx).                                                                                                              |
|       Authentication/WsFederation/ADFS/SignOutWreply        |                                                                                                                               The 'wreply' value used during sign-out. For more information: [WsFederationAuthenticationOptions.SignOutWreply](https://msdn.microsoft.com/library/microsoft.owin.security.wsfederation.wsfederationauthenticationoptions.signoutwreply.aspx).                                                                                                                               |
|     Authentication/WsFederation/ADFS/BackchannelTimeout     |                                                                                                         Timeout value for back channel communications. Example: 00:05:00 (5 mins). For more information: [WsFederationAuthenticationOptions.BackchannelTimeout](https://msdn.microsoft.com/library/microsoft.owin.security.wsfederation.wsfederationauthenticationoptions.backchanneltimeout.aspx).                                                                                                         |
| Authentication/WsFederation/ADFS/RefreshOnIssuerKeyNotFound |                                                                                  Determines if a metadata refresh should be attempted after a SecurityTokenSignatureKeyNotFoundException. For more information: [WsFederationAuthenticationOptions.RefreshOnIssuerKeyNotFound](https://msdn.microsoft.com/library/microsoft.owin.security.wsfederation.wsfederationauthenticationoptions.refreshonissuerkeynotfound.aspx).                                                                                  |
|      Authentication/WsFederation/ADFS/UseTokenLifetime      |                                                                                                   Indicates that the authentication session lifetime (e.g. cookies) should match that of the authentication token. [WsFederationAuthenticationOptions.UseTokenLifetime](https://msdn.microsoft.com/library/microsoft.owin.security.wsfederation.wsfederationauthenticationoptions.usetokenlifetime.aspx).                                                                                                   |
|     Authentication/WsFederation/ADFS/AuthenticationMode     |                                                                                                                                            The OWIN authentication middleware mode. For more information: [AuthenticationOptions.AuthenticationMode](https://msdn.microsoft.com/library/microsoft.owin.security.authenticationoptions.authenticationmode.aspx).                                                                                                                                             |
| Authentication/WsFederation/ADFS/SignInAsAuthenticationType |                                                                                            The AuthenticationType used when creating the System.Security.Claims.ClaimsIdentity. For more information: [WsFederationAuthenticationOptions.SignInAsAuthenticationType](https://msdn.microsoft.com/library/microsoft.owin.security.wsfederation.wsfederationauthenticationoptions.signinasauthenticationtype.aspx).                                                                                            |
|       Authentication/WsFederation/ADFS/ValidAudiences       |                                                                                                                                         Comma separated list of audience URLs. For more information: [TokenValidationParameters.AllowedAudiences](https://msdn.microsoft.com/library/system.identitymodel.tokens.tokenvalidationparameters.allowedaudiences.aspx).                                                                                                                                          |
|        Authentication/WsFederation/ADFS/ValidIssuers        |                                                                                                                                              Comma separated list of issuer URLs. For more information: [TokenValidationParameters.ValidIssuers](https://msdn.microsoft.com/library/system.identitymodel.tokens.tokenvalidationparameters.validissuers.aspx).                                                                                                                                               |
|         Authentication/WsFederation/ADFS/ClockSkew          |                                                                                                                                                                                                                               The clock skew to apply when validating times.                                                                                                                                                                                                                                |
|       Authentication/WsFederation/ADFS/NameClaimType        |                                                                                                                                                                                                                     The claim type used by the ClaimsIdentity to store the name claim.                                                                                                                                                                                                                      |
|       Authentication/WsFederation/ADFS/RoleClaimType        |                                                                                                                                                                                                                     The claim type used by the ClaimsIdentity to store the role claim.                                                                                                                                                                                                                      |
|   Authentication/WsFederation/ADFS/RequireExpirationTime    |                                                                                                                                                                                                                     A value indicating whether tokens must have an 'expiration' value.                                                                                                                                                                                                                      |
|    Authentication/WsFederation/ADFS/RequireSignedTokens     |                                                                                                                                                                       A value indicating whether a System.IdentityModel.Tokens.SecurityToken xmlns=<https://ddue.schemas.microsoft.com/authoring/2003/5> can be valid if not signed.                                                                                                                                                                       |
|      Authentication/WsFederation/ADFS/SaveSigninToken       |                                                                                                                                                                                                               A Boolean to control if the original token is saved when a session is created.                                                                                                                                                                                                                |
|       Authentication/WsFederation/ADFS/ValidateActor        |                                                                                                                                                                                                   A value indicating whether the System.IdentityModel.Tokens.JwtSecurityToken.Actor should be validated.                                                                                                                                                                                                    |
|      Authentication/WsFederation/ADFS/ValidateAudience      |                                                                                                                                                                                                               A Boolean to control if the audience will be validated during token validation.                                                                                                                                                                                                               |
|       Authentication/WsFederation/ADFS/ValidateIssuer       |                                                                                                                                                                                                                A Boolean to control if the issuer will be validated during token validation.                                                                                                                                                                                                                |
|      Authentication/WsFederation/ADFS/ValidateLifetime      |                                                                                                                                                                                                               A Boolean to control if the lifetime will be validated during token validation.                                                                                                                                                                                                               |
|  Authentication/WsFederation/ADFS/ValidateIssuerSigningKey  |                                                                                                                                                         A Boolean that controls if validation of the System.IdentityModel.Tokens.SecurityKey that signed the securityToken xmlns=<https://ddue.schemas.microsoft.com/authoring/2003/5> is called.                                                                                                                                                          |
|            Authentication/WsFederation/ADFS/Whr             |                                                                                                                                       Specifies a "whr" parameter in the identity provider redirect URL. For more information: [wsFederation](https://docs.microsoft.com/dotnet/framework/configure-apps/file-schema/windows-identity-foundation/wsfederation).                                                                                                                                       |
