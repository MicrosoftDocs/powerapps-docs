---
title: Optimize performance using QueryExpression
description: Learn how to optimize performance when you retrieve data from Microsoft Dataverse using QueryExpression.
ms.date: 08/11/2025
ms.reviewer: jdaly
ms.topic: how-to
author: MsSQLGirl
ms.subservice: dataverse-developer
ms.author: jukoesma
search.audienceType: 
  - developer
contributors:
 - JimDaly
---
# Optimize performance using QueryExpression

For guidance about general things to avoid when composing Dataverse queries, see [Query anti-patterns](../../query-antipatterns.md). The following sections are specific to [QueryExpression](/dotnet/api/microsoft.xrm.sdk.query.queryexpression).

## Query Hints

> [!IMPORTANT]
> Only apply these options when recommended by Microsoft technical support. Incorrect use of these options can damage the performance of a query.

Microsoft SQL Server supports many query hints to optimize queries. [QueryExpression](/dotnet/api/microsoft.xrm.sdk.query.queryexpression)
supports query hints and can pass these query options to SQL Server using the [QueryExpression.QueryHints property](/dotnet/api/microsoft.xrm.sdk.query.queryexpression.queryhints).

[!INCLUDE [cc-query-options](../../includes/cc-query-options.md)]


## No lock

In earlier versions, the [QueryExpression.NoLock property](/dotnet/api/microsoft.xrm.sdk.query.queryexpression.nolock) used to prevent shared locks on records. It's no longer necessary to include this property

## Union Hint

You can improve performance when adding a [FilterExpression](/dotnet/api/microsoft.xrm.sdk.query.filterexpression) that sets the `ConditionExpression` for columns in different tables by setting the [FilterExpression.FilterHint property](/dotnet/api/microsoft.xrm.sdk.query.filterexpression.filterhint) to `union`. But there are some restrictions:

- The [FilterExpression.FilterOperator](/dotnet/api/microsoft.xrm.sdk.query.filterexpression.filteroperator) must use [LogicalOperator](/dotnet/api/microsoft.xrm.sdk.query.logicaloperator)`.Or`.
- Each query can contain only one `union` hint.
- If a `FilterExpression` with `union` hint isn't at top level filter, Dataverse transforms the query and move the filter with a `union` hint to root filter.
- If a `union` hint is more than three levels deep, it's ignored.

The following example sets a filter with the `union` hint on the `telephone1` column for both the [account](../../reference/entities/account.md) and [contact](../../reference/entities/contact.md) tables.

```csharp
QueryExpression query = new("email")
{
   ColumnSet = new ColumnSet("activityid", "subject"),
   Criteria = new FilterExpression(LogicalOperator.And)
   {
      Conditions = {
         {
            new ConditionExpression(
               attributeName:"subject",
               conditionOperator:ConditionOperator.Like,
               value: "Alert:%")
         },
         {
            new ConditionExpression(
               attributeName:"statecode",
               conditionOperator:ConditionOperator.Equal,
               value: 0)
         }
      },
      Filters = {
         {
            new FilterExpression(LogicalOperator.Or){
               FilterHint = "union",
               Conditions = {
                  {
                     new ConditionExpression(
                        attributeName:"telephone1",
                        conditionOperator:ConditionOperator.Equal,
                        value: "555-123-4567"){
                           EntityName = "ac"
                        }
                  },
                  {
                     new ConditionExpression(
                        attributeName:"telephone1",
                        conditionOperator:ConditionOperator.Equal,
                        value: "555-123-4567"){
                           EntityName = "co"
                        }
                  }
               }
            }
         }
      }
   }
};        

LinkEntity linkToAccount = query.AddLink(
      linkToEntityName: "account",
      linkFromAttributeName: "regardingobjectid",
      linkToAttributeName: "accountid",
      joinOperator: JoinOperator.LeftOuter);
linkToAccount.EntityAlias = "ac";

LinkEntity linkToContact = query.AddLink(
      linkToEntityName: "contact",
      linkFromAttributeName: "regardingobjectid",
      linkToAttributeName: "contactid",
      joinOperator: JoinOperator.LeftOuter);
linkToContact.EntityAlias = "co";
```

[!INCLUDE [cc-automatic-query-optimization](../../includes/cc-automatic-query-optimization.md)]

### See also

[Query data using QueryExpression](overview.md)   
[Select columns using QueryExpression](select-columns.md)  
[Join tables using QueryExpression](join-tables.md)  
[Order rows using QueryExpression](order-rows.md)  
[Filter rows using QueryExpression](filter-rows.md)  
[Page results using QueryExpression](page-results.md)   
[Aggregate data using QueryExpression](aggregate-data.md)   
[Count rows using QueryExpression](count-rows.md)   
[Query anti-patterns](../../query-antipatterns.md)

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]