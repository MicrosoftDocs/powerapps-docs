---
title: "Use column comparison in queries (Common Data Service) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to compare columns when querying business data." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 07/08/2020
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "NHelgren" # GitHub ID
ms.author: "nhelgren" # MSFT alias of Microsoft employees only
manager: "mayadu" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Use column comparison in queries

In the Common Data Service, users can perform a column comparison for the
following condition operators using FetchXML, Web API, or the SDK API:

- Equal
- NotEqual
- GreaterThan
- GreaterEqual
- LessThan
- LessEqual

This will allow the comparison of an attribute against a specific value and
return all found records, or allow the comparison of two attributes to return
all records with a matching value.

## Limitations

Listed below are the limitations for the current Common Data Service column comparison support.

- You can only compare columns within a single entity
- Only two columns may be compared at a time.
- Multi-value condition operators are not supported (i.e., "in").
- Extended condition operators are not supported (i.e., "creditlimit \> spends+1000").
- Incompatible attribute comparison is not supported. For example, "int vs. int" attributes is a valid comparison but "int vs. string" attributes is not a valid comparison.

## Column comparison using FetchXML

The following example shows how to compare columns using FetchXML:

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

For FetchXML requests, a new node `valueof` has been added inside the condition
node. The `valueof` tag is used to identify the attribute that is being compared
to the selected attribute. In the above example, the 'firstname' column is being
compared against the 'lastname' column and will return any records that contain
the same value across both attributes.

### See Also

[Use FetchXML to construct a query](use-fetchxml-construct-query.md)  
[Column comparison using the Web API](webapi/query-data-web-api.md#column-comparison-using-the-web-api)  
[Column comparison using the SDK API](org-service/use-conditionexpression-class.md#column-comparison-using-the-sdk-api)
