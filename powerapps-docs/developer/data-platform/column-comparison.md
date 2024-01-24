---
title: Use column comparison in queries
description: Learn how to compare columns when querying business data in Microsoft Dataverse.
ms.date: 01/09/2024
ms.topic: how-to
author: pnghub
ms.author: gned
ms.reviewer: pehecke
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
ms.custom: bap-template
---

# Use column comparison in queries

In Microsoft Dataverse, users can perform a column comparison for the
following condition operators using FetchXML, Web API, or [QueryExpression](xref:Microsoft.Xrm.Sdk.Query.QueryExpression) using the SDK for .NET.


|FetchXml|Web API|ConditionOperator|
|---------|---------|---------|
|`eq`|`eq`|<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator.Equal>|
|`ne`|`ne`|<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator.NotEqual>|
|`gt`|`gt`|<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator.GreaterThan>|
|`ge`|`ge`|<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator.GreaterEqual>|
|`lt`|`lt`|<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator.LessThan>|
|`le`|`le`|<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator.LessEqual>|

These operators allow the comparison of a column against a specific value and return all found records, or allow the comparison of two columns to return all records with a matching value.

## Limitations

Dataverse column comparison has the following limitations:

- With Web API and [QueryExpression](xref:Microsoft.Xrm.Sdk.Query.QueryExpression), and you can only compare columns within a single table.

   With FetchXml, you can compare columns in other related tables. See [Cross table comparisons](#cross-table-comparisons).

- Only two columns can be compared at a time.
- Multi-value condition operators aren't supported (that is, "in").
- Extended condition operators aren't supported (that is, "creditlimit \> spends+1000").
- Incompatible column comparison isn't supported. For example, "int vs. int" columns is a valid comparison but "int vs. string" columns isn't a valid comparison.

## Column comparison using FetchXML

The following example shows how to compare columns using FetchXML.

```xml
<fetch>
  <entity name='contact' >
    <attribute name='firstname' />
    <filter>
      <condition attribute='firstname' operator='eq' valueof='lastname'/>
    </filter>
  </entity>
</fetch>
```

For FetchXML, the `valueof` attribute the condition element specifies the name of the column to compare with the selected column. In the previous example, the `firstname` column is being compared against the `lastname` column and returns any records that contain
the same value across both columns.

## Cross table comparisons

With FetchXML only, you can compare field values in related tables. The following example returns rows where the contact `fullname` column matches the account `name` column.

```xml
<fetch> 
  <entity name='contact'>
    <attribute name='contactid' />
    <attribute name='fullname' />
    <filter type='and'>
      <condition attribute='fullname' operator='eq' valueof='acct.name' />
    </filter>
    <link-entity name='account' from='accountid' to='parentcustomerid' link-type='outer' alias='acct'>
      <attribute name='name' />
    </link-entity>
  </entity>
</fetch>
```

The `link-entity` element must use an `alias` attribute and the value of the `valueof` parameter must reference that alias and the column name in the related table.


### See Also

[Column comparison using the Web API](webapi/query-data-web-api.md#column-comparison)<br />
[Column comparison using the SDK](org-service/use-conditionexpression-class.md#column-comparison)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
