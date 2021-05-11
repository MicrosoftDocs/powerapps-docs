---
title: "Authenticate to Microsoft Dataverse with the Web API (Dataverse)| Microsoft Docs"
description: "Learn about the different ways to manage authentication when using the Web API"
ms.custom: ""
ms.date: 10/31/2018
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 767f39d4-6a8e-48f0-bf7d-69ea1191acef
caps.latest.revision: 8
author: "JimDaly" # GitHub ID
ms.author: "jdaly"
ms.reviewer: "pehecke"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Authenticate to Microsoft Dataverse with the Web API

You must use OAuth as described in [Use OAuth with Dataverse](../authenticate-oauth.md).

The code you write to manage authentication when using the Web API depends on the type of deployment and where your code is.  
  
## Authenticate with JavaScript in web resources

When you use the Web API with JavaScript within HTML web resources, form scripts, or ribbon commands you don’t need to include any code for authentication. In each of these cases the user is already authenticated by the application and authentication is managed by the application.  

If you’re creating a single page application (SPA) using JavaScript you can use the adal.js library as described in [Use OAuth with Cross-Origin Resource Sharing  to connect a Single Page Application](../oauth-cross-origin-resource-sharing-connect-single-page-application.md).  
  
### See also
 
[Use the Dataverse Web API](overview.md)<br />
[Web API types and operations](web-api-types-operations.md)<br />
[Perform operations using the Web API](perform-operations-web-api.md)<br />
[Use OAuth with Dataverse](../authenticate-oauth.md)<br />
[Use OAuth with Cross-Origin Resource Sharing to connect a Single Page Application](../oauth-cross-origin-resource-sharing-connect-single-page-application.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]