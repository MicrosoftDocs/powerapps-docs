---
title: "Use CreateMultiple and UpdateMultiple (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "You can use the CreateMultiple and UpdateMultiple messages to optimize bulk data operations." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 12/12/2022
author: divka78
ms.author: dikamath
ms.reviewer: jdaly
ms.topic: article
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
 - JimDaly
 - phecke
---

# Use CreateMultiple and UpdateMultiple (Preview)

Use the [CreateMultipleRequest](/dotnet/api/microsoft.xrm.sdk.messages.createmultiplerequest) and [UpdateMultipleRequest](/dotnet/api/microsoft.xrm.sdk.messages.updatemultiplerequest) classes to create or update records in bulk much faster than any other method.

The `CreateMultiple` and `UpdateMultiple` messages are unique because they are optimized for performance when performing the same operation on the same table. Performance is greatly improved because these messages apply all the operations in a single transaction rather than as separate operations on individual rows. This design also enables the opportunity to improve performance by writing plug-ins that respond to these messages more efficiently than plug-ins that respond to individual `Create` and `Update` events.

## CreateMultiple

## UpdateMultiple

## Plug-ins and other event handlers

When `CreateMultiple` and `UpdateMultiple` messages are used the respective `Create` and `Update` events occur for each item in the `Targets` parameter. This means that any existing plug-ins or other event handlers for the `Create` and `Update` events will continue to work as they always have. You are not required to write new plug-ins to manage events raised by these messages.

When `Create` and `Update` messages are used the respective `CreateMultiple` and `UpdateMultiple` events occur with a single entity passed in the `Targets` parameter. This means that you can move any existing logic that currently responds to individual `Create` and `Update` events to the more efficient `CreateMultiple` and `UpdateMultiple` events.

## Limitations

### Limited to certain tables

Currently, `CreateMultiple` and `UpdateMultiple` messages are limited to those tables which have been created recently. You can use these messages on a new custom table you create. Eventually, these messages will be enabled for all tables that support individual `Create` and `Update` messages.

### No continue on error

The `ExecuteMultiple` message supports the option that will continue processing requests even when one or more requests fail. Due to the fact that `CreateMultiple` and `UpdateMultiple` messages achieve performance improvements by unifying all operations in a single transaction, it isn't possible to support the continue on error behaviors.

You should use `CreateMultiple` and `UpdateMultiple` messages when you have a high degree of confidence that all the operations will succeed. You may want to use a strategy that will allow the set of operations to fall back to use `ExecuteMultiple` when `CreateMultiple` and `UpdateMultiple` messages fail.

### .NET SDK only

Currently the `CreateMultiple` and `UpdateMultiple` messages are only available to be used with the .NET SDK. The capability to use these operations using Web API is coming soon.


### See Also

[Use messages with the Organization service](use-messages.md)<br />
[Use ExecuteTransaction](use-executetransaction.md)<br />
[Execute multiple requests using the Organization service](execute-multiple-requests.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]