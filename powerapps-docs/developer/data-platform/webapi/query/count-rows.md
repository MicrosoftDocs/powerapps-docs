---
title: Count rows using OData
description: Learn how to use OData to count rows from Microsoft Dataverse tables using Dataverse Web API.
ms.date: 07/11/2024
ms.topic: how-to
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - JosinaJoy
---
# Count rows using OData

Use the `$count=true` query option to include a count of entities that match the filter criteria, up to 5,000.  

**Request:**

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=accountid&$count=true
Accept: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts(accountid)",
    "@odata.count": 9,
    "value": [
        {
            "@odata.etag": "W/\"81359849\"",
            "accountid": "78914942-34cb-ed11-b596-0022481d68cd"
        },
        ... <Truncated for brevity>
    ]
}
```

The response `@odata.count` annotation contains the number of rows, up to 5,000, that matches the filter criteria irrespective of the page size requested.
  
> [!NOTE]
> If you want to retrieve a snapshot within the past 24 hours of the total number of rows for a table beyond 5,000, use the [RetrieveTotalRecordCount function](xref:Microsoft.Dynamics.CRM.RetrieveTotalRecordCount). 
  

If the count value is 5,000 and you want to know whether the count is exactly 5,000 or greater than 5,000, you can add the [Prefer request header](https://www.rfc-editor.org/rfc/rfc7240) to send the [odata.include-annotations preference](http://docs.oasis-open.org/odata/odata/v4.0/os/part1-protocol/odata-v4.0-os-part1-protocol.html#_Toc372793628) for these annotations:

 - `Microsoft.Dynamics.CRM.totalrecordcount`
 - `Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded`

```
Prefer: odata.include-annotations="Microsoft.Dynamics.CRM.totalrecordcount,Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded"
```

This header adds the following annotations to the result:

- `@Microsoft.Dynamics.CRM.totalrecordcount`
- `@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded`


When used with the `$count=true` query option and there are more than 5,000 records, the following values are returned:

```
"@odata.count": 5000,
"@Microsoft.Dynamics.CRM.totalrecordcount": 5000,
"@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded": true,
```

If there are fewer than 5000 records, the actual count is returned.

```
"@odata.count": 58,
"@Microsoft.Dynamics.CRM.totalrecordcount": 58,
"@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded": false,
```

If you don't include the `$count=true` query option, the total `@Microsoft.Dynamics.CRM.totalrecordcount` value is `-1`.

The following example shows that there are 10 accounts that match the `$filter`, but only the first three accounts are returned:
  
 **Request:**

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name?
&$filter=contains(name,'sample')
&$count=true  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Prefer: odata.maxpagesize=3
Prefer: odata.include-annotations="Microsoft.Dynamics.CRM.*"
```  
  
 **Response:** 
 
```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
Preference-Applied: odata.maxpagesize=3
Preference-Applied: odata.include-annotations="Microsoft.Dynamics.CRM.*"
  
{  
   "@odata.context":"[Organization URI]/api/data/v9.2/$metadata#accounts(name)",
   "@odata.count":10,
   "@Microsoft.Dynamics.CRM.totalrecordcount": 5000,
   "@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded": true,
   "value":[  
      {  
         "@odata.etag":"W/\"502482\"",
         "name":"Fourth Coffee (sample)",
         "accountid":"655eaf89-f083-e511-80d3-00155d2a68d3"
      },
      {  
         "@odata.etag":"W/\"502483\"",
         "name":"Litware, Inc. (sample)",
         "accountid":"675eaf89-f083-e511-80d3-00155d2a68d3"
      },
      {  
         "@odata.etag":"W/\"502484\"",
         "name":"Adventure Works (sample)",
         "accountid":"695eaf89-f083-e511-80d3-00155d2a68d3"
      }
   ],
   "@odata.nextLink":"[Organization URI]/api/data/v9.2/accounts?$select=name&$filter=contains(name,'sample')&$skiptoken=%3Ccookie%20pagenumber=%222%22%20pagingcookie=%22%253ccookie%2520page%253d%25221%2522%253e%253caccountid%2520last%253d%2522%257b695EAF89-F083-E511-80D3-00155D2A68D3%257d%2522%2520first%253d%2522%257b655EAF89-F083-E511-80D3-00155D2A68D3%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20istracking=%22False%22%20/%3E"
}

```  
  
To get just a number that represents the count of a collection, append `/$count`, as in the following example:
  
 **Request:**  

```http
GET [Organization URI]/api/data/v9.2/accounts/$count  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```  
  
 **Response:**

```http
HTTP/1.1 200 OK  
Content-Type: text/plain  
OData-Version: 4.0  
  
10  
```

## Next steps

Learn how to optimize performance.

> [!div class="nextstepaction"]
> [Optimize performance](optimize-performance.md)

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]