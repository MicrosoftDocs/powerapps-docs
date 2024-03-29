---
title: "Create a custom analyzer for Dataverse Search"
description: "TODO when it is clear what this article is about" 
ms.date: 03/28/2024
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

Dataverse search uses many different built-in capabilities that include both index and search analyzers to return the best data based on what the user asks for. These built-in capabilities to help define how an index maps certain phrases or words to the best match to data in a column and a row in a table.

Examples can include phrases that have special characters, or frequently used words (like '`of`' and '`or`')  that the back-end data engine removes from the search term when the query is processed.

Here are some examples where Dataverse search won't return an exact match because the data in the searched column isn't easily understood, or because certain characters are automatically removed or ignored based on the default analyzer used by Dataverse Search service.


|Examples|Desired|Actual|
|---------|---------|---------|
|`AB-84(q)(1)(c)`<br />or<br />`AB-84(1)(1)(-c)` |**TODO**: clearer example|**TODO**: clearer example|
|`2.2.3.1`|**TODO**: clearer example|**TODO**: clearer example|
|`PG-11.1`|**TODO**: clearer example|**TODO**: clearer example|
|`"%mn" +"ABC-123"`|**TODO**: clearer example|**TODO**: clearer example|
|`"Inspector of brakes"`|All results include the literal string `"Inspector of brakes"`|Returns results containing `Inspector of boilers`|

> **TODO**: Do these examples need an example data set to be clearer?

To ensure Dataverse Search returns expected results requires extra instructions via analyzers to match keywords and phrases to the data expected to be returned in a search term. The data is specific to a column and a table, and it's important to make sure Dataverse search uses the best analyzer, which is often a default Azure Search analyzer or a custom analyzer if needed.

## About analyzers

Dataverse search is built on top of the [Microsoft analyzers](/azure/search/index-add-language-analyzers#supported-language-analyzers) so if you're seeing results that you don't expect or would like to refine, make sure you have a good understanding of Azure search analyzer. Refer to [Analyzers for linguistic and text processing](/azure/search/search-analyzers) for details and information on how Azure search analyzers work in a search engine.

### Default Analyzers

For your search terms and phrases, the Azure default analyzers might work for you. You can learn more about the available search analyzers that are available to be used: [Add custom analyzers to string fields](/azure/search/index-add-custom-analyzers#built-in-analyzers), or you can also see if the [available language analyzers](/azure/search/index-add-language-analyzers#supported-language-analyzers) work for you.

To use one of the existing Azure analyzers, set the **Name**, **attributename**, and **entityname** to be used and set the **settings** to `{"analyzer": "keyword"}`, this is for a search analyzer or `{ "analyzer": "it.microsoft"}` for a language analyzer.

In Dataverse Search, an analyzer is automatically invoked on all string fields marked as searchable. There is no

By default, Dataverse Search uses the [Apache Lucene Standard analyzer (standard lucene)](https://lucene.apache.org/core/6_6_1/core/org/apache/lucene/analysis/standard/StandardAnalyzer.html), which breaks text into elements following the ["Unicode Text Segmentation"](https://unicode.org/reports/tr29/) rules. The standard analyzer converts all characters to their lower case form. Both indexed documents and search terms go through the analysis during indexing and query processing.

You can override the default on a field-by-field basis. Alternative analyzers can be a [language analyzer](/azure/search/index-add-language-analyzers) for linguistic processing, a [custom analyzer](/azure/search/index-add-custom-analyzers), or a built-in analyzer from the list of [available analyzers](/azure/search/index-add-custom-analyzers#built-in-analyzers).


## Set an analyzer for a field

To apply a different analyzer for a Dataverse table column, there needs to be a row identifying that column in the [searchattributesettings table](../reference/entities/searchattributesettings.md).

Setting this property doesn't require writing code. Anyone with access to [Power Apps](https://make.powerapps.com) and write access to the `searchattributesettings` table can apply this change, but they need to take extra care not to create a duplicate row. [Learn what makes a duplicate row ](#what-to-add-to-the-columns)

Open the [searchattributesettings table](../reference/entities/searchattributesettings.md) in [Power Apps](https://make.powerapps.com).

> [!NOTE]
> Make sure you are in the environment you want to apply the changes by clicking on Environment in the page's header and selecting your environment.

1. Select tables from the left navigation pane.
1. Select **All** tables.
1. In the top right search for `searchattributesettings`.
1. Open the table.
1. Make sure when the table opens the **Name**, **attributename**, **entityname** and **settings** columns are visible.You can easily add them by selecting "**+18 more**" next to the **Name** column.
1. After selecting the columns click on **Save**.
1. This will close the dialog and the columns will be visible on the page.
1. After saving the columns should be visible.

### What to add to the columns

The following table describes what to add to the columns:

> [!IMPORTANT]
> The combination of **attributename** and **entityname** values must be unique in the **searchattributesettings** table. You must make sure that you don't enter duplicate rows for with the same values for these columns.
>
> To avoid anyone unintentionally creating a duplicate row, you can add an alternate key to the `searchattributesettings` table specifying the `entityname` and `attributename` columns in the key. [Learn to alternate keys using Power Apps](../../../maker/data-platform/define-alternate-keys-portal.md)


|Name  |What to add|
|---------|---------|
|**Name**|It can be anything that helps you identify the custom analyzer you have added.|
|**entityname**|The logical name of the table that has the column you are configuring.|
|**attributename**|The logical name of column of the table you want the analyzer used for your search terms or phrases.|
|**settings**|The JSON string that identifies your custom analyzer. The value might look something like this: `{ "analyzer": "name_analyzer"}{"indexanalyzer": "name_analyzer", "searchanalyzer": "name_analyzer"}`|


A new index of the table mentioned in the `entityname` column starts when a new row is added or the `settings` column of an existing row is updated. The search engine needs this to use the columns defined by the new setting.

If you want to update this value using code, you can use the following examples

# [SDK for .NET](#tab/sdk)

This static `SetSearchAttributeSettings` method includes logic to ensure that duplicate rows are not added to the `searchattributesettings` table, and that any existing row isn't overwritten accidentally.

```csharp
/// <summary>
/// Creates or replaces a SearchAttributeSettings record
/// </summary>
/// <param name="service">The authenticated IOrganizationService instance</param>
/// <param name="entityName">The name of the entity for which the search attribute settings record is created.</param>
/// <param name="attributeName">The logical name of the column for which the search attribute settings record is created.</param>
/// <param name="settings">The settings for the search attribute.</param>
/// <param name="overwriteExisting">Verify that the intent is to replace any existing record</param>
static void SetSearchAttributeSettings(
   IOrganizationService service,
   string entityName,
   string attributeName,
   string settings,
   bool overwriteExisting = false)
{

   try
   {
         #region Check whether record exists

         Entity existingRecord = null;

         QueryExpression query = new("searchattributesettings")
         {
            ColumnSet = new ColumnSet(
               "searchattributesettingsid",
               "entityname",
               "attributename",
               "settings"),
            Criteria = new FilterExpression(LogicalOperator.And)
            {
               Conditions = {
               new ConditionExpression("entityname", ConditionOperator.Equal, entityName),
               new ConditionExpression("attributename", ConditionOperator.Equal, attributeName)
               }
            }
         };

         // Retrieve any matching records
         EntityCollection entityCollection = service.RetrieveMultiple(query);

         if (entityCollection.Entities.Count > 1)
         {

            string message = "More than one record is found in searchattributesettings ";
            message += $"with entityname {entityName} and attributename {attributeName}.";

            throw new Exception(message);
         }

         if (entityCollection.Entities.Count == 1)
         {
            existingRecord = entityCollection.Entities[0];
         }

         #endregion Check whether record exists

         if (existingRecord != null)
         {
            string currentSettings = existingRecord.GetAttributeValue<string>("settings");
            Guid recordId = existingRecord.Id;

            if (!overwriteExisting)
            {

               string message = "An existing record is found in searchattributesettings with entityname:";
               message += $"{entityName}, attributename: {attributeName} settings: {settings}. ";
               message += "Please update the value of overwriteExisting to true and ";
               message += " use the SetSearchAttributeSettings method again.";

               throw new Exception(message);
            }

            // Removing the existing record before replacing it
            service.Delete("searchattributesettings", recordId);
         }

         Entity newRecord = new("searchattributesettings")
         {
            Attributes = {
               { "entityname", entityName },
               { "attributename", attributeName },
               { "settings", settings }
            }
         };

         // Create the new record with the desired settings
         service.Create(newRecord);

   }
   catch (Exception)
   {
         throw;
   }
}
```

The following example shows how to use it to specify a custom analyzer named `msdyn_search_remove_parenthesis_analyzer` for the [Contact.JobTitle column](../reference/entities/contact.md#BKMK_JobTitle).

```csharp
SetSearchAttributeSettings(
      service: service,
      entityName: "contact",
      attributeName: "jobtitle",
      settings: "{ \"analyzer\": \"msdyn_search_remove_parenthesis_analyzer\" }",
      overwriteExisting: true
   );
```



# [Web API](#tab/webapi)

Content for Windows...

---

## Create a custom analyzer

When results aren't coming back from Dataverse as you would expect, you can build and configure a custom search analyzer. It's important to understand what an Azure custom analyzer is and how to build one that can be applied to your power platform environment so that Dataverse search can to return data as expected by your users. Refer to [Add custom analyzers to string fields](/azure/search/index-add-custom-analyzers) to learn more on what an Azure custom analyzer is and how it helps return the best results for your users.

## Enable the custom analyzer for Dataverse Search

After creating a custom search analyzer, you can enable it for Dataverse search by adding the definition of the analyzer in the configuration table and populate the attribute settings table with the field and analyzer name mappings.


## Set the custom analyzer definition

You will need to update the  [searchcustomanalyzer table](../reference/entities/searchcustomanalyzer.md). To update the table you will need to add the name of the analyzer and the .json file with the definitions into the table.

> **TODO**: Add the scripts given by engineering.



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



