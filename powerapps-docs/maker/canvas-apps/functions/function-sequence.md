---
title: Sequence function | Microsoft Docs
description: Reference information, including syntax and an example, for the Sequence function in Power Apps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 07/17/2020
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Sequence function in Power Apps
Generate a table of sequential numbers.

## Description
The **Sequence** function generates a table of sequential numbers, such as 1, 2, 3, 4.

Use **Sequence** with the **ForAll** function to iterate 

> [!Note]
> The **Sequence** function is limited to 50,000 records.

## Syntax
**Sequence**( *Records* [, *Start* [, *Step* ] ] )

* *Records* – Required. The number of records to create.
* *Start* – Optional.  The number to start the sequence with.  Default is 1.
* *Step* – Optional.  The increment for each successive number.  *Step* can be negative to count down from the *Start*.  Default is 1.

## Example

| Formula | Description | Result |
| --- | --- | --- |
