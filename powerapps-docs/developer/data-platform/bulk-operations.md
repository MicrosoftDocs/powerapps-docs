---
title: Bulk Operation messages (preview)
description: Learn how to use special APIs to perform operations on multiple rows of data. These API provide performance benefits compared to other options. 
ms.date: 04/03/2022
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
ms.topic: conceptual
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
---
# Bulk Operation messages (preview)

Use the following bulk operations messages get the best performance when performing data operations on multiple rows of data, but pay special attention to the [Limitations](#limitations):

|Message |Details|
|---------|---------|
|`CreateMultiple`|Use the SDK [CreateMultipleRequest class](xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest) or the Web API `CreateMultiple` action to create multiple records of the same type in a single request.|
|`UpdateMultiple`|Use the SDK [UpdateMultipleRequest class](xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest) or the Web API `UpdateMultiple` action to update multiple records of the same type in a single request.|
|`UpsertMultiple`|*Coming soon*|
|`DeleteMultiple`|For elastic tables only, use the SDK [OrganizationRequest class](xref:Microsoft.Xrm.Sdk.OrganizationRequest) to delete multiple records of the same type. More information: [Use DeleteMultiple with elastic tables](bulk-operations-elastic-tables.md#use-deletemultiple-with-elastic-tables).<br />**Note**:This message is not recommended for use with standard tables. For standard tables, use the SDK [BulkDeleteRequest class](xref:Microsoft.Crm.Sdk.Messages.BulkDeleteRequest) or the Web API [BulkDelete action](xref:Microsoft.Dynamics.CRM.BulkDelete).|

## Standard and Elastic table usage

Both standard and elastic tables see significant performance benefits when using these bulk operation messages you need to use them differently.

:::row:::
    :::column:::
      **Standard tables**
      
      With standard tables you gain greater efficiency by sending more operations with each request.
    :::column-end:::
    :::column:::
      **Elastic tables**
      
      With elastic tables, we recommend you send 100 operations in each request.
    :::column-end:::
:::row-end:::

Both stanard and elastic tables see greater throughput when using bulk operations requests sent in parallel. More information: [Send parallel requests](send-parallel-requests.md)



## Performance improvements for standard tables

## Limitations
