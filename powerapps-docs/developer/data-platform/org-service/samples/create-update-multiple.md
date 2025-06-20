---
title: "Sample: SDK for .NET Use bulk operations (Microsoft Dataverse) | Microsoft Docs"
description: "This sample shows how to perform bulk create and update operations using several different approaches including the use of CreateMultipleRequest and UpdateMultipleRequest classes. The messages for these request classes are optimized to provide the most performant way to create or update records with Dataverse."
ms.date: 06/01/2023
author: MsSQLGirl
ms.author: sriknair
ms.reviewer: jdaly
ms.topic: sample
search.audienceType:
  - developer
search.app:
  - PowerApps
  - D365CE
contributors:
  - JimDaly
  - phecke
---

# Sample: SDK for .NET Use bulk operations

These sample applications on GitHub show how to perform bulk create and update operations using several different approaches including the use of [CreateMultipleRequest](xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest) and [UpdateMultipleRequest](xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest) classes. The messages for these request classes are optimized to provide the most performant way to create or update records with Dataverse.

This sample is a Visual Studio .NET 6.0 solution that contains five different projects that perform the same operations in different ways so that you can compare the performance of each method.

> [!NOTE]
> This solution also contains an [UpsertMultiple project](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/orgsvc/CSharp-NETCore/BulkOperations/UpsertMultiple/README.md) that demonstrates the use of the [UpsertMultipleRequest class](xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest)

See the README.md file in each sample for detailed instructions about how to run the sample and what it does.

> [!div class="nextstepaction"]
> [SDK for .NET bulk operations sample](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/orgsvc/CSharp-NETCore/BulkOperations/README.md)

### See Also

[Bulk Operation messages](../../bulk-operations.md)   
[Write plug-ins for CreateMultiple and UpdateMultiple](../../write-plugin-multiple-operation.md)   
[Sample: CreateMultiple and UpdateMultiple plug-ins](createmultiple-updatemultiple-plugin.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
