<properties
    pageTitle="Delegable data sources | Microsoft PowerApps"
    description="List of all supported delegable data sources"
    services=""
    suite="powerapps"
    documentationCenter="na"
    authors="archnair"
    manager="anneta"
    editor=""
    tags=""/>
<tags
    ms.service="powerapps"
    ms.devlang="na"
    ms.topic="article"
    ms.tgt_pltfrm="na"
    ms.workload="na"
    ms.date="10/30/2016"
    ms.author="archanan"/>

# Delegable data sources #
As outlined in detail in the [Understand delegation](delegation-overview.md) article, delegation is where PowerApps will delegate the processing of data to the data source rather than moving data to the app for processing locally.

Delegation is supported for tabular data sources only. Tabular data sources include Common Data Service, SharePoint, SQL, Dynamics CRM, Salesforce and Excel, with more tabular data sources being added continuously. Delegation support for Excel is coming soon.

This document lists the current state of supported delegation per data source.

**Prerequisites**

- Familiarize yourself with [Understand delegation](delegation-overview.md) article

## List of datasources and supported delegation ##
This list will be updated periodically to reflect the current status of delegation support in PowerApps.

### Top Level Delegable Functions ###

|               | Common Data Service              | SharePoint | SQL | DynamicsCRM | Salesforce |
|---------------|----------------------------------|------------|-----|-------------|------------|
| Filter        | Yes                              | Yes        | Yes | Yes         | Yes        |
| Sort          | Yes                              | Yes        | Yes | Yes         | Yes        |
| SortByColumns | Yes                              | Yes        | Yes | Yes         | Yes        |
| Search        | Yes<sup>1</sup>                  | No         | Yes | Yes         | No         |
| LookUp        | Yes                              | Yes        | Yes | Yes         | No         |

<sup>1</sup>For String fields only

### Filter and LookUp Delegable Predicates ###

|                            | Common Data Service                              | SharePoint | SQL | DynamicsCRM | Salesforce |
|----------------------------|--------------------------------------------------|------------|-----|-------------|------------|
| Not                        | Yes                                              | No         | Yes | Yes         | Yes        |
| IsBlank                    | No                                               | No         | Yes | Yes         | Yes        |
| TrimEnds                   | No                                               | No         | Yes | No          | No         |
| Len (length)               | No                                               | No         | Yes | No          | No         |
| Now                        | No                                               | No         | Yes | No          | No         |
| Add                        | No                                               | No         | Yes | No          | No         |
| Sub                        | No                                               | No         | Yes | No          | No         |
| <, <=, =, <>, >, >=        | Yes                                              | Yes        | Yes | Yes         | Yes        |
| And (&&), Or (&#124;&#124;), Not (!) | Yes<sup>2</sup>                        | Yes        | Yes | Yes         | Yes        |
| In                         | No                                               | No         | Yes | No          | No         |

<sup>2</sup>For operators only. AND/OR function not delegated.
