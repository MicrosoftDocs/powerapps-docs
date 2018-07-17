---
title: "Get started with Online Management API (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Provides basic information to help you get started with the Online Admin API for Common Data Service for Apps." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "jamesol-msft" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Get started with Online Management API

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/online-management-api/get-started-online-management-api -->

This topic provides basic information to help you get started with the Online Admin API for Customer Engagement.

## Office 365 Admin roles

To use the Online Management API, you must have one of the following admin roles assigned to you in your Office 365 tenant:

- Global administrator
- Service administrator

For information about these roles, see [About Office 365 admin roles](https://support.office.com/en-us/article/About-Office-365-admin-roles-da585eea-f576-4f55-a1e0-87090b6aaa9d)

## Service URL

The service URL defines the endpoint address for accessing REST API. To perform any operation using the Online Management API, you need to specify the request URL in the following format:

`{ServiceUrl}/api/v1/{resource}`

For example, you can pass in the following URL with a **GET** request to retrieve the instances in your Office 365 tenant in North America:

`https://admin.services.crm.dynamics.com/api/v1/instances`


The following table lists the service URL of Online Management API for worldwide Office 365 data centers.

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


## Standard headers

The Online Management API has following standard request and response headers.   

### Request headers

| Header | Type | Description  |
|--------|------|--------------|
|**Accept-Language**|String|Specifies the preferred language for the response. More information about the header: [Accept-Language (MDN web docs)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Language)|
|**Authorization**|String|Specifies the credentials to authenticate a user with the Online Management API service. More information about the header: [Authorization (MDN web docs)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)|

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