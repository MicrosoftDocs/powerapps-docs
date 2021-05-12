---
title: "Optimistic concurrency (Microsoft Dataverse) | Microsoft Docs" 
description: "Optimistic concurrency provides the ability for your applications to detect whether a table record has changed on the server in the time between when your application retrieved the record and when it tries to update or delete that record"
ms.custom: ""
ms.date: 03/12/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Optimistic concurrency

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

On a multi-threaded and multi-user system like Power Apps, operations and data changes often happen in parallel. A problem arises when two or more update or delete operations on the same piece of data happen at the same time. This situation could potentially result in data loss. The optimistic concurrency feature provides the ability for your applications to detect whether a table record has changed on the server in the time between when your application retrieved the record and when it tries to update or delete that record.  
  
 Optimistic concurrency is supported on all out-of-box tables enabled for offline sync and all custom tables. You can determine if a table supports optimistic concurrency by retrieving the table's metadata using code or by viewing the metadata using the [Metadata Browser](browse-your-metadata.md), and check if the column **IsOptimisticConcurrencyEnabled** is set to `true`. For custom tables, this property is set to `true` by default.  
  
<a name="bkmk_enable"></a>   
## Enable optimistic concurrency  
 You can enable optimistic concurrency checking behavior when executing an <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> by setting the <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest.ConcurrencyBehavior> property of the request to <xref:Microsoft.Xrm.Sdk.ConcurrencyBehavior.IfRowVersionMatches>. Similarly, for a <xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest>, you would set the <xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest.ConcurrencyBehavior> property.  
  
 When using the organization service context to make data changes, set <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceContext.ConcurrencyBehavior> on the <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceContext> object. This value will be passed through to all of the **UpdateRequest** and **DeleteRequest** messages used by the **OrganizationServiceContext** when <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceContext.SaveChanges> is called.  
  
 Optimistic concurrency behavior can only be set through an SDK API call. There is presently no setting for it in a form of the Web application.  
  
## Apply optimistic concurrency using Web API

For information about using Web API to apply optimistic concurrency, see [Apply optimistic concurrency](webapi/perform-conditional-operations-using-web-api.md#apply-optimistic-concurrency)


## Apply optimistic concurrency using Organization service

For information about using Organization service to apply optimistic concurrency, see [Optimistic concurrency behavior](org-service/entity-operations-update-delete.md#optimistic-concurrency-behavior)
  
<a name="bkmk_handle"></a>   
## Handle exceptions  
 There are several error conditions that can be returned in a fault exception <<xref:Microsoft.Xrm.Sdk.OrganizationServiceFault>> from the Web service call when using optimistic concurrency.  
  
- **ConcurrencyVersionMismatch** (code=-2147088254)  
  
     When a row version is provided and the **IfVersionMatches** behavior is indicated, if the existing record’s version does not match the row version provided in the request, a fault is returned.  
  
- **ConcurrencyVersionNotProvided** (code= -2147088253)  
  
     When the **IfVersionMatches** behavior is indicated, and no value for row version is provided, a fault is returned.  
  
- **OptimisticConcurrencyNotEnabled** (code=-2147088243)  
  
     When the **IfVersionMatches** behavior is indicated on an update to a table, and where optimistic concurrency isn’t enabled, a fault is returned.  
  
  You can check the [Code](https://docs.microsoft.com/dotnet/api/system.servicemodel.faultexception.code?view=netframework-4.6.2) property of the returned fault to determine if the fault is related to optimistic concurrency. The codes for the error conditions that were shown previously were obtained from the ErrorCodes.cs helper code.  
  


[!INCLUDE[footer-include](../../includes/footer-banner.md)]