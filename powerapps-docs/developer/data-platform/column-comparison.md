---
title: Use column comparison in queries
description: Learn how to compare columns when querying business data in Microsoft Dataverse.
ms.date: 08/04/2023
ms.topic: how-to
author: NHelgren
ms.author: nhelgren
ms.reviewer: pehecke
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
ms.custom: bap-template
---

# Use column comparison in queries

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

In Microsoft Dataverse, users can perform a column comparison for the
following condition operators using FetchXML, Web API, or the SDK for .NET.


|FetchXml|Web API|ConditionOperator|
|---------|---------|---------|
|`eq`|`eq`|<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator.Equal>|
|`ne`|`ne`|<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator.NotEqual>|
|`gt`|`gt`|<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator.GreaterThan>|
|`ge`|`ge`|<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator.GreaterEqual>|
|`lt`|`lt`|<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator.LessThan>|
|`le`|`le`|<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator.LessEqual>|

This will allow the comparison of a column against a specific value and return all found records, or allow the comparison of two columns to return all records with a matching value.

## Limitations

Dataverse column comparison has the following limitations:

- You can only compare columns within a single table.
- Only two columns may be compared at a time.
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


### See Also

[Column comparison using the Web API](webapi/query-data-web-api.md#column-comparison)<br />
[Column comparison using the SDK](org-service/use-conditionexpression-class.md#column-comparison)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
