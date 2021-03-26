---
title: "Build web applications using server-to-server (S2S) authentication (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Use server-to-server (S2S) authentication to securely and seamlessly communicate with Microsoft Dataverse with your web applications and services." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/24/2021
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

# Build web applications using server-to-server (S2S) authentication

Use server-to-server (S2S) authentication to securely and seamlessly communicate with Microsoft Dataverse with your web applications and services. S2S authentication is the common way that apps registered on Microsoft AppSource use to access the Dataverse data of their subscribers.  

S2S authentication means you don’t need to use a paid Power Apps user license when you connect to Dataverse environments. There is no license fee for the special *application user* account you will use with S2S authentication. However, there are [limits to the number of requests the application user](/power-platform/admin/api-request-limits-allocations#non-licensed-usersapplication-users) account can call. With S2S authentication, a special unlicensed application user account is created and includes information about your application registered with Azure Active Directory (Azure AD). Rather than user credentials, the application is authenticated based on a service principal identified by an Azure AD Object ID value which is stored in the application user record. The application user is associated with a custom security role which controls the kinds of data and operations the application is allowed to perform.  

 All operations performed by your application or service using S2S will be performed as the application user you provide rather than as the user who is accessing your application. If you want your application to perform data operations on behalf of a specific user, such as the one who is interacting with your application, you can apply impersonation when the custom security role applied to your application service principal has the privileges required. More information: [Impersonate another user](impersonate-another-user.md)  

 A web application or service which uses S2S authentication is responsible for controlling access to the data that it has access to. This is typically done using an OpenID Connect provider. More information: [Open ID Connect](https://openid.net/connect/).

## Server-to-Server authentication scenarios

 There are two scenarios where you can apply S2S authentication.  

|   Scenario    |   Description  |
|---------------|---------------|
| Multi-Tenant  | This is the most common scenario and the one which is used for apps distributed using Microsoft AppSource.<br /><br /> Each Dataverse tenant is associated with an Azure AD tenant. Your web application or service is registered with your Azure AD tenant.<br /><br /> In this scenario any Dataverse tenant can potentially use your multi-tenant application after they grant consent for the application to access data in their tenant.                                                           |
| Single-Tenant | This scenario typically applies to Dataverse environments that want to develop apps for their own tenant and don’t intend to distribute them to other Dataverse environments.<br /><br /> An enterprise can create a web application or service to connect to all the Dataverse environments for their tenant.<br /><br /> In this scenario, your web application or service will only be able to connect to Dataverse environments using the same Azure AD tenant. |

 Both scenarios have common elements but there are some differences. Since multi-tenant is the most common scenario, the [Use Multi-Tenant server-to-server authentication](use-multi-tenant-server-server-authentication.md) content describes how you can use S2S in this scenario and include notes where the options for single-tenant configuration is different.

[Use Single-Tenant server-to-server authentication](use-single-tenant-server-server-authentication.md) provides an overview of this scenario and refer to the procedures described in the multi-tenant S2S authentication content.  

### See also  
  
[Use Multi-Tenant server-to-server authentication](use-multi-tenant-server-server-authentication.md)<br/> 
[Use Single-Tenant server-to-server authentication](use-single-tenant-server-server-authentication.md)   


[!INCLUDE[footer-include](../../includes/footer-banner.md)]