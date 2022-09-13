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
> - [Search for records by using Dataverse search](../../../user/relevance-search.md).
> - [Configure facets and filters](../../../user/facets-and-filters.md)
> - [Frequently asked questions about Dataverse search](../../../user/relevance-faq.md)
> - [Configure Dataverse search for your environment](/power-platform/admin/configure-relevance-search-organization)

## How to use

Developers can use the search APIs three different ways:

- The native Search `/api/search/v1.0/` endpoint
- The Dataverse SDK for .NET
- The Web API `/api/data/` endpoint


### Use the native search endpoint

The search endpoint is the native endpoint for Dataverse Search. This is the endpoint used for the search experience in model-driven apps. You can use this endpoint without authentication from within model-driven application experiences such as PCF controls or form scripts.

You can also authenticate to this endpoint from external applications just as you would when using Web API, but you will use the `/api/search/` path rather than `/api/data/`.

### Use the Dataverse SDK for .NET

For .NET projects using the Dataverse SDK for .NET, you can use the `CrmSvcUtil` command line code generation tool to generate `*Request` and `*Response` classes for these messages just as you would for any custom action. Or, you can use the <xref:Microsoft.Xrm.Sdk.OrganizationRequest?text=OrganizationRequest> and <xref:Microsoft.Xrm.Sdk.OrganizationResponse?text=OrganizationResponse> classes.

> [!NOTE]
> To use Dataverse search from a plug-in, you must use the SDK.

More information:

- [Generate early-bound classes for the Organization service](../org-service/generate-early-bound-classes.md)
- [Use messages with the Organization service](../org-service/use-messages.md)

### Use the Web API

In the Web API, the `searchquery`, `searchsuggest`, and `searchautocomplete` messages are exposed as OData actions. More information: [Use Web API actions](../webapi/use-web-api-actions.md)

## Search operations

Search provides three operations to support a user interface that enables searching for data and two operations that you can use to retrieve information about how the organization is configured to support search.

|Search Endpoint<br />Web API Action<br />SDK message|Description|
|---------|---------|
|`/api/search/v1.0/query`<br /><xref:Microsoft.Dynamics.CRM.searchquery?text=searchquery Action><br />`searchquery`| Returns a search results page.|
|`/api/search/v1.0/suggest`<br /><xref:Microsoft.Dynamics.CRM.searchquery?text=searchsuggest Action><br />`searchsuggest`|Provide suggestions as the user enters text into a form field. |
|`/api/search/v1.0/autocomplete`<br /><xref:Microsoft.Dynamics.CRM.searchquery?text=searchautocomplete Action><br />`searchautocomplete`| Provide autocompletion of input as the user enters text into a form field.|
|`/api/search/v1.0/status`<br /><xref:Microsoft.Dynamics.CRM.searchstatus?text=searchstatus Function><br />`status`|Search status of an Organization.|
|`/api/search/v1.0/searchstatistics`<br /><xref:Microsoft.Dynamics.CRM.searchstatistics?text=searchstatistics Function><br />`searchstatistics`|Provides organization storage size and document count.|

The Web API and Dataverse SDK for .NET expose the native Search verbs Web API Actions or as organization service `messages`. These actions and messages use the native search endpoint on the server and return the results.

## Search Status

Dataverse search is enabled by default for production environments, but it is an opt-out feature so it could be turned off even in a production environment. If you are using an environment other than a production environment, and administrator must enable it.

You will get the following error when using the native search endpoint and search is not enabled:

TODO: Check Web API and SDK errors as well

```http

HTTP/1.1 501 Not Implemented

{
  "Message": "The Relevance Search API is currently disabled. To enable this API, activate the Relevance Search experience administration option in System Settings.",
  "ExceptionMessage": "The Relevance Search API is currently disabled. To enable this API, activate the Relevance Search experience administration option in System Settings.",
  "ExceptionType": "Microsoft.Crm.CrmHttpException",
  "StackTrace": "[Redacted for brevity]",
  "ErrorCode": "0x8006088a"
}

```

You can detect whether the search service is enabled without catching the error using the following:

### Check Organization table

The [Organization table](../reference/entities/organization.md) contains a single row of data that controls how the organization is configured. You can query the following properties to determine the status of the service:

|Name  |Type|Description|
|---------|---------|---------|
|[IsExternalSearchIndexEnabled](../reference/entities/organization.md#BKMK_IsExternalSearchIndexEnabled)|Yes/No|Select whether data can be synchronized with an external search index.|
|[NewSearchExperienceEnabled](../reference/entities/organization.md#BKMK_NewSearchExperienceEnabled)|Yes/No|Indicates whether an organization has enabled the new Relevance search experience (released in Oct 2020) for the organization|
|[RelevanceSearchModifiedOn](../reference/entities/organization.md#BKMK_RelevanceSearchModifiedOn)|DateTime|This setting contains the last modified date for relevance search setting that appears as a toggle in PPAC.|
|[RelevanceSearchEnabledByPlatform](../reference/entities/organization.md#BKMK_RelevanceSearchEnabledByPlatform)|Yes/No|   Indicates whether relevance search was enabled for the environment as part of Dataverse's relevance search on-by-default sweep|

#### [.NET SDK](#tab/sdk)

```csharp
static void CheckOrganizationSearchProperties(IOrganizationService service) {

   QueryExpression query = new QueryExpression("organization") { 
      ColumnSet = new ColumnSet(
         "isexternalsearchindexenabled", 
         "newsearchexperienceenabled", 
         "relevancesearchmodifiedon", 
         "relevancesearchenabledbyplatform")
   };

   EntityCollection organizations = service.RetrieveMultiple(query);
   Entity organization = organizations.Entities.FirstOrDefault();
   Console.WriteLine("Organization Search Values:");
   Console.WriteLine($"\tIsExternalSearchIndexEnabled:{organization["isexternalsearchindexenabled"]}");
   Console.WriteLine($"\tNewSearchExperienceEnabled:{organization["newsearchexperienceenabled"]}");
   Console.WriteLine($"\tRelevanceSearchModifiedOn:{organization["relevancesearchmodifiedon"]}");
   Console.WriteLine($"\tRelevanceSearchEnabledByPlatform:{organization["relevancesearchenabledbyplatform"]}");
}
```

#### [Web API](#tab/webapi)

**Request**

```http
GET [Organization URI]/api/data/v9.2/organizations?$select=isexternalsearchindexenabled,newsearchexperienceenabled,relevancesearchmodifiedon,relevancesearchenabledbyplatform HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

```

**Response**

```http
HTTP/1.1 200 OK

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#organizations(isexternalsearchindexenabled,newsearchexperienceenabled,relevancesearchmodifiedon,relevancesearchenabledbyplatform)",
    "value": [
        {
            "@odata.etag": "W/\"73630341\"",
            "isexternalsearchindexenabled": true,
            "newsearchexperienceenabled": true,
            "relevancesearchmodifiedon": "2022-09-12T23:41:58Z",
            "relevancesearchenabledbyplatform": false,
            "organizationid": "883278f5-07af-45eb-a0bc-3fea67caa544"
        }
    ]
}
```

--- 


If you want to programatically enable search for an org, you can set these properties by updating the organization record for all of these properties.


### Use the status API

#### [Search endpoint](#tab/search)

**Request**

```http
GET [Organization URI]/api/search/v1.0/status HTTP/1.1
```

When search is not enabled, the status property will be `notprovisioned`.

**Response**

```http
HTTP/1.1 200 OK

{
  "value": {
    "status": "notprovisioned",
    "lockboxstatus": "Unknown"
  }
}
```

When search is enabled, detailed information about each entity is in the `entitystatusresults` 
property and the `status` value is `provisioned`.

**Response**

```http
HTTP/1.1 200 OK

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
          "emailaddress1": {
            "indexfieldname": "a3x"
          },
          "address1_city": {
            "indexfieldname": "a3y"
          },
          "modifiedon": {
            "indexfieldname": "j_0"
          },
          "telephone1": {
            "indexfieldname": "a3z"
          },
          "statecode": {
            "indexfieldname": "f_0"
          },
          "primarycontactid": {
            "indexfieldname": "a40"
          },
          "statuscode": {
            "indexfieldname": "g_0"
          },
          "createdon": {
            "indexfieldname": "i_0"
          },
          "entityimage_url": {
            "indexfieldname": "h_0"
          },
          "industrycode": {
            "indexfieldname": "a43"
          },
          "name": {
            "indexfieldname": "d_0"
          },
          "owningbusinessunit": {
            "indexfieldname": "c_0"
          },
          "crdcb_testrollupfield": {
            "indexfieldname": "a45"
          },
          "ownerid": {
            "indexfieldname": "b_0"
          },
          "accountnumber": {
            "indexfieldname": "a46"
          },
          "telephone2": {
            "indexfieldname": "a47"
          },
          "versionnumber": {
            "indexfieldname": "e_0"
          },
          "accountid": {
            "indexfieldname": "a_0"
          },
          "crdcb_throwawaydate": {
            "indexfieldname": "a48"
          },
          "crdcb_budget": {
            "indexfieldname": "a8f"
          }
        }
      },
<Information on other entities removed for brevity>      
    ],
    "status": "provisioned",
    "lockboxstatus": "Disabled",
    "cmkstatus": "Disabled"
  }
}
```

#### [.NET SDK](#tab/sdk)

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

#### [Web API](#tab/webapi)

**Request**

```http
GET [Organization URI]/api/data/v9.2/searchstatus HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

```

The `response` property returned by <xref:Microsoft.Dynamics.CRM.searchstatusResponse?text=searchstatusResponse ComplexType> is an escaped string containing JSON data.

When search is not enabled, the `status` property within that escaped string will be `notprovisioned`.

**Response**

```http
HTTP/1.1 200 OK

{
  "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.searchstatusResponse",
  "response": "{\"value\":{\"status\":\"notprovisioned\",\"lockboxstatus\":\"Unknown\"}}"
}
```

When search is enabled, the response property contains all the same data in an escaped string that is returned with the search endpoint.

**Response**

```http
HTTP/1.1 200 OK

{
  "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.searchstatusResponse",
  "response": "{\"value\":{\"entitystatusresults\":[{\"entitylogicalname\":\"account\",\"objecttypecode\":1,\"primarynamefield\":\"name\",\"lastdatasynctimestamp\":\"73630169!09/12/2022 14:26:14\",\"lastprincipalobjectaccesssynctimestamp\":\"72969347!09/12/2022 14:26:14\",\"entitystatus\":\"EntitySyncComplete\",\"searchableindexedfieldinfomap\":{\"emailaddress1\":{\"indexfieldname\":\"a3x\"},\"address1_city\":{\"indexfieldname\":\"a3y\"},\"modifiedon\":{\"indexfieldname\":\"j_0\"},\"telephone1\":{\"indexfieldname\":\"a3z\"},\"statecode\":{\"indexfieldname\":\"f_0\"},\"primarycontactid\":{\"indexfieldname\":\"a40\"},\"statuscode\":{\"indexfieldname\":\"g_0\"},\"createdon\":{\"indexfieldname\":\"i_0\"},\"entityimage_url\":{\"indexfieldname\":\"h_0\"},\"industrycode\":{\"indexfieldname\":\"a43\"},\"name\":{\"indexfieldname\":\"d_0\"},\"owningbusinessunit\":{\"indexfieldname\":\"c_0\"},\"crdcb_testrollupfield\":{\"indexfieldname\":\"a45\"},\"ownerid\":{\"indexfieldname\":\"b_0\"},\"accountnumber\":{\"indexfieldname\":\"a46\"},\"telephone2\":{\"indexfieldname\":\"a47\"},\"versionnumber\":{\"indexfieldname\":\"e_0\"},\"accountid\":{\"indexfieldname\":\"a_0\"},\"crdcb_throwawaydate\":{\"indexfieldname\":\"a48\"},\"crdcb_budget\":{\"indexfieldname\":\"a8f\"}}}, <Information on other entities removed for brevity> ],\"status\":\"provisioned\",\"lockboxstatus\":\"Disabled\",\"cmkstatus\":\"Disabled\"}}"
}

```

---

## Service Protection Limits

The search endpoint has service protection limits that are different from the Dataverse [Service protection API limits](../api-limits.md) that apply to the Web API and Dataverse SDK for .NET. The search endpoint returns a 429 error when # requests are received within a specific time frame. If a 429 error is returned, you should wait until the Retry-After period returned in the response header has passed before sending additional requests.

### See also

[Dataverse Search query](query.md)<br />
[Dataverse Search suggest](suggest.md)<br />
[Dataverse Search autocomplete](autocomplete.md)


[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]
