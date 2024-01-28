---
title: "Write quick find queries"
description: "Learn how to write queries to use Dataverse quick find"
ms.date: 01/25/2024
ms.reviewer: jdaly
ms.topic: article
author: pnghub
ms.subservice: dataverse-developer
ms.author: gned
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# Write quick find queries

Model-driven apps provide experiences to quickly find records using [quick find search](../../user/quick-find.md) or [Grid search](../../user/grid-filters.md#grid-search). With these experiences, users have a single text input that can be applied to multiple columns in a single table.

Model-driven apps also provide a search box that uses the [Dataverse search APIs](search/overview.md) when Dataverse search is enabled. With Dataverse search, the results can include results from multiple tables for a more relevant search capability. When Dataverse search is not enabled, model-driven apps provide a [multiple-table quick find (categorized search)](../../user/quick-find.md#multiple-table-quick-find-categorized-search) experience that combines results of up to 10 quick find queries. [Learn more about search options available for model-driven apps.](../../user/search.md)

> [!NOTE]
> Consider using the Dataverse search APIs instead of quick find queries for the following scenarios:
>
> - [Relevance search on multiple tables](search/query.md)
> - [Populating a drop-down with suggestions as people type](search/suggest.md)
> - [Autocomplete text suggestions as people type in a search box](search/autocomplete.md)

## Write a quick find query

Quick find queries use the following pattern:

1. They include a single filter using an 'OR' filter operator.

   - With FetchXml, the [filter element](fetchxml/reference/filter.md) `type` attribute is set to `'or'`.
   - With [QueryExpression](xref:Microsoft.Xrm.Sdk.Query.QueryExpression), the  [FilterExpression.FilterOperator](xref:Microsoft.Xrm.Sdk.Query.FilterExpression.FilterOperator) is set to [LogicalOperator.Or](xref:Microsoft.Xrm.Sdk.Query.LogicalOperator.Or).
   
   You can add additional filters, but they will be evaluated only after the quick find filter results are processed.

1. The 'OR' filter is marked as a quick find filter:

   - With FetchXml, the [filter element](fetchxml/reference/filter.md) `isquickfindfields` attribute is set to `'1'`. 
   - With [QueryExpression](xref:Microsoft.Xrm.Sdk.Query.QueryExpression), the [FilterExpression.IsQuickFindFilter](xref:Microsoft.Xrm.Sdk.Query.FilterExpression.IsQuickFindFilter) is set to `true`.

1. The filter has more than one condition. When only one condition is evaluated, the query will have better performance when it is processed as an ordinary query.
1. All of the conditions within the filter use the 'Like' operator:

   - With FetchXml, the [condition element](fetchxml/reference/condition.md) `operator` attribute is set to `'like'`.
   - With [QueryExpression](xref:Microsoft.Xrm.Sdk.Query.QueryExpression), [ConditionExpression.Operator](xref:Microsoft.Xrm.Sdk.Query.ConditionExpression.Operator) uses [ConditionOperator.Like](xref:Microsoft.Xrm.Sdk.Query.ConditionOperator.Like).

   The 'like' operator requires a search string that ends with `%`.

   > [!NOTE]
   > The 'Like' operator is the only supported operator for quick find queries. It is the only operator necessary for the application scenarios quick find queries are designed to support. Other operators have not been tested.

## Examples

How you write a quick find query depends on whether you are using [QueryExpression](xref:Microsoft.Xrm.Sdk.Query.QueryExpression) or FetchXml.

Each of the examples in the tabs below do the same thing:

1. Accept a single search string parameter. This could be a partial name, telephone number, email address, or account number.
1. Create a quick find query that tests the search string against the following account table columns:

   - `telephone2`
   - `telephone1`
   - `emailaddress1`
   - `accountnumber`
   - `name`

1. Filters out accounts that are not active.
1. Orders the results by account name.

### [QueryExpression](#tab/queryexpression)

You can use [QueryExpression](xref:Microsoft.Xrm.Sdk.Query.QueryExpression) with the Dataverse SDK for .NET.

```csharp
/// <summary>
/// Returns active accounts using quick find filter
/// </summary>
/// <param name="service">The authenticated IOrganizationService instance to use.</param>
/// <param name="searchString">The string to search for</param>
/// <returns>Collection of matching account records</returns>
static EntityCollection QuickFindActiveAccountsQueryExpression(
    IOrganizationService service, 
    string searchString)
{
    // Wildcard required for ConditionOperator.Like
    if (!searchString.EndsWith('%'))
    {
        searchString += '%';
    }

    QueryExpression query = new("account")
    {
        ColumnSet = new("accountid",
                        "name",
                        "accountnumber",
                        "primarycontactid",
                        "address1_city",
                        "telephone1",
                        "emailaddress1"),
        Criteria = new()
        {
            Filters =
            {
                new (LogicalOperator.Or)
                {    
                    // Specify Quick find filter
                    IsQuickFindFilter = true,
                    Conditions =
                    {
                        { new (attributeName: "telephone2", 
                            ConditionOperator.Like, 
                            value: searchString) },
                        { new (attributeName: "telephone1", 
                            ConditionOperator.Like, 
                            value: searchString) },
                        { new (attributeName: "emailaddress1", 
                            ConditionOperator.Like, 
                            value: searchString) },
                        { new (attributeName: "accountnumber", 
                            ConditionOperator.Like,
                            value: searchString) },
                        { new (attributeName: "name", 
                            ConditionOperator.Like,
                            value: searchString) }
                    }
                },
                // Condition to be evaluated after Quick find filter
                new (LogicalOperator.And)
                {
                     Conditions =
                    {
                        {new(attributeName:"statecode",
                            ConditionOperator.Equal, 
                            value: 0)}
                    }
                }
            }
        },
        Orders = {
            {
                new(attributeName: "name", 
                    orderType: OrderType.Ascending)
            }
        }
    };

    return service.RetrieveMultiple(query);
}
```

### [FetchXml](#tab/fetchxml)

You can use FetchXml with the Dataverse SDK for .NET or Dataverse Web API.

With the SDK for .NET, this static `QuickFindActiveAccountsFetchXml` method shows how to use [FetchExpression](xref:Microsoft.Xrm.Sdk.Query.FetchExpression) with a quick find query.

```csharp
/// <summary>
/// Returns active accounts using quick find filter with FetchXml
/// </summary>
/// <param name="service">The authenticated IOrganizationService instance to use.</param>
/// <param name="searchString">The string to search for</param>
/// <returns>Collection of matching account records</returns>
static EntityCollection QuickFindActiveAccountsFetchXml(IOrganizationService service, string searchString) {
    
    // Wildcard required for ConditionOperator.Like
    if (!searchString.EndsWith('%'))
    {
        searchString += '%';
    }

    string query = string.Format(@"<fetch>
           <entity name='account'>
              <attribute name='accountid' />
              <attribute name='name' />
              <attribute name='accountnumber' />
              <attribute name='primarycontactid' />
              <attribute name='address1_city' />
              <attribute name='telephone1' />
              <attribute name='emailaddress1' />
              <filter type='or'
                 isquickfindfields='1'>
                 <condition attribute='telephone2'
                    operator='like'
                    value='{0}' />
                 <condition attribute='telephone1'
                    operator='like'
                    value='{0}' />
                 <condition attribute='emailaddress1'
                    operator='like'
                    value='{0}' />
                 <condition attribute='accountnumber'
                    operator='like'
                    value='{0}' />
                 <condition attribute='name'
                    operator='like'
                    value='{0}' />
              </filter>
              <filter type='and'>
                 <condition attribute='statecode'
                    operator='eq'
                    value='0' />
              </filter>
              <order attribute='name'
              descending='false' />
           </entity>
        </fetch>", searchString);

    return service.RetrieveMultiple(new FetchExpression(query));
}
```

This `Get-QuickFindActiveAccounts` PowerShell function demonstrates how to use FetchXml with the Dataverse Web API. The `$baseURI`  and `$baseHeaders` variables are scoped outside this function. [Learn more about creating reusable PowerShell functions that used the Web API](webapi/use-ps-and-vscode-web-api.md#create-reusable-functions)

```powershell
function Get-QuickFindActiveAccounts {
   param (
      [Parameter(Mandatory)] 
      [String] 
      $searchString
   )
   #  Wildcard required for ConditionOperator.Like
   if (!$searchString.EndsWith('%')) {
      $searchString += '%'
   }

   $query = "<fetch>
      <entity name='account'>
         <attribute name='accountid' />
         <attribute name='name' />
         <attribute name='accountnumber' />
         <attribute name='primarycontactid' />
         <attribute name='address1_city' />
         <attribute name='telephone1' />
         <attribute name='emailaddress1' />
         <filter type='or'
            isquickfindfields='1'>
            <condition attribute='telephone2'
               operator='like'
               value='{0}' />
            <condition attribute='telephone1'
               operator='like'
               value='{0}' />
            <condition attribute='emailaddress1'
               operator='like'
               value='{0}' />
            <condition attribute='accountnumber'
               operator='like'
               value='{0}' />
            <condition attribute='name'
               operator='like'
               value='{0}' />
         </filter>
         <filter type='and'>
            <condition attribute='statecode'
               operator='eq'
               value='0' />
         </filter>
         <order attribute='name'
         descending='false' />
      </entity>
   </fetch>" -f $searchString

   $uri = $baseURI + 'accounts?fetchXml=' + [uri]::EscapeUriString($query)
   # Header for GET operations that have annotations
   $getHeaders = $baseHeaders.Clone()
   $getHeaders.Add('If-None-Match', $null)
   $getHeaders.Add('Prefer', 'odata.include-annotations="*"')
   $RetrieveMultipleRequest = @{
      Uri     = $uri
      Method  = 'Get'
      Headers = $getHeaders
   }
   Invoke-RestMethod @RetrieveMultipleRequest
}
```

---


## Quick find limits

Because quick find queries support specific user experiences in applications, they must return results or fail quickly. The user won't wait a long time for results and these queries can use a lot of system resources because they can have conditions on multiple columns of the table. For these reason, quick find queries return an error when the number results exceeds 10,000 rows. The error returned is:

> Name: `QuickFindQueryRecordLimitExceeded`   
> Code: `0x8004E024`   
> Number: `-2147164124`   
> Message: `The number of records for this search exceeds the Quick Search record limit. Please refine your query and try again.`

You don't need to display this error in your application, but you should expect that it can occur. You can mitigate this by:

- Limiting the number of fields searched by your query.
- Include limiting conditions in your query.
- Require the user to enter more characters in the search box to provide fewer total matches.

### How the search item limit is calculated

The search item limit is calculated using *ONLY* the items in the quick find filter. When processing the query, Dataverse detects whether there is a quick find filter and processes it first, even before applying security filters. If the results of the quick find filter exceed 10,000 rows, Dataverse throws the `QuickFindQueryRecordLimitExceeded` exception and no other filters are processed. Adding additional filters to get a smaller total number of records returned will not decrease the potentional of the `QuickFindQueryRecordLimitExceeded` exception. Someone querying a table without privileges to view all the matching records can get this error.


### Bypass the quick find limit

If you need to test a query that exceeds the quick find limit on a temporary basis, use FetchXml to compose the query and set the [filter element](fetchxml/reference/filter.md) `overridequickfindrecordlimitenabled` attribute to `'0'`.

### Organizational override

In extreme cases where a query essential to the business regularly returns the `QuickFindQueryRecordLimitExceeded` exception, an administrator can contact Microsoft Support to request the 10k item limit be disabled. Disabling the limit is not recommended and can result in over consumption of resources and environment wide outages if misused.

### See Also

[Query data using FetchXml](fetchxml/overview.md)   
[Build queries with QueryExpression](org-service/build-queries-with-queryexpression.md)   
[Dataverse search APIs](search/overview.md)