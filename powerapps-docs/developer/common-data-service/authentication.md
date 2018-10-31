---
title: "Authentication with Common Data Service for Apps web services (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Introduces authentication options that depend on the software framework you use." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "paulliew" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Authentication with Common Data Service for Apps web services

When you create client applications that use CDS for Apps web services you need to authenticate to gain access to data. 
How you authenticate depends on the software framework you use and which web service you want to connect with.

## .NET Framework Applications

If your client application uses the .NET Framework, you have two options:

- OAuth
- Office 365

### OAuth

OAuth is the preferred means to authenticate because it provides access to *both* the OData RESTful web services (Web API 
and OData Global Discovery Service) as well as to the SOAP web services (Organization Service and Discovery Service). 

OAuth is also required to support: 
 - Azure Active Directory configurations for conditional access, such as Two Factor Authentication (2FA)
 - Use of client secrets to enable server-to-server authentication scenarios.
 - Cross-Origin Resource Sharing (CORS) to connect a Single Page Application (SPA)

More information: [Use OAuth with Common Data Service for apps](authenticate-oauth.md)

### Office 365

Office 365 authentication requires using the .NET Framework SDK assemblies with the SOAP web services only.

Using Office 365 authentication does not require that your register your applications as OAuth does. You must simply provide a User Principal Name (UPN) and password for a valid user.

More information: [Authentication with .NET Framework applications](authenticate-dot-net-framework.md)

## All other software frameworks

If you are using anything other than .NET Framework, you must authenticate using OAuth and you must use the OData RESTful 
web services (Web API and OData Global Discovery Service).

More information:  [Use OAuth with Common Data Service for apps](authenticate-oauth.md)
