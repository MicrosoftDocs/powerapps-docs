---
title: "<Topic Title> (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "<Description>" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Query data using the Organization service

<!-- 

Introduce three ways of querying data:

This topic should provide simple examples and content to compare the advantages for each with links to more specific topics in other areas.

https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/org-service/retrieve-data-queries-sdk-assemblies 

-->
## Use FetchXML with FetchExpression
<!-- FetchXML used in both Organization service and web api, so concepts described at a higher shared level -->
## Use QueryExpression

## Use QueryByAttribute

## Access formatted values

<!-- Introduce how to access formatted values in the returned entity collection
 - entity-operations-retrieve will also need to link to that -->

## Other query options

<!-- Refer to other methods: 
1. Use LINQ with OrganizationServiceContext 
1. Execute pre-defined SavedQuery and UserQuery -->


<!-- Related FetchXML topics -->
[FetchXML schema](../fetchxml-schema.md)
[Page large result sets with FetchXML](page-large-result-sets-with-fetchxml.md)
[Use FetchXML aggregation](../use-fetchxml-aggregation.md)
[Use FetchXML to construct a query](../use-fetchxml-construct-query.md)
[Fiscal date and older than datetime query operators in FetchXML](../use-fetchxml-fiscal-date-older-datetime-query-operators.md)
[Use a left outer join in FetchXML to query for records "not in"](../use-fetchxml-left-outer-join-query-records-not-in.md)
<!-- Releated FetchXML samples -->
[Sample: Convert queries between Fetch and QueryExpression](samples/convert-queries-fetch-queryexpression.md)
[Sample: Use aggregation in FetchXML](samples/use-aggregation-fetchxml.md)
[Sample: Use FetchXML with a paging cookie](samples/use-fetchxml-paging-cookie.md)

<!-- Related QueryExpression topics -->
[Build queries with QueryExpression](build-queries-with-queryexpression.md)
[Page large result sets with QueryExpression](page-large-result-sets-with-queryexpression.md)
[Use the QueryExpression class](use-queryexpression-class.md)
[Use the ConditionExpression class](use-conditionexpression-class.md)
[Use the ColumnSet class](use-the-columnset-class.md)
[Use the FilterExpression class](use-filterexpression-class.md)


<!-- Related QueryExpression samples -->
[Sample: Retrieve multiple with the QueryExpression class](samples/retrieve-multiple-queryexpression-class.md)
[Sample: Convert queries between Fetch and QueryExpression](samples/convert-queries-fetch-queryexpression.md)
[Sample: Use QueryExpression with a paging cookie](samples/use-queryexpression-with-a-paging-cookie.md)

<!-- Related QueryByAttribute topics -->
[Use the QueryByAttribute class](use-querybyattribute-class.md)
[Sample: Retrieve multiple with the QueryByAttribute class](samples/retrieve-multiple-querybyattribute-class.md)