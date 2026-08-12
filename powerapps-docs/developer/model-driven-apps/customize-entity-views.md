---
title: "Customize Views in Model-driven Apps"
description: "Learn how to customize views in model-driven apps by creating, updating, retrieving, and deactivating them. Follow the examples to get started."
author: clromano
ms.author: clromano
ms.reviewer: jdaly
ms.date: 08/10/2026
ms.topic: how-to
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---

# Customize views in model-driven apps

Customize views in model-driven apps programmatically to control which data users retrieve and how the application displays it. Views are [`SavedQuery`](../data-platform/reference/entities/savedquery.md) records that use specific filters and display settings. You can create them in code or define them as XML and import them with an unmanaged solution.

A `SavedQuery` view is different from a [`UserQuery`](../data-platform/reference/entities/userquery.md). A user query, called a **Saved view** in model-driven apps, is owned by an individual user, can be assigned and shared with other users, and can be viewed by other users depending on the query's access privileges. This view type is appropriate for frequently used queries that span table types and queries that perform aggregation. For more information, see [Saved queries](../data-platform/saved-queries.md).

You can also use the customization tool to customize views. For more information, see [Create and edit views](../../maker/model-driven-apps/create-edit-views.md).






<a name="BKMK_TypesOfViews"></a>

## Types of views

The following table lists the five types of views that you can customize. The type code of a view is stored in the `SavedQuery.QueryType` parameter.

When you define views for a specific table, the `SavedQuery.ReturnedTypeCode` parameter returns the table logical name.

|View Type|Type Code|Description|
|---|---|---|
|**Public**|0|- **Occurrence**: Many<br />- **Actions**: Create, Update, Delete<br />- **Comments**: Set one of these views as the default public view by setting `SavedQuery.IsDefault` to true.|
|**Advanced Find**|1|- **Occurrence**: 1<br />- **Actions**: Update only.<br />- **Comments**: By default, this view is displayed when results are shown in **Advanced Find**.|
|**Associated**|2|- **Occurrence**: 1<br />- **Actions**: Update only,<br />- **Comments**: By default, this view is displayed when a grid of related records appears in the navigation pane of a record.|
|**Quick Find**|4|- **Occurrence**: 1<br />- **Actions**: Update only.<br />- **Comments**: This view defines the columns that are searched when a user searches for records by using the search column in a list view.|
|**Lookup**|64|- **Occurrence**: 1<br />- **Actions**: Update only.<br />- **Comments**: This is the default view that's used to look up a record when no other view is configured for the lookup column.|

<a name="BKMK_CreateViews"></a>

## Manage views as solution components

Views are solution components. When you create, update, or delete solution components, you apply the change to the solution that contains them. If you don't explicitly specify a solution, the changes get set [to the preferred solution](../../maker/data-platform/preferred-solution.md) of whoever runs your code. If that person doesn't have a preferred solution, the changes go to one of the [default solutions](/power-apps/maker/data-platform/solutions-overview#default-solutions).

As a developer, use the [`SolutionUniqueName` optional parameter](../data-platform/optional-parameters.md#associate-a-solution-component-with-a-solution) to explicitly associate these data changes with a specific unmanaged solution.



## Create views

To create a public view, specify the following [SavedQuery](../data-platform/reference/entities/savedquery.md) properties:

|Property|Description|
|---|---|
|[`Name`](../data-platform/reference/entities/savedquery.md#BKMK_Name)|A unique identifier for the saved query.|
|[`ReturnedTypeCode`](../data-platform/reference/entities/savedquery.md#BKMK_ReturnedTypeCode)|Matches the logical name of the table.|
|[`FetchXml`](../data-platform/reference/entities/savedquery.md#BKMK_FetchXml)| Edit filter criteria or configure sorting. See [Query data using FetchXml](../data-platform/fetchxml/overview.md).|
|[`LayoutXml`](../data-platform/reference/entities/savedquery.md#BKMK_LayoutXml)|See the `layoutxml` element in the [Customization solutions file schema](../data-platform/customization-solutions-file-schema.md) for the valid elements.|
|[`QueryType`](../data-platform/reference/entities/savedquery.md#BKMK_QueryType)|Must always be zero (0).|


The following sample creates a new public view for the [Opportunity table](/dynamics365/developer/reference/entities/opportunity):

### [SDK for .NET](#tab/sdk)

This sample uses the [IOrganizationService.Execute method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute(Microsoft.Xrm.Sdk.OrganizationRequest)) with the [CreateRequest class](xref:Microsoft.Xrm.Sdk.Messages.CreateRequest) and the [`SolutionUniqueName` optional parameter](../data-platform/optional-parameters.md#associate-a-solution-component-with-a-solution).

```csharp
System.String layoutXml =
@"<grid name='resultset' object='3' jump='name' select='1'
   preview='1' icon='1'>
   <row name='result' id='opportunityid'>
   <cell name='name' width='150' />
   <cell name='customerid' width='150' />
   <cell name='estimatedclosedate' width='150' />
   <cell name='estimatedvalue' width='150' />
   <cell name='closeprobability' width='150' />
   <cell name='opportunityratingcode' width='150' />
   <cell name='opportunitycustomeridcontactcontactid.emailaddress1'
      width='150' disableSorting='1' />
   </row>
</grid>";

System.String fetchXml =
@"<fetch>
   <entity name='opportunity'>
   <order attribute='estimatedvalue' descending='false' />
   <filter type='and'>
      <condition attribute='statecode' operator='eq'
      value='0' />
   </filter>
   <attribute name='name' />
   <attribute name='estimatedvalue' />
   <attribute name='estimatedclosedate' />
   <attribute name='customerid' />
   <attribute name='opportunityratingcode' />
   <attribute name='closeprobability' />
   <link-entity alias='opportunitycustomeridcontactcontactid'
      name='contact' from='contactid' to='customerid'
      link-type='outer' visible='false'>
      <attribute name='emailaddress1' />
   </link-entity>
   <attribute name='opportunityid' />
   </entity>
</fetch>";

var sq = new SavedQuery
   {
   Name = "A New Custom Public View",
   Description = "A Saved Query created in code",
   ReturnedTypeCode = "opportunity",
   FetchXml = fetchXml,
   LayoutXml = layoutXml,
   QueryType = 0
   };

var request = new CreateRequest
{
   Target = sq
};
request["SolutionUniqueName"] = "< Your Solution Unique Name >";

var response = (CreateResponse)service.Execute(request);
_customViewId = response.id;
Console.WriteLine("A new view with the name {0} was created.", sq.Name);
```

[Learn more about the Dataverse SDK for .NET](../data-platform/org-service/overview.md)

### [Dataverse CLI](#tab/cli)

This example uses the Dataverse CLI [api request](../data-platform/cli/reference.md#api-request-command) with the [`MSCRM.SolutionUniqueName` optional parameter](../data-platform/optional-parameters.md#associate-a-solution-component-with-a-solution).

```powershell
$solutionUniqueName = "< Your Solution Unique Name >"

$layoutXml = @"
<grid name='resultset' object='3' jump='name' select='1'
  preview='1' icon='1'>
  <row name='result' id='opportunityid'>
    <cell name='name' width='150' />
    <cell name='customerid' width='150' />
    <cell name='estimatedclosedate' width='150' />
    <cell name='estimatedvalue' width='150' />
    <cell name='closeprobability' width='150' />
    <cell name='opportunityratingcode' width='150' />
    <cell name='opportunitycustomeridcontactcontactid.emailaddress1'
      width='150' disableSorting='1' />
  </row>
</grid>
"@

$fetchXml = @"
<fetch>
  <entity name='opportunity'>
    <order attribute='estimatedvalue' descending='false' />
    <filter type='and'>
      <condition attribute='statecode' operator='eq' value='0' />
    </filter>
    <attribute name='name' />
    <attribute name='estimatedvalue' />
    <attribute name='estimatedclosedate' />
    <attribute name='customerid' />
    <attribute name='opportunityratingcode' />
    <attribute name='closeprobability' />
    <link-entity alias='opportunitycustomeridcontactcontactid'
      name='contact' from='contactid' to='customerid'
      link-type='outer' visible='false'>
      <attribute name='emailaddress1' />
    </link-entity>
    <attribute name='opportunityid' />
  </entity>
</fetch>
"@

$body = @{
  name             = "A New Custom Public View"
  description      = "A Saved Query created in code"
  returnedtypecode = "opportunity"
  fetchxml         = $fetchXml
  layoutxml        = $layoutXml
  querytype        = 0
}

$jsonBody = ConvertTo-Json $body -Depth 5 -Compress

$response = dataverse api request `
  --target dataverse `
  --path "/api/data/v9.2/savedqueries" `
  --method POST `
  --header "MSCRM.SolutionUniqueName:$solutionUniqueName" `
  --body $jsonBody `
  --include

$entityIdHeader = $response |
  Select-String -Pattern 'OData-EntityId:\s*(?<url>\S+)' |
  Select-Object -First 1

if (-not $entityIdHeader) {
  throw 'The response did not contain an OData-EntityId header.'
}

$entityUrl = $entityIdHeader.Matches[0].Groups['url'].Value
$idMatch = Select-String -InputObject $entityUrl -Pattern '(?<=\().*?(?=\))'

if (-not $idMatch.Matches.Success) {
  throw "The OData-EntityId header did not contain a record ID: $entityUrl"
}

$customViewId = [guid]::New($idMatch.Matches.Value.ToString())

Write-Host "A new view with the name "$($body.name)" and ID {$customViewId} was created."
```

[Learn more about the Dataverse CLI](../data-platform/cli/index.md)

---

<a name="BKMK_UpdateViews"></a>

## Update views

If the [`IsCustomizable`](../data-platform/reference/entities/savedquery.md#BKMK_IsCustomizable) managed property allows the view to be updated, use the [UpdateRequest class](xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest) message to update the view.  Always update views in the context of a solution. Use the [`SolutionUniqueName` optional parameter](../data-platform/optional-parameters.md#associate-a-solution-component-with-a-solution) to associate the change to a view with a solution.

For an update example, see [Deactivate views](#deactivate-views)

<a name="BKMK_DeleteViews"></a>

## Delete views

You should only delete saved queries that you created. A solution component or part of the application might depend on a specific saved query. If there are queries you don't want to appear in the application, deactivate them.  Always delete views in the context of a solution. Use the [`SolutionUniqueName` optional parameter](../data-platform/optional-parameters.md#associate-a-solution-component-with-a-solution) to associate the deletion of a view with a solution.

<a name="BKMK_RetrieveViews"></a>

## Retrieve views



The following samples retrieve all the public views for the [Opportunity table](/dynamics365/developer/reference/entities/opportunity):


### [SDK for .NET](#tab/sdk)

This example uses a [RetrieveMultipleRequest class](xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest) with the [IOrganizationService.Execute method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute\*) to retrieve saved query records.

```csharp
var mySavedQuery = new QueryExpression
{
   ColumnSet = new ColumnSet(
       "savedqueryid",
       "name",
       "querytype",
       "isdefault",
       "returnedtypecode",
       "isquickfindquery"),
   EntityName = SavedQuery.EntityLogicalName,
   Criteria = new FilterExpression
   {
       Conditions =
       {
           new ConditionExpression
           {
               AttributeName = "querytype",
               Operator = ConditionOperator.Equal,
               Values = { 0 }
           },
           new ConditionExpression
           {
               AttributeName = "returnedtypecode",
               Operator = ConditionOperator.Equal,
               Values = { Opportunity.EntityTypeCode }
           }
       }
   }
};
RetrieveMultipleRequest retrieveSavedQueriesRequest = new RetrieveMultipleRequest { Query = mySavedQuery };

RetrieveMultipleResponse retrieveSavedQueriesResponse =
   (RetrieveMultipleResponse)service.Execute(retrieveSavedQueriesRequest);

DataCollection<Entity> savedQueries = retrieveSavedQueriesResponse.EntityCollection.Entities;

// Display the retrieved views
foreach (Entity ent in savedQueries)
{
   SavedQuery rsq = (SavedQuery)ent;
   Console.WriteLine(
       "{0} : {1} : {2} : {3} : {4} : {5},",
       rsq.SavedQueryId,
       rsq.Name,
       rsq.QueryType,
       rsq.IsDefault,
       rsq.ReturnedTypeCode,
       rsq.IsQuickFindQuery);
}
```

[Learn more about the Dataverse SDK for .NET](../data-platform/org-service/overview.md)

### [Dataverse CLI](#tab/cli)

This example uses the [`data query` command](../data-platform/cli/reference.md#data-query-command) to retrieve saved query records.

```powershell
$selectColumns = @(
  'savedqueryid'
  'name'
  'querytype'
  'isdefault'
  'returnedtypecode'
  'isquickfindquery'
) -join ','

$filter = "querytype eq 0 and returnedtypecode eq 'opportunity'"

$response = dataverse data query `
  --target dataverse `
  --table savedqueries `
  --select $selectColumns `
  --filter $filter `
  --json | ConvertFrom-Json

$response.value | Select-Object `
  savedqueryid, `
  name, `
  querytype, `
  isdefault, `
  returnedtypecode, `
  isquickfindquery | Format-Table -AutoSize
```

[Learn more about the Dataverse CLI](../data-platform/cli/index.md)

---

<a name="BKMK_DeactivateViews"></a>

## Deactivate views

If you don't want a public view to appear in the application, deactivate it. You can't deactivate a public view that is set as the default view. 

Deactivation is an update operation. Always update views in the context of a solution. Use the [`SolutionUniqueName` optional parameter](../data-platform/optional-parameters.md#associate-a-solution-component-with-a-solution) to associate the change to a view with a solution.

The following sample deactivates the **Closed Opportunities in Current Fiscal Year** view for the [Opportunity table](/dynamics365/developer/reference/entities/opportunity):

### [SDK for .NET](#tab/sdk)

This sample uses the [IOrganizationService.Execute method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute(Microsoft.Xrm.Sdk.OrganizationRequest)) with the [UpdateRequest class](xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest) and the [`SolutionUniqueName` optional parameter](../data-platform/optional-parameters.md#associate-a-solution-component-with-a-solution).

```csharp
System.String SavedQueryName = "Closed Opportunities in Current Fiscal Year";
QueryExpression ClosedOpportunitiesViewQuery = new QueryExpression
{
   ColumnSet = new ColumnSet("savedqueryid", "statecode", "statuscode"),
   EntityName = SavedQuery.EntityLogicalName,
   Criteria = new FilterExpression
   {
       Conditions =
       {
           new ConditionExpression
           {
               AttributeName = "querytype",
               Operator = ConditionOperator.Equal,
               Values = { 0 }
           },
           new ConditionExpression
           {
               AttributeName = "returnedtypecode",
               Operator = ConditionOperator.Equal,
               Values = { Opportunity.EntityTypeCode }
           },
           new ConditionExpression
           {
               AttributeName = "name",
               Operator = ConditionOperator.Equal,
               Values = { SavedQueryName }
           }
       }
   }
};

RetrieveMultipleRequest retrieveOpportuntiesViewRequest = new RetrieveMultipleRequest
{
   Query = ClosedOpportunitiesViewQuery
};

RetrieveMultipleResponse retrieveOpportuntiesViewResponse =
   (RetrieveMultipleResponse)service.Execute(retrieveOpportuntiesViewRequest);

SavedQuery OpportunityView =
   (SavedQuery)retrieveOpportuntiesViewResponse.EntityCollection.Entities[0];

var updateRequest = new UpdateRequest
{
  Target = new SavedQuery
  {
    Id = OpportunityView.Id,
    StateCode = new OptionSetValue(1), // Inactive
    StatusCode = new OptionSetValue(2) // Inactive
  }
};
updateRequest["SolutionUniqueName"] = "< Your Solution Unique Name >";

service.Execute(updateRequest);
```

[Learn more about the Dataverse SDK for .NET](../data-platform/org-service/overview.md)

### [Dataverse CLI](#tab/cli)

This example uses the Dataverse CLI [api request](../data-platform/cli/reference.md#api-request-command) with the [`MSCRM.SolutionUniqueName` optional parameter](../data-platform/optional-parameters.md#associate-a-solution-component-with-a-solution).


```powershell
$solutionUniqueName = "< Your Solution Unique Name >"

$savedQueryName = "Closed Opportunities in Current Fiscal Year"
$escapedSavedQueryName = $savedQueryName.Replace("'", "''")

$selectColumns = @(
  'savedqueryid'
  'statecode'
  'statuscode'
) -join ','

$filter = @(
  'querytype eq 0'
  "returnedtypecode eq 'opportunity'"
  "name eq '$escapedSavedQueryName'"
) -join ' and '

$queryOutput = dataverse data query `
  --target dataverse `
  --table savedqueries `
  --select $selectColumns `
  --filter $filter `
  --top 1 `
  --json 2>&1

if ($LASTEXITCODE -ne 0) {
  $errorDetails = $queryOutput -join [Environment]::NewLine
  throw "Failed to retrieve view '$savedQueryName':`n$errorDetails"
}

try {
  $response = $queryOutput | ConvertFrom-Json -ErrorAction Stop
}
catch {
  throw "Failed to parse the query response: $($_.Exception.Message)"
}

$opportunityView = $response.value | Select-Object -First 1
if ($null -eq $opportunityView) {
  throw "The view '$savedQueryName' wasn't found."
}

$body = @{
  statecode  = 1
  statuscode = 2
} | ConvertTo-Json

$updateOutput = dataverse api request `
  --target dataverse `
  --path "/api/data/v9.2/savedqueries($($opportunityView.savedqueryid))" `
  --method PATCH `
  --header "MSCRM.SolutionUniqueName:$solutionUniqueName" `
  --body $body 2>&1

if ($LASTEXITCODE -ne 0) {
  $errorDetails = $updateOutput -join [Environment]::NewLine
  throw "Failed to update view '$savedQueryName':`n$errorDetails"
}

Write-Host "The state of view '$savedQueryName' was updated."
```

[Learn more about the Dataverse CLI](../data-platform/cli/index.md)

---

> [!NOTE]
> The view state: `active` or `inactive` isn't included with the view when you add it to a solution. Therefore, when you import the solution into a target organization, the status is set to active by default.

<a name="BKMK_EditColumns"></a>

## Edit columns

You can select columns to display in views from the table or related tables.
For more information about how to specify the columns to display, see the `layoutxml` element in the [Customization solutions file schema](../data-platform/customization-solutions-file-schema.md).

<a name="BKMK_CustomIcons"></a>

## Add custom icons and tooltips to view columns

You can add a custom icon with tooltip text to display in a column depending on the column value. You can also specify localized tooltip text. Add the custom icons as image web resources in your instance, and then use a JavaScript web resource to add JavaScript code for a column to display the icons depending on the column value.

> [!NOTE]
> You can add custom icons with tooltips only to read-only grids. This feature isn't supported for editable grids. For more information about editable grids, see [Use editable grids](./use-editable-grids.md).

Two new parameters, `imageproviderwebresource` and `imageproviderfunctionname`, are added to the `cell` element of the layoutxml of
savedquery. These parameters let you specify the name of a web resource
and a JavaScript function name to display custom icons and tooltip text for a column.
The JavaScript code runs when the page loads.

You can also use the new **Web Resource** and **Function Name** in the **Column Properties** page while modifying the property of a column in a view definition to specify the web resource name and JavaScript function name.

The following sample code demonstrates how you can programmatically specify a web resource and a JavaScript function name for adding custom icons and tooltips for the [`opportunityratingcode` column](/dynamics365/developer/reference/entities/opportunity#BKMK_OpportunityRatingCode) in layoutxml:


```xml
<grid name='resultset' object='3' jump='name' select='1'
  preview='1' icon='1'>
  <row name='result' id='opportunityid'>
    <cell name='name' width='150' />
    <cell name='customerid' width='150' />
    <cell name='estimatedclosedate' width='150' />
    <cell name='estimatedvalue' width='150' />
    <cell name='closeprobability' width='150' />
    <cell name='opportunityratingcode' width='150' 
          imageproviderwebresource='new_SampleWebResource'
          imageproviderfunctionname='displayIconTooltip' />
    <cell name='opportunitycustomeridcontactcontactid.emailaddress1'
        width='150' disableSorting='1' />
  </row>
</grid>
```

The JavaScript function for displaying custom icons and tooltip text expects the following two arguments: the entire row object specified in layoutxml and the calling user's Locale ID (LCID). The LCID parameter enables you to specify tooltip text for the icon in multiple languages. For more information about the supported languages, see [Regional and language options for your environment](/power-platform/admin/enable-languages). For a list of locale ID (LCID) values that you can use in your code, see [Locale IDs assigned by Microsoft](</previous-versions/windows/embedded/ms912047(v=winembedded.10)>).

Assuming you add custom icons for a choice type of column because it has a limited set of predefined options, use the integer value of the options instead of the label to avoid breaking the code due to changes in the localized label string. In your JavaScript function, specify just the name of an image web resource that you want to use as an icon for a value in the column. The image should be 16x16 pixels. Larger images are automatically scaled down to 16x16 pixels.

The following sample code displays different icons and tooltip text based on one of the values (1: Hot, 2: Warm, 3: Cold) in the `opportunityratingcode (Rating)` column. The sample code also shows how to display localized tooltip text. For this sample to work, you must create three image web resources each with 16x16 images (:::image type="icon" source="media/dynamics365hotgridicon.png":::, :::image type="icon" source="media/dynamics365warmgridicon.png":::, and :::image type="icon" source="media/dynamics365coldgridicon.png":::) in your instance with the following names respectively: `new_Hot`, `new_Warm`, and `new_Cold`.

```javascript
function displayIconTooltip(rowData, userLCID) {
  var str = JSON.parse(rowData);
  var coldata = str.opportunityratingcode_Value;
  var imgName = "";
  var tooltip = "";
  switch (parseInt(coldata, 10)) {
    case 1:
      imgName = "new_Hot";
      switch (userLCID) {
        case 1036:
          tooltip = "French: Opportunity is Hot";
          break;
        default:
          tooltip = "Opportunity is Hot";
          break;
      }
      break;
    case 2:
      imgName = "new_Warm";
      switch (userLCID) {
        case 1036:
          tooltip = "French: Opportunity is Warm";
          break;
        default:
          tooltip = "Opportunity is Warm";
          break;
      }
      break;
    case 3:
      imgName = "new_Cold";
      switch (userLCID) {
        case 1036:
          tooltip = "French: Opportunity is Cold";
          break;
        default:
          tooltip = "Opportunity is Cold";
          break;
      }
      break;
    default:
      imgName = "";
      tooltip = "";
      break;
  }
  var resultarray = [imgName, tooltip];
  return resultarray;
}
```

This results in displaying the values in the `Rating` column with appropriate icons depending on the value, and icon tooltip text when you hover over the icons.

:::image type="content" source="media/customiconsinviews.png" alt-text="Screenshot of custom icons displayed in the Rating column of a view.":::

<a name="BKMK_SetAsDefault"></a>

## Set a public view as the default view

You can set only one active public view as the default view. To make a view the default view, set the [`IsDefault` property](../data-platform/reference/entities/savedquery.md#BKMK_IsDefault) to true.


## Community tools

There are several community tools that use these APIs to manage views:

- [XrmToolBox View Layout Replicator](https://www.xrmtoolbox.com/plugins/MsCrmTools.ViewLayoutReplicator/)
- [XrmToolBox View Renamer](https://www.xrmtoolbox.com/plugins/Carfup.XTBPlugins.ViewRenamer/)
- [XrmToolBox View Transfer Tool](https://www.xrmtoolbox.com/plugins/DamSim.ViewTransferTool/)
- [Power Platform ToolBox View Layout Copier](https://www.powerplatformtoolbox.com/tools/5d42d392-776c-4ff5-bc0d-65f0492d7ed6)

> [!NOTE]
> These community tools aren't a product of Dataverse, and Microsoft doesn't provide support for the community tools. 
> If you have questions about a tool, contact the publisher. More Information: [Community tools](../../maker/model-driven-apps/community-tools.md)



[!INCLUDE[footer-include](../../includes/footer-banner.md)]
