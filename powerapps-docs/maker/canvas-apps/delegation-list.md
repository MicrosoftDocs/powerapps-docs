---
title: Delegable data sources in canvas apps | Microsoft Docs
description: List of all supported delegable data sources in canvas apps
author: lancedMicrosoft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: anneta
ms.date: 08/15/2017
ms.author: lanced
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Delegable data sources in canvas apps
As the [Understand delegation](delegation-overview.md) article outlines in detail, delegation is where PowerApps will delegate the processing of data to the data source rather than moving data to the canvas app for processing locally.

Delegation is supported for tabular data sources only. This list identifies tabular data sources and whether they support delegation, with details in the next section.

* Common Data Service (CDS) for Apps - **Yes**
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

Familiarize yourself with the [Understand delegation](delegation-overview.md) article.

## List of data sources and supported delegation
This list of data sources and delegable functions and predicates will be updated periodically to reflect the current status of delegation support in PowerApps.

### Top-level delegable functions

| &nbsp; | CDS for Apps | SharePoint | SQL Server | Dynamics 365 | Salesforce |
| --- | --- | --- | --- | --- | --- |
| Average |Yes<sup>2</sup> |No |Yes |No |No |
| Filter |Yes |Yes |Yes |Yes |Yes |
| LookUp |Yes |Yes |Yes |Yes |Yes |
| Max |Yes<sup>2</sup> |No |Yes |No |No |
| Min |Yes<sup>2</sup> |No |Yes |No |No |
| Search |Yes<sup>1</sup> |No |Yes |Yes |Yes |
| Sort |Yes |Yes |Yes |Yes |Yes |
| SortByColumns |Yes |Yes |Yes |Yes |Yes |
| Sum |Yes<sup>2</sup> |No |Yes |No |No |

<sup>1</sup> For string fields only.<br>
<sup>2</sup> **See note below**. The aggregate functions are limited to a collection of 50,000 records. If needed, use the [**Filter**](functions/function-filter-lookup.md) function to select 50,000 records from a larger set before using the aggregate function.

> [!NOTE]
> Aggregate functions for CDS for Apps are supported only with the new version of the connector. Depending on the version of PowerApps that you're using, enable this connector with either this Preview switch:<br>
> ![Preview switch for Relational data, option sets, and other new features for CDS](media/delegation-list/cdsv2-preview-switch.png)<br>
> or this Experimental switch:<br>
> ![Preview switch for Relational data, option sets, and other new features for CDS](media/delegation-list/cdsv2-experimental-switch.png)<br>
> To find both switches, open the **File menu**, and then select **App settings** > **Advanced settings**.

### Filter and LookUp delegable predicates

| &nbsp; | CDS for Apps | SharePoint | SQL Server | Dynamics 365 | Salesforce |
| --- | --- | --- | --- | --- | --- |
| Not |Yes |No |Yes |Yes |Yes |
| IsBlank |No |No |Yes |Yes |No |
| TrimEnds |No |No |Yes |No |No |
| Len |No |No |Yes |No |No |
| +, - |No |No |Yes |No |No |
| <, <=, =, <>, >, >= |Yes |Yes<sup>3</sup> |Yes |Yes |Yes |
| And (&&), Or (&#124;&#124;), Not (!) |Yes<sup>4</sup> |Yes (except Not(!)) |Yes |Yes |Yes |
| in |No |No |Yes |No |Yes |
| StartsWith |No |Yes |No |No |No |

<sup>3</sup> For numeric columns, all operators can be delegated. For ID columns, only the '=' can be delegated. Date columns can't be delegated.<br/>
<sup>4</sup> For operators only. And/Or/Not functions aren't delegated.
