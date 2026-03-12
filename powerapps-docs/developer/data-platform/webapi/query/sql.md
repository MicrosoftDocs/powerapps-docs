---
title: Use SQL to Query Data With the Dataverse Web API (Preview)
description: Learn how to use SQL to query data with the Microsoft Dataverse Web API. Retrieve table data using SQL SELECT commands passed via the sql query option.
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

You can use SQL to query data from Microsoft Dataverse by using the Web API. Pass Structured Query Language (SQL) `SELECT` commands through the `sql` query option to retrieve table data without composing OData query syntax.

[!INCLUDE [cc-dataverse-sql-limitations](../../includes/cc-dataverse-sql-limitations.md)]

Assign the SQL command to the `sql` query option by using the entity set name of the table you want to retrieve data from.

## Example SQL query using the Dataverse Web API

The following example sends this SQL query:

`SELECT name FROM account AS a WHERE a.name LIKE 'Fourth Coffee'`

**Request**

This example uses *percent-encoding* for the SQL query since spaces aren't allowed in a URL:

```http
GET [Organization URI]/api/data/v9.2/accounts?sql=SELECT%20name%20FROM%20account%20AS%20a%20WHERE%20a.name%20LIKE%20'Fourth%20Coffee' HTTP/1.1
Authorization: Bearer [REDACTED]
OData-MaxVersion: 4.0
OData-Version: 4.0
Prefer: odata.include-annotations="*"
Accept: application/json
```

This query uses *application/x-www-form-urlencoded* encoding and also works:

`SELECT+name+FROM+account+AS+a+WHERE+a.name+LIKE+%27Fourth+Coffee%27`

[Learn more about URL encoding](#url-encoding-the-sql-parameter)


**Response**

The response is exactly what you get with the equivalent OData query.

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

## URL encoding the `sql` parameter

Whenever you pass a value with a query parameter in a URL, URL encode it. SQL queries contain spaces, and spaces aren't valid in a URL, so you must replace them with either `%20` or `+`.

Many frameworks automatically encode URLs for you. For example, PowerShell [Invoke-RestMethod command](/powershell/module/microsoft.powershell.utility/invoke-restmethod) automatically encodes the `Uri` parameter value.

Otherwise, [just like with FetchXml](../../fetchxml/retrieve-data.md?tabs=webapi), encode any query parameter value, especially when it originates from user input. 

- In JavaScript, use the [encodeURIComponent function](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent).
- In .NET, use the [System.NET.WebUtility.UrlEncode(String) method](xref:System.Net.WebUtility.UrlEncode(System.String)).