---
title: Understand Record References | Microsoft Docs
description: Work with record references in canvas apps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: anneta
ms.date: 05/05/2019
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Understand Record References in Canvas apps

When writing a research paper in school you would often provide a list of your references at the end.  You didn't include a copy of the actual material you used, but rather a web link, book title and author, or some other means for someone to track down the original information.  Wikipedia articles often include a [long list of references](https://en.wikipedia.org/wiki/Microsoft#References).

In Canvas apps, we often work with copies of records downloaded from data sources.  We use the **First**, **LookUp**, and **Filter** functions and the **Gallery** control's **Selected** property to extract the specific record we want and all the fields of that record are available to us.

Canvas apps also support *Record References*.  Much like a research paper reference, record references refer to a specific record in an entity without having a copy of the record.  Many database systems use a *Primary Key* to uniquely identify a record.  A record reference is similar but combines the primary key and the entity information in which the record appears into a single value.

A record reference can be used to obtain the actual data of the record whenever needed by using the **AsType** function.  Use the **IsType** function to understand which entity the record comes from.

## Common Data Service polymorphic relationships

The Common Data Service supports relationships between records.  Each **Account** record has a **Primary Contact** lookup field to a record in the **Contacts** entity.  The lookup can only refer to a record in **Contacts** and can't refer to a record in say the **Teams** entity.  That last detail is important because we always know what fields will be available for the lookup.

CDS also supports *polymorphic* lookups: the lookup field can refer to records in more than one entity.  For example, the **Owner** field can refer to a record in the **Users** entity or the **Teams** entity.  Each record's lookup field could refer to records in different entities.  Here we don't always know the fields that will be available.

In Canvas app, record references are used to work with polymorphic lookups.

### Owner lookups

### Customer lookups

### Regarding lookups

## Filtering

## Reading

## Writing






  

 