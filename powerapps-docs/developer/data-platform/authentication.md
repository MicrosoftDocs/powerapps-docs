---
title: "Authenticate with Microsoft Dataverse web services (Dataverse) | Microsoft Docs"
description: "Introduces authentication options that depend on the software framework you use." 
ms.custom: ""
ms.date: 01/06/2022
ms.reviewer: "pehecke"

ms.topic: "article"
author: "paulliew" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "jdaly" # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
---
# Authenticate with Microsoft Dataverse web services

When you create client applications that use Dataverse web services you need to authenticate to gain access to data.
How you authenticate depends on the software framework you use and which web service you want to connect with.

## .NET Framework applications

If your client application uses the .NET Framework, you have two authentication options:

- OAuth (recommended)
- Microsoft 365

### OAuth

OAuth is the preferred means to authenticate because it provides access to all web services.

OAuth is also required to support:
 - Microsoft Entra ID configurations for conditional access, such as Two-factor Authentication (2FA)
 - Use of client secrets to enable server-to-server authentication scenarios.
 - Cross-Origin Resource Sharing (CORS) to connect a Single-page Application (SPA)

More information: [Use OAuth with Dataverse](authenticate-oauth.md)

### Microsoft 365

Microsoft 365 authentication (referred to as Office365 in code) requires using the .NET Framework SDK assemblies with the web services.

Using Microsoft 365 authentication does not require that your register your applications as OAuth does. You must simply provide a User Principal Name (UPN) and password for a valid user.

More information: [Authentication with .NET Framework applications](authenticate-dot-net-framework.md)

> [!IMPORTANT]
> Microsoft 365 authentication for Dataverse is deprecated. More information: [Use of Office365 authentication with Microsoft Dataverse](authenticate-office365-deprecation.md)

## All other software frameworks

If you are using anything other than .NET Framework, you must authenticate using OAuth and you must use the OData RESTful web services (Web API and OData global Discovery service).

More information:  [Use OAuth with Dataverse](authenticate-oauth.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
