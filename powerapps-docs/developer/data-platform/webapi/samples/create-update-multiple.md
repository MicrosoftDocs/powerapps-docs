---
title: "Sample: Web API Use bulk operations" 
description: "This sample shows how to perform bulk create and update operations using the Web API CreateMultiple and UpdateMultiple actions. The messages for these actions are optimized to provide the most performant way to create or update records with Dataverse."
ms.date: 02/08/2024
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
search.audienceType:
  - developer
search.app:
  - PowerApps
  - D365CE
contributors:
  - JimDaly
---

# Sample: Web API Use bulk operations

These sample applications on GitHub show how to perform bulk create and update operations using the Web API [CreateMultiple](xref:Microsoft.Dynamics.CRM.CreateMultiple), [UpdateMultiple](xref:Microsoft.Dynamics.CRM.UpdateMultiple) and [UpsertMultiple](xref:Microsoft.Dynamics.CRM.UpsertMultiple) actions. The messages for these actions are optimized to provide the most performant way to create or update records with Dataverse.

> [!div class="nextstepaction"]
> [View this sample on Github](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/CSharp-NETx/BulkOperations/README.md)

This sample is a Visual Studio .NET 6.0 solution that contains:

- Two projects that perform the same [CreateMultiple](xref:Microsoft.Dynamics.CRM.CreateMultiple) and [UpdateMultiple](xref:Microsoft.Dynamics.CRM.UpdateMultiple) operations in different ways so that you can compare the performance of each method.
- One project that demonstrates using the [UpsertMultiple](xref:Microsoft.Dynamics.CRM.UpsertMultiple) action.

See the README.md file in each sample for detailed instructions about how to run the sample and what it does.

### See Also

[Bulk Operation messages](../../bulk-operations.md)   
[Sample: SDK for .NET Use bulk operations](../../org-service/samples/create-update-multiple.md)   
[Write plug-ins for CreateMultiple and UpdateMultiple](../../write-plugin-multiple-operation.md)   
[Sample: CreateMultiple and UpdateMultiple plug-ins](../../org-service/samples/createmultiple-updatemultiple-plugin.md)

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]
