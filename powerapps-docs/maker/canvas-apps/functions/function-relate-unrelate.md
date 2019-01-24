---
title: Relate and Unrelate functions | Microsoft Docs
description: Reference information, including syntax and an example, for the Relate and Unrelate functions in PowerApps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: anneta
ms.date: 01/22/2019
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Relate and Unrelate functions in PowerApps
Link and unlink records of two entities that have a One-to-Many or Many-to-Many relationship. 

## Description
The **Relate** function links two records through a One-to-Many or Many-to-Many relationship in the Common Data Service for Apps.  The **Unrelate** function reverses the process and removes the link.

For Many-to-Many relationships a hidden join table is maintained by the system that links the records.  There is no direct access to this join table - it can only be read through a One-to-Many projection and set through the **Relate** and **Unrelate** functions.  There are no foreign keys on either of the two related entities.

For One-to-Many relationships there will be a foreign key field on the Many entity that points to a record of the One entity.  **Relate** will set this field to point to a specific record of the One entity while **Unrelate** will set this field to *blank*.  If the field is already set when **Relate** is called, the existing link will be lost in favor of the new link.

These functions never create or delete a record.  They only link or unlink two records that already exist.

## Syntax
**Relate**( *Entity1RelatedTable*, *Entity2Record* )

* *Entity1RelatedTable* - Required. The string of text to remove spaces from.
* *Entity2Record* - Required. The string of text to remove spaces from.

**Unrelate**( *Entity1RelatedTable*, *Entity2Record* )

* *Entity1RelatedTable* - Required. The string of text to remove spaces from.
* *Entity2Record* - Required. The string of text to remove spaces from.

## Examples

### One-to-Many



