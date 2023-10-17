---
title: "Dataverse Search statistics (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Use Dataverse search statistics to get information about search usage." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 10/20/2023
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

In many cases you may need to know the size of the data structure being returned to help you better optimize your query or query results and help you manage the size of your Database to manage cost.

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
OutputSearchStatistics START

        StorageSizeInBytes: 1341090
        StorageSizeInMb: 1
        DocumentCount: 1309

OutputSearchStatistics END
```

#### [Web API](#tab/webapi)

**Request**

```http
GET [Organization Uri]/api/data/v9.2/searchstatistics
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.searchstatisticsResponse",
  "response": "{\"value\":{\"storagesizeinbytes\":4539149,\"storagesizeinmb\":3,\"documentcount\":5515}}"
}
```

#### [Search 2.0 endpoint](#tab/search)

**Request**

```http
GET [Organization URI]/api/search/v2.0/statistics HTTP/1.1
```

The body of the response from the search endpoint is the same as the Web API.

---


### See also

[Search for Dataverse records](overview.md)<br />
[Dataverse Search query](query.md)<br />
[Dataverse Search suggest](suggest.md)<br />
[Dataverse Search autocomplete](autocomplete.md)<br />
[Dataverse Search status](status.md)<br />
[Dataverse legacy search](legacy.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]