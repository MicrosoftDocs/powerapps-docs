---
title: "API limits overview (Microsoft Dataverse) | Microsoft Docs" 
description: "Understand the limits for Microsoft Dataverse API requests." 
ms.custom: intro-internal
ms.date: 03/05/2020
ms.reviewer: "kvivek"
ms.service: powerapps
ms.topic: "conceptual"
author: "JimDaly" 
ms.author: "jdaly" 
manager: "ryjones" 
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Microsoft Dataverse API limits overview

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

Dataverse API limits help ensure service levels, availability, and quality. Dataverse API limits are part of the Power Platform Request limits and allocations. This article will introduce limits specifically for Dataverse applicable for Power Apps, Power Automate, and customer engagement apps (Dynamics 365 Sales, Dynamics 365 Customer Service, Dynamics 365 Field Service, Dynamics 365 Marketing, and Dynamics 365 Project Service Automation) connecting to Dataverse. 

For information about limits for all areas within Power Platform, see [Power Platform Request limits and allocations](/power-platform/admin/api-request-limits-allocations).

There are two categories of limits that apply for Dataverse: *Entitlement* and *Service protection* limits.

## Entitlement limits

These limits represent the number of requests users are entitled to make each day. The allocated limit depends on the type of license assigned to each user.

If any user exceeds their request entitlement the administrator would be notified and would be able to assign Power Apps and Power Automate request capacity to that user. Users will not be blocked from using apps for occasional and reasonable overages at this point of time.

For Dataverse, API requests include all data operations that interact with table rows where rows are created, retrieved, updated, or deleted (CRUD). Special operations such as *share* and *assign* are included because they are considered updates. These requests can be from any client or application and using any endpoint. These include, but are not limited to, operations performed by plug-ins, async workflows, custom controls, and $batch (ExecuteMultiple) operations. There are a small set of system internal operations that are excluded, like login, sign out, and system metadata operations.

> [!IMPORTANT]
> Power Platform API request allocations include use of Power Automate, AI Builder, and Connector APIs. All requests through a connector that result in a Dataverse request will represent 1 Power Platform request.

For details on these entitlement limits, see [Microsoft Power Platform requests allocations based on licenses](/power-platform/admin/api-request-limits-allocations#microsoft-power-platform-requests-allocations-based-on-licenses).

For information about viewing and allocating capacity add-ons, see [Capacity add-ons](/power-platform/admin/capacity-add-on).

For information about purchasing individual capacity add-ons see the [Power Apps and Power Automate Licensing Guide](https://go.microsoft.com/fwlink/?linkid=2085130). 
<!-- There should be some help about purchasing these through the Portal -->


## Service protection limits

To ensure consistent availability and performance for everyone we apply some limits to how APIs are used with Dataverse. Service protection API limits help ensure that users running applications cannot interfere with each other based on resource constraints. The limits will not affect normal users of the platform. Only applications that perform a large number of API requests may be affected. The limits provide a level of protection from random and unexpected surges in request volumes that threaten the availability and performance characteristics of the Dataverse platform.

We limit the number of concurrent connections per user account, the number of API requests per connection, and the amount of execution time that can be used for each connection. These are evaluated within a five-minute sliding window. When one of these limits is exceeded, an exception will be thrown by the platform.

> [!NOTE]
> Service protection limits apply to all external web service requests, not only the CRUD operations on tables counted against entitlement limits.
> 
> Service protection API limits are not applied against API calls made within workflows, custom workflow activities, or plug-in code. These operations are invoked internally.

Because service protection limits are usually only encountered by applications that perform a high volume of data operations, we recommend that developers building those applications apply patterns to retry operations after a period of time when these exceptions are returned. This will allow the application to respond to exceptions the service sends and reduce the total number of requests and achieve the highest possible throughput.

For information about the specific errors that can be returned and how developers can apply patterns to respond to these errors, see [Service Protection API Limits](../../developer/data-platform/api-limits.md).


### See also

[Administer Power Platform / Licensing and license management / Requests limits and allocations](/power-platform/admin/api-request-limits-allocations)<br />
[Developer / Work with data using code / Service Protection API Limits](../../developer/data-platform/api-limits.md)



[!INCLUDE[footer-include](../../includes/footer-banner.md)]