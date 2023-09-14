---
title: Elastic table sample code (preview)
description: Learn about the sample code that is available on GitHub for Dataverse elastic table operations and the ExecuteCosmosSqlQuery message.
ms.topic: article
ms.date: 07/21/2023
author: pnghub
ms.author: gned
ms.reviewer: jdaly
contributors:
 - sumantb-msft
 - JimDaly
---
# Elastic table sample code (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

The following sample applications on GitHub show how to use code to work with elastic tables. For detailed information about what each sample does and instructions for running it, read the *README.md* file in the sample.

## [SDK for .NET](#tab/sdk)

- Create elastic tables by using code.
- Create, retrieve, update, upsert, and delete elastic table records.
- Use the [CreateMultipleRequest class](xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest) and the [UpdateMultipleRequest class](xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest) to perform bulk operations with elastic table records.
- Set JavaScript Object Notation (JSON) data for a column.
- Use the `ExecuteCosmosSqlQuery` message.
- Use the `DeleteMultiple` message with the [OrganizationRequest class](xref:Microsoft.Xrm.Sdk.OrganizationRequest) to delete elastic table records in bulk.

> [!div class="nextstepaction"]
> [SDK for .NET elastic tables sample](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/orgsvc/C%23-NETCore/ElasticTableOperations/README.md)

## [Web API](#tab/webapi)

- Create elastic tables by using code.
- Create, retrieve, update, upsert, and delete elastic table records.
- Use the [CreateMultiple action](xref:Microsoft.Dynamics.CRM.CreateMultiple) to create elastic table records.
- Use the [UpdateMultiple action](xref:Microsoft.Dynamics.CRM.UpdateMultiple) to set JSON data for a column.
- Use the [ExecuteCosmosSqlQuery function](xref:Microsoft.Dynamics.CRM.ExecuteCosmosSqlQuery) to query JSON data in columns.
- Use the `DeleteMultiple` action to delete elastic table records in bulk.<!--TODO Add link -->

> [!div class="nextstepaction"]
> [Web API elastic tables sample](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/C%23-NETx/ElasticTableOperations/README.md)

---

### See also

[Elastic tables for developers (preview)](elastic-tables.md)  
[Create elastic tables using code (preview)](create-elastic-tables.md)  
[Use elastic tables using code (preview)](use-elastic-tables.md)  
[Query JSON columns in elastic tables (preview)](query-json-columns-elastic-tables.md)  
[Bulk operation messages (preview)](bulk-operations.md)
