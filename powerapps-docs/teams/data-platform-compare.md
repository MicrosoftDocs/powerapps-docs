---
title: ***REMOVED*** vs ***REMOVED*** Pro | Microsoft Docs
description: Explains the differences between ***REMOVED*** and ***REMOVED*** Pro.
author: NHelgren
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 08/17/2020
ms.author: nhelgren
ms.reviewer: matp
---

# How are ***REMOVED*** and ***REMOVED*** Pro different?

Applications within a Team have access to a Microsoft ***REMOVED*** environment.  ***REMOVED*** is a common platform that allows all these interfaces to have a unified understanding of how the data is modeled and consumed. ***REMOVED*** delivers a targeted set of the features commonly needed for creating apps, flows, and more within Teams. For scenarios where an organization may require additional capabilities, more granular control for security and governance, or capacity beyond the approximately 1 million rows a ***REMOVED*** environment can contain, ***REMOVED*** can be upgraded to ***REMOVED*** Pro. 

The table below outlines the differences between ***REMOVED*** tables and ***REMOVED*** Pro entities: 

|Data feature  |***REMOVED***  |***REMOVED*** Pro  |
|---------|---------|---------|
|Basic data types     |  Yes       |  Yes       |
|Advanced data types​ (customer, multiple transaction currencies)      |  No       |  Yes       |
|Common Data Model    |  No       |  Yes       |
|Relational storage      | Yes       |  Yes       |
|Non-relational​ storage     |  No       |  Yes       |
|Managed data lake​      |  No       | Yes        |
|File and image support     | Yes        |  Yes       |
|Find, filter, sort     |   Yes      |  Yes       |
|Advanced and relevance search​      |   No      | Yes        |
|Mobile offline     |  No       |  Yes       |

Also note that most of the standard tables that are provided with a ***REMOVED*** Pro environment will not be present as part of ***REMOVED***.

## Key terminology changes

Some terminology has changed between ***REMOVED*** Pro and ***REMOVED*** to make it easier for a broader audience. The table below provides a mapping between ***REMOVED*** Pro and ***REMOVED***:


|***REMOVED***  |***REMOVED*** Pro  |
|---------|---------|
|Table, Tables     | Entity, entities        |
|Column, columns     |  Field, fields <br /> attribute, attributes       |

This article uses the terms *field* and *column* interchangeably. We will continue working to fully align the ***REMOVED*** experience to be consistent with the terms *table* and *column*. 

Most of the processes for creating and managing tables in ***REMOVED*** are the same as creating and managing entities in ***REMOVED*** Pro. Where applicable, these articles about ***REMOVED*** link you to the ***REMOVED*** Pro documentation that provides more detail.  

### See also
[Create a table](create-table.md)