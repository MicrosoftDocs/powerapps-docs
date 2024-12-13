---
title: "Sample: Query schema definitions and detect changes (Microsoft Dataverse) | Microsoft Docs"
description: "This sample shows how to query schema definitions and detect definitions changes over time so you can maintain a persistent cache."
ms.date: 10/24/2022
author: mkannapiran
ms.author: kamanick
ms.reviewer: jdaly
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Query schema definitions and detect changes

This sample shows how to retrieve and detect changes in table definitions using [RetrieveMetadataChangeRequest](/dotnet/api/microsoft.xrm.sdk.messages.retrievemetadatachangesrequest) method. You can view the sample at [PowerApps-Samples/dataverse/orgsvc/C#-NETCore/Schema/RetrieveMetadataChanges/](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp-NETCore/Schema/RetrieveMetadataChanges)

See these topics for explaination of functionality:

- [Query schema definitions](../../query-schema-definitions.md)
- [Cache Schema data](../../cache-schema-data.md)

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

## How to run this sample

See the instructions here: [Schema samples instructions](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/orgsvc/CSharp-NETCore/Schema/README.md#instructions)

## Demonstrates

This sample shows how to retrieve schema definitions for a specific set of column definitions and save them (in memory) to represent a cache.

Then it creates a new column, retrieves the data for only that new column, which it adds to the cache.

Then it deletes the column, retrieves data about deleted items and uses it to remove the deleted column definition from the cache.

This sample has 6 sections:

### Define query

Define a query using [EntityQueryExpression](xref:Microsoft.Xrm.Sdk.Metadata.Query.EntityQueryExpression) that will return all the Picklist choice columns from the contact table.

### Initialize cache

1. Create an instance of [RetrieveMetadataChangesRequest](xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest) with the [Query](xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest.Query) parameter set to the query.
1. Send the request using [IOrganizationService.Execute](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A).
1. Cache the [RetrieveMetadataChangesResponse.EntityMetadata](xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesResponse.EntityMetadata) value.
1. Save the [RetrieveMetadataChangesResponse.ServerVersionStamp](xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesResponse.ServerVersionStamp) value for use in the next request.
1. Write a list of all the current columns in the cache.

### Add choice column

Create a new choice column by creating a new [PicklistAttributeMetadata](xref:Microsoft.Xrm.Sdk.Metadata.PicklistAttributeMetadata) instance in the contact table attributes.

### Detect added column

1. Create a new instance of [RetrieveMetadataChangesRequest](xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest) with the [Query](xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest.Query) parameter set to the original query.
1. Set the [RetrieveMetadataChangesRequest.ClientVersionStamp](xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest.ClientVersionStamp) with the value previously returned from the first request.
1. Send the request using [IOrganizationService.Execute](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A).
1. Verify that only one new column definition was returned to represent the choice column that was created.
1. Save the [RetrieveMetadataChangesResponse.ServerVersionStamp](xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesResponse.ServerVersionStamp) value for use in the next request.
1. Add that choice column data to the cache.

### Delete choice column

Delete the choice column created earlier.

### Detect deleted column

1. Create a new instance of [RetrieveMetadataChangesRequest](xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest) with the [Query](xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest.Query) parameter set to the original query.
1. Set the [RetrieveMetadataChangesRequest.ClientVersionStamp](xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest.ClientVersionStamp) with the value previously returned from the second request.
1. Set the [RetrieveMetadataChangesRequest.DeletedMetadataFilters](xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest.DeletedMetadataFilters) to [DeletedMetadataFilters.Attribute](xref:Microsoft.Xrm.Sdk.Metadata.Query.DeletedMetadataFilters.Attribute) because we are only looking for deleted column definitions.
1. Send the request using [IOrganizationService.Execute](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A).
1. Find the Id of the deleted choice column in the [RetrieveMetadataChangesResponse.DeletedMetadata](xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesResponse.DeletedMetadata), using [DeletedMetadataFilters.Attribute](xref:Microsoft.Xrm.Sdk.Metadata.Query.DeletedMetadataFilters.Attribute) as an index value for the collection.
1. Remove the column definition from the cache.
1. Write a list of all the current columns in the cache.

## Clean up

No clean up is required because all data created by this sample was deleted.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
