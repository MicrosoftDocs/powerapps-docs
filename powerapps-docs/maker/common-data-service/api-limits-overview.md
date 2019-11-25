---
title: "API limits overview (Common Data Service) | Microsoft Docs" 
description: "Understand the limits for Common Data Service API requests." 
ms.custom: ""
ms.date: 11/23/2019
ms.reviewer: "kvivek"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" 
ms.author: "jdaly" 
manager: "ryjones" 
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Common Data Service API limits overview

Common Data Service API limits help ensure service levels, availability and quality. Common Data Service API limits are part of the Power Platform Request limits and allocations. This topic will introduce limits specifically for Common Data Service applicable for model-driven apps in Dynamics 365 (such as Dynamics 365 Sales and Dynamics 365 Customer Service), Power Apps, and Power Automate connecting to Common Data Service/model-driven apps in Dynamics 365. 

For information about limits for all areas within Power Platform, see [Power Platform Request limits and allocations](/power-platform/admin/api-request-limits-allocations).

There are two categories of limits that apply for Common Data Service: *Entitlement* and *Service protection* limits.

## Entitlement limits

These limits represent the number of requests users are entitled to make each day. The allocated limit depends on the type of license assigned to each user.

If any user exceeds their request entitlement the administrator would be notified and would be able to assign Power Apps and Power Automate request capacity to that user. Users will not be blocked from using apps for occasional and reasonable overages at this point of time.

For Common Data Service, API requests include all data operations that interact with entity records where records are created, retrieved, updated, or deleted (CRUD). Special operations such as *share* and *assign* are included because they are considered updates. These requests can be from any client or application and using any endpoint. These include, but are not limited to, operations performed by plug-ins, async workflows, and custom controls. There are a small set of system internal operations that are excluded, like login, logout, and system metadata operations.

> [!IMPORTANT]
> Power Platform API request allocations include use of Power Automate, AI Builder, and Connector APIs. All requests through a connector that result in a Common Data Service request will represent 1 Power Platform request.

For details on these entitlement limits, see [Microsoft Power Platform requests allocations based on licenses](/power-platform/admin/api-request-limits-allocations#microsoft-power-platform-requests-allocations-based-on-licenses).

For information about viewing and allocating capacity add-ons, see [Capacity add-ons](/power-platform/admin/capacity-add-on).

For information about purchasing individual capacity add-ons see the [Power Apps and Power Automate Licensing Guide](https://go.microsoft.com/fwlink/?linkid=2085130). 
<!-- There should be some help about purchasing these through the Portal -->


## Service protection limits

To ensure consistent availability and performance for everyone we apply some limits to how APIs are used with Common Data Service. Service protection API limits help ensure that users running applications cannot interfere with each other based on resource constraints. The limits will not affect normal users of the platform. Only applications that perform a large number of API requests may be affected. The limits provide a level of protection from random and unexpected surges in request volumes that threaten the availability and performance characteristics of the Common Data Service platform.

We limit the number of concurrent connections per user account, the number of API requests per connection, and the amount of execution time that can be used for each connection. These are evaluated within a five minute sliding window. When one of these limits is exceeded, an exception will be thrown by the platform.

> [!NOTE]
> Service protection limits apply to all requests, not only the CRUD operations on entities counted against entitlement limits.
> 
> Since plug-ins and custom workflow activities execute on the server independent of a logged on user, service protection API limits are not applied against API calls made from plug-in code.

Because service protection limits are usually only encountered by applications that perform a high volume of data operations, we recommend that developers building those applications apply patterns to re-try operations after a period of time when these exceptions are returned. This will allow the application to respond to exceptions the service sends and reduce the total number of requests and achieve the highest possible throughput.

For information about the specific errors that can be returned and how developers can apply patterns to respond to these errors, see [Service Protection API Limits](../../developer/common-data-service/api-limits.md).


### See also

[Administer Power Platform / Licensing and license management / Requests limits and allocations](/power-platform/admin/api-request-limits-allocations)<br />
[Developer / Work with data using code / Service Protection API Limits](../../developer/common-data-service/api-limits.md)

