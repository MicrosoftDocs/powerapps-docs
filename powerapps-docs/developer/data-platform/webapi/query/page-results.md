---
title: "Page Results Using OData From Microsoft Dataverse Web API"
description: "Learn how to use OData paging to control and retrieve results from Microsoft Dataverse Web API efficiently. Follow step-by-step examples to implement pagination."
ms.date: 10/29/2026
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
# Page results by using OData

Use OData paging with the `Prefer: odata.maxpagesize` request header to control the number of records returned from Microsoft Dataverse Web API. If you don't specify a number, each request might return up to 5,000 table rows. For both standard and elastic tables, you can specify a max page size up to 5,000. The service ignores max page size requests larger than 5,000 for both standard and elastic tables.

> [!NOTE]
> Dataverse doesn't support the `$skip` query option, so you can't use the combination of `$top` and `$skip` for paging. [Learn about using the $top query option to limit the number of rows](overview.md#limit-the-number-of-rows).

The following example returns just the first two contact records:

**Request:**

```http
GET [Organization URI]/api/data/v9.2/contacts?$select=fullname
Accept: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
Prefer: odata.maxpagesize=2
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0
Preference-Applied: odata.maxpagesize=2

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#contacts(fullname)",
    "value": [
        {
            "@odata.etag": "W/\"72201545\"",
            "fullname": "Yvonne McKay (sample)",
            "contactid": "49b0be2e-d01c-ed11-b83e-000d3a572421"
        },
        {
            "@odata.etag": "W/\"80648695\"",
            "fullname": "Susanna Stubberod (sample)",
            "contactid": "70bf4d48-34cb-ed11-b596-0022481d68cd"
        }
    ],
    "@odata.nextLink": "[Organization URI]/api/data/v9.2/contacts?$select=fullname&$skiptoken=%3Ccookie%20pagenumber=%222%22%20pagingcookie=%22%253ccookie%2520page%253d%25221%2522%253e%253ccontactid%2520last%253d%2522%257bD5026A4D-D01C-ED11-B83E-000D3A572421%257d%2522%2520first%253d%2522%257b49B0BE2E-D01C-ED11-B83E-000D3A572421%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20istracking=%22False%22%20/%3E"
}
```

When there are more records than requested, the `@odata.nextLink` annotation provides a URL you can use with `GET` to return the next page of data, as shown in the following example:

**Request:**

```http
GET [Organization URI]/api/data/v9.2/contacts?$select=fullname&$skiptoken=%3Ccookie%20pagenumber=%222%22%20pagingcookie=%22%253ccookie%2520page%253d%25221%2522%253e%253ccontactid%2520last%253d%2522%257bD5026A4D-D01C-ED11-B83E-000D3A572421%257d%2522%2520first%253d%2522%257b49B0BE2E-D01C-ED11-B83E-000D3A572421%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20istracking=%22False%22%20/%3E
Accept: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
Prefer: odata.maxpagesize=2
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0
Preference-Applied: odata.maxpagesize=2

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#contacts(fullname)",
    "value": [
        {
            "@odata.etag": "W/\"80648710\"",
            "fullname": "Nancy Anderson (sample)",
            "contactid": "72bf4d48-34cb-ed11-b596-0022481d68cd"
        },
        {
            "@odata.etag": "W/\"80648724\"",
            "fullname": "Maria Campbell (sample)",
            "contactid": "74bf4d48-34cb-ed11-b596-0022481d68cd"
        }
    ],
    "@odata.nextLink": "[Organization URI]/api/data/v9.2/contacts?$select=fullname&$skiptoken=%3Ccookie%20pagenumber=%223%22%20pagingcookie=%22%253ccookie%2520page%253d%25222%2522%253e%253ccontactid%2520last%253d%2522%257bF2318099-171F-ED11-B83E-000D3A572421%257d%2522%2520first%253d%2522%257bBB55F942-161F-ED11-B83E-000D3A572421%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20istracking=%22False%22%20/%3E"
}
```

You should cache the results returned, or the `@odata.nextLink` URL value, and use it to return to previous pages.

Don't change the `@odata.nextLink` URL value or append any query options to it. For every subsequent request for more pages, use the same `odata.maxpagesize` preference value used in the original request. You can continue paging through the data until no `@odata.nextLink` annotation is included in the results.

In the earlier examples, the value of the `$skiptoken` parameter in the `@odata.nextLink` URL value contains encoded information. The server sets this encoded information to control paging. Don't modify the encoded information or encode it further. Use the URL value provided to retrieve the next page.

## Don't use the $top query option while paging records

Use the `$top` query option to limit the number of results returned. Don't use `$top` with the `Prefer: odata.maxpagesize` request header. If you include both, `$top` is ignored.

The following example returns just the first three account rows:

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name,revenue&$top=3
```

## PowerShell RetrieveAll example

This example `Get-AllRecords` PowerShell function  demonstrates how to retrieve all the records in a table limited only by the filter conditions. 

This function depends on the [`Get-Records`](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/PS/README.md#get-records-function) and [`Get-NextLink`](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/PS/README.md#get-nextlink-function) functions described in [Dataverse Web API PowerShell Helper functions](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/PS/README.md).

```powershell
<#
.SYNOPSIS
Retrieves all records matching an OData query.

.DESCRIPTION
Uses Get-Records for the first page and Get-NextLink for subsequent pages.
Follows each @odata.nextLink unchanged, using the same maximum page size.
Returns the combined records only after all requests succeed.

.PARAMETER setName
The entity set name, such as contacts.

.PARAMETER query
The OData query string, beginning with ?, or a related collection path as accepted
by Get-Records. Do not use the top-level $top or $skip query options with paging.
Include a deterministic $orderby, preferably including the primary key.
Use single quotes to prevent PowerShell from expanding OData option names.

.PARAMETER maxPageSize
Maximum records per page, from 1 to 5000. Defaults to 5000.

.EXAMPLE
$contacts = @(Get-AllRecords -setName 'contacts' `
   -query '?$select=fullname,jobtitle&$orderby=fullname,contactid' -maxPageSize 1000)

.OUTPUTS
The records themselves, not a Web API response envelope. Use @() to collect an
array even when zero or one record matches. Errors propagate to the caller.
#>
function Get-AllRecords {
   param (
      [Parameter(Mandatory)]
      [String]
      $setName,
      [Parameter(Mandatory)]
      [String]
      $query,
      [ValidateRange(1, 5000)]
      [int]
      $maxPageSize = 5000
   )

   if ($query -match '(?i)[?&](?:\$|%24)(top|skip)=') {
      throw 'The top-level $top and $skip query options cannot be used with paging.'
   }

   $records = [System.Collections.Generic.List[object]]::new()
   $response = Get-Records -setName $setName -query $query -maxPageSize $maxPageSize

   while ($true) {
      foreach ($record in $response.value) {
         $records.Add($record)
      }

      $nextLink = $response.'@odata.nextLink'
      if ([string]::IsNullOrWhiteSpace($nextLink)) {
         break
      }
      $response = Get-NextLink -nextLink $nextLink -maxPageSize $maxPageSize
   }

   return $records.ToArray()
}
```


[!INCLUDE [cc-ordering-paging](../../includes/cc-ordering-paging.md)]

## Next steps

Learn how to aggregate data.

> [!div class="nextstepaction"]
> [Aggregate data](aggregate-data.md)

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]