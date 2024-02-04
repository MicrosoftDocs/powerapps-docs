---
title: "Create a custom analyzer for Dataverse Search"
description: "TODO when it is clear what this article is about" 
ms.date: 02/10/2024
ms.reviewer: jdaly
ms.topic: article
author: mspilde
ms.author: mspilde
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
 - JimDaly
---
# Create a custom analyzer for Dataverse Search

Create a custom analyzer for Dataverse search when you want to: TODO: List one or more reasons why people want to do this.

- TODO: Reason 1
- TODO: Reason 2

TODO: This is a great place to introduce a scenario, perhaps based on any examples you have and customer asks

## About analyzers

TODO: This may be a good place to introduce any prerequisite information, such as we expect the reader to understand [Analyzers for text processing in Azure AI Search](/azure/search/search-analyzers) with links to content where they can learn more. Make it clear early that this article isn't going to teach them about this Azure capability, only how to apply the analyzers they create to Dataverse.

<!-- 

You can borrow and adapt some learn.microsoft.com content, like an overview description 
This comes from https://learn.microsoft.com/azure/search/search-analyzers#default-analyzer

You may want to replace 'Azure AI Search' with 'Dataverse Search'?
-->

In Azure AI Search, an analyzer is automatically invoked on all string fields marked as searchable.

By default, Azure AI Search uses the [Apache Lucene Standard analyzer (standard lucene)](https://lucene.apache.org/core/6_6_1/core/org/apache/lucene/analysis/standard/StandardAnalyzer.html), which breaks text into elements following the ["Unicode Text Segmentation"](https://unicode.org/reports/tr29/) rules. The standard analyzer converts all characters to their lower case form. Both indexed documents and search terms go through the analysis during indexing and query processing.

You can override the default on a field-by-field basis. Alternative analyzers can be a [language analyzer](/azure/search/index-add-language-analyzers) for linguistic processing, a [custom analyzer](/azure/search/index-add-custom-analyzers), or a built-in analyzer from the list of [available analyzers](/azure/search/index-add-custom-analyzers#built-in-analyzers).

Question: Is it possible to demonstrate the steps to apply to Dataverse search using an 'available analyzer' without providing a 'custom analyzer'?

TODO: If we have a scenario with a specific search analyzer project, we can add it to our [GitHub PowerApps-Samples repo](https://github.com/microsoft/PowerApps-Samples). Having this sample allows people to verify that the documented process works. Expect people will want to verify a 'happy path' solution works as an evaluation step before committing to engaging a developer to do this work.

## Create a custom analyzer

TODO: Describe the process to perform this at a high level

1. Do something first
1. Then do something else
1. Then complete another step
1. Finally, verify that the work you did has the desired result


### Do something first

### Then do something else

### Then complete another step

### Finally, verify that the work you did has the desired result


## Placeholder H2 for any other major tasks


### Links to reference content

[searchattributesettings table](../reference/entities/searchattributesettings.md)
The Web API entity set name for this table is `searchattributesettingses`.

To refer to specific columns:

- [attributename](../reference/entities/searchattributesettings.md#BKMK_attributename)
- [entityname](../reference/entities/searchattributesettings.md#BKMK_entityname)
- [name](../reference/entities/searchattributesettings.md#BKMK_name)
- [settings](../reference/entities/searchattributesettings.md#BKMK_settings)


### Web API examples

In my system there are no rows in this table.

**Request**

```http
GET https://yourorg.crm.dynamics.com/api/data/v9.2/searchattributesettingses?$select=name,entityname,attributename,settings HTTP/1.1
Prefer: odata.include-annotations="*"
Accept: application/json
Authorization: Bearer [REDACTED]
OData-MaxVersion: 4.0
OData-Version: 4.0
```

**Response**

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0
Preference-Applied: odata.include-annotations="*"

{
  "@odata.context": "https://yourorg.crm.dynamics.com/api/data/v9.2/$metadata#searchattributesettingses(name,entityname,attributename,settings)",
  "@Microsoft.Dynamics.CRM.totalrecordcount": -1,
  "@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded": false,
  "@Microsoft.Dynamics.CRM.globalmetadataversion": "107932318",
  "value": []
}
```


[searchcustomanalyzer table](../reference/entities/searchcustomanalyzer.md)

The Web API entity set name for this table is `searchcustomanalyzers`.

In my system there are no rows in this table.
Note: The [analyzers column](../reference/entities/searchcustomanalyzer.md#BKMK_analyzers) is a File column, so we can refer to these docs about uploading it: [Upload Files](../file-column-data.md#upload-files) and downloading it [Download Files](../file-column-data.md#download-files)

**Request**

```http
GET https://yourorg.crm.dynamics.com/api/data/v9.2/searchcustomanalyzers?$select=name,analyzers,analyzers_name,statecode,statuscode HTTP/1.1
Prefer: odata.include-annotations="*"
Accept: application/json
Authorization: Bearer [REDACTED]
OData-MaxVersion: 4.0
OData-Version: 4.0
```

**Response**

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0
Preference-Applied: odata.include-annotations="*"

{
  "@odata.context": "https://yourorg.crm.dynamics.com/api/data/v9.2/$metadata#searchcustomanalyzers(name,analyzers,analyzers_name,statecode,statuscode)",
  "@Microsoft.Dynamics.CRM.totalrecordcount": -1,
  "@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded": false,
  "@Microsoft.Dynamics.CRM.globalmetadataversion": "107932318",
  "value": []
}
```


<!-- The following stays at the bottom -->

### See also

[Dataverse Search](overview.md)   
[Configure Dataverse search for your environment](/power-platform/admin/configure-relevance-search-organization)   
[Analyzers for text processing in Azure AI Search](/azure/search/search-analyzers)


[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]



