---
title: "Use Single-Tenant server-to-server authentication (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "<Description>" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "paulliew" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Use Single-Tenant server-to-server authentication


The single-tenant server-to-server scenario typically applies for enterprise organizations who have multiple Common Data Service (CDS) for Apps environments using Active Directory Federation Services (AD FS) for authentication. However, it can also be applied by environments when the application won't be distributed to other environments.  
  
 An enterprise can create a web application or service to connect to all the CDS for Apps environments for the single tenant.  
  
## Differences from multi-tenant scenario  
 Creating a web application or service for a single-tenant server-to-server authentication is similar to that used for a multi-tenant organization but there are some important differences.  
  
-   Because all the organizations are in the same tenant, there is no need for a tenant admin to grant consent. The application is already registered on the tenant.  
  
-   You have the opportunity to use certificates rather than keys if you prefer.  
  
### See also  
 [Use Multi-Tenant Server-to-server authentication](use-multi-tenant-server-server-authentication.md)   
 [Build web applications using Server-to-Server (S2S) authentication](build-web-applications-server-server-s2s-authentication.md)

<!--

 Can this scenario be hightlighted here: https://crmtipoftheday.com/767/server-to-server-authentication-is-here/

-->