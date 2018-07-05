---
title: Delegable data sources | Microsoft Docs
description: List of all supported delegable data sources
documentationcenter: na
author: archnair
manager: kfile
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: conceptual
ms.component: canvas
ms.date: 08/15/2017
ms.author: archanan

---
# Delegable data sources
As outlined in detail in the [Understand delegation](delegation-overview.md) article, delegation is where PowerApps will delegate the processing of data to the data source rather than moving data to the app for processing locally.

Delegation is supported for tabular data sources only. This list identifies tabular data sources and whether they support delegation, with details in the next section.

* Common Data Service - **Yes**
* SharePoint - **Yes**
* SQL Server - **Yes**
* Dynamics 365 - **Yes**
* Salesforce - **Yes**
* Dynamics 365 for Operations - Not yet
* Dynamics 365 for Financials - Not yet
* Dynamics NAV - Not yet
* Google Sheets - Not yet

More tabular data sources and delegation support for them are being added continuously.

This document lists the current state of supported delegation per data source.

## Prerequisites

* Familiarize yourself with the [Understand delegation](delegation-overview.md) article

## List of data sources and supported delegation
This list of data sources and delegable functions and predicates will be updated periodically to reflect the current status of delegation support in PowerApps.

### Top-level delegable functions

| &nbsp; | Common Data Service | SharePoint | SQL Server | Dynamics 365 | Salesforce |
| --- | --- | --- | --- | --- | --- |
| Average |No |No |Yes |No |No |
| Filter |Yes |Yes |Yes |Yes |Yes |
| LookUp |Yes |Yes |Yes |Yes |Yes |
| Max |No |No |Yes |No |No |
| Min |No |No |Yes |No |No |
| Search |Yes<sup>1</sup> |No |Yes |Yes |Yes |
| Sort |Yes |Yes |Yes |Yes |Yes |
| SortByColumns |Yes |Yes |Yes |Yes |Yes |
| Sum |No |No |Yes |No |No |

<sup>1</sup>For string fields only

### Filter and LookUp delegable predicates

| &nbsp; | Common Data Service | SharePoint | SQL Server | Dynamics 365 | Salesforce |
| --- | --- | --- | --- | --- | --- |
| Not |Yes |No |Yes |Yes |Yes |
| IsBlank |No |No |Yes |Yes |No |
| TrimEnds |No |No |Yes |No |No |
| Len |No |No |Yes |No |No |
| +, - |No |No |Yes |No |No |
| <, <=, =, <>, >, >= |Yes |Yes (only =) |Yes |Yes |Yes |
| And (&&), Or (&#124;&#124;), Not (!) |Yes<sup>2</sup> |Yes (except Not(!)) |Yes |Yes |Yes |
| in |No |No |Yes |No |Yes |
| StartsWith |No |Yes |No |No |No |

<sup>2</sup>For operators only. And/Or/Not function not delegated.
