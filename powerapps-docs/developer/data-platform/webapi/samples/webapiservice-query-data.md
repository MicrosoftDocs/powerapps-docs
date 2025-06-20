---
title: "Web API Query Data sample (C#) (Microsoft Dataverse)| Microsoft Docs"
description: "This sample demonstrates how to query data of Microsoft Dataverse entity instances, using the Dataverse Web API along with the WebApiService class."
ms.date: 03/28/2023
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
search.audienceType:
  - developer
contributors:
  - JimDaly
---

# Web API Query Data sample (C#)

This .NET 6.0 sample demonstrates how to perform common data operations using the Dataverse Web API.

This sample uses the common helper code in the [WebAPIService class library (C#)](webapiservice.md).
  
> [!NOTE]
> This sample implements the Dataverse operations and console output detailed in [Web API Query Data Sample](../web-api-query-data-sample.md)  and uses the common C# constructs described in [Web API Samples (C#)](../web-api-samples-csharp.md).

## Prerequisites

The following is required to build and run this sample:

- Microsoft Visual Studio 2022.
- Access to Dataverse with privileges to perform data operations.
  
<a name="bkmk_runSample"></a>
  
## How to run this sample

1. Clone or download the [PowerApps-Samples](https://github.com/microsoft/PowerApps-Samples) repository.
1. Locate the [/dataverse/webapi/C#-NETx/QueryData/](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/CSharp-NETx/QueryData) folder.
1. Open the `QueryData.sln` file using Visual Studio 2022
1. Edit the `appsettings.json` file to set the following property values:

   |Property|Instructions  |
   |---------|---------|
   |`Url`|The Url for your environment. Replace the placeholder `https://yourorg.api.crm.dynamics.com` value with the value for your environment. See [View developer resources](../../view-download-developer-resources.md) to find this. |
   |`UserPrincipalName`|Replace the placeholder `you@yourorg.onmicrosoft.com` value with the UPN value you use to access the environment.|
   |`Password`|Replace the placeholder `yourPassword` value with the password you use.|

1. Save the `appsettings.json` file
1. Press F5 to run the sample.

## Code

The code for this sample is here: [PowerApps-Samples/dataverse/webapi/C#-NETx/QueryData/Program.cs](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/CSharp-NETx/QueryData/Program.cs)

## Demonstrates

This sample has 11 regions:

### Section 0: Create Records to query

Operations: Create 1 `account` record with 9 related `contact` records. Each `contact` has 3 related `task` records.

This is the data that will be used in this sample.

### Section 1 Selecting specific properties

Operations:

- Using `$select `against a contact entity to get the properties you want.
- Including annotations provides access to formatted values with the `@OData.Community.Display.V1.FormattedValue` annotation

### Section 2 Using query functions

Operations:

- Using standard query functions (`contains`, `endswith`, `startswith`) to filter results.
- Using Dataverse query functions (`LastXhours`, `Last7Days`, `Today`, `Between`, `In`)
- Using filter operators and logical operators (`eq`, `ne`, `gt`, `and`, `or`)
- Set precedence using parenthesis `((criteria1) and (criteria2)) or (criteria3)`

### Section 3 Ordering and aliases

Operations:

- Using `$orderby`
- Using parameterized aliases (`?@p1=fullname`) with `$filter` and `$orderby`

### Section 4 Limit and count results

Operations:

- Limiting results using `$top`.
- Get a count value using `$count`.

### Section 5 Pagination

Operations:

- Use the `Prefer: odata.maxpagesize` request header to limit the number of rows returned.
- Use the url returned with the `@odata.nextLink` annotation to retrieve the next set of records.

### Section 6 Expanding results

Operations:

- `$expand` with single-valued navigation properties.
- `$expand` with partner property.
- `$expand` with collection-valued navigation properties.
- `$expand` with multiple navigation property types in a single request.
- Nested `$expand`.
- Nested `$expand` having both single-valued and collection-valued navigation properties.

### Section 7 Aggregate results

Operations: Using `$apply=aggregate` with `average`, `sum`, `min`, & `max`.

### Section 8 FetchXML queries

Operations:

- Sending requests using fetchXml using `?fetchXml=`
- Paging using the `page` and `count` attributes.

### Section 9 Using predefined queries

Operations:

- Using `{entitysetname}?savedQuery={savedqueryid}` to return the results of a saved query (system view)
- Using `{entitysetname}?userQuery={userquery}` to return the results of a user query (saved view)

### Section 10: Delete sample records

Operations: A reference to each record created in this sample was added to a list as it was created. In this sample the records are deleted using a `$batch` operation.

### See also

[Query Data using the Web API](../query/overview.md)  
[Web API Query Data Sample](../web-api-query-data-sample.md)  
[Use the Dataverse Web API](../overview.md)
[Web API Basic Operations Sample (C#)](webapiservice-basic-operations.md)<br />
[Web API Conditional Operations sample (C#)](webapiservice-conditional-operations.md)<br />
[Web API Functions and Actions Sample (C#)](webapiservice-functions-and-actions.md)<br />
[Web API table schema operations sample (C#)](webapiservice-metadata-operations.md)<br />
[Web API WebApiService Parallel Operations Sample (C#)](webapiservice-parallel-operations.md)<br />
[Web API Parallel Operations with TPL Dataflow components Sample (C#)](webapiservice-tpl-dataflow-parallel-operations.md)<br />

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
