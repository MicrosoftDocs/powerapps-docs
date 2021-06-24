---
title: "Authenticate with Microsoft Dataverse web services (Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Introduces authentication options that depend on the software framework you use." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/23/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "paulliew" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Authenticate with Microsoft Dataverse web services

When you create client applications that use Dataverse web services you need to authenticate to gain access to data.
How you authenticate depends on the software framework you use and which web service you want to connect with.

## .NET Framework applications

If your client application uses the .NET Framework, you have two options:

- OAuth
- Microsoft 365

### OAuth

OAuth is the preferred means to authenticate because it provides access to *both* the OData RESTful web services (Web API and OData global Discovery service) as well as to the SOAP web services (Organization service and Discovery service).

OAuth is also required to support:
 - Azure Active Directory configurations for conditional access, such as Two-factor Authentication (2FA)
 - Use of client secrets to enable server-to-server authentication scenarios.
 - Cross-Origin Resource Sharing (CORS) to connect a Single-page Application (SPA)

More information: [Use OAuth with Dataverse](authenticate-oauth.md)

### Microsoft 365

Microsoft 365 authentication requires using the .NET Framework SDK assemblies with the SOAP web services only.

Using Microsoft 365 authentication does not require that your register your applications as OAuth does. You must simply provide a User Principal Name (UPN) and password for a valid user.

More information: [Authentication with .NET Framework applications](authenticate-dot-net-framework.md), [Use of Microsoft 365 authentication with the WS-Trust security protocol](authenticate-office365-deprecation.md)

## All other software frameworks

If you are using anything other than .NET Framework, you must authenticate using OAuth and you must use the OData RESTful 
web services (Web API and OData global Discovery service).

More information:  [Use OAuth with Dataverse](authenticate-oauth.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]