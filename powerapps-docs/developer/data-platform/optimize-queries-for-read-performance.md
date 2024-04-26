---
title: Optimize Queries For Read Performance 
description: Best practices when building queries to retrieve records from Dataverse.
author: dasuss
ms.topic: article
ms.date: 03/28/2024
ms.subservice: dataverse-developer
ms.author: dasuss
ms.reviewer: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
---
# Optimize Queries For Read Performance
<!-- #TODO: This needs to specify SQL Read performance. These tips do not apply to dataverse search -->

Building optimized queries for Dataverse is vital to ensuring a fast, responsive, and reliable experience for your users. This article will describe several things to avoid and to keep in mind when designing queries. 

## Minimize the number of selected columns

Queries which specify "all-attributes" or explicitly adds many columns in the select list may hit performance issues due to the size of the dataset. 

Queries with many logical attributes (for example, lookups) can also cause queries to be slow because each logical attribute needs to be retrieved from a seperate entity which can make a simple query much more complex and slow. 

We recommend customers to design their queries to select the bare minimum of columns needed.

## Avoid leading wild cards in filter conditions

Queries which use conditions with leading wild cards (either explicit , or implicit like with "ends-with") can lead to bad performance. This is because Dataverse can't take advantage of indexes when a query uses leading wild card which leads to table scans. This can happen even if there are other non-leading wild card queries which limit the result set. 

When queries using leading wild cards timeout, a unique error code will be thrown

<!-- Can this link to the current failure text in https://learn.microsoft.com/en-us/power-apps/developer/data-platform/reference/web-service-error-codes -->
<!-- Also we should update the throttle page to link back to here for the different rules -->
```
0x80048644
-2147187132	Name: DataEngineLeadingWildcardQueryThrottling
Message: This query cannot be executed because it conflicts with Query Throttling; the query uses a leading wildcard value in a filter condition, which will cause the query to be throttled more aggressively. Please refer to this document: https://go.microsoft.com/fwlink/?linkid=2162952
```
Dataverse will heavily throttle leading wild card queries which have been identified as a risk to the health of the org to help prevent outages. 

We recommend customers to either use Dataverse search to use leading wild card queries, or look into why leading wild cards are needed and re-architect their model to help users avoid needed leading wild cards.

Example fetchxml which uses a leading wild card: 
``` xml 
<fetch version='1.0' output-format='xml-platform' mapping='logical'>
	<entity name='account'>
		<attribute name='accountid' />
		<attribute name='accountnumber' />
		<filter type='and'>
			<condition attribute='accountnumber' operator='like' value='%234' />
		</filter>
	</entity>
</fetch>
```
For more information about wild card usage see: [Use wildcard characters in conditions for string values](/powerapps-docs/developer/data-platform/wildcard-characters) 

## Avoid using calculated columns in filter conditions

The result of calculcated columns are calculated on the retrieve/retrivemulitple of an entity. These results can't be pre-calcauated which means that filters on these columns will need to calculate and check the value for each possible entity it can return. These filters can lead to non-performant queries which can't be tuned or improved by the platform.

If this pattern is detected in timing out queries we will throw a unique error code to help identify which workflows are using non-performant query patterns. An example error thrown:

<!-- This error text should be updated like Wild Card to link to the throttle page -->
```
0x80048574
-2147187340	Name: ComputedColumnCauseTimeout
Message: The database operation timed out; this may be due to a computed column being used in a filter condition. Please consider removing filter conditions on computed columns, as these filter conditions are expensive and may cause timeouts.
```

Dataverse will heavily throttle queries with filters on calculated columns which have been identified as a risk to the health of the org to help prevent outages. Please see the Query Throttling page for more info about how throttling will impact these queries. [Query throttling (Microsoft Dataverse)](/powerapps-docs/developer/data-platform/query-throttling) 

For more information about calculated columns see [Formula, calculated, and rollup columns using code](powerapps-docs/developer/data-platform/calculated-rollup-attributes) 


## Avoid ordering by Optionsets

When filtering on an optionset (for example statecode), Dataverse will try to filter on the localized label of the optionset to give a more intuitive ordering experience. This leads to Dataverse needing to join and calculate the localized label for each row then order it to provide such an experience. This can lead to a non-performant query.

Dataverse recommends customers to avoid ordering on Optionsets if possible.

Example query ordering on the statecode optionset: 
``` xml
			string fetchxml = @"
<fetch version='1.0' output-format='xml-platform' mapping='logical' distinct='true'>
	<entity name='account'>
		<attribute name='accountnumber' />
		<order attribute='statecode' />
	</entity>
</fetch>
```

## Avoid ordering by link-entity attributes

Ordering by link-entity attributes can lead to sub-optimal query performance due to the added complexity. Ordering by Link-Entiies should only be done when needed to as described here: [Order rows using FetchXml](/powerapps-docs/developer/data-platform/fetchxml/order-rows.md) MicrosoftDocs/powerapps-docs-pr/powerapps-docs/developer/data-platform/fetchxml/order-rows.md

``` xml
<fetch version='1.0' output-format='xml-platform' mapping='logical' distinct='false'>
	<entity name='account'>
		<attribute name='accountnumber' />
    <link-entity name='account' from='accountid' to='parentaccountid' link-type='outer' alias='oaccount'>
        <attribute name='createdby' />
        <order attribute='name' />
    </link-entity>
	</entity>
</fetch>
```


## Avoid using like conditions on Large text columns

Columns like "Description" are defined in Dataverse as large text fields. These fields are too large to effectively index which leads to bad performance when fitlered on via query filter conditions.

Example fetchxml which searches on a large text column: 

``` xml 
<fetch version='1.0' output-format='xml-platform' mapping='logical'>
	<entity name='account'>
		<attribute name='accountid' />
		<attribute name='accountnumber' />
		<filter type='and'>
			<condition attribute='Description' operator='like' value='Sold%' />
		</filter>
	</entity>
</fetch>
```

Dataverse advises to use Dataverse search to handle these kinds of searches if needed.