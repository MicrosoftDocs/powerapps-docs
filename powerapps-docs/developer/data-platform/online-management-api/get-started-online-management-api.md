---
title: "Get started with Online Management API for Microsoft Dataverse| MicrosoftDocs"
description: "Provides basic information to help you get started with the Online Admin API for Microsoft Dataverse."
ms.date: 10/23/2020
ms.service: powerapps
ms.topic: conceptual
ms.assetid: c292c148-01f0-41f6-a2fe-7ed05a01a733
author: KumarVivek
ms.author: kvivek
manager: annbe
search.audienceType: 
  - developer
search.app: 
  - PowerApps
---
# Get started with Online Management API 

> [!NOTE]
> Effective August 26, 2020, the Online Management API is [deprecated](/power-platform/important-changes-coming#online-management-api-powershell-module-and-rest-api-are-deprecated). 

This topic provides basic information to help you get started with the Online Admin API for Microsoft Dataverse.

## Microsoft 365 Admin roles

To use the Online Management API, you must have one of the following admin roles assigned to you in your Microsoft 365 tenant:

- Global administrator
- Service administrator

For information about these roles, see [About admin roles](https://support.office.com/article/About-Office-365-admin-roles-da585eea-f576-4f55-a1e0-87090b6aaa9d)

## Service URL

The service URL defines the endpoint address for accessing REST API. To perform any operation using the Online Management API, you need to specify the request URL in the following format:

`{ServiceUrl}/api/v1.2/{resource}`

For example, you can pass in the following URL with a **GET** request to retrieve the instances in your Microsoft 365 tenant in North America:

`https://admin.services.crm.dynamics.com/api/v1.2/instances`

For a list service URLs, see [Service URL](/powershell/powerapps/overview?view=pa-ps-latest#service-url).

<!--
The following table lists the service URLs of Online Management API for worldwide Microsoft 365 data centers.

|Location | Service URL |
|---------|-------------|
|North America | https://admin.services.crm.dynamics.com |
|North America 2 | https://admin.services.crm9.dynamics.com |
|Europe, Middle East and Africa (EMEA) | https://admin.services.crm4.dynamics.com |
|Asia Pacific (APAC) | https://admin.services.crm5.dynamics.com |
|Oceania | https://admin.services.crm6.dynamics.com |
|Japan (JPN) | https://admin.services.crm7.dynamics.com |
|South America | https://admin.services.crm2.dynamics.com |
|India (IND) | https://admin.services.crm8.dynamics.com |
|Canada | https://admin.services.crm3.dynamics.com |
|United Kingdom (UK) | https://admin.services.crm11.dynamics.com |
|France | https://admin.services.crm12.dynamics.com |
-->

## Standard headers

The Online Management API has following standard request and response headers.

### Request headers

| Header | Type | Description  |
|--------|------|--------------|
|**Accept-Language**|String|Specifies the preferred language for the response. More information about the header: [Accept-Language (MDN web docs)](https://developer.mozilla.org/docs/Web/HTTP/Headers/Accept-Language)|
|**Authorization**|String|Specifies the credentials to authenticate a user with the Online Management API service. More information about the header: [Authorization (MDN web docs)](https://developer.mozilla.org/docs/Web/HTTP/Headers/Authorization)|

See [Authenticate to use the Online Management API](authentication.md) to know about setting these headers in your request.

### Response headers

| Header | Description  |
|--------|--------------|
|**Operation-Location**|For long-running operations, specifies the location of the operation query to check its status. For example:<br />`https://admin.services.crm.dynamics.com/operations/{operationid}`|
|**Retry-After**|For long-running operations, specifies the recommended period in seconds after which to query the operation status again. For example: **30**|
    
### Related Topics  

[Authenticate to use Online Management API](authentication.md)

[Operations supported by Online Management API](operations-supported.md)

[Online Management API Reference](/rest/api/admin.services.crm.dynamics.com)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]