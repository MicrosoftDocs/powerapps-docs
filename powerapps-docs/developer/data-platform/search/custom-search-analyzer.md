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

Dataverse search uses many different built in capabilities that include both index and search analyzers to return the best data based on what the user asks for. It is used to help define how an index maps certain phrases or words to the best match to data in a column and a row in a table.

Examples can include phrases that have special characters, use dashes or frequently used words like “of,” “or, etc. that are removed from the search term when the query is processed by the back-end data engine.

Here are some examples where Dataverse search will not return an exact match because the data in the searched column is not easily understood, or because certain characters are automatically removed or ignored based on the out of box analyzer used by Dataverse Search service.

TODO - Work with Jim on formatting a table:


To ensure Dataverse Search returns, the expected results will require additional instructions via analyzers to match keywords and phrases to the data expected to be returned in a search term.  The data is specific to a column and a table, and it is important to make sure Dataverse search uses the best analyzer, which is often a default Azure Search analyzer or a custom analyzer if needed.

## About analyzers

Dataverse search is built on top of the Microsoft analyzers (https://learn.microsoft.com/azure/search/index-add-language-analyzers#supported-language-analyzers) so if you are seeing results that you do not expect or would like to refine, please make sure you have a good understanding of Azure search analyzer. Please refer to Analyzers for linguistic and text processing - Azure AI Search | Microsoft Learn (https://learn.microsoft.com/en-us/azure/search/search-analyzers) for details and information on how Azure search analyzers work in a search engine.

Default Analyzers:
It might be possible for your search terms and phrases that the Azure default analyzers will work for you. You can learn more about the available search analyzers that are available to be used: Add custom analyzers to string fields - Azure Cognitive Search | Microsoft Learn (https://learn.microsoft.com/en-us/azure/search/index-add-custom-analyzers#built-in-analyzers), or you can also see if the available language analyzers: Add language analyzers to string fields - Azure Cognitive Search | Microsoft Learn (https://learn.microsoft.com/en-us/azure/search/index-add-language-analyzers#supported-language-analyzers) will work for you.

To use an out of the box Azure analyzer, set the name, attribute name and entityname to be used and set the settings to {"analyzer": "it.microsoft"}, this is for a search analyzer or { "analyzer": "it.microsoft"} for a language analyzer.

In Dataverse Search, an analyzer is automatically invoked on all string fields marked as searchable.

By default, Dataverse Search uses the [Apache Lucene Standard analyzer (standard lucene)](https://lucene.apache.org/core/6_6_1/core/org/apache/lucene/analysis/standard/StandardAnalyzer.html), which breaks text into elements following the ["Unicode Text Segmentation"](https://unicode.org/reports/tr29/) rules. The standard analyzer converts all characters to their lower case form. Both indexed documents and search terms go through the analysis during indexing and query processing.

You can override the default on a field-by-field basis. Alternative analyzers can be a [language analyzer](/azure/search/index-add-language-analyzers) for linguistic processing, a [custom analyzer](/azure/search/index-add-custom-analyzers), or a built-in analyzer from the list of [available analyzers](/azure/search/index-add-custom-analyzers#built-in-analyzers).

Question: Is it possible to demonstrate the steps to apply to Dataverse search using an 'available analyzer' without providing a 'custom analyzer'?

TODO: If we have a scenario with a specific search analyzer project, we can add it to our [GitHub PowerApps-Samples repo](https://github.com/microsoft/PowerApps-Samples). Having this sample allows people to verify that the documented process works. Expect people will want to verify a 'happy path' solution works as an evaluation step before committing to engaging a developer to do this work.

## Create a custom analyzer

When results are not coming back from Dataverse as you would expect, it is possible that you will need to build a custom search analyzer to be used when searching across your data in your application.  It is important to understand what an Azure custom analyzer is and how to build one that can be applied to your power platform environment and can be utilized by Dataverse search to return data as expected by your users.  Please refer to Add custom analyzers to string fields - Azure AI Search | Microsoft Learn (https://learn.microsoft.com/en-us/azure/search/index-add-custom-analyzers) to learn more on what an Azure custom analyzer is and how it will help return the best results for your users. 

## Enable the custom analyzer for Dataverse Search
After creating a custom search analyzer makers can enable it for Dataverse search by adding the definition of the analyzer in the configuration table and populate the attribute settings table with the field and analyzer name mappings.

Open the searchatributessetting table at https://make.powerapps.com
## NOTE! Make sure you are in the environment you want to apply the changes by clicking on Environment in the page's header and selecting your environment.

Select tables from the left navigation pane

Select the “All” tables

In the top right search for searchattributesettings
TODO: Get help from Jim to add the image

Open the table
Make sure when the table opens the Name, attributename, entityname and settings columns are visible.You can easily add them by selecting “+ more” next to the name column.

After selecting the columns click on save.

This will close the dialog and the columns will be visible on the page.
TODO: Get help from Jim to add the image

After saving the columns should be visible.

## What to add to the columns:
•	Enter a name, this would be the name of the row in the table. It can be anything that helps you identify the custom analyzer you have added.

•	In the attribute name column, enter the column of the table you want the analyzer used for your search terms or phrases.

•	In the entity name column, enter the name of the table where the column you entered in the attribute name exists.

•	In the setting column, copy the entire. Json string that defines your custom analyzer.

•	Tab to the next row, this will automatically save your record and update your environment.

NOTE! This will automatically kick off an index for the table defined. This is needed for the search engine to use the columns defined by your custom

TODO: Get help from Jim to add the image

Sample value of settings attribute: 
{ "analyzer": "name_analyzer"}
{"indexanalyzer": "name_analyzer", "searchanalyzer": "name_analyzer"}

## Set the custom analyzer definition.
You will need to update the searchcustomanlayzer table. To update the table you will need to add the name of the analyzer and the .json file with the definitions into the table.

TODO: Add the scripts given by engineering.







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



