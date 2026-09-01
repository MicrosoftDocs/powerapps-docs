---
title: "Optimistic concurrency (Microsoft Dataverse) | Microsoft Docs" 
description: "Optimistic concurrency provides the ability for your applications to detect whether a table record has changed on the server in the time between when your application retrieved the record and when it tries to update or delete that record"
ms.date: 08/27/2026
ms.reviewer: "pehecke"
ms.topic: "article"
author: "Peakerbl" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "jdaly" # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
contributors:
  - PHecke
  - JimDaly
---
# Optimistic concurrency

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

On a multithreaded and multiuser system like Power Apps, operations and data changes often happen in parallel. A problem arises when two or more update or delete operations on the same piece of data happen at the same time. This situation could potentially result in data loss. The optimistic concurrency feature provides the ability for your applications to detect whether a table record changed on the server in the time between when your application retrieved the record and when it tries to update or delete that record.  
  
 Optimistic concurrency is supported on all out-of-box tables enabled for offline sync and all custom tables. You can determine if a table supports optimistic concurrency by retrieving the table's metadata using code or by viewing the metadata using the [Metadata Browser](browse-your-metadata.md), and check if the column **IsOptimisticConcurrencyEnabled** is set to `true`. For custom tables, this property is set to `true` by default.  
  
<a name="bkmk_enable"></a>   
## Enable optimistic concurrency  
 You can enable optimistic concurrency checking behavior when executing an <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> by setting the <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest.ConcurrencyBehavior> property of the request to <xref:Microsoft.Xrm.Sdk.ConcurrencyBehavior.IfRowVersionMatches>. Similarly, for a <xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest>, you would set the <xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest.ConcurrencyBehavior> property.  
  
 When using the SDK for .NET context to make data changes, set <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceContext.ConcurrencyBehavior> on the <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceContext> object. This value passes through to all of the **UpdateRequest** and **DeleteRequest** messages used by the **OrganizationServiceContext** when <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceContext.SaveChanges> is called.  
  
 You can only set optimistic concurrency behavior through an SDK API call. There's currently no setting for it in a form of the web application.  
  
## Apply optimistic concurrency using Web API

For information about using Web API to apply optimistic concurrency, see [Apply optimistic concurrency](webapi/perform-conditional-operations-using-web-api.md#apply-optimistic-concurrency).


## Apply optimistic concurrency using SDK for .NET

For information about using SDK for .NET to apply optimistic concurrency, see [Optimistic concurrency behavior](org-service/entity-operations-update-delete.md#optimistic-concurrency-behavior).
  
<a name="bkmk_handle"></a>   
## Handle exceptions  
 When you use optimistic concurrency, the Web service call can return several error conditions in a fault exception <<xref:Microsoft.Xrm.Sdk.OrganizationServiceFault>>.  
  
- **ConcurrencyVersionMismatch** (code=-2147088254)  
  
     You get this error when you provide a row version and specify the **IfVersionMatches** behavior, but the existing record’s version doesn’t match the row version in your request.  
  
- **ConcurrencyVersionNotProvided** (code= -2147088253)  
  
     You get this error when you specify the **IfVersionMatches** behavior but don’t provide a value for the row version.  
  
- **OptimisticConcurrencyNotEnabled** (code=-2147088243)  
  
     You get this error when you specify the **IfVersionMatches** behavior on an update to a table, but optimistic concurrency isn’t enabled.  
  
  Check the [Code](/dotnet/api/system.servicemodel.faultexception.code) property of the returned fault to see if the fault is related to optimistic concurrency. The codes for these error conditions come from the `ErrorCodes.cs` helper code.  
 


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
