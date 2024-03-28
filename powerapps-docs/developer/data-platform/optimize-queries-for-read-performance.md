---
title: Optimize Queries For Read Performance 
description: Best practices when building queries to retrieve records from Dataverse.
author: dasuss
ms.topic: article
ms.date: 03/28/2024
ms.subservice: dataverse-developer
ms.author: dasyss
ms.reviewer: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
---
#TODO: This needs to specify SQL Read performance. These tips do not apply to dataverse search
# Optimize Queries For Read Performance

Building optimized queries for Dataverse is vital to ensuring a fast, responsive, and reliable experience for your users. This article will describe several things to avoid and to keep in mind when designing queries. 


## Minimize the number of selected columns

Queries which specify "all-attributes" or explicitly adds many columns in the select list may hit performance issues due to the size of the dataset. 

Queries with many logical attributes (for example, lookups) can also cause queries to be slow because each logical attribute needs to be retrieved from a seperate entity which can make a simple query much more complex and slow. 

We recommend customers to design their queries to select the bare minimum of columns needed.

## Avoid leading wild cards in filter conditions

Queries which use conditions with leading wild cards (either explicit , or implicit like with "ends-with") can lead to bad performance. This is because Dataverse can't take advantage of indexes when a query uses leading wild card which leads to table scans. This can happen even if there are other non-leading wild card queries which limit the result set. 

Dataverse will heavily throttle leading wild card queries which have been identified as a risk to the health of the org to help prevent outages.  

We recommend customers to either use Dataverse search to use leading wild card queries, or look into why leading wild cards are needed and re-architect their model to help users avoid needed leading wild cards.

## Avoid using calculated columns in filter conditions

Dataverse will heavily throttle queries with filters on calculated columns which have been identified as a risk to the health of the org to help prevent outages.  

## Avoid ordering by Optionsets

When filtering on an optionset (for example statecode), Dataverse will try to filter on the localized label of the optionset to give a more intuitive ordering experience. This leads to Dataverse needing to join and calculate the localized label for each row then order it to provide such an experience. This can lead to a non-performant query.

Dataverse recommends customers to avoid ordering on Optionsets if possible.

## Avoid ordering by link-entity attributes
#TODO: Add link to ordering doc.
Ordering by link-entity attributes can lead to sub-optimal query performance due to the added complexity. Ordering by Link-Entiies should only be done when needed to as described here 

## Avoid using like conditions on Large text columns
#TODO: Does Dataverse search handle this well? Might be better to recommend them to use Dataverse search.


Columns like "Description" are defined in Dataverse as large text fields. These fields are too large to effectively index which leads to bad performance when fitlered on via query filter conditions.

