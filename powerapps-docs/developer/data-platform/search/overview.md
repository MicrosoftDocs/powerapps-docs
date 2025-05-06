---
title: "Search for Dataverse records (Microsoft Dataverse) | Microsoft Docs"
description: "Use Dataverse search to return search results across multiple tables and provide suggestions and autocompletion experiences in apps." 
ms.date: 10/20/2023
ms.reviewer: jdaly
ms.topic: article
author: seanwat-msft
ms.author: seanwat
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
 - JimDaly
 - jeromeblouinms
---
# Search for Dataverse records

Dataverse search delivers fast and comprehensive search results across multiple tables, in a single list, sorted by relevance. It also provides capabilities to support suggestions and autocompletion experiences in apps.

> [!NOTE]
> This documentation for developers will describe how to programmatically interact with the Dataverse Search APIs.
> 
> See the following topics for information about the user experience and how to configure Dataverse Search for your environment:
> 
> - [What is Dataverse search?](../../../user/relevance-search-benefits.md)
> - [Configure Dataverse search for your environment](/power-platform/admin/configure-relevance-search-organization)

## How to use

Developers can use the search APIs three different ways:

- The Dataverse SDK for .NET
- The Web API `/api/data/v9.x` endpoint
- The native search `/api/search/v2.0/` endpoint

### [SDK for .NET](#tab/sdk)

Search operations are defined as Dataverse messages using [Custom APIs](../custom-api.md). For .NET projects, you can use the SDK for .NET.

There are currently no classes included in the SDK to use these operations. For .NET Framework projects, you can use the Power Platform CLI [pac modelbuilder build](/power-platform/developer/cli/reference/modelbuilder#pac-modelbuilder-build) to generate `*Request` and `*Response` classes for these messages just as you would for any custom action.

You can also use the [OrganizationRequest](xref:Microsoft.Xrm.Sdk.OrganizationRequest) and [OrganizationResponse](xref:Microsoft.Xrm.Sdk.OrganizationResponse) classes.

More information:

- [Generate early-bound classes for the SDK for .NET](../org-service/generate-early-bound-classes.md)
- [Use messages with the SDK for .NET](../org-service/use-messages.md)

### [Web API](#tab/webapi)

Search operations exposed with Web API are OData actions or functions described in the [CSDL $metadata document](../webapi/web-api-service-documents.md#csdl-metadata-document).

More information:

- [Use Web API actions](../webapi/use-web-api-actions.md)
- [Use Web API functions](../webapi/use-web-api-functions.md)

### [Search 2.0 endpoint](#tab/search)

The native search 2.0 endpoint isn't an OData service and has no service document. The native search 2.0 endpoint accepts the same parameters and returns the same responses as the corresponding Web API Actions and functions.

The [Dataverse legacy search](legacy.md) using `/api/search/v1.0/` hasn't been deprecated and continues to be supported.

---


## Search operations

Search provides three operations to support a user interface that enables searching for data.

|SDK Message Name<br />Web API Action<br />Search 2.0 Endpoint|Description|
|---------|---------|
|`searchquery`<br />[searchquery Action](xref:Microsoft.Dynamics.CRM.searchquery)<br />`/api/search/v2.0/query`| Returns a search results page. <br /> See [Dataverse Search query](query.md)|
|`searchsuggest`<br />[searchsuggest Action](xref:Microsoft.Dynamics.CRM.searchsuggest)<br />`/api/search/v2.0/suggest`|Provide suggestions as the user enters text into a form field. <br /> See [Dataverse Search suggest](suggest.md)|
|`searchautocomplete`<br />[searchautocomplete Action](xref:Microsoft.Dynamics.CRM.searchautocomplete)<br />`/api/search/v2.0/autocomplete`| Provide autocompletion of input as the user enters text into a form field.<br /> See [Dataverse Search autocomplete](autocomplete.md)|

There are also two operations you can use to understand whether search is enabled and how it's configured.

|SDK Message Name<br />Web API Function<br />Search 2.0 Endpoint|Description|
|---------|---------|
|`searchstatistics`<br />[searchstatistics Function](xref:Microsoft.Dynamics.CRM.searchstatistics)<br />`/api/search/v2.0/statistics`|Provides organization storage size and document count.<br /> See [Dataverse Search statistics](statistics-status.md#statistics)|
|`searchstatus`<br />[searchstatus Function](xref:Microsoft.Dynamics.CRM.searchstatus)<br />`/api/search/v2.0/status`|Search status of an Organization.<br /> See [Dataverse Search Status](statistics-status.md#status) |

## Use Insomnia with Dataverse search

If you have used Insomnia with Dataverse Web API, you know how useful it's to try using the APIs. We have some instructions about setting up a Insomnia environment to authenticate with the Dataverse Web API here: [Use Insomnia with Dataverse Web API](../webapi/insomnia.md)

You can use the same instructions with the search operations using Web API functions and actions. If you want to use the native search 2.0 endpoint, change these two environment variables:

|Variable|Web API Value|Search 2.0 Endpoint value|
|---------|---------|---------|
|`version`|`9.2`|`2.0`|
|`webapiurl`|`{{url}}/api/data/v{{version}}/`|`{{url}}/api/search/v{{version}}/`|


## Detect if search is enabled

Dataverse search is enabled by default for production environments, but it's an opt-out feature so it could be turned off even in a production environment. If you're using an environment other than a production environment, an administrator must enable it. [Learn how to enable search in the admin center](/power-platform/admin/configure-relevance-search-organization#enable-dataverse-search).

### Error when search not enabled

If you use the query, suggest, or autocomplete operations when the environment isn't enabled you'll get these errors:

#### [SDK for .NET](#tab/sdk)

> ErrorCode: `-2147185397`
> Message: `Dataverse Search feature is disabled for this organization.`

#### [Web API](#tab/webapi)

**Response**

```http
HTTP/1.1 400 Bad Request
{"error":{"code":"0x80048d0b","message":"Dataverse Search feature is disabled for this organization."}}
```

#### [Search 2.0 endpoint](#tab/search)

**Response**

```http
HTTP/1.1 400 Bad Request
{"error":{"code":"0x80048d0b","message":"Dataverse Search feature is disabled for this organization."}}
```

---

You can detect whether the search service is enabled by checking the settings in the organization table or by using the [Dataverse Search Status](statistics-status.md#status) operation.

### Check Organization table

The [Organization table](../reference/entities/organization.md) contains a single row of data that controls how the organization is configured. The [IsExternalSearchIndexEnabled](../reference/entities/organization.md#BKMK_IsExternalSearchIndexEnabled) boolean column tells you whether search is enabled for the organization.

#### [SDK for .NET](#tab/sdk)

This function returns the `IsExternalSearchIndexEnabled` property value for the organization.

```csharp
static bool IsExternalSearchIndexEnabled(IOrganizationService service) {

    QueryExpression query = new QueryExpression("organization") { 
        ColumnSet = new ColumnSet("isexternalsearchindexenabled")
    };

    EntityCollection organizations = service.RetrieveMultiple(query);
    return (bool)organizations.Entities.FirstOrDefault()["isexternalsearchindexenabled"];
}
```

More information: [Build queries with QueryExpression](../org-service/queryexpression/overview.md)

#### [Web API](#tab/webapi)

This Web API query returns the `IsExternalSearchIndexEnabled` property value for the organization.

**Request**

```http
GET [Organization URI]/api/data/v9.2/organizations?$select=isexternalsearchindexenabled HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response**

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0

{
   "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#organizations(isexternalsearchindexenabled)",
   "value": [
      {
         "@odata.etag": "W/\"73925407\"",
         "isexternalsearchindexenabled": true,
         "organizationid": "00aa00aa-bb11-cc22-dd33-44ee44ee44ee"
      }
   ]
}
```

More information: [Query data using the Web API](../webapi/query/overview.md)

#### [Search 2.0 endpoint](#tab/search)

You must use the SDK for .NET or Web API to check this setting.

---

## Enable tables and columns for search

Which tables and columns are enabled for search is controlled by data in Dataverse.

### Enable Tables

Only those tables where the [EntityMetadata.CanEnableSyncToExternalSearchIndex.Value property](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.CanEnableSyncToExternalSearchIndex) and [EntityMetadata.ChangeTrackingEnabled property](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.ChangeTrackingEnabled) are true can be enabled for Dataverse search. If the `CanEnableSyncToExternalSearchIndex.CanBeChanged` value is false, you can't change the value. More information: [Managed properties](/power-platform/alm/managed-properties-alm)

To enable a table for Dataverse Search, set the [EntityMetadata.SyncToExternalSearchIndex property](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.SyncToExternalSearchIndex) to `true`.

You can check the values for a table with the SDK or Web API using the table logical name. Replace `account` in the following queries  with the logical name of the table you want to check.

#### [SDK for .NET](#tab/sdk)

```csharp
static void RetrieveSearchSettingsForTable(IOrganizationService service, string logicalName = "account") {

    RetrieveMetadataChangesRequest request = new RetrieveMetadataChangesRequest() { 
            Query = new EntityQueryExpression() { 
                Properties = new MetadataPropertiesExpression(
                    "CanEnableSyncToExternalSearchIndex", 
                    "SyncToExternalSearchIndex")
            }
    };
    request.Query.Criteria.Conditions.Add(
        new MetadataConditionExpression(
            propertyName: "LogicalName", 
            conditionOperator: MetadataConditionOperator.Equals, 
            value: logicalName));

    var response = (RetrieveMetadataChangesResponse)service.Execute(request);

    EntityMetadata table = response.EntityMetadata.FirstOrDefault();

    Console.WriteLine($"CanEnableSyncToExternalSearchIndex: {table.CanEnableSyncToExternalSearchIndex.Value}");
    Console.WriteLine($"SyncToExternalSearchIndex: {table.SyncToExternalSearchIndex}");
}
```

**Output**

```
CanEnableSyncToExternalSearchIndex: True
SyncToExternalSearchIndex: True
```

More information:

- [Query schema definitions](../query-schema-definitions.md)
- [Retrieve, update, and delete tables](../org-service/metadata-retrieve-update-delete-entities.md)


#### [Web API](#tab/webapi)

**Request**

```http
GET [Organization URI]/api/data/v9.2/EntityDefinitions(LogicalName='account')?$select=CanEnableSyncToExternalSearchIndex,SyncToExternalSearchIndex HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response**

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0

{
   "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#EntityDefinitions(CanEnableSyncToExternalSearchIndex,SyncToExternalSearchIndex)/$entity",
   "SyncToExternalSearchIndex": true,
   "MetadataId": "70816501-edb9-4740-a16c-6a5efbc05d84",
   "CanEnableSyncToExternalSearchIndex": {
      "Value": true,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "canenablesynctoexternalsearchindex"
   }
}
```

More information:

- [Query table definitions using the Web API](../webapi/query-metadata-web-api.md)
- [Query schema definitions](../query-schema-definitions.md)
- [Create and update table definitions using the Web API](../webapi/create-update-entity-definitions-using-web-api.md)

#### [Search 2.0 endpoint](#tab/search)

You must use the SDK for .NET or Web API to check this setting.

---

More information:

- [Select tables for Dataverse search](/power-platform/admin/configure-relevance-search-organization#select-tables-for-dataverse-search)
- [Set managed properties for Dataverse search](/power-platform/admin/configure-relevance-search-organization#set-managed-properties-for-dataverse-search)

### Enable Columns

The columns that are searchable for the table are determined by whether they're included in the Quick Find view for each table. You can query the definition of the view in the [View (SavedQuery) table](../reference/entities/savedquery.md) and update it programmatically.

More information:

- [Select searchable fields and filters for each table](/power-platform/admin/configure-relevance-search-organization#select-searchable-fields-and-filters-for-each-table)
- [Customize views](../../model-driven-apps/customize-entity-views.md)

## Service Protection Limits

The common Dataverse [Service protection API limits](../api-limits.md) will never be approached because Dataverse search applies a lower limit. The way you manage them is the same.

Dataverse search allows a user to send one request per second, and each organization is limited to 150 requests per minute. If you exceed this limit, a [429 Too Many Requests](https://developer.mozilla.org/docs/Web/HTTP/Status/429) error is returned. If a `429` error is returned, you should wait until the period defined in the `Retry-After` response header value has passed before sending more requests. The value represents the number of seconds to wait.


### See also

[Dataverse Search query](query.md)   
[Dataverse Search suggest](suggest.md)   
[Dataverse Search autocomplete](autocomplete.md)   
[Dataverse Search statistics and status](statistics-status.md)   
[Dataverse legacy search](legacy.md)   
[Configure Dataverse search for your environment](/power-platform/admin/configure-relevance-search-organization)


[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]
