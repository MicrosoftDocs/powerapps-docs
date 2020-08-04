---
title: Dataflex vs Dataflex Pro | Microsoft Docs
description: Explains the differences between Dataflex and Dataflex Pro.
author: NHelgren
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 08/17/2020
ms.author: nhelgren
ms.reviewer: matp
---

# How are Dataflex and Dataflex Pro different?

Applications within a Team have access to a Microsoft Dataflex environment.  Dataflex is a common platform that allows all these interfaces to have a unified understanding of how the data is modeled and consumed. Dataflex delivers a targeted set of the features commonly needed for creating apps, flows, and more within Teams. If your organization requires additional capabilities, such as more granular control for security and governance, or capacity beyond the approximately 1 million rows a Dataflex environment can contain, Dataflex can be upgraded to Dataflex Pro.

The table below outlines the differences between Dataflex table and Dataflex Pro entity features:

|Feature  |Dataflex  |Dataflex Pro  |
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

Also note that most of the standard tables that are provided with a Dataflex Pro environment will not be present as part of Dataflex.

## Key terminology changes

Some terminology has changed between Dataflex Pro and Dataflex to make it easier for a broader audience. The table below provides a mapping between Dataflex Pro and Dataflex:


|Dataflex  |Dataflex Pro  |
|---------|---------|
|Table, Tables     | Entity, entities        |
|Column, columns     |  Field, fields <br /> attribute, attributes       |

Most of the processes for creating and managing tables in Dataflex are the same as creating and managing entities in Dataflex Pro. Where applicable, these articles about Dataflex link you to the Dataflex Pro documentation that provide more detail.  

### See also
[Create a table](create-table.md)