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

- The Web API `/api/data/v9.x` endpoint
- The native search `/api/search/v2.0/` endpoint
- The Dataverse SDK for .NET

### Web API

Search operations exposed with Web API are OData actions or functions described in the [CSDL $metadata document](../webapi/web-api-service-documents.md#csdl-metadata-document). You can use these in the same way you use other Web API operations.

More information:

- [Use Web API actions](../webapi/use-web-api-actions.md)
- [Use Web API functions](../webapi/use-web-api-functions.md)


### Native search 2.0

The native search 2.0 endpoint is not an OData service and has no service document. The native search 2.0 endpoint accepts the same parameters and returns the same responses as the corresponding Web API Actions and functions.

The [Dataverse native search 1.0](search1.0.md) has not been deprecated and continues to be supported.

### SDK for .NET

Search operations are defined as Dataverse messages using [Custom APIs](../custom-api.md). For .NET projects they can also be used with the SDK for .NET.

There are currently no classes included in the SDK to use these operations. For .NET Framework projects you can use the `CrmSvcUtil` command line code generation tool with the `/generateactions` parameter to generate `*Request` and `*Response` classes for these messages just as you would for any custom action.

You can also use the <xref:Microsoft.Xrm.Sdk.OrganizationRequest?text=OrganizationRequest> and <xref:Microsoft.Xrm.Sdk.OrganizationResponse?text=OrganizationResponse> classes.

More information:

- [Generate early-bound classes for the Organization service](../org-service/generate-early-bound-classes.md)
- [Use messages with the Organization service](../org-service/use-messages.md)

## Search operations

Search provides three operations to support a user interface that enables searching for data.

|Web API Action<br />Search Endpoint<br />SDK Message Name|Description|
|---------|---------|
|<xref:Microsoft.Dynamics.CRM.searchquery?text=searchquery Action><br />`/api/search/v1.0/query`<br />`searchquery`| Returns a search results page. <br /> See [Dataverse Search query](query.md)|
|<xref:Microsoft.Dynamics.CRM.searchquery?text=searchsuggest Action><br />`/api/search/v1.0/suggest`<br />`searchsuggest`|Provide suggestions as the user enters text into a form field. <br /> See [Dataverse Search suggest](suggest.md)|
|<xref:Microsoft.Dynamics.CRM.searchquery?text=searchautocomplete Action><br />`/api/search/v1.0/autocomplete`<br />`searchautocomplete`| Provide autocompletion of input as the user enters text into a form field.<br /> See [Dataverse Search autocomplete](autocomplete.md)|

There are also two operations you can use to understand whether search is enabled and how it is configured.

|Web API Function<br />Search Endpoint<br />SDK Message Name|Description|
|---------|---------|
|<xref:Microsoft.Dynamics.CRM.searchstatus?text=searchstatus Function><br />`/api/search/v1.0/status`<br />`status`|Search status of an Organization.<br /> See [Search Status](#search-status)|
|<xref:Microsoft.Dynamics.CRM.searchstatistics?text=searchstatistics Function><br />`/api/search/v1.0/searchstatistics`<br />`searchstatistics`|Provides organization storage size and document count.<br /> See [Search Statistics](#search-statistics)|


## Detect if search is enabled

Dataverse search is enabled by default for production environments, but it is an opt-out feature so it could be turned off even in a production environment. If you are using an environment other than a production environment, an administrator must enable it.

This is the error you will get when search is not enabled when using Web API or the Native search:

```http
HTTP/1.1 400 Bad Request
{"error":{"code":"0x80048d0b","message":"Dataverse Search feature is disabled for this organization."}}
```

TODO: Verify SDK Error is the same


You can detect whether the search service is enabled by checking the settings in the organization table or by using the [Search Status](#search-status) operation.

### Check Organization table

The [Organization table](../reference/entities/organization.md) contains a single row of data that controls how the organization is configured. The [IsExternalSearchIndexEnabled](../reference/entities/organization.md#BKMK_IsExternalSearchIndexEnabled) boolean column tells you whether search is enabled for the organization.

## Search Status

Use search status to know:

- Whether search is enabled.
- Which tables and columns are enabled for search.

autocomplete-settings-example.png

#### [Web API](#tab/webapi)

**Request**

```http
GET [Organization URI]/api/data/v9.2/searchstatus HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

```

The `response` property returned by <xref:Microsoft.Dynamics.CRM.searchstatusResponse?text=searchstatusResponse ComplexType> is an escaped string containing JSON data. The `status` property value can be either: `notprovisioned`, `provisioninginprogress`, or `provisioned`.

When not provisioned, you should get a response like this:

**Response**

```http
HTTP/1.1 200 OK

{
  "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.searchstatusResponse",
  "response": "{\"value\":{\"status\":\"notprovisioned\",\"lockboxstatus\":\"Unknown\"}}"
}
```

When search is enabled, there is more data that describes the search status for the org.

**Response**

```http
HTTP/1.1 200 OK

{
  "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.searchstatusResponse",
  "response": "{\"value\":{\"entitystatusresults\":[{\"entitylogicalname\":\"account\",\"objecttypecode\":1,\"primarynamefield\":\"name\",\"lastdatasynctimestamp\":\"73630169!09/12/2022 14:26:14\",\"lastprincipalobjectaccesssynctimestamp\":\"72969347!09/12/2022 14:26:14\",\"entitystatus\":\"EntitySyncComplete\",\"searchableindexedfieldinfomap\":{\"emailaddress1\":{\"indexfieldname\":\"a3x\"},\"address1_city\":{\"indexfieldname\":\"a3y\"},\"modifiedon\":{\"indexfieldname\":\"j_0\"},\"telephone1\":{\"indexfieldname\":\"a3z\"},\"statecode\":{\"indexfieldname\":\"f_0\"},\"primarycontactid\":{\"indexfieldname\":\"a40\"},\"statuscode\":{\"indexfieldname\":\"g_0\"},\"createdon\":{\"indexfieldname\":\"i_0\"},\"entityimage_url\":{\"indexfieldname\":\"h_0\"},\"industrycode\":{\"indexfieldname\":\"a43\"},\"name\":{\"indexfieldname\":\"d_0\"},\"owningbusinessunit\":{\"indexfieldname\":\"c_0\"},\"crdcb_testrollupfield\":{\"indexfieldname\":\"a45\"},\"ownerid\":{\"indexfieldname\":\"b_0\"},\"accountnumber\":{\"indexfieldname\":\"a46\"},\"telephone2\":{\"indexfieldname\":\"a47\"},\"versionnumber\":{\"indexfieldname\":\"e_0\"},\"accountid\":{\"indexfieldname\":\"a_0\"},\"crdcb_throwawaydate\":{\"indexfieldname\":\"a48\"},\"crdcb_budget\":{\"indexfieldname\":\"a8f\"}}}, 
  
  <Information on other tables removed for brevity> 
  
  ],\"status\":\"provisioned\",\"lockboxstatus\":\"Disabled\",\"cmkstatus\":\"Disabled\"}}"
}
```

When unescaped, the JSON of the `response` property looks like this:

```json
{
  "value": {
    "entitystatusresults": [
      {
        "entitylogicalname": "account",
        "objecttypecode": 1,
        "primarynamefield": "name",
        "lastdatasynctimestamp": "73630169!09/12/2022 14:26:14",
        "lastprincipalobjectaccesssynctimestamp": "72969347!09/12/2022 14:26:14",
        "entitystatus": "EntitySyncComplete",
        "searchableindexedfieldinfomap": {
          "emailaddress1": { "indexfieldname": "a3x" },
          "address1_city": { "indexfieldname": "a3y" },
          "modifiedon": { "indexfieldname": "j_0" },
          "telephone1": { "indexfieldname": "a3z" },
          "statecode": { "indexfieldname": "f_0" },
          "primarycontactid": { "indexfieldname": "a40" },
          "statuscode": { "indexfieldname": "g_0" },
          "createdon": { "indexfieldname": "i_0" },
          "entityimage_url": { "indexfieldname": "h_0" },
          "industrycode": { "indexfieldname": "a43" },
          "name": { "indexfieldname": "d_0" },
          "owningbusinessunit": { "indexfieldname": "c_0" },
          "crdcb_testrollupfield": { "indexfieldname": "a45" },
          "ownerid": { "indexfieldname": "b_0" },
          "accountnumber": { "indexfieldname": "a46" },
          "telephone2": { "indexfieldname": "a47" },
          "versionnumber": { "indexfieldname": "e_0" },
          "accountid": { "indexfieldname": "a_0" },
          "crdcb_throwawaydate": { "indexfieldname": "a48" },
          "crdcb_budget": { "indexfieldname": "a8f" }
        }
      },

  <Information on other tables removed for brevity> 

    ],
    "status": "provisioned",
    "lockboxstatus": "Disabled",
    "cmkstatus": "Disabled"
  }
}
```

The `entitystatusresults` contains information about each table configured for search. For each table, the `searchableindexedfieldinfomap` tells you which columns are included in search for that table. The `indexfieldname` property is for internal use only.

- `lockboxstatus` refers to the Power Platform Customer Lockbox. More information: [Securely access customer data using Customer Lockbox in Power Platform (preview)](/power-platform/admin/about-lockbox)
- `cmkstatus` refers to whether the environment has a customer managed key. More information: [Manage the encryption key](/power-platform/admin/manage-encryption-key)



#### [Search endpoint](#tab/search)

**Request**

```http
GET [Organization URI]/api/search/v2.0/status HTTP/1.1
```

The response from the search endpoint is the same as the Web API.

#### [SDK for .NET](#tab/sdk)

```csharp
static void CheckSearchStatus(IOrganizationService service) {
   try
   {
      var status = (searchstatusResponse)service.Execute(new searchstatusRequest());

      Console.WriteLine(status.response);
      //Expect that this value is an escaped string containing JSON that must be parsed
   }
   catch (FaultException<OrganizationServiceFault> osf)
   {
      Console.WriteLine($"OrganizationServiceFault:{osf.Message}");
      // Fails here, Due to plug-in in Custom API?

      /*
      ErrorCode: 0x80048D0A IsvAbortedInternalServerError
      Message: Object reference not set to an instance of an object.
      
      */
   }
   catch (Exception ex) {

      Console.WriteLine($"Exception:{ex.Message}");
   }      
}
```

**Output**

```
//TODO: Should be the same as the Web API.
```

---

### Enable tables and columns for search

Which tables and columns are enabled for search is driven by data in Dataverse.

#### Enable Tables

Only those tables where the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.CanEnableSyncToExternalSearchIndex?text=EntityMetadata.CanEnableSyncToExternalSearchIndex>.Value property is true can be enabled for Dataverse search.

To enable a table for Dataverse Search, set the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.SyncToExternalSearchIndex?text=EntityMetadata.SyncToExternalSearchIndex> boolean property to true.

More information:

- [Select tables for Dataverse search](/power-platform/admin/configure-relevance-search-organization#select-tables-for-dataverse-search)
- [Set managed properties for Dataverse search](/power-platform/admin/configure-relevance-search-organization#set-managed-properties-for-dataverse-search)

#### Enable Columns

The columns that are searchable for the table are determined by whether they are included in the Quick Find view for each table. You can query the definition of the view in the [View (SavedQuery)  table](../reference/entities/savedquery.md)

More information:

- [Select searchable fields and filters for each table](/power-platform/admin/configure-relevance-search-organization#select-searchable-fields-and-filters-for-each-table)
- [Customize views](../../model-driven-apps/customize-entity-views.md)


## Search statistics

Search statistics provides information about:

- Storage size in bytes
- Storage size in megabytes
- Number of documents

#### [Web API](#tab/webapi)

**Request**

```http
GET [Organization URI]/api/data/v9.2/searchstatistics HTTP/1.1
```

**Response**

```http
HTTP/1.1 200 OK

{
  "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.searchstatisticsResponse",
  "response": "{\"value\":{\"storagesizeinbytes\":11464058,\"storagesizeinmb\":10,\"documentcount\":13155}}"
}

```

#### [Search endpoint](#tab/search)

**Request**

```http
GET [Organization URI]/api/search/v2.0/statistics HTTP/1.1
```

The response from the search endpoint is the same as the Web API.

#### [SDK for .NET](#tab/sdk)

```csharp

static void CheckSearchStatistics(IOrganizationService service)
{
   try
   {
      var searchstatisticsResponse = (searchstatisticsResponse)service.Execute(new searchstatisticsRequest());
      Console.WriteLine(searchstatisticsResponse.response);

   }
   catch (FaultException<OrganizationServiceFault> osf)
   {
      
      Console.WriteLine($"OrganizationServiceFault:{osf.Detail}");
      Console.WriteLine($"StackTrace:{osf.Detail.TraceText}");

   }
   catch (Exception ex)
   {

      Console.WriteLine($"Exception:{ex.Message}");
   }            
}

```

**Output**

```
OrganizationServiceFault:Exception details:
ErrorCode: 0x80048D0A
Message: Object reference not set to an instance of an object.
TimeStamp: 2022-09-13T19:14:06.9534141Z
--
Exception details:
ErrorCode: 0x80048D0A
Message: Object reference not set to an instance of an object.
TimeStamp: 2022-09-13T19:14:06.9534141Z
--

StackTrace:
[Microsoft.CDS.RelevanceSearch.Plugins: Microsoft.CDS.RelevanceSearch.Plugins.StatisticsPlugin]
[1dc24ad0-fe44-ec11-8c60-002248208fac: CustomApi 'searchstatistics' implementation]
```

---

## Service Protection Limits

Dataverse search has service protection limits that are different from the Dataverse [Service protection API limits](../api-limits.md) that apply to the Web API and Dataverse SDK for .NET.

Dataverse search allows a user to send 1 request per second. If this is exceeded, a [429 Too Many Requests](https://developer.mozilla.org/docs/Web/HTTP/Status/429) error will be returned. If a `429` error is returned, you should wait until the period defined in the `Retry-After` response header value has passed before sending additional requests. The value represents the number of seconds to wait.


### See also

[Dataverse Search query](query.md)<br />
[Dataverse Search suggest](suggest.md)<br />
[Dataverse Search autocomplete](autocomplete.md)


[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]
