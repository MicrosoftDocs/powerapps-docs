---
title: "Dataverse Search statistics (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Use Dataverse search statistics to get information about search usage." # 115-145 characters including spaces. This abstract displays in the search result.
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
# Dataverse Search statistics

Search statistics provides information about:

- Storage size in bytes
- Storage size in megabytes
- Number of documents

**TODO**: Provide some information about why people might care about this data.

#### [SDK for .NET](#tab/sdk)

```csharp

static void CheckSearchStatistics(IOrganizationService service)
{
   try
   {

      OrganizationResponse searchstatisticsResponse = service.Execute(new OrganizationRequest("searchstatistics"));
  
      string responseString = searchstatisticsResponse.Results["response"];

      Console.WriteLine(responseString);

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

#### [Web API](#tab/webapi)

**Request**

```http
GET [Organization URI]/api/data/v9.2/searchstatistics HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response**

```http
HTTP/1.1 200 OK

{
  "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.searchstatisticsResponse",
  "response": "{\"value\":{\"storagesizeinbytes\":11464058,\"storagesizeinmb\":10,\"documentcount\":13155}}"
}

```

#### [Search 2.0 endpoint](#tab/search)

**Request**

```http
GET [Organization URI]/api/search/v2.0/statistics HTTP/1.1
```

The response from the search endpoint is the same as the Web API.

---


### See also

[Search for Dataverse records](overview.md)<br />
[Dataverse Search query](query.md)<br />
[Dataverse Search suggest](suggest.md)<br />
[Dataverse Search autocomplete](autocomplete.md)<br />
[Dataverse Search status](status.md)<br />
[Dataverse Native Search 1.0](search1.0.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]