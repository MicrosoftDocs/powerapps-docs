---
title: "Web API Query schema definitions and detect changes sample (C#)"
description: "This sample demonstrates the use of the RetrieveMetadataChanges Function using the Dataverse Web API to query schema definitions and detect changes so that you can create a persistent cache."
ms.date: 10/12/2022
author: mkannapiran
ms.author: kamanick
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---

# Web API Query schema definitions and detect changes sample (C#)

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

This sample shows how to retrieve and detect changes in table definitions using the [RetrieveMetadataChanges Action](xref:Microsoft.Dynamics.CRM.RetrieveMetadataChanges). 

You can view the sample at [PowerApps-Samples/dataverse/webapi/C#-NETCore/Schema/RetrieveMetadataChanges/](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/CSharp-NETx/RetrieveMetadataChanges)

See these articles for explanation of functionality:

- [Query schema definitions](../../query-schema-definitions.md)
- [Cache Schema data](../../cache-schema-data.md)

This sample uses the common helper code in the [WebAPIService class library (C#)](webapiservice.md).

## Prerequisites

The following prerequisites are required to build and run this sample:

- Microsoft Visual Studio 2022.
- Access to Dataverse with privileges to perform data operations.
  
<a name="bkmk_runSample"></a>
  
## How to run this sample

1. Clone or download the [PowerApps-Samples](https://github.com/microsoft/PowerApps-Samples) repository.
1. Locate the [/dataverse/webapi/C#-NETx/RetrieveMetadataChanges/](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/CSharp-NETx/RetrieveMetadataChanges) folder.
1. Open the `RetrieveMetadataChanges.sln` file using Visual Studio 2022
1. Edit the `appsettings.json` file to set the following property values:

   |Property|Instructions  |
   |---------|---------|
   |`Url`|The Url for your environment. Replace the placeholder `https://yourorg.api.crm.dynamics.com` value with the value for your environment. See [View developer resources](../../view-download-developer-resources.md) to find the Url for your environment. |
   |`UserPrincipalName`|Replace the placeholder `you@yourorg.onmicrosoft.com` value with the UPN value you use to access the environment.|
   |`Password`|Replace the placeholder `yourPassword` value with the password you use.|

1. Save the `appsettings.json` file
1. Press <kbd>F5</kbd> to run the sample.

## Code

The code for this sample is here: [PowerApps-Samples/dataverse/webapi/C#-NETx/RetrieveMetadataChanges/Program.cs](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/CSharp-NETx/RetrieveMetadataChanges/Program.cs)

## Demonstrates

This sample shows how to retrieve schema definitions for a specific set of column definitions and save them (in memory) to represent a cache.

Then it creates a new column, retrieves the data for only that new column, which it adds to the cache.

Then it deletes the column, retrieves data about deleted items and uses it to remove the deleted column definition from the cache.

This sample has six sections:

### Define query

Define a query using [EntityQueryExpression](xref:Microsoft.Dynamics.CRM.EntityQueryExpression) that returns all the Picklist choice columns from the contact table.

### Initialize cache

1. Create an instance of [RetrieveMetadataChanges](xref:Microsoft.Dynamics.CRM.RetrieveMetadataChanges) with the `Query` parameter set to the query.
1. Send the request and get a [RetrieveMetadataChangesResponse](xref:Microsoft.Dynamics.CRM.RetrieveMetadataChangesResponse).
1. Cache the `RetrieveMetadataChangesResponse.EntityMetadata` value.
1. Save the `RetrieveMetadataChangesResponse.ServerVersionStamp` value for use in the next request.
1. Write a list of all the current columns in the cache.

### Add choice column

Create a new choice column by creating a new [PicklistAttributeMetadata](xref:Microsoft.Dynamics.CRM.PicklistAttributeMetadata) instance in the contact table.

### Detect added column


1. Create a new instance of [RetrieveMetadataChanges](xref:Microsoft.Dynamics.CRM.RetrieveMetadataChanges) with the `Query` parameter set to the original query.
1. Set the `RetrieveMetadataChangesRequest.ClientVersionStamp` with the value previously returned from the first request.
1. Send the request and get a [RetrieveMetadataChangesResponse](xref:Microsoft.Dynamics.CRM.RetrieveMetadataChangesResponse).
1. Verify that only one new column definition was returned to represent the choice column that was created.
1. Save the `RetrieveMetadataChangesResponse.ServerVersionStamp` value for use in the next request.
1. Add that choice column data to the cache.

### Delete choice column

Delete the choice column created earlier.

### Detect deleted column

1. Create a new instance of [RetrieveMetadataChanges](xref:Microsoft.Dynamics.CRM.RetrieveMetadataChanges) with the `Query` parameter set to the original query.
1. Set the `RetrieveMetadataChangesRequest.ClientVersionStamp` with the value previously returned from the second request.
1. Set the `RetrieveMetadataChangesRequest.DeletedMetadataFilters` to `DeletedMetadataFilters.Attribute` because we're looking for deleted column definitions.
1. Send the request and get a [RetrieveMetadataChangesResponse](xref:Microsoft.Dynamics.CRM.RetrieveMetadataChangesResponse).
1. Find the ID of the deleted choice column in the `RetrieveMetadataChangesResponse.DeletedMetadata`, using `DeletedMetadataFilters.Attribute` as an index value for the collection.
1. Remove the column definition from the cache.
1. Write a list of all the current columns in the cache.

## Clean up

No clean-up is required because all data created by this sample was deleted.

### See also

[Query Schema Definitions](../../query-schema-definitions.md)<br />
[Cache Schema data](../../cache-schema-data.md)<br />
[Use the Dataverse Web API](../overview.md)<br />
[WebAPIService class library (C#)](webapiservice.md)<br />
[Web API table schema operations sample (C#)](webapiservice-metadata-operations.md)<br />

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
