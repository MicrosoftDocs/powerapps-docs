---
title: "Optimistic concurrency (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Optimistic Concurrency provides the ability for your applications to detect whether an entity record has changed on the server in the time between when your application retrieved the record and when it tries to update or delete that record" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Optimistic concurrency

On a multi-threaded and multi-user system like PowerApps, operations and data changes often happen in parallel. A problem arises when two or more update or delete operations on the same piece of data happen at the same time. This situation could potentially result in data loss. The optimistic concurrency feature provides the ability for your applications to detect whether an entity record has changed on the server in the time between when your application retrieved the record and when it tries to update or delete that record.  
  
 Optimistic concurrency is supported on all out-of-box entities enabled for offline sync and all custom entities. You can determine if an entity supports optimistic concurrency by retrieving the entity’s metadata using code or by viewing the metadata using the [Metadata Browser](browse-your-metadata.md), and check if the attribute **IsOptimisticConcurrencyEnabled** is set to `true`. For custom entities, this property is set to `true` by default.  
  
<a name="bkmk_enable"></a>   
## Enable optimistic concurrency  
 You can enable optimistic concurrency checking behavior when executing an <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> by setting the <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest.ConcurrencyBehavior> property of the request to <xref:Microsoft.Xrm.Sdk.ConcurrencyBehavior.IfRowVersionMatches>. Similarly, for a <xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest>, you would set the <xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest.ConcurrencyBehavior> property.  
  
 When using the organization service context to make data changes, set <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceContext.ConcurrencyBehavior> on the <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceContext> object. This value will be passed through to all of the **UpdateRequest** and **DeleteRequest** messages used by the **OrganizationServiceContext** when <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceContext.SaveChanges> is called.  
  
 Optimistic concurrency behavior can only be set through an SDK call. There is presently no setting for it in a form of the Web application.  
  
## Apply optimistic concurrency using Web API

For information about using Web API to apply optimistic concurrency, see [Apply optimistic concurrency](webapi/perform-conditional-operations-using-web-api.md##apply-optimistic-concurrency)


## Apply optimistic concurrency using Organization service

For information about using Organization service to apply optimistic concurrency, see [Optimistic concurrency behavior](org-service/entity-operations-update-delete.md##optimistic-concurrency-behavior)
  
<a name="bkmk_handle"></a>   
## Handle exceptions  
 There are several error conditions that can be returned in a [FaultException](https://msdn.microsoft.com/library/ms576199\(v=vs.110\).aspx)\<<xref:Microsoft.Xrm.Sdk.OrganizationServiceFault>> from the Web service call when using optimistic concurrency.  
  
- **ConcurrencyVersionMismatch** (code=-2147088254)  
  
     When a row version is provided and the **IfVersionMatches** behavior is indicated, if the existing record’s version does not match the row version provided in the request, a fault is returned.  
  
- **ConcurrencyVersionNotProvided** (code= -2147088253)  
  
     When the **IfVersionMatches** behavior is indicated, and no value for row version is provided, a fault is returned.  
  
- **OptimisticConcurrencyNotEnabled** (code=-2147088243)  
  
     When the **IfVersionMatches** behavior is indicated on an update to an entity, and where optimistic concurrency isn’t enabled, a fault is returned.  
  
  You can check the [Code](https://msdn.microsoft.com/library/system.servicemodel.faultexception.code\(v=vs.110\).aspx) property of the returned fault to determine if the fault is related to optimistic concurrency. The codes for the error conditions that were shown previously were obtained from the ErrorCodes.cs helper code.  
  
