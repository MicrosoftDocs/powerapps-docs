---
title: Project Oakdale vs Common Data Service | Microsoft Docs
description: Explains the differences between Project Oakdale and Common Data Service.
author: NHelgren
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 09/11/2020
ms.author: nhelgren
ms.reviewer: matp
---

# How are Project Oakdale and Common Data Service different?

[!INCLUDE [cc-beta-prerelease-disclaimer.md](../includes/cc-beta-prerelease-disclaimer.md)]

Applications within a Team have access to a Project Oakdale environment.  Project Oakdale is a common platform that allows all these interfaces to have a unified understanding of how the data is modeled and consumed. Project Oakdale delivers a targeted set of the features commonly needed for creating apps, flows, and more within Teams. If your organization requires additional capabilities, such as more granular control for security and governance, or capacity beyond the approximately 1 million rows a Project Oakdale environment can contain, Project Oakdale can be upgraded to Common Data Service.

## Entity features
This table describes the differences between Project Oakdale table and Common Data Service entity features:

|Feature  |Project Oakdale  |Common Data Service  |
|---------|---------|---------|
|Basic data types     |  Yes       |  Yes       |
|Advanced data types​ (customer, multiple transaction currencies)      |  No       |  Yes       |
|Common Data Model    |  No       |  Yes       |
|Relational storage      | Yes       |  Yes       |
|Non-relational​ storage (logs)   |  No       |  Yes       |
|Managed data lake​      |  No       | Yes        |
|File and image support     | Yes        |  Yes       |
|Find, filter, sort     |   Yes      |  Yes       |
|Advanced and relevance search​      |   No      | Yes        |
|Mobile offline     |  No       |  Yes       |

Also note that most of the standard tables that are provided with a Common Data Service environment will not be present as part of Project Oakdale.

## Business intelligence and professional developer features

This table describes the differences between Project Oakdale and Common Data Service business intelligence and professional developer features.


|Area  |Feature  |Project Oakdale  |Common Data Service  |
|---------|---------|---------|---------|
|Business intelligence     |  Data Visualization   |  Yes    |  Yes   |
|      |   Paginated Reports (SSRS)    |  No    |  Yes     |
|Professional developer     | API access       |  No     |  Yes     |
|      |  Plugins       |   No      |  Yes       |


## Key terminology changes

Some terminology has changed between Common Data Service and Project Oakdale to make it easier for a broader audience. The table below provides a mapping between Common Data Service and Project Oakdale:


|Project Oakdale  |Common Data Service  |
|---------|---------|
|Table, Tables     | Entity, entities        |
|Column, columns     |  Field, fields <br /> attribute, attributes       |

Most of the processes for creating and managing tables in Project Oakdale are the same as creating and managing entities in Common Data Service. Where applicable, these articles about Project Oakdale link you to the Common Data Service documentation that provide more detail.  

### See also
[Create a table](create-table.md)