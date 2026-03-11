---
title: Use SQL to query data using the Dataverse Web API (preview)
description: Learn to compose a query using OData with Microsoft Dataverse Web API
ms.date: 03/11/2026
ms.topic: how-to
author: paulliew
ms.author: paulliew
ms.reviewer: jdaly
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors: 
  - saurabhrb
---
# Use SQL to query data by using the Dataverse Web API (preview)

You can retrieve data from Dataverse by using Structured Query Language (SQL) `SELECT` commands.

[!INCLUDE [cc-dataverse-sql-limitations](../../includes/cc-dataverse-sql-limitations.md)]

Assign the SQL command to the sql query option using the entity set name of the table you want to retrieve data from.

## Example

The following example sends this SQL query:

`SELECT name FROM account AS a WHERE a.name LIKE 'Fourth Coffee'`

**Request**

This example uses *Percent-encoding* for the SQL sinces spaces aren't allowed in a URL:

```http
GET [Organization URI]/api/data/v9.2/accounts?sql=SELECT%20name%20FROM%20account%20AS%20a%20WHERE%20a.name%20LIKE%20'Fourth%20Coffee' HTTP/1.1
Authorization: Bearer [REDACTED]
OData-MaxVersion: 4.0
OData-Version: 4.0
Prefer: odata.include-annotations="*"
Accept: application/json
```

This query uses *application/x-www-form-urlencoded* and will also work:

`SELECT+name+FROM+account+AS+a+WHERE+a.name+LIKE+%27Fourth+Coffee%27`

[Learn more about url encoding](#example)


**Response**

The response is exactly what you would get with the equivilent OData query.

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0
Preference-Applied: odata.include-annotations="*"

{
   "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts(name,accountid)",
   "@Microsoft.Dynamics.CRM.totalrecordcount": -1,
   "@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded": false,
   "@Microsoft.Dynamics.CRM.globalmetadataversion": "173309522",
   "value": [
      {
         "@odata.etag": "W/\"173325408\"",
         "accountid": "0bdd4472-981d-f111-8341-0022482aa957",
         "name": "Fourth Coffee"
      }
   ]
}
```

## URL encoding

Whenever you pass a value with a query parameter in a URL, it should be URL encoded. SQL queries contain spaces, and spaces aren't valid in a URL, so they must be replaces with either `%20` or `+`.

Many frameworks will do this for you automatically.  For example PowerShell [Invoke-RestMethod command](/powershell/module/microsoft.powershell.utility/invoke-restmethod) will  automatically encode the `Uri` parameter value.

Otherwise, [just like with FetchXml](../../fetchxml/retrieve-data.md?tabs=webapi), you should encode any query parameter value, especially when it originates with user input. 

- In JavaScript, you use the [encodeURIComponent function](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent).
- In .NET, you can use the [System.NET.WebUtility.UrlEncode(String) method](xref:System.Net.WebUtility.UrlEncode(System.String))