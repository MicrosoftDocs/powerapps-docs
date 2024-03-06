---
title: Join tables using QueryExpression
description: Learn how to use QueryExpression to join tables when you retrieve data from Microsoft Dataverse.
ms.date: 02/29/2024
ms.reviewer: jdaly
ms.topic: how-to
author: pnghub
ms.subservice: dataverse-developer
ms.author: gned
search.audienceType: 
  - developer
contributors:
 - JimDaly
---
# Join tables using QueryExpression

Use the [QueryExpression.LinkEntities](xref:Microsoft.Xrm.Sdk.Query.QueryExpression.LinkEntities) property to describe the data from related tables to return with your query. This property contains a collection of [Query.LinkEntity](xref:Microsoft.Xrm.Sdk.Query.LinkEntity) instances that describe:

Which related table rows to return
Which columns of those records to return
How to filter any records

## Limitations

## Child elements

## Many-to-one relationships

## One-to-many relationships

## Many-to-many relationships

## No relationship

## Find records not in a set

## Use advanced link types?

## Next steps