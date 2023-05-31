---
title: "Elastic table sample code (preview) (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about the sample code available on GitHub for elastic table operations and the ExecuteCosmosSqlQuery message." # 115-145 characters including spaces. This abstract displays in the search result.
ms.topic: article
ms.date: 05/30/2023
author: pnghub
ms.author: gned
ms.reviewer: jdaly
contributors:
 - sumantb-msft
 - JimDaly
---
# Elastic table sample code (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

The following sample applications on GitHub demonstrate how to work with elastic tables using code. See the README.md file in each sample for detailed instructions about how to run the sample and what it does.

## [SDK for .NET](#tab/sdk)

- Create elastic tables using code.
- Create, retrieve, update, upsert, and delete elastic table records.
- Use the <xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest> and <xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest> classes to perform bulk operations with elastic table records.
- Set JSON data for a column.
- Use the `ExecuteCosmosSqlQuery` message.
- Use the `DeleteMultiple` message to delete elastic table record in bulk.

> [!div class="nextstepaction"]
> [SDK for .NET elastic tables sample](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/orgsvc/C%23-NETCore/ElasticTableOperations/README.md)


## [Web API](#tab/webapi)

- Create elastic tables using code.
- Create, retrieve, update, upsert, and delete elastic table records.
- Set JSON data for a column.
- Use `$batch` to create elastic tables in bulk.
- Use the [ExecuteCosmosSqlQuery Function](xref:Microsoft.Dynamics.CRM.ExecuteCosmosSqlQuery) to query JSON data in columns.


> [!div class="nextstepaction"]
> [Web API elastic tables sample](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/C%23-NETx/ElasticTableOperations/README.md)

---

## See also

[Elastic tables (preview)](elastic-tables.md)<br />
[Create elastic tables using code (preview)](create-elastic-tables.md)<br />
[Use elastic tables using code (preview)](use-elastic-tables.md)<br />
[Query JSON columns in elastic tables (preview)](query-json-columns-elastic-tables.md)<br />
[Bulk operations with elastic tables (preview)](bulk-operations-elastic-tables.md)
