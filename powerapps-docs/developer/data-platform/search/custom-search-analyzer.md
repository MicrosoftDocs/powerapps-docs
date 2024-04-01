---
title: "Custom column analyzers for Dataverse Search"
description: "You can tailor the search results you get from Dataverse search by applying special search analyzers for specific table columns. You can use default Azure Search analyzers or create your own custom analyzer." 
ms.date: 04/01/2024
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
# Custom column analyzers for Dataverse Search

Dataverse search uses many different [Azure AI Search](/azure/search/search-what-is-azure-search) capabilities that include both index and search analyzers to return the best data based on what the user asks for. These built-in capabilities to help define how an index maps certain phrases or words to the best match to data in a column and a row in a table.

Examples include search strings that have special characters, or frequently used words (like '`of`' and '`or`')  that the back-end data engine removes from the search term when the query is processed.

Here are some examples where Dataverse search won't return an exact match because the data in the searched column isn't easily understood, or because certain characters are automatically removed or ignored based on the default analyzer used by Dataverse Search service.


|Examples|Desired|Actual|
|---------|---------|---------|
|`AB-84(q)(1)(c)`<br />or<br />`AB-84(1)(1)(-c)` |Exact match|Unwanted matches: **TODO**|
|`2.2.3.1`|Exact match|Unwanted matches: **TODO**|
|`PG-11.1`|Exact match|Unwanted matches:**TODO**:|
|`"%mn" +"ABC-123"`|Exact match for: <br /> `TODO example`<br />`TODO example`|Unwanted matches: <br /> `TODO example`<br />`TODO example`|
|`"Inspector of brakes"`|Exact match|Unwanted matches: `Inspector of boilers`|

To ensure Dataverse Search returns expected results requires extra instructions via analyzers to match keywords and phrases to the data expected to be returned in a search term. The data is specific to a column and a table, and it's important to make sure Dataverse search uses the best analyzer, which is often a default Azure AI Search analyzer or a custom analyzer if needed.

## About analyzers

Dataverse search is built on top of the [Azure AI Search analyzers](/azure/search/index-add-language-analyzers#supported-language-analyzers), so if you're seeing results that you don't expect or would like to refine, make sure you have a good understanding of the Azure AI Search analyzers. Refer to [Analyzers for text processing in Azure AI Search](/azure/search/search-analyzers) for details and information on how Azure AI Search analyzers work in a search engine.

### Built-in analyzers

By default, Dataverse Search uses the [Apache Lucene Standard analyzer (standard lucene)](https://lucene.apache.org/core/6_6_1/core/org/apache/lucene/analysis/standard/StandardAnalyzer.html) analyzer, which breaks text into elements following [Unicode Text Segmentation](https://unicode.org/reports/tr29/) rules. This default analyzer converts all characters to their lower case form. Both indexed documents and search terms go through the analysis during indexing and query processing.

In Dataverse Search, an analyzer is automatically invoked on all string or memo [columns marked as searchable](/power-platform/admin/configure-relevance-search-organization#select-searchable-fields-and-filters-for-each-table). You can't apply analyzers for any other type of column.

For your search terms and phrases, the Azure AI Search built-in analyzers might work for you. You can learn more about the available search analyzers that are available to be used: [Built-in analyzers](/azure/search/index-add-custom-analyzers#built-in-analyzers), or you can also see if the [available language analyzers](/azure/search/index-add-language-analyzers#supported-language-analyzers) work for you. Generally, you use an language analyzer when you have a column that is used to store data in a language that is different from your Dataverse base language.

To use one of the Azure AI Search built-in analyzers for a specific column, create a row in the [SearchAttributeSettings table](../reference/entities/searchattributesettings.md) set the [**Name**](../reference/entities/searchattributesettings.md#BKMK_name), [**entityname**](../reference/entities/searchattributesettings.md#BKMK_entityname), and [**attributename**](../reference/entities/searchattributesettings.md#BKMK_attributename) to be used and set the [**settings**](../reference/entities/searchattributesettings.md#BKMK_settings) to refer to a built-in search analyzer like `{"analyzer": "keyword"}`, or a language analyzer like `{ "analyzer": "it.microsoft"}`. [Learn how to set an analyzer for a column](#set-an-analyzer-for-a-column)



You can override the default on a for string columns. Alternative analyzers can be a [language analyzer](/azure/search/index-add-language-analyzers) for linguistic processing, a [custom analyzer](/azure/search/index-add-custom-analyzers), or a built-in analyzer from the list of [available analyzers](/azure/search/index-add-custom-analyzers#built-in-analyzers).


## Set an analyzer for a column

To apply a different analyzer for a Dataverse table column, there needs to be a row identifying that column in the [SearchAttributeSettings table](../reference/entities/searchattributesettings.md). By default, this table has no data.

Setting this property doesn't require writing code. Anyone with access to [Power Apps](https://make.powerapps.com) and write access to the `SearchAttributeSettings` table can apply this change, but they need to take extra care not to create a duplicate row. If you want to use code to set this, see [Edit SearchAttributeSettings table columns with code](#edit-searchattributesettings-table-columns-with-code).

### Configure Power Apps to edit the SearchAttributeSettings table

Follow these steps to open the [SearchAttributeSettings table](../reference/entities/searchattributesettings.md) in [Power Apps](https://make.powerapps.com) and edit the view to enable editing the **Name**, **attributename**, **entityname** and **settings** columns.

> [!NOTE]
> Make sure you are in the environment you want to apply the changes by clicking on Environment in the page's header and selecting your environment.

1. Select **Tables** from the left navigation pane.
1. Select **All** tables.
1. In the top right search for `searchattributesettings`.
1. Open the **SearchAttributeSettings** table.
1. Make sure when the table opens the **Name**, **attributename**, **entityname** and **settings** columns are visible. You can add them by selecting "**+18 more**" next to the **Name** column.
1. After selecting the columns click on **Save**.
1. This will close the dialog and the columns will be visible on the page.
1. After saving the columns should be visible.

For more information, see [Table columns and data](../../../maker/data-platform/create-edit-entities-portal.md#table-columns-and-data)

### Edit SearchAttributeSettings table columns manually

The following table describes what to add to each column:

> [!IMPORTANT]
> The combination of **entityname** and **attributename** values must be unique in the **SearchAttributeSettings** table. You must make sure that you don't enter duplicate rows for with the same values for these columns. When a duplicate row exists Dataverse search will return an error when people perform a search.
>
> To avoid anyone unintentionally creating a duplicate row, you can add an alternate key to the `SearchAttributeSettings` table specifying the `entityname` and `attributename` columns in the key. [Learn to define alternate keys using Power Apps](../../../maker/data-platform/define-alternate-keys-portal.md)


|Name  |What to add|
|---------|---------|
|**Name**|The name can be anything that helps you identify the custom analyzer you have added.|
|**entityname**|The logical name of the table that has the column you are configuring.|
|**attributename**|The logical name of column of the table you want the analyzer used for your search terms or phrases.|
|**settings**|The JSON string that identifies your custom analyzer. The value might look something like this: `{ "analyzer": "name_analyzer"}{"indexanalyzer": "name_analyzer", "searchanalyzer": "name_analyzer"}`|


A new index of the table referenced by the `entityname` column starts when a new row is added or the `settings` column of an existing row is updated. The search engine needs this to use the analyzer for the column defined by the new setting.

### Edit SearchAttributeSettings table columns with code

The following code shows how to update the **SearchAttributeSettings** table columns with code and avoid creating duplicate columns and avoid accidentally overwriting existing values.

#### [SDK for .NET](#tab/sdk)

```csharp
/// <summary>
/// Creates or replaces a SearchAttributeSettings record
/// </summary>
/// <param name="service">The authenticated IOrganizationService instance</param>
/// <param name="entityName">
/// The name of the entity for which the search attribute settings record is created.
/// </param>
/// <param name="attributeName">
/// The logical name of the column for which the search attribute settings record is created.
/// </param>
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

               string message = "An existing record is found in searchattributesettings with";
               message += $" entityname:{entityName}, attributename: {attributeName}";
               message += $" and settings: {settings}.";
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

The following example shows how to use the `SetSearchAttributeSettings` method to specify a custom analyzer named `msdyn_search_remove_parenthesis_analyzer` for the [Contact.JobTitle column](../reference/entities/contact.md#BKMK_JobTitle).

```csharp
SetSearchAttributeSettings(
      service: service,
      entityName: "contact",
      attributeName: "jobtitle",
      settings: "{ \"analyzer\": \"msdyn_search_remove_parenthesis_analyzer\" }",
      overwriteExisting: true
   );
```

[Learn how to use the SDK for .NET](../org-service/quick-start-org-service-console-app.md)

#### [Web API](#tab/webapi)

This PowerShell function depends on the following functions described in [Use PowerShell and Visual Studio Code with the Dataverse Web API](../webapi/use-ps-and-vscode-web-api.md)

- `Connect`: [Learn to create a Connect function](../webapi/use-ps-and-vscode-web-api.md#create-a-connect-function)
- [Learn to create table operations functions](../webapi/use-ps-and-vscode-web-api.md#create-table-operations-functions):
   - `Get-Records`
   - `Remove-Record`
   - `New-Record`

```powershell
<#
.SYNOPSIS
Sets the search attribute settings for a given entity and attribute.

.DESCRIPTION
The Set-SearchAttributeSettings function sets the search attribute settings for a specified entity 
and attribute. 
- It checks if an existing record is found in the searchattributesettings table. 
- If an existing record is found and the $overwriteExisting parameter is set to $false, 
it throws an error message. 
- If an existing record is found and the $overwriteExisting parameter is set to $true, 
it deletes the existing record and creates a new record with the updated settings. 
-If no existing record is found, it creates a new record with the specified settings.

.PARAMETER entityName
The name of the entity for which the search attribute settings need to be set.

.PARAMETER attributeName
The name of the attribute for which the search attribute settings need to be set.

.PARAMETER settings
The settings to be applied to the search attribute.

.PARAMETER overwriteExisting
Specifies whether to update an existing attribute setting if found. 
If set to $true, it removes the existing record and creates a new record with the updated settings. 
If set to $false and an existing record is found, it throws an error message.

.EXAMPLE
Connect 'https://myorg.crm.dynamics.com/'

Set-SearchAttributeSettings `
   -entityName 'contact' `
   -attributeName 'jobtitle' `
   -settings '{ "analyzer": "msdyn_search_remove_parenthesis_analyzer" }' `
   -overwriteExisting $true

This example sets the search attribute settings for the 'jobtitle' column of the 'contact' table. 
If an existing record is found, it removes the existing record and creates a new record with the 
updated settings.

#>
function Set-SearchAttributeSettings {
   param (
      [Parameter(Mandatory)]
      [string]
      $entityName,
      [Parameter(Mandatory)]
      [string]
      $attributeName,
      [Parameter(Mandatory)]
      [string]
      $settings,
      [Parameter(Mandatory)]
      [bool]
      $overwriteExisting
   )
   
   $searchAttributeSettingRecord = $null

   # Columns to return
   $properties = @(
      'searchattributesettingsid', 
      'entityname', 
      'attributename', 
      'settings')

   $select = '?$select=' + ($properties -join ',')
   $filter = '&$filter=entityname eq ''{0}'' and attributename eq ''{1}''' -f $entityName, $attributeName

   $searchAttributeSettingRecords = (Get-Records `
         -setName 'searchattributesettingses' `
         -query ($select + $filter)).value

   if ($searchAttributeSettingRecords.Count -gt 1) {

      $invalidRecordException = @()
      $invalidRecordException += 'More than one record is found in searchattributesettings'
      $invalidRecordException += 'with entityname {0} and attributename {1}' -f $entityName, $attributeName
      throw $invalidRecordException -join ' '
   }
   if ($searchAttributeSettingRecords.Count -eq 1) { 
      $searchAttributeSettingRecord = $searchAttributeSettingRecords[0] 
   }
 
   if ($null -ne $searchAttributeSettingRecord) {

      $currentSettings = $searchAttributeSettingRecord.settings

      $recordId = $searchAttributeSettingRecord.searchattributesettingsid

      if (!$overwriteExisting) {
         $message = @()
         $message += 'An existing record is found in searchattributesettings with entityname:'
         $message += '{0}, attributename: {1} settings: {2}.' -f $entityName, $attributeName, $settings
         $message += 'Please update the value of $overwriteExisting to $true and'
         $message += 'execute the powershell script again.'
         throw $message -join ' '
      }

      # Delete the record because we are going to create a new one
      # Alternatively, you can update the existing record settings column value
      Remove-Record -setName 'searchattributesettingses' -id $recordId

      $removedRecordMessage = @()
      $removedRecordMessage += 'Removed existing record in searchattributesettings with entityname:'
      $removedRecordMessage += '''{0}'', attributename: ''{1}'', settings: ''{2}''.' -f $entityname, $attributename, $currentSettings
      Write-Host ($removedRecordMessage -join ' ')
   }

   # Properties for the new record.
   $searchAttributeSettingsBody = @{
      'entityname'    = $entityName
      'attributename' = $attributeName
      'settings'      = $settings
   }
    
   # Create the new record
   New-Record `
      -setName 'searchattributesettingses' `
      -body $searchAttributeSettingsBody `
   | Out-Null # We don't need the record id

   $createdRecordMessage = @()
   $createdRecordMessage += 'Created new record in searchattributesettings with entityname'
   $createdRecordMessage += '''{0}'', attributename ''{1}'', settings ''{2}''.' -f $entityname, $attributename, $settings
   Write-Host ($createdRecordMessage -join ' ')
}
```

---

## Create a custom analyzer

When you aren't getting the results from Dataverse search that you expect, and none of the built-in Azure AI Search analyzers do what you need, you can build and configure a custom search analyzer. It's important to understand what an Azure AI Search custom analyzer is and how to build one that can be applied to your power platform environment so that Dataverse search can to return data as expected by your users. Refer to [Add custom analyzers to string fields](/azure/search/index-add-custom-analyzers) to learn more on what an Azure custom analyzer is and how it helps return the best results for your users.

## Enable the custom analyzer for Dataverse Search

After creating a custom search analyzer, you must enable it for Dataverse search by adding the definition of the analyzer in the [SearchCustomAnalyzer table](../reference/entities/searchcustomanalyzer.md) and populate the [SearchAttributeSettings table](../reference/entities/searchattributesettings.md) with the data to use the custom analyzer as described in [Set an analyzer for a column](#set-an-analyzer-for-a-column).

> [!NOTE]
> The [SearchCustomAnalyzer table](../reference/entities/searchcustomanalyzer.md) must contain no more than one row of data. By default it has no data. If more than one row is added, people using Dataverse search will get errors.
>
> You can't upload a custom analyzer using [Power Apps](https://make.powerapps.com), you need to use code to upload the file containing the custom analyzer.


## Set the custom analyzer definition

You will need to update the [SearchCustomAnalyzer table](../reference/entities/searchcustomanalyzer.md). To update the table you will need to add the name of the analyzer and the .json file with the definitions into the table.

The following example code includes logic to ensure that no more than one row exists in the `searchcustomanalyzer` table, and that any existing row isn't overwritten accidentally.

### [SDK for .NET](#tab/sdk)


```csharp
/// <summary>
/// Sets the custom analyzers for a Dataverse environment
/// </summary>
/// <param name="service">The authenticated IOrganizationService instance</param>
/// <param name="customAnalyzerFile">Information about the file containing custom analyzers </param>
/// <param name="customAnalyzerName">The name for the custom analyzer record</param>
/// <param name="overwriteExisting">Whether to update an existing custom analyzer if found.</param>
/// <param name="isValidCustomAnalyzer">Whether the caller asserts that the custom analyzer file is valid.</param>
/// <exception cref="Exception"></exception>
static void SetSearchCustomAnalyzer(
   IOrganizationService service,
   FileInfo customAnalyzerFile,
   string customAnalyzerName,
   bool overwriteExisting,
   bool isValidCustomAnalyzer)
{

   if (!isValidCustomAnalyzer)
   {
         string message = "Please make sure the names of the custom analyzers, char filters, tokenizers and token filters";
         message += "defined in the file start with 'msdyn_search_' ";
         message += "and make sure the file is in a valid json format ";
         message += "by checking the file content in https://jsonviewer.stack.hu/. ";
         message += "Please update the value of validCustomAnalyzer ";
         message += "to true and execute SetSearchCustomAnalyzer again.";

         throw new Exception(message);
   }

   try
   {
         // Check if there are any existing records
         QueryExpression query = new("searchcustomanalyzer")
         {
            TopCount = 2,
            ColumnSet = new("searchcustomanalyzerid")
         };

         EntityCollection entityCollection = service.RetrieveMultiple(query);

         if (entityCollection.Entities.Count > 1)
         {
            throw new Exception("There should be exactly one record in the searchcustomanalyzer table.");
         }
         if (entityCollection.Entities.Count == 1)
         {
            //There is one record

            Guid searchCustomAnalyzerRecordId = entityCollection.Entities[0].Id;

            if (!overwriteExisting)
            {
               string message = "An existing record is found in searchcustomanalyzer.";
               message += "Please make sure the existing custom analyzers are ";
               message += "not changed or deleted in the uploaded file. ";
               message += "You can add new custom analyzers to the file. ";
               message += "Please update the value of overwriteExisting ";
               message += "to true and execute the SetSearchCustomAnalyzer again.";

               throw new Exception(message);
            }

            //Delete the existing record
            service.Delete("searchcustomanalyzer", searchCustomAnalyzerRecordId);
         }

         Entity newRecord = new("searchcustomanalyzer")
         {
            Attributes = {
               { "name", customAnalyzerName }
            }
         };

         Guid newRecordId = service.Create(newRecord);
         EntityReference newRecordReference = new("searchcustomanalyzer", newRecordId);

         // Upload the file
         UploadFile(
            service,
            newRecordReference,
            "analyzers",
            customAnalyzerFile,
            "application/json");

   }
   catch (Exception)
   {
         throw;
   }
}
```

The following example shows how to use the static `SetSearchCustomAnalyzer` method to upload a custom analyzer file.

```csharp
SetSearchCustomAnalyzer(
      service: service,
      customAnalyzerFile: new FileInfo("C:\\CustomAnalyzers\\SampleCustomAnalyzers.json"),
      customAnalyzerName: "Sample Custom Analyzer",
      overwriteExisting: true,
      isValidCustomAnalyzer: true
      );
```

[Learn how to use the SDK for .NET](../org-service/quick-start-org-service-console-app.md)


### [Web API](#tab/webapi)

This PowerShell function depends on the following functions described in [Use PowerShell and Visual Studio Code with the Dataverse Web API](../webapi/use-ps-and-vscode-web-api.md)

- `Connect`
- `Get-Records`
- `Remove-Record`
- `New-Record`

- [Learn to create a Connect function](../webapi/use-ps-and-vscode-web-api.md#create-a-connect-function)
- [Learn to create table operations functions](../webapi/use-ps-and-vscode-web-api.md#create-table-operations-functions)

This function also uses the `Set-FileColumn` function to upload the custom analyzer. [Learn more about this function and uploading files to Dataverse](../file-column-data.md#powershell-example-to-upload-file-in-a-single-request)

```powershell
<#
.SYNOPSIS
   Creates or replaces a custom search analyzer.

.DESCRIPTION
   The Set-SearchCustomAnalyzer function creates or replaces a custom search analyzer in 
   the searchcustomanalyzer table.
   - If there is an existing record in the table and the $overwriteExisting 
   parameter is set to $false, an error will be thrown.
   - If there is an existing record and $overwriteExisting is set to $true, 
   the existing record will be removed before creating a new one.
   - The function uploads the custom analyzer file specified by the $customAnalyzerFilePath parameter.

.PARAMETER customAnalyzerFilePath
   Specifies the path to the custom analyzer file to be uploaded.

.PARAMETER overwriteExisting
   Specifies whether to update an existing custom analyzer if found. 
   If set to $true, the existing record will be removed before creating a new one.
   If set to $false and an existing record is found, an error will be thrown.

.EXAMPLE
   Set-SearchCustomAnalyzer `
   -customAnalyzerFilePath "C:\CustomAnalyzers\analyzer.json" `
   -overwriteExisting $true

   This example uploads the custom analyzer file located at "C:\CustomAnalyzers\analyzer.json" and 
   updates the existing custom analyzer if found.
#>
function Set-SearchCustomAnalyzer {
   param (
      [Parameter(Mandatory)]
      [string]
      $customAnalyzerFilePath,
      [Parameter(Mandatory)]
      [string]
      $customAnalyzerName,
      [Parameter(Mandatory)]
      [bool]
      $overwriteExisting,
      [Parameter(Mandatory)]
      [bool]
      $validCustomAnalyzer
   )

   if (!$validCustomAnalyzer) {
      $errorMessage = @()
      $errorMessage += 'Please make sure the names of the custom analyzers, char filters, tokenizers and token filters'
      $errorMessage += 'defined in the file start with ''msdyn_search_'''
      $errorMessage += 'and make sure the file is in a valid json format'
      $errorMessage += 'by checking the file content in https://jsonviewer.stack.hu/.'
      $errorMessage += 'Please update the value of $validCustomAnalyzer'
      $errorMessage += 'to $true and execute the PowerShell script again.'
      throw $errorMessage -join ' '
   }

   $resp = Get-Records `
      -setName 'searchcustomanalyzers' `
      -query '?$select=searchcustomanalyzerid&$top=2&$count=true'

   $searchCustomAnalyzerCount =  $resp.'@odata.count'
   
   if ($searchCustomAnalyzerCount -gt 1) 
   { throw "You should not have more than one record in searchcustomanalyzer table." }
   if ($searchCustomAnalyzerCount -eq 1) {
      if (!$overwriteExisting) {
         $errorMessage = @()
         $errorMessage += 'An existing record was found in searchcustomanalyzer.'
         $errorMessage += 'Please make sure the existing custom analyzers are'
         $errorMessage += 'not changed or deleted in the uploaded file.'
         $errorMessage += 'You can add new custom analyzers to the file.'
         $errorMessage += 'Please update the value of $overwriteExisting'
         $errorMessage += 'to $true and execute the PowerShell script again.'
         throw ($errorMessage -join ' ')
      }

      $searchCustomAnalyzerRecordId = $resp.value[0].searchcustomanalyzerid

      Remove-Record `
         -setName 'searchcustomanalyzers' `
         -id $searchCustomAnalyzerRecordId
      
      Write-Host 'Removed existing record in searchcustomanalyzer.'
   }

   # Create a new record to upload the custom analyzer file.

   $customAnalyzerId = (New-Record `
         -setName 'searchcustomanalyzers' `
         -body @{
         'name' = $customAnalyzerName
      } )[1]
   
   # Upload the analyzer file to the new custom analyzer record.
   try {
      Set-FileColumn `
         -setName 'searchcustomanalyzers' `
         -id $customAnalyzerId `
         -columnName 'analyzers' `
         -file $customAnalyzerFilePath

      Write-Host 'Custom analyzer file is uploaded.'
   }
   catch {
      Write-Host ('Failed to upload Custom Analyzer: {0}' -f $_.Exception.Message) -ForegroundColor Red
   }
}
```

---



<!-- The following stays at the bottom -->

### See also

[Dataverse Search](overview.md)   
[Configure Dataverse search for your environment](/power-platform/admin/configure-relevance-search-organization)   
[Analyzers for text processing in Azure AI Search](/azure/search/search-analyzers)


[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]



