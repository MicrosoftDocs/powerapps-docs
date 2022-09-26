---
title: "Search for Dataverse records (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Use Dataverse search to return search results across multiple tables and provide suggestions and autocompletion experiences in apps." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 09/12/2022
ms.reviewer: jdaly
ms.topic: article
author: mspilde # GitHub ID
ms.author: mspilde # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
 - JimDaly
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

### SDK for .NET

Search operations are defined as Dataverse messages using [Custom APIs](../custom-api.md). For .NET projects they can also be used with the SDK for .NET.

There are currently no classes included in the SDK to use these operations. For .NET Framework projects you can use the `CrmSvcUtil` command line code generation tool with the `/generateactions` parameter to generate `*Request` and `*Response` classes for these messages just as you would for any custom action.

You can also use the <xref:Microsoft.Xrm.Sdk.OrganizationRequest?text=OrganizationRequest> and <xref:Microsoft.Xrm.Sdk.OrganizationResponse?text=OrganizationResponse> classes.

More information:

- [Generate early-bound classes for the Organization service](../org-service/generate-early-bound-classes.md)
- [Use messages with the Organization service](../org-service/use-messages.md)
- [Invoking Custom APIs](../custom-api.md#invoking-custom-apis)

### Web API

Search operations exposed with Web API are OData actions or functions described in the [CSDL $metadata document](../webapi/web-api-service-documents.md#csdl-metadata-document). You can use these in the same way you use other Web API operations.

More information:

- [Use Web API actions](../webapi/use-web-api-actions.md)
- [Use Web API functions](../webapi/use-web-api-functions.md)

### Native search 2.0

The native search 2.0 endpoint is not an OData service and has no service document. The native search 2.0 endpoint accepts the same parameters and returns the same responses as the corresponding Web API Actions and functions.

The [Dataverse native search 1.0](search1.0.md) has not been deprecated and continues to be supported.

## Search operations

Search provides three operations to support a user interface that enables searching for data.

|SDK Message Name<br />Web API Action<br />Search 2.0 Endpoint|Description|
|---------|---------|
|`searchquery`<br /><xref:Microsoft.Dynamics.CRM.searchquery?text=searchquery Action><br />`/api/search/v2.0/query`| Returns a search results page. <br /> See [Dataverse Search query](query.md)|
|`searchsuggest`<br /><xref:Microsoft.Dynamics.CRM.searchsuggest?text=searchsuggest Action><br />`/api/search/v2.0/suggest`|Provide suggestions as the user enters text into a form field. <br /> See [Dataverse Search suggest](suggest.md)|
|`searchautocomplete`<br /><xref:Microsoft.Dynamics.CRM.searchautocomplete?text=searchautocomplete Action><br />`/api/search/v2.0/autocomplete`| Provide autocompletion of input as the user enters text into a form field.<br /> See [Dataverse Search autocomplete](autocomplete.md)|

There are also two operations you can use to understand whether search is enabled and how it is configured.

|SDK Message Name<br />Web API Function<br />Search 2.0 Endpoint|Description|
|---------|---------|
|`searchstatus`<br /><xref:Microsoft.Dynamics.CRM.searchstatus?text=searchstatus Function><br />`/api/search/v2.0/status`|Search status of an Organization.<br /> See [Dataverse Search status](status.md)|
|`searchstatistics`<br /><xref:Microsoft.Dynamics.CRM.searchstatistics?text=searchstatistics Function><br />`/api/search/v2.0/statistics`|Provides organization storage size and document count.<br /> See [Dataverse Search statistics](statistics.md)|

## Use Postman with Dataverse search

If you have used Postman with Dataverse Web API you know how useful it is to try using the APIs. We have some instructions about setting up a Postman environment to authenticate with the Dataverse Web API here: [Set up a Postman environment](../webapi/setup-postman-environment.md).

You can use the same instructions with the search operations using Web API functions and actions. If you want to use the native search 2.0 endpoint, simply change these two environment variables:

|Variable|Web API Value|Search 2.0 Endpoint value|
|---------|---------|---------|
|`version`|`9.2`|`2.0`|
|`webapiurl`|`{{url}}/api/data/v{{version}}/`|`{{url}}/api/search/v{{version}}/`|

### Extract response JSON with Postman

Each of the search operations returns JSON that has a `response` property. The `response` property is an escaped string that contains JSON data. It is difficult to read this string value, but you can use the Postman Visualize feature to transform this string value into readable JSON.

1. In your Postman request select the **Tests** tab and enter the following script:

   ```javascript
   let responseString = JSON.stringify(JSON.parse(pm.response.json().response),null,1);
   
   template = '<pre>{{response}}</pre>';
   
   pm.visualizer.set(template, {
       response: responseString
   });
   ```

1. Execute your request and select the **Visualize** button.

You can now see the unescaped JSON data returned in the `response` property.

:::image type="content" source="../media/postman-query-visualize-script.png" alt-text="Postman query with test script to extract JSON from escaped string":::

More information:

- [Postman Learning Center: Visualizing responses](https://learning.postman.com/docs/sending-requests/visualizer/)
- [Postman Learning Center: Visualizing responses > Rendering HTML](https://learning.postman.com/docs/sending-requests/visualizer/#rendering-html)


## Detect if search is enabled

Dataverse search is enabled by default for production environments, but it is an opt-out feature so it could be turned off even in a production environment. If you are using an environment other than a production environment, an administrator must enable it.

If you use the query, suggest, or autocomplete operations when the environment is not enabled you will get these errors:

#### [SDK for .NET](#tab/sdk)

TODO

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

You can detect whether the search service is enabled by checking the settings in the organization table or by using the [Dataverse Search status](status.md) operation.

### Check Organization table

The [Organization table](../reference/entities/organization.md) contains a single row of data that controls how the organization is configured. The [IsExternalSearchIndexEnabled](../reference/entities/organization.md#BKMK_IsExternalSearchIndexEnabled) boolean column tells you whether search is enabled for the organization.


#### [SDK for .NET](#tab/sdk)

This function will return the `IsExternalSearchIndexEnabled` property value for the organization.

```csharp
static bool IsExternalSearchIndexEnabled(IOrganizationService service) {

    QueryExpression query = new QueryExpression("organization") { 
        ColumnSet = new ColumnSet("isexternalsearchindexenabled")
    };

    EntityCollection organizations = service.RetrieveMultiple(query);
    return (bool)organizations.Entities.FirstOrDefault()["isexternalsearchindexenabled"];
}
```

More information: [Build queries with QueryExpression](../org-service/build-queries-with-queryexpression.md)

#### [Web API](#tab/webapi)

This Web API query will return the `IsExternalSearchIndexEnabled` property value for the organization.

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
         "organizationid": "883278f5-07af-45eb-a0bc-3fea67caa544"
      }
   ]
}
```

More information: [Query data using the Web API](../webapi/query-data-web-api.md)

#### [Search 2.0 endpoint](#tab/search)

You must use the SDK for .NET or Web API to check this setting.

---

## Enable tables and columns for search

Which tables and columns are enabled for search is driven by data in Dataverse.

### Enable Tables

Only those tables where the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.CanEnableSyncToExternalSearchIndex?text=EntityMetadata.CanEnableSyncToExternalSearchIndex>`.Value` property is true can be enabled for Dataverse search. If the `CanEnableSyncToExternalSearchIndex.CanBeChanged` value is false, you cannot change the value. More information: [Managed properties](/power-platform/alm/managed-properties-alm)

To enable a table for Dataverse Search, set the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.SyncToExternalSearchIndex?text=EntityMetadata.SyncToExternalSearchIndex> boolean property to true.

You can check the values for a table with the Web API using the table logical name. Replace `account` in the queries below with the logical name of the table you want to check.


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

More information: [Retrieve and detect changes to table definitions](../org-service/metadata-retrieve-detect-changes.md)


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

More information: [Query table definitions using the Web API](../webapi/query-metadata-web-api.md)

#### [Search 2.0 endpoint](#tab/search)

You must use the SDK for .NET or Web API to check this setting.

---

More information:

- [Select tables for Dataverse search](/power-platform/admin/configure-relevance-search-organization#select-tables-for-dataverse-search)
- [Set managed properties for Dataverse search](/power-platform/admin/configure-relevance-search-organization#set-managed-properties-for-dataverse-search)

### Enable Columns

The columns that are searchable for the table are determined by whether they are included in the Quick Find view for each table. You can query the definition of the view in the [View (SavedQuery) table](../reference/entities/savedquery.md) and update it programmatically.

More information:

- [Select searchable fields and filters for each table](/power-platform/admin/configure-relevance-search-organization#select-searchable-fields-and-filters-for-each-table)
- [Customize views](../../model-driven-apps/customize-entity-views.md)

## Service Protection Limits

When using either Web API and Dataverse SDK for .NET the common [Service protection API limits](../api-limits.md) will never be approached because Dataverse search applies a lower limit.

Dataverse search allows a user to send 1 request per second. If this is exceeded, a [429 Too Many Requests](https://developer.mozilla.org/docs/Web/HTTP/Status/429) error will be returned. If a `429` error is returned, you should wait until the period defined in the `Retry-After` response header value has passed before sending additional requests. The value represents the number of seconds to wait.


### See also

[Dataverse Search query](query.md)<br />
[Dataverse Search suggest](suggest.md)<br />
[Dataverse Search autocomplete](autocomplete.md)<br />
[Dataverse Search status](status.md)<br />
[Dataverse Search statistics](statistics.md)<br />
[Dataverse Native Search 1.0](search1.0.md)


[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]
